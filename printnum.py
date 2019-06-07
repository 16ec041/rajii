N,K= map(int,input().split())
c = list(map(int,input().split()))
e=0
for i in c:
	if i==K:
		e+=1
print(e)
