import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")
output_data_csv = os.path.join("Analysis", "PyPoll_output_data.csv")

totalVotes = 0
winnerVotes = 0 
winner = ""

votes = {}
votes["Khan"] = 0
votes["Correy"] = 0
votes["Li"] = 0
votes["O'Tooley"] = 0

with open(election_data_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)


    for row in csvreader:

        totalVotes += 1

        if row[2] == "Khan":
            votes["Khan"] += 1
        elif row[2] == "Correy": 
            votes["Correy"] += 1  
        elif row[2] == "Li": 
            votes["Li"] += 1
        elif row[2] == "O'Tooley": 
            votes["O'Tooley"] += 1 



for name in ["Khan", "Correy", "Li", "O'Tooley"]:    
    if votes[name] > winnerVotes:
        winnerVotes = votes[name]
        winner = name


output = f"""
Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
Khan: {votes["Khan"]/totalVotes * 100:.2f}% ({votes["Khan"]})
Correy: {votes["Correy"]/totalVotes * 100:.2f}% ({votes["Correy"]})
Li: {votes["Li"]/totalVotes * 100:.2f}% ({votes["Li"]})
O'Tooley: {votes["O'Tooley"]/totalVotes * 100:.2f}% ({votes["O'Tooley"]})
-------------------------
Winner: {winner}
-------------------------
"""

print(output)

# open the output file
with open(output_data_csv, "w", newline="") as dataFile:
    dataFile.write(output)


