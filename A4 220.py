import sys
import math
from collections import defaultdict 


input_list = []
input_amount = 0
cities = 0
for line in sys.stdin:
    row = line.split()
    input_list.append(row)
    
input_list.append('!')
city_list = []
city_amount_list = []
distance_list = []
process_list = []
dijkstra_list = []
#Sorts the input into seperate lists to process
for i in range(len(input_list)):
    if input_list[i] is input_list[0]:
        tests = input_list[i]
    else:
        if str(input_list[i]).isdigit() == True and input_list[i] != '!':
            if str(input_list[i+1]).isdigit() == False and input_list[i+1] != '!':
                city_amount_list.append(input_list[i])
            else:
                distance = input_list[i]
                distance_list.append(input_list[i])
        else:
            if input_list[i] != '!':
                city_list.append(input_list[i])
for i in range(tests):
    while city_amount_list[i] != 0:
        process_list.append(city_list[city_amount_list[0]])
        city_amount_list[i] += -1
    for value in process_list:
        for compare in process_list:
            temp1 = value.split()
            temp2 = compare.split()
            dijkstra_list.append(temp1[2], temp2[2], get_distance(temp1[0:1], temp2[0:1]))
print(dijkstra_list)    


    






def get_distance(coor1, coor2):
    r = 6371
    diff_lat = coor2[0] - coor1[0]
    diff_long = coor2[1] - coor1[1]
    a = (math.sin(diff_lat/2)) +math.cos(coor1[0]) * math.cos(coor2[0]) * (math.sin(diff_long/2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = r * c
    return c

