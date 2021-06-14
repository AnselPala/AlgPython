JawabUlangProg ="y"
while JawabUlangProg=="y" or JawabUlangProg=="T":
    print("===========================")
    print("=  Tampilkan Nilai Huruf   =")
    print("===========================") 

    u = input(">> Masukkan Umur = ")
    if int(u)>0 and int(u)<=100:
        if int(u)>80:
            sts="BAIK SEKALI"
        elif int(u)>=65: sts="BAIK"
        elif int(u)>=55: sts="CUKUP"
        elif int(u)>=40: sts="KURANG"
        else:
            sts="KURANG SEKALI"
        print(sts)
        
    else:
            pesan="Masukkan Nilai 1-100 saja"
            print(pesan)

    JawabUlangProg = input(">>> Ulang Program? y/t= ")
    if JawabUlangProg=="t" or JawabUlangProg=="T":
            break