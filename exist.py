N,K=map(int,input().split())
N1=list(map(int,input().split()))
for i in range(len(N1)):
    if N1[i]==K:
        print("yes")
        break
else:
    print("no")
