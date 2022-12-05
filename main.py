# https://classic.warcraftlogs.com/v1/docs

import requests
import json

api_url = 'https://classic.warcraftlogs.com:443/v1/'
client_key = '?api_key=bc47c55038353c9ea9a5f32148822099'


def zone_request():
    return requests.get(api_url + 'zones' + client_key).json()
    # params:   none
    # returns:  list[] > dict{id, name, frozen, encounters, brackets, partitions}


def class_request():
    return requests.get(api_url + 'classes' + client_key).json()
    # params:   none
    # returns:  list > dict{id, name, specs[list > dict{id name}]}


def encounter_ranking_request(encounter_id):
    return requests.get(api_url + 'rankings/encounter/' + encounter_id + client_key).json()
    # params:   encounterID, metric, size, difficulty, partition, class, spec, bracket, server, region, page, filter, bool(includeCombtantInfo)
    # returns:  dict {page, hasMorePages, count, rankings{name, class, spec, total, duration, startTime, fightID, reportID, guildName,
    #           serverName, regionName, hidden, itemLevel, faction, size}}


def character_ranking_request(character_name):
    return requests.get(api_url + 'rankings/character/' + character_name + '/Eranikus/US' + client_key).json()
    # params:   characterName
    # returns:  list > dict {encounterID, encounterName, class, spec, rank, outOf, duration, startTime, reportID, fightID, 
    #           difficulty, size, characterID, characterName, server, percentile, ilvlKeyOrPatch, total, estimated}


def parse_request(character_name):
    return requests.get(api_url + 'parses/character/' + character_name + '/Eranikus/US' + client_key).json()
    # params:   characterName
    # returns:  list > dict {encounterID, encounterName, class, spec, rank, outOf, duration, startTime, reportID, fightID, 
    #           difficulty, size, characterID, characterName, server, percentile, ilvlKeyOrPatch, total, estimated}


def guild_report_request(guild_name):
    return requests.get(api_url + 'reports/guild/' + guild_name + '/Eranikus/US' + client_key).json()
    # params:   guildName
    # returns:  id, title, owner, start, end, zone


def fight_request(report_id):
    return requests.get(api_url + 'report/fights/' + report_id + client_key).json()
    # lang, fights[{id, boss, start_time, end_time, name, zoneID, zoneName, zoneDifficulty, size, difficulty, kill,...}]


def events_request(view, report_id, params):
    url = api_url + 'report/events/' + view + '/' + report_id
    for param in params:
        url += param
    url += client_key
    return requests.get(url).json()
    # views:    summary, damage-done, damage-taken, healing, casts, summons, debuffs,
    #           deaths, threat, resources, interrupts, dispels
    # params:   start, end, hostility, sourceid, sourceinstance, sourceclass, targetid, targetinstance, targetclass,
    #           sourceAurasPresent, sourceAurasAbsent, targetAurasPresent, targetAurasAbsent, abilityid, death, options,
    #           cutoff, encounter, wipes, difficulty, filter
    # returns:  dict {timestamp, type, fight, encounterID, name, difficulty, size, sourceID, gear, auras, expansion, faction, 
    #           specID, strength, agility, stamina, intellect, spirit, dodge, parry, block, armor, critMelee, critRanged, 
    #           critSpell, hasteMelee, hasteRanged, hasteSpell, hitMelee, hitRanged, hitSpell, expertise, resilienceCritTaken, 
    #           resilienceDamageTaken, talentTree, talents, pvpTalents, customPowerSet, secondaryCustomPowerSet, tertiaryCustomPowerSet}


# tables
# 
