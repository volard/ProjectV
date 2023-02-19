from random import choice
import pandas as pd

# To generate xlsx
import openpyxl

# Read data
datasetPath = 'y_2021_csv.csv'
data = pd.read_csv('y_2021_csv.csv')

# Standard
standard = 120

# Columns names for convenience
column_push_ups = '1'
column_100m = '2'
column_3km = '3'

# Generate fake 2020 dataset
dataset_2020 = data.copy()

available_values_push_ups = dataset_2020[column_push_ups].copy().tolist()
# FIX broken push ups value < 34
available_values_push_ups = [34 if value < 34 else value for value in available_values_push_ups]

available_values_100m = dataset_2020[column_100m].copy().tolist()
available_values_3km = dataset_2020[column_3km].copy().tolist()


for current_index in range(dataset_2020[column_push_ups].count()):
    # Find new values
    current_push_ups = choice(available_values_push_ups)
    current_100m = choice(available_values_100m)
    current_3km = choice(available_values_3km)

    while current_push_ups + current_100m + current_3km <= standard:
        current_push_ups = choice(available_values_push_ups)
        current_100m = choice(available_values_100m)
        current_3km = choice(available_values_3km)

    # Save new values
    dataset_2020[column_push_ups][current_index] = current_push_ups
    dataset_2020[column_100m][current_index] = current_100m
    dataset_2020[column_3km][current_index] = current_3km

    # Forget used values
    available_values_push_ups.remove(current_push_ups)
    available_values_100m.remove(current_100m)
    available_values_3km.remove(current_3km)


# Generate fake 2022 dataset
dataset_2022 = data.copy()

available_values_push_ups = dataset_2022[column_push_ups].copy().tolist()
# FIX broken push ups value < 34
available_values_push_ups = [34 if value < 34 else value for value in available_values_push_ups]

available_values_100m = dataset_2022[column_100m].copy().tolist()
available_values_3km = dataset_2022[column_3km].copy().tolist()


for current_index in range(dataset_2022[column_push_ups].count()):
    # Find new values
    current_push_ups = choice(available_values_push_ups)
    current_100m = choice(available_values_100m)
    current_3km = choice(available_values_3km)

    while current_push_ups + current_100m + current_3km <= standard:
        current_push_ups = choice(available_values_push_ups)
        current_100m = choice(available_values_100m)
        current_3km = choice(available_values_3km)

    # Save new values
    dataset_2022[column_push_ups][current_index] = current_push_ups
    dataset_2022[column_100m][current_index] = current_100m
    dataset_2022[column_3km][current_index] = current_3km

    # Forget used values
    available_values_push_ups.remove(current_push_ups)
    available_values_100m.remove(current_100m)
    available_values_3km.remove(current_3km)

# Fancy output just for fun
print(dataset_2020.head(10))
print()
print(dataset_2022.head(10))

# Generate files
dataset_2020.to_excel("./data/dataset2020.xlsx")
dataset_2022.to_excel("./data/dataset2022.xlsx")
