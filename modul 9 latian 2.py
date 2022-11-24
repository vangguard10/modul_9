# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 15:56:10 2022

@author: fariz
"""

def tulis (a,b):
    file = open(f'{a}.txt' ,'a')
    file.write(f'{b}')
    file.close()
def baca(a):
    file = open(f'{a}.txt' ,'r')
    text=file.read()
    print()
    print(text)
    print()
    file.close()  
def tambah (a,b):
    file = open(f'{a}.txt' ,'a')
    file.write(f'''
{b}''')
    file.close()

nama_file=input('File name: ')
i=1
while i==1:
    print('Press <ENTER> to exit')
    jwb=input('Do you want to read or edit file?[R/E]: ')
    if jwb.upper()=='E':
        o=1
        while o==1:
            print('Press <ENTER> to exit')
            rsp=input('Do you want to write or add?[W/A]: ')
            if rsp.upper()=='W':
                isi=input('''input:
''')
                o=0
                tulis(nama_file , isi)
            elif rsp.upper()=='A':
                isi=input('''input:
''')        
                o=0
                tambah(nama_file , isi)
            elif rsp=='':
                o=0
            else:
                print('Invalid response')
    elif jwb.upper() =='R':
        baca(nama_file)
        
    elif jwb=='':
        i=0
    else:
        i=0
print('''
terima kasih telah menggunakan program saya
ig: alfarizqiwira''')