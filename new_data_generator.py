import random

import pandas as pd

# Read data
datasetPath = 'y_2021_csv.csv'
data = pd.read_csv('y_2021_csv.csv')

# Columns names for convenience
column_push_ups = '1'
column_100m = '2'
column_3km = '3'

# Generate fake 2020 dataset
dataset_2021 = data.copy()

for current in range(dataset_2021[column_push_ups].count()):
    dataset_2021[column_push_ups][current] = dataset_2021[column_push_ups][current] * random.randrange(1, 7)

for current in range(dataset_2021[column_100m].count()):
    dataset_2021[column_100m][current] = dataset_2021[column_100m][current] * random.randrange(1, 7)

for current in range(dataset_2021[column_3km].count()):
    dataset_2021[column_3km][current] = dataset_2021[column_3km][current] * random.randrange(1, 7)

# Generate fake 2022 dataset
dataset_2022 = data.copy()

for current in range(dataset_2022[column_push_ups].count()):
    dataset_2022[column_push_ups][current] = dataset_2022[column_push_ups][current] * random.randrange(1, 7)

for current in range(dataset_2022[column_100m].count()):
    dataset_2022[column_100m][current] = dataset_2022[column_100m][current] * random.randrange(1, 7)

for current in range(dataset_2022[column_3km].count()):
    dataset_2022[column_3km][current] = dataset_2022[column_3km][current] * random.randrange(1, 7)

print(dataset_2021.head(10))
print(dataset_2022.head(10))
