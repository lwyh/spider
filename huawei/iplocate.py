import re


def iplocate():
    in1= input()
    in2= input()
    arra1 = re.split(r'[=,;]', in1)
    arra2 = in2.split(',')
    #print(arra1,arra2)
    result_dict={}
    i=0
    counter=0
    def get_unique_key(city,counter):
        return f"{city}_{counter}"
    while i<len(arra1):
        city=arra1[i]
        unique_key = get_unique_key(city,counter)
        if city not in result_dict:
            result_dict[unique_key]=[]
        if i+1<len(arra1) and len(arra1[i+1].split('.'))==4:
            result_dict[unique_key].append(arra1[i+1])
            result_dict[unique_key].append(arra1[i+2])
            i+=1
        counter+=1
        i+=2
    print(result_dict)
    result_dict2={}
    for key,value in result_dict.items():
        if len(value)==2:
            print(key,value[0],value[1])
        
    def is_ip_in_range(target_ip,ip_start,ip_end):
        ip_start_arr=list(map(int,ip_start.split('.')))
        ip_end_arr=list(map(int,ip_end.split('.')))
        target_ip_arr=list(map(int,target_ip.split('.')))

        for target ,start,end in zip(target_ip_arr,ip_start_arr,ip_end_arr):
            if start<=target<=end:
                return True
            return False
    for i in range(len(arra2)):
        for key,value in result_dict.items():
            if len(value)==2:
                if is_ip_in_range(arra2[i],value[0],value[1]):
                    result_dict2[arra2[i]]=key[:5]
                    break
    out = ', '.join(str(value) for value in result_dict2.values())
    print(out)
    print(list(result_dict2.values()))
    print(*result_dict2.values())
        

    return out

if __name__ == '__main__':
    iplocate()

