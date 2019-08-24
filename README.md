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
  - for numeric / categorical features - The number of nulls in the data (number and percentage for each column)
  - grid of histograms 
  - Top-5 of the most frequent categorical features (for each)

Parameters (function view):
 * d - table with data
 * only_numeric - True / False, default: True. True - information output only by numerical features, False - information output by numerical and categorical features.
 * full_stats - True / False, default: False. False - output information on numerical features without interquartile range, data boundaries without outliers, True - complete output with IQR, min and max by IQR and amount of outliers.
 * histograms - True / False, default: True. True - output with building histograms for numerical signs, False - without building histograms

Top-5 elements of categorical signs

 The table is formed as follows. The postfix (_name / _count) is assigned to the name of the data column:
  - __name_ - category name
  - __count_ - number of elements in this category If there are less than 5 elements in the attribute, then the values ​​in the _count field are filled -1

Install
-------
	$ pip install data_view

Usage
-----

    $ python3

    from data_view import *

    d = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])

    view(d, only_numeric=True, histograms=False)

