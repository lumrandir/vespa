module Main where

import Upkeep
import Distributions
import Graphics.Rendering.Chart.Simple
import Data.List
import System.Random
import Control.Monad
import Maybe

fixedSize :: Double
fixedSize = 10

fixedPeriod :: Double
fixedPeriod = 10

main :: IO ()
main = do
-- получим данные
  fpu <- roll False countBound []
  fsu <- roll True countBound []
-- отрисуем графики:
  plotPDF "fixedPeriod.pdf" [1..countBound] fpu "Upkeep with constant order period"
  plotPDF "fixedSize.pdf" [1..countBound] fsu "Upkeep with constant order size"
-- ищем оптимальные значения
  let optimalSize = fromJust (findIndex (== (minimum fpu)) fpu) + 1
  let optimalPeriod = fromJust (findIndex (== (minimum fsu)) fsu) + 1
  putStrLn $ "Optimal order size is: " ++ (show optimalSize) ++ "\nOptimal order period is: " ++  (show optimalPeriod)

rnd :: IO ([Double], [Double])
rnd = do
-- обновим генератор
  newStdGen
-- найдём границы
  let upperNormal = getNormalUpperBound (countBound / 2, 5, (1, countBound - 1))
  let upperGeom = getGeomUpperBound 0.7 (1, countBound - 1)
-- получим списки рандомов
  let listNormal = getStdGen >>= (\g -> return (randomRs (1, upperNormal) g))
  let listGeom = getStdGen >>= (\g -> return (randomRs (1, upperGeom) g))
-- упакуем и отошлём их
  liftM2 (\x y -> (x, y)) listNormal listGeom

roll :: Bool -> Double -> [Double] -> IO [Double]
roll t 0 acc = do
  return acc
roll t x acc = do
  r <- rnd
  let u = case t of
            True -> getUpkeep fixedSize x r
            False -> getUpkeep x fixedPeriod r
  roll t (x - 1) (u:acc)
 
