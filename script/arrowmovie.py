import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as manimation

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib', comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)

fig = plt.figure()
ax = plt.axes()

plt.xlim(-5, 5)
plt.ylim(-5, 5)

x0, y0 = 0, -2

with writer.saving(fig, '../movie/writer_test.mp4', 100):
    for i in range(100):
        ar = ax.arrow(0, 0, x0, y0, head_width=0.05, head_length=0.1, fc='k', ec='k')
        x0 += 0.05
        y0 += 0.05
        writer.grab_frame()
        ar.remove()
