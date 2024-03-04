import math

# Question 1

"""
lst = list(range(10))


def at_least_n(lst, n):
    for i in range(len(lst)):
        if lst[i] < n:
            lst.remove(lst[i])
    return lst


print(at_least_n(lst, 5))


def at_least_n2(lst, n):
    for i in lst:
        if i < n:
            lst.remove(i)
    return lst

print(at_least_n2(lst, 5))

Are this implementations correct?
# Type your answer here
No.

What is the moral of the story?
# Type your answer here

When you remove an element from the list using lst.remove(), it modifies the list in-place by shifting the subsequent elements to fill the gap left by the removed element. However, when you remove an element at index i, the next element will shift down to index i, and the loop will increment i to the next value. As a result, you will end up skipping the element that shifted down.
"""

lst_a = [3, 4, 6, 8, 9, 10]


def at_least_n(lst, n):
    for num in lst[::-1]:
        if num < n:
            lst.remove(num)
    return lst


# print(at_least_n(lst_a, 7))

# Question 2


def contains(obj, tup):
    for item in tup:
        if item is obj:
            return True
    return False

# Question 3


def find_equi(lst):
    equi = []
    for i in range(len(lst)):
        if sum(lst[:i]) == sum(lst[i+1:]):
            equi.append(i)
    if len(equi) == 0:
        return -1
    return equi


# print(find_equi([-7, 1, 5, 2, -4, 3, 0]))

# Question 4

tri_lst_a = [[[0, 0], [3, 0], [3, 4]],
             [[0, 0], [6, 0], [7, 1]],
             [[1, 1], [2, 1], [2, 2]]]


def only_right_tri(tri_lst):
    right_tri_lst = []

    def is_right_tri(tri):
        def calculate_length(p1, p2):
            return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

        side1 = calculate_length(tri[0], tri[1])
        side2 = calculate_length(tri[1], tri[2])
        side3 = calculate_length(tri[2], tri[0])

        # if (side1**2 + side2**2 == side3**2) or (side2**2 + side3**2 == side1**2) or (side3**2 + side1**2 == side2**2):
        if math.isclose(side1**2 + side2**2, side3**2) or math.isclose(side2**2 + side3**2, side1**2) or math.isclose(side3**2 + side1**2, side2**2):
        
            # couldn't think of a way to fix the floats so had to use math.isclose(), but if the triangles are just slightly off such that they are no longer a right angled triangle, isclose() tolerance might still consider it equal then it wouldn't work.

            return True
        return False

    for tri in tri_lst:
        if is_right_tri(tri):
            right_tri_lst.append(tri)

    return right_tri_lst


print(only_right_tri(tri_lst_a))
