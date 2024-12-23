from collections import deque

u = [1]
generated = set(u)
queue = deque(u)

result = []
while len(result) < 10000:  
    x = queue.popleft()
    result.append(x)
    
    # Generate new values and add to the queue if not already generated
    for new_x in (2 * x + 1, 3 * x + 1):
        if new_x not in generated:
            generated.add(new_x)
            queue.append(new_x)

print(sorted(result))