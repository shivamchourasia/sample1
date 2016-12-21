import sys
try:
	#cmdargs=str(sys.argv)
	var1=int(str(sys.argv[1]))
	var=str(sys.argv[2])
	var2=int(str(sys.argv[3]))
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
