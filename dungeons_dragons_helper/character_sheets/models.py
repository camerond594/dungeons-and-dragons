# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class AttributesSavingThrowsMixin(models.Model):

    # Attributes

    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)

    # Saving Throw Proficiencies

    strength_prof = models.BooleanField(default=False)
    dexterity_prof = models.BooleanField(default=False)
    constitution_prof = models.BooleanField(default=False)
    intelligence_prof = models.BooleanField(default=False)
    wisdom_prof = models.BooleanField(default=False)
    charisma_prof = models.BooleanField(default=False)


class BasicFactsMixin(models.Model):

    character_name = models.CharField(max_length=50, null=True)
    character_class = models.CharField(max_length=50, null=True)
    character_level = models.IntegerField(default=1)
    character_race = models.CharField(max_length=50, null=True)
    character_background = models.CharField(max_length=50, null=True)
    character_alignment = models.CharField(max_length=50, null=True)
    character_exp_points = models.IntegerField(default=0)


class SkillsMixin(models.Model):

    acrobatics = models.IntegerField(default=0)
    animal_handling = models.IntegerField(default=0)
    arcana = models.IntegerField(default=0)
    athletics = models.IntegerField(default=0)
    deception = models.IntegerField(default=0)
    history = models.IntegerField(default=0)
    insight = models.IntegerField(default=0)
    intimidation = models.IntegerField(default=0)
    investigation = models.IntegerField(default=0)
    medicine = models.IntegerField(default=0)
    nature = models.IntegerField(default=0)
    perception = models.IntegerField(default=0)
    performance = models.IntegerField(default=0)
    persuasion = models.IntegerField(default=0)
    religion = models.IntegerField(default=0)
    sleight_of_hand = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)


class HitDiceMixin(models.Model):

    HIT_DIE_CHOICES = (
        ('D10', 'd10'),
        ('D8', 'd8'),
        ('D6', 'd6'),
    )

    primary_hit_die = models.CharField(max_length=4, choices=HIT_DIE_CHOICES)
    primary_class_level = models.IntegerField()
    multiclass_hit_die = models.CharField(max_length=4, choices=HIT_DIE_CHOICES)
    multiclass_level = models.IntegerField()


# Possibility for an extension to include Magic?
class WeaponsMixin(models.Model):

    DAMAGE_TYPE_CHOICES = (
        ('AD', 'Acid'),
        ('BLG', 'Bludgeoning'),
        ('CLD', 'Cold'),
        ('FR', 'Fire'),
        ('FOR', 'Force'),
        ('LTG', 'Lightning'),
        ('NTC', 'Necrotic'),
        ('PRC', 'Piercing'),
        ('PSN', 'Poison'),
        ('PSY', 'Psychic'),
        ('RDN', 'Radiant'),
        ('SLH', 'Slashing'),
        ('THU', 'Thunder'),
    )

    HIT_DIE_CHOICES = (
        ('D10', 'd10'),
        ('D8', 'd8'),
        ('D6', 'd6'),
    )

    name = models.CharField(max_length=30)
    attack_bonus = models.IntegerField()
    damage_type = models.CharField(max_length=20)
    hit_die = models.CharField(max_length=4, choices=HIT_DIE_CHOICES)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=False)


class EquipmentMixin(models.Model):

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)


class PlayerDescriptionMixin(models.Model):

    DESCRIPTION_TYPES_CHOICES = (
        ('PERSONALITY_TRAITS', 'Personality Traits'),
        ('IDEALS', 'Ideals'),
        ('FLAWS', 'Flaws'),
        ('BONDS', 'Bonds'),
        ('FEATURES_AND_TRAITS', 'Features and Traits'),
        ('GENERIC_DESCRIPTION', 'Generic Description'),
    )

    description_type = models.CharField(max_length=20, choices=DESCRIPTION_TYPES_CHOICES)
    description = models.CharField(max_length=200)


class CharacterLooksBackstoryMixin(models.Model):

    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    eyes = models.CharField(max_length=10)
    skin = models.CharField(max_length=10)
    hair = models.CharField(max_length=10)
    appearance = models.CharField(max_length=500)

    character_backstory = models.CharField(max_length=1000)


class AlliesOrganizations(models.Model):

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=30)


class LanguageMixin(models.Model):

    language_name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    races_used_by = models.ManyToManyField('Race')


