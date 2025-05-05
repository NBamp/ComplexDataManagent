#Nikos Babalis , 4430
import csv
import sys

class Intersect:
	
	def __init__(self):
		pass

	def calc_intersect(self,file_1,file_2):

		line_1 = file_1.readline()
		line_2 = file_2.readline()
		global data
		data = []

		while(line_1!="" and line_2!=""):

	
			if(line_1==line_2):

				l = [line_1[:2],line_1[3:5]]
				data.extend([l])
				l=[]
				line_1 = self.new_line(file_1, line_1)
				line_2 = self.new_line(file_2, line_2)

			elif(line_1[0]==line_2[0]):
				
				
				if(line_1[1]<line_2[1]):

					line_1 = self.new_line(file_1, line_1)


				elif(line_1[1]>line_2[1]):	
					
					line_2 = self.new_line(file_2, line_2)


					
				elif(line_1[3:5]<line_2[3:5]):
					
					line_1 = self.new_line(file_1, line_1)
					
					

				elif(line_1[3:5]>line_2[3:5]):

					line_2 = self.new_line(file_2, line_2)
		
					


			elif(line_1[0]<line_2[0]):
				
				line_1 = self.new_line(file_1, line_1)
				
			
			elif(line_1[0]>line_2[0]):
				
				line_2 = self.new_line(file_2, line_2)
			
		
	def new_line(self,file,line):
		newline = file.readline()
		while(newline==line and newline!=""):
			newline = file.readline()
		return newline


if __name__ == '__main__':
	f1 = sys.argv[1]
	f2 = sys.argv[2]
	with open(f1,'r') as file_1, open(f2,'r') as file_2, open("RintersectionS.tsv", mode='w', newline='') as file_3:
		Intersect().calc_intersect(file_1,file_2)
		writer=csv.writer(file_3,delimiter='\t')
		writer.writerows(data)

			