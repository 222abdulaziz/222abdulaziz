

# ARRAYS
# LIST

# arr = list()
# arr = [1,2,3]
# arr.append(4)
# print(len(arr))
# print(arr[0])
# print(arr[len(arr)-1])
# print(arr[-1])

# a = arr[2:]
# list1 = arr[:]
# reversed1=arr[::-1]
# print(a)
# print(list1)

# beginner    
# arr = []    
# for i in range(10):
#     arr.append(i)
# print(arr)

# junior
# arr = [i for i in range(10)]
# print(arr)

# middle
# print(list(range(10)))

# 1 var
# for i in range(1,11):
#     if i % 2 == 0:
#         arr.append(i**10)

# arr = [i * 10 for i in range(1, 11)if i % 2 == 0 ]
# print(arr)

# print(list(range(2,10,2)))


# from unittest import result


# arr = [[1,2], [3,4], [5,6], [7,8]]
# result_list = []
# for i in arr:
#     for j in i:
#         if j % 2 ==0:
#             result_list.append(j*10)
# print(result_list)



# arr = []
# gen_list = [j * 10 for i in arr for j in i if j % 2 == 0]
# print(gen_list)
# print(list(range(2,10,2)*10))

# def my_func(elem):
#     return elem *1

# arr = [1,2,3,4,5]
# print(map(my_func , arr))

# def get_more_elems(el1,el2,el3):
#     return el1 + el2 + el3
# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]
# print(list(map(get_more_elems,a,b,c)))

# arr = [1,2,3,4,5]
# for i in range(-len(arr),5):
#     print(i)

# print(arr[-1])
  
import pygal


line_chart = pygal.line()
line_chart.title = 'Statistika'
line_chart.x_labels = ['Fevral', 'Mart', 'aprel', 'May']
line_chart.add('Facebook', [9.24, 13.7, 16.24, 18.07])
line_chart.add('Instagram', [9.24, 13.7, 16.24, 18.07])
line_chart.render_in_browser()







