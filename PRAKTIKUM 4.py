from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from matplotlib import pyplot as plt
import pandas as pd

# LIST
listmetode = ['Cash', 'Debit', 'e-Wallet']
# ===> Tambahan
itemdijual = ['sabun cair', 'sabun cuci', 'sampo keratin', 'sikat gigi', 'minuman Dingin', 'makanan ringan', 'mi instan', 'air mineral']
listharga = [200000, 120000, 190000, 180000, 210000, 170000, 110000, 220000]
# ===> Tambahan
waktunow = datetime.now()
formatwaktu = waktunow.strftime('%A, %d %B %Y')

listitemdibeli = []
listharganow = []
listtotalharga = []
listkuantitas = []
listlabel = []

allitem = []
allharga = []
allkuantitas = []
allharganow = []
diskon2 = []

dataitem = pd.read_excel("Data Item Dijual.xlsx")
itemdijual = dataitem['Jenis Item'].tolist()
listharga = dataitem['Harga Satuan'].tolist()
print(dataitem)

# WINDOW
main_window = Tk()
main_window.title('Kasir LOSIK GROCERY')
main_window.withdraw()


# Login
userpass = {'admin' : '123'}
coba = 0
def login():
    global coba
    username1 = inputusername.get()
    password1 = inputpassword.get()
    if username1 in userpass and password1 == userpass[username1]:
        window_login.destroy()
        main_window.deiconify()
    elif coba == 3:
        showwarning(message='Terminated')
        main_window.destroy()
        window_login.destroy()
    else:
        showerror(message='Username / Password salah')
        inputusername.delete(0,END)
        inputpassword.delete(0,END)
    coba += 1

# Input Item
def tambah():
    if not inputitem.get():
        showerror(title='Error', message='Silahkan Masukkan Jenis Item', )
    elif not inputjumlah.get():
        showerror(title='Error', message='Silahkan Masukkan Jumlah Item yang akan dibeli', )
    else:
        if inputitem.get() in listitemdibeli:
            i = 0
            while i < len(listitemdibeli):
                if listitemdibeli[i] == inputitem.get():
                    x = i
                    listtotalharga[x] += (listharga[x]*int(inputjumlah.get()))
                    listkuantitas[x] += int(inputjumlah.get())
                i += 1
        else:
            inputjumlah.get()
            listitemdibeli.append(inputitem.get())
            listkuantitas.append(int(inputjumlah.get()))
            i = 0
            while i < len(itemdijual):
                if itemdijual[i] == inputitem.get():
                    x = i 
                    listharganow.append(listharga[x])
                    listtotalharga.append(listharga[x]*int(inputjumlah.get()))
                i +=1
        inputitem.delete(0,END)
        inputjumlah.delete(0,END)

    # print("Item yang Dibeli")
    # while True:
    #     inputitem = input('Silahkan Masukkan Jenis Item \t\t: ').lower()
    #     inputjumlah = input('Silahkan Masukkan Jumlah Item \t\t: ')

    #     if inputitem in listitemdibeli:
    #         i = 0
    #         while i < len(listitemdibeli):
    #             if listitemdibeli[i] == inputitem:
    #                 x = i
    #                 listtotalharga[x] += (listharga[x]*int(inputjumlah)) 
    #                 listkuantitas[x] += int(inputjumlah)
    #             i += 1
    #     else:
    #         listitemdibeli.append(inputitem)
    #         listkuantitas.append(int(inputjumlah))
    #         i = 0
    #         while i < len(itemdijual):
    #             if itemdijual[i] == inputitem:
    #                 x = i
    #                 listharganow.append(listharga[x])
    #                 listtotalharga.append(listharga[x]*int(inputjumlah))                   
    #             i +=1


# Menampilkan Keranjang
def keranjang():
    global no1, item, quantity, harga, Total
    i= 0
    while i < len(listitemdibeli):
        no1 = Label(framerincian1, text= 1 + i)
        no1.grid(row=i+1, column=0,)

        item = Label(framerincian1, text= listitemdibeli[i])
        item.grid(row=i+1, column=1, )

        quantity = Label(framerincian1, text= listkuantitas[i])
        quantity.grid(row=i+1, column=2, )

        harga = Label(framerincian1, text= 'Rp{:,.2f}'.format(listharganow[i]))
        harga.grid(row=i+1, column=3, )

        Total = Label(framerincian1, text='Rp{:,.2f}'.format(listtotalharga[i]))
        Total.grid(row=i+1, column=4, )

        listlabel.append(no1)
        listlabel.append(item)
        listlabel.append(quantity)
        listlabel.append(harga)
        listlabel.append(Total)

        i += 1

    totalll = Label(framerincian2, text=': Rp. {}'.format(sum(listtotalharga)))
    totalll.grid(column=1, row=0)

    listlabel.append(totalll)

