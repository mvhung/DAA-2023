import timeit

import numpy as np
from comprasion import DP, GA
from read_write import create_data, read_data, save_result
import matplotlib.pyplot as plt

# Dữ liệu thời gian chạy của các thuật toán
sizes = [5, 10, 15, 20, 30, 50,100]  # Kích thước bài toán knapsack
# recursive_times = []  # Thời gian chạy thuật toán đệ quy tương ứng
# backtracking_times = []  # Thời gian chạy thuật toán quay lui tương ứng
# brute_force_times = []  # Thời gian chạy thuật toán vét cạn tương ứng
dynamic_times = [] 
GA_times = []
dp_results = []
ga_results = []

fitness_avgs=[]
for n in sizes:
    # create_data(n)
    values,weights, knapsack_capacity = read_data("data"+ str(n)+ ".txt")
    results = []
    exe_time_dynamic= timeit.timeit(lambda: results.append(DP(knapsack_capacity, weights, values, n)), number=3)
    dp_results.append(results[0])

    # exe_time_backtracking = timeit.timeit(lambda: knapsack_backtracking(values, weights, knapsack_capacity), number=20)
    results = []
    exe_time = timeit.timeit(lambda: results.append(GA(knapsack_capacity, weights, values, n)), number=20) 
        
    mean_result = np.mean(results)
    ga_results.append(mean_result)
    # recursive_times.append(exe_time_recursive)
    # backtracking_times.append(exe_time_backtracking)
    GA_times.append(exe_time)
    dynamic_times.append(exe_time_dynamic)
    save_result("GA_times",GA_times)
    save_result("dynamic_times",dynamic_times)
    save_result("GA_results",ga_results)
    save_result("dp_results",dp_results)
    # fitness , fitness_avgs = GA_calculate_Avgfitness(knapsack_capacity, weights, values, n)

# print(fitness_avgs)
# Vẽ đồ thị
# plt.plot(sizes, recursive_times, label='Đệ quy')
# plt.plot(sizes, backtracking_times, label='Quay lui')
# plt.plot(sizes, GA_times, label='thời gian GA')
# plt.plot(sizes, dynamic_times, label='thời gian quy hoạch động')
plt.plot( sizes,ga_results, label='kết quả GA')
plt.plot( sizes,dp_results, label='kết quả quy hoạch động')

# plt.plot(fitness_avgs, label="trung bình fitness")
# Đặt tên cho trục x và trục y
plt.xlabel('Kích thước knapsack')
plt.ylabel('Thời gian chạy (giây)')

# plt.xlabel('thế hệ')
# plt.ylabel('value')
# Đặt tiêu đề cho đồ thị
plt.title('Thời gian chạy')
# plt.title('trung bình fitness qua các thế hệ')

# Hiển thị chú thích
plt.legend()

# Hiển thị đồ thị
plt.show()

