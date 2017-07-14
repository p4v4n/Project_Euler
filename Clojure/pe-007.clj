(defn is-prime-number? [n]
    (loop [x (int (Math/floor (Math/pow n 0.5)))]
        (if (= x 1)
            true
            (if (= 0 (rem n x))
                false
                (recur (dec x))))))

(defn nth-prime [n]
    (->> (range)
         (drop 2)
         (filter is-prime-number?)
         (take n)
         (last)))

(println (nth-prime 10001))
