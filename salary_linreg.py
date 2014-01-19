import pandas as pd

training_set = pd.read_csv('train.csv')

print training_set
print training_set['Title']
print training_set['LocationRaw']
print training_set['LocationNormalized']  # Much better than locationraw, use this one
print training_set['ContractType']  # Good but a lot of null values
print training_set['ContractTime']  # Good but a lot of null values
print training_set['Company']  # Good, but a lot of null values
print training_set['Category']  # This one b/c it's standardized
print training_set['SourceName']  # This one b/c it's standardized


# Top prospects: LocationRaw, Company, Category, SourceName, 
# AND ContractType, looking for permanent