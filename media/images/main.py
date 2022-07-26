import subprocess

input_file = 'media/images/20171001_141258.jpg'
exe = 'hachoir-metadata'
process = subprocess.Popen([exe, input_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

for output in process.stdout:
    print(output)