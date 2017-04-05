#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print ('# enron people: ' + str(len(enron_data)))

print ('# features: ' + str(len(enron_data['METTS MARK'].keys())))

poi = list()
count = 0
for person in enron_data:
    if (enron_data[person]["poi"] == 1):
        poi.append(person)
        count = count + 1
        print person

print ('# POIs: ' + str(count))

names_file = open('../final_project/poi_names.txt', "r")
names_file.readline()
names_file.readline()
names = list()

for line in names_file:
    names.append(line)

for person in poi:
    
    print(person.split()[0].lower())
    
    
# print ('#names len ' + str(len(names)))
# print (names[1])

# for n in names:
#     print(n)