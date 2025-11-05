from classes.Soldier import Soldier
from classes.Agent import Agent
from classes.Mission_Briefing import MissionManager
from classes.Unit_abstract import AbstractUnit, Unit
from classes.Battle_Simulation import Army
from classes.Combined_Mission import Commander, ReconMission, StrikeMission,RescueMission
from classes.New_Units import Infantry90, Sniper, TankUnit
from classes.Strike_Options import Tank, Drone
from classes.Army_Inventory import Weapon

if __name__ == "__main__":
    rifle = Weapon("Rifle", 30)
    pistol = Weapon("Pistol", 15)

    commander_alpha = Commander("John", "Colonel", pistol)
    soldiers_alpha = [Soldier("Mike", "Private", rifle), Soldier("Alex", "Corporal", rifle)]
    alpha_infantry = Infantry90("Alpha Squad", commander_alpha, soldiers_alpha)

    commander_bravo = Commander("Sarah", "Colonel", pistol)
    soldiers_bravo = [Soldier("Emma", "Private", rifle)]
    bravo_tank = TankUnit("Bravo Tanks", commander_bravo, soldiers_bravo)

    commander_charlie = Commander("Luke", "Colonel", pistol)
    soldiers_charlie = [Soldier("Liam", "Private", rifle)]
    charlie_sniper = Sniper("Charlie Snipers", commander_charlie, soldiers_charlie)

    tank1 = Tank("M1A2", 2)
    drone1 = Drone("Reaper", 1)
    strike_unit = Unit("Strike Squad", commander_alpha, soldiers_alpha )

    red_army = Army("Red Army", [alpha_infantry, bravo_tank, charlie_sniper, strike_unit])

    agent_fox = Agent("J7", 5)

    recon_mission = ReconMission("Recon Alpha", "Enemy Territory", agent_fox, [alpha_infantry, charlie_sniper])
    strike_mission = StrikeMission("Strike Bravo", "Enemy Base", agent_fox, [strike_unit])
    rescue_mission =RescueMission ("Rescue Charlie", "Hostage Camp", agent_fox, [alpha_infantry, bravo_tank])

    mission_manager = MissionManager()
    for m in [recon_mission, strike_mission, rescue_mission]:
        mission_manager.add_mission(m)

    print("\n--- Army Coordinated Attack ---")
    red_army.attack_all("Enemy Stronghold")

    print("\n--- Executing Missions ---")
    mission_manager.briefing_all()
    for mission in mission_manager.missions:
        mission.execute()

    print(f"\nTotal coordinated attacks: {Army.total_attacks}")
    print(f"Total Weapons created: {Weapon.total_weapons}")
