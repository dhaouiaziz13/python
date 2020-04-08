import re

print('MADE BY DHAOUI '.center(50))
print('***put the mail_list in the same folder with the script***\n')

file1=input('give me list 1  name :')
file2=input('give me list 2  name :')
file3=input('give me list 3  name :')




with open(file1) as a , open(file2) as b ,open(file3) as c:
    data1=a.read()
    data2=b.read()
    data3=c.read()
    data=(data1+data2+data3)


def find(filename):
    mail=re.compile(f'\w+@{filename}\.\w+')
    f1=(mail.findall(data,re.I))
    new_file=(open(filename,'w+'))
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

print('\n')
input('DONE......')