# fibonacci

lots of implementations of functions that find the nth fibonacci number

# motivation

I started work on this analysis when I took a class called "intro to algorithms". in the class, we talked about running time and fibonacci sequences was a very fitting example for it. we started with an exponential time implementation (recursion with no caching), then looked at a linear one (iterative) and then finally got to the constant time solution (closed form). what bothered me, though, was the fact that we could not get infinite precision at a fast speed with the closed form due to how expensive float operations get when you have big numbers. 

# implementations

there are a couple of implementations that i considered (some were just for fun)
* iterative: in a loop, do `a, b = b, a + b`
* recursive without caching: `def fibonacci(n): return fibonacci(n - 1) + fibonacci(n - 2)`
* recursive with caching: just the last one but with `@lru_cache(maxsize=None) 
  * there were actually two versions of this: one that is just the last one, but one that uses an even faster recursion that for some reason works
* closed: returns `floor(phi ^ n)` where `phi` is `(1 + sqrt(5)) / 2`
* closed_precise: uses the Decimal built-in class from python for (supposedly) infinite precision
* matrix: takes [1 1; 1 0] and takes n powers of itself, and after thats done, take the [1][0] index of the matrix
* matrix_eigen_decomposition (WIP): same as matrix but takes the eigen decomposition of the matrix first so that when taking powers, its faster

# evaluations

* iterative
  * was reliable in the 0 -> 100_000 range for python
  * could do 1_000_000 in lisp on one CPU very quickly
  * took 5.5 mins to do 10_000_000
  * much faster in non python langs like lisp, c, c++, etc.
* recursive without caching
  * ... its exponential time :skull:
* recursive without caching
  * was very fast for lower numbers (up to 3300 or so)
  * after that, python was experiencing issues due to not being "tail end optimized" or smth
  * lisp was also fine until around 35000
* closed
  * for some reason doesnt work for lisp if input is more than 180
  * not good for python (float just turns into "inf")
* closed_precise
  * pretty good in python, can go up to 100_000
* matrix
  * very good, could do 10_000_000 in 10-20s on python on one core
  * could do 100_000_000 in ~7 mins (also on one core)

# files / directories

* `implementations.lsp`
* `implementations.py`
* `evaluation.lsp`: runs the number and function that you specify in the file. times the execution of the function, and saves result to a text file
* `evaluation.py`: runs the number you speficy in the file. runs and times each function that has been implemented, and prints the last 10 digits of the result
* `calculations`: directory with all of the cached results from `implementations.lsp`

# todo

implement recursive or iterative in c
* how to bypass int limits?

optimize matrix in python:
* run on multiple CPU
* use gpu in matrix multiplication
* run eigen decomposition
* ensure fast exponentiation when doing matrix exponentiation
