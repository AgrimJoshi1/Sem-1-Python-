time_hour1 = float(input("Enter first hour: "))
time_minute1 = float(input("Enter first minutes: "))
time_hour2 = float(input("Enter second hour: "))
time_minute2 = float(input("Enter second minutes: "))

# h1  = time_hour1 * 60 
# h2 = time_hour2 * 60 
# diff_min = time_minute1 - time_minute2
# diff_min2 = h1 - h2 
diff = (time_hour1*60 + time_minute1) - (time_hour2*60 -time_minute1)

if diff == 0:
    print("On time")
elif diff <30: 
    print("Early")
elif 30 <diff<60:
    print("Late") 
elif diff > 60:
    print("very late")
else:
    print("Error")
# if  diff_min == 0 and diff_min2 ==0:
#     print("On time")
# elif diff_min < 30 or diff_min2<30 : 
#     print("Very Early")
# elif diff_min < 60 or diff_min2 <60: 
#     print("Late")
# elif  diff_min > 60 or diff_min2 >60: 
#     print("Very late")
