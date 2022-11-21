# https://classic.warcraftlogs.com/v1/docs

import requests

api_url = 'https://classic.warcraftlogs.com:443/v1/'
client_key = '?api_key=bc47c55038353c9ea9a5f32148822099'


def zone_request():
    return requests.get(api_url + 'zones' + client_key)


def class_request():
    return requests.get(api_url + 'classes' + client_key)


def encounter_ranking_request(encounter_id):
    return requests.get(api_url + 'rankings/encounter/' + encounter_id + client_key)
    # page, hasMorePages, count, rankings[name, class, spec, total, duration, startTime, fightID, reportID, guildName,
    # serverName, regionName, hidden, itemLevel, faction, size


def character_ranking_request(character_name):
    return requests.get(api_url + 'rankings/character/' + character_name + '/Eranikus/US' + client_key)
    # encounterID, encounterName, class, spec, rank, outOf, duration, startTime, reportID, fightID, difficulty, size,
    # characterID, characterName, server, percentile, ilvlKeyOrPatch, total, estimated


def parse_request(character_name):
    return requests.get(api_url + 'parses/character/' + character_name + '/Eranikus/US' + client_key)
    # encounterID, encounterName, class, spec, rank, outOf, duration, startTime, reportID, fightID, difficulty, size,
    # characterID, characterName, server, percentile, ilvlKeyOrPatch, total, estimated


def guild_report_reuqest(guild_name):
    return requests.get(api_url + 'reports/guild/' + guild_name + '/Eranikus/US' + client_key)
    # id, title, owner, start, end, zone


def fight_request(code):
    return requests.get(api_url + 'report/fights/' + code + client_key)
    # lang, fights[{id, boss, start_time, end_time, name, zoneID, zoneName, zoneDifficulty, size, difficulty, kill,...}]


def events_request(view, code, params):
    url = api_url + 'report/events/' + view + '/' + code
    for param in params:
        url += param
    url += client_key
    return requests.get(url)
    # views:    summary, damage-done, damage-taken, healing, casts, summons, debuffs,
    #           deaths, threat, resources, interrupts, dispels
    # params:   start, end, hostility, sourceid, sourceinstance, sourceclass, targetid, targetinstance, targetclass,
    #           sourceAurasPresent, sourceAurasAbsent, targetAurasPresent, targetAurasAbsent, abilityid, death, options,
    #           cutoff, encounter, wipes, difficulty, filter


def table_request(view, code, params):
    url = api_url + 'report/tables/' + view + '/' + code
    for param in params:
        url += param
    url += client_key
    return requests.get(url)
    # views:    healing, casts, summons, buffs, debuffs, deaths, survivability, resources, resources-gains
    # params:   start, end, hostility, sourceid, sourceinstance, sourceclass, targetid, targetinstance, targetclass,
    #           sourceAurasPresent, sourceAurasAbsent, targetAurasPresent, targetAurasAbsent, abilityid, death, options,
    #           cutoff, encounter, wipes, difficulty, filter


