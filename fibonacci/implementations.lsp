(defun iterative-fibonacci (n)
  "Iterative Fibonacci function using arbitrary precision numbers."
  (if (<= n 1)
      n
      (let ((a 0)
            (b 1))
        (loop for i from 2 to n do
          (let ((temp b))
            (setf b (+ a b))
            (setf a temp)))
        b)))

(defun recursive-fibonacci (n)
  (if (< n 2)
      (nth n '(0 1)) ; Base case: return 0 for n = 0, 1 for n = 1
      (+ (recursive-fibonacci (- n 1)) (recursive-fibonacci (- n 2))))) ; Recursive case

(defun fib-func (n &optional (a 0) (b 1))
  (cond
   ((= n 1) b)
   (t (fib-func (1- n) b (+ a b)))))

(defun closed (n)
  (round (expt (/ (+ 1 (sqrt 5)) 2) n)))

(defun memoized-recursive-fibonacci (n)
  (let ((cache (make-hash-table :test 'equal)))  ;; Create a hash table for caching results
    (labels ((memoized-helper (n)  ;; Define a helper function for recursion
               (or (gethash n cache)  ;; Check if the result for `n` is already in the cache
                   (setf (gethash n cache)  ;; If not, compute it and store it in the cache
                         (if (> n 2)
                             (+ (memoized-helper (- n 1)) (memoized-helper (- n 2)))
                             (nth n '(0 1 1)))))))  ;; Return the nth Fibonacci value for n <= 2
      (memoized-helper n))))  ;; Start the recursion