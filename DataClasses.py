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

class PlotLine:
    def __init__(self, firstPoint: DataPoint, secondPoint: DataPoint):
        self.firstPeriod = firstPoint.period
        self.firstValue = firstPoint.value
        self.secondPeriod = secondPoint.period
        self.secondValue = secondPoint.value
        if self.firstValue > self.secondValue:
            self.color = 'green'
        else:
            self.color = 'red'

def convertData(data: DataPoint) -> PlotLine:
    result = []
    for i, point in enumerate(data):
        if i == 0:
            continue
        else:
            result.append(PlotLine(data[i - 1], point))
    return result