import os

for file in os.listdir('.'):
	if file[-2:]=='py':
		continue
	name =file.replace(' ','')
	new_name =name[12:100]##����ǰ׺���ȶ���
	os.rename(file,new_name)