try:
	var1=int(raw_input("enter the first value"))
	var=raw_input("enter the sign for the calculation")
	var2=int(raw_input("enter the second value"))
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
	print("wrong calculation")
except ValueError :
	print("invalid input")
