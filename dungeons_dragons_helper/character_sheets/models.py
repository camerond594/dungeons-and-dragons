# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class AttributesSavingThrowsMixin(models.Model):

    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)


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


class WeaponMixin(models.Model):

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

    name = models.CharField(max_length=30)
    attack_bonus = models.IntegerField()
    damage_type = models.CharField()


class Character(models.Model):

    character_id = models.IntegerField()
    active = models.BooleanField(default=True)

    # User for a given Character

    player = models.ForeignKey('Player', on_delete=models.CASCADE)

    # Basic Character Facts

    facts = models.ForeignKey('BasicFactsMixin', on_delete=models.CASCADE)

    # Attributes

    attributes = models.ForeignKey('AttributesSavingThrowsMixin', on_delete=models.CASCADE)

    inspirations_die = models.IntegerField()
    prof_bonus = models.IntegerField()

    # Saving Throws

    saving_throws = models.ForeignKey('AttributesSavingThrowsMixin', on_delete=models.CASCADE)

    # Skills

    skills = models.ForeignKey('SkillsMixin', on_delete=models.CASCADE)

    armor_class = models.IntegerField()
    initiative = models.IntegerField()
    speed = models.IntegerField()

    hit_points_max = models.IntegerField()
    curr_hit_points = models.IntegerField()
    temp_hit_points = models.IntegerField()

    hit_dice = models.ForeignKey('HitDiceMixin', on_delete=models.CASCADE)

    death_save_success = models.IntegerField()
    death_save_failure = models.IntegerField()

    def __unicode__(self):
        return self.character_name


class Player(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.name