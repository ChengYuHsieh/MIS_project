import sys

fo = open(sys.argv[1], "r")
fw = open(sys.argv[2], "wb")
index = 1
lines = fo.read().splitlines()
fo.close()
for line in lines:
	if index <= 2:
		if index == 1:
			fw.write("set I :=")
			col = int(line)
		if index == 2:
			fw.write("set J :=")
			row = int(line)
		for i in range(1, int(line)+1):
			fw.write(" "+str(i)),
		fw.write(";\n")
	elif index == 3 or index == 4+col:
		if index == 3:
			fw.write("param h :=")
		else:
			fw.write("param f :=")
		for indexh, h in enumerate((line.split(' '))[:-1]):
			fw.write("\n\t"+str(indexh+1)+" "+h)
		fw.write(";\n")	
	elif index >= 5+col+row:
		if index == 5+col+row:
			fw.write("param d :\n\t\t")
			for r in range(1, row+1):
				fw.write(str(r)+" ")
			fw.write(":=")
		fw.write("\n\t"+str(index-4-col-row)+"\t"+line+" ")

	index = index + 1
fw.write(";")
fw.close()