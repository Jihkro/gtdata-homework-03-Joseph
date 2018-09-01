#The purpose of this file is to take data from budget_data.csv and interpret several things about it

import csv
import math

netgains = 0
firstline = True
secondline = True
monthcounter = 0
recordgain = 0
recordloss = 0
recordgaindate = ''
recordlossdate = ''


with open('budget_data.csv','r+') as csvfile:
    budgetreader = csv.reader(csvfile, delimiter=',')
    for row in budgetreader:
        if firstline:
            firstline = False
        elif secondline:
            secondline = False
            openingvalue = int(row[1])
            netgains += int(row[1])
            monthcounter += 1
            if int(row[1])> recordgain:
                recordgain = int(row[1])
                recordgaindate = row[0]
                #print(f'New record gain of {recordgain} on {recordgaindate}')
            if int(row[1])<recordloss:
                recordloss = int(row[1])
                recordlossdate = row[0]
                #print(f'New record loss of {recordloss} on {recordlossdate}')


        else:
            netgains += int(row[1])
            monthcounter += 1
            closingvalue = int(row[1])
            if int(row[1])> recordgain:
                recordgain = int(row[1])
                recordgaindate = row[0]
                #print(f'New record gain of {recordgain} on {recordgaindate}')
            if int(row[1])<recordloss:
                recordloss = int(row[1])
                recordlossdate = row[0]
                #print(f'New record loss of {recordloss} on {recordlossdate}')


    f = open('pybankoutput.txt','w+')

    print('Financial Analysis')
    f.write('Financial Analysis\n')
    print('------------------')
    f.write('------------------\n')
    print(f'Total Months: {monthcounter}')
    f.write(f'Total Months: {monthcounter}\n')
    print(f'Total: ${netgains}')
    f.write(f'Total: ${netgains}\n')
    print(f'Average Change: ${math.floor(100 * (closingvalue-openingvalue)/(monthcounter - 1))/100}')
    f.write(f'Average Change: ${math.floor(100 * (closingvalue-openingvalue)/(monthcounter - 1))/100}\n')
    print(f'Greatest Increase in Profits: {recordgaindate} (${recordgain})')
    f.write(f'Greatest Increase in Profits: {recordgaindate} (${recordgain})\n')
    print(f'Greatest Decrease in Profits: {recordlossdate} (${recordloss})')
    f.write(f'Greatest Decrease in Profits: {recordlossdate} (${recordloss})\n')
