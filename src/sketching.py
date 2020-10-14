stringdict = {}

alist = ['23','45','x','t5','af','5']
blist = []
elist = []
for i, thing in enumerate(alist):
	try:
		blist.append(float(thing))
	except:
		elist.append(i)

print(alist)
print(blist)
print(elist)


