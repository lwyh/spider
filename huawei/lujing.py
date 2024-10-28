"""
问题描述

K小姐所在公司举办了 Family Day 活动，邀请员工及其家属参观公司园区。将公司园区视为一个 n×mn×m 的矩形网格，起始位置在左上角，终点位置在右下角。家属参观园区时，只能向右或向下移动。园区中有些位置设有闸机，无法通行。请问，从起始位置到终点位置，一共有多少种不同的参观路径？
输入格式

第一行包含两个正整数 nn 和 mm，分别表示园区的行数和列数。 接下来 nn 行，每行包含 mm 个空格分隔的数字，数字为 00 表示该位置可以通行，数字为 11 表示该位置无法通行。

题解

本题可以使用动态规划的思想求解。设 dp[i][j]dp[i][j] 表示从起始位置到达位置 (i,j)(i,j) 的不同路径数量。对于每个位置 (i,j)(i,j)，如果该位置可以通行，那么到达该位置的路径数量等于到达其上方位置 (i−1,j)(i−1,j) 和左侧位置 (i,j−1)(i,j−1) 的路径数量之和。

初始条件：dp[0][0]=1dp[0][0]=1，表示起始位置的路径数量为 11。 状态转移方程：

    如果位置 (i,j)(i,j) 可以通行，即 grid[i][j]=0grid[i][j]=0，则 dp[i][j]=dp[i−1][j]+dp[i][j−1]dp[i][j]=dp[i−1][j]+dp[i][j−1]。
    如果位置 (i,j)(i,j) 无法通行，即 grid[i][j]=1grid[i][j]=1，则 dp[i][j]=0dp[i][j]=0。

最终答案为 dp[n−1][m−1]dp[n−1][m−1]，表示从起始位置到终点位置的不同路径数量。

时间复杂度：O(nm)O(nm)，需要遍历整个网格。 空间复杂度：O(nm)O(nm)，需要创建一个二维数组存储状态值。

"""

def uniquePaths(n, m, grid):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dp[i][j] =0
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
    return dp[n-1][m-1]

n,m = map(int,input().split())
grid = []
for _ in range(n):
    row = list(map(int,input().split()))
    grid.append(row)

result = uniquePaths(n, m, grid)
print(result)