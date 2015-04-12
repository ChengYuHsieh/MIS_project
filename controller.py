#!usr/bin/python
import sys
import numpy as np
import generator
import split
import submod
import merge

def lancal(ret,anv):
	mm=anv[0]
	nn=anv[1]
	hh=anv[2]
	ff=anv[3]
	dd=anv[4]
	ll=ret[0]
	xx=ret[2]
	yy=ret[3]
	retval=0
	for i in range(mm):
		for j in range(nn):
			retval+=float(hh[i])*float(dd[j][i])*float(yy[j][i])
	for j in range(nn):
		retval+=float(ff[j])*float(xx[j])
	instance = np.array([1.0]*mm)
	for i in range(mm):
		for j in range(nn):
			instance[i]-=float(yy[j][i])
		retval+=ll[i]*instance[i]
	return retval

def main():
	num = 1
	m = int(raw_input("The number of demand:"))
	n = int(raw_input("The number of facility:"))
	hbar = int(raw_input("Quantity Limit H-bar:"))
	dbar = int(raw_input("Distance Matrix D-bar:"))
	fbar = int(raw_input("Fix Cost Limit F-bar:"))
	
	# run random to generate random nums
	generator.main(num,m,n,hbar,dbar,fbar)
	
	prelamda = np.array([100]*m)	#init lamda
	while True:		
		# split the random nums and generate j subdata files
		coor = split.main(prelamda)	#three element: 1. demand_coor 2, supply_coor 3. hi
		# solve each submodel and save the ampl solution 
		submod.main(n)
		# merge the sols
		returnitem = merge.main(m,n)	#returnitem = [Xi,Yi,Z,subgrad]
		
		
		
		

	# output graph txt
	# f = open('graph.txt','w')
	# f.write(str(dbar)+'\n')
	# f.write(str(m)+'\n')
	# for item in coor[0]:
	# 	f.write(item)
	# f.write(str(n)+'\n')
	# for item in coor[1]:
	# 	f.write(item)
	# f.write(coor[2])
	# Xj = ' '.join(returnitem[2].split())
	# f.write(Xj+'\n')
	# for i in range(len(returnitem[2])):
	# 	if i == len(returnitem[2])-1:
	# 		f.write(str(returnitem[2][i])+'\n')
	# 	else:
	# 		f.write(str(returnitem[2][i])+' ')
	# for line in zip(*returnitem[3]):
	# 	for i in range(len(line)):
	# 		if i == len(line)-1:
	# 			f.write(str(line[i])+'\n')
	# 		else:
	# 			f.write(str(line[i])+' ')

	
	
				

if __name__=="__main__":
	main()