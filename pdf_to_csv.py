
from tabula import convert_into
import csv

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            if type(row[5] == str) and "NUS" in row[5]:
                continue
            rows += (tuple(row), )
    return rows[1:]

convert_into("mappings.pdf", "raw.csv", output_format = "csv", pages = "all", guess = False)

data = read_csv("raw.csv")

final = []
for row in data:
    new = list(row[4:] + row[:4])
    counter = 0
    for elem in new:
        if type(elem) == str:
            new[counter] = elem.replace(",", ";")
        counter += 1
    final += [new,]

with open("output.csv", "w") as outfile:
    for entries in final:
        for element in entries:
            outfile.write(element)
            outfile.write(",")
        outfile.write("\n")



