# yad avari jasase ghadl
# class method 
# static method 
# class car:
#     def __init__(self , brand , model ,color ):
#         self.brand = brand 
#         self.model = model
#         self.color = color


#     km = 0
#     # isinstance method 
#     def move(self):
#         print("drivig")

#     @classmethod
#     def default(cls):
#         return cls("new car" , 2026 ,"no color")
    
# c1 = car("benz" , 2020 , "black")
# c1.move()
# print(c1.brand)
# c2 = car.default()
# print(c2.brand)
# print(c2.model)
# print(c2.color)

# ---------
# yad avari jasase ghadl
# class method 
# static method 
# class car:
#     def __init__(self , brand , model ,color ):
#         self.brand = brand 
#         self.model = model
#         self.color = color


#     km = 0
#     # isinstance method 
#     def move(self):
#         print("drivig")

#     @classmethod
#     def default(cls):
#         return cls("new car" , 2026 ,"no color")
    
#     @classmethod
#     def change(cls , value):
#         cls.km = value
    
# c1 = car("benz" , 2020 , "black")
# c1.move()
# print(c1.brand)
# c2 = car.default()
# print(c2.brand)
# print(c2.model)
# print(c2.color)

# print(c1.km)
# c1.change(100)
# print(c1.km)

# -------
# yad avari jasase ghadl
# class car:
#     def __init__(self , brand , model ,color ):
#         self.brand = brand 
#         self.model = model
#         self.color = color


#     @ststicmethod
#     def convert():
#         km = int(input(" ->"))
#         return f"{km * 0.62} mails"
    

#     @staticmethod
#     def covert_new(km:int):
#         return f"{km * 0.62} mails"

# c1 = car("benz" , 2020 , "black")

# --------
# moduls
# majol navisi

# from calculation.calculations import show_name
# show_name()
# --------

# barname navis ha beshtareshon az in bara run kardan estefade mikonan
# if __name__ == "__main__":
# s1 = students_info.studentd("mehrdad" , "AI" , "trhran")
# s2 = students_info.studentd("nasim" , "CS" , "shiraz")

# s1_info = s1.gpa_scores()
# print(cal_gpa(
#     s1_info[0] , s1_info[1]
# ))
# print(check_gpa(
#     s1_info[0] , s1_info[1]
# ))



# s2_info = s2.gpa_scores()
# print(cal_gpa(
#     s2_info[0] , s2_info[1]
# ))
# print(check_gpa(
#     s2_info[0] , s2_info[1]
# ))

# -----------

# from datetime import datetime

# x = datetime.now()
# print(x)
# print(x.year)
# print(x.month)
# print(x.day)
# print(x.hour)
# print(x.minute)


# x = datetime(2026 , 7 , 1 , 19)
# print(x)

# -----------
# sal tavaod khodemon be miladi va senemon ro bedast biyarim
# from datetime import datetime
# x = datetime(2006 , 10 ,20)
# now = datetime.now()
# print(now - x)
# print(now.year - x.year)
# ----------
# from datetime import datetime
# x = datetime(2006 , 10 ,20)
# now = datetime.now()

# print(x.weekday())
# print(now.weekday())

# ----------
# mitone timee ke mikhay ro behesh bedi va menha time zaman alan mekone
# from datetime import datetime , timedelta
# x = datetime.now()
# new = x + timedelta(days = 2)
# new = x + timedelta(hours = -3)
# new = x + timedelta(minutes = 50)
# new = x + timedelta(weeks = -1)
# print(new)  
# # -------------
# hw1
# from datetime import datetime , timedelta

# def calculation(start:datetime , end :datetime):
#     if start > end:
#         raise ValueError("start date must be before and date")
    

#     counter = 0 
#     while start <= end:
#         if not (start.weekday() == 3 or start.weekday() == 4):
#             counter += 1


#         start += timedelta(days = 1)

#     return counter


# try:
#     date1 = datetime(2026 , 7 , 25)
#     date2 = datetime(2026 , 8 , 8)
#     # result = calculation(date1 , date2)
#     result = calculation(date2 , date1)
#     print(result)
# except ValueError as err:
#     print(err)
# ----------
# inja ba in % neshon midim sahat ro ba p.m va .am va halal baghyash
# from datetime import datetime , timedelta
# x = datetime.now()
# print(x)
# print(x.strftime("%I:$M %P"))
# print(x.strftime("%I:$M %PM, today is $A , %D of $b"))
# ----------
# JSON => typpe (String)
# ISON => javascaript object notashin
# import json

# person = {
    # "name" : "nasim",
    # "age" : 20,
    # "favorites" :["python " , "ML"]
# }
# print(person)
# print(type(person))
# print(person(person))
# print(person["name"])

# output = json.dumps(person)
# print(person(person))
# print(person["name"])
# # ---------
# import json

# person = {
#     "name" : "nasim",
#     "age" : 20,
#     "favorites" :["python " , "ML"]
# }
# output =json.dumps(person)
# print(output)


# output = json.dumps(person , indent = 4 , sort_keys = True)
# print(output)

# --------
# import json
# person = {"name" : "nasim" , "age" : 20 , "favorites" :["python " , "ML"]}

# print(person)
# print(type(person))

# result = json.loads(person)
# print(result)
# print(type(result))
# print(result("name"))
# ---------
# serfan morafi kardan
'''
Regex => Regular Expression
'''
# import re

# import webbrowser

# webbrowser.open("adrs mored nazar ro mizarim inja")
# webbrowser.open_new_tab("adrs mored nazar ro mizarim inja")
# webbrowser.open_new("adrs mored nazar ro mizarim inja")
# --------
'''
reqiests
bs4
selenium


pip install requests , bs 4 , selenium
python -m pip install



'''


















