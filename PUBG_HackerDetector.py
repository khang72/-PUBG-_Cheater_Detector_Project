from pubg_python import PUBG, Shard
from chicken_dinner.pubgapi import PUBGCore

apikey = open("PUBGAPIKEY.txt").read().strip()
api = PUBG(apikey, Shard.PC_NA)

sample = api.samples().filter(created_at_start='2019-05-25T00:00:00Z').get()

Match = []
i = 0

for match in sample.matches:
    Match.append(match)
    i += 1
    if i == 1:
        break
print(Match)

Name = []
player = []
X1 = []
X2 = []
X3 = []
X4 = []
X = []
Damage=[]
Head  =[]
Long  =[]
Kill  =[]
KDA   =[]

def ExpectedValue(List,Range):
    avg = 0
    for i in range(Range):
        avg += List[i]
    return avg/i

for a in Match:
    match = api.matches().get(a)
    for i in range(4):
        player.append( match.rosters[i].participants[i] )
        Name.append( player[i].name )
        #X.append(player[i].damage_dealt + player[i].headshot_kills + player[i].kills + player[i].longest_kill )
        Damage.append(player[i].damage_dealt)
        Head.append(player[i].headshot_kills)
        Long.append(player[i].longest_kill)
        Kill.append(player[i].kills)
        
for a in Damage:
    X1.append(a/ExpectedValue(Damage,len(Damage)))
for a in Head:
    X2.append(a/ExpectedValue(Head,len(Head)))
for a in Kill:
    X3.append(a/ExpectedValue(Kill,len(Kill)))
for a in Long:
    X4.append(a/ExpectedValue(Long,len(Long)))
#print(api.players_from_names(Name[0]).get_current_season().game_mode_stats("squad","fpp"))  
print(Name)
print(X1)
print(X2)
print(X3)
print(X4)
for i in range(4):
    X.append(X1[i] + X2[i] + X3[i] + X4[i])
print(X)
