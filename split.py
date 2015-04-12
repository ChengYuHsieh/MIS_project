import sys

def main(lamda):
	# f = open('output1.txt','r')
	f = open('Random1.txt','r')
	index = 1
	dij = list()
	demand_coor = list()
	supply_coor = list()
	returnitem = [demand_coor,supply_coor] # the return item of the function, has three element, 1. demand_coor 2, supply_coor 3. hi
	for line in f:
		if index ==1:
			m = int(line)
		elif index ==2:
			n = int(line)
		elif index==3:
			hi = line
			returnitem.append(hi) # append hi to the coor list
		elif index>3 and index <=3+m:
			demand_coor.append(line)
		elif index ==4+m:
			fj = line
		elif index >4+m and index <= 4+m+n:
			supply_coor.append(line)
		elif index >= 5+m+n:
			dij.append(line)
		index+=1
		
	
	dij = [item.split() for item in dij]
	
	dij_splt = zip(*dij)
	fj_splt = fj.split()
	f.close()

	for j in range(n):
		fname = 'split_'+str(j+1)+'.dat'
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
	return returnitem
if __name__=="__main__":
	main()