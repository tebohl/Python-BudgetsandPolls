#create file paths across operatings systems
import os
#module for reading csv files
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#define dictionaries for values below with total votes starting at zero
votes = 0
candidates = {}
percentages = {}

#read csv file
with open(csvpath) as csvfile:

    #csv reader shows delimiter
    csvreader = csv.reader(csvfile, delimiter= ",")
    #read header row
    header = next(csvreader)

    #loop through rows
    for row in csvreader:
        #count rows (votes)
        votes += 1
        #store candidate name in variable
        candidate_name = row[2]
        
        #find candidate name and store in dictionary or add to votes
        if candidate_name in candidates.keys():
            candidates[candidate_name] +=1
            percentages[candidate_name] = candidates[candidate_name]/votes*100
        else:
            candidates[candidate_name] = 1
            percentages[candidate_name] = candidates[candidate_name]/votes*100
       
        #find max key       
        winner = max(candidates,key=candidates.get)

#create variable for text file with printed results
election_results = f"""
Election Results
----------------
Total Votes: {votes}
----------------
Charles Casper Stockham: {round(percentages["Charles Casper Stockham"], 3)}% ({candidates["Charles Casper Stockham"]})
Diana DeGette: {round(percentages["Diana DeGette"], 3)} % ({candidates["Diana DeGette"]})
Raymon Anthony Doane: {round(percentages["Raymon Anthony Doane"], 3)} % ({candidates["Raymon Anthony Doane"]})
Winner: {winner}
----------------
"""

#write new text file with results
print(election_results)

with open("poll_results.txt", "w") as new_file:
        new_file.write(election_results)
