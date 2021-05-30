# Project 3 - Bike Rental Demand Prediction

## Summary:
Here the task is to predict the count of the total bikes rented during a given hour on the test dataset

## Output:
My base model trained on linear regression provided an Rsquared of 24% on test data
My **best model (Random Forest model) provides an Rsquared of 81%** on test data, which is a significant improvement from the base model.

## Dataset:
*Source: Data has been downloaded from kaggle: https://www.kaggle.com/c/bike-sharing-demand/data*
* train: Contains 10886 rows of hourly bike rental data spanning for 2 years (2011-2012). The training set is comprised of the first 19 days of each month.
* test: Contains 6493 rows of hourly bike rental data spanning for 2 years (2011-2012). The test set is comprised of the hourly data from 20th to the end of the month for each month.

## Columns present in the Dataset:

| Columns    | Description                                                                                                                                                    |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| datetime   | hourly date + timestamp                                                                                                                                        |
| season     | 1 = spring, 2 = summer, 3 = fall, 4 = winter                                                                                                                   |
| holiday    | whether the day is considered a holiday                                                                                                                        |
| workingday | whether the day is neither a weekend nor holiday                                                                                                               |
| weather    | 1: Clear, Few clouds, Partly cloudy 2: Mist, Cloudy, Broken clouds 3: Light snow, Light rain, Thunderstorm 4: Heavy rain, Ice pallets, Thunderstorm, Snow, Fog |
| temp       | temperature in celsius                                                                                                                                         |
| atemp      | "feels like" temperature in celsius                                                                                                                            |
| humidity   | relative humidity                                                                                                                                              |
| windspeed  | wind speed                                                                                                                                                     |
| casual     | number of non-registered user rentals                                                                                                                          |
| registered | number of registered user rentals                                                                                                                              |
| count      | number of total rentals (casual + registered)                                                                                                                  |

## Code is split in the following parts:
* Reading the data
* Exploratory data analysis
* Base Model training (Used Linear Regression)
* Feature Engineering and Feature Expansion
* Model Training on new features. Models used:
 * Linear Regression
 * Ridge Regression
 * Lasso Regression
 * Elastic Net Regression
 * Poisson Regression
 * Random Forest Regression
* Hyperparameter optimisation
* Cross Validation of the final model to test for underfitting/ overfitting

## Technologies Used:
Project is created with:
* Python version: 3.7.3
