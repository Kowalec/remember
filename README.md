# Remember

[English](#english) | [Polski](#polski)

## Polski

Remember to nowoczesna aplikacja do zarządzania przypomnieniami, stworzona w języku Python z wykorzystaniem interfejsu graficznego Tkinter. Aplikacja pozwala na efektywne zarządzanie zadaniami i wydarzeniami, wysyłając powiadomienia w określonym czasie.

### Funkcjonalności

- 🎯 Tworzenie przypomnień z nazwą i datą
- ⏰ Precyzyjne ustawianie daty i godziny
- 🔔 Powiadomienia dźwiękowe
- 📊 Przejrzysty interfejs użytkownika
- ⏳ Dynamiczne odliczanie czasu do wydarzenia
- 🗑️ Łatwe zarządzanie przypomnieniami (dodawanie/usuwanie)

### Wymagania systemowe

- Python 3.x
- Biblioteki Python (instalowane automatycznie):
  - tkinter
  - playsound==1.2.2
  - python-dateutil>=2.8.2

### Instalacja

1. Sklonuj repozytorium:
```bash
git clone https://github.com/kowalec/remember.git
cd remember
```

2. Zainstaluj wymagane biblioteki:
```bash
pip install -r requirements.txt
```

### Uruchomienie

Uruchom aplikację komendą:
```bash
python main.py
```

### Zrzuty ekranu

![Główne okno aplikacji](https://kowalec.pl/rem1.png)
*Główne okno aplikacji z listą przypomnień*

![Dodawanie nowego przypomnienia](https://kowalec.pl/rem2.png)
*Okno dodawania nowego przypomnienia*

### Użytkowanie

1. Kliknij "Dodaj przypomnienie" aby utworzyć nowe wydarzenie
2. Wprowadź nazwę wydarzenia
3. Wybierz datę z kalendarza
4. Ustaw godzinę przypomnienia
5. Zatwierdź przyciskiem "Zapisz"

Aplikacja będzie działać w tle i wyświetli powiadomienie o określonej godzinie.

---

## English

Remember is a modern reminder management application built in Python using the Tkinter graphical interface. The application allows for efficient task and event management, sending notifications at specified times.

### Features

- 🎯 Create reminders with name and date
- ⏰ Precise date and time setting
- 🔔 Sound notifications
- 📊 Clean user interface
- ⏳ Dynamic countdown to events
- 🗑️ Easy reminder management (add/delete)

### System Requirements

- Python 3.x
- Python libraries (automatically installed):
  - tkinter
  - playsound==1.2.2
  - python-dateutil>=2.8.2

### Installation

1. Clone the repository:
```bash
git clone https://github.com/kowalec/remember.git
cd remember
```

2. Install required libraries:
```bash
pip install -r requirements.txt
```

### Running the Application

Launch the application with:
```bash
python main.py
```

### Screenshots

![Main application window](https://kowalec.pl/rem1.png)
*Main application window with reminders list*

![Adding a new reminder](https://kowalec.pl/rem2.png)
*New reminder creation window*

### Usage

1. Click "Add reminder" to create a new event
2. Enter the event name
3. Select a date from the calendar
4. Set the reminder time
5. Confirm with "Save" button

The application will run in the background and display a notification at the specified time.