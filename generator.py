import time
import random
import sys


class p:
	
	def __init__(self,dbar=0):
		self.x = round(random.random() * dbar, 2)
		self.y = round(random.random() * dbar, 2)
	
	def dij(self,pj):
		return ((self.x-pj.x)**2 + (self.y-pj.y)**2)**0.5

	def str(self):
		return "({0}, {1})".format(self.x, self.y)
# Inputs are num,n,m,fbar,hbar,dbar.
# Outputs are n,m, m*hi, n*fj, m*n dij
def main(num,m,n,hbar,dbar,fbar):
# num = int(sys.argv[1])
# m = int(sys.argv[2])
# n = int(sys.argv[3])
# hbar = int(sys.argv[4])
# dbar = int(sys.argv[5])
# fbar = int(sys.argv[6])
	random.seed(1)

	for k in range(num): 

		hi = [round(random.random() * hbar, 2) for _ in range(m)]
		fj = [round(random.random() * fbar, 2) for _ in range(n)]

		demand = [p(dbar) for _ in range(m)]
		supply = [p(dbar) for _ in range(n)]

		d = []
		for i in range (m):
			dxj = []
			for j in range(n):
				dxj.append(float((round(demand[i].dij(supply[j]),2))))
			d.append(dxj)

		fname = 'Random' + str(k+1) + '.txt'
		fo = open(fname, "w")
		# fo.write(str(num)+'\n')
		fo.write(str(m)+'\n')
		fo.write(str(n)+'\n')
		for i in range(m):
			fo.write(str(hi[i])+' ')
		fo.write ('\n')
		for i in range(m):
			fo.write(str(demand[i].x) + ' ' + str(demand[i].y) + '\n')
		for i in range(n):
			fo.write(str(fj[i])+' ')
		fo.write ('\n')	
		for i in range(n):
			fo.write(str(supply[i].x) + ' ' + str(supply[i].y) + '\n')
		for i in range(m):
			for j in range(n):
				fo.write(str(d[i][j])+' ')
			fo.write('\n')

		# print ('num= ', num)
		# print ('m= ', m)
		# print ('n= ', n)
		# print ('hi= ')
		# for i in range (m):
		# 	print (hi[i])
		# print ('demand: ')
		# for i in range (m):
		# 	print (str(demand[i].x) + ' ' + str(demand[i].y))
		# print ('fj= ')
		# for i in range (n):
		# 	print (fj[i])		
		# print('supply: ')
		# for i in range(n):
		# 	print (str(supply[i].x) + ' ' + str(supply[i].y))
		# for i in range(m):
		# 	print (d[i])
		# print ('\n')

if __name__=="__main__":
	main()