inf = 10 ** 9


def lower_bound(a, x):
    l, r = 0, len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m
    return l


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    pref = [0]
    for x in arr:
        pref.append(pref[-1] + x)

    vals = sorted(set(pref))
    pos = {}
    for i in range(len(vals)):
        pos[vals[i]] = i

    size = 1
    while size < len(vals):
        size *= 2

    seg = [inf] * (2 * size)

    def update(v, x):
        v += size
        if x < seg[v]:
            seg[v] = x
        v //= 2
        while v:
            seg[v] = min(seg[v * 2], seg[v * 2 + 1])
            v //= 2

    def query(l, r):
        res = inf
        l += size
        r += size
        while l <= r:
            if l % 2 == 1:
                res = min(res, seg[l])
                l += 1
            if r % 2 == 0:
                res = min(res, seg[r])
                r -= 1
            l //= 2
            r //= 2
        return res

    dp = [inf] * (n + 1)
    dp[0] = 0
    update(pos[0], 0)

    for i in range(1, n + 1):
        ind = lower_bound(vals, pref[i] - k)
        if ind < len(vals):
            best = query(ind, len(vals) - 1)
            if best != inf:
                dp[i] = best + 1
        update(pos[pref[i]], dp[i])

    if dp[n] == inf:
        print(-1)
    else:
        print(dp[n])
