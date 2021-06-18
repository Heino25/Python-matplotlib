#grid chart
import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [2,4,6,8,16]

plt.plot(x1, y1, "r-.o", label='students')
plt.legend(loc='best')
plt.xlabel("Horizontal_Title")
plt.ylabel("Vertical_Title")
plt.title("Your Title")
plt.grid(linewidth=2.0,linestyle='-', color='black')
plt.show()