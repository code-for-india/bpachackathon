import json
import pdf2txt
import collections

datalist = []
pdf2txt.main(["", "-M 40", "-ooutput.txt", "voterdata.pdf"])
finaldata = []

infile = open('output_v2.txt').readlines()
for i in xrange(len(infile)):
    if infile[i].strip() and infile[i].strip().split()[0].isdigit():
        fullstring = ','.join(w for w in infile[i].strip().split() if w)
        pointer = 0
        t = collections.OrderedDict()

        pc_no = fullstring.split(',')[pointer]
        pointer += 1
        t["PC Num"] = pc_no

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
        t["District Num"] = dist_no

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
        t["Male"] = male

        female = ""
        if fullstring.split(',')[pointer].isdigit():
            female = fullstring.split(',')[pointer]
            pointer += 1
        t["Female"] = female

        others = ""
        if fullstring.split(',')[pointer].isdigit():
            others = fullstring.split(',')[pointer]
            pointer += 1
        t["Others"] = others

        total = ""
        if fullstring.split(',')[pointer].isdigit():
            total = fullstring.split(',')[pointer]
            pointer += 1
        t["Total"] = total

        finaldata.append(t)


# for line in infile:
#     s = []
#     if line.split():
#         if line.split()[0].isdigit():
#             for word in line.split():
#                 if word:
#                     s.append(word)
#         datalist.append(','.join(w for w in s))

# for line in datalist:
#     if len(line.strip().split(',')) > 1:
#         t = {"pc_no": line.strip().split(',')[0], "pc_name": line.strip().split(',')[1], "dist_no": line.strip().split(',')[2], "district": line.strip().split(',')[3], "assembly_constituency": line.strip().split(',')[4], "male": line.strip().split(',')[5], "female": line.strip().split(',')[6], "others": line.strip().split(',')[7], "total": line.strip().split(',')[8]}
#         print ', '.join(w for w in t.values())
#         finaldata.append(t)

outfile = open('sanitized_data.json', 'w')
outfile.write(json.dumps(finaldata, indent=4))
outfile.close()
