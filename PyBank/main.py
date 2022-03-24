
#create file paths across operatings systems
import os
#module for reading csv files
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#empty list for profit changes to be stored
month_to_month = []

#read csv file
with open(csvpath) as csvfile:

    #csv reader shows delimiter
    csvreader = csv.reader(csvfile, delimiter= ",")
   
    #read header row
    header = next(csvreader)
    
    # grab first row of data
    first_row = next(csvreader)
 
    # first profit value
    profit_initial = first_row[1]

    #read each row following, beginning variables with first row values
    count = 1
    net_total = int(profit_initial)

    for row in csvreader:
        #count months (rows) for total months
        count += 1
        net_total += int(row[1])

        #find profit change and store in list
        profit_change = int(row[1]) - int(profit_initial)
        month_to_month.append(profit_change)

        #reset profit initial to current value for next loop
        profit_initial = row[1]

        #define variables for table
        greatest_month_increase = (max(month_to_month))
        greatest_month_decrease = (min(month_to_month))
    
        #conditional to keep track of max and min profit change in variables
        if profit_change > (max(month_to_month)):
            greatest_month_increase = profit_change
            increase_monthyear = row[0]

        elif profit_change < (min(month_to_month)):
            greatest_month_decrease = profit_change
            decrease_monthyear = row[0]

    #create variable for text file with printed results
    financial_analysis = f"""
    Financial Analysis
    -----------------
    Total Months: {count}
    Total: ${net_total}
    Average Change: {(round((sum(month_to_month)/len(month_to_month)),0))}
    Greatest Increase in Profits: ${increase_monthyear} ({greatest_month_increase})
    Greatest Decrease in Profits: ${decrease_monthyear} ({greatest_month_decrease})
    """

    #write new text file with results
    print(financial_analysis)

    with open("budget_data.txt", "w") as new_file:
        new_file.write(financial_analysis)