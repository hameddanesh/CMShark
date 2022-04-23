import sqlite3
import numpy


class DatasetIntegrator:
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('CMShark.db')
        self._flowDirection = ["in", "out"]

    def IntegrateDatasets(self, flowDirection,shuffleIt=True):

        # <read dataset files list>
        # the flowDirection indicates weather we do dataset integration for sent packet data or received packet data
        myCursor = self.con.cursor()
        myCursor.execute(
            'SELECT dataset_name FROM datasets WHERE source_id=1 AND dataset_use_vpn=0 AND dataset_direction=' + str(flowDirection))

        datasetFileList = myCursor.fetchall()

        myCursor.close()
        # <read dataset files list>

        # <read each input file contents and combine them in outputArray>
        outputArray = []
        for datasetFile in datasetFileList:

            datasetFileName = datasetFile[0].rstrip()

            # <read dataset file content>
            path = "flow_dg/inputs/"+datasetFileName
            fileHandler = open(path, 'r')
            flowList = fileHandler.readlines()
            fileHandler.close()
            # </read dataset file content>

            # <concat dataset data>
            for flow in flowList:
                singleFlow = flow.split(",")
                outputArray.append([datasetFileName.split(".")[0],str(singleFlow[1].rstrip())])
            # </concat dataset data>

            print(datasetFileName)
        # </read each input file contents and combine them in outputArray>

        # <shuffle combined dataset>
        if shuffleIt:
            numpy.random.shuffle(outputArray)
        # </shuffle combined dataset>

        # <write output>
        path = "flow_dg/accuracy_comparison/caprolu_novpn/output-" + \
            self._flowDirection[flowDirection]+"flow.csv"

        outputHandler = open(path, "w")
        outputHandler.write("name,size\n")
        for outArrayLine in outputArray:
            outputHandler.write(str(outArrayLine[0])+","+outArrayLine[1]+"\n")

        outputHandler.close()
        print("\ndataset generated!")
        # </write output>



if __name__ == "__main__":
    datasetIntegrator = DatasetIntegrator()
    datasetIntegrator.IntegrateDatasets(0)
    datasetIntegrator.IntegrateDatasets(1)

