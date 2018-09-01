import csv
import math

#set firstline as true to avoid trying to count the column labels
firstline = True
#initialize a dictionary to store results
candidatetally = {}


with open('election_data.csv','r+') as csvfile:
    electionreader = csv.reader(csvfile, delimiter=',')
    #tally number of votes for each candidate individually
    for row in electionreader:
        tempname = row[2]
        if firstline:
            firstline = False
        elif tempname in candidatetally:
            candidatetally[tempname] += 1
        else:
            candidatetally[row[2]] = 1

    #tally the total number of Votes.  Cheaper to do it here than during earlier loop
    subtotal = 0
    for name in candidatetally:
        subtotal += candidatetally[name]

    #output header
    print('Election Results')
    print('----------------------')
    print(f'Total Votes: {subtotal}')
    print('----------------------')


    #print number of votes including rounded percentages (rounded to 3 decimal places)
    for name in candidatetally:
        print(f'{name}: {math.floor(100*1000*candidatetally[name]/subtotal)/1000}% ({candidatetally[name]})')
    print('----------------------')

    #determine Winner
    currentrecord = 0
    currentrecordname = ''
    for name in candidatetally:
        if candidatetally[name] > currentrecord:
            currentrecordname = name
            currentrecord = candidatetally[name]

    print(f'Winner: {currentrecordname}')

    #.txt output
    f = open('pypollresults.txt','w+')
    f.write('Election Results\n')
    f.write('----------------------\n')
    f.write(f'Total Votes: {subtotal}\n')
    f.write('----------------------\n')

    for name in candidatetally:
        f.write(f'{name}: {math.floor(100*1000*candidatetally[name]/subtotal)/1000}% ({candidatetally[name]})\n')
    f.write('----------------------\n')
    f.write(f'Winner: {currentrecordname}')
