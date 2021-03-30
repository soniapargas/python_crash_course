import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
# fig represents entire variable or collection
fig, ax = plt.subplots()
ax.plot(squares)
# This opens a Mtplotlib viewer and displays the plot.
plt.show()