# Needs more work
class Race(models.Model):

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)


class SpellsMixin(models.Model):

    SPELLCASTING_CLASS_CHOICES = (
        ('INT', 'Intelligence'),
        ('CHA', 'Charisma'),
        ('WIS', 'Wisdom'),
        ('CON', 'Constitution'),
    )

    spellcasting_class = models.CharField(max_length=20, choices=SPELLCASTING_CLASS_CHOICES)

    # Ability Modifier for given class
    spellcasting_ability = models.IntegerField()

    # = 8 + Proficiency + Ability Score
    spell_save_dc = models.IntegerField()

    # = Proficiency + Ability Score
    spell_attack_bonus = models.IntegerField()


class Spell(models.Model):

    SPELL_SHAPE_CHOICES = (
        ('TCH', 'Touch'),
        ('CN', 'Cone'),
        ('CB', 'Cube'),
    )

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    spell_level = models.IntegerField(default=0)
    casting_time = models.IntegerField(default=0)
    range = models.IntegerField(default=0)
    shape = models.CharField(max_length=20, choices=SPELL_SHAPE_CHOICES)
    active = models.BooleanField(default=False)


class Character(models.Model):

    active = models.BooleanField(default=True)

    # User for a given Character

    # player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player')
    #
    # # Basic Character Facts
    #
    facts = models.ForeignKey('BasicFactsMixin', on_delete=models.CASCADE, related_name='facts', default=None)
    #
    # # Attributes
    #
    # attributes = models.ForeignKey('AttributesSavingThrowsMixin', on_delete=models.CASCADE, related_name='attributes')
    #
    # inspiration_die = models.IntegerField()
    # prof_bonus = models.IntegerField()
    #
    # # Saving Throws
    #
    # saving_throws = models.ForeignKey('AttributesSavingThrowsMixin', on_delete=models.CASCADE, related_name='saving_throws')
    #
    # # Skills
    #
    # skills = models.ForeignKey('SkillsMixin', on_delete=models.CASCADE, related_name='skills')
    #
    # armor_class = models.IntegerField()
    # initiative = models.IntegerField()
    # speed = models.IntegerField()
    #
    # hit_points_max = models.IntegerField()
    # curr_hit_points = models.IntegerField()
    # temp_hit_points = models.IntegerField()
    #
    # hit_dice = models.ForeignKey('HitDiceMixin', on_delete=models.CASCADE, related_name='hit_dice')
    #
    # death_save_success = models.IntegerField()
    # death_save_failure = models.IntegerField()
    #
    # weapons = models.ManyToManyField('WeaponsMixin', related_name='weapons')
    # spells = models.ManyToManyField('Spell', related_name='spells')
    #
    # spellcasting_skills = models.ForeignKey('SpellsMixin', related_name='spellcasting')
    #
    # equipment = models.ManyToManyField('EquipmentMixin', related_name='equipment')
    #
    # # Player Description Basics
    #
    # personality_traits = models.ManyToManyField('PlayerDescriptionMixin', related_name='personality_traits')
    # ideals = models.ManyToManyField('PlayerDescriptionMixin', related_name='ideals')
    # bonds = models.ManyToManyField('PlayerDescriptionMixin', related_name='bonds')
    # flaws = models.ManyToManyField('PlayerDescriptionMixin', related_name='flaws')
    # features_and_traits = models.ManyToManyField('PlayerDescriptionMixin', related_name='features_and_traits')
    #
    # # Character Looks and Backstory
    #
    # looks_backstory = models.ForeignKey('CharacterLooksBackstoryMixin', related_name='looks_backstory')
    # # character_image = models.ImageField()
    #
    # # Treasure
    #
    # treasure = models.ManyToManyField('PlayerDescriptionMixin', related_name='treasure')

    def __unicode__(self):
        return self.facts.character_name

    def create_character(self):
        self.active = True
        self.save()
        return


class Player(models.Model):
    name = models.CharField(max_length=50, null=True)
    dungeon_master = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


# class DungeonMaster(models.Model):
#     name = models.CharField(max_length=50, null=True)
#
#     def __unicode__(self):
#         return self.name
#
#
# class Campaign(models.Model):
#
#     dm = models.ForeignKey('Player', related_name='dungeon_master')
#     players = models.ManyToManyField('Player')