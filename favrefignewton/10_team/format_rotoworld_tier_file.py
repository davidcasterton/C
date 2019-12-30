#!/usr/bin/python

import os
import csv
import pdb
from BeautifulSoup import BeautifulSoup
import re

def FormatRow(row, tag, espn_auction_values, columns_to_keep, position_top_ten_pts_diff, position_top_ten_pts_avg, position_scaling):
    cells = row.findAll(tag)

    if tag == 'td' and cells:
        if not re.search(r"#([\d]+)", str(cells[0])):
            return None, columns_to_keep

    csv_row = ""
    if columns_to_keep == {}:
        for i in range(len(cells)):
            keywords = ['Rank', 'Overall', 'Tier', 'Player', 'Tm', 'AGE', 'BYE', '62S']
            for keyword in keywords:
                if keyword in cells[i]:
                    if keyword == "Player":
                        player = cells[i]
                    csv_row += re.sub(r"<([\w\s=\"\-\:\#\;\/]+)>", "", str(cells[i])).strip() + ","
                    columns_to_keep[keyword] = i
                    break
        columns_to_keep
    else:
        columns = columns_to_keep.values()
        columns.sort()
        for i in columns:
            if i == columns_to_keep['62S']:
                roto_weekly_points = int(re.sub(r"<([\w\s=\"\-\:\#\;\/]+)>", "", str(cells[i])).strip().split('.')[0])/15
                csv_row += str(roto_weekly_points) + ","
            else:
                csv_row += re.sub(r"<([\w\s=\"\-\:\#\;\/]+)>", "", str(cells[i])).strip() + ","
        try:
            #ESPN points
            player = re.sub(r"<([\w\s=\"\-\:\#\;\/]+)>", "", str( cells[ columns_to_keep['Player'] ])).strip()
            espn_weekly_pts = int(espn_auction_values[player][1])/15
            csv_row += str(espn_weekly_pts) + ","

            #ESPN - roto points
            csv_row += str( espn_weekly_pts - roto_weekly_points  ) + ","

            #roto calculated $
            rank = int( re.sub(r"<([\w\s=\"\-\:\#\;\/]+)>", "", str( cells[ columns_to_keep['Rank'] ])).strip()[1:] )
            tier = int( re.sub(r"<([\w\s=\"\-\:\#\;\/]+)>", "", str( cells[ columns_to_keep['Tier'] ])).strip() )
            roto_price = round(roto_weekly_points*(position_top_ten_pts_diff/7.15)*(position_top_ten_pts_avg/9)-(tier*2)-(rank/2)+10+position_scaling,2)
            if roto_price>=0:
                csv_row += str(roto_price) + ","
            else:
                csv_row += ","

            #ESPN $
            espn_price = int( espn_auction_values[player][0][1:].strip() )
            csv_row += str(espn_price) + ","

            #ESPN - roto $
            if roto_price>=0:
                csv_row += str(espn_price - roto_price) + ","
        except:
            #pdb.set_trace()
            pass

    return csv_row, columns_to_keep



if __name__ == "__main__":
    #init
    position_const = {
        'QB' :[4.89, 18.76, 0],
        'RB' : [16.28, 13.97, 0],
        'WR' : [9.2, 11.78, 10],
        'TE' : [8.68, 7.25, 5],
        'K' : [2.25, 9.3, 0],
    }

    #read ESPN auction values file
    f_espn = open('espn_auction_values.csv')
    data = f_espn.read()
    f_espn.close()

    espn_auction_values = {}
    for row in data.split('\r\n'):
        cells = row.split(',')
        if len(cells) == 3:
            espn_auction_values[cells[0]] = [cells[1], cells[2]]

    tiers_files = []

    for file_name in os.listdir('.'):
        if 'tiers' in file_name:
            tiers_files.append(file_name)

    for file_name in tiers_files:
        #create csv file
        position = file_name.split('_')[1].upper()
        csv_file_name = position + '.csv'
        print file_name + " -> " + csv_file_name
        f_csv = open( csv_file_name, 'w' )

        #read tiers file
        f_xls = open(file_name)
        html = f_xls.read()
        f_xls.close()
        soup = BeautifulSoup(html)
        table = soup.find("table")

        #process tiers file
        rows = table.findAll('tr')
        header_found = False
        columns_to_keep = {}
        for row in rows:
            if row.findAll('td'):
                csv_row, columns_to_keep = FormatRow(row, 'td', espn_auction_values, columns_to_keep, position_const[position][0], position_const[position][1], position_const[position][2])
            elif row.findAll('th'):
                if header_found:
                    continue
                csv_row, columns_to_keep = FormatRow(row, 'th', espn_auction_values, columns_to_keep, position_const[position][0], position_const[position][1], position_const[position][2])
                csv_row += "ESPN points,ESPN - roto pts,rotoCal$,ESPN$,ESPN - roto $"
                header_found =True

            if csv_row and not "www.rotoworld.com" in csv_row.lower():
                f_csv.write(csv_row + '\n')

        f_csv.close()