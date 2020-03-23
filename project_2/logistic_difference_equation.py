import matplotlib.pyplot as plt


def y(r1, x1):
    """
    :param r1: growth rate r
    :param x1: percentage of the maximum (expressed in decimals) x
    :return: xn+1
    """
    return r1*x1*(1-x1)


r = 2.6
x = 0.4
track_list_x = list()
for t in range(0, 101):
    track_list_x.append(x)
    x = y(r, x)

plt.plot(list(range(0, 101)), track_list_x)

plt.xlabel('time')
plt.ylabel('population')

plt.title(f'Population vs Time, growth rate {r}')

plt.show()
