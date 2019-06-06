a=int(input(""))
b=list(input().split())
sum=0
for i in range(a):
  sum=sum+int(b[i])
d=len(b)
avg=sum//d
print(avg)
