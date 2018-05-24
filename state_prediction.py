#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
import warnings
import numpy as np
import re
from termcolor import colored
from sklearn import preprocessing
from sklearn.externals import joblib

# Disable warnings (data format warnings)
if not sys.warnoptions:
    warnings.simplefilter("ignore")

# FUNCTIONS

# Checks if an input is an integer and if true it checks if it is within
# two possible boundaries and if affirmative, it adds it to a dictionary
def check_input_boundary(input_text, lower_limit, higher_limit, dict, key):
    while True:
        try:
            num_input = input(input_text)
            if lower_limit <= num_input <= higher_limit:
                dict[key] = num_input
                break
            else:
                msg = "The input must be in the interval (" + str(lower_limit) + ", " + str(higher_limit) + ")"
                print colored(msg, "red")
        except (NameError, SyntaxError) as e:
           print colored("Please enter a valid number", "red")

# Checks if input is an integer
def check_input_number(input_text, dict, key):
    user_input = ''
    while user_input is not int:
        try:
            user_input = int(input(input_text))
            dict[key] = user_input
            break
        except (NameError, SyntaxError) as e:
            print colored("Please enter a valid number", "red")

def check_input_text(input_text, dict, key):
    while True:
        try:
            inp = raw_input(input_text)
            if re.match('[0-9]{2}:[0-9]{2}$', inp):
                dict[key] = inp
                break
            else:
                print colored("Please enter a valid hour", "red")
        except (NameError, SyntaxError) as e:
            print colored("Please enter a valid hour", "red")

# Prints the title of the application
def print_title():
    print "\n"
    print "----------------------------------------"
    print "|  BIPOLAR DISORDER CRISIS PREDICTION  |"
    print "----------------------------------------"
    print "Author: Axel Junestrand"
    print "License: Apache 2.0"
    print "\n"

def show_prediction(pred):
    msg = ''
    if pred == 'D':
        msg = colored("The patient could be tending towards a DEPRESSION episode", "yellow")
    elif pred == 'M':
        msg = colored("The patient could be tending towards a MANIA episode", "yellow")
    else:
        msg = colored("The patient is staying in a EUTHYMIC state", "cyan")
    return msg

# EXECUTION

print_title()
print "Please indicate each of the values gathered during the interview:"

# Get patient features
features = dict()

check_input_boundary("* Mood (-3 to 3)? ", -3, 3, features, "mood")
check_input_boundary("* Motivation (-3 to 3)? ", -3, 3, features, "motivation")
check_input_boundary("* Attention (0 to 4)? ", 0, 4, features, "attention")
check_input_boundary("* Irritability (0 to 4)? ", 0, 4, features, "irritability")
check_input_boundary("* Anxiety (0 to 4)? ", 0, 4, features, "anxiety")
check_input_boundary("* Sleep quality (0 to 4)? ", 0, 4, features, "sleep_quality")

check_input_number("* Number of cigarettes smoked? ", features, "nr_cigarettes")
check_input_number("* Amount of caffeine ingested? ", features, "caffeine")

check_input_text("* When did the patient wake up (hh:mm)? ", features, "wake_up")
check_input_text("* When did the patient go to bed (hh:mm)? ", features, "going_to_bed")

# Calculate amount of time the patient has been active
wake_up = int(features["wake_up"].replace(':',''))
going_to_bed = int(features["going_to_bed"].replace(':',''))

if going_to_bed < wake_up:
    going_to_bed += 2400

active_time = abs(wake_up - going_to_bed)

test = np.array([features['mood'], features['motivation'], features['attention'],
                features['irritability'], features['anxiety'], features['sleep_quality'],
                features['nr_cigarettes'], features['caffeine'], active_time])

test = test.reshape(1, -1)

rf = joblib.load("rf.pkl")

print "\n"
print show_prediction(rf.predict(test)[0])
print "\n"
