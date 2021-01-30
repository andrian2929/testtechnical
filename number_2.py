def myfunction(huruf, kalimat):
    counter=0
    for i in kalimat:
        if huruf ==i:
             counter = counter+1
    return counter    

kalimat = input('Masukkan kalimat')
huruf = input('Masukkan huruf yang dicari')

print(myfunction(huruf, kalimat))
            
