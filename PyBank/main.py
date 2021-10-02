import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")
output_data_csv = os.path.join("analysis", "PyBank_output_data.csv")

totalMonths = 0
totalDollars = 0
changeCount = 0
totalChanges = 0
change = 0
biggestIncrease = 0
biggestDecrease = 0
previousBudget = 0

with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        # exit()

        totalMonths += 1

        currentBudget = int(row[1])

        totalDollars += currentBudget

        if previousBudget != 0:
            change = currentBudget - previousBudget
            totalChanges += change
            changeCount += 1

            if change > biggestIncrease:
                biggestIncrease = change
                biggestIncreaseDate = row[0]

            if change < biggestDecrease:
                biggestDecrease = change
                biggestDecreaseDate = row[0] 

        previousBudget = currentBudget     


output = f"""
Financial Analysis
----------------------------
Total Months: {totalMonths}
Total: ${totalDollars:,.2f}
Average Change: (${totalChanges / changeCount:,.2f})
Greatest Increase in Profits: {biggestIncreaseDate} ${biggestIncrease:,.2f}
Greatest Decrease in Profits: {biggestDecreaseDate} (${biggestDecrease:,.2f})
"""

print(output)

# open the output file
with open(output_data_csv, "w", newline="") as dataFile:
    dataFile.write(output)
    
