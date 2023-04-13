'''
Python file to evaluate results
'''

import argparse
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

def evaluate_results(predictions, labels):
    accuracy = accuracy_score(labels, predictions)
    f1 = f1_score(labels, predictions)
    auc_roc = roc_auc_score(labels, predictions)

    return accuracy, f1, auc_roc

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a CSV file.')
    parser.add_argument('--predictions', type=str, help='Path to the predictions CSV file')
    parser.add_argument('--labels', type=str, help='Path to the labels CSV file')
    args = parser.parse_args()
    
    # get file paths of predictions/labels
    predictions_filepath = args.predictions
    labels_filepath = args.labels
    
    # read files of predictions/labels
    predictions = pd.read_csv(predictions_filepath)
    labels = pd.read_csv(labels_filepath)
    
    # obtain list of predictions/labels
    predictions = predictions.label.to_list()
    labels = labels.label.to_list()

    # convert to numpy arrays
    predictions = np.array(predictions)
    labels = np.array(labels)
    
    # get results
    accuracy, f1, auc_roc = evaluate_results(predictions, labels)
    
    # display results
    print(f"Accuracy: {accuracy:.2f}, F1-score: {f1:.2f}, AUC-ROC: {auc_roc:.2f}")