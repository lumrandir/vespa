module Main where

import System
import Text.CSV
import System.Random
import Header
import Upkeep

main :: IO ExitCode
main =  do
        args <- getArgs
        let params = read $ args !! 0 :: CalcParams
        randoms <- rnd
        let fixedPeriodResults = [result | value <- [ fixedPeriod params, fixedPeriod params + 1, fixedPeriod params - 1],
                                         let result = getUpkeepList ConstantPeriod params value randoms, 
                                         value > 0]
        let fixedSizeResults = [result | value <- [ fixedSize params, fixedSize params + 1, fixedSize params - 1],
                                       let result = getUpkeepList ConstantSize params value randoms, 
                                       value > 0]
        writeFile "fixedPeriodResults.csv" $ printCSV fixedPeriodResults
        writeFile "fixedSizeResults.csv" $ printCSV fixedSizeResults
        exitWith ExitSuccess

rnd :: IO [Double]
rnd = do
        newStdGen
        getStdGen >>= (\g -> return $! randomRs (0.0, 1.0) g)
        
