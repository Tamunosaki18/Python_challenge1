import os
import csv

# Path to the CSV file
budget_data = os.path.join("C:/Users/amach/Downloads/Starter_Code (19)/Starter_Code/PyBank/Resources/budget_data.csv")

# Define variables
total_months = 0
net_profit = 0
dates = []
profits = []
previous_profit = None
changes = []

# Open the file
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
     
    # Skip the header row
    header = next(csvreader)
    
    # Start loop to calculate values
    for row in csvreader:
        # Extract data from row
        date = row[0]
        profit = int(row[1])
        
        # Calculate the total number of months over the entire period 
        total_months += 1
        
        # Calculate net total amount over entire period
        net_profit += profit
        
        # Store the date and profit in lists
        dates.append(date)
        profits.append(profit)
        
        # Calculate profit change (skip for the first row)
        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)
        previous_profit = profit

# Calculate the average change
average_change = round(sum(changes) / len(changes), 2)

# Calculate the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Find the corresponding dates for the greatest increase and decrease
increase_date = dates[changes.index(greatest_increase) + 1]
decrease_date = dates[changes.index(greatest_decrease) + 1]

# Print the results to the console
print("Financial Analysis")
print("-------------------")
print("Total Months:", total_months)
print("Total: $", net_profit)
print("Average Change: $", average_change)
print("Greatest Increase in Profits:", increase_date, "($", greatest_increase, ")")
print("Greatest Decrease in Profits:", decrease_date, "($", greatest_decrease, ")")

# Print results to a text file
with open("PyBank.txt", "w") as f:
    f.write("Financial Analysis\n")
    f.write("-------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${net_profit}\n")
    f.write(f"Average Change: ${average_change}\n")
    f.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
    f.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")
   