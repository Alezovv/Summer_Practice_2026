def main():
    n, m, k = map(int, input().split())

    width = m + 1
    is_safe = bytearray([1] * ((n + 1) * width))

    for _ in range(k):
        x, y = map(int, input().split())
        is_safe[x * width + y] = 0

    MOD = 10**9 + 7

    dp = [0] * width
    dp[0] = 1

    for i in range(n + 1):
        row_offset = i * width
        for j in range(width):
            if is_safe[row_offset + j] == 0:
                dp[j] = 0
            elif j > 0:
                dp[j] = (dp[j] + dp[j - 1]) % MOD

    print(dp[m])


if __name__ == '__main__':
    main()
