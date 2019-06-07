st1=[]
st2=[]
b=0
n=int(input())
item=input().split()
for i in item:
  st1.append(int(i))
for i in range(0,n-1):
  b=0
  for j in range(i+1,n):
    if st1[i]==st1[j]:
      b=b+1
      break
  if b>=1 and st1[i] not in st2:
    st2.append(st1[i])
z=len(st2)
if z==0:
  print("unique")
else:
  for i in st2:
    print(i,end=" ")
