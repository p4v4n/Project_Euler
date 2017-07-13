;(Math/pow 4 0.5)
;(Math/floor 1.2)
(defn is-prime-number? [n]
    (loop [x (int (Math/floor (Math/pow n 0.5)))]
        (if (= x 1)
            true
            (if (= 0 (rem n x))
                false
                (recur (dec x))))))

(defn largest-prime-factor [n]
    (loop [x (long (/ n 2))]
        (println x)
        (if (and (= (rem n x) 0) (is-prime-number? x))
            x
            (recur (dec x)))))

;;This approach is too slow
;;-------------
(defn largest-prime-factor2 [n]
    (loop [cur-num n f 2 lpf 1]
        (if (> (Math/pow f 2) cur-num)
            (if (> cur-num 1)
                cur-num
                lpf)
            (if (= 0 (rem cur-num f))
                (recur (/ cur-num f) f f)
                (recur cur-num (inc f) lpf)))))

(println (largest-prime-factor2 (long 600851475143)))


