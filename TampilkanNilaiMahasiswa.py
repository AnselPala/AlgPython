JawabUlangProg ="y"
while JawabUlangProg=="y" or JawabUlangProg=="T":
    print("===============================")
    print("=  Tampilkan Nilai Mahasiswa  =")
    print("===============================") 

    n = input(">> Masukkan Nilai = ")
    if int(n)>0 and int(n)<=100:
        if int(n)>91:
            x="A"
        elif int(n)>=81: x="B"
        elif int(n)>=71: x="C"
        else:
            x="D"
        print(x)
        
    else:
            pesan="Masukkan Nilai 1-100 saja"
            print(pesan)

    JawabUlangProg = input(">>> Ulang Program? y/t= ")
    if JawabUlangProg=="t" or JawabUlangProg=="T":
            break