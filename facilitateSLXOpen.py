import subprocess
import sys

directory = ''  # blank if in same directory
subprocess.run(['python', directory + 'simulinkOpen.py'], capture_output=True, text=True)

print("stdout:", result.stdout)
print("stderr:", result.stderr)








# result = subprocess.run(
#     [sys.executable, "-c", "raise ValueError('oops')"], capture_output=True, text=True, shell=True)

