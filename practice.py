#!/usr/bin/env python3
## [1] + [2,3] == [1,2]
## a[0] == 1
## a[1:] == [2,3,4]
a = [1,2,3,4]

# [int] -> [int]
def plus10All(lst):
  return mymap(lst, lambda x: x + 10)

def multtenall(lst):
  fn = lambda x: x * 10
  return mymap(lst, fn)


def mymap(lst, fn):
  if len(lst) == 0:
    return []
  else:
    newList= [fn(lst[0])]
    return newList + mymap(lst[1:], fn)

# [int] -> int
def sum(lst):
  if len(lst) == 0:
    return 0
  else: 
    return lst[0]+ sum(lst[1:])

def product(lst):
  if len(lst) == 0:
    return 1
  else:
    return lst[0] * product(lst[1:])

#[x] -> ( x -> y -> y) -> y -> y
def foldr(lst, fn, unit):
  if len(lst) == 0:
    return unit
  else:
    return fn(lst[0], foldr(lst[1:], fn, unit))

def foldl(lst, fn, unit):
  if len(lst) == 0:
    return unit
  else:
    return foldl(all_but_first(lst), fn, fn(unit, first(lst)))


def foldl(lst, fn, unit):
  while len(lst) > 0:
    unit = fn(unit, first(lst))
    lst = all_but_first(lst)
  return unit

#foldr(lst, monoid) -- monoid == [binary_fn,unit] 

def product2(lst):
  return foldr(lst, lambda x, acc: x * acc, 1)

def sum2(lst):
  return foldr(lst, lambda x, acc: x + acc, 0)

def map2(lst, fn):
  return foldr(0lst, lambda x, acc: [fn(x)] + acc,[])

## [x] -> x -> [x] ==== intercalate(["1","2","3","4","5"], "x")== 
#["1", "x", "2", "x", "3", "x", "4", "x", "5"]

def intercalate(lst, x):
  interhelper = lambda y, acc: [x, y] + acc
  return foldr(lst, interhelper, [])[1:]

def join(lst, el):
  return foldr(intercalate(lst, el), lambda x, acc: x + acc, "")

def insert(dct, key, val):
  dct[key]=val
  return dct


def deepMap(dct, fn):
  mapDictionaryValue = lambda key, dctnew: insert(dctnew, key, deepMap(dct[key], fn))
  if type(dct) == dict:
    return foldr([*dct.keys()], mapDictionaryValue, {})
  else:
    if type(dct) == list:
      return mymap(dct, lambda x: deepMap(x, fn))
    else:
      return fn(dct)


def id(x):
  return x

def deepCopy(dct):
  return deepMap(dct, id)

def first(lst):
  return lst[0]

def last(lst):
  return lst[-1]

def all_but_first(lst):
  return lst[1:]

def all_but_last(lst):
  return lst[:-1]

def length(lst):
  return 0 if lst == [] else 1 + length(all_but_last(lst))

def reverseR(lst):
  return foldr(lst, lambda x, acc:  acc + [x], [])

def reverse(lst):
  return foldl(lst, lambda acc, x: [x] + acc, [])

## foldl takes a list, a helper function, and a unit
## the unit is what you get when the list is empty
## otherwise, you construct the helper function as follows:

# helper(acc, x) if it's foldl, and helper(x, acc) if it's foldr
# given that we are trying to use foldl since we are in python
# 

# crossproduct : [x] -> [y] -> [[x,y]]
# crossproduct([1,2,3], [4,5,6]) == [[1,4], [1,5], [1,6], [2,4], [2,5], [2,6], [3,4], [3,5], [3,6]]
def crossproduct(lst1,lst2):
  ...

def any_p(lst, boolean_fn):
  ...

def all_p(lst, boolean_fn):
  ...

def append(list1,list2):
  ...

def transpose(lst_of_lists):
  ...

def subsequences(lst):
  ...

def intercalate(lst, lst_of_lsts):
  ...

def permutations(lst):
  ...

def deepZip(dct1, dct2):
  ...

def deepMerge(dct1 , dct2):
  ...


example_dict = {
  "a": 1, 
  "b": 2, 
  "c": {
    "d": 3, 
    "e": {
      "f": 4
     }
  },
  "z": [ 1, 2, 3, [ 4 , 5 ], {"foo": 7}]
}

deepMap(example_dict, lambda x: x * 10)

{
  "a": 10,
  "b": 20,
  "c": {
    "d": 30,
    "e": {
      "f": 40
    }
  },
  "z": [ 10, 20, 30, [ 40 , 50 ], {"foo": 70} ]
}
## you will need to look up the following: how do i figure out if something is a dictionary in python?
dct={}
 type(dct) == dict
## how do i get a list of keys from a dictionary
dct.keys()
## foldr across the list of keys to produce a new dictionary ({} will be your unit)






