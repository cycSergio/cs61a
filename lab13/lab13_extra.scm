; Q4
(define (rle s)
  (define (helper s value count)
           (cond ((null? s) (cons-stream (cons value (cons count nil)) nil))
                 ((= value (car s)) (helper (cdr-stream s) value (+ 1 count)))
                 (else (cons-stream (cons value (cons count nil)) (helper (cdr-stream s) (car s) 1)))
           )
  )
  (if (null? s) nil (helper (cdr-stream s) (car s) 1))
)

; Q4 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q5
(define (insert n s)
  (define (helper n s r)
          (cond ((null? s) (append r (list n)))
                ((< n (car s)) (append r (list n) s))
                (else (helper n (cdr s) (append r (list (car s)))))
          )
  )
  (helper n s nil)
)

; Q6
(define (deep-map fn s)
  (cond ((null? s) nil)
        ((list? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
        (else (cons (fn (car s)) (deep-map fn (cdr s))))
  )
)

; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
(define (unique s name)
  'YOUR-CODE-HERE
  (filter (lambda (x) (not (eq? x name))) s)
)

(define (count name s)
  'YOUR-CODE-HERE
  (if (null? s)
      0
      (if (eq? (car s) name)
          (+ 1 (count name (cdr s)))
          (count name (cdr s))))
)

(define (tally names)
  'YOUR-CODE-HERE
  (if (null? names)
      nil
      (cons (cons (car names) (count (car names) names)) (tally (unique names (car names)))))
)