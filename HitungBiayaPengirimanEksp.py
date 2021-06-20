import os
clear = lambda : os.system('cls')
jwb = 'y'
while jwb == 'y' or jwb == 'Y' :
    clear()
    print("======================================================")
    print("=                TRANSAKSI EKSPEDISI                 =")
    print("======================================================")

    print('KODE TUJUAN')
    print("======================================================")
    print('Kode = A. Suarabaya')
    print('Kode = B. Bandung')
    print("=======================================================")
    
    kota = ['surabaya','Bandung']
    Jarak = [169,452]
    OngkirPerKM = [2500,4000]   

    Pilihan = input("Masukan Kode Tujuan = ")  
    if Pilihan == 'A':
        idx = 0
    elif pilihan == 'B':
        idx = 1
    else:
        idx = 0

    print('>>> Pilihan Tujuan             = ' + kota[idx])
    print('>>> Jarak                      = ' + str(Jarak)[idx] + 'KM')
    print('>>> Ongkir Per KM              =Rp. ' + str(OngkirPerKM))

    fixJarak  = Jarak[idx]
    fixOngkir = OngkirPerKM[idx]
    TotOngKir = fixJarak*OngkirPerKM

    print('=============================================')
    print('>>> Total Biaya     =Rp. ' + TotOngKir)
    jwb = input('Apakah Lanjut? (y/t) : ')
    if jwb == 't' or jwb == 'T':
        break