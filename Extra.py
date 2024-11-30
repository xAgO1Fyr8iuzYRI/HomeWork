grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
avg = [[sum(grades[0])/len(grades[0])],[sum(grades[1])/len(grades[1])],
        [sum(grades[2])/len(grades[2])],[sum(grades[3])/len(grades[3])],
        [sum(grades[4])/len(grades[4])]]
list_ = sorted(students)
dict_avg = {}
dict_avg.update({list_[0]:avg[0],
                list_[1]:avg[1],
                list_[2]:avg[2],
                list_[3]:avg[3],
                list_[4]:avg[4]})
print(dict_avg)
# dict_avg_2 = dict(zip(list_,avg))
# print(dict_avg_2)


