# Merge Sort

[16,21,11,8,12,22]

## First Step: we will divide the array into two equal halves, till we reach individual values.
[16,21,11]-[8,12,22]
[16,21]-[11]  [8,12]-[22]
[16]-[21]-[11]  [8]-[12]-[22]

## Second Step: we wil now merge individual figures while comparing value of each one to another.

[16,21]-[11]  [8,12]-[22]
[11,16,21]  [8,12,22]
[8,11,12,16,21,22]

# Big O Notation

O(nlogn)
for this particular array: O(6log6)