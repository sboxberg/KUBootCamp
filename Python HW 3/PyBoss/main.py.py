import os
import csv

#based on the instructions, I'm assuming we want to import both datasets and then combine to a single output.  

employee_data1_csv = os.path.join("Resources","employee_data1.csv")
employee_data2_csv = os.path.join("Resources","employee_data2.csv")

employee_data = []
new_employee_data = []
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
with open(employee_data1_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    for row in csv_reader:
        employee_data.append(row)

with open(employee_data2_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    for row in csv_reader:
        employee_data.append(row)       

EmplID = []
FirstName =[]
LastName =[]
DOB = []
SSN = []
State = []

for row in employee_data:
    EmplID.append(row[0])
    FirstLast = row[1].split (" ")
    FirstName.append(FirstLast[0])
    LastName.append(FirstLast [1])
    Date = row[2].split ("-")
    DOB.append(Date[1]+"/"+Date[2]+"/"+Date[0])
    SSN_split= row[3].split ("-")
    SSN.append("***-**-"+SSN_split[2])
    State.append(us_state_abbrev.get (row[4]))
    
new_employee_data = zip(EmplID,FirstName,LastName,DOB,SSN,State)    

output_file = os.path.join("Resources","employee_data_clean.csv")
with open (output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    writer.writerows(new_employee_data)
