import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os
from playsound import playsound
from pathlib import Path
from add_event_dialog import AddEventDialog

class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Przypominajka')
        self.root.geometry('800x600')
        
        # Ustawienie nowoczesnego stylu
        style = ttk.Style()
        style.theme_use('clam')
        
        # Kolory i style
        self.bg_color = '#f5f5f7'
        self.accent_color = '#0071e3'
        self.text_color = '#1d1d1f'
        self.secondary_color = '#86868b'
        
        self.root.configure(bg=self.bg_color)
        
        # Konfiguracja stylów
        style.configure('TFrame',
            background=self.bg_color
        )
        
        style.configure('Accent.TButton',
            background=self.accent_color,
            foreground='white',
            font=('SF Pro Text', 13),
            padding=(20, 10),
            borderwidth=0,
            relief='flat'
        )
        style.map('Accent.TButton',
            background=[('active', '#0077ed')],
            relief=[('pressed', 'flat')]
        )
        
        style.configure('Secondary.TButton',
            background='#ffffff',
            foreground=self.text_color,
            font=('SF Pro Text', 13),
            padding=(20, 10),
            borderwidth=1,
            relief='solid'
        )
        style.map('Secondary.TButton',
            background=[('active', '#f5f5f7')],
            relief=[('pressed', 'solid')]
        )
        
        style.configure('Treeview',
            background='white',
            fieldbackground='white',
            foreground=self.text_color,
            font=('SF Pro Text', 13),
            borderwidth=0,
            rowheight=40
        )
        
        style.configure('Treeview.Heading',
            background='white',
            foreground=self.secondary_color,
            font=('SF Pro Text', 12, 'bold'),
            borderwidth=0,
            padding=(10, 5)
        )
        style.map('Treeview',
            background=[('selected', '#f0f0f0')],
            foreground=[('selected', self.text_color)]
        )
        
        # Dane
        self.events = []
        self.load_events()
        
        # Główny kontener
        main_frame = ttk.Frame(root, style='TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Nagłówek
        header_frame = ttk.Frame(main_frame, style='TFrame')
        header_frame.pack(fill=tk.X, pady=(0, 30))
        
        header = ttk.Label(
            header_frame,
            text='Przypominajka',
            font=('SF Pro Display', 34, 'bold'),
            foreground=self.text_color,
            background=self.bg_color
        )
        header.pack(side=tk.LEFT)
        
        subtitle = ttk.Label(
            header_frame,
            text='Twoje przypomnienia',
            font=('SF Pro Text', 15),
            foreground=self.secondary_color,
            background=self.bg_color
        )
        subtitle.pack(side=tk.LEFT, padx=(10, 0), pady=(15, 0))
        
        # Przyciski
        button_frame = ttk.Frame(main_frame, style='TFrame')
        button_frame.pack(fill=tk.X, pady=(0, 30))
        
        add_btn = ttk.Button(
            button_frame,
            text='Dodaj przypomnienie',
            command=self.add_event,
            style='Accent.TButton'
        )
        add_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        delete_btn = ttk.Button(
            button_frame,
            text='Usuń zaznaczone',
            command=self.delete_event,
            style='Secondary.TButton'
        )
        delete_btn.pack(side=tk.LEFT)
        
        # Lista wydarzeń
        self.event_list = ttk.Treeview(
            main_frame,
            columns=('name', 'date', 'countdown'),
            show='headings'
        )
        
        self.event_list.heading('name', text='Nazwa')
        self.event_list.heading('date', text='Data')
        self.event_list.heading('countdown', text='Pozostało')
        
        self.event_list.pack(fill=tk.BOTH, expand=True)
        
        # Aktualizacja odliczania
        self.update_countdown()
    
    def load_events(self):
        try:
            with open('events.json', 'r') as f:
                self.events = json.load(f)
        except FileNotFoundError:
            self.events = []
    
    def save_events(self):
        with open('events.json', 'w') as f:
            json.dump(self.events, f)
    
    def add_event(self):
        dialog = AddEventDialog(self.root)
        result = dialog.show()
        
        if result:
            self.events.append(result)
            self.save_events()
            self.refresh_events()
    
    def delete_event(self):
        selected = self.event_list.selection()
        if selected:
            for item in selected:
                event_data = self.event_list.item(item)
                self.events.remove(next(
                    event for event in self.events
                    if event['name'] == event_data['values'][0]
                ))
            self.save_events()
            self.refresh_events()
    
    def refresh_events(self):
        for item in self.event_list.get_children():
            self.event_list.delete(item)
        
        for event in self.events:
            event_time = datetime.strptime(event['datetime'], '%Y-%m-%d %H:%M')
            now = datetime.now()
            
            if event_time > now:
                delta = event_time - now
                days = delta.days
                hours = delta.seconds // 3600
                minutes = (delta.seconds % 3600) // 60
                
                countdown = f'{days}d {hours}h {minutes}m'
                
                self.event_list.insert(
                    '',
                    'end',
                    values=(event['name'], event['datetime'], countdown)
                )
    
    def check_reminders(self):
        now = datetime.now()
        for event in self.events:
            event_time = datetime.strptime(event['datetime'], '%Y-%m-%d %H:%M')
            if event_time <= now:
                self.show_notification(event)
                self.events.remove(event)
        self.save_events()
    
    def show_notification(self, event):
        try:
            playsound('notification.mp3')
        except:
            pass
        
        messagebox.showinfo(
            'Przypomnienie!',
            f'Wydarzenie: {event["name"]}\nCzas: {event["datetime"]}'
        )
    
    def update_countdown(self):
        self.refresh_events()
        self.check_reminders()
        self.root.after(1000, self.update_countdown)

def main():
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()