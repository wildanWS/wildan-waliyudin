class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.pintu = 'tertutup'
        self.mesin = 'mati'

    def bukaPintu(self):
            if self.pintu == 'tertutup':
                print('pintu berhasil dibuka')
                self.pintu = 'terbuka'
            else:
                print('pintu telah terbuka')
    def tutupPintu(self):
            if self.pintu == 'terbuka':
                print('pintu berhasil ditutup')
                self.pintu = 'tertutup'
            else:
                print('pintu telah tertutup')

    def nyalakanMobil(self):
            if self.mesin == 'mati':
                print('mobil berhasil dinyalakan')
                self.mesin = 'hidup'
            else:
                print('mobil berhasil dinyalakan')
        
    def matikanMobil(self):
            if self.mesin == 'hidup':
                print('mobil berhasil dimatikan')
                self.mesin = 'mati'
            else:
                print('mobil berhasil dimatikan')

car1 = Car('honda', 2045)
car1.bukaPintu()
car1.bukaPintu()
car1.tutupPintu()
car1.bukaPintu()
car1.tutupPintu()
print('')
car1.nyalakanMobil()
car1.nyalakanMobil()
car1.matikanMobil()
car1.nyalakanMobil()
car1.matikanMobil()
car1.nyalakanMobil()
print('')




    