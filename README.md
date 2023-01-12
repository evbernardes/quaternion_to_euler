# Quaternion to Euler Scipy Implementation
It contains the implementation of the method described in [https://doi.org/10.1371/journal.pone.0276302](https://doi.org/10.1371/journal.pone.0276302). for the direct conversion of a rotation Quaternion into Euler angles of any given sequence.

This implementation is heavily based in the older Scipy implementation.

~In order to easily test the differences in time execution of this method compared to the Quaternion-to-Matrix-to-Euler method implemented originally in Scipy, it is best to use a version of Scipy that has both methods compiled. This can be found here: [https://github.com/evbernardes/scipy](https://github.com/evbernardes/scipy)~

## This algorithm has been integrated in the following projects:
- [Sympy](https://github.com/sympy/sympy)
- [SciPy](https://github.com/scipy/scipy)
- [pytransform3d](https://github.com/dfki-ric/pytransform3d)

## Contents:
- **euler_from_quat.py**: Implementation of the method in Scipy-based code style.
- **main.py**: Execution time comparison of both methods. 

## Little warning:
On the PLOS ONE paper, I am following the convention of real part as the first element (like SymPy, for example.)

In this implementation, I am following SciPy's convention of the real part as the last element.

This means that, for example, a rotation around axis x of angle 90 degrees should be: 
```
q = np.asarray([[1/sqrt(2), 0, 0, 1/sqrt(2)]])
```
Instead of:
```
q = np.asarray([[1/sqrt(2), 1/sqrt(2), 0, 0]])
```
