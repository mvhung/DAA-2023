import time
import random

# Hàm knapsack bằng dynamic programming
def DP(capacity, weights, values, n):
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                K[i][w] = max(values[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][capacity]

# Hàm knapsack bằng genetic algorithm
def GA(capacity, weights, values, n, population_size=2000, generations=400):
    # Khởi tạo quần thể
    population = []
    for i in range(population_size):
        chromosome = [random.randint(0, 1) for i in range(n)]
        population.append(chromosome)

    # Vòng lặp chạy thuật toán
    for i in range(generations):
        # Tính giá trị fitness cho từng cá thể trong quần thể
        fitness = []
        for chromosome in population:
            weight = sum([weights[j] * chromosome[j] for j in range(n)])
            if weight > capacity:
                fitness.append(0)
            else:
                value = sum([values[j] * chromosome[j] for j in range(n)])
                fitness.append(value)
        
        # Lựa chọn cá thể tốt nhất để giữ lại trong quần thể
        best_chromosome = population[fitness.index(max(fitness))]

        # Tạo ra quần thể mới bằng cách lai ghép và đột biến
        new_population = [best_chromosome]
        while len(new_population) < population_size:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = []
            for j in range(n):
                if random.random() < 0.5:
                    child.append(parent1[j])
                else:
                    child.append(parent2[j])
            if random.random() < 0.1:
                j = random.randint(0, n - 1)
                if child[j] == 1:
                    child[j] = 0
                else:
                    child[j] = 1
            new_population.append(child)
        population = new_population

    # Tính giá trị tối ưu của bài toán knapsack
    best_fitness = 0
    for chromosome in population:
        weight = sum([weights[j] * chromosome[j] for j in range(n)])
        if weight <= capacity:
            value = sum([values[j] * chromosome[j] for j in range(n)])
            if value > best_fitness:
                best_fitness = value

    return best_fitness

import random

def knapsack_ga(values, weights, capacity, pop_size, num_generations, crossover_rate, mutation_rate):
    # Khởi tạo quần thể ban đầu
    population = []
    fitness_avgs = []

    for i in range(pop_size):
        individual = [random.randint(0, 1) for _ in range(len(values))]
        population.append(individual)

    # Hàm đánh giá mức độ thích nghi của mỗi cá thể
    def fitness(individual):
        total_value = 0
        total_weight = 0
        for i in range(len(values)):
            if individual[i] == 1:
                total_value += values[i]
                total_weight += weights[i]
        if total_weight > capacity:
            return 0
        return total_value

    # Thực hiện phép lai ghép (crossover) giữa hai cá thể cha mẹ
    def crossover(parent1, parent2):
        child1 = parent1.copy()
        child2 = parent2.copy()
        crossover_point = random.randint(1, len(parent1) - 1)
        child1[crossover_point:], child2[crossover_point:] = child2[crossover_point:], child1[crossover_point:]
        return child1, child2

    # Thực hiện phép đột biến (mutation) trên một cá thể
    def mutate(individual):
        index = random.randint(0, len(individual) - 1)
        individual[index] = 1 - individual[index]

    # Lựa chọn các cá thể tốt nhất trong quần thể hiện tại
    def selection(population):
        sorted_population = sorted(population, key=fitness, reverse=True)
        return sorted_population[:int(len(sorted_population)*0.2)]

    # Thực hiện quá trình GA
    for i in range(num_generations):
        # Lựa chọn các cá thể tốt nhất
        selected_population = selection(population)

        # Tạo quần thể mới cho thế hệ tiếp theo
        new_population = []
        while len(new_population) < pop_size:
            parent1 = random.choice(selected_population)
            parent2 = random.choice(selected_population)
            if random.random() < crossover_rate:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1.copy(), parent2.copy()
            if random.random() < mutation_rate:
                mutate(child1)
            if random.random() < mutation_rate:
                mutate(child2)
            new_population.append(child1)
            new_population.append(child2)
        total_fitness = sum(fitness(individual) for individual in population)
        average_fitness = total_fitness / len(population)
        fitness_avgs.append(average_fitness)
        population = new_population

    # Trả về cá thể tốt nhất trong quần thể cuối cùng
    best_individual = max(population, key=fitness)
    return best_individual
# Hàm so sánh hai thuật toán
# def compare_algorithms():
#     # Khởi tạo các biến
#     sizes = [1000 ]  # Kích thước tăng dần
#     results_dp = []
#     results_ga = []
#     times_dp = []
#     times_ga = []

#     # Chạy thuật toán trên các kích thước khác nhau
#     for size in sizes:
#         # Tạo dữ liệu đầu vào ngẫu nhiên
#         capacity = 1000000
#         weights = [random.randint(1, size * 2) for _ in range(size)]
#         values = [random.randint(1, size * 2) for _ in range(size)]
#         n = len(weights)

#         # Chạy thuật toán DP và đo thời gian chạy
#         start_time = time.time()
#         # dp_result = DP(capacity, weights, values, n)
#         dp_time = time.time() - start_time

#         # Chạy thuật toán GA và đo thời gian chạy
#         start_time = time.time()
#         ga_result = GA(capacity, weights, values, n)
#         ga_time = time.time() - start_time

#         # Lưu trữ kết quả
#         # results_dp.append(dp_result)
#         results_ga.append(ga_result)
#         times_dp.append(dp_time)
#         times_ga.append(ga_time)

#     # In kết quả
#     for i in range(len(sizes)):
#         print("Size:", sizes[i])
#         # print("Dynamic programming result:", results_dp[i])
#         print("Dynamic programming time:", times_dp[i])
#         print("Genetic algorithm result:", results_ga[i])
#         print("Genetic algorithm time:", times_ga[i])
#         print()

# compare_algorithms()