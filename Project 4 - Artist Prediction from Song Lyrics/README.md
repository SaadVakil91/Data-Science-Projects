# Project 3 - Artist Prediction from Song Lyrics

## Summary:
Here the task is to train a classification model to predict the artist from a given line of a song

## Output:
* My **best model (Random Forest model) correctly predicts artists for 75% of the song lyrics in the test data  

## Dataset:
*Source: Artist/ lyrics has been extracted using requests library from lyrics.com: https://www.lyrics.com/
* I have selected the following 5 artists: Chet Faker, Tom Odell, KSI, Cold Play, Eminem

## Models Used:
* Logistics Regression
* Naive Bayes Classifier
* Random Forest Classifier
                                                                                                 
## Code is split in the following parts:
* Extracting song lyrics from lyrics.com
* Cleaning the lyrics for any punctuation marks and converting them to lower case
* Training the Base Classification model
* Feature Engineering 1 (FE1): Removing/ Penalizing frequently occuring words using count vectorizer and TFidf transformer
* Model Training on the engineered features (FE1) and HyperParameter optimization
* Feature Engineering 2 (FE2): Accounting for Class Imbalance
* Model Training on the engineered features (FE2) and HyperParameter optimization
* Feature Engineering 3 (FE3): Passing entire lyrics rather each each line of lyrics into TFidf transformer
* Model Training on the engineered features (FE3) and HyperParameter optimization
* Cross Validation
* Conclusion

## Technologies Used:
Project is created with:
* Python version: 3.7.3
