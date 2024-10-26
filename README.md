# algorithms

My implementation of some interesting algorithms.

* `calculus`
  * area approximation schemes
    * riemann sums
    * monte carlo simulations
  * euler's method for approximating points in differential equations
* `fast_exponentiation`
  * implementations of the fast exponentiation algorithm that can exponentiate in log(n) time
* `fibonacci` (WIP)
  * differnt implementations to get the nth fibonacci number
    * recursive: literally implements f(n) = f(n-1) + f(n-2) \[exponential]
    * cached recursive: same as recursive but caches results \[linear]
    * better cached recursive: same as cached recursive but uses a different formula \[logmarithmic]
    * iterative: does a, b = 0, 1 and then a, b = b, a + b \[linear]
    * closed: uses the (very accurate) approximation of f(n) ≈ round(phi^n / sqrt(5)) where phi is (1 + sqrt(5)) / 2 \[constant (but doesnt work for high n)]
    * closed precise: same as closed but uses decimal.Decimal data type for more precision \[linear]
    * matrix: since \[[1, 1], [1, 0]]^n = \[[f(n+1), f(n)], [f(n), f(n-1)]] uses fast exponentiation to multiply matrices and get result \[logmarithmic]
  * scripts like `evaluation.py` and `evaluation.lsp` to compare them
* `knapsack_problem`
  * dynamic programming soultion to [knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem?scrlybrkr=7aea1319)
  * c++!
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
