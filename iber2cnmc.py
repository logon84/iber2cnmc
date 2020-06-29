#!/usr/bin/python3 
import sys, getopt
import os
import datetime
		
def get_int_hour (s): #remove starting zeros & minutes from hours
	s = s.replace("00:","24:") #convert midnight hour
	if s[:1] == '0':
		return s[1:2] #if hour starts with zero, remove it at return and also minutes
	else:
		return s[:2] #just remove minutes

def csv2csv(inname, outname):
	csv_head = 'CUPS;Fecha;Hora;Consumo_kWh;Metodo_obtencion\n'
	out_file = csv_head
	with open(inname) as file_in:
		next(file_in)
		for line in file_in:
			line_split = line.split(";")
			CUPS = line_split[0]+";"
			date = datetime.datetime.strptime(line_split[1].split()[0], "%Y/%m/%d").strftime("%d/%m/%Y") + ";"
			hour = get_int_hour(line_split[1].split()[1]) + ";"
			consumption = str(float(line_split[3])/1000).replace('.',',') + ";"
			obtained = "R"
			out_file = out_file + CUPS + date + hour + consumption + obtained + "\n"
	file_out = open(outname,'w')
	file_out.write (out_file)
	file_out.close()

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print('iber2cnmc.py -i <inputfile.csv> -o <outputfile.csv>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('iber2cnmc.py -i <inputfile.csv> -o <outputfile.csv>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	if inputfile != '' and outputfile != '':
		csv2csv(inputfile, outputfile)
	else:
		print('iber2cnmc.py -i <inputfile.csv> -o <outputfile.csv>')
		sys.exit()	

if __name__ == "__main__":
   main(sys.argv[1:])
