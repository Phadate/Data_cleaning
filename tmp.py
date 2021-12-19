import pandas as pd
import numpy as np
import re

# Loading the files
data = pd.read_csv("persons.csv")
# print(data)

# printing the first value using map and apply
def lower_case(value):
    print("Here is the first value: ", value)
    return value.lower()

# data['first_name_min'] = data['first name'].apply(lower_case)

# del data['first_name_min']

VALID_COUNTRIES = ['France', 'Madagascar', 'Benin', 'Germany', 'Canada', 'USA']

def check_country(country):
    if country not in VALID_COUNTRIES:
        print(f'"{country}" is not a valid country. so we delete it')
        return np.nan
    return country
# data['country_key'] = data['country'].apply(check_country)

# To check email

def first(string):
    parts = string.split(',')
    first_part = parts[0]
    if len(parts) >= 2:
        print(f'There are several part in {parts}, so we can only keep {first_part}')
    return first_part

# data['email_key'] = data['email'].apply(first)
# height function

def convert_height(height):
    found = re.search('\d\.\d{2}m', height)
    if found == None:
        print(f'{height} is not in the right order, it will be ignored')
        return np.nan
    else:
        value = height[:-1] # i.e checking the last character if it is m or cm
        return float(value)

def check_fill(height, replacement):
    if pd.isnull(height):
        print(f'Imutation of mean by : {replacement}')
        return replacement
    return height
# date field
data['first_name_min'] = data['first name'].apply(lower_case)
del data['first_name_min']
data['country'] = data['country'].apply(check_country)
data['email'] = data['email'].apply(first)
data["Date_of_birth"] = pd.to_datetime(data['date_of_birth'], format='%d/%m/%Y', \
                                       errors="coerce")

data['height'] = [convert_height(t) for t in  data['height']]
data['height'] = [t if t <3 else np.nan for  t in data['height']]
mean_height = data['height'].mean()
data['height'] = [check_fill(t, mean_height) for t in data['height']]

print(data)
