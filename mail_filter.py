import re

print('MADE BY DHAOUI '.center(50))
print('***put the mail_list in the same folder with the script***\n')
file_name=input('enter file name in this form file_name.txt :')
file=open(file_name,encoding='utf-8')
data=file.read()
file.close()

def find(filename):
    mail=re.compile(f'\w+@{filename}\.\w+')
    f1=(mail.findall(data,re.I))
    new_file=(open(filename+'.txt','w+'))
    j=0
    for i in f1:
       j+=1
       new_file.write(i+'\n')
    print(f'there are {j} {filename} accounts ')

find('yandex')
find('gmail')
find('yahoo')
find('aol')
find('comcast')
find('seznam')
find('outlook')
find('hotmail')


print('\n')
input('HASTA_LAVISTA_BABY.......... ')



