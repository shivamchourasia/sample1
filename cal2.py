import sys
try:
	m=[]
	m=sys.argv[1]
	#cmdargs=str(sys.argv)
	var1=int(m[0])
	var=m[1]
	var2=int(m[2])
	if var=='+':
		print(var1+var2)
	elif var=='-':
		print(var1-var2)
	elif var=='*':
		print(var1*var2)
	elif var=='/':
		print(var1/var2)
	else:
		raise ValueError	
except ArithmeticError:
	print("wrong calculation",sys.exc_info()[0])
except ValueError :
	print("invalid input",sys.exc_info()[0])
