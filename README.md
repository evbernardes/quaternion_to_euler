# Quaternion to Euler Scipy Implementation
It contains the implementation of the method described in [https://doi.org/10.1371/journal.pone.0276302](https://doi.org/10.1371/journal.pone.0276302). for the direct conversion of a rotation Quaternion into Euler angles of any given sequence.

This implementation is heavily based in the Scipy implementation.

In order to easily test the differences in time execution of this method compared to the Quaternion-to-Matrix-to-Euler method implemented originally in Scipy, it is best to use a version of Scipy that has both methods compiled. This can be found here: [https://github.com/evbernardes/scipy](https://github.com/evbernardes/scipy)



## Contents:
- **euler_from_quat.py**: Implementation of the method in Scipy-based code style.
- **main.py**: Execution time comparison of both methods. 

