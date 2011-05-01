module Main where

import System

main :: IO ExitCode
main = do
  args <- getArgs
  exitWith ExitSuccess
