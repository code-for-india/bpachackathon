import json
import csv
import collections

csvfile = open('hebbal.csv', 'rU')
csvdata = csv.reader(csvfile)

csv_skip = 0

header_data = []
final_data = {}
final_data["constituency"] = collections.OrderedDict()
final_data["total"] = collections.OrderedDict()
final_data["grand_total"] = collections.OrderedDict()
candidates = []

for row in csvdata:
    if csv_skip == 7:
        for el in row:
            if el.strip() and el != "No Of Valid Votes Cast in Favour of":
                if el == "Polling Station No" and el not in header_data:
                    header_data.append("Polling Station")
                else:
                    header_data.append(el)

    if csv_skip == 8:
        for el in row:
            if el and el not in header_data:
                header_data.append(el)
        candidates = header_data[5:]
    if csv_skip > 9:
        local = collections.OrderedDict()
        # print row
        for i in xrange(len(header_data)):
            if row[i].isdigit():
                local[header_data[i]] = int(row[i])
            else:
                local[header_data[i]] = row[i]
        final_data["constituency"][row[1]] = local

    if row[0].startswith("TOTAL"):
        c = 0
        for el in row:
            if el and not el.startswith("TOTAL"):
                if el.isdigit():
                    final_data["total"][candidates[c]] = int(el)
                else:
                    final_data["total"][candidates[c]] = el
                c += 1

    if row[0].startswith("ALL"):
        c = 0
        for el in row:
            if el and not el.startswith("GRAND") and not el.startswith("ALL"):
                if el.isdigit():
                    final_data["grand_total"][candidates[c]] = int(el)
                else:
                    final_data["grand_total"][candidates[c]] = el
                c += 1

    csv_skip += 1

outfile = open("hebbal.json", "w")
outfile.write(json.dumps(final_data, indent=4))
outfile.close()
