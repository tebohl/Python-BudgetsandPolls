
#create file paths across operatings systems
import os
#module for reading csv files
import csv

csvpath = os.path.join("Resources", "budget_data.csv")



#read csv file
with open(csvpath) as csvfile:

    #csv reader shows delimiter
    csvreader = csv.reader(csvfile, delimiter= ",")

    #read header row
    header = next(csvreader)
    print(f"{header}")

    #read each row following and count/calculate table values as read
    count = 0
    total = 0
    for row in csvreader:
        print(row)
        count += 1
        net_total = int(row[1])
        total += net_total

    #print data in table
    print("Financial Analysis")
    print("-----------------")
    #print total months
    print("Total Months: " + str(count))
    print("Total: $" + str(total))


