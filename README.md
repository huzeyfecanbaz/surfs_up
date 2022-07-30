# surfs_up
## Overview of the Analysis
The main purpose of this study is to write a code to get the temperature statistics of two specific months:June and December in order to see whether a surf shop is sustainable to open in Oahu. To do this, the code seperated into two different parts where each code served to get the statistics of different month. The codes fisrtly filtered the tables to make it more meaningful by implementing the filter on 'date' and 'tobs'(temperatures observed) columns of the table. Then a query written to get them in a list. Lastly, a pandas dataframe has been created from the list and its summary statistics get by using describe() method.

## Resources
In this project following resources used;
- Jupyter Notebook
- VS Code
- SQLAlchemy
- Pandas
- Numpy
- hawaii.sqlite

## Results
- As it can be seen in the image below, the results show that the count of the June is 1700, mean temperature is 74.9, min temperature is 64.0 and max temperature is 85.0, and the standard deviation is 3.25.
https://github.com/huzeyfecanbaz/surfs_up/blob/26d6c7d32ca153f44c7453bbce8011144b6d349c/June%20Temp.png

- As it can be seen in the image below, the results show that the count of the December is 1517, mean temperature is 71.0, min temperature is 56.0 and max temperature is 83.0, and the standard deviation is 3.75.
https://github.com/huzeyfecanbaz/surfs_up/blob/26d6c7d32ca153f44c7453bbce8011144b6d349c/Dec%20Temp.png

The comparison of the standard deviations are giving .5 difference in the two different months or seasons.

## Summary
The query written in this assignment helps us to understand the temperature change in the seasons but of course this query can be enriched by implementing additional attributes by using different columns of the table such as precipitation so that it shows that we can run additional queries to let us know whether or not people can come and visit the shop. If we are able to gain more data for the area we can run even more queries! From there we can decide how we would like to build the shop and what areas would make this a more prominent location for visitors to come.
