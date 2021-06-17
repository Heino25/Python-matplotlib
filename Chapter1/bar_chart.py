#line chart
import matplotlib.pyplot as plt

x1 = [1,2,3,4,5,6,7,8]
y1 = [2,4,6,8,10,2,4,6]

colors = ['green', 'red', 'blue', 'orange', 'lightblue' ]

plt.bar(x1, y1, edgecolor='black', color=colors, linewidth=2)
# plt.barh(x1, y1)
plt.xlabel("Horizontal_Title")
plt.ylabel("Vertical_Title")
plt.title("Your Title")
plt.show()