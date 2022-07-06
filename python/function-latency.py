#!/usr/bin/env python3

import time
import datetime

################################################
# Test function
################################################
 
def testFunction():
  return 

##########################################
# Main app code
##########################################
def main():

  print ("Test latency of function call")
  t1 = time.time_ns()
  print ("Start time:",t1)

  num_of_func_calls = 10000000
  i = num_of_func_calls

  # Call function
  while i>0:
    testFunction()
    i = i-1

  t2 = time.time_ns()
  print ("End time: ",t2)

  t = t2 - t1
  print ("Number of function calls: ",num_of_func_calls)
  print ("Process time:",t,"ns")
  ft = t / num_of_func_calls
  print ("Single function time:", ft, "ns"); 

# Main
main()
