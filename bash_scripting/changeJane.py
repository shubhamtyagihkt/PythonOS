#!/usr/bin/env python3
import sys
import subprocess


with open(sys.argv[1]) as file:
  lines = file.readlines()
  for line in lines:
    print(line)
    line = line.strip()
    if 'jane' in line:
      subprocess.run(['mv', line, line.replace('jane', 'jdoe')])
