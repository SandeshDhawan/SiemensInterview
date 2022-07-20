import csv

with open('TestData.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.DictReader(file)

    # Initialized max and min to First Employee Salary
    for value in csvFile:
        max = int(value["Salary"])
        min = int(value["Salary"])
        maxSalary = value
        minSalary = value
        break

    # Comparing a salary and if it is maximum then assigning to a max variable and whole record to a maxSalary
    # Comparing a salary and if it is minimum then assigning to a min variable and whole record to a minSalary
    for lines in csvFile:
        if int(lines['Salary']) > max:
            maxSalary = lines
            max = int(lines["Salary"])

        if int(lines['Salary']) < min:
            minSalary = lines
            min = int(lines["Salary"])

# Checking Second Highest and Lowest Salary
with open('TestData.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.DictReader(file)

    secondMaxSalary = minSalary
    secondMinSalary = maxSalary
    small = int(max)
    large = int(min)

    for lines in csvFile:
        if small > int(lines['Salary']) > min:
            small = int(lines["Salary"])
            secondMinSalary = lines

        if large < int(lines['Salary']) < max:
            large = int(lines["Salary"])
            secondMaxSalary = lines

print("Maximum Salary in Employee Record is=", maxSalary)
print("Second Maximum Salary in Employee Record is=", secondMaxSalary)

print("Minimum Salary in Employee Record is = ", minSalary)
print("Second Minimum Salary in Employee Record is=", secondMinSalary)
