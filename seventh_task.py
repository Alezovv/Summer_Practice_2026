import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)

    t = int(next(it))

    for _ in range(t):
        n = int(next(it))
        s = [int(x) for x in next(it)]
        for k in range(n, 0, -1):
            possible = True
            flip = 0
            diff = [0] * (n + 1)
            for i in range(n):
                flip ^= diff[i]
                if s[i] ^ flip == 0:
                    if i + k > n:
                        possible = False
                        break
                    flip ^= 1
                    diff[i + k] ^= 1
            if possible:
                print(k)
                break


if __name__ == "__main__":
    solve()
