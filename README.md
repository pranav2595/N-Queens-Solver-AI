-----------------------
Installing Requirements
-----------------------
1) Navigate to the project directory
2) Open command line 
3) Run the following
  pip install -r requirements.txt
  
  
----------------------
Command Line Arguments
----------------------
1) Navigate to project directory
2) Open command line in that directory
3) Run the following command
	
  python NQueens.py <ALG> <N> <CFile>  <RFile>
  ALG: FOR or MAC   (FOR for Forward Checking and MAC for MAintaining Arc Consistency)
  N: Size of the chess board for which N queen needs to be solved
  CFile: File name given to generate the file and put constraints, variables and domains.
  RFile: File name given to generate the file and write the results upto 2*n 


------------------------
Understanding the Output
------------------------

1) The format of the output is as follows :

	FOLLOWING ARE THE RESULTS UPTO 2*N FOR THE NQUEEN PROBLEM
    '_' represents empty cell and 'Q' represents a cell having the Queen placed safely following the constraints.
    Solution 1: Values(Corresponding columns which they are placed) of Queen variables respectively are [0, 2, 5, 7, 9, 4, 8, 1, 3, 6]
    Q __ __ __ __ __ __ __ __ __
    __ __ Q __ __ __ __ __ __ __
    __ __ __ __ __ Q __ __ __ __
    __ __ __ __ __ __ __ Q __ __
    __ __ __ __ __ __ __ __ __ Q
    __ __ __ __ Q __ __ __ __ __
    __ __ __ __ __ __ __ __ Q __
    __ Q __ __ __ __ __ __ __ __
    __ __ __ Q __ __ __ __ __ __
    __ __ __ __ __ __ Q __ __ __
    >>>>More solutions depending on the input
    .
    .
    .
    .
    .
    .
    .
    >>>>
    Solutions found :20 with 137 backtracks performed and 0.1349194049835205 seconds taken to execute
    >NOTE: Currently I am showing and calculating just solutions upto 2*n. If this is not to be done then please remove 2nd if block in both MAC and FOR implementation methods.
    The above graph shows the chess of size n input by the user and 
    Q in the chess represents a cell having the Queen placed safely following the constraints.
    '_' represents empty cell.
    
    