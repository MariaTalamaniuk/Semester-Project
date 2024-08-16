weapon_euporia = {
    'Attack power': {
        'Physical': 150,
        'Magic': 245,
        'Fire': 0,
        'Lightening': 0,
        'Holy': 75,
        'Critical': 70
    },
    'Damage negation': {
        'Physical': 28.0,
        'Magic': 70.0,
        'Fire': 22.0,
        'Lightening': 27.0,
        'Guard Boost': 48
    },
    'Attributes': {
        'Vigor': 55,
        'Mind': 30,
        'Endurance': 25,
        'Strength': 16,
        'Dexterity': 16,
        'Intelligence': 16,
        'Faith': 70,
        'Arcane': 0.9
    },
}

weapon_dark_moon_greatsword = {
    'Attack power': {
        'Physical': 200,
        'Magic': 240,
        'Fire': 0,
        'Lightening': 0,
        'Holy': 0,
        'Critical': 100
    },
    'Damage negation': {
        'Physical': 57.0,
        'Magic': 63.0,
        'Fire': 31.0,
        'Lightening': 31.0,
        'Guard Boost': 48
    },
    'Attributes': {
        'Vigor': 50,
        'Mind': 35,
        'Endurance': 13,
        'Strength': 16,
        'Dexterity': 12,
        'Intelligence': 80,
        'Faith': 14,
        'Arcane': 9
    }
}

weapon_reduvia = {
    'Attack power': {
        'Physical': 180,
        'Magic': 310,
        'Fire': 70,
        'Lightening': 0,
        'Holy': 0,
        'Critical': 200
    },
    'Damage negation': {
        'Physical': 39.0,
        'Magic': 77.0,
        'Fire': 30.0,
        'Lightening': 28.0,
        'Guard Boost': 32
    },
    'Attributes': {
        'Vigor': 50,
        'Mind': 22,
        'Endurance': 30,
        'Strength': 0.8,
        'Dexterity': 25,
        'Intelligence': 16,
        'Faith': 0.7,
        'Arcane': 80
    }
}

weapon_twinblade = {
    'Attack power': {
        'Physical': 210,
        'Magic': 175,
        'Fire': 0,
        'Lightening': 75,
        'Holy': 0,
        'Critical': 75
    },
    'Damage negation': {
        'Physical': 43.0,
        'Magic': 65.0,
        'Fire': 20.0,
        'Lightening': 80.0,
        'Guard Boost': 44
    },
    'Attributes': {
        'Vigor': 50,
        'Mind': 30,
        'Endurance': 30,
        'Strength': 35,
        'Dexterity': 34,
        'Intelligence': 17,
        'Faith': 25,
        'Arcane': 0.9
    },
}

weapon_death_poker = {
    'Attack power': {
        'Physical': 170,
        'Magic': 220,
        'Fire': 40,
        'Lightening': 0,
        'Holy': 0,
        'Critical': 75
    },
    'Damage negation': {
        'Physical': 81.0,
        'Magic': 47.0,
        'Fire': 66.0,
        'Lightening': 33.0,
        'Guard Boost': 60
    },
    'Attributes': {
        'Vigor': 50,
        'Mind': 31,
        'Endurance': 32,
        'Strength': 35,
        'Dexterity': 45,
        'Intelligence': 20,
        'Faith': 7,
        'Arcane': 9
    },
}

weapons = [weapon_euporia, weapon_dark_moon_greatsword, weapon_reduvia, weapon_twinblade, weapon_death_poker]

def show_weapon_stats(name):
    name = name.lower()
    for weapon in weapons:
        if
