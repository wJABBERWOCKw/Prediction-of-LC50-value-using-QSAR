# Prediction-of-LC50-value-using-QSAR
 QSAR models to predict acute aquatic toxicity towards the fish 


Thousands of chemical substances for which no ecological toxicity data are available
can benefit from QSAR modelling to help prioritise testing. One of the data set
encompassing in vivo test data on fish for hundreds of chemical substances using the
ECOTOX database of the US Environmental Protection Agency, you can check that
dataset through this link: ECOTOX Database and additional data from ECHA. We can
utilise this to develop QSAR models that could forecast two sorts of end points: acute
LC50 (median lethal concentration) and points of departure akin to the NOEC (no
observed effect concentration) for any period (the “LC50” and “NOEC” models,
respectively). Study factors, such as species and exposure route, were incorporated as
features in these models to allow for the simultaneous use of many data types. To
maximise generalizability to other species, a novel way of substituting taxonomic
categories for species dummy variables was introduced.
The goal here is to build an end-to-end automated Machine Learning model that
predicts the LC50 value, the concentration of a compound that causes 50% lethality of
fish in a test batch over a duration of 96 hours, using 6 given molecular descriptors.


To build an end-to-end automated Machine Learning model that predicts the LC50 value (median lethal concentration) for fish, we'll need to perform the following steps:

Data Preprocessing: Prepare the data for training the model.

Feature Selection: Select the relevant molecular descriptors to use as features.

Train the Model: Use the selected features and the target variable (LC50) to train the model.

Used a Support Vector Regression (SVR) model. 

SVR stands for Support Vector Regression, which is a type of supervised machine learning algorithm used for regression tasks. Unlike traditional linear regression, SVR is based on the concept of Support Vector Machines (SVM), which was originally designed for classification problems.

In SVR, the goal is to find a regression function that best fits the data while also controlling the margin of error (epsilon) around the predicted values. The key idea behind SVR is to find a hyperplane in a higher-dimensional feature space that is as flat as possible while still including as many data points as possible within the specified margin (epsilon). The data points that fall within the margin are called support vectors, hence the name "Support Vector Regression."


Make Predictions: Use the trained model to predict the LC50 values for new chemical substances.