#Pembayaran          
def pembayaran():
    global nilaipembelian, nilaidiskon, nilaitotal, nilaibayar, nilaikembali, tanggalpembelian, totaldiskon
    buttonselesai['state'] = ACTIVE
    buttongrafik['state'] = ACTIVE
    totalbayar = sum(listtotalharga)
    if not inputmetodebayar.get():
        showerror(title='Error', message='Silahkan Pilih Metode Bayar', )
    else :
        if inputmetodebayar.get() != 'Cash':
            if inputmetodebayar.get() == 'Debit':
                totalbayar *= 0.95
                kembalian = 0
            
            elif inputmetodebayar.get() == 'e-Wallet':
                totalbayar *= 0.93
                kembalian = 0
            else:
                pass

            if sum(listtotalharga) >= 500000:
                diskon2 = 20000
                totalbayar -= diskon2
            else:
                diskon2 = 0
            nominalbayar = totalbayar
            
            tanggalpembelian = Label(framenota, text=': {}'.format(formatwaktu))
            tanggalpembelian.grid(row=0, column=1, sticky="w")

            nilaipembelian = Label(framenota, text=': Rp{:,.2f} '.format(sum(listtotalharga)))
            nilaipembelian.grid(row=2,column=1, sticky= "w")
            
            totaldiskon = sum(listtotalharga) - totalbayar
            nilaidiskon = Label(framenota, text=': Rp{:,.2f} (%{} +Rp.{:,.2f} '.format(totaldiskon, inputmetodebayar.get(), diskon2))
            nilaidiskon.grid(row=3,column=1, sticky='w')

            nilaitotal = Label(framenota, text=': Rp{:,.2f}'.format(totalbayar))
            nilaitotal.grid(row=4,column=1, sticky='w')

            nilaibayar = Label(framenota, text=': Rp{:,.2f}'.format(nominalbayar))
            nilaibayar.grid(row=5,column=1, sticky='w')

            nilaikembali = Label(framenota, text=': Rp{:,.2f}'.format(kembalian))
            nilaikembali.grid(row=6,column=1, sticky='w')
        
        # elif input('Masukkan Metode Pembayaran : ') == 'Cash':
        elif inputmetodebayar.get() == 'Cash':
            totalbayar = (sum(listtotalharga))
        if sum(listtotalharga) >= 500000:
            diskon2 = 20000
            totalbayar -= diskon2
        else:
            diskon2 = 0
            
        def bayarcash():
            if int(inputbayar2.get()) < totalbayar:
                showinfo(message='Jumlah Pembayaran kurang dari Total Pembelian')
            else:
                global nilaipembelian, nilaidiskon, nilaitotal, nilaibayar, nilaikembali, tanggalpembelian
                nominalbayar = int(inputbayar2.get())
                totaldiskon = sum(listtotalharga) - totalbayar
                kembalian = nominalbayar - totalbayar

                tanggalpembelian = Label(framenota, text=': {}'.format(formatwaktu))
                tanggalpembelian.grid(row=0, column=1, sticky="w")

                nilaipembelian = Label(framenota, text=': Rp{:,.2f} '.format(sum(listtotalharga)))
                nilaipembelian.grid(row=2, column=1, sticky="w")

                nilaidiskon = Label(framenota, text=': Rp{:,.2f}'.format(totaldiskon))
                nilaidiskon.grid(row=3, column=1, sticky='w')

                nilaitotal = Label(framenota, text=': Rp{:,.2f}'.format(totalbayar))
                nilaitotal.grid(row=4, column=1, sticky='w')

                nilaibayar = Label(framenota, text=': Rp{:,.2f}'.format(int(nominalbayar)))
                nilaibayar.grid(row=5, column=1, sticky='w')

                nilaikembali = Label(framenota, text=': Rp{:,.2f}'.format(kembalian))
                nilaikembali.grid(row=6, column=1, sticky='w')

                window.destroy()

            
            
        window = Toplevel()
        window.geometry('250x250')

        frame1 = Frame(window)
        frame1.pack(padx=25, pady=25)
            
        totalakhir2 = Label(frame1, text='Total Harga', padx= 10)
        totalakhir2.grid(row=0, column=0, sticky="w")

        showtotalakhir2 = Label(frame1, text= ': Rp{:,.2f}'.format(totalbayar))
        showtotalakhir2.grid(row=0, column=1, sticky="w")

        bayar2 = Label(frame1, text='Bayar Cash', padx= 10)
        bayar2.grid(row=1, column=0, sticky="w")

        inputbayar2 = Spinbox(frame1, from_=0, to=10**10)
        inputbayar2.grid(row=1, column=1, pady=10, sticky="w", padx=10)

        buttonbayar2 = Button(frame1, text='BAYAR', bg='#7ED957', command=lambda: [bayarcash()])
        buttonbayar2.grid(row=2, column=0, columnspan=2)
    
    buttoninput['state'] = DISABLED
    buttonpay['state'] = DISABLED

