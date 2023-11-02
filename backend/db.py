import sqlite3
table_one = """
CREATE TABLE if not exists info(
    username VARCHAR(255),
    text TEXT
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
        
        sql = """
        INSERT INTO info (username,text) VALUES (?,?);
        """
        self.execute(sql,("SQLite数据库","成功启动！"))

    def show(self):
        sql = "select * from info;"
        results = self.execute(sql)
        if results:
            print(results[0][0]+results[0][1])
    