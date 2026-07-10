import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    ptr = 1
    out = []

    for i in range(t):
        n = int(input_data[ptr])
        m = int(input_data[ptr + 1])
        k = int(input_data[ptr + 2])
        ptr += 3
        res = list(range(n, m, -1)) + list(range(1, m + 1))
        out.append(' '.join(map(str, res)))

    print('\n'.join(out))


if __name__ == '__main__':
    solve()
