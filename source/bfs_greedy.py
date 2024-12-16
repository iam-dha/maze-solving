import math
import random


def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# Hàm thực hiện Greedy Best-First Search
import heapq

def greedy_bfs(start, goal, matrix):
    # Lấy số hàng và cột của ma trận
    rows, cols = len(matrix), len(matrix[0])

    # Danh sách mở, sử dụng heap để lưu trữ các ô cần khám phá, với giá trị ưu tiên là heuristic
    open_list = []
    # Đẩy vào heap phần tử gồm giá trị heuristic (khoảng cách Euclidean từ current đến goal) và vị trí hiện tại
    heapq.heappush(open_list, (euclidean_distance(start, goal), start))  # Heuristic + current position

    # Danh sách đóng lưu các ô đã khám phá
    closed_list = set()

    # Dictionary để lưu lại đường đi từ mỗi ô (neighbor) về ô hiện tại
    came_from = {}

    # Các hướng di chuyển: lên, xuống, trái, phải
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Vòng lặp duyệt qua các ô trong danh sách mở
    while open_list:
        # Lấy ra ô có giá trị heuristic thấp nhất từ heap
        _, current = heapq.heappop(open_list)

        # Nếu ô hiện tại là đích, ta dựng lại đường đi từ start đến goal
        if current == goal:
            # Danh sách lưu đường đi từ goal về start
            path = []
            # Dựng lại đường đi từ goal về start thông qua came_from
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)  # Thêm start vào đường đi
            path.reverse()  # Đảo ngược lại để có đường đi từ start đến goal
            return path

        # Thêm ô hiện tại vào danh sách đóng
        closed_list.add(current)

        # Kiểm tra các ô xung quanh ô hiện tại (các ô láng giềng)
        for move in moves:
            # Tính vị trí của ô láng giềng
            neighbor = (current[0] + move[0], current[1] + move[1])

            # Kiểm tra xem ô láng giềng có hợp lệ không (trong phạm vi ma trận và chưa được khám phá)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                # Nếu ô láng giềng là ô trống (giá trị 0) và chưa được khám phá, ta thêm vào danh sách mở
                if matrix[neighbor[0]][neighbor[1]] == 0 and neighbor not in closed_list:
                    # Đẩy vào danh sách mở với giá trị ưu tiên là khoảng cách Euclidean đến goal
                    heapq.heappush(open_list, (euclidean_distance(neighbor, goal), neighbor))
                    # Lưu lại bước đi từ neighbor về current
                    came_from[neighbor] = current

    # Nếu không tìm thấy đường đi, trả về None
    return None

def random_matrix(num_rows, num_cols, num_obs):
    # Khởi tạo ma trận với các ô trống (0)
    arr = [0 for _ in range(num_rows * num_cols)]

    # Chọn ngẫu nhiên các vị trí có vật cản (1)
    obs_positions = random.sample(range(num_rows * num_cols), num_obs)
    for pos in obs_positions:
        arr[pos] = 1  # 1 đại diện cho vật cản

    # Tạo ma trận từ danh sách arr
    matrix = [arr[i * num_cols:(i + 1) * num_cols] for i in range(num_rows)]

    return matrix

# Hiển thị ma trận
def print_maze(maze):
    for row in maze:
        print(" ".join(str(cell) for cell in row))


def main():
    # Tạo ma trận 10x10
    rows, cols = 10, 10
    maze_matrix = random_matrix(rows, cols,20)

    # Hiển thị ma trận
    print("Maze:")
    print_maze(maze_matrix)

    start = (0, 0)  # Vị trí bắt đầu
    goal = (9, 9)  # Vị trí đích

    path = greedy_bfs(start, goal, maze_matrix)

    if path:
        print("Đường đi tới đích:")
        print(path)
    else:
        print("Không thể tìm đường tới đích!")


if __name__ == "__main__":
    main()
