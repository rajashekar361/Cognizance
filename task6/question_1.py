import re,csv
file= open('onelinefile.txt') #reading the txt file
for i in file:
        num = re.findall(r'[+-]?[0-9]+\.[0-9]+', i) #for float valuesa
        alpha = re.findall(r'[a-zA-Z]+', i) #for strings
        j = 0
        for p in range(len(num)):
            with open('filename2.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([str(p+1), alpha[j],num[p],alpha[j+1]]) #creating a line in csv file{in the form int,string,float,string}eg:{1,Aaa,3.5,maths}
            j += 2

with open('filename2.csv', 'r',) as file:
    reader = csv.reader(file)
    for row in reader:   #printing by reading from csv file
        print(','.join(row))