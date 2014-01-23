import pandas as pd
import statsmodels.formula.api as sm
from patsy import dmatrices
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.cross_validation import cross_val_score
import math
import random
import csv


#################################################################################
# Initial parsing script
#################################################################################

print '#' * 75
print 'DATA PARSING SCRIPT INITIATED'
print '#' * 75


datafile = open('train.csv', 'r')
datareader = csv.reader(datafile)

print 'datareader created'

data = []
for row in datareader:
	data.append(row)

print len(data)

print 'data created'

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

training_set = split_data[0]
testing_set = split_data[1]

print '#' * 75
print 'DATA PARSING SCRIPT COMPLETE'
print '#' * 75

#################################################################################
# Model fitting script from statsmodel
#################################################################################


print '#' * 75
print 'MODEL FITTING SCRIPT INITIATED'
print '#' * 75

model = sm.ols("SalaryNormalized ~ LocationNormalized + Category + LocationNormalized:Category", training_set).fit()
model.summary()

#################################################################################
# Model fitting script from Sklearn, using dmatrices.
# Allows for LinearRegression model with regularization
#################################################################################

y, X = dmatrices('SalaryNormalized ~ LocationNormalized + Category + LocationNormalized:Category', data=training_set, return_type='dataframe')

model = LinearRegression()
model = model.fit(X,y)
model.score(X,y)

model = linear_model.Ridge(alpha = .5)
model.fit(X,y)

print model.coef_

model = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
model.fit(X,y)

print model.coef_
print model.alpha_

# http://scikit-learn.org/stable/modules/cross_validation.html



