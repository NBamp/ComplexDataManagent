#Nikos Bampalis , 4430
import heapq
import sys
import ast
from nodes import Node




class Range_Queries:


	
	
	def R_Tree_Construct(self,R_txt):

		global RTree
		RTree = []
		count = 0
		for i in R_txt:

			if(i[0]==0): #Leaf nodes
				RTree.append(Node([i[1],i[2]]))
				 

			else: #Non leaf nodes
				RTree.append(Node([i[1],i[2]]))
				
				
				while(len(RTree[len(RTree)-1].children)<20 and count<i[1]-1):
					
					RTree[len(RTree)-1].children.append(RTree[count])
					count += 1


				if(count == i[1] and count!= len(R_txt)-1):
					count -= 1
				
				

				while(len(RTree[len(RTree)-1].children)<8 and 	i[1]!=len(R_txt)-1):
					
					RTree[len(RTree)-1].children.append(RTree[len(RTree)-2].children.pop())

	
				


	def intersect(self,MBR,window,switch):

		count  = 0 


		if(not switch):
			points  = [[window[0],window[1]],[window[0],window[3]],[window[2],window[1]],[window[2],window[3]]]
		else:
			points  = [[window[0],window[2]],[window[0],window[3]],[window[1],window[2]],[window[1],window[3]]]


		for i in points:

			if(not switch):
				if(MBR[0]<=i[0]<=MBR[1] and MBR[2]<=i[1]<=MBR[3]):
					count += 1
			else:
				
				if(MBR[0]<=i[0]<=MBR[2] and MBR[1]<=i[1]<=MBR[3]):
					count += 1

		return count


	



		

	def range_query(self,root_id,window):

		if(len(RTree[root_id].children) == 0): 				#We have reached a leaf node

			if(Range_Queries().intersect(window,RTree[root_id].data[1][1],True)==4):

				result.append(RTree[root_id].data[1][0])
				
		else:

			if(Range_Queries().intersect(RTree[root_id].data[1][1],window,False)>=1):  #The MBR contains at least one point of the window 
				for i in RTree[root_id].children:
					Range_Queries().range_query(i.data[0],window)
				
			
		

		
		

		






if __name__ == '__main__':
	with open(sys.argv[1],'r') as file_1 , open(sys.argv[2], 'r') as file_2:

		
		global result
		result = []

		line_number = 0

		RTree_txt = file_1.readlines()

		for i in range(0,len(RTree_txt)):
			RTree_txt[i] = ast.literal_eval(RTree_txt[i])


		Range_Queries().R_Tree_Construct(RTree_txt)

		root_id = RTree[len(RTree)-1].data[0]

		window  = [float(i) for i in file_2.readline().split()]
		
		while(window):
			Range_Queries().range_query(root_id,window)
			print(str(line_number) + '('+str(len(result))+'): ',end='')
			for i in result:
				if(i == result[len(result)-1]):
					print(str(i)+'\n')
				else:
					print(i ,end=',')
			result = []
			window = [float(i) for i in file_2.readline().split()]
			line_number += 1
		
			
			
		