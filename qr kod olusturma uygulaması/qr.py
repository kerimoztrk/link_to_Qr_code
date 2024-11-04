import tkinter as tk

from tkinter import filedialog

import pyqrcode 

from pyqrcode import QRCode

#temel kodlar
def qrKoduOlustur():
    url = urlGirdi.get()

    if url:
        qrUrl= pyqrcode.create(url)
        dosyaYolu=filedialog.asksaveasfilename(defaultextension=".svg",filetypes=[("SVG dosyaları","*.svg")])

        if dosyaYolu:
            qrUrl.svg(dosyaYolu, scale=8)
            durumEtiketi.config(text="QR kodu oluşturuldu ve kaydedildi.")

#tasarım

uygulamaPencere=tk.Tk()
uygulamaPencere.title("QR kodu oluşturucu")

etiket=tk.Label(uygulamaPencere,text="URL GİRİNİZ")
urlGirdi=tk.Entry(uygulamaPencere,width=40)
qrKoduOlusturButonu=tk.Button(uygulamaPencere,text="QR kodu oluştur",command=qrKoduOlustur)
durumEtiketi=tk.Label(uygulamaPencere,text="")

etiket.grid(row=0,column=0,padx=10,pady=10)
urlGirdi.grid(row=0,column=1,padx=10,pady=10)
qrKoduOlusturButonu.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
durumEtiketi.grid(row=2,column=0,columnspan=2,padx=10,pady=10)



uygulamaPencere.mainloop()