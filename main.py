import array as arr

num = arr.array('i',[1, 3, 5, 3, 7, 9, 3])
print("array is",num)

#the number of occurrences of number 9 in the array
print("occurrance of number 9 is:",num.count(9))

#reversed array
num.reverse()
print("Reversed array is:",num)