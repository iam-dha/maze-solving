import random
from pyamaze import maze, agent

def DFS_with_full_path(m):
    start = (m.rows, m.cols)  # Điểm bắt đầu là góc dưới cùng bên phải
    goal = (1, 1)  # Điểm đích là góc trên cùng bên trái

    stack = [start]  # Sử dụng stack để duyệt DFS
    visited = set()  # Lưu trữ các ô đã thăm
    path = {}  # Lưu trữ cha của mỗi ô
    full_path = []  # Lưu trữ toàn bộ hành trình

    while stack:
        current = stack.pop()
        if current in visited:
            continue

        visited.add(current)
        full_path.append(current)  # Ghi lại mỗi bước mà agent đi qua

        # Nếu đã đến đích
        if current == goal:
            break

        # Lấy danh sách các ô kề có thể đi
        directions = ['N', 'E', 'S', 'W']
        random.shuffle(directions)  # Thêm độ ngẫu nhiên vào thứ tự các hướng

        for direction in directions:
            if m.maze_map[current][direction]:  # Kiểm tra xem ô có đường đi theo hướng đó không
                if direction == 'N':
                    neighbor = (current[0] - 1, current[1])
                elif direction == 'E':
                    neighbor = (current[0], current[1] + 1)
                elif direction == 'W':
                    neighbor = (current[0], current[1] - 1)
                elif direction == 'S':
                    neighbor = (current[0] + 1, current[1])

                if neighbor not in visited:
                    stack.append(neighbor)
                    path[neighbor] = current  # Lưu lại cha của ô đó

    # Dựng lại đường đi từ start đến goal
    fwd_path = {}
    cell = goal
    while cell != start:
        fwd_path[path[cell]] = cell
        cell = path[cell]

    return fwd_path, full_path

# Tạo mê cung và chạy DFS
m = maze(5, 5)  # Tạo mê cung kích thước 5x5
m.CreateMaze()

# Tìm đường đi bằng DFS
dfs_path, full_path = DFS_with_full_path(m)

# Hiển thị toàn bộ hành trình
a = agent(m, footprints=True, color='blue')  # Tạo agent hiển thị dấu chân
m.tracePath({a: full_path}, delay=100)  # Hiển thị toàn bộ hành trình (bao gồm thử sai)

# Hiển thị đường đi tối ưu cuối cùng
b = agent(m, footprints=True, color='green')  # Tạo agent hiển thị đường đi đúng
m.tracePath({b: dfs_path}, delay=300)  # Hiển thị đường đi tối ưu

m.run()
