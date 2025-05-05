#Nikos Babalis , 4430
import csv
import sys


class GroubBy:


	def sort_merge(self,arr):

		if len(arr) <= 1:
			
			return arr
		
		mid = len(arr) // 2
		leftHalf = arr[:mid]
		rightHalf = arr[mid:]   


		sortedLeft = self.sort_merge(leftHalf)
		sortedRight = self.sort_merge(rightHalf)
      
		return self.merge(sortedLeft, sortedRight)

		
	
		
	def merge(self,left,right):

		result = []
		i = j = 0

		
		while i < len(left) and j < len(right):
			
			
			if(left[i][:2] < right[j][:2]):
				
				result.append(left[i])

				if(i+1<len(left) and left[i]==left[i+1]): #For avoiding duplicate
					i+=2
				else:
					i+=1

				

			
			elif(left[i][:2] > right[j][:2]):

				result.append(right[j])

				if(j+1<len(right) and right[j]==right[j+1]): #For avoiding duplicate
					j+=2
				else:
					j+=1
				


				
			elif(left[i][:2] == right[j][:2]):

				group = left[i][:2]
				sum_ = int(left[i][3:5]) + int(right[j][3:5])
				del left[i]
				del right[j]
				result.append(group+'\t'+str(sum_)+'\n')
				

			

		result.extend(left[i:])
		result.extend(right[j:])

	
		
		

		return result






if __name__ == '__main__':
	f1 = sys.argv[1]
	with open(f1,'r') as file_1,open("RgroubBy.tsv", mode='w', newline='') as file_2:
		file = file_1.readlines()
		res = GroubBy().sort_merge(file)
		writer=csv.writer(file_2,delimiter='\t')
		for line in res:
			line = line.split('\t')
			line[1] = line[1].strip('\n')
			writer.writerow([line[0],line[1]])
		

			