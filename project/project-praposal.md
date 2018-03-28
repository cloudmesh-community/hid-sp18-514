# Determining The Universality Of Benford’s Law Using Datasets In Data.gov
By Orly Esteban and Ravinder Lambadi

## Abstract

It is observed that a lot of real-life data, from personal expenses to world population data, tend to obey Benford’s Law. 
Because of this phenomenon, Benford’s Law has been leveraged in a lot of statistical analysis – including fraud detection. 
In 2009,  Benford’s Law has been utilized to detect election fraud in Iran. In this paper, 
the authors will determine the universality of the law. Is the law applicable to any dataset? 
The authors will analyze and visualize data on publicly available data sets at data.gov and determine which datasets follow this law and which ones do not, if any.

## Introduction

Benford’s law is a phenomenon about the distribution of the first-digits of numerical sets of real-life data. The law states that the distribution of the first digits follows a certain mathematical pattern. For example, the digit 1 tends to occur about 30% of the time compared to 11% if the distribution is evenly flat. The probability distribution tends to go lower from the digit 1 to the digit 9. 

A dataset is said to satisfy Benford’s Law if the leading digits have the following the probability distribution: 

Table1: Probability distribution of Benford’s Law

![Benfords Law Table](https://github.com/cloudmesh-community/hid-sp18-514/blob/master/project/images/benfords_law.JPG?raw=true)

In mathematical terms, Benford’s Law can be represented by the following equation: 

P(d) = log (d+1) - log (d)

The logarithmic function can be in any base. However, in this paper, only base 10 will be used. For example, in analyzing the leading digit 1,

P(1) = log (1+1) - log(1) = 0.301 

which means, if the dataset complies with Benford's Law, the probability of finding a leading digit 1 is about 30.1% of the time. Therefore, Benford’s Law indicates that the most likely leading digit for us to see is 1, the second most likely 2, the third most 3, the fourth most likely 4, and so on. 

Benford’s law not only apply to the scale invariant data but also applies to various data sources, that we are going to analyze and visualize in this project.

## Scope of work
- Define Benford’s Law
  - Show mathematical formula
  - Show the probability distribution (graph) according to Benford’s Law
- Download and store the following datasets from data.gov
  - National Student Loan Student system
  - National Stock Number Extract
  - Demographic Statistics
  - Consumer Fraud Refunds
  - Hospital Compare Data
  - Medicare Cost Reports
  - And Etc, there will be additional (4) datasets

- Analyze the data. And select the data field on which Benford’s Law will be applied.
- Draw the probability distribution of the first digits of the selected field.
- Compare the distribution in #4 with the expected Benford’s law distribution in #1
- Draw conclusions

## Technology Stack

Python will be used for Data Analytics and Visualization. As we are planning to analyze multiple data sets to check whether Benford’s law can be applied either HBase or MySQL database will be used for storing Big data set.

## References
- https://www.data.gov/

- https://en.wikipedia.org/wiki/Benford%27s_law

 - S. Newcomb. Note on the frequency of use of the different digits in natural numbers, Amer. J.
Math. 4 (1881) 39-40.

- F. Benford. The law of anomalous numbers, Proc. Am. Philos. Soc. 78 (1938) 551-538.

- L. Pietronero, E. Tossati, V. Tossati and A. Vespignani. Explaining the uneven distribution of
numbers in nature: the laws of Benford and Zipf, Physica A 293 (2001) 297-304.

- M. Nigrini. Peculiar patterns of first digits, IEEE Potentials 18, 2 (1999) 24-27
- M. Nigrini. A taxpayer compliance application of Benford's law, Journal of the American Taxation
- https://www.youtube.com/watch?v=SZUDoEdjTzg
- https://www.youtube.com/watch?v=0fKBhvDjuy0
- J. Barlow and E. Bareiss. On roundoff error distribution in floating point and logarithmic arithmetic, Computing 34 (1985) 325-347.
