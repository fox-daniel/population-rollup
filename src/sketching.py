import csv

with open("sketching.csv", "r+", newline="") as rpfile:
	reader = csv.reader(rpfile, delimiter=",")
	writer = csv.writer(rpfile, delimiter=",")
	for row in reader:
		new_row = [ r*2 for r in row]
		writer.writerow(new_row)
