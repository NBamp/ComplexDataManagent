#Nikos Babalis , 4430
import csv
import sys

class Merge:
	
	def __init__(self):
		pass

	

	
	def calc_merge(self,file_1,file_2):
		
		line_1 = file_1.readline()
		line_2 = file_2.readline()
		global data  
		data = []
		buffer = []
		flag = False #When there is a match for merge,except the case we are looking to the buffer array,flag becomes true
		counter = -1
		same_line = False #True if the current line has the same value in the first attribute in comparison to the previous one
		while(line_1!=""):

			if(counter>=0 and line_1[:2]==buffer[counter][0][:2]  and same_line==True):   #Check if there is a match in buffer array

				index = counter #In order to store the initial value of counter

				while(counter>=0 and line_1[:2]==buffer[counter][0][:2]):   #Check if there are more than one matches in buffer array

					k = [line_1[:2],line_1[3:5]]
					k.extend([buffer[counter][1]])
					data.extend([k])
					k=[]	
					counter-=1

				

				counter = index #Replace the value of counter with the initial
				new_line = self.new_line(file_1,line_1) 
				if(new_line[:2]==line_1[:2]):
					same_line = True
				else:
					same_line = False
				line_1 = new_line
	


			elif(line_1[0]==line_2[0]):

				if(line_1[1]==line_2[1]):    #Equal Attributes
					flag = True
					buffer.extend([[line_2[:2],line_2[3:5]]])  #Store line from table S in buffer
					counter+=1
				
				elif(line_1[1]<line_2[1]):  #Attribute from R has lower value from attribute in S

					new_line = self.new_line(file_1,line_1)
					if(new_line[:2]==line_1[:2]):
						same_line = True
					else:
						same_line = False
					line_1 = new_line

				else:						#Attribute from S has lower value from attribute in R
					line_2 = self.new_line(file_2,line_2)
					


			elif(line_1[0]<line_2[0]):		#Attribute from R has lower value from attribute in S

				new_line = self.new_line(file_1,line_1)
				if(new_line[:2]==line_1[:2]):
					same_line = True
				else:
					same_line = False
				line_1 = new_line

			else:							#Attribute from S has lower value from attribute in R
				line_2 = self.new_line(file_2,line_2)

			if(flag):						#Pass the match in output
				data.extend([[line_1[:2],line_1[3:5],line_2[3:5]]])
				line_2 = self.new_line(file_2,line_2)
				flag = False

		print(len(buffer))
		data.sort()

	def new_line(self,file,line):  #In order to read a new line in comparison to the previous one

		newline = file.readline()
		while(newline==line):
			newline = file.readline()
		return newline
	



if __name__ == '__main__':
	f1 = sys.argv[1]
	f2 = sys.argv[2]
	with open(f1,'r') as file_1, open(f2,'r') as file_2, open("RjoinS.tsv", mode='w', newline='') as file_3:
		Merge().calc_merge(file_1,file_2)
		writer=csv.writer(file_3,delimiter='\t')
		writer.writerows(data)

			





	