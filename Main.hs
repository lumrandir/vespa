module Main where

import Upkeep
import Distributions
import Graphics.Rendering.Chart.Simple
import Data.List
import System.Random
import Control.Monad

main :: IO ()
main = do
-- сначала достанем верхнее значение нашего нормального распределения
  let upperNormal = getNormalUpperBound (5, 10, (1, 19))
-- теперь сгенерим бесконечный список случайных значений в пределах от 1 до верхнего значения
  let listNormal = getStdGen >>= (\g -> return (randomRs (1, upperNormal) g))
-- теперь проделаем ту же самую фигню для геометрического распределения
  let upperGeom = getGeomUpperBound
  let listGeom = getStdGen >>= (\g -> return (randomRs (1, upperGeom) g))
-- пакуем их в кортеж
  let rnd = liftM2 (\x y -> (x, y)) listNormal listGeom
-- теперь запустим вычисления, вбросив этот кортеж в качестве источников рандомных чисел
--  let fixedPeriodUpkeep = [ getUpkeep x 10 | x <- [1..20] ]
--  let fixedSizeUpkeep   = [ getUpkeep 10 x | x <- [1..20] ]
--  putStrLn "ssss"
--  plotPDF "fixedPeriod.pdf" ([1..20] :: [Double]) (fixedPeriodUpkeep :: [Double]) "Upkeep with constant order period"
--  plotPDF "fixedSize.pdf" ([1..20] :: [Double]) (fixedSizeUpkeep :: [Double]) "Upkeep with constant order size"
--  putStrLn $ "Optimal order size is: " ++ (show (minimum fixedPeriodUpkeep)) ++ "\nOptimal order period is: " ++  (show (minimum fixedSizeUpkeep))
  putStrLn "Hello"

