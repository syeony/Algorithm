# 아래 블로그 보고 dp이해
# https://assb.tistory.com/entry/%EB%B0%B1%EC%A4%80-11726%EB%B2%88-2xn-%ED%83%80%EC%9D%BC%EB%A7%81
# 깃허브 데스크탑 테스트

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1001

dp[1] = 1
dp[2] = 2

for i in range(3,1001):
    dp[i] = (dp[i-1]+dp[i-2])%10007

print(dp[n])