import glob
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([-2, 2])
ax.set_ylim([-1, 1])

colors = ["black", "blue", "red"]

variables = {
    'x':float(),
    'y':float(),
    'class':int()
}
df = pd.DataFrame(variables, index=[])

files = glob.glob("data-*.csv")
save_name = f"data-{len(files) + 1}.csv"
print("save_name", save_name)

def onclick(event):
    if event.button != 2:
        c = 0 if event.button == 1 else 1
        print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f, class=%d' % (event.button, event.x, event.y, event.xdata, event.ydata, c))
        plt.scatter(event.xdata, event.ydata, marker=',', color=colors[c])
        global df
        df = df.append({"x": event.xdata, "y": event.ydata, "class": c}, ignore_index=True)
        fig.canvas.draw()
    else:
        print(f"SAVED {save_name}")
        print(df["class"].value_counts())
        df["class"] = df["class"].astype(int)
        df.to_csv(save_name, index=False)

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()