def rekap():
    if not inputitem.get():
        pass
    elif not inputjumlah.get():
        pass
    else:
        if inputitem.get() in allitem:
            i = 0
            while i < len(allitem):
                if allitem[i] == inputitem.get():
                    x = i
                    allharga[x] += (listharga[x]*int(inputjumlah.get())) 
                   
                    allkuantitas[x] += int(inputjumlah.get())
                i += 1
        else:            
            inputjumlah.get()
            allitem.append(inputitem.get())
            allkuantitas.append(int(inputjumlah.get()))
            i = 0
            while i < len(itemdijual):
                if itemdijual[i] == inputitem.get():
                    x = i 
                    allharganow.append(listharga[x])
                    allharga.append(listharga[x]*int(inputjumlah.get()))                   
                i +=1

def selesai():
    # Pandas
    data = {'Jenis Item':listitemdibeli,
            'Harga Satuan': listharganow,
            'Kuantitas': listkuantitas,
            'Harga Total':listtotalharga}
    # #Membuat Dataframe dari data diatas
    df = pd.DataFrame(data)
    #append data ke Excel
    df.to_excel("Rekapitulasi Pembelian di LOSIK Grocery.xlsx", index=False, header=False)
    
    # Reset Window
    for i in listlabel:
        i.destroy()

    listitemdibeli.clear()
    listtotalharga.clear()
    listharganow.clear()
    listkuantitas.clear()

    nilaipembelian.destroy()
    nilaidiskon.destroy()
    nilaitotal.destroy() 
    nilaibayar.destroy() 
    nilaikembali.destroy()
    tanggalpembelian.destroy()

    inputmetodebayar.delete(0,END)

    buttoninput['state'] = ACTIVE
    buttonpay['state'] = ACTIVE
    buttonselesai['state'] = DISABLED
    inputitem.current(0)
    inputmetodebayar.current(0)

def grafik():
    plt.pie(allharga,
    labels=allitem,
    autopct='%1.1f%%')
    plt.title('Grafik Proporsi Penjualan Jenis Item')
    plt.xlabel('Total Penjualan : {}'.format(int(sum(allharga) - totaldiskon)))
    plt.legend()
    plt.show()


# FRAME
# ===> Tambahan
frame = Frame(main_window)
frame.pack()
frameitem = LabelFrame(frame, padx=10)
frameitem.grid(row=0, column=0, padx=20, pady=5)
# ===> Tambahan

framerincian = LabelFrame(frame)
framerincian.grid(row=1, column=0, sticky='news', padx=20, pady=5)

framerincian1 = LabelFrame(framerincian)
framerincian1.grid(row=0, column=0, sticky='news')

framerincian2 = LabelFrame(framerincian)
framerincian2.grid(row=1, column=0, sticky='news')

framebayar = LabelFrame(frame, pady= 5,  padx=10)
framebayar.grid(row=2, column=0 ,sticky='news', padx=20, pady=5)

framenota = LabelFrame(frame,  padx=10)
framenota.grid(row=3, column=0,sticky='news', padx=20, pady=5)

frameselesai = LabelFrame(frame)
frameselesai.grid(row=4, column=0,sticky='news', padx=20, pady=5)
frameselesai.grid_columnconfigure(1,weight=1)

framegrafik = LabelFrame(frame)
framegrafik.grid(row=5, column=0,sticky='news', padx=20, pady=5)
framegrafik.grid_columnconfigure(1,weight=1)

