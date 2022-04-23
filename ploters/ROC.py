from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import RocCurveDisplay
import matplotlib.pyplot as plt
import pickle


class DataFlowTrainer:
    def __init__(self):
        super().__init__()

    def ReadDataset(self, fileName):
        X_Array = []
        y_Array = []
        dataset = open("./flow_dg/outputs/"+fileName)
        firstLine = True
        for row in dataset:
            if not firstLine:
                temp = row.split(",")
                X_Array.append([int(temp[0])])
                y_Array.append(temp[1].strip("\n"))
            else:
                firstLine = False
        dataset.close()

        return X_Array, y_Array

    def Draw(self, fileName):
        X_Array, y_Array = self.ReadDataset(fileName)
        X_train, X_test, y_train, y_test = train_test_split(
            X_Array, y_Array, test_size=0.33, random_state=42)

        # increasing depth of random forest increases accuracy but it also makes model heavier
        clf = RandomForestClassifier(max_depth=100, random_state=0)
        clf.fit(X_train, y_train)
        ax = plt.gca()
        
        clf_disp = RocCurveDisplay.from_estimator(clf, X_test, y_test, ax=ax, alpha=0.8)
        clf_disp.plot(ax=ax, alpha=0.8)
        # plt.xlabel('false positive rate')
        # plt.ylabel('true positive rate')
        plt.show()



if __name__ == "__main__":
    dft = DataFlowTrainer()
    dft.Draw("netflow-dataset-in.csv")
    dft.Draw("netflow-dataset-out.csv")
