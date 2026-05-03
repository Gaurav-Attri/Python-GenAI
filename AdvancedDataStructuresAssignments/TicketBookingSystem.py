import heapq

queue = []
heapq.heappush(queue, (3, "Regular"))
heapq.heappush(queue, (1, "VIP"))

priority, name = heapq.heappop(queue)
print(f"Processing {name}")