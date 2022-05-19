import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Tworzenie nowego bladzenia losowego, dopoki program pozostaje aktywny.
while True:
    # Przygotowanie danych bladzenia losowego i wyswietlenie puntkow.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Okreslenie wielkosci okna wykresu
    plt.figure(dpi=192, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap="Blues", edgecolor='none', s=1)
    # plt.plot(rw.x_values, rw.y_values, linewidth=0.3)  # 15.3.

    # Podkreslenie pierwszego i ostatniego punktu bladzenia losowego.
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

    # Ukrycie osi
    plt.axis('off')

    plt.show()

    keep_running = input("Utworzyc kolejne bladzenia losowe? (t/n): ")
    if keep_running == 'n':
        break
