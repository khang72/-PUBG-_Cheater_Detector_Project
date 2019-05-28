from pubg_python import PUBG, Shard
from chicken_dinner.pubgapi import PUBGCore
import math

apikey = open("PUBGAPIKEY.txt").read().strip()  #Authentication of API KEY
api = PUBG(apikey, Shard.PC_NA)

#Get a sample of matches played starting from 2019 May 23rd, at 12am
sample = api.samples().filter(created_at_start='2019-05-23T00:00:00Z').get()

Match = []
for match in sample.matches:
    Match.append(match)

runtime = 0
runtime1 = 0
while runtime < 100: #Number of matches will be tested
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

    def ExpectedValue(List,Range): #Calculate Average number
        avg = 0
        for i in range(Range):
            avg += List[i]
        return avg/i

    z = 0
    runtime1 += 1
    a = Match[runtime1]
    for iii in range(1):
        match = api.matches().get(a)
        if match.game_mode == 'squad' or match.game_mode == 'squad-fpp': #Fetching Data for Squad games
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
                    except IndexError: #Some cases where the match has less than 100 players needs to be raised error when out of index
                        pass
        elif match.game_mode == 'duo' or match.game_mode == 'duo-fpp': #Fetching Data for Duo games
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
                    except IndexError:#Some cases where the match has less than 100 players needs to be raised error when out of index
                        pass
        elif match.game_mode == 'solo' or match.game_mode == 'solo-fpp': #Fetching Data for Solo games
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
                    except IndexError:#Some cases where the match has less than 100 players needs to be raised error when out of index
                        pass
            
    for a in Damage:
        try:
            X1.append(a/ExpectedValue(Damage,len(Damage)))
        except ZeroDivisionError: #Raise error when ExpectedValue is 0
            X1.append(1)
    for a in Head:
        try:
            X2.append(a/ExpectedValue(Head,len(Head)))
        except ZeroDivisionError: #Raise error when ExpectedValue is 0
            X2.append(1)
    for a in Kill:
        try:
            X3.append(a/ExpectedValue(Kill,len(Kill)))
        except ZeroDivisionError: #Raise error when ExpectedValue is 0
            X3.append(1)
    for a in Long:
        try:
            X4.append(a/ExpectedValue(Long,len(Long)))
        except ZeroDivisionError: #Raise error when ExpectedValue is 0
            X4.append(1)
    for a in TimeS:
        try:
            X5.append(a/ExpectedValue(TimeS,len(TimeS)))
        except ZeroDivisionError: #Raise error when ExpectedValue is 0
            X5.append(1)
    #print(api.players_from_names(Name[0]).get_current_season().game_mode_stats("squad","fpp"))  
    
    for i in range(100):
        try:
            BBT = (X1[i] + X2[i]*20 + X3[i]*10 + X4[i]*5 + X5[i])/37
            X.append(BBT)
            XX.append(BBT*BBT)
        except IndexError:
            pass
    Exp = 0;
    if z > 40:
        print(runtime, z)
        SampleMean = ExpectedValue(X,z) #Calculate Sample mean
        print(SampleMean)
        for i in X:
            Exp += (i - SampleMean)*(i - SampleMean)
        Devi = math.sqrt(ExpectedValue(XX,z) - SampleMean*SampleMean) #Calculate Deviation
        print(Devi)
        Exp = - Exp / ( 2 * Devi * Devi)
        print(Exp)
    else:
        runtime -= 1
    runtime += 1
    
    for i in X:
        if i > 1 + 0.1285 * sqrt( 2 * ( -Exp[InDex] * 2 * Devi[InDex] * Devi[InDex] ) / z ):
            print(Name[X.index(i)]) #List of suspicious players name
