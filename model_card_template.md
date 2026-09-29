# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This is a RandomForestClassifier model from Scikit-Learn.  The model divides the data into training and testing subsets, then uses estimators and a default state of 42


## Intended Use
The use for this data and the model was to determine if an individual had a salary of over $50,000.  This was done for a school project, and as such is strictly educational.

## Training Data
The dataset was split up into two subsets, one of which was used for training.

## Evaluation Data
The other set of the test was the testing data, which was used for the evaluation.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
The metrics used were Precision, Recall, and the F1 score, and the models preformance was:
Precision: 0.7391 | Recall: 0.6384 | F1: 0.6851

Further metrics are available in the slice_output.txt file.

## Ethical Considerations
The dataset contains a large amount of census information, however, none of it can be used to personally identify any individuals.


## Caveats and Recommendations
The data is old, and as such is likely out of date for modern analysis.