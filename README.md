# Summer Challenge on Writer Verification
---
## Intriduction
The Writer Verification challenge is a competition that involves identifying whether a given pair of handwritten text samples were written by the same person or two different persons. In the accompanying Github repository, you will find starter code to help you get started on this task.

## Dataset
* Training set contains 1352 folders of images. All the images in one folder are written by the same person. 
* Validation set contains a set of images from 92 different writers. The val.csv file contains name of image pairs and the corresponding labels. A label of 1 indicates that the images are written by the same writer and a label of 0 indicates that the images are written by different writers.
* Test set contains images from 360 writers. In test.csv you are given name of image pairs. For output, you need to predict the label for given pair of images and submit the csv file in the format by editing the test.csv file.
![format](./assets/format.png)

## Evaluation
Your submissions will be evaluated against the ground truth using F1 score and AUC.
* F1 score: A measure of a model's accuracy that considers both precision and recall.
* AUC (Area Under the Curve): A measure of a model's performance that calculates the area under the Receiver Operating Characteristic (ROC) curve.
```
F1 = 2 * (precision * recall) / (precision + recall)
AUC = integral(TPR(FPR^-1)(f)df) where FPR is false positive rate and TPR is true positive rate
```

## Starter Code
You can find the starter code [here]()

--- 
For more details, please refer to our site [here](https://ceyxasm.github.io/WVSite/#task)