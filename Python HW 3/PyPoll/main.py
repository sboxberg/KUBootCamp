import os
import csv

csvname = input ("What .csv file do you want to analyze? ")
electiondata_csv = os.path.join("Resources",csvname)

election_results = {}


with open(electiondata_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    for row in csv_reader:
        #Add to existing total
        if row[2] in election_results:
            election_results[row[2]]=election_results.get(row[2],0)+ 1
        #Add new candidate
        else:
            election_results[row[2]] = 1

winnertotal = 0
totalvotes = 0

for key, value in election_results.items():
    totalvotes = totalvotes + value
    if value > winnertotal:
        winnertotal=value
        winnername = key

output_file = os.path.join("Resources","ElectionResults.txt")
with open (output_file, "w") as text_file:
    print ("Election Results", file=text_file)
    print ("-" * 25, file=text_file)
    print ("Total Votes: " + str(totalvotes), file=text_file)
    print ("-" * 25, file=text_file) 

    for key, value in election_results.items():
        percenttotal = round ((value/totalvotes) * 100, 1)
        print(key + ": " + str (percenttotal) + "% " + "(" + str (value) + ")", file=text_file)

    print ("-" * 25, file=text_file)
    print ("Winner: " + winnername, file=text_file)
    print ("-" * 25, file=text_file)

print ("Election Results")  
print ("-" * 25)
print ("Total Votes: " + str(totalvotes))
print ("-" * 25) 

for key, value in election_results.items():
    percenttotal = round ((value/totalvotes) * 100, 1)
    print(key + ": " + str (percenttotal) + "% " + "(" + str (value) + ")")

print ("-" * 25)
print ("Winner: " + winnername)
print ("-" * 25)

        
