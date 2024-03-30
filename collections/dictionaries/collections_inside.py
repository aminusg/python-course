teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

astros = teams['astros']
print(astros)
print(teams['angels'])
print(teams['yankees'])

#How to Add New Key/Value Pairs to Diccionaries
#Se hace prácticamente como si hiciéramos una consulta
teams['red sox'] = ['Price', 'Betts']

print(teams)


#Fallback Lookup Values
featured_team = teams.get('yankees', 'No featured team')

print(featured_team)