import sys
import numpy as np
import random
def main(m,n):
	# m = int(sys.argv[1]) # number of demand
	# n = int(sys.argv[2]) # number of supplier
	# lamda = int(sys.argv[3]) #value of lamda
	# iteration = int(sys.argv[4])
	Xi = list()
	Yi = list()
	Z = 0
	for i in range(n):
		fname = 'sub_sol_'+str(i+1)+'.txt'
		f = open(fname, 'r')
		index = 1
		subY=list()
		for line in f:
			if index==1:
				Z +=float(line.split()[len(line.split())-1])
			if index==5:
				Xi.append(int(line.split()[2]))
			if index>=8 and index<8+m:
				subY.append(int(line.split()[1]))
			index +=1
		Yi.append(subY)
		
	subgrad = np.array([1]*m)-np.array([sum(i) for i in zip(*Yi)])
	print 'objective Z: '+ str(Z)	
	print 'Xi: '+str(Xi)
	print 'Yi: '+str(Yi)
	print 'grad'+str(subgrad)
	# new_lamda = lamda + (5/iteration)*subgrad
	# print 'lamda'+str(new_lamda)
	return [Xi,Yi,Z,subgrad]



if __name__ == "__main__":
	main()	