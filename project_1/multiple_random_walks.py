import random
import matplotlib.pyplot as plt


def y(t, track_list):
    """
    :param t: time
    :param track_list: y values track list
    :return: the y value (position) in a specific time and the y values track list
    """
    e = random.choice([-1, 1])
    if t == 1:
        y_value = e
        track_list.append(y_value)
        return y_value, track_list
    else:
        y_value = y(t - 1, track_list)[0] + e
        track_list.append(y_value)
        return y_value, track_list


time = 5
x = list(range(time+1))         # It works with range() too, but I wanted both x and y to be class 'list'

for i in range(1, 4):
    plt.plot(x, y(time, [0])[1], label=f'Random Walk {i}', marker='X')

plt.xlabel('time')
plt.ylabel('position')

plt.title('Multiple Random Walks')

plt.legend()

plt.show()
