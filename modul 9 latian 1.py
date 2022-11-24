# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 14:14:16 2022

@author: fariz
"""

def tulis(a,b,c,d,e):
    file = open('Biodata.txt' ,'w')
    file.write(f'''
Nama: {a}
Umur: {b}
Alamat: {c}
Email: {d}
Dosen wali: {e} ''')
    file.close()

def baca():
    file = open('Biodata.txt' ,'r')
    text=file.read()
    print(text)
    file.close()


nama=input('siapa nama mu? ')
umur=input('berapa umur mu? ')
alm=input('dimana alamat mu? ')
ema=input('apa email mu? ')
dsn=input('siapa dosen wali mu? ')
tulis(nama, umur, alm, ema, dsn)
baca()