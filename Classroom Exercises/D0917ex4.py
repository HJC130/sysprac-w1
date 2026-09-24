adc=float(input("輸入一個 ADC 原始值（0～4095）:"))
voltage = adc/4096*3.3
current=float(input("輸入電流（安培）："))
power=voltage*current
print("--量測報告--")
print(f"電壓:{voltage:.2f} V")
print(f"電流:{current:.2f} A")
print(f"功率:{power:.2f} W")