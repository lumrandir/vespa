module Upkeep (
  getUpkeep
) where

getUpkeep :: Int -> Double -> Double -> Double
getUpkeep 0 size period = undefined
getUpkeep 1 size period = undefined

-- функция должна принимать:
--  текущее количество товара на складе
--  число дней, оставшихся до поступления следующего заказа
-- вроде бы этого достаточно...
-- возвращать будет, естессно Double - величина затрат за текущий день
-- итак, если имеем ноль на входе там, где должны быть дни до заказа,
-- расходы формируем как сумму затрат на заказ orderCost и затрат на хранение единицы
-- unitCost (в случае дефицита просто берём модуль)
dayUpkeep :: Double -> Double -> Double
dayUpkeep storage 0 = storage * unitCost + orderCost

-- стоимость одной единицы товара на складе, константа, попросту говоря
unitCost :: Double
unitCost = 1

-- затраты на оформление заказа
orderCost :: Double
orderCost = 5

