# charran-tor

There are several methods in which a problem can be encoded within the SAT language. 
However not all of these encodings are equal, some encodings prove much more efficient by various measures, such as the number of auxiliary variables introduced, or the total number of clauses.
Two such metrics are consistency, in which unit propogation can detect when an assignment of inputs will produce a contradiction, and domain consistency, in which unit propogation is able to resolve an input.
This project attempts to provide a tool in order to test encodings, specifically to produce examples of inputs which are either not consistent or domain consistent.


The organisation of this repo is such:  
The upres folder contains bule2 encodings which test whether an encoding is consistent or domain consistent on full assignment.  
The part folder contains bule2 encodings which test whether an encoding is consistent or domain consistent on partial assignments.  
The encod folder contains bule2 encodings which are tested as part of our test data.  
The tests folder contains a number of basic tests as well as scripts which are used to test the encodings in upres and part.  


