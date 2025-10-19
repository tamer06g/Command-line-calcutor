def hesap_makinesi():
    print("===Bu Hesap Makinesi")
    print("İşlemler: +  -  *  /")


    while True: 
        sayı1=input("lütfen sayı giriniz(q basıp cıkın):")  

        if sayı1.lower()=="q":       
            print("program sonlanıyor")
            break

        sayı2=input("2.sayı giriniz:")     
        islem=input("işlemi giriniz(*,/,+,-):")    

        try:        
            sayı1=int(sayı1)
            sayı2=int(sayı2)
        except:
            print("Lütfen sayı giriniz")
            continue
        
        

        if islem=="+":     
            sonuc=sayı1+sayı2
        
        elif islem=="-":
            sonuc=sayı1-sayı2
        elif islem=="/":
            if sayı1==0:
                print("sıfıra bölme hatası")
                continue
            sonuc=sayı1/sayı2
        elif islem=="*":
            sonuc=sayı1*sayı2

        else:
            print("geçersiz işlem")
            continue

        

        
        print(f"Sonuç: {sonuc}\n")




hesap_makinesi()







        





