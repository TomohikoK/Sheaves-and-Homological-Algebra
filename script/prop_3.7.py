import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import math

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='f_{n-1} induce image map', artist='TomohikoK')
writer = FFMpegWriter(fps=30, metadata=metadata)

fig = plt.figure()
ax = plt.axes()

plt.xlim(-2, 2)
plt.ylim(-1, 2)

with writer.saving(fig, '../movie/prop_3.7.mp4', 100):
    # d'_{n-1}・f_{n-1} = d_n・f_n
    x0, y0 = -1, 0
    dx, dy = 1, 1
    frame_count = 100

    cok_dd_n_1 = ax.arrow(0, 0, 1 * 0.9, 0 * 0.9,
                          head_width=0.1, head_length=0.1,
                          fc='k', ec='k')
    for i in range(frame_count):
        x = x0 + (i * dx) / (frame_count - 1)
        y = y0 + (i * dy) / (frame_count - 1)

        f_n_1 = ax.arrow(-1, 1, x + 1, y - 1, fc='k', ec='k')
        dd_n_1 = ax.arrow(x, y, -x, -y, fc='k', ec='k')
        writer.grab_frame()
        f_n_1.remove()
        dd_n_1.remove()

    # cok(d_{n-1})
    x0, y0 = 0, 1
    dx, dy = 1, 0
    frame_count = 100

    d_n_1 = ax.arrow(-1, 1, 1, 0, fc='k', ec='k')
    f_n = ax.arrow(0, 1, 0, -1, fc='k', ec='k')
    cok_dd_n_1 = ax.arrow(0, 0, 1 * 0.9, 0 * 0.9,
                          head_width=0.1, head_length=0.1,
                          fc='k', ec='k')
    for i in range(frame_count):
        x_i = (i * dx) / (frame_count - 1)
        y_i = (i * dy) / (frame_count - 1)

        cok_d_n_1 = ax.arrow(x0, y0, x_i * 0.9, y_i * 0.9,
                             head_width=0.1, head_length=0.1,
                             fc='k', ec='k')
        writer.grab_frame()
        cok_d_n_1.remove()

    # universality
    x0, y0 = 1, 1
    dx, dy = 0, -1
    frame_count = 100

    cok_d_n_1 = ax.arrow(0, 1, 1 * 0.9, 0 * 0.9,
                         head_width=0.1, head_length=0.1,
                         fc='k', ec='k')
    for i in range(frame_count):
        x = x0 + (i * dx) / (frame_count - 1)
        y = y0 + (i * dy) / (frame_count - 1)

        univ = ax.arrow(1, 1, (x - 1) * 0.9, (y - 1) * 0.9,
                        head_width=0.1, head_length=0.1,
                        fc='r', ec='r')
        writer.grab_frame()
        univ.remove()
