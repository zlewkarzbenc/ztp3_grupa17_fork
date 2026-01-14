# Wizualizacja poziomu zanieczyszczeń (PM2.5)

## Cel projektu
Głównym celem projektu była analiza godzinnych pomiarów stężeń drobnego pyłu **PM2.5** (pyłu o średnicy poniżej 2.5 µm) w latach **2015, 2018, 2021 i 2024**. Pyły PM2.5 są bardzo szkodliwe dla zdrowia, gdyż mogą przenikać głęboko do układu oddechowego oraz krwiobiegu.

Dane niezbędne do analizy jakości powietrza w Polsce zostały pozyskane ze strony [https://powietrze.gios.gov.pl/pjp/current](https://powietrze.gios.gov.pl/pjp/current). Dane historyczne wykorzystane w projekcie pochodzą z archiwów GIOŚ. Każdy rok udostępniany jest w postaci oddzielnego archiwum ZIP dostępnego pod adresem: [https://powietrze.gios.gov.pl/pjp/archives](https://powietrze.gios.gov.pl/pjp/archives).

Projekt stanowi rozwinięcie i modyfikację rozwiązania *Małego Projektu 1* do wersji projektowej, w której kod został uporządkowany i podzielony na moduły, a notatnik *.ipynb* wykorzystuje przygotowane funkcje.

### Struktura projektu
- *get_data.py*: wczytanie, czyszczenie i łączenie danych
- *stats.py*: przygotowanie danych i obliczenia statystyczne
- *plots.py*: generowanie wykresów
- *Proj1_WL_KW.ipynb*: analiza i interpretacje z użyciem funkcji z powyższych modułów .py
- *tests/*: testy jednostkowe (pytest)


### Etap 1: Wczytanie i czyszczenie danych - get_data.py
Pierwszym etapem było wczytanie metadanych oraz danych dla lat: **2015, 2018, 2021 i 2024** za pomocą funkcji download_gios_meta, download_gios_archive. Następnie dane zostały oczyszczone i ujednolicone:
- usunięto niepotrzebne wiersze oraz ujednolicono format danych (funkcja clean_pm25)
- pomiary dokonane o północy (00:00:00) potraktowano jako te dotyczące poprzedniego dnia (funkcja midnight)
- zaktualizowano stare kody stacji zgodnie z metadanymi (funkcja update_stations)
- kody stacji uzupełniono o miejscowości dostępne w metadanych (funkcja add_city) 
- pozostawiono tylko stacje występujące we wszystkich czterech latach i zapisano do jednego DataFrame (funkcja make_pm25_data). 

### Etap 2: Liczenie średnich i wskazywanie dni z przekroczeniem normy - stats.py
W kolejnym etapie wykonano obliczenia statystyczne na danych przygotowanych za pomocą funkcji convert_df:
- obliczono średnie miesięczne stężenia PM2.5 dla każdej stacji i roku (calc_monthly_means) 
- obliczono średnie miesięczne stężenia PM2.5 uśrednione po wszystkich stacjach dla **Warszawy** i **Katowic** (funkcja calc_monthly_city_means) 
- obliczono dzienne średnie stężenia PM2.5 dla każdej stacji (funkcja calc_daily_means)
- dla każdej stacji i roku obliczono liczbę dni, w których wystąpiło przekroczenie dobowej normy stężenia PM2.5 (15 µg/m³) oraz wyznaczono 3 stacje z najmniejszą i 3 stacje z największą liczbą dni z przekroczeniem normy dobowej (funkcja top_bottom_stations)

### Etap 3: Wizualizacja - plots.py
Ostatnim etapem było przygotowanie wizualizacji wyników:
- wykres liniowy przedstawiający trend średnich miesięcznych wartości PM2.5 w latach 2015 i 2024 roku dla **Warszawy** i **Katowic** (funkcja plot_means)
- heatmapy średnich miesięcznych stężeń PM2.5 w latach 2015, 2018, 2021 i 2024 dla każdej miejscowości (funkcja heatmaps_means). 
- *grouped barplot* dla 3 stacji z najmniejszą i 3 stacji z największą liczbą dni z przekroczeniem dobowej normy stężenia PM2.5 (funkcja plot_overnorm)

### Testy jednostkowe
Projekt zawiera również testy jednostkowe, znajdujące się w plikach *test_get_data.py* oraz *test_stats.py*, weryfikujące poprawność działania funkcji zaimplementowanych w modułach *get_data.py* i *stats.py*.

### Release i CI
Projekt posiada wersjonowanie (release) oraz skonfigurowane uruchamianie testów po dodaniu nowego kodu (CI).

### Podział pracy
- Wojtek Laskowski: odpowiedzialny za przygotowanie repozytorium i modyfikację rozwiązania *Małego Projektu 1* do wersji projektowej
- Karolina Winczewska: odpowiedzialna za przygotowanie testów, dokumentacji, zrobienie release’u, skonfigurowane uruchamianie testów po dodaniu nowego kodu (CI)
 



