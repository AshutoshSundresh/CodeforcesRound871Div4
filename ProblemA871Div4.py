n = int(input())

for i in range(n):
    s = input()
    count = 0
    for i in range(0, 10):
        if s[i] != "codeforces"[i]:
            count += 1
    print(count)
