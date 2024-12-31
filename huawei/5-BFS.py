"""
题目描述

LYA开发了一款智能驾驶系统,可以让汽车在 M×NM×N 的地图上从左上角(起点)开往右下角(终点)。地图上的每个位置都有一个数字,表示汽车经过该位置需要消耗的油量。地图上还有一些加油站,汽车经过加油站时可以加满油。

LYA想知道,汽车从起点出发,确保能够到达终点,初始时油箱里至少需要多少油量。

注意:

    汽车可以向上、下、左、右四个方向行驶。
    地图上的数字含义如下:
        −1−1:表示该位置是加油站,汽车经过时可以将油箱加满,油箱容量为 100100。
        00:表示该位置是障碍物,汽车无法通过。
        正整数:表示汽车经过该位置需要消耗的油量。
    如果无论初始油量多少,汽车都无法到达终点,则输出 −1。




"""

import heapq

def check(mid):
    dis = [[-1] * m for _ in range(n)]
    vis = [[False]* m for _ in range(n)]
    dis[0][0] = mid - grid[0][0]
    if grid[0][0] == -1:
        dis[0][0] = 100
    elif grid[0][0] == 0 or dis[0][0]<0:
        return False
    q = [(-dis[0][0], 0, 0)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while q:
        w, x, y = heapq.heappop(q)
        w= -w
        if vis[x][y]:
            continue
        vis[x][y] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <=nx<n and 0<=ny< m and grid[nx][ny] != 0 and not vis[nx][ny] and grid[nx][ny] <=w:
                if grid[nx][ny] == -1:
                    nw = 100
                else:
                    nw = w - grid[nx][ny]
                if nw > dis[nx][ny]:
                    dis[nx][ny] = nw
                    heapq.heappush(q, (-nw, nx, ny))
    return vis[n-1][m-1]
n,m = map(int, input().split(','))
grid = [list(map(int,input().split(','))) for _ in range(n)]

left,right = 0,100
ans = -1
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)