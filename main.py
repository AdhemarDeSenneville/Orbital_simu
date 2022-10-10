import matplotlib.pyplot as plt
import matplotlib.animation as anim

def plot_cont( xmax):
    y = []
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    def update(i):
        yi = 4*i
        y.append(yi)
        x = range(len(y))
        ax.clear()
        ax.plot(x, y)
        print(i, ': ', yi)

    a = anim.FuncAnimation(fig, update, frames=xmax, repeat=False)
    plt.show()

plot_cont(7)