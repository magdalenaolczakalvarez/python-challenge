# import Python Modules 
import os
import csv


# In[3]:


# set file path
file_to_load = "C:/Users/polska2207/Downloads/Starter_Code (8)/Starter_Code/PyBank/Resources/budget_data.csv"
file_to_output = "C:/Users/polska2207/Downloads/Starter_Code (7)/Starter_Code/Financial_Analysis.txt"

# set variables
MonthCount = 0
Total = 0
PL = []
monthList = []
monthlyChanges = []


# In[5]:


# read input csv file
with open(file_to_load, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip first row which contains headers
    csvheader = next(csvreader)
    
    for row in csvreader:
        MonthCount += 1
        Total += int(row[1])
        PL.append(row[1])
        monthList.append(row[0])


# In[6]:


# first month P&L value
firstPL = int(PL[0])

# this loop creates a list of monthly changes
for i in range(1, len(PL)):
    monthlyChanges.append(int(PL[i]) - firstPL)
    firstPL = int(PL[i])
    i += 1

# find max increase and min increase
MaxIncrease = max(monthlyChanges)
MaxDecrease = min(monthlyChanges)


# In[8]:


# find month index for the Max Increase and Max Decrease
for i in range(len(monthlyChanges)):
    if monthlyChanges[i] == MaxIncrease:
        maxIndex = (i - 1)
    elif monthlyChanges[i] == MaxDecrease:
        minIndex = (i - 1)
    else:
        i += 1
        
MaxMonth = monthList[maxIndex]
MinMonth = monthList[minIndex]


# Financial Analysis
# ----------------------------
# Total Months: 
# Total: 
# Average  Change: 
# Greatest Increase in Profits: 
# Greatest Decrease in Profits: 

# In[9]:


print("Financial Analysis")
print("-"*50)
print(f"Total Months: {MonthCount}")
print(f"Average Change: ${Total}")
print(f"Greatest Increase in Profits: {MaxMonth}  (${MaxIncrease})")
print(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")


# In[13]:


# write financial analysis summary to txt file
outputfile = 'summary.txt'

# use "\n" to create a new line
with  open(outputfile, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("-"*50 + "\n")
    output.write(f"Total Months: {MonthCount}\n")
    output.write(f"Average Change: ${Total}\n")
    output.write(f"Greatest Increase in Profits: {MaxMonth}  (${MaxIncrease})\n")
    output.write(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")
 