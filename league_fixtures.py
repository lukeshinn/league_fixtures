class Team:
    def __init__(self, id):
        self.id = id
        self.name = ""
        self.league_points = 0
        self.points_for = 0
        self.points_against = 0

    def report_game_score(self, points_for, points_against):
        self.points_for += points_for
        self.points_against += points_against

    def report_league_points(self, league_points_earned):
        self.league_points += league_points_earned


def create_teams(team_list):
    active_teams = {}
    for team in team_list:
        id = team.strip(":")[0]
        active_teams[id] = Team(id)
        active_teams[id].name = team.split(":")[1]
    return active_teams


def aggregate_points_scored(active_teams, B, C):
    for i, match in enumerate(B):
        home_team = match.split(":")[0]
        away_team = match.split(":")[1]
        home_score = int(C[i].split(":")[0])
        away_score = int(C[i].split(":")[1])
        active_teams[home_team].report_game_score(home_score, away_score)
        active_teams[away_team].report_game_score(away_score, home_score)


def aggregate_league_points(active_teams, B, C):
    for i, match in enumerate(B):
        home_team = match.split(":")[0]
        away_team = match.split(":")[1]
        home_score = int(C[i].split(":")[0])
        away_score = int(C[i].split(":")[1])
        if home_score > away_score:
            active_teams[home_team].report_league_points(4)
        elif home_score == away_score:
            active_teams[home_team].report_league_points(1)
            active_teams[away_team].report_league_points(1)
        else:
            active_teams[away_team].report_league_points(4)


def determine_winners(active_teams):
    first_place = 0
    second_place = 0
    winner = None
    runner_up = None
    for team in active_teams:
        if active_teams[team].league_points > first_place:
            second_place = first_place
            first_place = active_teams[team].league_points
            winner = active_teams[team]
        elif first_place > active_teams[team].league_points > second_place:
            second_place = active_teams[team].league_points
            runner_up = active_teams[team]
        elif first_place == active_teams[team].league_points and runner_up:
            if runner_up.points_for > winner.points_for:
                winner = runner_up
                runner_up = winner
    print([winner.name, runner_up.name])
    return [winner.name, runner_up.name]


def solution(A, B, C):
    active_teams = create_teams(A)
    if len(B) == len(C):
        aggregate_points_scored(active_teams, B, C)
        aggregate_league_points(active_teams, B, C)
        return determine_winners(active_teams)
    else:
        raise Exception("There is not a score recorded for every match")
    # for x in active_teams:
    #     print(active_teams[x].name)
    #     print(active_teams[x].league_points)
    #     print(active_teams[x].points_for)
    #     print(active_teams[x].points_against)


A = ["a:Essendon", "b:East Coast", "c:Swans", "d:Tigers"]
B = ["a:b", "a:c", "a:d", "b:a", "b:c", "b:d", "c:a", "c:b", "c:d", "d:a", "d:b", "d:c"]
C = [
    "37:55",
    "44:50",
    "111:88",
    "102:42",
    "112:81",
    "81:36",
    "72:39",
    "38:64",
    "57:53",
    "46:65",
    "37:73",
    "95:62",
]


solution(A, B, C)
