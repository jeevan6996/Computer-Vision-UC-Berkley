import matplotlib.pyplot as plt

def calculate_length(x1, x2):
    return abs(x1) + abs(x2)

def calculate_line_segments(point_X, f=1):
    calculated_lengths_list = []
    for Z in range(10, 1001):
        perspective_point_a = -f * (point_X/Z)
        perspective_point_b = -f * (-point_X/Z)
        calculated_lengths_list.append((Z, round(calculate_length(perspective_point_a, perspective_point_b), 5)))
    return calculated_lengths_list

if __name__ == "__main__":
    ans = calculate_line_segments(5)
    z, lengths = zip(*ans)
    plt.plot(z, lengths, color='b')
    plt.title('Distance "Z" vs Projected line segment length')
    plt.xlabel('Z')
    plt.ylabel('Length of line segment')
    plt.grid(True)
    plt.show()