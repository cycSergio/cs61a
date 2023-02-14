; Q1
(define (compose-all funcs)
  (define (helper x funcs)
          (if (null? funcs) x (helper ((car funcs) x) (cdr funcs)))
  )
  (lambda (x) (helper x funcs))
)

; Q2
(define (tail-replicate x n)
  (define (helper x n result)
         (if (= n 0) result
             (helper x (- n 1) (cons x result)))
  )
  (helper x n nil)
)