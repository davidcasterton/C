#!/usr/bin/python

import csv
import pdb
import os
import math
import sys
import copy
import datetime


debug = False

class Player(object):
    def __init__(self, name, estimated_total_points, tier):
        self.name = name
        self.estimated_total_points = int( estimated_total_points )
        self.estimated_weekly_points = round( estimated_total_points / 16, 1)
        self.tier = tier

        self.position = None
        self.price_estimate = None
        self.price_actual = None
        self.differential = None
        self.top_ten_ave_pts = None

    def __str__(self):
        indent = 20
        string = ""
        string += "name:".ljust(indent) + self.name + "\n"
        if position:
            string += "position:".ljust(indent) + self.position + "\n"
        string += "est total pts:".ljust(indent) + str(self.estimated_total_points) + "\n"
        string += "tier:".ljust(indent) + str(self.tier) + "\n"
        if self.price_estimate:
            string += "price est:".ljust(indent) + str(self.price_estimate) + "\n"
        if self.price_actual:
            string += "price actual:".ljust(indent) + str(self.price_actual) + "\n"
        if self.differential:
            string += "differential:".ljust(indent) + str(self.differential) + "\n"
        if self.top_ten_ave_pts:
            string += "top 10 ave pts:".ljust(indent) + str(self.top_ten_ave_pts) + "\n"

        return string

    def setPriceActual(self, price):
        self.price_actual = price

    def EstimatePrice(self):
        weekly_total_pt_target = 100
        total_draft_budget = 200
        ave_differential = 7.15
        ave_player_pts = weekly_total_pt_target / 9

        self.price_estimate = int(  self.estimated_weekly_points * (total_draft_budget / weekly_total_pt_target) * (self.differential / ave_differential) * (self.top_ten_ave_pts / ave_player_pts)  )

class QB(Player):
    def __init__(self, name, estimated_total_points, tier):
        Player.__init__(self, name, estimated_total_points, tier)
        self.position = 'QB'
        self.differential = 4.89125
        self.top_ten_ave_pts = 18.76
        self.EstimatePrice()

class RB(Player):
    def __init__(self, name, estimated_total_points, tier):
        Player.__init__(self, name, estimated_total_points, tier)
        self.position = 'RB'
        #self.differential = 16.2875
        self.differential = 10
        self.top_ten_ave_pts = 13.97
        self.EstimatePrice()

class WR(Player):
    def __init__(self, name, estimated_total_points, tier):
        Player.__init__(self, name, estimated_total_points, tier)
        self.position = 'WR'
        #self.differential = 9.2625
        self.differential = 10
        self.top_ten_ave_pts = 11.78
        self.EstimatePrice()

class TE(Player):
    def __init__(self, name, estimated_total_points, tier):
        Player.__init__(self, name, estimated_total_points, tier)
        self.position = 'TE'
        self.differential = 8.6875
        self.top_ten_ave_pts = 7.25
        self.EstimatePrice()

class K(Player):
    def __init__(self, name, estimated_total_points, tier):
        Player.__init__(self, name, estimated_total_points, tier)
        self.position = 'K'
        self.differential = 2.25
        self.top_ten_ave_pts = 9.3
        self.EstimatePrice()

class TM(Player):
    def __init__(self, name, estimated_total_points, tier):
        Player.__init__(self, name, estimated_total_points, tier)
        self.position = 'TM'
        self.differential = 10.625
        self.top_ten_ave_pts = 9.66
        self.EstimatePrice()




