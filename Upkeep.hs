module Upkeep where

import Distributions
import Debug.Trace
import Data.List

getUpkeep :: (Double, Double) -> ([Double], [Double]) -> Double
getUpkeep (size, period) (nRands, gRands) = getUpkeep' (365, period) (initialStorage, []) 0 (nRands, gRands)
  where getUpkeep' (0, _) _ u _ = u
        getUpkeep' (r, 0) (s, q) u (n:ns, g:gs) = getUpkeep' (r - 1, period) (today (s, (1:q)) (n, g) size) (u + positive (fst (today (s, (1:q)) (n, g) size)) * unitCost + orderCost) (ns, gs)
        getUpkeep' (r, t) sq u (n:ns, g:gs) = getUpkeep' (r - 1, t - 1) (today sq (n, g) size) (u + positive (fst (today sq (n, g) size)) * unitCost) (ns, gs)

today :: (Double, [Double]) -> (Double, Double) -> Double -> (Double, [Double])
today (s, q) (n, g) size = (s - (taken n) + (fst (delivered q g size)), snd (delivered q g size))

taken :: Double -> Double
taken n = (getNormal (countBound / 2, 5, (1, countBound - 1)) n)

isDelivered :: Double -> Double -> Bool
isDelivered g n = g <= (getGeom 0.7 (1, countBound - 1)) !! (round (n - 1) :: Int)

delivered :: [Double] -> Double -> Double -> (Double, [Double])
delivered q g size = let src = mapAccumL (\acc x -> case isDelivered g x of
                                                      True -> (acc + size, 0)
                                                      False -> (acc, x + 1)
                                         ) 0 q
                     in (fst src, filter (/= 0.0) (snd src))
{-
getUpkeep :: Double -> Double -> ([Double], [Double]) -> Double
getUpkeep size period (nRnd, gRnd) = getUpkeep' 365 0 period initialStorage (nRnd, gRnd) []
-- если счётчик дней достигает нуля, останавливаем рекурсию и возвращаем аккумулированные расходы
-- если он не нулевой, добавляем к текущим расходам расходы на сегодня, вычитаем день и уменьшаем счётчик дней 
-- до поступления следующего заказа
-- если счётчик до заказа становится нулевым, возвращаем ему значение периода и добавляем к расходам сумму за оформление заказа
  where getUpkeep' 0 upkeep _ _ _ _ = upkeep
        getUpkeep' days upkeep remains storage (n:ns, g:gs) orderQueye
          | remains == 0 = let nStor = fst $ newStorage storage (n, g) orderQueye size
                               nQueye = 1 : (snd (newStorage storage (n, g) orderQueye size))
                           in getUpkeep' (days - 1) (upkeep + (toDayUpkeep nStor remains)) period nStor (ns, gs) nQueye
          | otherwise = let nStor = fst $ newStorage storage (n, g) orderQueye size
                            nQueye = snd $ newStorage storage (n, g) orderQueye size
                        in getUpkeep' (days - 1) (upkeep + (toDayUpkeep nStor remains)) (remains - 1) nStor (ns, gs) nQueye

-- изменившийся объём товара на складе (+ привезли - забрали)
newStorage :: Double -> (Double, Double) -> Double -> [Double] -> (Double, [Double])
newStorage storage (n, g) size queye = (storage - taken + fst (deliver queye g) * size, snd (deliver queye g)) 
  where taken = (getNormal (countBound / 2, 5, (1, countBound - 1)) n)
-}
positive :: Double -> Double
positive s | s > 0 = s
           | otherwise = 0
{-
deliver :: [Double] -> Double -> (Double, [Double])
deliver q g = mapAccumL (\acc x -> case delivered x g of
                                    True -> (acc + 1, 0)
                                    False -> (acc, x + 1)
                        ) 0 q

delivered = undefined
--)
-- расходы за сегодня равны сумме на хранение товара, который уже есть
-- за вычетом суммы на хранение товара, который сегодня забрали
-- плюс сумма на хранение товара, который сегодня (возможно) привезли
-- плюс сумма за оформление заказа, если это необходимо
--
-- очевидно, функция должна принимать текущий объём товара на складе
-- и время, оставшееся до следующего заказа
-- и пару случайных чисел для вычисления спроса и привоза
toDayUpkeep :: Double -> Double -> Double
-- toDayUpkeep storage remains | trace ("storage " ++ (show storage)) False = undefined
toDayUpkeep storage remains = positive storage * unitCost + (orderCost remains)
  where positive s | s > 0 = s
                   | otherwise = 0
-}
-- стоимость одной единицы товара на складе, константа, попросту говоря
unitCost :: Double
unitCost = 1

-- затраты на оформление заказа
orderCost :: Double
orderCost = 5

-- первоначальное количество товара на складе
initialStorage :: Double
initialStorage = 100

-- граница счёта (до какого предела изменяем контролируемый параметр)
countBound :: Double
countBound = 100
