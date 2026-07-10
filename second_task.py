s = input()
p = s + '$' + s[::-1]
m = len(p)
pi = [0] * m

for i in range(1, m):
    j = pi[i - 1]
    while j > 0 and p[i] != p[j]:
        j = pi[j - 1]
    if p[i] == p[j]:
        j += 1
    pi[i] = j

print(pi[-1])
