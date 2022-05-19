# 15.1. 15.2.
import matplotlib.pyplot as plt


x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap='Greens', edgecolor='none', s=30)

# Zdefiniowanie tytulu wykresu i etykiet osi.
plt.title("Szesciany liczb", fontsize=24)
plt.xlabel("Wartosc", fontsize=14)
plt.ylabel("Szesciany wartosci", fontsize=14)

# Zdefiniowanie wielkosci etykiet
plt.tick_params(axis='both', labelsize=14)

plt.show()
