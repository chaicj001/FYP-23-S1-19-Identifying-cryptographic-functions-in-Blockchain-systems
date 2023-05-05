import subprocess

# ask for user input
text = input("Enter some text: ")

with open('output.txt', 'w') as f:
    subprocess.run(["python", "hashid.py", text], stdout=f)
#runs hashid and
#saves it to file

noko = subprocess.Popen(["python", "hashid.py", text], stdout=subprocess.PIPE)

output = noko.stdout.read()
#runs hashid but pipes output to "output" variable
output_decoded = output.decode("utf-8")
#remove first line, then process text below to match 

print(output_decoded)
