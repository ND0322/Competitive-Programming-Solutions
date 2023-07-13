ans = 0
p = int(input())
s = int(input())

ans += 50 * p
ans -= 10 * s

if p > s:
    ans += 500

print(ans)
