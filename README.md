# Summer Challenge on Writer Verification

1. <a href="#introduction">Introduction</a>
2. <a href="#dataset">Dataset</a>
3. <a href="#evaluation">Evaluation</a>
4. <a href="#references">References</a>



 
---
## Introduction
The Writer Verification challenge is a competition that involves identifying whether a given pair of handwritten text samples was written by the same person or two different persons. In the accompanying Github repository, you will find starter code to help you get started on this task.

## Dataset
* The training set consists of 1352 folders, each containing a set of images written by the same person.
* The validation set contains a set of images from 92 different writers, along with a file called 'val.csv' that contains pairs of image names and corresponding labels. A label of 1 indicates that the images were written by the same writer, and a label of 0 indicates that the images were written by different writers.
* Test set contains images from 360 writers. In test.csv you are given name of image pairs. For output, you need to predict the label for given pair of images and submit the csv file in the format by editing the test.csv file.

![format](./assets/format.png)

---


## Evaluation
Your submissions will be evaluated against the ground truth using F1 score and AUC.
* F1 score: A measure of a model's accuracy that considers both precision and recall.
* AUC (Area Under the Curve): A measure of a model's performance that calculates the area under the Receiver Operating Characteristic (ROC) curve.
```
F1 = 2 * (precision * recall) / (precision + recall)
AUC = integral(TPR(FPR^-1)(f)df) where FPR is false positive rate and TPR is true positive rate
```


### Submission Format
You are required to submit a .csv file with following rules in mind.
* Name your csv file as `<team_name>_<submission_number.csv>`. So for team named VL2G making their first submission, file would be named `VL2G_1.csv`
* The csv file must have 4 columns `img1_name`, `img2_name`, `label` and `proba`. You may generate your submission file by creating a copy of `val.csv` that is provided to you so that ordering of the pairs is same as in original `val.csv`
![WVSC_1](./assets/WVSC_1.png)


Test you file by running [evaluate.py](./evaluate.py) script

```
python3 evaluate --label <path/to/ground/truth/csv/file> --pred <path/to/prediction/file>
```
![eval](./assets/eval.gif)


Leader-board will be generated using [leader_board.py](./leader_board.py). This is just for transparency and you may not use this script at your end.

```
python3 leader_board.py --gt <path/to/ground/truth/csv/file> --path <path/to/submission/folder>
```
![leaderboard](./assets/leader_board.gif)

--- 
For more details, please refer to our site [here](https://vl2g.github.io/challenges/wv2023/)

---
## References
For our baseline model, followong references were used and you are advised too look at the same.

* [SigNet: Convolutional Siamese Network for Writer Independent Offline Signature Verification](https://arxiv.org/pdf/1707.02131v2.pdf)
* [Attention based Writer Independent Verification](https://arxiv.org/pdf/2009.04532v3.pdf)
