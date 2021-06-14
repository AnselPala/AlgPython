JawabUlangProg ="y"
while JawabUlangProg=="y" or JwbUlangProg=="T":
    print("===========================")
    print("=    Cek Golongan Usia    =")
    print("===========================") 

    u = input(">> Masukkan Umur = ")
    if int(u)>0 and int(u)<=100:
        if int(u)>60:
            sts="LANSIA"
        elif int(u)>=35: sts="DEWASA"
        elif int(u)>=18: sts="PEMUDA"
        elif int(u)>=15: sts="REMAJA"
        else:
            sts="ANAK - ANAK"

        print(sts)
        
    else:
            pesan="Masukkan Nilai 1-100 saja"
            print(pesan)

    JawabUlangProg = input(">>> Ulang Program? y/t= ")
    if JawabUlangProg=="t" or JawabUlangProg=="T":
            break