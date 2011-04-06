module Main where

import Upkeep
import Distributions
import Graphics.Rendering.Chart.Simple
import Data.List
import System.Random
import Control.Monad
import Maybe

main :: IO ()
main = do
-- сначала достанем верхнее значение нашего нормального распределения
  let upperNormal = getNormalUpperBound (10, 5, (1, 19))
-- теперь сгенерим бесконечный список случайных значений в пределах от 1 до верхнего значения
  let listNormal = getStdGen >>= (\g -> return (randomRs (1, upperNormal) g))
-- теперь проделаем ту же самую фигню для геометрического распределения
  let upperGeom = getGeomUpperBound 0.7 (1, 19)
  let listGeom = getStdGen >>= (\g -> return (randomRs (1, upperGeom) g))
-- пакуем их в кортеж
  let rnd = liftM2 (\x y -> (x, y)) listNormal listGeom
-- теперь запустим вычисления, вбросив этот кортеж в качестве источников рандомных чисел
  let fixedPeriodUpkeep = rnd >>= (\r -> return ([ getUpkeep x 10 r | x <- [1..20] ]))
  let fixedSizeUpkeep = rnd >>= (\r -> return ([ getUpkeep 10 x r | x <- [1..20] ]))
-- рисуем графики
  fpu <- fixedPeriodUpkeep
  fsu <- fixedSizeUpkeep
  plotPDF "fixedPeriod.pdf" ([1..20] :: [Double]) (fpu) "Upkeep with constant order period"
  plotPDF "fixedSize.pdf" ([1..20] :: [Double]) (fsu) "Upkeep with constant order size"
-- ищем оптимальные значения
  let optimalSize = fromJust (findIndex (== (minimum fpu)) fpu) + 1
  let optimalPeriod = fromJust (findIndex (== (minimum fsu)) fsu) + 1
  putStrLn $ "Optimal order size is: " ++ (show optimalSize) ++ "\nOptimal order period is: " ++  (show optimalPeriod)

