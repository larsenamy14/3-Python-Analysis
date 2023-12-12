#Write pseudo code for PyPoll analysis

#Import
import os
import csv
import collections
from collections import Counter

#Define variables
total_votes = 0
candidates = []
votes_per_candidate = []

#Find file location
pypollfile = os.path.join('..', 'Downloads', 'election_data.csv')

#Open and read csv
with open(pypollfile) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

#Calculate the total number of votes cast
    for row in csv_reader:
        total_votes += 1
        candidates.append((row[2]))

#Sort and arrange list of votes by candidate
    sorted_list = sorted(candidates)
        
    arrange_list = sorted_list
 
#Calculate the total number of votes each candidate won
    count_candidate = Counter(arrange_list)
    votes_per_candidate.append(count_candidate.most_common())
        
#Find percentage of top 3 candidates
    for item in votes_per_candidate:
        
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')

#Print
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {total_votes}")
print("-------------------------")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print("-------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print("-------------------------")


#Export
election_file = os.path.join("election_data.txt")
with open(election_file, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {total_votes}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
    outfile.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
    outfile.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
    outfile.write("-------------------------\n")
