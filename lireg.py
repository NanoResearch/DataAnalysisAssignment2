import pandas as pd
import statsmodels.formula.api as sm
import math
import random

data = pd.read_csv('train.csv')



model = sm.ols(" SalaryNormalized ~ LocationNormalized + ContractTime + Category + LocationNormalized:Category", data).fit()
model.summary()

def parse(data):

	original_size = len(data.index)

	training_size = len(data.index)

	testing_size = 1

	row = random.randint(1, len(data.index))

	testing_data = data.iloc[row]
	training_data = data.drop(row)

	while testing_size/original_size < 0.2 and training_size/original_size > 0.8:

		row = random.randint(1, len(training_data.index))

		testing_data.join(training_data.iloc[row])
		training_data = training_data.drop(row)

		testing_size = len(testing_data.index)
		training_size = len(training_data.index)

	end

	return [training_data, testing_data]

end