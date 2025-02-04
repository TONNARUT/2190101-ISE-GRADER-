x_min, x_max = float('inf'), float('-inf')
y_min, y_max = float('inf'), float('-inf')

i = 0  # Row counter
while True:
    command = input().strip()
    if command in ('Zig-Zag', 'Zag-Zig'):
        break  
    
    x, y = map(int, command.split())  
    
    if i % 2 == 1:
        x, y = y, x
        x_min = min(x_min, x)
    x_min = min(x_min,x)
    x_max = max(x_max, x)
    y_min = min(y_min, y)
    y_max = max(y_max, y)
    
    i += 1  


if command == 'Zag-Zig':
    print(y_min, x_max)
elif command == 'Zig-Zag':
    print(x_min, y_max)
