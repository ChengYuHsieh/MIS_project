import sys
import numpy as np
import random
def main(m,n,lamda,iteration,stop):
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
	adj = 0
	for i in range(n):
		adj+= np.inner(np.array(Yi[i]),lamda)
	print 'objective Z:'+ str(Z)	

	if iteration==199:
		stop= True
		print Z
		print Xi
		print Yi
	print 'grad'+str(subgrad)
	new_lamda = lamda + (5/iteration)*subgrad
	print 'lamda'+str(new_lamda)
	return [new_lamda,stop,Xi,Yi]



if __name__ == "__main__":
	main()	