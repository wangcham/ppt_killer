import sqlite3
#create table
table_one = """
CREATE TABLE if not exists info(
    token VARCHAR(255),
    type INT,
    content TEXT
)
"""


class database:
    def execute(self,query,args=None):
        self.conn = None
        self.cursor = None        
        try:
            self.conn = sqlite3.connect('sql.db')
            self.cursor = self.conn.cursor()

            if args:
                self.cursor.execute(query,args)
            else:
                self.cursor.execute(query)
            
            results = self.cursor.fetchall()
            self.conn.commit()
            
            return results
        
        except Exception as e:
            print(e)
            if self.conn:
                self.conn.rollback()

    
    def close(self):
        if self.conn:
            self.conn.close()
    
    def create(self):
        self.execute(table_one)
        print("成功建表")
        
    