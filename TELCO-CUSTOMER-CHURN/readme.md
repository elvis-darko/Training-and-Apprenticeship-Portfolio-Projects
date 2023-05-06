In this project, we analyze funding received by startups in India from 2018 to 2021. Data for each year of funding is located in a separate csv file in the dataset provided. In these files are the startups' details, the funding amounts received, and the investors' information.

As Data Analysts for this project, we ask business questions, explore the datasets, clean and prepare the datasets, analyze the final prepared dataset and tell compelling stories with intuitive and appropraite visulaizations.



## SUMMARY
| Code      | Name        | Published Article |  Deployed App |
|-----------|-------------|:-------------|:------|
| LP 1      | Indian Start-up Ecosystem Funding - Data Analysis Project | [Medium](https://medium.com/@el.darkoel/the-indian-start-up-ecosystem-an-analysis-of-funding-d234f84f13bb) <br />[LinkedIn](https://www.linkedin.com/feed/update/urn:li:share:7050151401053708288/)| [Jupyter Notebook](https://github.com/elvis-darko/Training-and-Apprenticeship-Portfolio-Projects/blob/main/INDIAN-STARTUP-ECOSYSTEM-FUNDING/INDIAN%20START-UP%20ECOSYSTEM%20FUNDING%20-%20EXPLORATORY%20DATA%20ANALYSIS.ipynb)<br />[Power BI](https://app.powerbi.com/groups/me/reports/d9972c7c-e3cb-4179-8273-ff602519514c/ReportSection) |





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
