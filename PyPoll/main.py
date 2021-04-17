#import libraries
import os
import csv

#path to file
pypoll_path = os.path.join(".", "Resources", "election_data.csv")

#set up variables
vote_col = []
total_votes: 0
total_votes: 0
total_candidates = []
khan_total = 0
correy_total = 0
li_total = 0
otooley_total = 0

#open file
with open(pypoll_path) as pypoll_file:
    pypoll_reader = csv.reader(pypoll_file, delimiter = ",")
    pypoll_header = next(pypoll_reader)
    print(f"Budget Header: {pypoll_header}")
    for row in pypoll_reader:
        vote_col.append(row[2])

#Save candidate information to list and iterate off list
total_votes = len(vote_col)

#Find unique candidates
unique_candidates = list(set(vote_col))

#Add number of votes to each unique candidate's vote total variable
for name in vote_col:
    if name == "Khan":
        khan_total += 1
    elif name == "Correy":
        correy_total += 1
    elif name == "Li":
        li_total += 1
    else:
        otooley_total +=1

#Find percentage of votes each candidate wins
percentage_khan = round(((khan_total / total_votes) * 100), 2)
correy_percentage = round(((correy_total / total_votes) * 100), 2)
li_percentage = round(((li_total / total_votes) * 100), 2)
otooley_percentage = round(((otooley_total / total_votes) * 100), 2)

#Print out vote count receipt
print(f''' Election results:
---------------------------
Total votes: {total_votes}
=========================
Khan votes: {khan_total} 
Khan Percent: {percentage_khan}%
===============================
Correy votes: {correy_total}
Correy Percent: {correy_percentage}%
===============================
Li votes: {li_total} 
Li Percent: {li_percentage}%
===============================
O'tooley votes: {otooley_total}
otooley_percentage: {otooley_percentage}%
=======================================
Winner: Khan
''')

#exporting results to to txt
pypoll_txt = os.path.join(".", "Resources", "pypoll_data_info.txt")
with open(pypoll_txt, 'w') as pypoll_text:
    pypoll_text.write(f''' 
                        Election Results:
                        -------------------------------------
                        Total votes: {total_votes}
                        =====================================
                        Khan: {percentage_khan}% ({khan_total}) 
                        ======================================
                        Correy: {correy_percentage}% ({correy_total})
                        =====================================
                        Li votes: {li_percentage}% ({li_total}) 
                        ======================================
                        O'tooley votes: {otooley_percentage}% ({otooley_total})
                        =======================================
                        Winner: Khan
                        ''')