"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.
	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	UNARMED_POWER = 20

	def __init__(self, name, power, min_level):
		self.__name = name
		self.power = power
		self.min_level = min_level



	@property
	def min_level(self):
		return self.min_level

	@min_level.setter
	def min_level(self, value):
		self.min_level = value

	@property
	def power(self):
		return self.power

	@power.setter
	def min_level(self, value):
		self.power = value

	@property
	def name(self):
		return self.__name

	@staticmethod
	def make_unarmed(self):
		return Weapon('unarmed', self.UNARMED_POWER, 1)



class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

	def __init__(self, name, max_hp, attack, defense, level):
		self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level

	def compute_damage(self,defendeur):

		pass



def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	pass


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	pass
