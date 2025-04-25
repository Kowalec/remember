import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime

class AddEventDialog:
    def __init__(self, parent):
        self.dialog = tk.Toplevel(parent)
        self.dialog.title('Dodaj przypomnienie')
        self.dialog.geometry('400x600')
        self.dialog.transient(parent)
        self.dialog.configure(bg='#ffffff')
        
        # Efekt szkła
        self.dialog.attributes('-alpha', 0.97)
        
        # Styl
        style = ttk.Style()
        style.configure('Dialog.TFrame', background='#ffffff')
        style.configure('Dialog.TLabel',
            background='#ffffff',
            foreground='#1d1d1f',
            font=('SF Pro Text', 13)
        )
        style.configure('Dialog.TEntry',
            fieldbackground='#ffffff',
            borderwidth=0,
            relief='flat',
            padding=12
        )
        
        # Główny kontener z cieniem
        container_frame = ttk.Frame(self.dialog)
        container_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        main_frame = ttk.Frame(container_frame, style='Dialog.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # Nagłówek
        header = ttk.Label(main_frame,
            text='Nowe przypomnienie',
            font=('SF Pro Display', 28, 'bold'),
            background='#ffffff',
            foreground='#1d1d1f'
        )
        header.pack(anchor=tk.W, pady=(0, 24))
        
        # Nazwa wydarzenia
        name_label = ttk.Label(main_frame,
            text='Nazwa wydarzenia',
            style='Dialog.TLabel'
        )
        name_label.pack(anchor=tk.W, pady=(0, 8))
        
        entry_frame = ttk.Frame(main_frame, style='Dialog.TFrame')
        entry_frame.pack(fill=tk.X, pady=(0, 24))
        entry_frame.configure(style='EntryContainer.TFrame')
        
        self.name_entry = ttk.Entry(entry_frame,
            width=40,
            style='Dialog.TEntry',
            font=('SF Pro Text', 13)
        )
        self.name_entry.pack(fill=tk.X, padx=2, pady=2)
        
        # Dodanie stylu dla kontenera entry
        style.configure('EntryContainer.TFrame',
            background='#f5f5f7',
            borderwidth=0,
            relief='flat'
        )
        
        # Kalendarz
        cal_label = ttk.Label(main_frame,
            text='Data przypomnienia',
            style='Dialog.TLabel'
        )
        cal_label.pack(anchor=tk.W, pady=(0, 8))
        
        calendar_frame = ttk.Frame(main_frame, style='Dialog.TFrame')
        calendar_frame.pack(fill=tk.X, pady=(0, 24))
        calendar_frame.configure(style='CalendarContainer.TFrame')
        
        self.calendar = Calendar(
            calendar_frame,
            selectmode='day',
            date_pattern='y-mm-dd',
            showweeknumbers=False,
            background='#ffffff',
            foreground='#1d1d1f',
            headersbackground='#ffffff',
            headersforeground='#86868b',
            selectbackground='#0071e3',
            font=('SF Pro Text', 13),
            borderwidth=0,
            relief='flat'
        )
        self.calendar.pack(padx=2, pady=2)
        
        # Styl dla kontenera kalendarza
        style.configure('CalendarContainer.TFrame',
            background='#f5f5f7',
            borderwidth=0,
            relief='flat'
        )
        
        # Czas
        time_label = ttk.Label(main_frame,
            text='Godzina przypomnienia',
            style='Dialog.TLabel'
        )
        time_label.pack(anchor=tk.W, pady=(0, 8))
        
        time_container = ttk.Frame(main_frame, style='Dialog.TFrame')
        time_container.pack(fill=tk.X)
        time_container.configure(style='TimeContainer.TFrame')
        
        time_frame = ttk.Frame(time_container, style='Dialog.TFrame')
        time_frame.pack(padx=2, pady=2)
        
        # Styl dla kontenera czasu
        style.configure('TimeContainer.TFrame',
            background='#f5f5f7',
            borderwidth=0,
            relief='flat'
        )
        
        style.configure('Time.TSpinbox',
            fieldbackground='#ffffff',
            borderwidth=0,
            relief='flat',
            padding=12,
            arrowsize=13
        )
        
        # Style dla przycisków
        style.configure('Accent.TButton',
            background='#0071e3',
            foreground='white',
            font=('SF Pro Text', 13, 'bold'),
            padding=(20, 12),
            borderwidth=0,
            relief='flat'
        )
        style.map('Accent.TButton',
            background=[('active', '#0077ed')],
            relief=[('pressed', 'flat')]
        )
        
        style.configure('Secondary.TButton',
            background='#f5f5f7',
            foreground='#1d1d1f',
            font=('SF Pro Text', 13),
            padding=(20, 12),
            borderwidth=0,
            relief='flat'
        )
        style.map('Secondary.TButton',
            background=[('active', '#e5e5e5')],
            relief=[('pressed', 'flat')]
        )
        
        self.hour_spinbox = ttk.Spinbox(
            time_frame,
            from_=0,
            to=23,
            width=4,
            format='%02.0f',
            font=('SF Pro Text', 13),
            style='Time.TSpinbox'
        )
        self.hour_spinbox.pack(side=tk.LEFT)
        
        separator = ttk.Label(time_frame,
            text=':',
            style='Dialog.TLabel',
            font=('SF Pro Text', 18)
        )
        separator.pack(side=tk.LEFT, padx=10)
        
        self.minute_spinbox = ttk.Spinbox(
            time_frame,
            from_=0,
            to=59,
            width=4,
            format='%02.0f',
            font=('SF Pro Text', 13),
            style='Time.TSpinbox'
        )
        self.minute_spinbox.pack(side=tk.LEFT)
        
        # Przyciski
        button_frame = ttk.Frame(main_frame, style='Dialog.TFrame')
        button_frame.pack(fill=tk.X, pady=(30, 0))
        
        save_btn = ttk.Button(
            button_frame,
            text='Zapisz',
            command=self.save_event,
            style='Accent.TButton'
        )
        save_btn.pack(side=tk.RIGHT)
        
        cancel_btn = ttk.Button(
            button_frame,
            text='Anuluj',
            command=self.dialog.destroy,
            style='Secondary.TButton'
        )
        cancel_btn.pack(side=tk.RIGHT, padx=(0, 10))
        
        self.result = None
        
    def save_event(self):
        date = self.calendar.get_date()
        hour = self.hour_spinbox.get()
        minute = self.minute_spinbox.get()
        
        try:
            event_time = datetime.strptime(
                f'{date} {hour}:{minute}',
                '%Y-%m-%d %H:%M'
            )
            
            self.result = {
                'name': self.name_entry.get(),
                'datetime': event_time.strftime('%Y-%m-%d %H:%M')
            }
            self.dialog.destroy()
        except ValueError:
            tk.messagebox.showerror(
                'Błąd',
                'Nieprawidłowy format daty lub czasu'
            )
    
    def show(self):
        self.dialog.grab_set()
        self.dialog.wait_window()
        return self.result