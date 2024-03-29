from datetime import datetime
from tkinter import *

from Revenue import Revenue
from Tables.clients import Clients
from Tables.discount import Discount
from Tables.reservation import Reservation
from Tables.room import Room
from Tables.type import RoomType
from Tables.users import Users
from connection import cur, conn


class ManagerPanel:
    def __init__(self):
        self.win = Tk()
        self.frame = Frame(self.win)
        self.win.title('Панель менеджера')
        self.win.geometry('800x650')
        self.Create()

    def Create(self):
        menu = Menu(self.win)
        file_menu = Menu(menu, tearoff=0)

        file_menu.add_command(label="Комнаты", command=self.CreateRoom)
        file_menu.add_command(label="Клиенты", command=self.CreateClient)
        file_menu.add_command(label="Бронирование", command=self.CreateReserv)
        file_menu.add_separator()

        menu.add_cascade(label="Таблицы", menu=file_menu)
        menu.add_cascade(label='Прибыль', command=self.CreateRevenue)
        self.win.configure(menu=menu)
        self.frame.grid(row=0, column=0)

        now = datetime.now().date().strftime('%d.%m.%Y')
        cur.execute('SELECT room, departure_date FROM reservation')
        date = cur.fetchall()
        for i in date:
            if i[1] < now:
                cur.execute('UPDATE rooms SET busy = 0 WHERE id={0}'.format(i[0]))
                conn.commit()

        self.win.mainloop()

    def CreateRoom(self):
        try:
            for widget in self.frame.winfo_children():
                widget.destroy()
        except:
            pass
        Room(self.frame)

    def CreateClient(self):
        try:
            for widget in self.frame.winfo_children():
                widget.destroy()
        except:
            pass
        self.clients = Clients(self.frame)
        self.clients.create()

    def CreateReserv(self):
        try:
            for widget in self.frame.winfo_children():
                widget.destroy()
        except:
            pass
        self.reservation = Reservation(self.frame)
        self.reservation.create()

    def CreateRevenue(self):
        revenue = Revenue()
        revenue.MonthlyRevenue()