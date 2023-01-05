#Deliverables:
#Total number of votes cast
#complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")



with open(file_to_load) as election_data:    

    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    print(headers)

