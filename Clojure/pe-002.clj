(defn fib [n]
	  (loop [a 1 b 2 c 1]
	  	(if (= c n)
	  		a
	  		(recur b (+ a b) (inc c)))))

(defn even-sum-below-n [n]
	(->> (range 1 n)
		 (map fib)
		 (take-while #(<= % n))
		 (filter even?)
		 (reduce +)))

(println (even-sum-below-n 4000000))
