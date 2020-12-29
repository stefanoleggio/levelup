
import discord
import core.settings as settings
import json

def get_users_in_voice_channels(voice_channels):
    active_users = []
    for voice_channel in voice_channels:
        for user in voice_channel.members:
            active_users.append(user)
    return active_users

def increment_xp(active_users):
    f = open('AppData/users.json', 'r')
    json_users = json.load(f)
    f.close()
    for user in active_users:
        for json_user in json_users:
            if(user.id == json_user['id']):
                json_user['xp'] = json_user['xp'] + 1
                json_user = check_level(json_user)
                
    f = open('AppData/users.json', 'w')
    f.write(json.dumps(json_users, indent=4))
    f.close()

def check_level(user):
    if(user['xp'] < user['max_xp']):
        return user
    f = open('AppData/levels.json', 'r')
    levels = json.load(f)
    f.close()
    if(user['level'] < len(levels)):
        user['level'] += 1
        for level in levels:
            if(level['id'] == user['level']):
                user['max_xp'] = level['max_xp']
        print("Level Up!!!")
    return user

def core(guild):
    voice_channels = settings.get_xp_channels(guild)
    active_users = get_users_in_voice_channels(voice_channels)
    increment_xp(active_users)