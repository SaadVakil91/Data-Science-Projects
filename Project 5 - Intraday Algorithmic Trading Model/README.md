# Project 5 - Intrayday Algorithmic Trading Model

## Summary:
Here I have developed an Intraday Model using Machine Learning methods to trade CFD's using FXCM's restful API. I have trained my model on 15m timeframe data for 4 different tickers (EUR/USD, USOil, SPX500, XAU/USD). The historical OHLV (Open, High, Low, Close) data was downloaded using FXCM's API. I then added various technical indicators as features for my Machine Learning model. I then used different combination of technical indicators and lookback features to label my data into "Buy", "Sell" and "No Signal". Then I split the data into train and test. I then trained the training data on Random Forest Classifier Model.

## Output:
* My **best model (Random Forest model)** produced very good fit on test data and produced very little false signals. The model had a CAGR of approximately 50% on test data. I ran my model on the live markets for 3 days. The model produced 23 trades of which 15 were profitable trades and 8 were loss making trades.   

## Dataset:
* 15m timeframe data for the 4 tickers was downloaded using FXCM's restful API
* Tickers: EUR/USD, USOil, SPX500, XAU/USD

## Models Used:
* Logistics Regression
* Gradient Boosting Classifier
* Random Forest Classifier

## Technologies Used:
Python, pandas, numpy, fxcmpy, statsmodel, sklearn, pickle, matplotlib, plotly 
                                                                                                 
## Code is split in the following parts:
* Downloading Data
* Adding Features to the Data
* Adding Labels to the Data
* Splitting Data into Train and Test
* Model Training and Testing 
* Signal Generation on Live Data using the Trained Model
* Live Trading
