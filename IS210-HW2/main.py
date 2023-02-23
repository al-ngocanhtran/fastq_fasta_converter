import re
import sys
import random 
import string

"""
SIMPLE FASTA-FASTQ CONVERTER

To run script in command line, enter: 
python main.py function file

Function 
q2a: convert fastq to fasta file 
a2q: convert fasta to fastq file with fake randomized quality score data
"""

def q2a(file):
    with open(file) as f:
        lines = [line.rstrip() for line in f]
    output = "> \n"
    n = 0 #line count indicator
    for n in range(1, len(lines), 4):
        output += lines[n]
    newfile = file.replace('fastq', '') + 'fasta' 
    f = open(newfile, "w")
    f.write(output)
    f.close()
    print("Conversion success!")

def a2q(file):
    f = open(file)
    for n in range(2): 
        lines = f.readline().rstrip()
    n = random.randrange(100, 251)
    reads = [lines[i:i+n] for i in range(0, len(lines), n)]
    output = ''
    for i in range(len(reads)):
        line1 = '@'.join(random.choice(string.ascii_uppercase) for k in range(3))
        line1 = line1.join(random.choice(string.digits) for k in range(5))
        line1 += "." + str(i+1) + " " + str(i+1) + "/1 \n" 
        line2 = reads[i] + "\n" 
        line4 = "".join(random.choice(chr(random.randrange(33, 74))) for k in range(len(reads[i])))
        output += line1 + line2 + "+ \n" + line4 + '\n'
    
    newfile = file.replace('fasta', '') + 'fastq' #change file format
    f = open(newfile, "w")
    f.write(output)
    f.close()
    print("Conversion success!")
    

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
