
#create file paths across operatings systems
import os
#module for reading csv files
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#define empty lists for values and calculations below
month_to_month = []

#read csv file
with open(csvpath) as csvfile:

    #csv reader shows delimiter
    csvreader = csv.reader(csvfile, delimiter= ",")

    #read header row
    header = next(csvreader)
    print(f"{header}")

    #read each row following
    count = 0
    net_total = 0
    for row in csvreader:
        print(row)
        #count months (rows) for total months
        count += 1
        total = int(row[1])
        net_total += total

    #reset csvreader to read through rows a second time
    csvfile.seek(0)    
    header = next(csvreader)
    
    #find change between consecutive months and store in list
    for row in csvreader:
        currentrow = row[1]
        nextrowtotal= next(csvreader)
        change = int(nextrowtotal[1]) - int(currentrow)
        month_to_month.append(change)


    #print data in table
    print("Financial Analysis")
    print("-----------------")
    print("Total Months: " + str(count))
    print("Total: $" + str(net_total))
    print(month_to_month)
    


