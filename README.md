# xirr_calculator_zerodha
Python based command line tool to calculate XIRR from Zerodha funds statement

This takes input as the Zerodha funds statement as input to calculate XIRR. Along with that it takes the date and portfolio value for which the XIRR needs to be calculated

##Calculation
It takes voucher comment Bank Receipts as negative cash flow and withdrawals as positive cashflow. So all charges are taken into account. Only dividends are not taken in the calculation. If you want you can add them manually in the ledger by keeping voucher column as 'Bank Payments' and adding the correct date and amount.

## How to get Funds Statement from Zerodha
1. Open console.zerodha.com
2. Click on Funds in the header banner to reveal the dropdown manner
3. Click on Statement from the dropdown menu
4. Select the date range. For now XIRR can only be calculated since the beginning of the account.
5. Download the csv format statements file

## How to get current Account value
1. Open https://console.zerodha.com/dashboard
2. You will see Account Value displayed which includes Equity Holdings and funds balance

## Requirements
Python 3.x
Modules: PyXIRR and datetime

Install Pyxirr: pip install pyxirr
Install datetime: pip install DateTime

## How to run the tool
1. Download the tool from the GitHub repo
2. Copy Zerodha funds ledger to the same folder
3. Open command prompt or Windows Powershell in the same folder. One way is to hold shift key, right click in the folder and select 'Open Powershell window here'
5. Run the python script by entering 'python .\xirr_cal_pyxirr.py' in powershell
6. Enter the date in 'dd-mm-yyyy' format, Account value and file name of the zerodha funds statement

## SciPy based tool
You can find the SciPy based python file under the SciPy folder. It works but will no longer be updated. Simply because PyXIRR module is faster and simpler. Adding that in case people want to create their own versions or include in their workflows. SciPy might be more versatile in that case.

## Acknowledgements

User @Anexen (Alexander Volkovsky) for the PyXIRR library (https://github.com/Anexen/pyxirr)
StackOverflow question and answer https://stackoverflow.com/questions/46668172/calculating-xirr-in-python
