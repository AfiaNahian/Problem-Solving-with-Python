days = int(input())

year=days//365
remain_days = days%365
month = remain_days//30
remain_days_2 = remain_days%30
print(year,"ano(s)")
print(month,"mes(es)")
print(remain_days_2,"dia(s)")