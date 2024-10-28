import torch
import torch.distributed as dist
from torch.utils.data import DataLoader,DistributedSampler
from torch.nn.parallel import DistributedDataParallel as DDP
import torch.nn as nn

import tarfile
from PIL import Image
import  numpy as np

with tarfile.open('D:\\yzbx\\picture\\005600.tar','r') as tar:
    file_names = tar.getnames()
    jpg_files = [name for name in file_names if name.lower().endswith('jpg')]
    image_arrays = []

    for file_name in jpg_files:
        with tar.extractfile(file_name) as img_file:
            with Image.open(img_file) as image:
                image = image.convert('RGB')
                image_array = np.array(image)
                image_arrays.append(image_array)





# 定义一个简单的模型
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(10, 1)

    def forward(self, x):
        return self.linear(x)
    
dataset = image_arrays

#初始化进程
dist.init_process_group(backend='nccl')

#根据进程划分数据集
sampler = DistributedSampler(dataset,num_replicas=dist.get_world_size())
rank = dist.get_rank()
data_loader = DataLoader(dataset,batch_size=16,sampler=sampler)

#包装模型进行分布式推理
model = SimpleModel()
model.to(dist.get_rank())
model= DDP(model,device_ids=[dist.get_rank()])


#推理
results = []
for data in  data_loader:
    outputs = model(data)
    results.extend(outputs)

#收集结果到rank 0进程
if dist.get_rank() == 0 :
    gathered_results = [None]*dist.get_world_size()
    dist.gather(results,gathered_results,dst=0)

else:
    dist.gather(results,None)


