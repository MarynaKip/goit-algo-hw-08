import heapq

def min_connection_cost(cables):
    # Ініціалізуємо купу на основі довжин кабелів
    heapq.heapify(cables)
    total_cost = 0
    
    # Поки в купі більше одного кабелю
    while len(cables) > 1:
        # Витягуємо два найкоротших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Об'єднуємо їх, додаючи до загальних витрат
        cost = first + second
        total_cost += cost
        
        # Додаємо новий об'єднаний кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost

cables = [4, 3, 2, 6]
print(min_connection_cost(cables))