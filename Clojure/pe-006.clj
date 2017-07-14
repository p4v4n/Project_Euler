(defn squares-of-sum [n]
	(->> (range 1 (inc n))
		 (reduce +)
		 (#(* % %))))

(defn sum-of-squares [n]
	(->> (range 1 (inc n))
		 (map #(* % %))
		 (reduce +)))

(defn sum-square-difference [n]
	(int (- (squares-of-sum n) (sum-of-squares n))))

(println (sum-square-difference 100))
