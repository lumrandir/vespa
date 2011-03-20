module Main where

import Upkeep
import Graphics.Rendering.Chart.Simple
import Data.List

main :: IO ()
main = do
  let fixedPeriodUpkeep = [ getUpkeep x 10 | x <- [1..20] ]
  let fixedSizeUpkeep   = [ getUpkeep 10 x | x <- [1..20] ]
--  putStrLn "ssss"
--  plotPDF "fixedPeriod.pdf" ([1..20] :: [Double]) (fixedPeriodUpkeep :: [Double]) "Upkeep with constant order period"
--  plotPDF "fixedSize.pdf" ([1..20] :: [Double]) (fixedSizeUpkeep :: [Double]) "Upkeep with constant order size"
--  putStrLn $ "Optimal order size is: " ++ (show (minimum fixedPeriodUpkeep)) ++ "\nOptimal order period is: " ++  (show (minimum fixedSizeUpkeep))
  putStrLn "Hello"

