import os
import csv

#open/read csv
csvpath = os.path.join("Resources", "budget_data.csv")

#variables
Date = []
Profit_Loss = []
Dif = []
Greastest_Increase_Date = ""
Greatest_Decrease_Date = ""


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  
    csv_header = next(csvfile)

    for row in csvreader:
        Date.append(row[0])
        Profit_Loss.append(int(row[1]))

    #print("Financial Analysis")
    #print("_______________________")
    #print("Total Months", len(Date))
    #print("Total: $", sum(Profit_Loss))

    for i in range(1, len(Profit_Loss)):
        Dif.append(Profit_Loss[i] - Profit_Loss[i-1])
        Average_Change = sum(Dif) / len(Dif)

        Greatest_Increase = max(Dif)
        Greastest_Increase_Date = str(Date[Dif.index(max(Dif))])

        Greatest_Decrease = min(Dif)
        Greastest_Decrease_Date = str(Date[Dif.index(max(Dif))])
    
    output = (
        f"Financial Analysis\n"
        f"____________________\n"
        f"Total Months {len(Date)}\n"
        f"Total: ${sum(Profit_Loss)}\n"
        f"Average Change: ${round(Average_Change)}\n"
        f"Greatest Increase: {Greastest_Increase_Date} (${Greatest_Increase})\n"
        f"Greatest Decrease: {Greastest_Decrease_Date} (${Greatest_Decrease})\n"

    )
    print(output)
    #print("Average Change: $", round(Average_Change))
    #print("Greatest Increase: ", Greastest_Increase_Date, "($", Greatest_Increase,")")
    #print("Greatest Decrease: ", Greatest_Decrease_Date, "($", Greatest_Decrease,")")

outputpath = os.path.join("analysis", "budget_analysis.txt")

with open(outputpath, "w") as txtfile:
    txtfile.write(output)

    


