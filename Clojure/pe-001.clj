(defn sum-multiples-below [k n]
	"sum of all the multiples of k below n"
	(->> (range k n k)
	     (reduce +)))

(println (- (+ (sum-multiples-below 3 1000) 
	           (sum-multiples-below 5 1000)) 
	        (sum-multiples-below 15 1000)))
