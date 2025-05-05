#Nikos Bampalis , 4430
import heapq
import sys



_DIVISORS = [180.0 / 2 ** n for n in range(32)]

class R_Tree:



	def interleave_latlng(self, lat, lng):

	    if not isinstance(lat, float) or not isinstance(lng, float):
	        print('Usage: interleave_latlng(float, float)')
	        raise ValueError("Supplied arguments must be of type float!")

	    if (lng > 180):
	        x = (lng % 180) + 180.0
	    elif (lng < -180):
	        x = (-((-lng) % 180)) + 180.0
	    else:
	        x = lng + 180.0
	    if (lat > 90):
	        y = (lat % 90) + 90.0
	    elif (lat < -90):
	        y = (-((-lat) % 90)) + 90.0
	    else:
	        y = lat + 90.0

	    morton_code = ""
	    for dx in _DIVISORS:
	        digit = 0
	        if (y >= dx):
	            digit |= 2
	            y -= dx
	        if (x >= dx):
	            digit |= 1
	            x -= dx
	        morton_code += str(digit)

	    return morton_code



	def compute_MBR(self,file_1,file_2):

		line_2 = file_2.readline().split(',')
		global MBR_pair,z_curves
		MBR_pair = {}
		z_curves = {}

		while(line_2!=['']):

			heap_x = []
			heap_y = []
			mbr=[]
	
			for i in range(int(line_2[1]),int(line_2[2])+1): #In order to read between start and end from file offset for each polygon

				line_1 = file_1.readline().split(',')
				heap_x.append(float(line_1[0])) #Adding to list for x 
				heap_y.append(float(line_1[1]))	#Adding to list for y

			heapq.heapify(heap_x) #Transforming into heap
			heapq.heapify(heap_y) #Transforming into heap


			mbr =  heapq.nsmallest(1,heap_x) + heapq.nlargest(1,heap_x) +  heapq.nsmallest(1,heap_y) + heapq.nlargest(1,heap_y) #Computing MBR


			#Finding the center for computing z curve space filling
			x_median = (float(mbr[0]) + float(mbr[1]))/2 
			y_median = (float(mbr[2]) + float(mbr[3]))/2
			z_curves[int(line_2[0])] = R_Tree().interleave_latlng(y_median,x_median)

			MBR_pair[int(line_2[0])] = mbr

			
			line_2 = file_2.readline().split(',')
		z_curves = dict(sorted(z_curves.items(), key=lambda item:item[1]))  #In order to sort based on result of space filling curve z

		R_Tree().construct_RTree()
		

	def construct_RTree(self):

		global RTree
		RTree = [[]]

		level = 0 
		count = 0 

		for i in z_curves:   
			
			RTree[level].append([0 , count , [i, MBR_pair.get(i)]])  #leaves are constructed here
			count += 1


		while(len(RTree[level])!=1):


			help_list = []
			heap_x = []
			heap_y = []
			

			if(len(RTree[level]) % 20 == 0 ):  #Nodes will conducted properly because the the integer division gives modulo = zero

				for j in RTree[level]:
					
					#Adding elements from x and y axis
					heap_x.append(j[2][1][0]) 
					heap_x.append(j[2][1][1])
					heap_y.append(j[2][1][2])
					heap_y.append(j[2][1][3])

					if((RTree[level].index(j)+1) % 20 == 0):   #In order to group by 20 
						heapq.heapify(heap_x)
						heapq.heapify(heap_y)
						MBR = heapq.nsmallest(1,heap_x) + heapq.nlargest(1,heap_x) +  heapq.nsmallest(1,heap_y) + heapq.nlargest(1,heap_y)  #Computing MBR of node 
						help_list.append([1 , count , [count, MBR]])

						count += 1

						heap_x = []
						heap_y = []
						MBR = []
				
				RTree.extend([help_list])

			
				
			elif(len(RTree[level]) % 20 > 0 and len(RTree[level]) // 20 > 0): #In order to exclude the case for root 

				nodes = [[]] 
				nodes_help = []

				for j in RTree[level]:  #Pass the element in help list nodes with each level containing group of 20 and the remaining

					nodes_help.append(j)
					if((RTree[level].index(j)+1) % 20 == 0):

						nodes.extend([nodes_help])
						nodes_help=[]

					elif((RTree[level].index(j)+1) == len(RTree[level])):

						nodes.extend([nodes_help])
						nodes_help=[]



				nodes.pop(0)

				

				for i in range (0,len(nodes)): #Providing that each node has at least 8 elements 
					while(len(nodes[i]) < 8):
						nodes[i].append(nodes[i-1].pop())

				
				for node in nodes:
					for j in node:

						#Adding elements from x and y axis
						heap_x.append(j[2][1][0])
						heap_x.append(j[2][1][1])
						heap_y.append(j[2][1][2])
						heap_y.append(j[2][1][3])

						if(node.index(j)+1 == len(node)): #When we reach the end of length in node we compute MBR

							heapq.heapify(heap_x)
							heapq.heapify(heap_y)
							MBR = heapq.nsmallest(1,heap_x) + heapq.nlargest(1,heap_x) +  heapq.nsmallest(1,heap_y) + heapq.nlargest(1,heap_y)
							help_list.append([1 , count , [count, MBR]])

							count += 1

							heap_x = []
							heap_y = []
							MBR = []
				
				RTree.extend([help_list])

				

			else: #This case is enabled when len(Rtree[level]) // 20 == 0,which means that the root is about to be constructed) 
				
				for j in RTree[level]:
					
					heap_x.append(j[2][1][0])
					heap_x.append(j[2][1][1])
					heap_y.append(j[2][1][2])
					heap_y.append(j[2][1][3])

				heapq.heapify(heap_x)
				heapq.heapify(heap_y)
				MBR = heapq.nsmallest(1,heap_x) + heapq.nlargest(1,heap_x) +  heapq.nsmallest(1,heap_y) + heapq.nlargest(1,heap_y)
				help_list.append([1 , count , [count, MBR]])

				RTree.extend([help_list])



			level +=1

				

		#Printing sum of nodes for each level
		for i in range (0,len(RTree)):
			if(i == len(RTree)-1):
				print(str(len(RTree[i])) + " node at level "+str(i-1))
			elif(i != 0):
				print(str(len(RTree[i])) + " nodes at level "+str(i-1))

		
					

		



				


	


if __name__ == '__main__':
	with open(sys.argv[1],'r') as file_1 , open(sys.argv[2],'r') as file_2 , open("RTree.txt", mode='w' , newline='') as file_3:
		R_Tree().compute_MBR(file_1,file_2)
		for line in RTree:
			for element in line:
				file_3.write(f"{str(element)}\n")
			