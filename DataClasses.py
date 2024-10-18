class DataPoint:
    def __init__(self, element):
        self.value = element['wartosc']
        self.period = element['id-okres']
        self.year = element['id-daty']
    def calculateDate(self):
        self.period = (self.period - 7) % 12
        self.period = self.period + 1
    def normalizeValue(self):
        self.value -= 100