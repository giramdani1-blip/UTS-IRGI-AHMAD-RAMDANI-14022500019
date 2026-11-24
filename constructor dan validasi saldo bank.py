class Bankaccount:
    no = 0
    saldo = ""
    aktif = True

    def __init__(self, no, saldo=0):
        if saldo < 0:
            raise ValueError("Gagal")

        self.no = no
        self.saldo = saldo


budi = Bankaccount(13579, 1000)

print(budi.no)
print(budi.saldo)
