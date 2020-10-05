import subprocess

# here we run command and can check exit status of the command ran
print(subprocess.run(["date"]))
print(subprocess.run(["sleep", "2"]))
# output will be like this:

# CompletedProcess(args=['date'], returncode=0)
# CompletedProcess(args=['sleep', '2'], returncode=0)