import os
clear = lambda : os.system('cls')

jwbulangProg = "y"
while jwbulangProg == "y" or jwbulangProg == "Y" :
    clear()
    print("===============================================") 
    print("=  Program Hitung Transaksi Printer dan Infus =")
    print("===============================================")   
    hrgPrinter = 660000
    diskon = 0.15   
    qty = input("Masukkan Quantity = ")
    jmlhPrt = int(qty)
    totHrg = jmlhPrt * hrgPrinter

    if totHrg > 1500000 :
        totDiskon = diskon * totHrg
        totBy = totHrg - totDiskon
        print()
        print("Diskon 15%")
        print("Total Harga  = Rp.",format(totHrg,',.2f'))
        print("Total Diskon = Rp.",format(totDiskon,',.2f'))
        print("Total Biaya  = Rp.",format(totBy,',.2f')) 
    else :
        totBy = totHrg
        print()
        print("Total Biaya = Rp.",format(totBy,',.2f'))  
    print() 
    jwbulangProg = input("Cek Lagi? (y/t) = ")
    if jwbulangProg == "t" or jwbulangProg == "T" :
        break