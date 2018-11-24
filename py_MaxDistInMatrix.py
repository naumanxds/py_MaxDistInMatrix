def recursion(powered, count):
	i = 0
	sqmatrix = []
	while(i < len(powered)):
		j = 0
		arr = []
		while(j < len(powered)):
			total = 0
			k = 0
			while(k < len(powered)):
				total += powered[i][k] * original[k][j]
				k+=1
			if(total > 0):
				arr.append(1)
			else:
				arr.append(0)
			j+=1
		sqmatrix.append(arr)
		i+=1
	print("count : \t" , count)
	print("original : \t" , original)
	print("powered : \t", powered)
	print("sqmatrix : \t", sqmatrix)
	print('----------------------------')

	if(powered == sqmatrix):
		print("maximum distance is : " , count)
	else:
		recursion(sqmatrix, count+1)


original = [[0,1,0,0,0,1,0,0,0,0],
			[0,0,1,0,0,0,0,0,0,0],
			[0,0,0,0,0,1,0,0,0,0],
			[0,0,0,0,1,0,0,0,0,0],
	 		[0,0,0,0,0,1,0,0,0,0],
	 		[0,0,0,0,0,0,1,0,1,0],
	 		[0,0,0,0,0,0,0,1,0,0],
	 		[0,0,0,0,0,0,0,0,1,0],
	 		[0,0,0,0,0,0,0,0,0,1],
			[0,0,0,0,0,0,1,0,0,0]]

loop = 0
while(loop < len(original)):
	loop2 = 0
	while(loop2 < len(original)):
		original[loop2][loop2] = 1
		loop2+=1	
	loop+=1

recursion(original, 1)