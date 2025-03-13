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
'''