import sys
import copy
initialmapreader = open(sys.argv[1],"r")
rulebookreader = open(sys.argv[2],"r")
gen_num = int(sys.argv[3])

initialmap = initialmapreader.readlines()
rulebook = rulebookreader.readlines()
initialmapreader.close()
rulebookreader.close()


rulebook[-1] = rulebook[-1]+"\n"
rulebookforfroblin = []
rulebookforempty = []
redundantrules = []
for a in rulebook:
	if a[0]==a[3]:
	    redundantrules.append(a)
	elif int(a[2])>8:
	    redundantrules.append(a)
	elif a[0] == ("*") and (a not in redundantrules):
	    rulebookforfroblin.append(a[:-1])
	elif a[0] == ("-") and (a not in redundantrules):
	    rulebookforempty.append(a[:-1])

def helpcomparison(a,b):
	if a[1]== "<":
		return b < int(a[2])
	elif a[1]==">":
		return b > int(a[2])
	elif a[1]== "=":
		return b == int(a[2])

def shaper(initialmap):
	for  i in range(len(initialmap)):
		if i != len(initialmap)-1:
			initialmap[i] = initialmap[i][:-1]
	return initialmap
def surrounder(initialmap):
	for i in range(len(initialmap)):
		initialmap[i] = "0"+ initialmap[i] +"0"
	
	initialmap.insert(0,(len(initialmap[0])+2)*"0")
	initialmap.insert(len(initialmap), (len(initialmap[0])+2)*"0")	
	return initialmap	

def finale(initialmap):
	k = 1
	while k <= gen_num:
		maptochange = copy.deepcopy(initialmap)
		for i in range(len(initialmap)):
			for j in range(len(initialmap[1])):
				if initialmap[i][j] == "*":
					for z in range(len(rulebookforfroblin)):	
						neighbourlist = initialmap[i-1][j-1]+ initialmap[i-1][j]+  initialmap[i-1][j+1]+ initialmap[i+1][j]+ initialmap[i+1][j-1]+  initialmap[i+1][j+1]+ initialmap[i][j+1]+ initialmap[i][j-1] 
						neighbourcount = neighbourlist.count("*")
						
						if helpcomparison(rulebookforfroblin[z], neighbourcount) :
							maptochange[i] = list(maptochange[i])
							maptochange[i][j]=rulebookforfroblin[z][3]
							maptochange[i]= "".join(maptochange[i])
						
				if initialmap[i][j] == "-":
					for z in range(len(rulebookforempty)):	
						neighbourlist = initialmap[i-1][j-1]+ initialmap[i-1][j]+  initialmap[i-1][j+1]+ initialmap[i+1][j]+ initialmap[i+1][j-1]+  initialmap[i][j+1]+ initialmap[i][j-1]+ initialmap[i+1][j+1]
						neighbourcount = neighbourlist.count("*")
						
						if helpcomparison(rulebookforempty[z], neighbourcount) :
							maptochange[i] = list(maptochange[i])
							maptochange[i][j]=rulebookforempty[z][3]
							maptochange[i]= "".join(maptochange[i])
		initialmap = maptochange
		k += 1
	return initialmap[1:-1]
	
def printmap(a):
	x = 0
	while x < len(a):
		a[x] = a[x][1:-1]
		x+=1
	return a
		

print "\n".join(printmap(finale(surrounder(shaper(initialmap)))))





