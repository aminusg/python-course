teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}
print(teams.get('mets', 'No team found by that name'))
del teams['angels']
removed_team = teams.pop('mets', 'Team not found')

print(teams)
print(removed_team)