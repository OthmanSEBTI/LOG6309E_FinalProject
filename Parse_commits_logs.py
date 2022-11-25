
from os import listdir
from os.path import isfile, join

fichiers = [f for f in listdir('Commits logs')
            if isfile(join('Commits logs', f))]
NumberOfFailures = []
NumberOfMerges = []

for f in fichiers:

    file1 = open('./Filter Commits logs/'+f+'_' +
                 'merge_lines.txt', 'w', encoding='utf-8')
    file2 = open('./Filter Commits logs/'+f+'_' +
                 'Fix_lines.txt', 'w', encoding='utf-8')
    file3 = open('./Filter Commits logs/'+f+'_' +
                 'normal_lines.txt', 'w', encoding='utf-8')

    if (f in ['composer', 'otp']):
        continue

    file = open('./Commits logs/'+f, 'r', encoding='utf-8')
    Lines = file.readlines()

    for line in Lines:
        if "Fix" in line:
            file2.write(line)
        elif "Merge" in line:
            file1.write(line)
        else:
            file3.write(line)

    file1 = open('./Filter Commits logs/'+f+'_' +
                 'merge_lines.txt', 'r', encoding='utf-8')
    file2 = open('./Filter Commits logs/'+f+'_' +
                 'Fix_lines.txt', 'r', encoding='utf-8')
    NumberOfMerges.append(len(file1.readlines()))
    NumberOfFailures.append(len(file2.readlines()))
