import sys

def main(lamda):
	# f = open('output1.txt','r')
	f = open('Random1.txt','r')
	index = 1
	dij = list()
	demand_coor = list()
	supply_coor = list()
	coor = [demand_coor,supply_coor]
	for line in f:
		if index ==1:
			m = int(line)
		elif index ==2:
			n = int(line)
		elif index==3:
			hi = line
			coor.append(hi)
		elif index>3 and index <=3+m:
			# pass
			demand_coor.append(line)
		elif index ==4+m:
			fj = line
		elif index >4+m and index <= 4+m+n:
			# pass
			supply_coor.append(line)
		elif index >= 5+m+n:
			dij.append(line)
		index+=1
		
	
	dij = [item.split() for item in dij]
	
	dij_splt = zip(*dij)
	# print dij_splt
	fj_splt = fj.split()
	# print fj_splt
	f.close()
	# lamda = (0,0,0)
	# print 'split_lamda'+str(lamda)
	for j in range(n):
		fname = 'split_'+str(j+1)+'.dat'
		# f = open(fname,'w')
		# f.write(str(m)+'\n')
		# f.write('1\n')
		# f.write(hi)
		# f.write(fj_splt[j]+'\n')
		# for i in range(m):
		# 	f.write(dij_splt[j][i]+'\n')
		
		# for item in lamda:
		# 	f.write(str(item)+' ')
		# f.close()

		# openf = open(fname,'r')
		f = open(fname,'w')
		x = [i+1 for i in range(m)]
		x = ' '.join(str(p) for p in x)
		f.write('set I := '+x+';\n')
		f.write('param h :=\n')
		x = hi.split()
		for i in range(m):
			if i==m-1:
				f.write(str(i+1)+' '+ x[i]+';\n')
			else:
				f.write(str(i+1)+' '+ x[i]+'\n')		
		f.write('param f :='+str(fj_splt[j])+';\n')

		f.write('param l :=\n')
		for i in range(m):
			if i == m-1:
				f.write(str(i+1)+' '+str(lamda[i])+';\n')
			else:
				f.write(str(i+1)+' '+str(lamda[i])+'\n')
		f.write('param d :=\n')
		for i in range(m):
			if i ==m-1:
				f.write(str(i+1)+' '+dij_splt[j][i]+';\n')
			else:
				f.write(str(i+1)+' '+dij_splt[j][i]+'\n')
		f.close()
	return coor
if __name__=="__main__":
	main()