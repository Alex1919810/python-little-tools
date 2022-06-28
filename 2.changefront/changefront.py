import os

for file in os.listdir('.'):
	if file[-2:]=='py':
		continue
	name =file.replace(' ','')
	new_name =name[12:100]##根据前缀长度而定
	os.rename(file,new_name)