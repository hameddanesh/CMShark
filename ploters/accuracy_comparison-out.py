import numpy as np 
import matplotlib.pyplot as plt 
  
X = ['caprolu','caprolu_novpn','mixed','filtered','final']
accuracy = [68.82,81.52,91.35,91.81,93.98]
f1_score = [46.87,81.10,91.50,92.10,94.30]
auc=[96.70,97.00,97.10,97.30,97.30]
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, accuracy, 0.2, label = 'Accuracy')
plt.bar(X_axis + 0.0, f1_score, 0.2, label = 'F1-score')
plt.bar(X_axis + 0.2, auc, 0.2, label = 'AUC')

  
plt.xticks(X_axis, X)
plt.xlabel("model name")
plt.ylabel("score")
plt.title("OutFlow Model Accuracy Comparison")
plt.legend()
plt.show()