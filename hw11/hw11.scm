;Q1
(define (find s predicate)
  (cond ((null? s) #f)
        ((predicate (car s)) (car s))
        (else (find (cdr-stream s) predicate))
  )
)

; Q2
(define (scale-stream s k)
    (if (null? s) s (cons-stream (* k (car s)) (scale-stream (cdr-stream s) k)) )
)

;Q3
(define (has-cycle s)

    (define (if-in lst x)
    (cond ((null? lst) #f)
            ((eq? (car lst) #t))
            (else (if-in (cdr-stream lst) x))))

    (define seen nil)

  (define (helper s)
  (append (list s) seen)
    (if (null? s) #f (if (if-in seen s) #t (helper (cdr-stream s)))))
(helper s)
)


; extra credit for Q3
(define (has-cycle-constant s)
  (define (helper fast slow)
          (cond ((null? fast) #f)
                ((eq? (cdr-stream (cdr-stream fast)) (cdr-stream slow)) #t)
                (else (helper (cdr-stream (cdr-stream fast)) (cdr-stream slow)))
          )
  )
  (helper s s)
)
