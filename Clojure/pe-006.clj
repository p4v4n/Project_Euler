(defn squares-of-sum [n]
	(Math/pow (/ (* n (inc n)) 2) 2))

(defn sum-of-squares [n]
	(/ (* n (inc n) (inc (* 2 n))) 6))

(defn sum-square-difference [n]
	(int (- (squares-of-sum n) (sum-of-squares n))))

(println (sum-square-difference 100))
