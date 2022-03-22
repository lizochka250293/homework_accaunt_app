import sqlite3
import datetime
def cheack_activ(cur):
    dt_month_now = datetime.datetime.now().date().month
    dt_day_now = datetime.datetime.now().date().day
    data = []
    con = sqlite3.connect('db.sqlite3')
    cursor = con.cursor()
    result = cursor.execute('SELECT * FROM ac_app_accaunt WHERE login = ?',[cur],).fetchone()
    if result != None:
        for row in result:
            data.append(row)
        con.close()
        if len(data)>0:
            for arg in range(len(data)):
                date_start = data[3]
            date_start_date_time = datetime.datetime.strptime(date_start, '%Y-%m-%d %H:%M:%S.%f')
            month_start = date_start_date_time.date().month
            day_start = date_start_date_time.date().day
            if (dt_month_now - month_start >= 1) and (abs(dt_day_now - day_start))>=1:


                choose = str(input("Продлить подписку? "))
                if choose.lower() == 'yes':
                    return f'Пользователь, {cur}, приятного просмотра'

                elif choose.lower() == 'no':
                    return f'Данное видио доступно только подписчикам. Продлить подписку?'
            else:
                print(f'Пользователь, {cur}, приятного просмотра')
    else:
        while True:
            choose_2 = str(input("Данное видио доступно по подписке. Хотите оформить? "))
            if choose_2.lower() == 'yes':
                print(f'Пользователь, {cur}, приятного просмотра')
                break

            elif choose_2.lower() == 'no':
                break




cheack_activ(cur = 'xsacdv@yandex.ru')

