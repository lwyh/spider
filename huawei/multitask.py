"""
多线程任务处理


"""
from multiprocessing import Pool
from tqdm import tqdm
import os
import time


def run_multi_thread(func, list_data, num_thread=0, max_chunksize=1000):
    if num_thread == 0:
        num_thread = max(1, os.cpu_count() // 2)

    # set max_chunksize for better tqdm output
    chunk_size = min(max_chunksize, max(1, len(list_data) // num_thread))

    with Pool(num_thread) as p:
        list_result = list(tqdm(p.imap(func, list_data, chunksize=chunk_size), total=len(list_data), desc=f'threads: {num_thread}, chunksize: {chunk_size}'))

    return list_result

def my_func(i):
    time.sleep(0.01)
    return i*2
def test_func():
    list_data = [i for i in range(1000)]
    result = run_multi_thread(my_func, list_data, num_thread=10, max_chunksize=100)


if __name__=="__main__":
    test_func()