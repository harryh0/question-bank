taken from [Maximize distance to closest person](https://leetcode.com/problems/maximize-distance-to-closest-person/)

### Question

You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

A person wants to sit in the seat such that the distance between them and the closest person is maximized. 

Return that maximum distance to the closest person.

### Test case 1
Input: seats = [1,0,0,0,1,0,1]
Output: 2

#### Reasoning for Test case 1
The maximum distance to any closest person is 2 if the person sits in at seats[2]. If the person sits anywhere else, the maximum distance to any closest person is 1.

### Test case 2
Input: seats = [1,0,0,0]
Output: 3

#### Reasoning for Test case 2
The maximum distance to the person is 3 if the person sits at seats[3].

### Test case 3
Input: seats = [0,1]
Output: 1

#### Reasoning for Test case 3
The only other possible seat is at seats[0]


### Test case 4
Input: seats = [1,0,0,0,1,0,0,0,1]
Output: 2

#### Reasoning for Test 4
Although there is a tie between the maximum distance between seats[2] and seats[6], we break the tie with the smaller index.