class Roster(object):
    def __init__(self):
        self.roster = {}
        self.slots_filled = {
            'QB' : 0,
            'RB' : 0,
            'WR' : 0,
            'TE' : 0,
            'flex' : 0,
        }
        self.slots_total = {
            'QB' : 1,
            'RB' : 2,
            'WR' : 2,
            'TE' : 1,
            'flex' :1,
        }
        self.estimated_total_points = 0
        self.estimated_weekly_points = 0
        self.price_total = 0
        self.price_total_max = 165

    def __str__(self):
        return str(self.roster)

    def AddPlayer(self, player):
        #check if position available on roster
        if player.name in self.roster.keys():
            #player already on roster
            roster_position_available = None
        elif self.slots_filled[player.position] >= self.slots_total[player.position]:
            #position's slots full
            if (((player.position == 'WR') or (player.position == 'RB')) and (self.slots_filled['flex']==0)):
                #add as flex
                roster_position_available = 'flex'
            else:
                #cannot add as flex
                roster_position_available = None
        else:
            #add player in their position
            roster_position_available = player.position

        #check if can afford player
        player_affordable = self.price_total + player.price_estimate < self.price_total_max

        if roster_position_available and player_affordable:
            if debug:
                print "adding %s for %s, current salary %s"%(player.name, player.price_estimate, self.price_total)
            #add player to roster
            self.roster[player.name] = player
            self.slots_filled[roster_position_available] += 1
            self.estimated_total_points = round( self.estimated_total_points + player.estimated_total_points, 1)
            self.estimated_weekly_points = round( self.estimated_weekly_points + player.estimated_weekly_points, 1 )
            self.price_total += player.price_estimate
            result = True
        else:
            if debug:
                print "NOT adding %s for %s, current salary %s"%(player.name, player.price_estimate, self.price_total)
            result = False
        return result

    def RosterFull(self):
        return self.slots_filled == self.slots_total

    def PositionFull(self, position):
        #print self.slots_filled
        return self.slots_filled[position] == self.slots_total[position]

def ParseCsv(path):
    #init
    players = {}
    position = path.split('.')[0]

    #check file exists
    if not os.path.exists(path):
        return players

    #process file
    with open(path) as f:
        print "processing: %s"%path
        reader = csv.reader(f)
        row_num = 0
        for row in reader:
            if row_num == 0:
                idx_name = row.index('Player')
                idx_estimated_total_points = row.index('62S')
                idx_tier = row.index('Tier')
            else:
                name = row[idx_name]
                estimated_total_points = row[idx_estimated_total_points]
                tier = row[idx_tier]
                players[name] = eval( "%s(\"%s\", %s, %s)"%(position, name, estimated_total_points, tier) )
            row_num += 1

    return players


"""
def GenerateRosters2(players_by_position, rosters, roster):
    sys.setrecursionlimit(10000)

    if roster.RosterFull():
        #if roster is full, return
        return rosters

    players_by_position2 = copy.deepcopy( players_by_position )
    positions = players_by_position.keys()
    for position in positions:
        if roster.PositionFull(position):
            del players_by_position2[position]
            continue
        for player_name, player in players_by_position[position].iteritems():
            del players_by_position2[position][player_name]
            roster2 = copy.deepcopy( roster )

            #generate all rosters without current player
            rosters.update(  GenerateRosters(players_by_position2, rosters, roster2)  )

            #attempt to generate roster with current player
            if roster2.AddPlayer(player):
                print player.name + " added to roster: " + str(roster2)
                if roster2.RosterFull():
                    return rosters.update( { roster2 : roster2.estimated_weekly_points } )
                else:
                    rosters.update(  GenerateRosters(players_by_position2, rosters, roster2)  )

    return rosters
"""

def GenerateRosters(players_by_position, roster_weekly_floor):
    rosters = {}
    qb_list = players_by_position['QB'].values()
    rb_list = players_by_position['RB'].values()
    wr_list = players_by_position['WR'].values()
    te_list = players_by_position['TE'].values()

    for qb in qb_list:
        print qb.name
        for i in range( len(rb_list) ):
            rb1 = rb_list[i]
            for k in range(i+1, len(rb_list) ):
                rb2 = rb_list[k]
                for l in range( len(wr_list) ):
                    wr1 = wr_list[l]
                    for m in range(l+1, len(wr_list) ):
                        wr2 = wr_list[m]
                        flex_list = rb_list[k+1:] + wr_list[m+1:]
                        for te in te_list:
                            for flex in flex_list:
                                if debug:
                                    print "\n"
                                roster = Roster()
                                roster.AddPlayer(qb)
                                roster.AddPlayer(rb1)
                                roster.AddPlayer(rb2)
                                roster.AddPlayer(wr1)
                                roster.AddPlayer(wr2)
                                roster.AddPlayer(te)
                                roster.AddPlayer(flex)
                                #print "%s %s %s %s"%(i,k,l,m)
                                #print qb.name, rb1.name, rb2.name, wr1.name, wr2.name, te.name, flex.name
                                if not roster.RosterFull():
                                    if debug:
                                        print "rejected, not full: " + str(roster.estimated_weekly_points) + "\t" + str(roster.roster)
                                    del roster
                                elif roster.estimated_weekly_points < roster_weekly_floor:
                                    if debug:
                                        print "rejected, below point floor: " + str(roster.estimated_weekly_points) + "\t" + str(roster.roster)
                                    del roster
                                else:
                                    print "ADDED: " + str(roster.estimated_weekly_points) + "\t" + str(roster.roster)
                                    rosters[roster] = roster.estimated_weekly_points
    return rosters

