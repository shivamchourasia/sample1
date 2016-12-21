import sys
try:
#	count=0
	m=[]
	s=[]
	s1=[]
	m=sys.argv[1]
	p=m[-1]
	l1=int(m.index(p))
	#cmdargs=str(sys.argv)
#	print("////")
	if "+" in m:
	#	print("]]]]]]")
		l=int(m.index("+"))
	#	print("{{{{{{")
		for i in range(0,l):
	#		print("lll")
			s.append(m[i])
	#	print(s)
		n=''.join(s)
	#	print("ppp")
		var1=int(n)
	#	print("oooooo")
		for k in range(l+1,len(m)):
			s1.append(m[k])
	#	print(s1)
		n1=''.join(s1)
		var2=int(n1)	
		print(var1+var2)
	elif '-' in m:
	#	print("]]]]]]")
		l=int(m.index("-"))
	#	print("{{{{{{")
		for i in range(0,l):
	#		print("lll")
			s.append(m[i])
	#	print(s)
		n=''.join(s)
	#	print("ppp")
		var1=int(n)
	#	print("oooooo")
		for k in range(l+1,len(m)):
			s1.append(m[k])
	#	print(s1)
		n1=''.join(s1)
		var2=int(n1)	
		print(var1-var2)
	elif '*' in m:
	#	print("]]]]]]")
		l=int(m.index("*"))
	#	print("{{{{{{")
		for i in range(0,l):
	#		print("lll")
			s.append(m[i])
	#	print(s)
		n=''.join(s)
	#	print("ppp")
		var1=int(n)
	#	print("oooooo")
		for k in range(l+1,len(m)):
			s1.append(m[k])
	#	print(s1)
		n1=''.join(s1)
		var2=int(n1)	
		print(var1*var2)
	elif '/' in m:
	#	print("]]]]]]")
		l=int(m.index("/"))
	#	print("{{{{{{")
		for i in range(0,l):
	#		print("lll")
			s.append(m[i])
	#	print(s)
		n=''.join(s)
	#	print("ppp")
		var1=int(n)
	#	print("oooooo")
		for k in range(l+1,len(m)):
			s1.append(m[k])
	#	print(s1)
		n1=''.join(s1)
		var2=int(n1)	
		print(var1/var2)
	else:
		raise ValueError	
except ArithmeticError:
	print("wrong calculation",sys.exc_info()[0])
except ValueError :
	print("invalid input",sys.exc_info()[0])
