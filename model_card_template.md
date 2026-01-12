# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
For this project, I decided to use a Random Forest classifier to predict whether income of $50,000 or more can be predicted based on the dataset provided.
It was developed by me, Stephane Roux as part of a machine Learning pipeline project as well as FastAPI web service
## Intended Use
The intended use of this model is purely educational as it is develop in class setting. The outcome can be used to identify so socio-economic trends
## Training Data
The model was trained on the Census Income Dataset from the UCI Machine Learning Repository. The data includes features such as age, education level, marital status, occupation, and native country. Containing total of 32,561 records, a standard 80/20 split was used for training and testing, and the data underwent preprocessing including One-Hot Encoding for categorical variables and Label Binarization for the target variable
## Evaluation Data
Evaluation was performed on a held-out test set comprising 20% of the original dataset. To ensure robustness and fairness, the model was also evaluated on various data slices across categorical features like education and race to check for performance disparities.
## Metrics
The model's performance was evaluated using Precision, Recall, and the F1-Score. These metrics were chosen to provide a balanced view of the model's ability to minimize both false positives and false negatives.
Based on the latest evaluation run, the global performance metrics are as follows:
Precision: 0.7391
Recall: 0.6384
F1-Score: 0.6851

Detailed performance on data slices is documented in the artifact "slice_output.txt" file generated during the evaluation phase.

## Ethical Considerations
The dataset used contains sensitive demographic information, including race and gender. There is a risk that the model may learn and perpetuate historical biases present in the census data especially considering that this data is quite old. 

## Caveats and Recommendations
The data is based on 1994 Census results, which means the income thresholds and socioeconomic factors are significantly outdated and do not reflect current economic conditions. In order to be used outside of academia it would be wise to retrain the model on more recent datasets.