def PrunePlayers(players_by_position, roster_weekly_floor, player_price_ceiling):
    print """# players before prune: %s
    #QB: %s
    #RB: %s
    #WR: %s
    #TE: %s"""%( len(players_by_position['QB'].keys() + players_by_position['RB'].keys() + players_by_position['WR'].keys() + players_by_position['TE'].keys()),
                 len(players_by_position['QB'].keys()), len(players_by_position['RB'].keys()), len(players_by_position['WR'].keys()), len(players_by_position['TE'].keys()) )

    weekly_max = {}
    for position in ['QB','RB','WR','TE']:
        weekly_max[position] = 0
        for player in players_by_position[position].values():
            if player.estimated_weekly_points > weekly_max[position]:
                weekly_max[position] = player.estimated_weekly_points
    for position in ['QB','RB','WR','TE']:
        if position == 'QB':
            other_position_max = weekly_max['RB']*2 + weekly_max['WR']*2 + max([weekly_max['RB'], weekly_max['WR']]) + weekly_max['TE']
        elif position == 'RB':
            other_position_max = weekly_max['QB'] + weekly_max['RB'] + weekly_max['WR']*2 + max([weekly_max['RB'], weekly_max['WR']]) + weekly_max['TE']
        elif position == 'WR':
            other_position_max = weekly_max['QB'] + weekly_max['RB']*2 + weekly_max['WR'] + max([weekly_max['RB'], weekly_max['WR']]) + weekly_max['TE']
        elif position == 'TE':
            other_position_max = weekly_max['QB'] + weekly_max['RB']*2 + weekly_max['WR']*2 + max([weekly_max['RB'], weekly_max['WR']])

        for player in players_by_position[position].values():
            if player.estimated_weekly_points + other_position_max < roster_weekly_floor:
                print "%s cannot make roster weekly total floor: %s"%(player.name, player.estimated_weekly_points)
                del players_by_position[position][player.name]
            if player.price_estimate > player_price_ceiling:
                print "%s above price ceiling: %s > %s "%(player.name, player.price_estimate, player_price_ceiling)
                del players_by_position[position][player.name]

    print """# players after prune: %s
    #QB: %s
    #RB: %s
    #WR: %s
    #TE: %s"""%( len(players_by_position['QB'].keys() + players_by_position['RB'].keys() + players_by_position['WR'].keys() + players_by_position['TE'].keys()),
                 len(players_by_position['QB'].keys()), len(players_by_position['RB'].keys()), len(players_by_position['WR'].keys()), len(players_by_position['TE'].keys()) )

    return players_by_position

def PrintPlayers(players):
    for player_name, player in players.iteritems():
        print player.position.ljust(5) + player_name.ljust(30) + (str(player.estimated_weekly_points) + " pts").ljust(12) + "$" + str(player.price_estimate)

if __name__ == "__main__":
    players = {}
    roster_weekly_floor = 95
    player_price_ceiling = 55
    players_by_position = {}
    for position in ['QB','RB','WR','TE']:
        players_by_position[position] = ParseCsv(position+'.csv')
        players.update( players_by_position[position] )

    players_by_position = PrunePlayers(players_by_position, roster_weekly_floor, player_price_ceiling)

    start = datetime.datetime.now()
    rosters = GenerateRosters(players_by_position, roster_weekly_floor)
    time_delta = datetime.datetime.now() - start
    if type(time_delta.min) == int:
        print "%s mins %s secs"%(time_delta.min, time_delta.seconds)
    else:
        print "%s secs"%(time_delta.seconds)

    pdb.set_trace()