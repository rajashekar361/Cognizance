import re,csv
fh = open('onelinefile.txt')
for i in fh:
        num = re.findall(r'[+-]?[0-9]+\.[0-9]+', i)
        alpha = re.findall(r'[a-zA-Z]+', i)
        j = 0
        for p in range(len(n)):
            with open('filename2.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([str(p+1), alpha[j],num[p],alpha[j+1]])
            j += 2

with open('filename2.csv', 'r',) as file:
    reader = csv.reader(file)
    for row in reader:
        print(','.join(row))