def main():
    t = int(input())
    ans = []

    for i in range(t):
        num = int(input())
        line = list(map(int, input().split()))
        max_xor = -10**19
        for x in range(len(line)):
            for y in range(x + 1, len(line)):
                xor = line[x] ^ line[y]
                if xor >= max_xor:
                    max_xor = xor
        ans.append(max_xor)

    for i in ans:
        print(i)


if __name__ == '__main__':
    main()
