import sys
l=len(sys.argv)
if(l==2):
	try:
		m=[]
		s=[]
		s1=[]
		m=sys.argv[1]
		p=m[-1]
		l1=int(m.index(p))
		if "+" in m:
			l=int(m.index("+"))
			for i in range(0,l):
				s.append(m[i])
			n=''.join(s)
			var1=int(n)
			for k in range(l+1,len(m)):
				s1.append(m[k])
			n1=''.join(s1)
			var2=int(n1)	
			print(var1+var2)
		elif '-' in m:
			l=int(m.index("-"))
			for i in range(0,l):
				s.append(m[i])
			n=''.join(s)
			var1=int(n)
			for k in range(l+1,len(m)):
				s1.append(m[k])
			n1=''.join(s1)
			var2=int(n1)	
			print(var1-var2)
		elif '*' in m:
			l=int(m.index("*"))
			for i in range(0,l):
				s.append(m[i])
			n=''.join(s)
			var1=int(n)
			for k in range(l+1,len(m)):
				s1.append(m[k])
			n1=''.join(s1)
			var2=int(n1)	
			print(var1*var2)
		elif '/' in m:
			l=int(m.index("/"))
			for i in range(0,l):
				s.append(m[i])
			n=''.join(s)
			var1=int(n)
			for k in range(l+1,len(m)):
				s1.append(m[k])
			n1=''.join(s1)
			var2=int(n1)	
			print(var1/var2)
		else:
			raise ValueError	
	except ArithmeticError:
		print("wrong calculation",sys.exc_info()[0])
	except ValueError :
		print("invalid input",sys.exc_info()[0])
else:
	try:
		var1=int(str(sys.argv[1]))
		var=sys.argv[2]
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
