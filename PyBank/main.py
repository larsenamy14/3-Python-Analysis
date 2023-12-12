#Write pseudo code for PyBank activity

#Import
import os
import csv

#Define variables
months = []
profit_loss_changes = []

monthly_count = 0
net_profit_loss = 0
prior_profit_loss = 0
current_profit_loss = 0
profit_loss_change = 0

#Find file location
pybankfile = os.path.join('..', 'Downloads', 'budget_data.csv')

#Open and read csv
with open(pybankfile) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csv_reader:
        monthly_count += 1
        
        
        current_profit_loss = int(row[1])
        net_profit_loss += current_profit_loss
        
        if (monthly_count ==1):
            prior_profit_loss = current_profit_loss
            continue
            
        else:
            profit_loss_change = current_profit_loss - prior_profit_loss
            months.append(row[0])
            profit_loss_changes.append(profit_loss_change)
            prior_profit_loss = current_profit_loss
            
#Find and calculate requested output
    total_profit_loss = sum(profit_loss_changes)
    avg_profit_loss = round(total_profit_loss/(monthly_count -1),2)
    
    greatest_increase = max(profit_loss_changes)
    greatest_decrease = min(profit_loss_changes)
    
    greatest_increase_month_index = profit_loss_changes.index(greatest_increase)
    greatest_decrease_month_index = profit_loss_changes.index(greatest_decrease)
    
    best_month = months[greatest_increase_month_index]
    worst_month = months[greatest_decrease_month_index]
    
#Print
print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {monthly_count}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${avg_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${greatest_increase})")
print(f"Greatest Decrease in Losses:  {worst_month} (${greatest_decrease})")

#Export a text file with the results
pybank_analysis = os.path.join("budget_data.txt")
with open(pybank_analysis, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {monthly_count}\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${avg_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${greatest_decrease})\n")
