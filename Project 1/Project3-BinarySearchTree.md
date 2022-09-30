# Project 3 - Binary Search Tree

Array:[7,5,1,8,3,6,0,9,4,2]

1. 7 root node.
2. 5 lower than 7 so put it on left subtree.
3. 1 lower than 7 so move to left, lower than 5 so move it left again.
4. 8 higher than 7 so put it on right subtree.
5. 3 lower than 7 so put it on left, lower than 5 so move it left, higher than 1 so move to right.
6. 6 lower than 7 so put it on the left subree, higher than 5 so move to right.
7. 0 lower than 7, lower than 5 and 1 so move it far left of subtree
8. 9 higher than 7 so move to right, higher than 8 so move to right again.
9. 4 lower than 7 so put it on left, lower than 5 so move to left, higher than 1 so move it right, lower than 6 so put it left side of 6
10. 2 lower than 7, lower than 5, highr than 1, so move it right, lower than 3 so move it left.





                    7
                  /   \ 
                 5     8
               /   \     \
              1     6      9           
            /   \               
           0     3
               /  \
              2    4