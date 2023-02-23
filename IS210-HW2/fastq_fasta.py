import re
import sys
import random 
import string

"""
To run script in command line, enter: 
python.py fastq_fasta function file_name

"""#function: 

def q2a(file):
    with open(file) as f:
        lines = [line.rstrip() for line in f]
    result = "> \n"
    n = 0 #line count indicator
    for line in lines:
        if (n % 4 == 1):
            result += line
        n += 1
    newfile = file.replace('fastq', '') + 'fasta' 
    f = open(newfile, "w")
    f.write(result)
    f.close()
    print("Open folder to view file!")

def a2q(file):
    f = open(file)
    for n in range(2): 
        dna = f.readline().rstrip()
    n = random.randrange(100, 251)
    seqs = [dna[i:i+n] for i in range(0, len(dna), n)]
    result = ''
    for i in range(len(seqs)):
        first_line = '@'.join(random.choice(string.ascii_uppercase) for k in range(3))
        first_line = first_line.join(random.choice(string.digits) for k in range(5))
        first_line += "." + str(i+1) + " " + str(i+1) + "/1 \n" 
        second_line = seqs[i] + "\n" 
        nus = len(seqs[i])
        fourth_line = "".join(random.choice(chr(random.randrange(33, 74))) for k in range(nus))
        result += first_line
        result += second_line
        result += "+ \n"
        result += fourth_line + '\n'
    
    newfile = file.replace('fasta', '') + 'fastq' 
    f = open(newfile, "w")
    f.write(result)
    f.close()
    print("Open folder to view file!")
    

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
