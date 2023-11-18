import os
import glob

# Use glob to get a list of HTML files in the directory
html_files = glob.glob(os.path.join('../html', '*.html'))

# Loop through each HTML file
for lesson in html_files:
	with open('out.csv','a') as outfile:
		with open(lesson, 'r') as f:
			for line in f:
				line = line.strip()
				parts = line.split('\t')
				if len(parts)>1:
					if parts[1].isdigit():
						month = parts[0]
						num = parts[1]
					else:
						newlist = [str(month),str(num)] + parts
						outline = ','.join('"' + item + '"' for item in newlist)
						outfile.write(outline+'\n') 
