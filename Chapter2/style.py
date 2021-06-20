import matplotlib.pyplot as plt
import seaborn as sns

# plt.style.use('_classic_test_patch')
print(plt.style.available)
sns.set_style("whitegrid")

x1 = [1,2,3,4,5]
y1 = [2,4,6,8,16]

x2 = [1,2,3,4,5]
y2 = [1,3,9,13,16]

x1 = [1,2,3,4,5]
y1 = [2,4,6,8,10]


plt.bar(x1, y1)
# plt.barh(x1, y1)
plt.xlabel("Horizontal_Title")
plt.ylabel("Vertical_Title")
plt.title("Your Title")
plt.show()