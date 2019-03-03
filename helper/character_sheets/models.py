from django.db import models


class Character(models.Model):
    player_id = models.IntegerField()
    name = models.CharField(max_length=50)

    BARBARIAN = 'BARB'
    BARD = 'BARD'
    CLERIC = 'CLE'
    DRUID = 'DRU'
    FIGHTER = 'FIG'
    MONK = 'MON'
    PALADIN = 'PAL'
    RANGER = 'RNG'
    ROGUE = 'ROG'
    SORCEROR = 'SOR'
    WARLOCK = 'WAR'
    WIZARD = 'WIZ'
    NO_CLASS = 'NA'

    CHARACTER_CLASS_CHOICES = (
        (BARBARIAN, 'Barbarian'),
        (BARD, 'Bard'),
        (CLERIC, 'Cleric'),
        (DRUID, 'Druid'),
        (FIGHTER, 'Fighter'),
        (MONK, 'Monk'),
        (PALADIN, 'Paladin'),
        (RANGER, 'Ranger'),
        (ROGUE, 'Rogue'),
        (SORCEROR, 'Sorceror'),
        (WARLOCK, 'Warlock'),
        (WIZARD, 'Wizard'),
        (NO_CLASS, 'No Class'),
    )

    character_class = models.CharField(max_length=4, choices=CHARACTER_CLASS_CHOICES, default=NO_CLASS)

    def __unicode__(self): # __str__ for Python 3, __unicode__ for Python 2
            return self.name

    def attributes(self):
        return self.name, self.character_id, self.character_class
