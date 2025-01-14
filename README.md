# algorithms

My implementation of some interesting algorithms.

* `calculus`
  * area approximation schemes
    * riemann sums
    * monte carlo simulations
  * euler's method for approximating points in differential equations
* `fast_exponentiation`
  * implementations of the fast exponentiation algorithm that can exponentiate in log(n) time
* `knapsack_problem`
  * dynamic programming soultion to [knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem)
  * c++!
  * and a python implementation that my friend wrote
* `miller_rabin_rsa`: an RSA implementation using the miller rabin primality test
* `optimizers`
  * gradient descent to solve linear and non-linear systems of equations, find roots of functions
  * line search for faster convergence than gradient descent
  * adagrad for faster convergence than gradient descent
  * alberth method for roots of polynomials/maybe other functions
  * my own approximation scheme for minimizing continuous functions
  * genetic algorithm, just for fun
* `sorting`: sorting algorithms  
  * bubble sort  
  * counting sort  
  * insertion sort  
  * merge sort  
  * selection sort  
* `stable_matching_problem`
  * implementation of the solution to the problem in python
  * test cases to make sure it works
* `primality_test.py`
  * two implementations:
    * unoptimized
      * check up to floor(sqrt(n)) + 1
    * optimized
      * rule out n % 2 == 0 and n % 3 == 0
      * check every 6 up to floor(sqrt(n)) + 1
  * time comparison
* `subtraction_set.py`: determination of to and from positions for certain subtraction games (CGT)
