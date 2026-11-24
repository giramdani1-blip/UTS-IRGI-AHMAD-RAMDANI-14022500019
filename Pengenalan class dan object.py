class Yamaha:
    pass

class Redbull:
    pass

Fabio_Quartararo = Yamaha()
Alex_Rins = Yamaha()

print(type(Fabio_Quartararo))
print(type(Alex_Rins))

Pedro_Acosta = Redbull()
Brad_Binder = Redbull()

print(type(Pedro_Acosta))
print(type(Brad_Binder))

Fabio_Quartararo = Yamaha()
Fabio_Quartararo.nama = "Fabio Quartararo"
Fabio_Quartararo.nopunggung = 20
Fabio_Quartararo.motor = "Yamaha YZR-M1"

print(Fabio_Quartararo.nama)
print(Fabio_Quartararo.nopunggung)
print(Fabio_Quartararo.motor)

Alex_Rins = Yamaha()
Alex_Rins.nama = "Alex Rins"
Alex_Rins.nopunggung = 42
Alex_Rins.motor = "Yamaha YZR-M1"

print(Alex_Rins.nama)
print(Alex_Rins.nopunggung)
print(Alex_Rins.motor)
