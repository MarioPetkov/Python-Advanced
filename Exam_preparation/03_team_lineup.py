def team_lineup(*players):
    country_counts = {}

    for name, country in players:
        if country not in country_counts:
            country_counts[country] = []
        country_counts[country].append(name)

    result = ''

    sorted_players = sorted(country_counts.items(), key = lambda kvp: (-len(kvp[1]), kvp[0]))
    for country, players in sorted_players:
        result += f'{country}:\n'
        for player_name in players:
            result += f'  -{player_name}\n'
    return result[:-1]
    




print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

