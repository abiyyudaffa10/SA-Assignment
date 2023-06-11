import itertools    #import modul itertools yang berfungsi untuk iterasi dan kombinasi elemen dengan efisien

def calculate_cost(assignment, costs, profit):  #mendefinisikan fungsi calculate_cost yang menerima tiap variabel
    total_cost = 0  #inisialisasi var menjadi 0
    total_profit = 0    #inisialisasi var menjadi 0
    for i, j in enumerate(assignment):  #looping dimana i mewakili indeks dan j mewakili job
        total_cost += costs[i][j]   #menambah biaya dan keuntungan untuk assign keuntungan dan job
        total_profit += profit[i][j]    #menambah biaya dan keuntungan untuk assign keuntungan dan job
    return total_cost, total_profit   #mengembalikan

def brute_force_job_assignment(jobs, costs, profit):
    best_assignment = None
    max_profit = 0

    for assignment in itertools.permutations(range(len(jobs))):
        cost, cur_profit = calculate_cost(assignment, costs, profit)
        if cur_profit > max_profit and cost <= 20:
            max_profit = cur_profit
            best_assignment = assignment

    return best_assignment, max_profit


jobs = ['Soal 1', 'Soal 2', 'Soal 3']
costs = [
    [2, 4, 8],   # Cost of assigning Soal 1 to stage 1, stage 2, stage 3
    [4, 5, 6],   # Cost of assigning Soal 2 to stage 1, stage 2, stage 3
    [5, 7, 10]   # Cost of assigning Soal 3 to stage 1, stage 2, stage 3
]

profit = [
    [6000, 10000, 20000],
    [7000, 7500, 9000],
    [9000, 11000, 15000]
]

best_assignment, profit = brute_force_job_assignment(jobs, costs, profit)
print("Best course:", best_assignment)
print("Max profit:", profit)