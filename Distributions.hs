module Distributions where

import Data.List
import System.Random
import Control.Monad

{-
getY :: (Floating t) => t -> t -> t -> t
getY m d x = 1.0 / (sqrt (2 * pi * d)) * exp (- (x - m)^2 / (2 * d))

getDistrLine :: (Floating t) => [t] -> [t]
getDistrLine xs = map (* k) xs
	     	  where k = 1 / (head xs)

randomSequence :: (Floating t, Random t, Integral t1) => (t, t) -> t1 -> [t] -> [t]
randomSequence range 0 xs    = xs
randomSequence range seed xs = randomSequence range (seed - 1) (x:xs)
		     	       where x = fst $ (randomR range newGen)
			       		 where newGen = snd $ randomR range (mkStdGen seed)
-- returns an order value, takes one three-tuple, which is a tuple of parameters:
-- mathematical waiting, dispersion and edges (like (1,19))
getOrder :: (Floating t) => (t, t, (t, t ), Int) -> Maybe Int
getOrder (m, d, (l, r), seed) = findIndex (\x -> x >= y) (tail (scanl (+) 0 line))
	   		  	where line = map round (getDistrLine (map (getY m d) [l..r]))
				      y    = randomSequence (l, upperBound) seed [] !! seed
		     		             where upperBound = sum line
-}

geomDecide :: Int -> Int
geomDecide day =
  | liftM2 (<) rand (return (getGeomDistr (1, 20) !! day) :: IO Double) = 0
  | otherwise = 1
  
getGeomDistr :: (Double, Double) -> [Double]
getGeomDistr = undefined

rand :: IO Double
rand = undefined
