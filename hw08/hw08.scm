(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
   (cond ((> x 0) 1) ((= x 0) 0) ((< x 0) -1)
   )
)

(define (square x) (* x x))

(define (pow b n)
  (cond ((= n 0) 1)
      	((= 0 (remainder n 2)) (square (pow b (/ n 2))))
        (else (* b (pow b (- n 1))))
   )
)

(define (ordered? s)
    (if (null? (cdr s)) 'True
        (cond ((< (cadr s) (car s)) 'False)
              (else (ordered? (cdr s))))
    )
)

: Q5: no dots
(define (nodots s)
    (cond ((null? s) s)
          ((not (pair? s)) s)
          ((and (not(pair? (cdr s)))(not (null? (cdr s)))) (nodots (list (car s) (cdr s))))
          (else (append (list (nodots (car s))) (nodots (cdr s))))
    )
)

; Sets as sorted lists
; Q6: contains

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) #f)
          ((> (car s) v) False)
          ((= (car s) v) True)
          (else (contains? (cdr s) v)) ; replace this line
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

; Q7 add
(define (add s v)
    (cond ((empty? s) (list v))
          ((> (car s) v) (append (list v) s))
          ((= (car s) v) s)
          (else (append (list (car s)) (add (cdr s) v)))
          ))
; Q8 intersection & union
(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((= (car s) (car t)) (append (list (car s)) (intersect (cdr s) (cdr t))))
          ((< (car s) (car t)) (intersect (cdr s) t))
          (else (intersect s (cdr t)))
          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s) (car t)) (append (list (car s)) (union (cdr s) (cdr t))))
          ((< (car s) (car t)) (append (list (car s)) (union (cdr s) t)))
          (else (append (list (car t)) (union s (cdr t))))
          ))