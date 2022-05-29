import csv

name = {}  # This is the name directory used to hold ID-Name pair for the training images
filename = "mycsvfile.csv"
# it Reads the ID-Name pair from the CSV file
name_list = []
with open(filename, 'r') as data:
    for line in csv.DictReader(data):
        name[int(line['Id'])] = line['Name']


