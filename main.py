from DAL.DALagent import DALagent
from models.agent import Agent


class AgentsManager:

    def __init__(self):
        self.DAL = DALagent()

    def start(self):
        run = True

        while run:
            option = self.menu_agents()
            if option == '1':
                self.insert_agent()
            elif option in ['2', '3', '4']:
                self.update_agent(option)
            elif option in ['5', '6', '7', '8']:
                agents =  self.select_agents(option)
                self.print_agents(agents)
            elif option == '9':
                self.delete_agent()
            elif option == '0':
                run = False
            else:
                pass



    def menu_agents(self):

        menu = ("To add new agent enter 1\n"
                "To update location of agent enter 2\n"
                "To update status of agent enter 3\n"
                "To update num missions completed of agent enter 4\n"
                "To get information about all agents enter 5\n"
                "To get information about specific agents by name enter 6\n"
                "To get information about specific agents by code name enter 7\n"
                "To get information about specific agents by id enter 8\n"
                "To delete agent enter 9\n"
                "To exit enter 0\n")

        option = input(menu)
        return option


    def select_agents(self, option):
        agents = []
        if option == '5':
            agents = self.DAL.select_agents()
        elif option == '6':
            name = input("Enter agent's name\n")
            agents = self.DAL.select_agent_by_name(name)
        elif option == '7':
            code_name = input("Enter agent's code name\n")
            agents = self.DAL.select_agent_by_code_name(code_name)
        elif option == '8':
            id = input("Enter agent's id\n")
            agents = self.DAL.select_agent_by_id(id)
        else:
            pass

        return agents


    def print_agents(self, agents):
        print()
        if not isinstance(agents, list) or len(agents) == 0:
            print("The agent not exit")
        for agent in agents:
            if isinstance(agent, Agent):
                print(agent)
        print()


    def insert_agent(self):
        name = input("Enter agent's name\n")
        code_name = input("Enter agent's code name\n")
        location = input("Enter location of agent\n")
        status = input("Enter status of agent\n")
        missions_completed = input("Enter num missions completed of agent\n")
        agent = Agent(code_name, name, location, status, missions_completed)
        self.DAL.insert_new_agent(agent)


    def update_agent(self, option):

        agent_id = self.get_agent_id()
        if agent_id > 0:
            if option == '2':
                location = input("Enter new location of agent\n")
                self.DAL.update_location_by_id(location, agent_id)
            elif option == '3':
                status = input("Enter new status of agent\n")
                self.DAL.update_status_by_id(status, agent_id)
            elif option == '4':
                missions_completed = input("Enter new num missions completed of agent\n")
                self.DAL.update_missions_completed_by_id(missions_completed, agent_id)
            else:
                    pass


    def get_agent_id(self):
        id = -1
        code_name = input("Enter agent's code name\n")
        agents = self.DAL.select_agent_by_code_name(code_name)
        if not isinstance(agents, list) or len(agents) == 0 or not isinstance(agents[0], Agent):
            print("The agent's code name not exit")
        else:
            id = agents[0].id

        return id


    def delete_agent(self):
        agent_id = self.get_agent_id()
        if agent_id > 0:
            self.DAL.delete_agent_by_id(agent_id)





if __name__ == "__main__":

    DAL = AgentsManager()
    DAL.start()