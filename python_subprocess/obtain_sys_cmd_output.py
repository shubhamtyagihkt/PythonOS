import subprocess

result = subprocess.run(["host", '8.8.8.8'])
print(result.returncode)

# capture output work only after python3.7
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.stdout)
# print(result.stderr)