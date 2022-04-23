import numpy as np 
import matplotlib.pyplot as plt 
  
X = ['caprolu','caprolu_novpn','mixed','filtered','final']
accuracy = [72.63,79.81,95.49,96.29,97.02]
f1_score = [46.27,78.30,95.40,96.20,96.90]
auc=[96.40,94.80,96.80,96.40,97.20]
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, accuracy, 0.2, label = 'Accuracy')
plt.bar(X_axis + 0.0, f1_score, 0.2, label = 'F1-score')
plt.bar(X_axis + 0.2, auc, 0.2, label = 'AUC')

  
plt.xticks(X_axis, X)
plt.xlabel("model name")
plt.ylabel("score")
plt.title("InFlow Model Accuracy Comparison")
plt.legend()
plt.show()