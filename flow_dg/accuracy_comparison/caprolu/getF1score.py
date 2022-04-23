from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score


class DataFlowTrainer:
    def __init__(self):
        super().__init__()

    def ReadDataset(self, fileName):
        X_Array = []
        y_Array = []
        dataset = open(fileName)
        firstLine = True
        for row in dataset:
            if not firstLine:
                temp = row.split(",")
                X_Array.append([int(temp[1])])
                y_Array.append(temp[0].strip("\n"))
            else:
                firstLine = False
        dataset.close()

        return X_Array, y_Array


    def TestModel(self, fileName):
        X_Array, y_Array = self.ReadDataset(fileName)
        X_train, X_test, y_train, y_test = train_test_split(
            X_Array, y_Array, test_size=0.33, random_state=42)

        # increasing depth of random forest increases accuracy but it also makes model heavier
        clf = RandomForestClassifier(max_depth=100, random_state=0)
        clf.fit(X_train, y_train)
        result = clf.predict(X_test)
        print(" ", fileName, "accuracy score is:",
              accuracy_score(y_test, result), " and f1 score is:", f1_score(y_test, result, average='macro'))


if __name__ == "__main__":
    dft = DataFlowTrainer()
    dft.TestModel("flow_dg/accuracy_comparison/caprolu/output-inflow.csv")
    dft.TestModel("flow_dg/accuracy_comparison/caprolu/output-outflow.csv")
