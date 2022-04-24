# Copyright 2022 rajitsaria
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import string
import pandas as pd
import datetime
from scipy import optimize
from sympy import Add 

def listOfTuples(list1, list2):
    #make a list of tuples having an element from each list
    return list(map(lambda x, y:(x,y), list1, list2))

def secant_method(tol, f, x0):
    x1 = x0*1.1
    while (abs(x1-x0)/abs(x1) > tol):
        x0, x1 = x1, x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
    return x1

def xnpv(rate,cashflows):

    chron_order = sorted(cashflows, key = lambda x: x[0])
    t0 = chron_order[0][0] #t0 is the date of the first cash flow

    return sum([cf/(1+rate)**((t-t0).days/365.0) for (t,cf) in chron_order])

def xirr(cashflows,guess=0.1):

    #return secant_method(0.0001,lambda r: xnpv(r,cashflows),guess)
    return optimize.newton(lambda r: xnpv(r,cashflows),guess)

def readLedger(filename):
    headers = ['particulars', 'posting_date', 'cost_center', 'voucher_type', 'debit', 'credit', 'net_balance']
    dataType = {'particulars': 'str', 'posting_date': 'str', 'cost_center': 'str', 'voucher_type': 'str', 'debit': 'float', 'credit': 'float', 'net_balance': 'float'}
    dateColumns = ['posting_date']
    return pd.read_csv(filename, sep=',', header = 0, names = headers, dtype = dataType, parse_dates = dateColumns, dayfirst=True)

ledgerData = readLedger("ledger.csv")           //provide ledger name here
dateLedger = list(ledgerData["posting_date"])
voucherData = ledgerData['voucher_type'].tolist()
debitData = ledgerData['debit'].tolist()
creditData = ledgerData['credit'].tolist()

combinedFlow = list()

for entryIndex, voucher in enumerate(voucherData):
    if voucher == 'Bank Receipts':
        combinedFlow.append(-1*creditData[entryIndex])
    elif voucher == 'Bank Payments':
        combinedFlow.append(debitData[entryIndex])
    else:
        combinedFlow.append(0)

cashFlow = listOfTuples(dateLedger, combinedFlow)
calculatedXIRR = xirr(cashFlow)
print(calculatedXIRR*100)
