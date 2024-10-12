#continue bu deyim kendinden sonra gelen hiçbir işlemi yapmadan döngünün en başına geçer
#klavyeden sayı girilcek en fazla 3 basamakla olcak fazla olursa hata mesajı iptal yazıldığında program sonalncak

while True:
    s=input("bir sayı gir")
    if (s=="iptal"):
      break
    if(len(s)<=3):
        continue
    print("en fazla 3 karakter giriliebilir")