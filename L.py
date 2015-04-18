import sys
import os
import subprocess
import random
import time
from random import randint, sample
from math import sqrt, pow

#### para input can call rand_para
num = int(sys.argv[1])
m = int(sys.argv[2])
n = int(sys.argv[3])
hbar = int(sys.argv[4])
dbar = int(sys.argv[5])
fbar = int(sys.argv[6])
# num = int(raw_input("The number of instance:"))
# m = int(raw_input("The number of demand:"))
# n = int(raw_input("The number of facility:"))
# hbar = int(raw_input("Quantity Limit H-bar:"))
# dbar = int(raw_input("Distance Matrix D-bar:"))
# fbar = int(raw_input("Fix Cost Limit F-bar:"))
h = []
f = []
d = [[0 for x in range(n)] for x in range(m)]
l = [0.0 for i in range(m)]
old1_l = [0.0 for i in range(m)]
old2_l = [0.0 for i in range(m)]
max_l = [0.0 for i in range(m)]
x = [0 for i in range(n)]
old1_x = [0 for i in range(n)]
old2_x = [0 for i in range(n)]
max_x = [0 for i in range(n)]
y = [[0 for i in range(m)] for j in range(n)]
old1_y = [[0 for i in range(m)] for j in range(n)]
old2_y = [[0 for i in range(m)] for j in range(n)]
max_y = [[0 for i in range(m)] for j in range(n)]
value = [0 for i in range(n)]
lagrangian = 0
last1_lagrangian = 0
last2_lagrangian = 0
max_lagrangian = 0
sub = [0 for i in range(m)]
delta = 1.0
times = 1;
stop = 0;
count = 0;
t_start = 0
t_stop = 0

#Generate random instance
def output(filename):
	#Set random seed
	random.seed(1)
	#Generate demand quantity
	for i in range(m):
		h.append(randint(1, hbar))
	#Generate facility cost
	for i in range(n):
		f.append(randint(1, fbar))
	#Generate node and compute distance
	p = [[0 for x in range(dbar)] for x in range(dbar)]  

	samples = sample(xrange( 1, dbar**2 ), m + n)
	for i, r in enumerate(samples[:m]):
		p[r / dbar][r % dbar] = -(i + 1)
	for i, r in enumerate(samples[m:]):
		p[r / dbar][r % dbar] = i + 1
		for k in range(0, dbar**2):
			if p[k / dbar][k % dbar] < 0:
				ith = -p[k / dbar][k % dbar]
				jth = p[r / dbar][r % dbar]
				d[ith - 1][jth - 1] = float(sqrt(pow(k / dbar - r / dbar, 2) + pow(k % dbar - r % dbar, 2)))
	#Generate data file for IP or LP
	fw = open(filename + ".dat" , "wb")
	fw.write("set I :=")
	for i in range(m):
		fw.write(" " + str(i+1))
	fw.write(";\n")

	fw.write("set J :=")
	for i in range(n):
		fw.write(" " + str(i+1))
	fw.write(";\n")

	fw.write("param h :=")
	for i in range(m):
		fw.write("\n\t" + str(i+1) + " " + str(h[i]))
	fw.write(";\n")

	fw.write("param f :=")
	for i in range(n):
		fw.write("\n\t" + str(i+1) + " " + str(f[i]))
	fw.write(";\n")

	fw.write("param d :\n\t\t")
	for i in range(n):
		fw.write(str(i+1) + " ")
	fw.write(":=")

	for i, j in zip(range(1, 1+m), d):
		fw.write("\n\t" + str(i) + "\t")
		for k in j:
			fw.write(str(k) + " ")
	fw.write(";\n")
	fw.close()

#Generate ampl run script
def runfile(num):
	filename = "data" + "_" + str(num) + ".dat"
	f = open("LP.run",'wb')
	f.write("model UFL2.mod;")
	dataf = "data "+ filename + ";"
	f.write(dataf)
	f.write("option solver cplex;")
	f.write("solve;")
	f.write("display x;")
	f.write("display y;")

def lag(x, y):
	z = 0
	for i in range(m):
		for j in range(n):
			z = z + h[i] * y[j][i] * d[i][j]
	for j in range(n):
		z = z + f[j] * x[j]
	for i in range(m):
		p = 0
		for j in range(n):
			p = p + y[j][i]
		z = z + l[i] * (1 - p)
	return z

def heuristic(solution):
	for j in range(m):
			sub[j] = 1
			for k in range(n):
				sub[j] -= max_y[k][j]
	for i in range(m):
		if sub[i] > 0:
			min_cost = 100000
			temp_x = 0;
			for j in range(n):
				max_y[j][i] = 0
				if max_x[j] > 0:
					cost = h[i] * d[i][j]
					if cost < min_cost:
						temp_x = j
						min_cost = cost
			max_y[temp_x][i] = 1
			solution -= max_l[i]
			solution += min_cost
		elif sub[i] < 0:
			min_cost = 100000
			temp_x = 0;
			for j in range(n):
				if max_y[j][i] > 0:
					max_y[j][i] = 0
					solution += max_l[i]
					cost = h[i] * d[i][j]
					if cost < min_cost:
						temp_x = j
						min_cost = cost
			max_y[temp_x][i] = 1
			solution -= max_l[i]
			solution += min_cost
	return solution

