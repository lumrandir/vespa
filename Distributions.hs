module Distributions where

import Data.List

getY :: Double-> Double-> Double -> Double
getY m d x = 1.0 / (sqrt (2 * pi * d)) * exp (- (x - m)^2 / (2 * d))

getDistrLine :: [Double] -> [Double]
getDistrLine xs = map (* k) xs
	     	  where k = 1 / (head xs)

-- returns an order value, takes one three-tuple, which is a tuple of parameters:
-- mathematical waiting, dispersion and edges (like (1,19))
getNormal :: (Double, Double, (Double, Double)) -> Double -> Maybe Int
getNormal (m, d, (l, r)) rnd = findIndex (\x -> x >= rnd) (tail (scanl (+) 0 line))
  where line = getDistrLine $ map (getY m d) [l..r]

getNormalUpperBound (m, d, (l, r)) = sum list
  where list = tail $ scanl (+) 0 line
        line = getDistrLine $ map (getY m d) [l..r]

getGeom :: (Double, Double) -> [Double]
getGeom = undefined

