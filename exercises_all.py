'''
Question 1
The accompanying file data.csv contains information for the value x of
something observed at time t.

Given this data, we want to calculate the rate of change of this value over
time - we'll do this by taking two consecutive observations, say
 and
 and approximate the rate of change using this formula:



For example, if the data looks like this:

t     x
0.1   10
0.2   12
0.4   14
0.5   15
Then the first row of data would be considered
, the second row
, etc

And we can start approximating the rate of change starting at
 which would be calculated as:



Similarly,
 would be calculated as:



Use NumPy arrays to create an array that holds the calculated rates of change
and determine the minimum, maximum, average and standard deviation of the rate
of change.

Question 2
In linear regression we try to find the coefficients m (slope) and c
(y-intercept) of a straight line


that provides the "best" fit given some x and y data. This formula then allows
to predict y values for given x values.

Given an array of n (x, y) data pairs, these coefficients can be calculated
very simply.

A bit of terminology first:

Let X mean the column of X values.
Let Y mean the column of Y values.
Let XX mean a column calculated by multiplying each x in the X column by itself
Let XY mean a column calculated by multiplying the x and y values from the X
and Y columns
Then, given some column (say X), this symbol:
 means the sum of all the elements in the column.

Similarly, the symbol
 means the sum of the values obtained by multiplying (pairwise) the values in
 X and Y.

Given those definitions, the formulas for calculating the "best" values of m
and c are given by:





(where n is the number of (x,y) pairs in our data set.)

Using the same data we saw in Question 1, calculate the values for m and c for
that data set given the formulas above.

You can think of the t column in the data as the X column, and the x values in
the data as the Y column - we are trying to predict the value of x given a
value of t.

This will result in a straight line that "best" fits through the data.

Compare the slope of this regression line to the average rate of change you
calculated in Question 1.
'''