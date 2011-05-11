module Header where

data ConstantParameter = ConstantPeriod | ConstantSize
type CalcParams = (Int, Int, Int, Int, Int, Int, Int, Int, Int, [(Int, Double)], [(Int, Double)])

fixedPeriod :: CalcParams -> Int
fixedPeriod (_, _, x, _, _, _, _, _, _, _, _) = x

fixedSize :: CalcParams -> Int
fixedSize (_, _, _, x, _, _, _, _, _, _, _) = x

maxPeriod :: CalcParams -> Int
maxPeriod (_, _, _, _, x, _, _, _, _, _, _) = x

maxSize :: CalcParams -> Int
maxSize (_, _, _, _, _, x, _, _, _, _, _) = x

initialStorage :: CalcParams -> Int
initialStorage (x, _, _, _, _, _, _, _, _, _, _) = x

countPeriod :: CalcParams -> Int
countPeriod (_, x, _, _, _, _, _, _, _, _, _) = x

ordLine :: CalcParams -> [(Double, Int)]
ordLine (_, _, _, _, _, _, _, _, _, xs, _) = zip (tail (scanl (+) 0 (map (/(sum (map snd xs))) (map snd xs)))) (map fst xs)

delLine :: CalcParams -> [(Double, Int)]
delLine (_, _, _, _, _, _, _, _, _, _, xs) = zip (tail (scanl (+) 0 (map (/(sum (map snd xs))) (map snd xs)))) (map fst xs)

orderCost :: CalcParams -> Int
orderCost (_, _, _, _, _, _, _, x, _, _, _) = x

unitCost :: CalcParams -> Int
unitCost  (_, _, _, _, _, _, x, _, _, _, _) = x

deficitCost :: CalcParams -> Int
deficitCost (_, _, _, _, _, _, _, _, x, _, _) = x

