
#create file paths across operatings systems
import os
#module for reading csv files
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#define empty lists for values and calculations below
monthyear = []
month_to_month = []

#read csv file
with open(csvpath) as csvfile:

    #csv reader shows delimiter
    csvreader = csv.reader(csvfile, delimiter= ",")
   
    #read header row
    header = next(csvreader)
    
    # grab first row of data
    first_row = next(csvreader)
    #store date information in list
    monthyear.append(first_row[0])
    # first profit value
    profit_initial = first_row[1]

    #read each row following, beginning variables with first row values
    count = 1
    net_total = int(profit_initial)

    for row in csvreader:
        #store date information in list
        monthyear.append(row[0])

        #find profit change and store in list
        profit_change = int(row[1]) - int(profit_initial)
        month_to_month.append(profit_change)

        #count months (rows) for total months
        count += 1
        net_total += int(row[1])

        #reset profit initial to current value for next loop
        profit_initial = row[1]
        

    #print data in table
    print("Financial Analysis")
    print("-----------------")
    print("Total Months: " + str(count))
    print("Total: $" + str(net_total))
    print("Average Change: " + str(round((sum(month_to_month)/count),0)))
    print("Greatest Increase in Profits: " + monthyear[79] + " ($" + str(max(month_to_month)) + ")")
    #print(month_to_month.index(1862002))
    print("Greatest Decrease in Profits: " + monthyear[49] + " ($" + str(min(month_to_month)) + ")")
    #print(month_to_month.index(-1825558))