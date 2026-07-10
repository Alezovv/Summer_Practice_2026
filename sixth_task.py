n = int(input())

c = [list(map(int, input().split())) for _ in range(n)]

size = 1 << n

dp = [[0] * n for _ in range(size)]

for i in range(n):
    dp[1 << i][i] = 1

for mask in range(size):
    for last in range(n):
        if dp[mask][last] == 0:
            continue

        for nxt in range(n):
            if (mask & (1 << nxt)) == 0 and c[last][nxt]:
                dp[mask | (1 << nxt)][nxt] += dp[mask][last]

full = size - 1

ans = 0
for last in range(n):
    ans += dp[full][last]

print(ans)
