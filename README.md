Description
===========

Requirements
------------

* python >= 3.6
* numpy >= 1.16
* pandas >= 0.23
* matplotlib >= 3.02
* IPython >= 7.2.0

------------

Module, provides the function _view_, which displays general information on the data:
  - Result of method info()
  - Result of method describe()
  - for numeric / categorical variables - The number of nulls in the data (amount and percentage for each column)
  - grid of histograms for numeric variables
  - Top-5 of the most frequent categorical variables (for each)
  - Split count statistic by category with less 5 unique values
  - matrix correlation

Parameters (function view):
 * d - table with data
 * only_numeric - True / False, default: True. True - information output only by numerical variables, False - information output by numerical and categorical variables.
 * full_stats - True / False, default: False. False - output information on numerical variables without interquartile range, data boundaries without outliers, True - complete output with IQR, min and max by IQR and amount of outliers.
 * histograms - True / False, default: True. True - output with building histograms for numerical variables, False - without building histograms

Top-5 elements of categorical variables

 The postfix (_name / _count) is assigned to the name of the data column to create top-5 elements table:
  - __name_ - category name
  - __count_ - number of unique elements in this category. If there are less than 5 unique elements, then the values ​​in the _count field are filled -1

Count statistic of numbers variables split by some categorical variables
 - if number of unique elements in category variable less 5, then show count statistic

Correlation matrix
 - Correlation matrix with heatmap (pearson corr index)

Install
-------
	$ pip install data_view

Usage
-----

    $ python3

    from data_view import *

    d = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])

    view(d, only_numeric=True, histograms=False)

