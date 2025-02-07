"""
第一行输入是格子的总数量
第二行输入是每个格子的分数
第三行是每次跳的最大步长
求最终跳到终点获得的最大分数

"""
def tiaogezi():
    N=int(input())
    score = list(map(int,input().split()))
    k=int(input())
    def dfs_biggest_score(score,k,N,start,scores,visited,scores_dict,path): 
        path.append(start)
        scores += score[start] 
        print("start,N",start,N)
        if(start==N-1):
            scores_dict[tuple(path)]=scores
            scores=0
            return scores_dict
        steps=[ele for ele in range(1,k+1)]
        print("steps",steps)
        visited.add(start)
        for step in steps:
            start2=start+step
            if(start2 not in visited and start2<N):
                new_path=path.copy()
                new_visited=visited.copy()   
                scores_dict = dfs_biggest_score(score,k,N,start2,scores,new_visited,scores_dict,new_path)
        visited.remove(start)
        path.pop()
        scores -= score[start] 
        return scores_dict

    scores_dict = dfs_biggest_score(score,k,N,0,0,set(),dict(),[])
    print("scores_list",scores_dict)
    maxscore=max(scores_dict.values())
    print(maxscore,"maxscore")
    return maxscore 

if __name__=="__main__":
    tiaogezi()

