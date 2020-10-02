class txtFiles:
    def __init__(self, ccList):
        self.__ccList = ccList

    def createTXTfiles(self):
        self.expCostCentre()

    # exporting the cost centres as a txt file
    def expCostCentre(self):

        # costCentres = open("./Project_1/python/output/txt_files/costCentre.txt", "tx")

        with open(
            "./Project_1/python/output/txt_files/costCentre.txt", "tw"
        ) as costCentres:
            # creating the heading
            heading = "Cost Centre"
            costCentres.write(heading + "\n")
            costCentres.write(str((len(heading) + 10) * "-") + "\n")

            # generating the data
            for cc in self.__ccList:
                costCentres.write(cc + "\n")

