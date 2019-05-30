#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import csv
import functools as f
import statistics
import matplotlib.pyplot as plt
import plotly as plotly
import plotly.plotly as py
import plotly.graph_objs as go
import scipy.stats as st
import seaborn as sns
import subprocess as sp

# _p == returns true or false
# _e == computation performs side effects
# _i == computation ask_ios for user input
# _o == computation provides output to user
# _io == computation ask_ios for input and provides output to user

VALID_FILE_TYPES= ["csv"]
VALID_DATA_KINDS= ["gene_enrichment"]
VALID_ANALYSES= {
  "gene_enrichment": ["pathways"]
}

def exec(command):
  return sp.check_output(command,shell=True)

def any_p(lst, bool_fn):
  return f.reduce(lambda acc, x: acc | bool_fn(x), lst, False)

def all_p(lst, bool_fn):
  return f.reduce(lambda acc, x: acc & bool_fn(x), lst, True)

def exists_p(filepath):
  try:
    return sp.check_output("ls " + filepath, shell=True)[0:2] != "ls:"
  except:
    return False

def append(el, lst):
  lst.append(el)
  return lst

def my_map(lst, fn):
  return f.reduce(lambda mapped_lst_so_far, elem: 
    append_e(fn(elem),mapped_lst_so_far), lst, [])

def filter(lst, bool_fn):
  add_to_filter = lambda filtered_lst_so_far, x: append(x, filtered_lst_so_far) if bool_fn(x) else filtered_lst_so_far
  return f.reduce(add_to_filter, lst, [])
# the bottom two instances of code are exactly equal in outcome
#xs=[1,2,3]

#sum = 0
#for x in xs:
#  sum = sum + x

#f.reduce(lambda acc, x: acc+x, xs, 0)

def main():
  ## define the input data
  input_metadata = define_input_metadata()
  ## set up analyses based on what data is available
  output_files = run_analysis(input_metadata)
  print("Your data is available at: ")
  map(lambda y: map(lambda x: print(x), y), output_files)
  return output_files

def define_input_metadata():
  input_file_paths = get_input_file_paths_io()
  if all_p(input_file_paths, exists_p):
    file_types = get_file_types_for_files(input_file_paths)
    data_kinds = get_data_kinds_for_files(input_file_paths)
    input_metadata = [*zip(input_file_paths, file_types, data_kinds)]
    return input_metadata
  else:
    print("The following input files could not be found: ")
    [*map(lambda x: print(x), filter(input_file_paths, lambda x: not(exists_p(x))))]
    return define_input_metadata()


def run_analysis(input_metadata):
  # input_metadata is a lst of (filepath, filetype, datakind) triples
  analysis_kinds = ask_io("What kind(s) of analysis would you like to run?", VALID_ANALYSES)
  result_comparison_kinds = ask_io("What would you like to compare your results against?", result_comparisons(analysis_kinds))
  output_file_paths = ask_io("Where would you like to store the results?")
  analysis = gsea_analysis(input_metadata, analysis_kinds, result_comparison_kinds, output_file_paths)
  return [analysis, output_file_paths]

## analysis helpers

def gsea_analysis(input_metadata, analysis_metadata, result_comparisons, output_file_paths):
  sp.check_output("echo 'hi' ", shell=True)

def result_comparisons(analysis_kinds):
  return None


## input helpers

def get_file_types_for_files(input_file_paths):
  path_fn = lambda path: path.split(".")[-1] if len(path.split(".")) >= 2 else ask_io("What file type is " + path + "?", VALID_FILE_TYPES)
  return map(path_fn, input_file_paths)

def get_data_kinds_for_files(input_file_paths):
  path_fn = lambda path: ask_io("What kind of data is " + path + "?", VALID_DATA_KINDS)
  return map(path_fn, input_file_paths)

def get_input_file_paths_io():
  return [*map(lambda x: x.strip(), ask_io("Where are the (comma-separated) file(s) you would like to analyze? (e.g. hello.txt,/local/foo.csv )").split(","))]

def file_type_not_present_in(file_paths):
  #For now we're only going to look for csv
  #And we will assume there is only one file_path in file_paths
  file_paths


# ask_io
def ask_io(question, answers=None):
  if type(answers) == list:
    if len(answers) == 1:
      return answers[0]
    else:
      print(question)
      ## if input answer is in answers list, return answer
      ## else say sorry, the answer must be one of, print the answers list
      ## and then call ask_io again with the same question and answers
      print("( the answer must be one of: " + ", ".join(answers) + " )")
      answer = input()
      if answer in answers:
        return answer
      else:
        if all_p(answer.split(","), lambda resp: resp in answers):
          return answer.split(",")
        else:
          return ask_io(question, answers)
  else:
    if type(answers) == dict:
      True
      #print("why did you give me a dictionary?")
    else: 
      print(question)
      return input()

def add_io(response):
  print("not actually doing anything")

main()