from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.1,0]
colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

plt.pie(slices, labels=labels, explode=explode, shadow = True,
         startangle = 45, autopct='%1.1f%%',
         wedgeprops={'edgecolor': 'white'})

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()