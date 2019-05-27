from pubg_python import PUBG, Shard
from chicken_dinner.pubgapi import PUBGCore
import math

apikey = open("PUBGAPIKEY.txt").read().strip()
api = PUBG(apikey, Shard.PC_NA)

sample = api.samples().filter(created_at_start='2019-05-23T00:00:00Z').get()

Match = []
for match in sample.matches:
    Match.append(match)

runtime = 0
runtime1 = 0
while runtime < 100:
    Name = []
    player = []
    X1 = []
    X2 = []
    X3 = []
    X4 = []
    X5 = []
    X = []
    XX = []
    Damage=[]
    Head  =[]
    Long  =[]
    Kill  =[]
    TimeS   =[]

    def ExpectedValue(List,Range):
        avg = 0
        for i in range(Range):
            avg += List[i]
        return avg/i

    z = 0
    runtime1 += 1
    a = Match[runtime1]
    for iii in range(1):
        match = api.matches().get(a)
        if match.game_mode == 'squad' or match.game_mode == 'squad-fpp':
            for i in range(25):
                for j in range(4):
                    try:
                        player.append( match.rosters[i].participants[j] )
                        Name.append( player[z].name )
                        Damage.append(player[z].damage_dealt)
                        Head.append(player[z].headshot_kills)
                        Long.append(player[z].longest_kill)
                        Kill.append(player[z].kills)
                        TimeS.append(player[z].time_survived)
                        z += 1
                    except IndexError:
                        pass
        elif match.game_mode == 'duo' or match.game_mode == 'duo-fpp':
            for i in range(50):
                for j in range(2):
                    try:
                        player.append( match.rosters[i].participants[j] )
                        Name.append( player[z].name )
                        Damage.append(player[z].damage_dealt)
                        Head.append(player[z].headshot_kills)
                        Long.append(player[z].longest_kill)
                        Kill.append(player[z].kills)
                        TimeS.append(player[z].time_survived)
                        z += 1
                    except IndexError:
                        pass
        elif match.game_mode == 'solo' or match.game_mode == 'solo-fpp':
            for i in range(100):
                for j in range(1):
                    try:
                        player.append( match.rosters[i].participants[j] )
                        Name.append( player[z].name )
                        Damage.append(player[z].damage_dealt)
                        Head.append(player[z].headshot_kills)
                        Long.append(player[z].longest_kill)
                        Kill.append(player[z].kills)
                        TimeS.append(player[z].time_survived)
                        z += 1
                    except IndexError:
                        pass
            
    for a in Damage:
        try:
            X1.append(a/ExpectedValue(Damage,len(Damage)))
        except ZeroDivisionError:
            X1.append(1)
    for a in Head:
        try:
            X2.append(a/ExpectedValue(Head,len(Head)))
        except ZeroDivisionError:
            X2.append(1)
    for a in Kill:
        try:
            X3.append(a/ExpectedValue(Kill,len(Kill)))
        except ZeroDivisionError:
            X3.append(1)
    for a in Long:
        try:
            X4.append(a/ExpectedValue(Long,len(Long)))
        except ZeroDivisionError:
            X4.append(1)
    for a in TimeS:
        try:
            X5.append(a/ExpectedValue(TimeS,len(TimeS)))
        except ZeroDivisionError:
            X5.append(1)
    #print(api.players_from_names(Name[0]).get_current_season().game_mode_stats("squad","fpp"))  
    #print(Name)
    for i in range(100):
        try:
            BBT = (X1[i] + X2[i]*20 + X3[i]*10 + X4[i]*5 + X5[i])/37
            X.append(BBT)
            XX.append(BBT*BBT)
        except IndexError:
            pass
    #print(X)
    #print(XX)
    Exp = 0;
    if z > 40:
        print(runtime,z)
        SampleMean = ExpectedValue(X,z)
        print(SampleMean)
        for i in X:
            Exp += (i - SampleMean)*(i - SampleMean)
        Devi = math.sqrt(ExpectedValue(XX,z) - SampleMean*SampleMean)
        print(Devi)
        Exp = - Exp / ( 2 * Devi * Devi)
        #print(Exp)
    else:
        runtime -= 1
    runtime += 1
