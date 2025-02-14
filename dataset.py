#!/usr/bin/env python
# coding: utf-8

# # Viets Express File Handling in Python
# Welcome to the Jupyter Notebook for File Handling in Python. We want to generate a random dataset of names of residents residing in Viets tower and the information on their packages.

# ### Generating Fake Names, Room Numbers & Package Quantity.
# We start off by generating the fake names using the `Faker` library. We then used `.strip()` the separate the names into the first and second names. We then used the `random` library to generate random room numbers and random quantities of packages. Lastly, we use `initial_list` to pick a random initial.

# In[1]:


# importing and instantiating faker
from faker import Faker
import random

fake = Faker()

# creating a list for storing names
initials_list = ["MW", "CZ", "KS", "BM", "NS"]
initial_names = []
first_names = []
second_names = []
room_number = []
package_list = []

# adding fake names to the list 
for i in range(0, 50):
    room_num = random.randint(100, 1200)
    package_num = random.randint(1, 5)
    random_initial = random.choice(initials_list)
    room_number.append(room_num)
    fake_name = fake.name().split()
    first_names.append(fake_name[0])
    second_names.append(fake_name[1])
    package_list.append(package_num)
    initial_names.append(random_initial)


# checking the lengths of the lists
print("Number of Room Numbers: ", len(room_number))
print("Number of First Names: ", len(first_names))
print("Number of Last Names: ", len(second_names))
print("Number of Packages: ", len(package_list))
print("Number of Room Numbers: ",len(room_number))
print("Number of Initials: ", len(initial_names))


# ### Generating the Fake Dates
# We want to ensure that we have the necessary fake dates to add the dates at which the package arrived and when the packages were checked out. 

# In[2]:


from datetime import datetime, timedelta

# creating a list for date in and date out
date_in = []
date_out = []

# defining the range of dates to be picked from
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)
print("Start Date: ", start_date)
print("End Date: ", end_date)

# function for creating a random date
def date_generator(start, end):
    difference = end - start
    random_day = random.randint(0, difference.days)
    start_day = start + timedelta(days=random_day)
    end_day = (start + timedelta(days=random_day + 14))
    return start_day, end_day

# generating 50 random dates
for i in range(0, 50):
    start, end = date_generator(start_date, end_date)
    formatted_start = start.strftime("%Y-%m-%d")
    formatted_end = end.strftime("%Y-%m-%d")
    date_in.append(formatted_start)
    date_out.append(formatted_end)

# printing out the start and end dates
print("Number of Dates In: ", len(date_in))
print("Number of Dates Out: ", len(date_out))


# ### Converting Fake Data into a Pandas DataFrame
# Using the different lists of our fake data, we need to make a Pandas Data Frame and convert it into a full data set so that we can then convert it into a `.csv` file.

# In[4]:


# importing the pandas library
import pandas as pd


# converting the lists into a pandas data frame
packages_df = pd.DataFrame({
    'Room' : room_number,
    'First Name' : first_names,
    "Last Name" : second_names,
    "Date In" : date_in,
    "Packages" : package_list,
    "Date Out" : date_out,
    "Staff Initial" : initial_names
})

# viewing the data frame
packages_df.head(10)

# converting the data frame to csv
packages_df.to_csv("data/VietsData.txt", index=False)

# converting the data frame to excel sheet
packages_df.to_excel("data/VietsData.xlsx", index=False)

