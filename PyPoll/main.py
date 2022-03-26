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
        
        #find candidate name and store in dictionary or add to votes for exisitng key
        if candidate_name in candidates.keys():
            candidates[candidate_name] +=1
            percentages[candidate_name] = candidates[candidate_name]/votes*100
        else:
            candidates[candidate_name] = 1
            percentages[candidate_name] = candidates[candidate_name]/votes*100       
       
        #find max key       
        winner = max(candidates,key=candidates.get)

#print analysis to terminal
print("Election Results")
print("----------------")
print("Total Votes: " + str(votes))

#iterate through keys and values in dictionaries
for key,value in percentages.items():
    print(f' {key} : {round(value,3)}%')

for key,value in candidates.items():
    print(f"({value})")

print("-----------------")
print("Winner: " + str(winner))
print("-----------------")

#define variable for new text file with results
newline = "\n"
election_results = f"""
Election Results
----------------
Total Votes: {votes}
{newline.join(f"{key}: {(round(value,3))}%" for key,value in percentages.items())}
{newline.join(f"{value}" for value in candidates.items())}
----------------
Winner: {winner}
----------------
"""

#write new text file with results
with open("Analysis/poll_results.txt", "w") as new_file:
    new_file.write(election_results)
