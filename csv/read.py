import csv

f = open("hello.csv")
csv_f = csv.reader(f)
# opening csv file without headers
for row in csv_f:
    name, phone, address = row
    print("Name: {}, Phone: {}, Address: {}".format(name, phone, address))


# opening csv files with header
with open("hello_header.csv") as dict_file:
    csv_dict = csv.DictReader(dict_file)
    for row in csv_dict:
        print("Name: {}, Address: {}".format(row["name"], row["address"]))
