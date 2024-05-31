from itemadapter import ItemAdapter
import sqlite3

class ComponentsPipeline:
    def __init__(self):
        self.con = sqlite3.connect('components.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS components(
        processor TEXT,
        gpu TEXT,
        motherboard TEXT,
        ram TEXT
        )""")

    def process_item(self, item, spider):
        processors = item.get('processors', [])
        gpus = item.get('gpus', [])
        motherboards = item.get('motherboards', [])
        rams = item.get('rams', [])

        max_length = max(len(processors), len(gpus), len(motherboards), len(rams))
        processors.extend([''] * (max_length - len(processors)))
        gpus.extend([''] * (max_length - len(gpus)))
        motherboards.extend([''] * (max_length - len(motherboards)))
        rams.extend([''] * (max_length - len(rams)))

        for i in range(max_length):
            self.cur.execute("INSERT INTO components  VALUES (?, ?, ?, ?)",
                             (processors[i],
                              gpus[i],
                              motherboards[i],
                              rams[i]))

        self.con.commit()
        return item
