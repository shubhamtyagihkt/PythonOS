#!/usr/bin/env python3

import csv

def read_employee(csv_file_location):
        with open(csv_file_location) as file:
                dict_reader = csv.DictReader(file)
                # there is not standard way to define csv
                # so the parser need to be flexible
                # for  thi swe use dialect property
                csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
                # this dailct remove any leading spaces while parsing
                emp_file = csv.DictReader(file, dialect = 'empDialect')
                employee_list = []
                for data in emp_file:
                        employee_list.append(data)
                return employee_list

def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
                department_list.append(employee_data['Department'])
        department_data = {}
        for department_name in set(department_list):
                department_data[department_name] = department_list.count(department_name)
        return department_data


def write_report(dictionary, report_file):
        with open(report_file, "w+") as f:
                for k in sorted(dictionary):
                        f.write(str(k)+':'+str(dictionary[k])+'\n')


employee_list = read_employee('employees.csv')
dictionary = process_data(employee_list)
write_report(dictionary, 'report.txt')
