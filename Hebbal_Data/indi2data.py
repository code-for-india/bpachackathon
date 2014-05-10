import json
import pdf2txt
from urllib import urlretrieve
import collections

headers = ["Starting Serial Num", "Ending Serial Num", "Male", "Female", "Others", "Total"]
finaldata = collections.OrderedDict()

for item in range(1580001, 1580213):
    url = "http://ceokarnataka.kar.nic.in/FinalRoll2013_Final/English/WOIMG/AC158/AC" + str(item) + ".pdf"
    filename = str(item) + ".pdf"
    urlretrieve(url, filename)
    pdf2txt.main(["", "-M 40", "-p 1", "-oa.txt", filename])

    infile = open("a.txt").readlines()

    output = collections.OrderedDict()

    for line in infile:
        if line.strip().startswith("Part"):
            for el in line.strip().split():
                if el.isdigit():
                    part = el

        if line.startswith("Male Female"):
            for i in xrange(len(infile[infile.index(line) + 1].strip().split())):
                output[headers[i]] = infile[infile.index(line) + 1].strip().split()[i]

    finaldata["158"+str(item)[-3:]] = output
    print str(item), "complete"

outfile = open("fulldata.json", "w")
outfile.write(json.dumps(finaldata, indent=4))
outfile.close()
