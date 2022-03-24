#create file paths across operatings systems
import os
#module for reading csv files
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#define empty lists for values below
total_votes = []
candidates = {"candidate_name": "votes"}
candidates = dict()


#read csv file
with open(csvpath) as csvfile:

    #csv reader shows delimiter
    csvreader = csv.reader(csvfile, delimiter= ",")
    #read header row
    header = next(csvreader)

    votes = 0
    for row in csvreader:
        #count rows (votes)
        votes += 1
        candidate_name = row[3]
        #find candidate name and store in list
    if candidate_name in candidates():
        candidates["votes" +1]
    else:
        candidates[row[3]: 1]


        

print("Election Results")
print("----------------")
print("Total Votes: " + str(votes))
print("----------------")
# print(str(candidate1) + ":(" + str(sum(votes_candidate1)) + ")")
# print(str(candidate2) + ":(" + str(sum(votes_candidate2)) + ")")
# print(str(candidate3) + ":(" + str(sum(votes_candidate3)) + ")")
