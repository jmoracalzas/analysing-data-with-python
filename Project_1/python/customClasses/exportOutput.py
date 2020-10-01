class output:
    def expTXT_CC(self):
        test = ["cc1", "cc2", "cc3", "cc4"]

        with open(
            "./Project_1/python/output/txt_files/costCentre.txt", "tw"
        ) as costCentres:

            costCentres.write("Cost Centre\n")  # header
            for cc in test:
                costCentres.write(cc + "\n")
