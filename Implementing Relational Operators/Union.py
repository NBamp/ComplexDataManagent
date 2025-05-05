#Nikos Babalis,4430

import sys
import csv

class Union:

	def __init__(self):
		pass


	def calc_union(self,file_1,file_2):

		global data
		line_1 = file_1.readline()
		line_2 = file_2.readline()
		data = []
		

		while True:



			if(line_1==""):   #line_1 == empty and line_2 not
				
				while(line_2!=""):
					newline2 = line_2
					data.extend([[line_2[:2],line_2[3:5]]])
					line_2 = self.new_line(file_2,newline2)
				break		
				
			elif(line_2==""): #line_2 == empty and line_1 not
 
				while(line_1!=""):
					newline1 = line_1
					line_1 = self.new_line(file_1,newline1)
					data.extend([[line_2[:2],line_2[3:5]]])
				break

			elif(line_1[0]==line_2[0]):  # Case having the first letter of attribute equal.


				if(line_1[1]<line_2[1]):
					data.extend([[line_1[:2],line_1[3:5]]])
					while True:
						line_1 = self.new_line(file_1,line_1)
						if(line_1=="" or line_1[0]!=line_2[0] or line_1[1]>=line_2[1]):
							break
						else:
							data.extend([[line_1[:2],line_1[3:5]]])



					if(line_1==line_2): #If  there is a match def equal is called
						self.equal(line_1,line_2)
						line_1 = self.new_line(file_1,line_1)
						line_2 = self.new_line(file_2,line_2)

				elif(line_1[1]>line_2[1]):
					data.extend([[line_2[:2],line_2[3:5]]])
					while True:
						newline2 = line_2
						line_2 = self.new_line(file_2,newline2)
						if(line_2=="" or line_2[0]!=line_1[0] or line_2[1]>=line_1[1]):
							break
						else:
							data.extend([[line_2[:2],line_2[3:5]]])

					if(line_1==line_2): #If  there is a match def equal is called
						self.equal(line_1,line_2)
						line_1 = self.new_line(file_1,line_1)
						line_2 = self.new_line(file_2,line_2)
						

				elif(line_1[3:5]<line_2[3:5]):

					data.extend([[line_1[:2],line_1[3:5]]])
					while True:
						line_1 = self.new_line(file_1,line_1)
						if(line_1=="" or line_1[:2]!=line_2[:2] or line_1[3:5]>=line_2[3:5]):
							break
						else:
							data.extend([[line_1[:2],line_1[3:5]]])


				elif(line_1[3:5]>line_2[3:5]):
					data.extend([[line_2[:2],line_2[3:5]]])
					while True:
						line_2 = self.new_line(file_2,line_2)
						if(line_2=="" or line_1[:2]!=line_2[:2] or line_2[3:5]>=line_1[3:5]):
							break
						else:
							data.extend([[line_2[:2],line_2[3:5]]])

				else:
					self.equal(line_1,line_2)
					line_1 = self.new_line(file_1,line_1)
					line_2 = self.new_line(file_2,line_2)
					

			elif(line_1[0]<line_2[0]):
				data.extend([[line_1[:2],line_1[3:5]]])
				while True:
					line_1 = self.new_line(file_1,line_1)
					if(line_1=="" or line_1[0]>=line_2[0]):
						break
					else: 
						data.extend([[line_1[:2],line_1[3:5]]])

			elif(line_1[0]>line_2[0]):
				data.extend([[line_2[:2],line_2[3:5]]])
				while True:
					line_2 = self.new_line(file_2,line_2)
					if(line_2=="" or line_2[0]>=line_1[0]):
						break
					else:
						data.extend([[line_2[:2],line_2[3:5]]])

			data.sort()




	def new_line(self,file,line):  #In order to avoid duplicate rows from each table

		newline = file.readline()
		while(newline==line):
			newline = file.readline()
		return newline

	


	def equal(self,line_1,line_2):

		if(line_1==line_2):
			l = [line_1[:2],line_1[3:5]]
			data.extend([l])
			l=[]












if __name__ == '__main__':
	f1 = sys.argv[1]
	f2 = sys.argv[2]
	with open(f1,'r') as file_1, open(f2,'r') as file_2, open("RunionS.tsv", mode='w', newline='') as file_3:
		Union().calc_union(file_1,file_2)
		writer=csv.writer(file_3,delimiter='\t')
		writer.writerows(data)

			
