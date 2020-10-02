class txtFiles:
    def __init__(self, ccList, incList):
        self.__ccList = ccList
        self.__incList = incList
        self.__path = "./Project_1/python/output/txt_files/"

    def createTXTfiles(self):
        self.incTypes()
        self.expCostCentre()

    # exporting the cost centres as a txt file
    def expCostCentre(self):

        with open(
            "./Project_1/python/output/txt_files/costCentres.txt", "tw"
        ) as costCentres:
            # creating the file heading
            heading = "Cost Centre"
            costCentres.write(heading + "\n")
            costCentres.write(str((len(heading) + 10) * "-") + "\n")

            # generating the data
            for cc in self.__ccList:
                costCentres.write(cc + "\n")

    def incTypes(self):
        with open(self.__path + "incomeTypes.txt", "tw") as incomeTypes:
            # creating the file heading
            heading = "Income type"
            incomeTypes.write(heading + "\n")
            incomeTypes.write(str((len(heading) + 10) * "-") + "\n")

            for inc in self.__incList:
                incomeTypes.write(inc + "\n")

