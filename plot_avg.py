import timeit

import numpy as np
from comprasion import DP, GA, GA_calculate_Avgfitness, knapsack_ga
from read_write import create_data, read_data, save_result
import matplotlib.pyplot as plt

# Dữ liệu thời gian chạy của các thuật toán
sizes = [5, 10, 15, 20, 30, 50]
dynamic_times = [] 
GA_times = []
dp_results = []
ga_results = []

fitness_avgs=[]
size = 100
values,weights, knapsack_capacity = read_data("data"+ str(size)+ ".txt")
   
best_individual, fitness_avgs =  knapsack_ga(values, weights, knapsack_capacity, pop_size =1000, num_generations = 300, crossover_rate  = 0.5, mutation_rate= 0.1)

# Vẽ đồ thị
# plt.plot(sizes, recursive_times, label='Đệ quy')
# plt.plot(sizes, backtracking_times, label='Quay lui')
# plt.plot(sizes, GA_times, label='thời gian GA')
# plt.plot(sizes, dynamic_times, label='thời gian quy hoạch động')
# plt.plot(sizes, ga_results, label='kết quả GA')
# plt.plot(sizes, dp_results, label='kết quả quy hoạch động')

plt.plot(fitness_avgs, label="trung bình fitness")
# Đặt tên cho trục x và trục y
# plt.xlabel('Kích thước knapsack')
# plt.ylabel('Thời gian chạy (giây)')

plt.xlabel('thế hệ')
plt.ylabel('value')
# Đặt tiêu đề cho đồ thị
# plt.title('Thời gian chạy')
plt.title('trung bình fitness qua các thế hệ')

# Hiển thị chú thích
plt.legend()

# Hiển thị đồ thị
plt.show()

