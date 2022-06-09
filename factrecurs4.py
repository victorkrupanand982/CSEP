def rec_fac(n):
	if n==1:
		return n
	else:
		return n*rec_fac(n-1)
num=int(input("enter the number"))
if(num<0):
	print("factorial does not exist for negative numbers")
elif num == 0:
	print("factorial of 0 is 1")
else:
	print("factorial of",num,"is",rec_fac(num))