# WIDGET
jumlahitem = Label(frameitem, text='Jumlah Item')
jumlahitem.grid(row=1, column=0, sticky="w")

# ===> Tambahan
inputitem = ttk.Combobox(frameitem, values= itemdijual)
inputitem.current(0)
inputitem.grid(row=0, column=1, sticky="w", pady=10, padx=10)

jumlahitem = Label(frameitem, text='Jumlah Item')
jumlahitem.grid(row=1, column=0, sticky="w")

inputjumlah = Spinbox(frameitem, from_=1, to=100)

inputjumlah.grid(row=1, column=1, sticky="w", pady=10, padx=10)

buttoninput = Button(frameitem, text='Input',command= lambda:[rekap(),tambah(), keranjang(),], bg='#7ED957', padx=20, pady=2.5, )
buttoninput.grid(row=0, column=2, rowspan=2, padx=25)
# ===> Tambahan

no = Label(framerincian1, text='No')
no.grid(row=0, column=0)

item = Label(framerincian1, text='Jenis Item')
item.grid(row=0, column=1)

quantity = Label(framerincian1, text='Quantity')
quantity.grid(row=0, column=2)

harga = Label(framerincian1, text='Harga')
harga.grid(row=0, column=3)

Total = Label(framerincian1, text='Total')
Total.grid(row=0, column=4)

totall = Label(framerincian2, text='Total Belanja')
totall.grid(column=0,row=0)

# ===> Tambahan
for i in framerincian1.winfo_children():
    i.grid_configure(padx= 17.5, pady=2)
# ===> Tambahan

metodebayar = Label(framebayar, text='Metode Pembayaran')
metodebayar.grid(row=0, column=0, sticky="w")

inputmetodebayar = ttk.Combobox(framebayar, values= listmetode)
inputmetodebayar.current(0)
inputmetodebayar.grid(row=0,column=1, sticky="w", pady=10, padx=10)

buttonpay = Button(framebayar, text= 'Bayar', padx=10, bg='#7ED957', command= lambda: [pembayaran()])
buttonpay.grid(row=1, column=0, columnspan= 2)

tanggal = Label(framenota, text='Tanggal Pembelian')
tanggal.grid(row=0, column=0, sticky="w")

rincian1 = Label(framenota, text='Rincian: ')
rincian1.grid(row=1, column=0, sticky="w")

pembelian = Label(framenota, text='1. Total Pembelian')
pembelian.grid(row=2, column=0, sticky="w")

diskon = Label(framenota, text='2. Total Diskon')
diskon.grid(row=3, column=0, sticky="w")

totalakhir = Label(framenota, text='3. Total Harga')
totalakhir.grid(row=4, column=0, sticky="w")

bayar = Label(framenota, text='Total Pembayaran')
bayar.grid(row=5, column=0, sticky="w")

kembali = Label(framenota, text='Total Kembalian')
kembali.grid(row=6, column=0, sticky="w")

buttonselesai = Button(frameselesai, text= 'SELESAI', padx=10, bg='#6297FF',command=selesai )
buttonselesai.grid(row=0,column=0, sticky='news', columnspan=4)
buttonselesai['state'] = DISABLED

buttongrafik = Button(framegrafik, text= 'Tampilkan Grafik', padx=10, bg='#6297FF',command=grafik )
buttongrafik.grid(row=0,column=0, sticky='news', columnspan=4)
buttongrafik['state'] = DISABLED

#Login
window_login= Toplevel()
window_login.title('Login LOSIK')
window_login.geometry("250x250")

framelogin = Frame(window_login)
framelogin.pack(padx=10, fill='x')

dashboardlogin = Label(
    framelogin,
    text="SILAHKAN LOGIN",
    font=('Algerian', 15, 'bold')
)
dashboardlogin.grid(row=0, column=0, columnspan=2)

username = Label(framelogin, text='Username')
username.grid(row=1, column=0, sticky="w")

inputusername = Entry(framelogin)
inputusername.grid(row=1, column=1, padx= 20, pady=10)

password = Label(framelogin, text='Password')
password.grid(row=2,column=0, sticky="w")

inputpassword = Entry(framelogin, show='*')
inputpassword.grid(row=2,column=1)

buttonlogin= Button(framelogin, text='Login', command= lambda: login())
buttonlogin.grid(row=3,column=1,columnspan=2, sticky='we',padx=10,pady=10)

# # END OF WINDOW
main_window.mainloop()