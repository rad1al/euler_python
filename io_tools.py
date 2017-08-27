import csv

def read_data(filename, delim=','):
	with open(filename, 'rb') as inputfile:
		filereader = csv.reader(inputfile, delimiter=delim)
		data = list(filereader)
		if len(data[0]) == 1:
			data_list = [row[0] for row in data]
		else:
			data_list = data
		return data_list

# print read_data("data/PE99_base_exp.txt")

def write_data(filename, data):
	with open(filename, 'wb') as outputfile:
		outputwriter = csv.writer(outputfile, delimiter=',')
		if type(data[0]) != list:
			data = [[row] for row in data]
		for row in data:
			outputwriter.writerow(row)

# write_data("numbers.txt", [1,2,3,4,5])