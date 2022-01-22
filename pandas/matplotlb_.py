import matplotlib.pyplot as plt
import pandas as pd

# plt.plot([1, 5, 2, 9])
# plt.plot([3, -9, 0])
# plt.show()

# plt.plot([1, 5, 2, 9], [3, -9, 2, 1])
# plt.show()

# plt.bar([1, 5, 2, 9], [3, -9, 2, 1])
# plt.show()


df = pd.read_csv('city.csv')
data = df.groupby('region')[['population']].sum().sort_values(by='population', ascending=False).head(10)
print(data)

plt.bar(data.index, data.population)
plt.title('Численность населения 10 регионов')
plt.legend(['Население'])
plt.xticks(rotation=90)
plt.xlabel('Регионы')
plt.ylabel('Млн человек')
plt.grid()
plt.show()