for i in range(num):
	output("data" + "_" + str(i + 1))

for i in range(num):
	runfile(i + 1)
	ampl_cmd = "ampl <LP.run> ampl_sol1.txt"
	subprocess.call(ampl_cmd, shell = True)
	ampl_sol = open("ampl_sol1.txt", "r")
	index = 1
	line = ampl_sol.readline()
	ampl_sol.close()
	#Save LP objective value
	temp = line.find("objective")
	upperbound = float(line[temp + 10:len(line)])
	print("IP solution = " + str(upperbound))
	t_start = time.time()
	while True:
		#change lambda to data
		if times > 1:
			old2_x = old1_x
			old1_x = x
			old2_y = old1_y
			old1_y = y
		#Run n times AMPL
		for j in range(n):
			#Each demand
			total = 0.0
			total += f[j]
			for k in range(m):
				co_y = float(h[k] * d[k][j] - l[k])
				if co_y < 0:
					total += co_y
					y[j][k] = 1
				else:
					y[j][k] = 0
			if total < 0:
				x[j] = 1
				value[j] = total
			else:
				x[j] = 0
				value[j] = 0
				for k in range(m):
					y[j][k] = 0
					
		last2_lagrangian = last1_lagrangian
		last1_lagrangian = lagrangian
		lagrangian = 0
		for j in range(n):
			lagrangian = lagrangian + value[j]
		for j in range(m):
			lagrangian = lagrangian + l[j]
		print("lagrangian = " + str(lagrangian))
		#Record max lagrangian
		if lagrangian >= max_lagrangian:
			max_lagrangian = lagrangian
			for j in range(m):
				max_l[j] = l[j]
			for j in range(n):
				max_x[j] = x[j]
			for j in range(n):
				for k in range(m):
					max_y[j][k] = y[j][k]
		#compute subgradian
		for j in range(m):
			sub[j] = 1
			for k in range(n):
				sub[j] -= y[k][j]
		print("subgradian = " + str(sub))
		#print("lagrangian2 = " + str(lag(x, y)))

		#check the solution
		#If run too many times
		if times == 1000:
			t_stop = time.time()
			# solution = max_lagrangian
			# solution = heuristic(solution)
			print("Run time: " + str(t_stop - t_start))
			print("Run " + str(times) + " times.")
			# print("x = " + str(max_x))
			# print("y = " + str(max_y))
			print("lagrangian = " + str(max_lagrangian))
			# print("after adjust = " + str(solution))
			print("IP solution = " + str(upperbound))
			for j in range(m):
				check = 0
				for k in range(n):
					check = check + max_y[k][j]
				print("Demand" + str(j + 1) + " " + str(check))
			print(max_l)
			break
		elif times > 3:
			check = 0
			for j in range(m):
				if sub[j] != 0: 
					check = 1
			#If subgradian is all 0 
			if check == 0:
				t_stop = time.time()
				print("Run time: " + str(t_stop - t_start))
				print("Run " + str(times) + " times.")
				print("x = " + str(max_x))
				print("y = " + str(max_y))
				print("lagrangian = " + str(max_lagrangian))
				print("IP solution = " + str(upperbound))
				for j in range(m):
					check = 0
					for k in range(n):
						check += max_y[k][j]
					print("Demand" + str(j + 1) + " " + str(check))
				print(max_l)
				break
			#If lagrangian value start to become small
			elif lagrangian - last1_lagrangian < 0:
				if stop < 10:
					stop += 1
					for j in range(m):
						l[j] = old1_l[j]
					delta = 1.0
					last1_lagrangian = last1_lagrangian
				else:
					delta = delta / 2
			#If improvement is very small
			elif float(lagrangian - last1_lagrangian) / last1_lagrangian <= 0.0001:
				if count < 20:
					count = count + 1
					for j in range(m):
						old2_l[j] = old1_l[j]
						old1_l[j] = l[j]
					for j in range(m):
						l[j] = l[j] + sub[j] * delta
					times = times + 1
				else:
					count = 0
					for j in range(m):
						old2_l[j] = old1_l[j]
						old1_l[j] = l[j]
					for j in range(m):
						l[j] = l[j] + sub[j] * 3
					times = times + 1
			else:
				count = 0
				for j in range(m):
					old2_l[j] = old1_l[j]
					old1_l[j] = l[j]
				for j in range(m):
					l[j] = l[j] + sub[j] * delta
				times = times + 1
				if stop < 10:
					delta = delta + 1
		else :
			for j in range(m):
				old2_l[j] = old1_l[j]
				old1_l[j] = l[j]
			for j in range(m):
				l[j] = l[j] + sub[j] * delta
			times = times + 1
			if stop < 10:
				delta = delta + 1