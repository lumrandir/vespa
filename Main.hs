module Main where

import System
import Text.CSV
import System.Random
import Header

main :: IO ExitCode
main =  do
        args <- getArgs
        let params = read $ args !! 0 :: CalcParams
        let (initStorage, countPeriod, fixedPeriod, fixedSize, maxPeriod, maxSize,
                 unitCost, orderCost, deficitCost, ordProbs, delProbs) = params
        fixedPeriodResults <- roll 5 ConstantPeriod params []
        fixedSizeResults <- roll 5 ConstantSize params []
        writeFile "fixedPeriodResults.csv" $ printCSV fixedPeriodResults
        writeFile "fixedSizeResults.csv" $ printCSV fixedSizeResults
        exitWith ExitSuccess

roll :: Int -> ConstantParameter -> CalcParams -> CSV -> IO CSV
roll 0 _ _ results = do
        return results
roll n const params results = do
        r <- rnd
        let x = undefined
        roll (n - 1) const params (x:results)

rnd :: IO [Double]
rnd = do
        newStdGen
        getStdGen >>= (\g -> return $ randomRs (0.0, 1.0) g)
        
