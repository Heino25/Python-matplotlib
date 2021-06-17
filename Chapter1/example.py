#line chart
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [2,4,6,8,10,2,4,6]

plt.plot(x, y, "b-.o",)
plt.axis([0,10,0,10])
plt.xlabel("Horizontal_Title")
plt.ylabel("Vertical_Title")
plt.title("Your Title")
plt.show()