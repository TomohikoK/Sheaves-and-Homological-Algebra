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

plt.axis('off')

with writer.saving(fig, '../movie/prop_3.7.mp4', 100):
    # operation description
    operation = ax.text(0, 1.5, '', fontsize=15, ha='center', va='bottom')

    # objects
    m_n_1 = ax.text(-1, 1, r'$M^{n-1}$', fontsize=10, va='bottom')
    m_n = ax.text(0, 1, r'$M^n$', fontsize=10, va='bottom')
    obj_cok_d_n_1 = ax.text(1, 1, r'$\mathrm{Cok}(d^{n-1})$', fontsize=10, va='bottom')

    mp_n_1 = ax.text(-1, 0, r"$M'^{n-1}$", fontsize=10, va='bottom')
    mp_n = ax.text(0, 0, r"$M'^n$", fontsize=10, va='bottom')
    obj_cok_dp_n_1 = ax.text(1, 0, r"$\mathrm{Cok}(d'^{n-1})$", fontsize=10, va='bottom')

    # f^{n-1}・cok(d'^{n-1})・d'^{n-1} = f^{n-1}・0 = 0
    operation.set_text(r"$\mathrm{cok}(d'^{n-1}) \cdot d'^{n-1} \cdot f^{n-1} = 0 \cdot f^{n-1} = 0$")

    f_n_1 = ax.arrow(-1, 1, 0 * 0.9, -1 * 0.9,
                     head_width=0.1, head_length=0.1,
                     fc='k', ec='k')
    dp_n_1 = ax.arrow(-1, 0, 1 * 0.9, 0 * 0.9,
                      head_width=0.1, head_length=0.1,
                      fc='k', ec='k')
    cok_dp_n_1 = ax.arrow(0, 0, 1 * 0.9, 0 * 0.9,
                          head_width=0.1, head_length=0.1,
                          fc='k', ec='k')
    for i in range(40):
        writer.grab_frame()
    f_n_1.remove()
    dp_n_1.remove()
    cok_dp_n_1.remove()

    # d'^{n-1}・f^{n-1} = d^n・f^n
    operation.set_text(r"$d'^{n-1} \cdot f^{n-1} = d^n \cdot f^n$")
    left_commutativity = ax.text(-0.5, 0.5, r"$\circlearrowright$", fontsize=20, ha='center', va='center')

    x0, y0 = -1, 0
    dx, dy = 1, 1
    frame_count = 100

    cok_dp_n_1 = ax.arrow(0, 0, 1 * 0.9, 0 * 0.9,
                          head_width=0.1, head_length=0.1,
                          fc='k', ec='k')
    for i in range(frame_count):
        x = x0 + (i * dx) / (frame_count - 1)
        y = y0 + (i * dy) / (frame_count - 1)

        f_n_1 = ax.arrow(-1, 1, x + 1, y - 1, fc='k', ec='k')
        dp_n_1 = ax.arrow(x, y, -x, -y, fc='k', ec='k')
        writer.grab_frame()
        f_n_1.remove()
        dp_n_1.remove()
    left_commutativity.set_text('')

    # cok(d^{n-1})
    operation.set_text("$\mathrm{cok}(d'^{n-1}) \cdot f^n \cdot d^{n-1} = 0$")

    d_n_1 = ax.arrow(-1, 1, 1, 0, fc='k', ec='k')
    f_n = ax.arrow(0, 1, 0, -1, fc='k', ec='k')

    for i in range(40):
        writer.grab_frame()
    # cok_d_n_1.remove()

    operation.set_text("$\mathrm{cok}(d^{n-1}) \cdot d^{n-1} = 0$")
    cok_d_n_1 = ax.arrow(0, 1, 1 * 0.9, 0 * 0.9,
                         head_width=0.1, head_length=0.1,
                         fc='k', ec='k')
    for i in range(40):
        writer.grab_frame()

    # universality
    operation.set_text("universality of $\mathrm{cok}(d^{n-1})$")
    right_commutativity = ax.text(0.5, 0.5, r"$\circlearrowright$", fontsize=20, ha='center', va='center')

    x0, y0 = 1, 1
    dx, dy = 0, -1
    frame_count = 100

    for i in range(frame_count):
        x = x0 + (i * dx) / (frame_count - 1)
        y = y0 + (i * dy) / (frame_count - 1)

        univ = ax.arrow(1, 1, (x - 1) * 0.9, (y - 1) * 0.9,
                        head_width=0.1, head_length=0.1,
                        fc='r', ec='r')
        writer.grab_frame()
        univ.remove()

    # pause
    univ = ax.arrow(1, 1, 0 * 0.9, -1 * 0.9,
                    head_width=0.1, head_length=0.1,
                    fc='k', ec='k')

    for i in range(40):
        writer.grab_frame()
    univ.remove()

    # replace objects
    operation.set_text(r"$\psi \cdot \mathrm{cok}(d^{n-1}) \cdot \mathrm{ker}(\mathrm{cok}(d^{n-1})) = \psi \cdot 0 = 0$")

    obj_im_d_1 = m_n_1
    obj_im_dp_1 = mp_n_1

    obj_im_d_1.set_text(r"$\mathrm{Ker}(\mathrm{cok}(d^{n-1}))$")
    obj_im_dp_1.set_text(r"$\mathrm{Ker}(\mathrm{cok}(d'^{n-1}))$")
    d_n_1.remove()
    f_n.remove()
    cok_d_n_1.remove()
    cok_dp_n_1.remove()

    im_d_1 = ax.arrow(-1, 1, 1, 0, fc='k', ec='k')
    cok_d_n_1 = ax.arrow(0, 1, 1, 0, fc='k', ec='k')
    univ = ax.arrow(1, 1, 0 * 0.9, -1 * 0.9,
                    head_width=0.1, head_length=0.1,
                    fc='k', ec='k')

    for i in range(40):
        writer.grab_frame()
    cok_d_n_1.remove()
    univ.remove()

    # univ・cok(d^{n-1}) = cok(d'^{n-1})・f^n
    operation.set_text(r"$\psi \cdot \mathrm{cok}(d^{n-1}) = \mathrm{cok}(d'^{n-1}) \cdot f^n$")

    x0, y0 = 1, 1
    dx, dy = -1, -1
    frame_count = 100

    for i in range(frame_count):
        x = x0 + (i * dx) / (frame_count - 1)
        y = y0 + (i * dy) / (frame_count - 1)

        univ = ax.arrow(x, y, (1 - x) * 0.9, -y * 0.9,
                        head_width=0.1, head_length=math.hypot(1-x, -y) * 0.1,
                        fc='k', ec='k')
        cok_d_n_1 = ax.arrow(0, 1, x, y - 1, fc='k', ec='k')
        writer.grab_frame()
        univ.remove()
        cok_d_n_1.remove()

    # cok(d'^{n-1})・f^n・im(d^{n-1}) = univ・cok(d^{n-1})・im(d^{n-1}) = univ・0 = 0
    operation.set_text(r"$\mathrm{cok}(d'^{n-1}) \cdot f^n \cdot \mathrm{ker}(\mathrm{cok}(d^{n-1})) = 0$")

    f_n = ax.arrow(0, 1, 0, -1, fc='k', ec='k')
    cok_dp_n_1 = ax.arrow(0, 0, 1 * 0.9, 0 * 0.9,
                          head_width=0.1, head_length=0.1,
                          fc='k', ec='k')
    
    for i in range(40):
        writer.grab_frame()

    # cok(d'^{n-1})・ker(cok(d'^{n-1})) = 0
    operation.set_text(r"$\mathrm{cok}(d'^{n-1}) \cdot \mathrm{ker}(\mathrm{cok}(d'^{n-1})) = 0$")

    im_dp_n_1 = ax.arrow(-1, 0, 1, 0, fc='k', ec='k')
    right_commutativity.set_text('')

    for i in range(40):
        writer.grab_frame()

    # universality
    operation.set_text("universality of $\mathrm{ker}(\mathrm{cok}(d'^{n-1}))$")

    x0, y0 = -1, 1
    dx, dy = 0, -1
    frame_count = 100

    left_commutativity.set_text(r"$\circlearrowright$")

    for i in range(frame_count):
        x = x0 + (i * dx) / (frame_count - 1)
        y = y0 + (i * dy) / (frame_count - 1)

        univ = ax.arrow(-1, 1, (x + 1) * 0.9, (y - 1) * 0.9,
                        head_width=0.1, head_length=0.1,
                        fc='r', ec='r')
        writer.grab_frame()
        univ.remove()

    # pause
    operation.set_text(r"$\psi': \mathrm{Im}(d^{n-1}) \rightarrow \mathrm{Im}(d'^{n-1})$")
    univ = ax.arrow(-1, 1, 0 * 0.9, -1 * 0.9,
                    head_width=0.1, head_length=0.1,
                    fc='r', ec='r')

    for i in range(40):
        writer.grab_frame()
    univ.remove()
