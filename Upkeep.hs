module Upkeep (
  getUpkeep,
  countBound
) where

import Distributions
import Debug.Trace

-- чтобы избежать везде явного выбора типа из класса типов, я не буду париться
-- с оптимизацией памяти и просто буду юзать повсюду Double. Не бейте, если что...
--
-- собственно, главная функция, принимает на вход три параметра - размер заказа, период заказа и 
-- кучу рандомных чисел
getUpkeep :: Double -> Double -> ([Double], [Double]) -> Double
getUpkeep size period (nRnd, gRnd) = getUpkeep' 365 0 period initialStorage (nRnd, gRnd)
-- если счётчик дней достигает нуля, останавливаем рекурсию и возвращаем аккумулированные расходы
-- если он не нулевой, добавляем к текущим расходам расходы на сегодня, вычитаем день и уменьшаем счётчик дней 
-- до поступления следующего заказа
-- если счётчик до заказа становится нулевым, возвращаем ему значение периода и добавляем к расходам сумму за оформление заказа
  where getUpkeep' 0 upkeep remains storage (ns, gs) = upkeep
        getUpkeep' days upkeep remains storage (n:ns, g:gs)
          | remains == 0 = let nStor = newStorage storage (n, g)
                           in getUpkeep' (days - 1) (upkeep + (toDayUpkeep nStor remains)) period nStor (ns, gs)
          | otherwise = let nStor = newStorage storage (n, g)
                        in getUpkeep' (days - 1) (upkeep + (toDayUpkeep nStor remains)) (remains - 1) nStor (ns, gs)

-- изменившийся объём товара на складе (+ привезли - забрали)
newStorage :: Double -> (Double, Double) -> Double
newStorage storage (n, g) = storage - (getNormal (countBound / 2, 5, (1, countBound - 1)) n)
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

-- стоимость одной единицы товара на складе, константа, попросту говоря
unitCost :: Double
unitCost = 1

-- затраты на оформление заказа
orderCost :: Double -> Double
orderCost 0 = 5
orderCost _ = 0

-- первоначальное количество товара на складе
initialStorage :: Double
initialStorage = 100

countBound :: Double
countBound = 20
