from classes.Mission import Mission



class MissionManager():
    def __init__(self):
        self.missions = []

    def add_mission(self, mission: Mission):
        self.missions.append(mission)
        print(f"Mission '{mission.mission_name}' added.")


    def list_missions(self):
        print("\n Current Missions")
        for mission in self.missions:
            print(f"- {mission.mission_name} (Target: {mission.target})")

    def remove_mission(self, mission_name: str):
        self.missions = [m for m in self.missions if m.mission_name != mission_name]
        print(f"Mission '{mission_name}' removed.")

    def briefing_all(self):
        for mission in self.missions:
            mission.briefing()
