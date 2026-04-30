# etl-sales-pipeline

ETL zbudowany w Pythonie, służący do automatycznego przetwarzania, czyszczenia i walidacji surowych danych sprzedażowych.

## O Projekcie

Projekt demonstruje pełny cykl życia danych w architekturze modułowej. System pobiera dane z plików CSV, przeprowadza transformację (w tym obliczenia biznesowe np. revenue i segmentację), wykonuje rygorystyczne testy jakości (Data Quality Checks) i zapisuje wynik do ustandaryzowanego formatu.

### Kluczowe Funkcjonalności:
- **Extract**: Pobieranie danych z plików CSV z obsługą błędów.
- **Transform**: 
    - Usuwanie duplikatów i rekordów z brakującymi danymi.
    - Automatyczna konwersja typów danych.
    - Obliczanie przychodu (revenue).
    - Segmentacja klientów za pomocą biblioteki NumPy.
- **Quality Checks**: Wielostopniowa walidacja danych (sprawdzanie braków, duplikatów, poprawności typów i logiki biznesowej) przed zapisem.
- **Load**: Bezpieczny zapis do folderu `data/processed/` z automatycznym tworzeniem struktury katalogów.

## Technologie

- **Python 3.x**
- **Pandas**: Manipulacja i analiza danych.
- **NumPy**: Obliczenia numeryczne i segmentacja.
- **OS**: Zarządzanie ścieżkami systemowymi i automatyzacja folderów.

## Struktura Projektu

```text
etl-sales-pipeline/
├── data/
│   ├── raw/             # Surowe dane wejściowe
│   └── processed/       # Wyczyszczone i sprawdzone dane wynikowe
├── src/                 # Kod źródłowy podzielony na moduły
│   ├── extract.py       # Pobieranie danych
│   ├── transform.py     # Logika transformacji i czyszczenia
│   ├── quality_checks.py # Testy jakości danych (Data Quality)
│   └── load.py          # Ładowanie danych do pliku
├── main.py              # Główny skrypt uruchamiający pipeline
├── requirements.txt     # Zależności projektu
└── README.md            # Dokumentacja
