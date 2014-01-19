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

	testing_data = data.pop(row)
	training_data = data

	counter = 0

	headers = ['Title', 'FullDescription', 'LocationRaw', 'LocationNormalized', 'ContractType', 'ContractTime', 'Company', 'Category', 'SalaryRaw', 'SalaryNormalized', 'SourceName']

	while testing_size/original_size < 0.2 and training_size/original_size > 0.8:

		print 'testing_size/original_size: '  + str(float(testing_size)/original_size)
		print 'training_size/original_size: ' + str(float(training_size)/original_size) 


		counter += 1

		row = random.randint(0, len(training_data) - 1)

		print 'row: ' + str(row)
		print 'count: ' + str(len(training_data))

		testing_data.append(training_data.pop(row))

		testing_size = float(len(testing_data))
		training_size = float(len(training_data))

		print 'testing_size: ' + str(len(testing_data))
		print 'training_size: ' + str(len(training_data))
		print ''

	return [pd.DataFame(training_data, columns=header), pd.DataFrame(testing_data, columns=headers)]

split_data = parse(data)

print split_data