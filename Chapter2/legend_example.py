import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]
y2 = [1,1,2,3,5]

plt.plot(x1, y1, 'ro-', label='studens')
plt.plot(x1, y2, 'b^-', label='teachers')

plt.subplots_adjust(right=0.7, bottom=0.3)
plt.legend(bbox_to_anchor=(1.05,1))
plt.title("Your title")
plt.xlabel("Horizontal_Title")
plt.ylabel("Vertical_Title")
plt.grid(True)
plt.show()