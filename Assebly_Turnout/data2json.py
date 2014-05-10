import json
import pdf2txt
import collections

datalist = []
pdf2txt.main(["", "-M 40", "-ooutput.txt", "voterdata.pdf"])
finaldata = {}
finaldata["assemblywise"] = []
finaldata["total"] = []

infile = open('output.txt').readlines()
sanitized = []

for line in infile:
    if line.strip() and line.strip().split()[0].isdigit() and len(line.strip().split()) > 4:
        sanitized.append(line.strip())

for i in xrange(len(sanitized)):
    if sanitized[i].strip() and sanitized[i].strip().split()[0].isdigit():
        fullstring = ','.join(w for w in sanitized[i].strip().split() if w)
        pointer = 0
        t = collections.OrderedDict()

        pc_no = fullstring.split(',')[pointer]
        pointer += 1
        t["PC Num"] = int(pc_no)

        pc_name = ""
        if not fullstring.split(',')[pointer].isdigit():
            pc_name += fullstring.split(',')[pointer]
            pointer += 1
        if not fullstring.split(',')[pointer].isdigit():
            pc_name  += " " + fullstring.split(',')[pointer]
            pointer += 1
        t["PC Name"] = pc_name

        dist_no = ""
        if fullstring.split(',')[pointer].isdigit():
            dist_no = fullstring.split(',')[pointer]
            pointer += 1
        t["District Num"] = int(dist_no)

        district = ""
        if not fullstring.split(',')[pointer].isdigit():
            district += fullstring.split(',')[pointer]
            pointer += 1
        if '-' not in fullstring.split(',')[pointer]:
            district  += " " + fullstring.split(',')[pointer]
            pointer += 1
        t["District Name"] = district

        assembly_constituency = ""
        if not fullstring.split(',')[pointer].isdigit():
            assembly_constituency += fullstring.split(',')[pointer]
            pointer += 1
        if not fullstring.split(',')[pointer].isdigit():
            assembly_constituency  += " " + fullstring.split(',')[pointer]
            pointer += 1
        t["Assembly Constituency"] = assembly_constituency

        male = ""
        if fullstring.split(',')[pointer].isdigit():
            male = fullstring.split(',')[pointer]
            pointer += 1
        try:
            t["Male"] = int(male)
        except ValueError:
            t["Male"] = male

        female = ""
        if fullstring.split(',')[pointer].isdigit():
            female = fullstring.split(',')[pointer]
            pointer += 1
        try:
            t["Female"] = int(female)
        except ValueError:
            t["Female"] = female

        others = ""
        if fullstring.split(',')[pointer].isdigit():
            others = fullstring.split(',')[pointer]
            pointer += 1
        try:
            t["Others"] = int(others)
        except ValueError:
            t["Others"] = others

        total = ""
        if fullstring.split(',')[pointer].isdigit():
            total = fullstring.split(',')[pointer]
            pointer += 1
        try:
            t["Total"] = int(total)
        except:
            t["Total"] = total

        finaldata["assemblywise"].append(t)

for line in infile:
    try:
        if not line.strip().split()[0].isdigit() and "Total" in line.strip() and line.strip().split()[-1].isdigit():
            t = collections.OrderedDict()
            t["PC Name"] = line.strip().split("Total")[0].strip()
            t["Male"] = int(line.strip().split()[-4])
            t["Female"] = int(line.strip().split()[-3])
            t["Others"] = int(line.strip().split()[-2])
            t["Total"] = int(line.strip().split()[-1])
            finaldata["total"].append(t)
            # print line.strip().split()
            # print line.strip().split()[-4], line.strip().split()[-3], line.strip().split()[-2], line.strip().split()[-1]
    except:
        pass

outfile = open('sanitized_data.json', 'w')
outfile.write(json.dumps(finaldata, indent=4))
outfile.close()
