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
from __future__ import division
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Data points: ", len(enron_data)
print "Features number: ", len(enron_data["SKILLING JEFFREY K"])
print "POI number: ", sum(enron_data[name]["poi"] for name in enron_data)

#for name in enron_data:
#    if  enron_data[name]["poi"]:
#        print name, " - ", enron_data[name]["total_payments"]

print "Total value of the stock belonging to James Prentice: ", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Email messages Wesley Colwell to persons of interest: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Value of stock options exercised by Jeffrey K Skilling: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "Lay took: ", enron_data["LAY KENNETH L"]["total_payments"]
print "Skilling took: ", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Fastow took: ", enron_data["FASTOW ANDREW S"]["total_payments"]

print "Have quantified salary: ", sum(enron_data[name]["salary"] != 'NaN' for name in enron_data)
print "Have known email address: ", sum(enron_data[name]["email_address"] != 'NaN' for name in enron_data)

print "People have NaN in total payments: ", round(sum(enron_data[name]["total_payments"] == 'NaN' for name in enron_data) / len(enron_data), 3) * 100,"%"
print "POIs have NaN in total payments: ", round(sum(enron_data[name]["total_payments"] == 'NaN' and enron_data[name]["poi"] for name in enron_data) / len(enron_data), 3) * 100,"%"
print "People + 10 have NaN in total payments: ", sum(enron_data[name]["total_payments"] == 'NaN' for name in enron_data) + 10