(defn product-number-str [some-str]
  (->> (seq some-str)
       (map str)
       (map #(Integer/parseInt %))
       (reduce *)))

(defn thirteen-subs-largest-product [some-str]
  (->> (range 0 988)
       (map #(subs some-str % (+ 13 %)))   
       (map product-number-str)
       (apply max)))

(def input-str (->> (take-while #(not= "" %) (repeatedly #(.readLine *in*)))
                    (reduce str)))

;Press Enter twice after you input the 1000-number string at stdin

(println (thirteen-subs-largest-product input-str))
