n1=int(input())
f=list(map(int,input().split()))
f.sort(reverse=True)
for i in range(0,n1):
  print(f[i],end="")
