import random

class Player:
    def __init__(self, name, position, batting_average, pitching_speed, fielding_ability):
        self.name = name
        self.position = position
        self.batting_average = batting_average
        self.pitching_speed = pitching_speed
        self.fielding_ability = fielding_ability

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.wins = 0
        self.losses = 0
        self.score = 0

class Manager:
    def __init__(self, team):
        self.team = team
        self.lineup = []

    def select_lineup(self):
        self.lineup = random.sample(self.team.players, 9)

    def make_substitution(self, player_in, player_out):
        self.lineup.remove(player_out)
        self.lineup.append(player_in)

    def call_pitching_change(self, new_pitcher):
        self.lineup[0] = new_pitcher

    def make_batting_decision(self):
        batter = self.lineup[self.team.score % 9]
        if random.random() < batter.batting_average:
            self.team.score += 1
            print(f"{batter.name} hits a single!")
        else:
            print(f"{batter.name} strikes out.")

class BaseballGame:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.inning = 1
        self.outs = 0
        self.bases = [0, 0, 0]
        self.top_of_inning = True

    def play_ball(self):
        while self.inning <= 9 or (self.inning == 10 and self.home_team.score == self.away_team.score):
            print(f"Top of inning {self.inning}" if self.top_of_inning else f"Bottom of inning {self.inning}")
            manager = self.home_team_manager if self.top_of_inning else self.away_team_manager
            while self.outs < 3:
                manager.make_batting_decision()
                if self.bases[2] == 1:
                    self.home_team.score += 1 if self.top_of_inning else 0
                    self.away_team.score += 1 if not self.top_of_inning else 0
                    self.bases[2] = 0
                for i in range(2, -1, -1):
                    if self.bases[i] == 1:
                        self.bases[i+1] = 1
                        self.bases[i] = 0
                if random.random() < manager.lineup[0].pitching_speed:
                    self.outs += 1
                    print("Strikeout!")
            self.inning += 1
            self.outs = 0
            self.bases = [0, 0, 0]
            self.top_of_inning = not self.top_of_inning
        print(f"Final score: {self.home_team.name} {self.home_team.score}, {self.away_team.name} {self.away_team.score}")

home_team_players = [
    Player("Player 1", "Catcher", 0.3, 0.7, 0.8),
    Player("Player 2", "First Base", 0.2, 0.5, 0.9),
    Player("Player 3", "Second Base", 0.25, 0.6,0.9), 
