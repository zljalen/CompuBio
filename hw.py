#! /usr/bin/python
#   Welcome! Let's go to reverse complement a Fasta file.
#   Please enter your command line as the following format:
#   Python run_file.py fasta_filename RNA[Optional]

import sys
import os.path

# Reading input file into a list
def read_file(filename):
	if os.path.isfile(filename):						# Check if "filename" is an existing regular file
		with open(filename,"r") as myfile:
			myfile = myfile.readlines()				
			if myfile[0][0] == ">":				# Check if the input file starts with ">"
				return myfile				# Read the input file as a list
			else:
				print "This is not a fasta file!!!"
				myfile.close()
				return 
	else:
		print "Can not find the file!!!"
		return 

# Find titles(Labels include names and comments) and sequences 
def read_titles_sequences(myfile):
	titles = []
	sequences = []
	sequences_number = 0
	for line in myfile:
		if line.startswith(">"):
			titles.append(line.replace('\n',''))
			sequences.append('')                     
			sequences_number += 1
		else:
			sequences[sequences_number-1] += line.replace('\n','')
	for i in range(len(titles)):
		titles[i] += ", %s bp" %str(len(sequences[i]))    # Add the sequence length to the end of the sequence label
	return titles, sequences                              # Return two lists

#For DNA reverse complement
def DNA_RevCom(sequences):
	sequences_reverse = []
	sequences_revcom = []
	for i in range(len(sequences)):
		sequences_reverse.append(sequences[i][::-1])
		seq_middle = sequences_reverse[i].replace("A","a").replace("T","b").replace("C","c").replace("G","d")
		seq_final = seq_middle.replace("a","T").replace("b","A").replace("c","G").replace("d","C")
		sequences_revcom.append(seq_final)
	return sequences_revcom

#For RNA reverse complement
def RNA_RevCom(sequences):
	sequences_reverse = []
	sequences_revcom = []
	for i in range(len(sequences)):
		sequences_reverse.append(sequences[i][::-1])
		seq_middle = sequences_reverse[i].replace("A","a").replace("T","b").replace("C","c").replace("G","d")
		seq_final = seq_middle.replace("a","U").replace("b","A").replace("c","G").replace("d","C")
		sequences_revcom.append(seq_final)
	return sequences_revcom

#Output the DNA reverse complement
def file_write_DNA(titles,sequences_revcom):
	with open("DNA_output.fa",'w') as DNA_file:
		for i in range(len(titles)):
			DNA_file.write(titles[i])
			DNA_file.write("\n")
			for j in range(len(sequences_revcom[i])):
				if (j+1)%60 == 0:
					DNA_file.write(sequences_revcom[i][j])
					DNA_file.write("\n")
				else:
					DNA_file.write(sequences_revcom[i][j])
			DNA_file.write("\n")
	print "Check the output result in file DNA_output.fa!"  #Put the output result in a file named "DNA_output.fa"
	DNA_file.close()

#Output the RNA reverse complement
def file_write_RNA(titles,sequences_RNA_revcom):
	with open("RNA_output.fa",'w') as RNA_file:
		for i in range(len(titles)):
			RNA_file.write(titles[i])
			RNA_file.write("\n")
			for j in range(len(sequences_RNA_revcom[i])):
				if (j+1)%60 == 0:
					RNA_file.write(sequences_RNA_revcom[i][j])
					RNA_file.write("\n")
				else:
					RNA_file.write(sequences_RNA_revcom[i][j])
			RNA_file.write("\n")
	print "Check the output result in file RNA_output.fa!" #Put the output result in a file named "RNA_output.fa"
	RNA_file.close()
	



# For users to enter commands
# The entry format must be: Python run_file.py fasta_filename RNA[Optional]

if len(sys.argv) == 1:
	print "Did you enter the fasta file?"    #Remind users to input the name of fasta file.

if len(sys.argv) == 2:                       # DNA Reverse complement
	filename = sys.argv[1]
	myfile = read_file(filename)
	titles,sequences = read_titles_sequences(myfile)
	sequences_revcom = DNA_RevCom(sequences)
	file_write_DNA(titles,sequences_revcom)

if len(sys.argv) == 3:						# RNA Reverse complement
	filename =sys.argv[1]
	kind = sys.argv[2]
	if kind == "RNA":
		myfile = read_file(filename)
		titles,sequences = read_titles_sequences(myfile)
		sequences_revcom = RNA_RevCom(sequences)
		file_write_RNA(titles,sequences_revcom)
	else:
		print "Did you output reverse complement as an RNA sequence?"  # Remind the error when users input a string not "RNA"

if len(sys.argv) >3:
	print "Oops, you enter two many arguments!!!" 		# Remind the error when users input two many arguments




