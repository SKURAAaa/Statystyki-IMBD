import pandas as pd
import matplotlib.pyplot as plt

# Wczytaj zbiór danych z pliku CSV
my_loaded_csv = pd.read_csv("imdb_top_1000.csv")

# Usunięcie przecinków z kolumny 'Gross' i konwersja na wartość numeryczną
my_loaded_csv['Gross'] = my_loaded_csv['Gross'].str.replace(',', '').astype(float)

# Ustawienie formatu wyświetlania danych numerycznych
pd.options.display.float_format = '{:.2f}'.format

# Obliczenie średnich zarobków z filmów, grupując dane po gatunkach
mean_gross_by_genre = my_loaded_csv.groupby('Genre')['Gross'].mean().sort_values(ascending=False)

# Utworzenie wykresu
plt.figure(figsize=(14, 6))  # Ustawienie rozmiaru wykresu
mean_gross_by_genre.plot(kind='bar', color='skyblue')  # Wykres słupkowy na podstawie danych
plt.title('Średnie zarobki filmów według gatunku')  # Tytuł wykresu
plt.xlabel('Gatunek filmu')  # Etykieta osi X
plt.ylabel('Średnie zarobki w $')  # Etykieta osi Y
plt.xticks(rotation=45)  # Obrót etykiet osi X dla czytelności
plt.grid(axis='y')  # Dodanie siatki tylko dla osi Y
plt.show()  # Wyświetlenie wykresu

# Usunięcie mniej 'wpływowych' gatunków filmowych
q3 = mean_gross_by_genre.quantile(0.75)
filtered_data = mean_gross_by_genre[mean_gross_by_genre > q3]

# Utworzenie wykresu po filtracji
plt.figure(figsize=(12, 6))  # Ustawienie rozmiaru wykresu
filtered_data.plot(kind='bar', color='skyblue')  # Wykres słupkowy na podstawie danych po filtracji
plt.title('Średnie zarobki filmów według gatunku (po usunięciu mniej wpływowych)')  # Tytuł wykresu
plt.xlabel('Gatunek filmu')  # Etykieta osi X
plt.ylabel('Średnie zarobki w $')  # Etykieta osi Y
plt.xticks(rotation=45, fontsize=8, ha='right')  # Obrót etykiet osi X i zmniejszenie czcionki dla czytelności
plt.ticklabel_format(axis='y', style='plain')  # Wyłączenie notacji naukowej dla osi Y
plt.ylim(min(filtered_data) * 0.9, max(filtered_data) * 1.1)  # Ustawienie zakresu osi Y
plt.grid(axis='y')  # Dodanie siatki tylko dla osi Y
plt.tight_layout()  # Dopasowanie układu
plt.show()  # Wyświetlenie wykresu po filtracji
