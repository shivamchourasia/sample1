import sys
import pickle
def filehandle(var):
	f=open("testing.txt","rb")
	lines=pickle.load(f)
	lines=lines.split("\n")
	dict={}
#	var=raw_input("enter a word ")
	print "input is "+var
	for line in lines:
		word=line.split(" ")
		dict[word[0]]=word[1:]
	
	if var in dict:
		print(dict[var])
	else:
		var1=raw_input("please enter the synonyms")
		dict[var]=var1
#	v1=dict[var]
		f=open("testing.txt","ab")
		pickle.dump("\n"+var+" "+":")
		pickle.dumps(str(dict[var]))
		print(var,":",dict[var])
		f.close
var1=1
	
while var1==1:
	var=raw_input("enter a word to find the synonyms or 'quit' to exit\t")
	if var!="quit":
		filehandle(var)
	else:
		sys.exit("you typed quit")
