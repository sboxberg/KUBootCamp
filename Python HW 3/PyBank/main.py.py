import os
import csv

csvname = input ("What .csv file do you want to analyze? ")
bankdata_csv = os.path.join("Resources",csvname)

bank_results = []


with open(bankdata_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
    monthcount = 0
    previousmonth = 0

    for row in csv_reader:
        revenue_change = int(row[1]) - previousmonth
        previousmonth = int(row[1])
        row = row + [revenue_change]
        bank_results.append(row)
        monthcount = monthcount + 1

#The first month revenue chanage should be 0 since there is nothing to compare against
bank_results[0][2]=0

max_revenue_increase = 0
max_revenue_decrease = 0
sum_revenue = 0
sum_revenue_change = 0

#I agonized over whether or not I should use absolute value for revenue change or just some including sign
#I finally decided absolute value would give a more logical answer since similar +/- values could negate
#each other and end up with showing very little volatility (average changes) in a data set with potentially
#high volatility.  In the "real world" I would know what question I was trying to answer and would code accordingly

for row in bank_results:
    sum_revenue = sum_revenue + int(row[1])
    sum_revenue_change = sum_revenue_change + abs(row[2])
    if row[2] > max_revenue_increase:
        max_revenue_increase=row[2]
        max_revenue_increase_date = row[0]
        
    if row[2] < max_revenue_decrease:
        max_revenue_decrease = row [2]
        max_revenue_decrease_date = row[0]

#at first I assume revenue change was looking at last month minus first month, but after examining the data
#and thinking more, I think it's the sum (including negatives) of each month's revenue.  I'll comment out my formula
#and leave it here in case I decide I was right the first time. :)
#total_revenue_change = int(bank_results[monthcount-1][1]) - int(bank_results[0][1])

output_file = os.path.join("Resources","FinancialAnalysis.txt")
with open (output_file, "w") as text_file:
    print ("Financial Analysis", file=text_file)  
    print ("-" * 20, file=text_file)
    print ("Total Months: " + str(monthcount), file=text_file)
    print ("Total Revenue: $" + str(sum_revenue), file=text_file)
    print ("Average Revenue Change: $" + str (int(sum_revenue_change/monthcount)), file=text_file)
    print ("Greatest Increase in Revenue: " + max_revenue_increase_date + " ($" + str(max_revenue_increase) + ")", file=text_file)
    print ("Greatest Decrease in Revenue: " + max_revenue_decrease_date + " ($" + str(max_revenue_decrease) + ")", file=text_file)

print ("Financial Analysis")  
print ("-" * 20)
print ("Total Months: " + str(monthcount))
print ("Total Revenue: $" + str(sum_revenue))
print ("Average Revenue Change: $" + str (int(sum_revenue_change/monthcount)))
print ("Greatest Increase in Revenue: " + max_revenue_increase_date + " ($" + str(max_revenue_increase) + ")")
print ("Greatest Decrease in Revenue: " + max_revenue_decrease_date + " ($" + str(max_revenue_decrease) + ")")
      