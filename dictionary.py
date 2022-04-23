class dictionary:
    def __init__(self, maxCount=10):
        super().__init__()
        self.dictionaryKeeper = []
        self.maxCount = maxCount

    def Find(self, ip):
        counter = 0
        for row in self.dictionaryKeeper:
            if ip == row[0]:
                return counter
            counter += 1
        return -1

    def Add(self, ip, type):
        if type == 1:
            self.dictionaryKeeper.append([ip, 1])
            return 1
        else:
            self.dictionaryKeeper.append([ip, 0])
            return 0

    def SetProbability(self, ip, type):
        currentIndex = self.Find(ip)
        if currentIndex != -1:
            currentCount = self.dictionaryKeeper[currentIndex][1]
            if currentCount < self.maxCount and type == 1:
                self.dictionaryKeeper[currentIndex][1] += 1
            elif currentCount > 0 and type == 0:
                self.dictionaryKeeper[currentIndex][1] -= 1

            return self.dictionaryKeeper[currentIndex][1]
        else:
            return self.Add(ip, type)

    def GetProbabilityByIp(self, ip):
        return self.Find(ip)

    def GetProbabilityByIndex(self, index):
        return self.dictionaryKeeper[index]

    def GetProbabilityAll(self):
        return self.dictionaryKeeper
