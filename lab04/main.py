import random

N = 31
i = 0
mounth = []
water = 0
show = 0

while i < N:
    # day = (random.randint(-10,10),random.randint(-25,25))
    day = {"day": i+1,"precipitation": random.randint(-10,10),"C*":random.randint(-25,25)}
    mounth.append(day)
    if day["C*"] < 0:
        show = show + day["precipitation"]
    else:
        water = water + day["precipitation"]
    i = i + 1

print("Статистика опадів за місяць:")
print(mounth)
print("Кількість випавшего снігу за місяць: "+str(show))
print("Кількість випавшего дощу за місяць: "+str(water))
print("\n\nEnter day index which you wand delete: ")
delete_day_index = int(input())
save_day = mounth[delete_day_index-1]
mounth.pop(delete_day_index-1)
print("New mounth list: " + str(mounth))
print("\n\nAnd now we return it back!")
mounth.insert(delete_day_index-1,save_day)
print("New mounth list: " + str(mounth))
print("Sorted mounth list on C*: "+str(sorted(mounth, key=lambda k: k['C*'])))



