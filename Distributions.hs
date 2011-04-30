module Distributions where

import Data.List
import Maybe
import Debug.Trace

getNormalY :: Double-> Double-> Double -> Double
getNormalY m d x = 1.0 / (sqrt (2 * pi * d)) * exp (- (x - m)^2 / (2 * d))

getDistrLine :: [Double] -> [Double]
getDistrLine xs = map (* k) xs
	     	  where k = 1 / (head xs)

getNormal :: (Double, Double, (Double, Double)) -> Double -> Double
getNormal (m, d, (l, r)) rnd = fromIntegral $ fromJust $ findIndex (>= rnd) (tail (scanl (+) 0 line)) :: Double
  where line = getDistrLine $ map (getNormalY m d) [l..r]

getNormalUpperBound :: (Double, Double, (Double, Double)) -> Double
getNormalUpperBound (m, d, (l, r)) = head $ reverse list
  where list = tail $ scanl (+) 0 line
        line = getDistrLine $ map (getNormalY m d) [l..r]

getGeom :: Double -> (Double, Double) -> [Double]
getGeom initialP (l, r) = map (getGeomY initialP) [l..r]

getGeomY :: Double -> Double -> Double
getGeomY p n = 1 - ((1 - p) ** n)

getGeomUpperBound :: Double -> (Double, Double) -> Double
getGeomUpperBound initialP (l, r) = head $ reverse $ map (getGeomY initialP) [l..r]

