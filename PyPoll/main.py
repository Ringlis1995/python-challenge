import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

Candidates = []
Candidate_Votes = {}
Count = 0
Votes_Cast = 0 
Votes_Percent = 0
Votes_Won = 0
Most_Voted = ""

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header= next(csvfile)

    for row in csvreader: 
    #count total votes cast 
        Count = Count + 1
        Candidate = row[2]

        if Candidate not in Candidates : 
            Candidates.append(Candidate)
            Candidate_Votes[Candidate] = 0 
    
        Candidate_Votes[Candidate] = Candidate_Votes[Candidate] + 1

    #total votes per candidate 

#print("Election Results")
#print("_____________________________")
#print(f"Total Votes: {Count}")
#print("_____________________________")

outputpath = os.path.join("analysis", "election_analysis.txt")

with open(outputpath, "w") as txtfile:
    output = (
        f"Election Results\n"
        f"________________________\n"
        f"Total Votes: {Count}\n"
        f"________________________\n"
    )
    txtfile.write(output)
    print(output)

    for Candidate in Candidate_Votes : 
        Votes = Candidate_Votes[Candidate]
        Votes_Percent = float(Votes)/float(Count)*100

        if (Votes > Votes_Won) : 
            Votes_Won = Votes
            Most_Voted = Candidate 


        output = f"{Candidate}: {Votes_Percent}% ({Votes})\n"

        txtfile.write(output)
        print(output)
    output = (
        f"________________________\n"
        f"Winner: {Most_Voted}\n"
        f"________________________\n"
    )

    txtfile.write(output)
    print(output)


