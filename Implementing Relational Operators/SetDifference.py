#Nikos Babalis , 4430
import csv
import sys


class SetDifference:

	

	def calc_set_difference(self,file_1,file_2):

		line_1 = file_1.readline()
		line_2 = file_2.readline()
		global data
		data = []
		
		while(line_1!="" and line_2!=""):


			if(line_1[:2]==line_2[:2]):

				if(line_1[3:5]<line_2[3:5]):
					data.extend([[line_1[:2],line_1[3:5]]])
					while True:
						newline1 = line_1
						line_1 = self.new_line(file_1,newline1)
						if(line_1[:2]!=line_2[:2] or line_1[3:5]>=line_2[3:5]):
							break
						else:
							data.extend([[line_1[:2],line_1[3:5]]])
							

				elif(line_1[3:5]>line_2[3:5]):
					newline2 = line_2
					while True:
						line_2 = self.new_line(file_2,newline2)
						if(line_1[:2]!=line_2[:2] or line_2[3:5]>=line_1[3:5]):
							break
					if(line_1!=line_2):
						data.extend([[line_1[:2],line_1[3:5]]])
						newline1 = line_1
						line_1 = self.new_line(file_1,newline1)
						
				else: 		
					newline1 = line_1
					newline2 = line_2
					line_1 = self.new_line(file_1,newline1)
					line_2 = self.new_line(file_2,newline2)

			elif(line_1[0]==line_2[0]):

				if(line_1[1]<line_2[1]):
					data.extend([[line_1[:2],line_1[3:5]]])
					while True:
						newline = line_1
						line_1 = self.new_line(file_1,newline)
						if(line_1[0]!=line_2[0] or line_1[1]>=line_2[1]):
							break
						else:
							data.extend([[line_1[:2],line_1[3:5]]])
														


				elif(line_1[1]>line_2[1]):
					newline = line_2
					while True:
						line_2 = self.new_line(file_2,newline)
						if(line_1[0]!=line_2[0] or line_2[1]>=line_1[1]):
							break
					if(line_2[1]>line_1[1]):
						data.extend([[line_1[:2],line_1[3:5]]])
						newline1 = line_1
						line_1 = self.new_line(file_1,newline1)



			elif(line_1[0]<line_2[0]):
				data.extend([[line_1[:2],line_1[3:5]]])
				newline = line_1
				while True:
					line_1 = self.new_line(file_1,newline)
					if(line_1[0]>=line_2[0]):
						break
					else:
						data.extend([[line_1[:2],line_1[3:5]]])
						

			elif(line_1[0]>line_2[0]):
				newline = line_2
				while True:
					line_2 = self.new_line(file_2,newline)
					if(line_2[0]>=line_1[0]):
						break
					else:
						data.extend([[line_2[:2],line_2[3:5]]])
						


						

		data.sort()
		
			


	def new_line(self,file,line):
		
		
		newline = file.readline()
		while(newline==line):
			newline = file.readline()
		return newline



if __name__ == '__main__':
	f1 = sys.argv[1]
	f2 = sys.argv[2]
	with open(f1,'r') as file_1, open(f2,'r') as file_2, open("RdifferenceS.tsv", mode='w', newline='') as file_3:
		SetDifference().calc_set_difference(file_1,file_2)
		writer=csv.writer(file_3,delimiter='\t')
		writer.writerows(data)

			