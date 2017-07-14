(defn gcd [a b]
    (loop [n1 a n2 b]
        (if (= n2 0)
            n1
            (recur n2 (rem n1 n2)))))

(defn lcm [a b]
    (/ (* a b) (gcd a b)))

(defn smallest-multiple [n]
    (->> (inc n)
         (range 1)
         (reduce lcm)))

(println (smallest-multiple 20))
