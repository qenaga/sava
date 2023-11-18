import os
import glob

months = ['September','October','November','December','January', 'February','March','April','May','June']

for i,mo in enumerate(months):
	short = mo[:3].lower()
	
	outfile = 'lessons/' + short + '.md'
	with open(outfile, 'a') as f:
		f.write('---\n')
		f.write('layout: lesson\ntitle: ' + mo + '\n')
		f.write('parent: Category\n')
		f.write('section: ' + str(i) + '\n' )
		f.write('navorder: ' + str(i) + '\n' )
		f.write('permalink: '+ short + '\n')
		f.write('---\n')
