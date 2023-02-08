import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('resources/salarys.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color="#444444", linestyle = '--', label='All Devs')
plt.plot(ages, py_salaries, label = 'Python')
plt.plot(ages, js_salaries, label='JavaScript')

overall_median = 60000

plt.fill_between(ages, py_salaries, y2 = overall_median, where=(py_salaries > overall_median), alpha= 0.25)

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()