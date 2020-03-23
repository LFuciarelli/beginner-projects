import random
import matplotlib.pyplot as plt


def x_and_y_values(t, track_list_x, track_list_y):
    """
    :param t: time
    :param track_list_x: x values track list
    :param track_list_y: y values track list
    :return: the x values track list and the y values track list
    """
    for i in range(0, t):
        e1 = random.choice([1, -1])
        e2 = random.choice([1, -1])
        if e1 == 1 and e2 == 1:
            track_list_y.append(track_list_y[-1] + 1)
            track_list_x.append(track_list_x[-1])
        elif e1 == 1 and e2 == -1:
            track_list_x.append(track_list_x[-1] + 1)
            track_list_y.append(track_list_y[-1])
        elif e1 == -1 and e2 == 1:
            track_list_x.append(track_list_x[-1] - 1)
            track_list_y.append(track_list_y[-1])
        elif e1 == -1 and e2 == -1:
            track_list_y.append(track_list_y[-1] - 1)
            track_list_x.append(track_list_x[-1])
    return track_list_x, track_list_y


time = 500
x, y = x_and_y_values(time, [0], [0])

plt.plot(x, y)

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.title('2D Random Walk')

plt.show()
