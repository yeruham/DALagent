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
        condition = f"WHERE id = '{id}'"
        return self.select_agents(condition)

    def select_agent_by_name(self, name):
        condition = f"WHERE realName = '{name}'"
        return self.select_agents(condition)

    def select_agent_by_code_name(self, code_name):
        condition = f"WHERE codeName = '{code_name}'"
        return self.select_agents(condition)



    def update_location_by_id(self, new_location, id):
        update = f"location = '{new_location}'"
        condition = f"WHERE id = '{id}'"
        self.update(update, condition)

    def update_status_by_id(self, new_status ,id):
        update = f"status = '{new_status}'"
        condition = f"WHERE id = '{id}'"
        self.update(update, condition)

    def update_missions_completed_by_id(self,num_missions , id):
        update = f"missionsCompleted = '{num_missions}'"
        condition = f"WHERE id = '{id}'"
        self.update(update, condition)



    def insert_new_agent(self, agent):
        if not isinstance(agent, Agent):
            return None
        table_columns = ("codeName", "realName", "location", "status", "missionsCompleted")
        new_values = (agent.code_name, agent.real_name, agent.location, agent.status, agent.missions_completed)
        self.insert(table_columns, new_values)



    def delete_agent_by_id(self, id):
        condition = f"WHERE id = '{id}'"
        return self.delete(condition)





#
# x = DALagent()
# print(x.select_agents())
# print(x.select_agent_by_id(1)[0])
# print(x.select_agent_by_name("yeruham")[0])
# print(x.select_agent_by_code_name("f")[0])
# x.update_location_by_id("USA", 1)
# x.update_status_by_id("ded", 1)
# x.update_missions_completed_by_id(8, 5)
# print(x.select_agent_by_id(5)[0])
