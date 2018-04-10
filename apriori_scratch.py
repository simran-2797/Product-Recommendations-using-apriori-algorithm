#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 11:38:03 2018

@author: simranmhatre
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import math

dataset = pd.read_csv('/Users/simranmhatre/Desktop/MachineLearning/MarketBasket/Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])
set_transactions = list(map(set,transactions))

    
#----------------------------------FUNCTIONS-----------------------------------------------  
def getsupport(small_set,set_transactions):
    count = getcount(small_set,set_transactions)
    support = count / len(set_transactions)
    return support

          
def getcount(small_set,set_transactions):
    count = 0
    for i in range(len(set_transactions)):
        if small_set.issubset(set_transactions[i]):
            count = count + 1
    return count

def formck(prev_ck):
    newck = list()
    newset = set()
    for i in range(len(prev_ck)):
        for j in range(i+1,len(prev_ck)):
            newset = prev_ck[i].union(prev_ck[j])
            if newset not in newck:
                newck.append(newset)
    return newck

def fun_small_list(newck,set_transactions):
    small_list = list()
    for i in range(len(newck)):
        support = getsupport(newck[i],set_transactions)
        if support > 0.00:
            small_list.append(newck[i])
    return small_list

def findsubsets(rule_set):
    subset = list()
    for i in range(len(big_list)):
        temp = big_list[i]
        for j in range(len(temp)):
            if temp[j].issubset(rule_set) and len(temp[j]) != len(rule_set):
               subset.append(temp[j])
    return subset  

def generaterules(big_list,set_transactions):
    list_of_rules = list()
    for i in range(len(big_list)-1,0,-1):
        temp = big_list[i]
        for j in range(len(temp)):
            subsets = list()
            subsets = findsubsets(temp[j])
            for a in range(len(subsets)):
                lhs = subsets[a]
                for b in range(len(subsets)):
                   if len(subsets[a]) + len(subsets[b]) == len(temp[j]):
                       if not subsets[a].issubset(subsets[b]) and not subsets[b].issubset(subsets[a]):
                           comb = subsets[a].union(subsets[b])
                           denom = subsets[a]
                           confidence = getconfidence(comb,denom,set_transactions)
                           if confidence > 0.009:
                               small = list()
                               small.append(subsets[a])
                               small.append(subsets[b])
                               list_of_rules.append(small)
    return list_of_rules

def getconfidence(comb,denom,set_transactions):
    n = getcount(comb,set_transactions)
    d = getcount(denom,set_transactions)
    confidence = n/d
    return confidence 
#-----------Code-----------------

#step 1 : make initial ck list
new_ck = list()
for i in range(len(transactions)):
    temp = transactions[i]
    for j in range(0,len(temp)):
        if temp[j] not in new_ck and temp[j] != 'nan':
            new_ck.append(temp[j])
            
set_ck = list()
for i in range(len(new_ck)):
    s = set({new_ck[i]})
    set_ck.append(s)

big_list = list()
small_list = fun_small_list(set_ck,set_transactions)
big_list.append(small_list)
count = 0
while count < 3:
     prev_ck = small_list
     small_list = list()
     new_ck = formck(prev_ck)
     small_list = fun_small_list(new_ck,set_transactions)
     if len(small_list) != 0:
         big_list.append(small_list)
         count = count + 1 
     else:
         break


list_of_rules = list()    
list_of_rules = generaterules(big_list,set_transactions)

print("######--------Welcome to Tasty Super Market---------######" )
print("Here is a list of products we have....")
for i in range(len(big_list[0])):
    temp = big_list[0]
item = set({input("What would you like to buy??")})

recommendations = list()
temp = big_list[len(big_list)-1]
for j in range(len(temp)):
    if item.issubset(temp[j]):
        temp1 = big_list[0]
        for i in range(len(temp1)):
            if temp1[i].issubset(temp[j]) and temp1[i] not in recommendations:
                recommendations.append(temp1[i])
                
recommendations            
            


            

            
    





        
    
    

            


        
            