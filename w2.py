temp=25.0
print(temp)
temp=26.5
print(temp)
count = 0
count =count +10
a="NULL"
print(count)
print(type(count))#輸出count的資料型態
print(type(a))
print(type(temp))

# 資料型態轉換
str1="ID"+"520"
str2="123"+str1
print(str1)
test="第一"+str(count)+"筆"#str(變數)，把變數的資料型態轉成字串
print(test)
print(str2)
#應用
reading="23.7 "
print(reading*2)
value = float(reading)#把reading轉成浮點數
print(f"溫度{value}度")
print(f"兩倍 {value * 2} 度")#要f{}才是變數
#隨堂練習
sensorID="reading"
temprature="30.5"
count=1
print(sensorID )
print(temprature)
print(count)
print(type(sensorID) )#type(變數)輸出資料型態
print(type(temprature))
print(type(count))
a=float(temprature)+0.5
print( sensorID +"=" + str(a) )
