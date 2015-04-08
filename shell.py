#!usr/bin/python
from __future__ import print_function
import sys
import subprocess
# import generator

def runfile(num):
	filename = "data"+str(num)+".dat"
	f = open("ufl1.run",'w')
	f.write("model UFL1.mod;\n")
	dataf = "data "+filename+";"
	f.write(dataf+'\n')
	f.write('option solver "./ampl/cplex";\n')
	f.write("solve;\n")
	f.write("display X;\n")
	f.write("display Y;\n")

def main():
	#### para input can call rand_para
	num = raw_input("The number of instance:")
	m = raw_input("The number of demand:")
	n = raw_input("The number of facility:")
	hbar = raw_input("Quantity Limit H-bar:")
	dbar = raw_input("Distance Matrix D-bar:")
	fbar = raw_input("Fix Cost Limit F-bar:")
	
	rand_cmd = "./rand_para %s %s %s %s %s %s" % (num, m , n, hbar, dbar, fbar)
	
	subprocess.call("g++ rand_para.cpp -o rand_para ",shell=True)
	subprocess.call(rand_cmd,shell=True)

	for i in range(int(num)):

		#### call ampl_dat to create ampl data file using txt created in previous stage
		outputf = "output"+str(i+1)+".txt"
		dataf = "data"+str(i+1)+".dat"		
		dat_cmd = "python todat.py "
		runfile(i+1)
		subprocess.call(dat_cmd+outputf+" "+dataf,shell=True)
		#### call ampl to solve the LP and write back to ampl_sol.txt
		ampl_cmd = "./ampl/ampl < ufl1.run > ampl_sol.txt"
		subprocess.call(ampl_cmd,shell=True)
		ampl_sol = open('ampl_sol.txt','r')

		isX = False
		xi =[]
		isY = False
		yi=[]
		isMatrix = False
		isTrans =False
		for line in ampl_sol:
			if line ==";\n":
				isX = False
				isY = False
			if isX:
				xi.append(line.split()[1])
			if isY:
				yi.append(line.split()[2])
			if isMatrix:
				if jump:
					jump=False
				else:
					yi.append(line.split())

			if line =="X [*] :=\n":
				isX = True
			if line =="Y :=\n":
				isY = True
			if line =="Y [*,*]\n" or line == "Y [*,*] (tr)\n":
				isMatrix = True	
				jump = True
			if line == "Y [*,*] (tr)\n":				
				isTrans = True

		#### formatting the result
		para = open(outputf,'r')
		
		locationf = "location"+str(i+1)+".txt"
		result = open(locationf,'w')
		
		print(dbar, file=result)
		print(m,file=result)
		for i in range(2):
			para.readline()
		hi = para.readline()
		for i in range(int(m)):
			x = para.readline()
			result.write(x)
		print(n,file=result)
		para.readline()
		for i in range(int(n)):
			x = para.readline()
			result.write(x)
		result.write(hi)
		print(" ".join(xi),file=result)
		row =int(m)
		col =int(n)
		# print(yi,file=result)
		if isMatrix:
			if not isTrans:
				for line in yi:
					print(" ".join(line[1:]),file=result)
			else:
				print(yi,file = result)	
		else:
			for i in range(row):
					print(" ".join(yi[col*i:(i+1)*col]),file=result)
				

if __name__=="__main__":
	main()