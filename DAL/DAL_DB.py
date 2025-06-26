import mysql.connector


class DALagent:

    def __init__(self, host, user, password, database, table):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.table = table


    def select(self, query):
        with mysql.connector.connect(host= self.host, user= self.user, password= self.password, database= self.database) as connection:
            basic_query = f"SELECT * FROM {self.table}"
            cursor = connection.cursor()
            cursor.execute(basic_query + query)
            rows_agents = cursor.fetchall()
            return rows_agents


    def insert(self, table_columns,  new_values):
        with mysql.connector.connect(host= self.host, user= self.user, password= self.password, database= self.database) as connection:
            columns = ", ".join(table_columns)
            values = "', '".join(new_values)
            query = f"INSERT INTO {self.table}({columns}) VALUES('{values}')"
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()

    def delete(self, condition):
        with mysql.connector.connect(host= self.host, user= self.user, password= self.password, database= self.database) as connection:
            query = f"DELETE FROM {self.table} WHERE {condition}"
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()


    def update(self, update, condition):
        with mysql.connector.connect(host= self.host, user= self.user, password= self.password, database= self.database) as connection:
            query = f"UPDATE {self.table} SET {update} WHERE {condition}"
            cursor = connection.cursor()
            cursor.execute()
            connection.commit()




# x = DALagent( host = "localhost", user = "root", password = "", database = "agentDB", table= "agents")
# x.insert(("codeName", "realName", "location", "status", "missionsCompleted"), ("f", "or", "USA", "alive", "2"))
# print(x.select(""))