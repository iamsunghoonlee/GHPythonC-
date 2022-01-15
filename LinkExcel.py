"""This is a simple component used for loading excel files.
    Inputs:
        filePath: Connect to "filepath" component in GH as "item access", data "string"
    Output:
        a: The a output variable"""

import Rhino.Geometry as rg
import clr
clr.AddReference("Microsoft.Office.Interop.Excel")
import Microsoft.Office.Interop.Excel as excel

#Excel
ex = excel.ApplicationClass()

#Open Workbook
workbook = ex.Workbooks.Open(filePath)

#Read Workbook
ws = workbook.Worksheets[1]

""" Use this setion for what you want to do with Excel data
pX = []
pY = []
pZ = []

for i in range(ws.UsedRange.Rows.Count):
    if i == 0:
        continue
    
    x = ws.Range("A{}".format(i + 1)).Value2
    y = ws.Range("B{}".format(i + 1)).Value2
    z = ws.Range("C{}".format(i + 1)).Value2
    
    pX.append(x)
    pY.append(y)
    pZ.append(z)

"""
workbook.Close(False)
ex.Quit()
""" Output of you code
a = pX
b = pY
c = pZ
"""