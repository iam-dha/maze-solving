import matplotlib
matplotlib.use('TkAgg')  # Hoặc 'QtAgg', 'Agg', tùy môi trường
import matplotlib.pyplot as plt
import seaborn as sns

# Giả sử bạn có một danh sách các thuật toán và thời gian tương ứng
algorithms = ['BFS', 'A*', 'Greedy']
execution_times = [0.12, 0.08, 0.15]  # Thời gian thực thi của mỗi thuật toán

# Vẽ biểu đồ
sns.barplot(x=algorithms, y=execution_times)
plt.xlabel('Thuật toán')
plt.ylabel('Thời gian (giây)')
plt.title('So sánh thời gian thực thi của các thuật toán')
plt.show()
