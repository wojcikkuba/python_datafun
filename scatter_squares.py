import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap='Blues', edgecolor='none', s=40)

# Zdefiniowanie tytulu wykresu i etykiet osi.
plt.title("Kwadraty liczb", fontsize=24)
plt.xlabel("Wartosc", fontsize=14)
plt.ylabel("Kwadraty wartosci", fontsize=14)

# Zdefiniowanie wielkosci etykiet.
plt.tick_params(axis='both', which='major', labelsize=14)

# Zdefiniowanie zakresu dla kazdej osi.
plt.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png')
