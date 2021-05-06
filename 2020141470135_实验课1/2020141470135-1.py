TempStr = input('先输入RMB或USD后输入数：')
if TempStr[0:3]in["RMB"]:
    Trans = float(TempStr[3:])/6.78
    print("USD{:.2f}".format(Trans))
elif TempStr[0:3]in["USD"]:
        F = 6.78*float(TempStr[3:])
        print("RMB{:.2f}".format(F))
