# generate lessons pages for each months
import os
import glob
import csv

outpath = 'pages/'

with open('../_data/lessons.csv', 'r') as csvf:
	csvdict = csv.DictReader(csvf, delimiter=',')
	for row in csvdict:
		mo = row["month_name"]
		short = mo[:3].lower() + str(row["lesson"])
		perm = mo[:3].lower() + '/' + str(row["lesson"])
		with open(outpath + short + '.md', 'w') as f:
			f.write('---\n')
			f.write('title: ' + row["title"] + '\n')
			f.write('parent: ' + mo + '\n')
			f.write('month: ' + str(row["month"]) + '\n' )
			f.write('section: ' + str(row["lesson"]) + '\n' )
			f.write('nav_order: ' + str(row["lesson"]) + '\n' )
			f.write('permalink: '+ perm + '\n')
			f.write('---\n')

