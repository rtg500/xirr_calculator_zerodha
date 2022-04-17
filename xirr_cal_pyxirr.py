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

import pandas as pd
from pyxirr import xirr
import datetime


def listOfTuples(list1, list2):
    #make a list of tuples having an element from each list
    return list(map(lambda x, y:(x,y), list1, list2))

def readLedger(filename):
    #read ledger file from Zerodha in a specified format
    headers = ['particulars', 'posting_date', 'cost_center', 'voucher_type', 'debit', 'credit', 'net_balance']
    dataType = {'particulars': 'str', 'posting_date': 'str', 'cost_center': 'str', 'voucher_type': 'str', 'debit': 'float', 'credit': 'float', 'net_balance': 'float'}
    dateColumns = ['posting_date']
    return pd.read_csv(filename, sep=',', header = 0, names = headers, dtype = dataType, parse_dates = dateColumns, dayfirst=True)

#take inputs from user
endDate = pd.to_datetime(input("Enter Date for end of investment period in dd-mm-yyyy format: "), format= '%d-%m-%Y')
fundBalance = float(input("Enter the final portfolio value including fund balance: "))
ledgerData = readLedger(input("Enter funds ledger name: "))

dateLedger = list(ledgerData["posting_date"])
voucherData = ledgerData['voucher_type'].tolist()
debitData = ledgerData['debit'].tolist()
creditData = ledgerData['credit'].tolist()

combinedFlow = list()

for entryIndex, voucher in enumerate(voucherData):
    if voucher == 'Bank Receipts':
        #all deposits to Zerodha funds are treated as negative flow
        combinedFlow.append(-1*creditData[entryIndex])
    elif voucher == 'Bank Payments':
        #all withdrawals to account are treated as positive flow
        combinedFlow.append(debitData[entryIndex])
    else:
        combinedFlow.append(0)

dateLedger.append(endDate)
combinedFlow.append(fundBalance)
calculatedXIRR = xirr(dateLedger, combinedFlow)
print(calculatedXIRR*100)
