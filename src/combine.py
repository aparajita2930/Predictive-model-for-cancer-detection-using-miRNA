import csv
from glob import glob
import re

FILES = glob("F:/NYU/Hackathon/**/*.mirna.quantification.txt")
print FILES.count
FILES.sort()
#print FILES
OUT_FILE = 'F:/NYU/Hackathon/output_file'

output_writer = open(OUT_FILE, 'a')

patients = dict()
id = 0

for file in FILES:
	print "processing file ", file
	output_writer.write("\n")

	m = re.search("TCGA-..-([A-Za-z0-9]{4,4})-(\d{2,2})[A-Za-z]", file)
	#print m
	patient_id = m.group(1)
	tissue_type = m.group(2)
	
	if patient_id not in patients:
		id = id + 1
		patients[patient_id] = id;

	patient_id = patients[patient_id]

	cancer_type = 2
	tmp = re.search("PAAD", file)
	if tmp is not None:
		cancer_type = 1

	output_writer.write("{0} {1} {2} ".format(patient_id, cancer_type, tissue_type))
	with open(file, 'r') as myFile:
		reader = csv.reader(myFile, delimiter='\t')
		count = 0
		for row in reader:
			try:
				if count == 0:
					count += 1
					continue
				
				#has_header = csv.Sniffer().has_header(myFile.read(1024))
				#reads_per_million_miRNA_mapped = 'NA'
				#myFile.seek(0)  # rewind
				#incsv = csv.reader(myFile)
				#if has_header:
				#	next(incsv)  # skip header row
				reads_per_million_miRNA_mapped = row[2]
				if reads_per_million_miRNA_mapped == 'NA':
					reads_per_million_miRNA_mapped = '0.0'
				reads_per_million_miRNA_mapped = float(reads_per_million_miRNA_mapped)
				output_writer.write(str(reads_per_million_miRNA_mapped))
				
			except ValueError as e:
				output_writer.write('0.0')
				print "Exception wile reading line ", reader.line_num, " from file ", file, "  Expeced a float. Got ", reads_per_million_miRNA_mapped
			
			output_writer.write(" ")