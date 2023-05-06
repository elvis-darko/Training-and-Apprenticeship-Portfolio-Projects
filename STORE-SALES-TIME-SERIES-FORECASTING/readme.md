## PROJECT DESCRIPTION
In this time series forecasting project, I predict store sales on data from Corporation Favorita, a large Ecuadorian-based grocery retailer. 

Specifically, I build a model that more accurately predicts the unit sales for thousands of items sold at different Favorita stores

The dataset is in a zip file within a folder called Dataset. The training and test data are in the zip file. The training data includes dates, store, and product information, whether that item was being promoted, as well as the sales numbers. Also, there are additional files which include supplementary information that may be useful in building my models.

### File Descriptions and Data Field Information

#### train.csv

The training data, comprising time series of features store_nbr, family, and onpromotion as well as the target sales.

`store_nbr` identifies the store at which the products are sold.

`family` identifies the type of product sold.

`sales` gives the total sales for a product family at a particular store at a given date. Fractional values are possible since products can be sold in fractional units (1.5 kg of cheese, for instance, as opposed to 1 bag of chips).

`onpromotion` gives the total number of items in a product family that were being promoted at a store at a given date.

#### test.csv

The test data, having the same features as the training data. You will predict the target sales for the dates in this file.

The dates in the test data are for the 15 days after the last date in the training data.

#### transaction.csv

Contains date, store_nbr and transaction made on that specific date.
#### sample_submission.csv

A sample submission file in the correct format.
#### stores.csv

Store metadata, including city, state, type, and cluster.

`Cluster` is a grouping of similar stores.

#### oil.csv

Daily oil price which includes values during both the train and test data timeframes. (Ecuador is an oil-dependent country and its economical health is highly vulnerable to shocks in oil prices.)

#### holidays_events.csv

Holidays and Events, with metadata

`NOTE:` Pay special attention to the transferred column. A holiday that is transferred officially falls on that calendar day but was moved to another date by the government. A transferred day is more like a normal day than a holiday. To find the day that it was celebrated, look for the corresponding row where type is Transfer.

For example, the holiday Independencia de Guayaquil was transferred from 2012-10-09 to 2012-10-12, which means it was celebrated on 2012-10-12. Days that are type Bridge are extra days that are added to a holiday (e.g., to extend the break across a long weekend). These are frequently made up by the type Work Day which is a day not normally scheduled for work (e.g., Saturday) that is meant to payback the Bridge.

`Additional holidays` are days added a regular calendar holiday, for example, as typically happens around Christmas (making Christmas Eve a holiday).

#### Additional Notes

Wages in the public sector are paid every two weeks on the 15th and on the last day of the month. Supermarket sales could be affected by this.

A magnitude 7.8 earthquake struck Ecuador on April 16, 2016. People rallied in relief efforts donating water and other first need products which greatly affected supermarket sales for several weeks after the earthquake.



## SUMMARY
| Code      | Name        | Published Article |  Deployed App |
|-----------|-------------|:-------------|:------|
| LP 2      | Store Sales - Time Series Forecasting - Regression Project| Medium<br />LinkedIn | [Jupyter Notebook](https://github.com/elvis-darko/Training-and-Apprenticeship-Portfolio-Projects/blob/main/STORE-SALES-TIME-SERIES-FORECASTING/STORE-SALES-TIME-SERIES-FORECASTING-REGRESSION%20PROJECT.ipynb) |




## SETUP
It is recommended to have a Jupyter Noteotebook or any other standard code editor on your local machine.<br />Install the required packages locally to your computer.

It is recommended that you run a python version above 3.0. 
You can download the required python version from [here](https://www.python.org/downloads/).

Use these recommended steps to set up your local machine for this project:

1. **Create the Python's virtual environment :** <br />This will isolate the required libraries of the project to avoid conflicts.<br />Choose any of the line of code that will work on your local machine.

            python3 -m venv venv
            python -m venv venv


2. **Activate the Python's virtual environment :**<br />This will ensure that the Python kernel & libraries will be those of the created isolated environment.

            - for windows : 
                         venv\Scripts\activate

            - for Linux & MacOS :
                         source venv/bin/activate


3. **Upgrade Pip :**<br />Pip is the installed libraries/packages manager. Upgrading Pip will give an to up-to-date version that will work correctly.

            python -m pip install --upgrade pip


4. **Install the required libraries/packages :**<br />There are libraries and packages that are required for this project. These libraries and packages are listed in the `requirements.txt` file.<br />The text file will allow you to import these libraries and packages into the python's scripts and notebooks without any issue.

            python -m pip install -r requirements.txt 



## EVALUATION

## AUTHOR
Elvis Darko

elvis_darko@outlook.com
