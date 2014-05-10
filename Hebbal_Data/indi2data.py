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

final_voter_data = []

for j in range(1580001, 1580212):
    pdf2txt.main(["", "-M 100", "-ob.txt", "pdf/" + str(j) + ".pdf"])
    infile = open("b.txt").readlines()

    globallist = []
    locallist = []
    record = 0

    for line in infile:
        if line.startswith("SOH") and len(locallist) != 0:
            globallist.append(locallist)
            locallist = []
            locallist.append(line)
            record = 1
        elif line.startswith("SOH") and len(globallist) == 0:
            locallist.append(line)
            record = 1
        elif not line.startswith("SOH") and record == 1:
            locallist.append(line)

    locallist = []
    for line in infile:
        if line.startswith("BCW") and len(locallist) != 0:
            globallist.append(locallist)
            locallist = []
            locallist.append(line)
            record = 1
        elif line.startswith("BCW") and len(globallist) == 0:
            locallist.append(line)
            record = 1
        elif not line.startswith("BCW") and record == 1:
            locallist.append(line)

    for item in globallist:
        try:
            new_list = []
            t = collections.OrderedDict()
            for i in xrange(len(item)):
                if item[i].strip():
                    new_list.append(item[i].strip())
            t["id"] = new_list[0]
            t["name"] = new_list[1]
            t["f/m/h name"] = new_list[2]
            for el in new_list:
                if el.startswith("House"):
                    t["house no"] = el.split(":")[1]
                elif el.startswith("Sex"):
                    t["sex"] = el.split("Age")[0].split(":")[1].strip()
                    t["age"] = el.split("Age")[1].split(":")[1].strip()
            final_voter_data.append(t)
        except:
            print "error"

    print str(j), "complete"

print len(final_voter_data)
outfile = open("fulldata_voterwise.json", "w")
outfile.write(json.dumps(final_voter_data, indent=4))
outfile.close()
