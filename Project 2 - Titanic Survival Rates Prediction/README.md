# Project 2 - Titanic Survival Rates Prediction

## Summary:
Here the task is to predict the survival of passengers on board the titanic ship

## Output:
My trained Random Forest model is able to predict survivalability of **85 percent** of the passengers on board the titanic.

## Dataset:
*Source: Data has been downloaded from kaggle: https://www.kaggle.com/c/titanic/data*
* train: Contains 891 rows of data of passengers aboard the titanic ship

## Columns present in the Dataset:

| Variable | Definition                                 | Key                                            |
|----------|--------------------------------------------|------------------------------------------------|
| survival | Survival                                   | 0 = No, 1 = Yes                                |
| pclass   | Ticket class                               | 1 = 1st, 2 = 2nd, 3 = 3rd                      |
| sex      | Male or Female                             |                                                |
| Age      | Age in years                               |                                                |
| sibsp    | # of siblings / spouses aboard the Titanic |                                                |
| parch    | # of parents / children aboard the Titanic |                                                |
| ticket   | Ticket number                              |                                                |
| fare     | Passenger fare                             |                                                |
| cabin    | Cabin number                               |                                                |
| embarked | Port of Embarkation                        | C = Cherbourg, Q = Queenstown, S = Southampton |

## Code is split in the following parts:
* Reading the data
* Exploratory data analysis
* Feature engineering
* Model training (Used Logistics Regression and Random Forest model)
* Cross validation to check for model over/under fitting

## Technologies Used:
Project is created with:
* Python version: 3.7.3
