import csv

# working with csv files without headers
hosts = [["hallo.load", "192.168.2.2"], ["workload.load", "10.1.102.1"]]

with open("host_info.csv", "w") as hosts_info:
    writer = csv.writer(hosts_info)
    writer.writerows(hosts)

# working with csv files with headers

keys = ["name", "designation", "emp_id"]
dict_data = [{"name": "Shubham", "designation": "SDE I", "emp_id": "1001"},
              {"name": "Shubham", "designation": "SDE I", "emp_id": "1001"},
              {"name": "Shubham", "designation": "SDE I", "emp_id": "1001"}]
with open("emp_info.csv", "w") as emp_info:
    writer = csv.DictWriter(emp_info, keys)
    writer.writeheader()
    writer.writerows(dict_data)