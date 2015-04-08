#!usr/bin/python
import sys
import numpy as np
import generator
import split
import submod
import merge

def main():
	num = 1
	m = int(raw_input("The number of demand:"))
	n = int(raw_input("The number of facility:"))
	hbar = int(raw_input("Quantity Limit H-bar:"))
	dbar = int(raw_input("Distance Matrix D-bar:"))
	fbar = int(raw_input("Fix Cost Limit F-bar:"))
	
	# run random to generate random nums
	generator.main(num,m,n,hbar,dbar,fbar)
	
	iteration = 1.0
	lamda = np.array([100]*m)	#init lamda
	stop = False
	while True:		
		# split the random nums and generate j subdata files
		coor = split.main(lamda)
		# solve each submodel and save the ampl solution 
		submod.main(n)
		# merge the sols and rewrite the lamda in datafiles
		returnitem = merge.main(m,n,lamda,iteration,stop)
		lamda = returnitem[0]
		iteration+=1
		if returnitem[1]:
			break

	# output graph txt
	f = open('graph.txt','w')
	f.write(str(dbar)+'\n')
	f.write(str(m)+'\n')
	for item in coor[0]:
		f.write(item)
	f.write(str(n)+'\n')
	for item in coor[1]:
		f.write(item)
	f.write(coor[2])
	# Xj = ' '.join(returnitem[2].split())
	# f.write(Xj+'\n')
	for i in range(len(returnitem[2])):
		if i == len(returnitem[2])-1:
			f.write(str(returnitem[2][i])+'\n')
		else:
			f.write(str(returnitem[2][i])+' ')
	for line in zip(*returnitem[3]):
		for i in range(len(line)):
			if i == len(line)-1:
				f.write(str(line[i])+'\n')
			else:
				f.write(str(line[i])+' ')

	
	
				

if __name__=="__main__":
	main()