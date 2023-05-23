import argparse
import numpy as np
import pandas as pd
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt



def plot_auc(y_true, y_proba):
    fpr, tpr, _ = roc_curve(y_true, y_proba)
    plt.figure()
    plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % auc)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0, 1.05])
    plt.ylim([0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc="lower right")
    plt.savefig('roc_curve.png')
    

parser = argparse.ArgumentParser()
parser.add_argument('--pred', type=str, required=True, help='path to prediction file') #path to the prediction.csv
parser.add_argument('--label', type=str, required=True, help='path to ground truth label file') #path to ground truth file

args = parser.parse_args()

Y_true = pd.read_csv(args.label)
Y_pred = pd.read_csv(args.pred)

y_true = Y_true['label'].values
y_pred = Y_pred['label'].values
y_proba = Y_pred['proba'].values

f1_score = f1_score(y_true, y_pred)
auc = roc_auc_score(y_true, y_proba)
plot_auc(y_true, y_proba)

print('F1 score: {:.4f}'.format(f1_score))
print('AUC: {:.4f}'.format(auc))
