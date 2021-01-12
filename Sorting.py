from tkinter import ttk, END

from connection import cur


class Sorting():
    def __init__(self, win, query, table, fieldRU, fieldEN):
        self.query = query
        self.table = table
        self.fieldsRU = fieldRU
        self.fieldsEN = fieldEN

        self.fieldsRU.append('Отмена')
        self.fieldsEN.append('Отмена')
        self.field = ''

        self.combosorting = ttk.Combobox(win, width=17, values=self.fieldsRU)
        self.combosorting.bind('<<ComboboxSelected>>', self.sort)

        self.Create()

    def Create(self):
        self.combosorting.grid(row=1, column=1)

    def sort(self, event):
        try:

            for i in range(0, len(self.fieldsRU)):
                if self.combosorting.get() == self.fieldsRU[i]:
                    self.field = self.fieldsEN[i]
            if self.field != 'Отмена':
                self.table.delete(*self.table.get_children())
                cur.execute(self.query + ' ORDER BY {0} LIMIT 5 OFFSET 0 '.format(self.field))
                rows = cur.fetchall()
                for row in rows:
                    self.table.insert("", "end", values=row)
            else:
                self.table.delete(*self.table.get_children())
                cur.execute(self.query + ' LIMIT 5 OFFSET 0')
                rows = cur.fetchall()
                for row in rows:
                    self.table.insert("", "end", values=row)
                self.combosorting.delete(0, END)
        except:
            pass