module Upkeep where

import Distributions
import Debug.Trace
import Data.List
import Header
import Data.Maybe
import Text.CSV

getUpkeepList :: ConstantParameter -> CalcParams -> Int -> [Double] -> Record
getUpkeepList cp params value randoms = let lines = (ordLine params, delLine params) in 
                                        case cp of
                                                ConstantPeriod -> [ getUpkeep params (initialStorage params, countPeriod params)
                                                        (s, value) randoms |
                                                        s <- [1 .. maxSize params] ]
                                                ConstantSize -> [ getUpkeep params (initialStorage params, countPeriod params)
                                                        (value, p) randoms |
                                                        p <- [1 .. maxPeriod params] ]
                                                

getUpkeep :: CalcParams -> (Int, Int) -> (Int, Int) -> [Double] -> Field
getUpkeep params (is, cp) (size, period) rands = getUpkeep' (cp, period) (is, [], 0) rands
        where getUpkeep' (0, _) (_, _, u) _ = show $ round $ (fromIntegral u :: Double) / (fromIntegral cp :: Double)
              getUpkeep' (r, 0) (s, q, u) (r1:(r2:rs)) = getUpkeep' (r - 1, period) (newState params (r1, r2) size
                (s, 1:q, u + orderCost params)) rs
              getUpkeep' (r, t) state (r1:(r2:rs)) = getUpkeep' (r - 1, t - 1) (newState params (r1, r2) size state) rs

newState :: CalcParams -> (Double, Double) -> Int -> (Int, [Int], Int) -> (Int, [Int], Int)
newState params (r1, r2) size (s, q, u) = let newQuery = delivered params size r2 q
                                              newStorage = s - (taken params r1) + fst newQuery
                                          in (newStorage, snd newQuery, u + positive params newStorage)

positive :: CalcParams -> Int -> Int
positive params s 
        | s >= 0 = s * unitCost params
        | s < 0 = -1 * s * deficitCost params

taken :: CalcParams -> Double -> Int
taken params r = snd $ head $ filter (\(x, _) -> x >= r) (ordLine params)

isDelivered :: CalcParams -> Double -> Int -> Bool
isDelivered params r n = n == snd point 
        where point = head $ filter (\(x, _) -> x >= r) (delLine params)

delivered :: CalcParams -> Int -> Double -> [Int] -> (Int, [Int])
delivered params size r q = let src = mapAccumL (\acc x -> case isDelivered params r x of
                                                      True -> (acc + size, 0)
                                                      False -> (acc, x + 1)
                                                ) 0 q
                            in (fst src, filter (/= 0) (snd src))

