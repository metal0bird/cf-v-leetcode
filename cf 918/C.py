n = int(input())
for i in range(n):
    dummy = input()
    arr = list(map(int,input().split()))
    s = sum(arr)

    root = s**0.5
    if root.is_integer():
        print("YES")
    else:
        print("NO")