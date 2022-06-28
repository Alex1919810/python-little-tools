import os
import random
filePath = 'E:\\help'#此处修改目录
list_data=os.listdir(filePath)
file = open('x.txt', 'w+')
for i in list_data:
    if i.split('.')[1]=='doc':
        file.write('pandoc -f docx -t markdown -o '+i.split('.')[0] +'.md'+' '+i.split('.')[0]+'.doc'+'\n')
    else:
        file.write('pandoc -f docx -t markdown -o '+i.split('.')[0]+'.md'+' '+i.split('.')[0]+'.docx'+'\n')
file.close()