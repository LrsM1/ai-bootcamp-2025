import csv

with open("data.csv") as fd:
    reader = csv.reader(fd)
    for line in reader:
        print(line)

with open("data.csv") as fd:
    reader = csv.reader(fd)
    head = next(reader)
    sorted_data = sorted(reader, key =lambda person: (person[1],person[0]))
    print(sorted_data)
    for k, v in enumerate(sorted_data):
        # head.append(v)
        v.insert(0, f"{k + 1}")
        print(v)

with open("data_output.csv", "w") as fd:
    writer = csv.writer(fd)
    writer.writerow(head)
    writer.writerows([s[1:] for s in sorted_data])


