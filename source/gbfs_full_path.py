from pyamaze import maze, agent, COLOR
import heapq
import math
import time


def euclidean_distance(a, b):
    """Hàm tính khoảng cách Euclidean giữa hai điểm a và b."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def greedy_bfs(m, start, goal, display_process=False):
    """Thực hiện thuật toán Greedy Best-First Search (GBFS) trên mê cung m."""
    open_list = []
    heapq.heappush(open_list, (euclidean_distance(start, goal), start))  # (heuristic, position)
    closed_list = set()
    came_from = {}

    visited_steps = []  # Lưu các bước đi để hiển thị

    while open_list:
        _, current = heapq.heappop(open_list)
        visited_steps.append(current)  # Lưu lại bước đi

        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, visited_steps  # Trả về đường đi và các bước đã đi

        closed_list.add(current)
        for direction in 'ESNW':  # Các hướng: Đông, Nam, Tây, Bắc
            if m.maze_map[current][direction]:  # Kiểm tra hướng hợp lệ
                if direction == 'E':
                    neighbor = (current[0], current[1] + 1)
                elif direction == 'W':
                    neighbor = (current[0], current[1] - 1)
                elif direction == 'N':
                    neighbor = (current[0] - 1, current[1])
                elif direction == 'S':
                    neighbor = (current[0] + 1, current[1])

                if neighbor not in closed_list:
                    heapq.heappush(open_list, (euclidean_distance(neighbor, goal), neighbor))
                    came_from[neighbor] = current

    return None, visited_steps  # Không tìm thấy đường đi


def main():
    # Tạo mê cung
    rows, cols = 100,100  # Kích thước mê cung
    m = maze(rows, cols)
    m.CreateMaze(loopPercent=30)  # Tạo mê cung với tỷ lệ vòng lặp 30%

    start = (m.rows, m.cols)  # Vị trí bắt đầu (dưới cùng bên phải)
    goal = (1, 1)  # Vị trí đích (trên cùng bên trái)

    # Thực hiện Greedy BFS
    path, visited_steps = greedy_bfs(m, start, goal)

    # Hiển thị từng bước đi qua
    a = agent(m, footprints=True, color=COLOR.blue)
    for step in visited_steps:
        m.tracePath({a: [step]}, delay=100)  # Hiển thị từng bước đi
        time.sleep(0.1)

    # Hiển thị đường đi cuối cùng
    if path:
        print("Đường đi tìm được:", path)
        b = agent(m, footprints=True, color=COLOR.red)
        m.tracePath({b: path}, delay=100)
    else:
        print("Không tìm thấy đường đi!")

    m.run()  # Chạy để hiển thị mê cung


if __name__ == "__main__":
    main()
