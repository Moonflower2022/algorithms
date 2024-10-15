(load "implementations.lsp")

(defun save-number-to-file (input filename)
  "Save the Fibonacci result for n to a text file."
  (with-open-file (stream filename :direction :output :if-exists :supersede)
    ;; Write the number to the file
    (format stream "~a~%" input)
    ;; Print confirmation to console
    (format t "Saved number to ~a~%" filename)))

;; Calculate Fibonacci and store the result
(defvar fib-number 100)
(let ((result (time (fib-func fib-number))))
  ;; Use format correctly to create the filename string
  (save-number-to-file result (format nil "f(~d).txt" fib-number)) 
  result)
