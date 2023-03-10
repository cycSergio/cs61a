(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
    (define (my-helper rest) (cons first rest))
  (cond ((null? rests) (cons (cons first nil) nil))
  ((and (null? (cdr rests)) (number? (car rests))) (cons-all first (cons rests nil)))
  (else (map my-helper rests))
  ))

(define (zip pairs)
  (if (eq? pairs nil) '(() ())
      (cons )
  )
  )

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
        (define (my-helper s n)
                (if (eq? s nil) nil
                    (cons (cons n (cons (car s) nil)) (my-helper (cdr s) (+ 1 n)))
                )
        )
        (my-helper s 0)
  )
  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 18
  (define (helper total denoms my-list)
    (cond ((= total 0) nil)
           ((null? denoms ) nil)
           ((< total (car denoms)) (helper total (cdr denoms) my-list))
           ((< total 0) nil)
           (else (append (cons-all (car denoms) (helper (- total (car denoms)) denoms nil))
                                   (helper total (cdr denoms) nil)))
    ))
    (helper total denoms nil))
  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         'replace-this-line
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         'replace-this-line
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           'replace-this-line
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           'replace-this-line
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         'replace-this-line
         ; END PROBLEM 19
         )))
