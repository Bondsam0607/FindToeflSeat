from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://toefl.neea.edu.cn/')
time.sleep(60)

citiesList = ['NINGBO','SHANGHAI','SUZHOU','NANJING','TAICANG','HANGZHOU']
dateList = ['2020-05-10','2020-05-16','2020-05-24','2020-05-30','2020-06-13','2020-06-14','2020-06-20','2020-07-04','2020-07-05','2020-07-11','2020-08-16','2020-08-16','2020-08-22','2020-08-23','2020-08-23','2020-08-29','2020-08-30']
data = []

for city in citiesList:
    print(city)
    for date in dateList:
        js = 'return $.getJSON("testSeat/queryTestSeats",{city: "' + city + '",testDay: "' + date + '"});'
        dataJSON = driver.execute_script(js)
        date_str = "".join(date.split('-'))
        if dataJSON['status']==True:
            print(date_str)
            for info in dataJSON['testSeats']['09:00|'+date_str+'|08:30']:
                tmp = []
                tmp.append(date)
                tmp.append(info['centerCode'])
                tmp.append(info['centerNameCn'])
                tmp.append(info['seatStatus'])
                data.append(tmp)
            time.sleep(1)

seat = pd.DataFrame(data)
seat.columns = ['date','centerCode','centerName','seatStatus']
seat[seat.seatStatus==1]
empty = seat.sort_values(by='date', ascending = True)[seat.seatStatus==1]