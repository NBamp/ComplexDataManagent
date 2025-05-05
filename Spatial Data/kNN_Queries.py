
#Nikos Bampalis,4430
import heapq
import sys
import ast
import math
from nodes import Node


class kNN_Queries:



	def R_Tree_Construct(self,R_txt):

		global RTree
		RTree = []
		count = 0
		for i in R_txt:


			if(i[0]==0): #Leaf nodes
				RTree.append(Node([i[1],i[2]]))
				 

			else: #Non leaf nodes
				RTree.append(Node([i[1],i[2]]))
				
				
				while(len(RTree[len(RTree)-1].children)<20 and count<i[1]) :
					
					RTree[len(RTree)-1].children.append(RTree[count])
					count += 1
				
				
				if(count == i[1] and count!= len(R_txt)-1):

					count -= 1
				
			

				while(len(RTree[len(RTree)-1].children)<8 and i[1]!=len(R_txt)-1):
					
					RTree[len(RTree)-1].children.append(RTree[len(RTree)-2].children.pop())




	def  BF_NN_search(self,point,root_id,k):

		global result
		queue = []
		result = []

		for i in RTree[root_id].children:
			
			dist = kNN_Queries().distance(i.data[1][1],point)
			heapq.heappush(queue,(dist,i.data[0]))


		while(len(result)<k):
			result.append(kNN_Queries().get_next_BF_NN(point,queue))

		


	def get_next_BF_NN(self,point,queue):
		


		while(queue):

			n = heapq.heappop(queue)[1]
			if(len(RTree[n].children)>0):
				for i in RTree[n].children:
					dist = kNN_Queries().distance(i.data[1][1],point)
					heapq.heappush(queue,(dist,i.data[0]))
			else:
				return RTree[n].data[1][0]


	def distance(self,MBR,point):

		dx = max(abs(MBR[0] - point[0]),abs(MBR[1]-point[0]))
		dy = max(abs(MBR[2] - point[1]),abs(MBR[3]-point[1]))
		return math.sqrt(dx * dx + dy * dy)



if __name__ == '__main__':
	with open(sys.argv[1],'r') as file_1 , open(sys.argv[2], 'r') as file_2:

		k = int(sys.argv[3])

		RTree_txt = file_1.readlines()

		for i in range(0,len(RTree_txt)):
			RTree_txt[i] = ast.literal_eval(RTree_txt[i])

		line_number = 0

		kNN_Queries().R_Tree_Construct(RTree_txt)
	
		root_id = RTree[len(RTree)-1].data[0]
		point = [float(i) for i in file_2.readline().split()]
		while(point):
			kNN_Queries().BF_NN_search(point,root_id,k)
			print(str(line_number) + '('+str(len(result))+'): ',end='')
			for i in result:
				if(i == result[len(result)-1]):
					print(str(i)+'\n')
				else:
					print(i ,end=',')
			result = []
			point = [float(i) for i in file_2.readline().split()]
			
			line_number += 1
		

		

		
		

		
