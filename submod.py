#!usr/bin/python
import sys
import subprocess

def runfile(num):
	filename = "split_"+str(num)+".dat"
	f = open("ufl1.run",'w')
	f.write("model submodel.mod;\n")
	dataf = "data "+filename+";"
	f.write(dataf+'\n')
	f.write('option solver "./ampl/cplex";\n')
	f.write("solve;\n")
	f.write("display X;\n")
	f.write("display Y;\n")

def main(n):
	# n = int(sys.argv[1])
	for i in range(n):
		outf = 'sub_sol_'+str(i+1)+'.txt'
		runfile(i+1)
		subprocess.call('./ampl/ampl < ufl1.run > '+outf,shell=True)

	
				

if __name__=="__main__":
	main()