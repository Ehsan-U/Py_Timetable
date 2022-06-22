import openpyxl
from rich.console import Console
c = Console()
from hashlib import md5

class TimeTable():
    def __init__(self):
        self.hashes = {}
        self.conflict = {'conflicts':[]}
        self.weekly = {}
        self.wb = openpyxl.load_workbook('timetable.xlsx')
        self.it = self.wb['BSIT(M)-VIII']

    def get_data(self):
        for row in self.it.iter_rows():
            for cell in row:
                if cell.value and cell.row != 1:
                    if cell.column == 1:
                        day = cell.value
                        self.weekly[day] = []
                    if cell.column == 5:
                        # print(cell.value,row[5].value,row[6].value)
                        teacher = cell.value
                        timing = row[5].value
                        room = row[6].value
                        self.weekly[day].append([day.lower(), teacher.lower(), timing.lower(), room.lower()])
    def evaluate(self):
        for day, val in self.weekly.items():
            if val:
                for v in val:
                    dtr = v[0]
                    dtr += v[2]
                    dtr += v[3]
                    unique_id = md5(dtr.encode()).hexdigest()
                    if unique_id not in self.hashes:
                        self.hashes[unique_id] = v[1]
                    else:
                        self.conflict['conflicts'].append([self.hashes.get(unique_id),v[1],v[2]])
        
t = TimeTable()
t.get_data()
t.evaluate()
c.print(t.conflict)
