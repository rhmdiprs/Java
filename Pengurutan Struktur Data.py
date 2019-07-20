
# coding: utf-8

# In[2]:


list=[] #deklarasi list sebagai array

def swap(a,b):
    list[a],list[b]=list[b],list[a]

def awal():

    print ("Rahmad Ady")
    print ("18364007")
    print ("Program Sorting \n")
    print ("Menu Pilihan")
    print ("1. Create Program")
    print ("2. Exit")
    
    data=input ("masukan pilihan :")
    if data=='1':
        array()
    elif data=='2':
        exit()


def array():
    jumlah= int(input("\nBanyak Data : "))
    awal=0
    while (awal<jumlah): 
        awal=awal+1
        bil=input("input data ke-%d:"%awal)
        list.append(bil) 
    print ("data acak =", list)
    pilih(jumlah)
    
def pilih(jumlah):   
    print ("\nPilih Jenis Sorting :")
    print ("1) Bubble sort")
    choice=input("Pilihan =")
    tipe(choice,jumlah)
    
def tipe(pilih,jumlah):
    print ("\n1) Ascending")
    print ("2) Descending")
    p=input("Tipe yang dipilih :")
    if pilih=='1':
        bubble(p,jumlah)
    elif pilih=='2':
        quick(p,jumlah)
    elif pilih=='3':
        select(p,jumlah)
    elif pilih=='4':
        insert(p,jumlah)
    elif pilih=='5':
        exchange(p,jumlah)

def bubble(p,jumlah):  
    for a in range(0,jumlah):
            for b in range(1,jumlah):
                if p=='1':
                   if list[b]<list[b-1]:
                       swap(b,b-1)
                else:
                    if list[b]>list[b-1]:
                         swap(b,b-1)
    print (list)


awal()

