class Company(object):
    pkg = 0
    totalTransDist = 0
    facCount = 0
    hourlyFacEmm = 0
    nonrenPerc = 0
    yearlyIndProfit = 0
    yearlyIndWaste = 0
    avgStockPrice = 0
    avgWorkerCount = 0
    avgWorkArea = 0

    def __init__(self, pkg, totalTransDist, facCount, hourlyFacEmm, nonrenPerc, yearlyIndProfit, yearlyIndWaste, avgStockPrice, avgWorkerCount, avgWorkArea):
        self.pkg = pkg

        # Environment
        self.totalTransDist = totalTransDist
        self.facCount = facCount
        self.hourlyFacEmm = hourlyFacEmm
        self.nonrenPerc = nonrenPerc

        # Economy
        self.yearlyIndProfit = yearlyIndProfit
        self.yearlyIndWaste = yearlyIndWaste
        self.avgStockPrice = avgStockPrice

        # Social
        self.avgWorkerCount = avgWorkerCount
        self.avgWorkArea = avgWorkArea

    def getScore(self):
        score = 0

        if 0 <= self.totalTransDist <= 50:
            if self.pkg == 2: print("{} (total weekly freight transport distance) is good!".format(self.totalTransDist))
            score += 1
        elif 51 <= self.totalTransDist <= 100:
            if self.pkg == 2: print("{} (total weekly freight transport distance) should be reduced by {}.".format(self.totalTransDist, self.totalTransDist - 50))
            score += 2
        elif 101 <= self.totalTransDist <= 150:
            if self.pkg == 2: print("{} (total weekly freight transport distance) should be reduced by {}.".format(self.totalTransDist, self.totalTransDist - 50))
            score += 3
        elif 151 <= self.totalTransDist <= 200:
            if self.pkg == 2: print("{} (total weekly freight transport distance) should be reduced by {}.".format(self.totalTransDist, self.totalTransDist - 50))
            score += 4
        else:
            if pkg == 2: print("{} (total weekly freight transport distance) should be reduced by {}.".format(self.totalTransDist, self.totalTransDist - 50))
            score += 5

        totalHourlyFacEmm = self.facCount * self.hourlyFacEmm
        # 200 = facCount * hourlyFacEmm
        # facCount - 200 / hourlyFacEmm
        # hourlyFacEmm - 200 / facCount
        if 0 <= totalHourlyFacEmm <= 4000:
            if self.pkg == 2: print("{} (total hourly factory emmissions) are good!".format(totalHourlyFacEmm))
            score += 1
        elif 100001 <= totalHourlyFacEmm <= 8000:
            if self.pkg == 2: print("{} (number of factories) should be reduced by {} or {} (hourly factory emmissions) should be reduced by {}".format(self.facCount, self.facCount - 4000 / self.hourlyFacEmm, self.hourlyFacEmm, self.hourlyFacEmm - 4000 / self.facCount))
            score += 2
        elif 200001 <= totalHourlyFacEmm <= 12000:
            if self.pkg == 2: print("{} (number of factories) should be reduced by {} or {} (hourly factory emmissions) should be reduced by {}".format(self.facCount, self.facCount - 4000 / self.hourlyFacEmm, self.hourlyFacEmm, self.hourlyFacEmm - 4000 / self.facCount))
            score += 3
        elif 300001 <= totalHourlyFacEmm <= 16000:
            if self.pkg == 2: print("{} (number of factories) should be reduced by {} or {} (hourly factory emmissions) should be reduced by {}".format(self.facCount, self.facCount - 4000 / self.hourlyFacEmm, self.hourlyFacEmm, self.hourlyFacEmm - 4000 / self.facCount))
            score += 4  
        else:
            if self.pkg == 2: print("{} (number of factories) should be reduced by {} or {} (hourly factory emmissions) should be reduced by {}".format(self.facCount, self.facCount - 4000 / self.hourlyFacEmm, self.hourlyFacEmm, self.hourlyFacEmm - 4000 / self.facCount))
            score += 5
        
        if 0 <= self.nonrenPerc <= 20:
            if self.pkg == 2: print("{} (percentage of energy that's non-renewable) is good!".format(nonrenPerc))
            score += 1
        elif 21 <= self.nonrenPerc <= 40:
            if self.pkg == 2: print("{} (percentage of energy that's non-renewable) should be reduced by {}.".format(self.nonrenPerc, self.nonrenPerc - 20))
            score += 2
        elif 41 <= self.nonrenPerc <= 60:
            if self.pkg == 2: print("{} (percentage of energy that's non-renewable) should be reduced by {}.".format(self.nonrenPerc, self.nonrenPerc - 20))
            score += 3
        elif 61 <= self.nonrenPerc <= 80:
            if self.pkg == 2: print("{} (percentage of energy that's non-renewable) should be reduced by {}.".format(self.nonrenPerc, self.nonrenPerc - 20))
            score += 4
        else:
            if self.pkg == 2: print("{} (percentage of energy that's non-renewable) should be reduced by {}.".format(self.nonrenPerc, self.nonrenPerc - 20))
            score += 5

        profWasteRatio = self.yearlyIndProfit / self.yearlyIndWaste
        # 401 = yearlyIndProfit / yearlyIndWaste
        # 401 * yearlyIndProfit = yearlyIndWaste
        # yearlyIndWaste - 401 * yearlyIndProfit
        if 401 <= profWasteRatio <= 500:
            if self.pkg == 2: print("{} (yearly waste in kg) should be reduced by {}".format(self.yearlyIndWaste, self.yearlyIndWaste - 101 * self.yearlyIndProfit))
            score += 5
        elif 301 <= profWasteRatio <= 400:
            if self.pkg == 2: print("{} (yearly waste in kg) should be reduced by {}".format(self.yearlyIndWaste, self.yearlyIndWaste - 101 * self.yearlyIndProfit))
            score += 4
        elif 201 <= profWasteRatio <= 300:
            if self.pkg == 2: print("{} (yearly waste in kg) should be reduced by {}".format(self.yearlyIndWaste, self.yearlyIndWaste - 101 * self.yearlyIndProfit))
            score += 3
        elif 101 <= profWasteRatio <= 200:
            if self.pkg == 2: print("{} (yearly waste in kg) should be reduced by {}".format(self.yearlyIndWaste, self.yearlyIndWaste - 101 * self.yearlyIndProfit))
            score += 2
        else:
            if self.pkg == 2: print("{} (yearly profit to yearly waste [in kg] ratio) is good!".format(profWasteRatio))
            score += 1
        
        revenueStockRatio = self.yearlyIndProfit / self.avgStockPrice
        if 0 <= revenueStockRatio <= 1000000:
            if self.pkg == 2: print("{} (stock price ) is unhealthy for a yearly profit of {}".format(self.avgStockPrice, self.yearlyIndProfit))
            score += 5
        elif 1000001 <= revenueStockRatio <= 2000000:
            if self.pkg == 2: print("{} (stock price ) is unhealthy for a yearly profit of {}".format(self.avgStockPrice, self.yearlyIndProfit))
            score += 4
        elif 2000001 <= revenueStockRatio <= 3000000:
            if self.pkg == 2: print("{} (stock price ) is unhealthy for a yearly profit of {}".format(self.avgStockPrice, self.yearlyIndProfit))
            score += 3
        elif 3000001 <= revenueStockRatio <= 4000000:
            if self.pkg == 2: print("{} (stock price ) is unhealthy for a yearly profit of {}".format(self.avgStockPrice, self.yearlyIndProfit))
            score += 2
        elif 4000001 <= revenueStockRatio <= 5000000:
            if self.pkg == 2: print("{} (stock price to yearly revenue ratio) is good!".format(revenueStockRatio))
            score += 1

        workplaceDensity = self.avgWorkArea / self.avgWorkerCount
        # 13 * avgWorkerCount - avgWorkArea
        if 0 <= workplaceDensity <= 3:
            if self.pkg == 2: print("{} (average cubicle/workplace area) should be increased by {} to accomidate for {} workers.".format(self.avgWorkArea,13 * avgWorkerCount - avgWorkArea, self.avgWorkerCount))
            score += 5
        elif 4 <= workplaceDensity <= 6:
            if self.pkg == 2: print("{} (average cubicle/workplace area) should be increased by {} to accomidate for {} workers.".format(self.avgWorkArea,13 * avgWorkerCount - avgWorkArea, self.avgWorkerCount))
            score += 4
        elif 7 <= workplaceDensity <= 9:
            if self.pkg == 2: print("{} (average cubicle/workplace area) should be increased by {} to accomidate for {} workers.".format(self.avgWorkArea,13 * avgWorkerCount - avgWorkArea, self.avgWorkerCount))
            score += 3
        elif 10 <= workplaceDensity <= 12:
            if self.pkg == 2: print("{} (average cubicle/workplace area) should be increased by {} to accomidate for {} workers.".format(self.avgWorkArea,13 * avgWorkerCount - avgWorkArea, self.avgWorkerCount))
            score += 2
        else:
            if self.pkg == 2: print("{} (average workplace density) is good!".format(workplaceDensity))
            score += 1
        
        return score

apple = Company(2, 100, 4, 3000, 90, 500000, 10000, 15, 100, 6000)
samsung = Company(2, 150, 5, 3500, 100, 490000, 15000, 10, 90, 5000)
print("Your company has a Zoom-score of {}. (6 is the best possible score.)".format(apple.getScore()))
# pkg
# totalTransDist
# facCount
# hourlyFacEmm
# nonrenPerc
# yearlyIndProfit
# yearlyIndWaste
# avgStockPrice
# avgWorkerCount
# avgWorkArea