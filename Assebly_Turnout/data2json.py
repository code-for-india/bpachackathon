import json

infile = open('output_v2.txt').readlines()

datalist = []

finaldata = []

for line in infile:
    s = []
    if line.split():
        if line.split()[0].isdigit():
            for word in line.split():
                if word:
                    s.append(word)
        datalist.append(','.join(w for w in s))

for line in datalist:
    if len(line.strip().split(',')) > 1:
        t = {"pc_no": line.strip().split(',')[0], "pc_name": line.strip().split(',')[1], "dist_no": line.strip().split(',')[2], "district": line.strip().split(',')[3], "assembly_constituency": line.strip().split(',')[4], "male": line.strip().split(',')[5], "female": line.strip().split(',')[6], "others": line.strip().split(',')[7], "total": line.strip().split(',')[8]}
        print ', '.join(w for w in t.values())
        finaldata.append(t)

# outfile = open('sanitized_data.json', 'w')
# outfile.write(json.dumps(finaldata, indent=4))
# outfile.close()
