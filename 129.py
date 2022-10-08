import csv
import pandas as pd

df=pd.read_csv('dwarf_stars.csv')
df=df.dropna()

d1 = []
d2 = []
csv_reader=csv.reader(df)
for i in csv_reader:
        d2.append(i)

with open('star_data.csv', 'r') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        d1.append(i)

head1 = d1[0]
head2 = d2[0]

stardata1 = d1[1:]
stardata2 = d2[1:]

head = head1+head2

stardata = []

for i in stardata1:
    stardata.append(i)
for j in stardata2:
    stardata.append(j)
with open("total_Stars.csv", 'w',newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(head)
    csvwriter.writerows(stardata)
