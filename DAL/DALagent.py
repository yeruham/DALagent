import mysql.connector
from DAL.DAL_DB import DALagent
from models.agent import Agent


class DALagent(DALagent):

    def __init__(self):
        super().__init__(host = "localhost", user = "root", password = "", database = "agentDB", table= "agents")

    def select_agents(self, condition= ""):
        rows = self.select(condition)
        agents = []
        for row in rows:
            if (len(row) == 6):
                id = row[0]
                code_name = row[1]
                real_name = row[2]
                location = row[3]
                status = row[4]
                missions_completed = row[5]
                agent = Agent(code_name, real_name, location, status, missions_completed, id)
                agents.append(agent)
        return agents


    def select_agent_by_id(self, id):
        condition = f" WHERE id = '{id}'"
        return self.select_agents(condition)

    def select_agent_by_name(self, name):
        condition = f" WHERE realName = '{name}'"
        return self.select_agents(condition)

    def select_agent_by_code_name(self, code_name):
        condition = f" WHERE codeName = '{code_name}'"
        return self.select_agents(condition)





x = DALagent()
print(x.select_agents())
print(x.select_agent_by_id('5'))
print(x.select_agent_by_name("yeruham"))
print(x.select_agent_by_code_name("f"))
