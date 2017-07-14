(defn is-prime-number? [n]
  (let [upper-limit (inc (int (Math/floor (Math/pow n 0.5))))]
    (loop [x 2]
        (if (= x upper-limit)
            true
            (if (= 0 (rem n x))
                false
                (recur (inc x)))))))

(defn sum-of-primes-below-n [n]
    (->> (range 2 n)
         (filter is-prime-number?)
         (reduce +)))

(println (sum-of-primes-below-n 2000000))
