import argparse
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

import os

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, required=True, help='path to predictions folder')
parser.add_argument('--gt', type=str, required=True)
args = parser.parse_args()

y_true = pd.read_csv(args.gt)['label'].values

leader_board = pd.DataFrame(columns=['team_name', 'sub_#', 'f1_score', 'auc'])

predictions_files = os.listdir(args.path)
for file in predictions_files:
    path = os.path.join(args.path, file)
    file_name = file.split('.')[0]
    team_name = file_name.split('_')[0]
    sub_no = file_name.split('_')[1]

    y_pred = pd.read_csv(path)['label'].values
    y_proba = pd.read_csv(path)['proba'].values
    f1 = f1_score(y_true, y_pred)
    auc = roc_auc_score(y_true, y_proba)

    new_row = {'team_name': team_name, 'sub_#': sub_no, 'f1_score': f1, 'auc': auc }
    leader_board = leader_board.append(new_row, ignore_index=True)

leader_board.to_csv('leader_board.csv', index=False)

