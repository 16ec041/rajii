num1= int(input())
for i in range(2, num1):
	if num1 % i  == 0:
		print("no")
		break
else:
	print("yes")

