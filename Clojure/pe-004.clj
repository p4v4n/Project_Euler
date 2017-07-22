(defn all-palindromes []
  (for [x (range 100 1000)
        y (range 100 1000)
        :when (= (str (* x y)) 
                 (clojure.string/reverse (str (* x y))))]
      (* x y)))

(println (->> (all-palindromes)
              (apply max)))
