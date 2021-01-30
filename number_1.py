tipe_rumah = input('Masukkan tipe rumah : ')
lama_kredit = int(input('Masukkan lama kredit : '))

if tipe_rumah == "Rose":
    harga = 120000000
elif tipe_rumah == "Gold":
    harga = 300000000
elif tipe_rumah == "Platinum":
    harga = 360000000
else:
    print('Tipe rumah tidak tersedia')

uang_muka = harga * (20/100)
sisa = harga - uang_muka
angsuran = sisa/lama_kredit

print('Tipe Rumah : ' + tipe_rumah)
print('Harga Rumah :' + str(harga))
print('Uang Muka : ' + str(uang_muka))
print('Sisa : ' + str(sisa))
print('Lama Kredit :' + str(lama_kredit))
print('Angsuran :' + str(angsuran))
