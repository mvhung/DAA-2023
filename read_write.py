import random

def random_data(size) :
    values = [random.randint(1, 100) for _ in range(size)]  # Giá trị của các món đồ
    weights = [random.randint(1, 50) for _ in range(size)]  # Trọng lượng của các món đồ
    knapsack_capacity = random.randint(size * 2, size * 10)  # Sức chứa của knapsack
    
    return values, weights, knapsack_capacity

def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1
# Tạo dữ liệu

def create_data(n):

    data = random_data(n)

    # Lưu dữ liệu vào file
    with open("data"+(str) (n)+".txt", "w") as file:
        file.write("Values: {}\n".format(data[0]))
        file.write("Weights: {}\n".format(data[1]))
        file.write("Knapsack capacity: {}\n".format(data[2]))

def save_result(name ,info):
    with open("result"+name+".txt", "w") as file:
         file.write("{}\n".format(info))

def read_data(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        values = eval(lines[0].split(": ")[1])
        weights = eval(lines[1].split(": ")[1])
        knapsack_capacity = int(lines[2].split(": ")[1])
    return values, weights, knapsack_capacity

def read_result(filename):
    with open(filename, 'r') as file:
        content = file.readlines()[1:]
        values = [int(val) for val in content[0].split()]
    
    return values