import pandas as pd
import statsmodels.formula.api as sm
import math
import random
import csv

print 'script started'

datafile = open('train.csv', 'r')
datareader = csv.reader(datafile)

print 'datareader created'

data = []
for row in datareader:
	data.append(row)

print len(data)

print 'data created'
# model = sm.ols(" SalaryNormalized ~ LocationNormalized + ContractTime + Category + LocationNormalized:Category", data).fit()
# model.summary()

def parse(data):

	print 'started parse'

	original_size = len(data)

	training_size = len(data)

	testing_size = 1

	row = random.randint(0, len(data)-1)

	row = data.pop(row)

	templist = []
	for item in row:
		templist.append(item)

	testing_data = []
	testing_data.append(list(templist))
	training_data = data

	counter = 0

	headers = ['ID', 'Title', 'FullDescription', 'LocationRaw', 'LocationNormalized', 'ContractType', 'ContractTime', 'Company', 'Category', 'SalaryRaw', 'SalaryNormalized', 'SourceName']

	while testing_size/original_size < 0.2 and training_size/original_size > 0.8:

		# print 'testing_size/original_size: '  + str(float(testing_size)/original_size)
		# print 'training_size/original_size: ' + str(float(training_size)/original_size) 


		counter += 1

		row = random.randint(0, len(training_data) - 1)

		# print 'row: ' + str(row)
		# print 'count: ' + str(len(training_data))

		row = training_data.pop(row)
		# print ''
		# print row
		# print ''
		templist = []


		for item in row:
			templist.append(item)

		testing_data.append(list(templist))

		testing_size = float(len(testing_data))
		training_size = float(len(training_data))

		# print 'testing_size: ' + str(len(testing_data))
		# print 'training_size: ' + str(len(training_data))
		# print ''

	training_data.pop(0)
	# testing_data.pop(0)

	# print testing_data[0]
	# print training_data[0]
	return [pd.DataFrame(training_data, columns=headers), pd.DataFrame(testing_data, columns=headers)]

split_data = parse(data)

print split_data[0]
print split_data[1]
