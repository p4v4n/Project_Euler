(defn is-perfect-square? [n]
  (= (Math/pow (int (Math/pow n 0.5)) 2)
     (float n)))

(defn special-triplet-product []
  (for [x (range 1 500)
        y (range x 500)
        :let [z (+ (* x x) (* y y))]
        :when (and (is-perfect-square? z)
                   (= (+ x y (int (Math/pow z 0.5))) 1000))]
    (* x y (int (Math/pow z 0.5)))))

(println (first (special-triplet-product)))


