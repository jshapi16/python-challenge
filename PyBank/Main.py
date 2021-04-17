#import libraries
import os
import csv
#set variable for total months, 
total_months = 0
# set variable for total profit/loss, 
total_profit = 0
# set variable for change in profit/loss
change_profit = []
#store previous amount to calculate each month's change
previous_amount = 0
#set variable for average profit/loss
average_profit = []
#set varaible for greatest increase in profit (date and amount)
greatest_increase_month = ""
max_increase = 0
#set variable for greatest decrease in profit (date and amount)
least_increase_month = ""
min_increase = 1000000000

#Set file path
budget_path = os.path.join(".", "Resources", "budget_data.csv")
 #count number of months and print
#month_count = sum(1 for row in budget_path)






#Open file with header and delimited rows and columns
with open(budget_path) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter = ",")
    budget_header = next(budget_reader)
    print(f"Budget Header: {budget_header}")
    #For loop to iterate over each row in pybank
    for row in budget_reader:
        print(row)
        total_months += 1
        total_profit += int(row[1])
        #Calculating change in profit and min and max increase 
        change_profit.append(int(row[1])- previous_amount)
        if max_increase < (int(row[1])- previous_amount):
            max_increase = (int(row[1])- previous_amount)
            greatest_increase_month = row[0]
        if min_increase > (int(row[1]) - previous_amount):
            min_increase = (int(row[1])- previous_amount)
            least_increase_month = row[0]
        previous_amount = int(row[1])
    #Delete the first row of the data because it would subtract from zero
    del change_profit[0]
    max_increase = max(change_profit)
    min_increase = min(change_profit)
    average_profit = round(sum(change_profit) / (total_months- 1), 2)
#print out results
print(f'''
    Financial Analysis
    ==============================
    Total Months: {total_months}
    Total Profit/Loss: ${total_profit}
    Average Profit Change: ${average_profit}
    Greatest Increase in Profits: {greatest_increase_month} (${max_increase})
    Greatest Decrease in Profits: {least_increase_month} (${min_increase})
    ''')
#exporting results to to txt
budget_txt = os.path.join(".", "Resources", "budget_data_info.txt")
with open(budget_txt, 'w') as budget_text:
    budget_text.write(f'''
    Financial Analysis
    ==============================
    Total Months: {total_months}
    Total Profit/Loss: ${total_profit}
    Average Profit Change: ${average_profit}
    Greatest Increase in Profits: {greatest_increase_month} (${max_increase})
    Greatest Decrease in Profits: {least_increase_month} (${min_increase})
    ''')