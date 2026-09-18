import csv
with open("t4.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)

    for row in reader:
        maara = int(row[1])
        kokonaishinta = float(row[2].replace(",", "."))
        print(row[0], kokonaishinta / maara)