sec = int(input())
min = sec//60
remain_sec = sec%60
hour = min//60
remain_min= min%60
print("{}:{}:{}".format(hour,remain_min,remain_sec))