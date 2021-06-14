JwbUlangProg = "y"
while JwbUlangProg=="y" or JwbUlangProg=="Y":
    print("=======================")
    print("=    Cek Kelulusan    =")
    print("=======================")
    
    n = input(">> Masukkan Nilai = ")
    if int(n)>0 and int(n)<=100:
        if int(n)>60:
            sts="LULUS"
        else:
            sts="ULANG"

        print(sts)
    else:
        pesan="Masukkan standar peniaian 1-100 saja"
        print(pesan)

    JwbUlangProg = input(">>> Ulang Program? y/t= ")
    if JwbUlangProg=="t" or JwbUlangProg=="T":
        break