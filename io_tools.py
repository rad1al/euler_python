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