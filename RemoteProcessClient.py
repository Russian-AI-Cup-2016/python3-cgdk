import _socket
import struct

from model.Bonus import Bonus
from model.BonusType import BonusType
from model.Building import Building
from model.BuildingType import BuildingType
from model.Faction import Faction
from model.Game import Game
from model.LaneType import LaneType
from model.Message import Message
from model.Minion import Minion
from model.MinionType import MinionType
from model.Player import Player
from model.PlayerContext import PlayerContext
from model.Projectile import Projectile
from model.ProjectileType import ProjectileType
from model.SkillType import SkillType
from model.Status import Status
from model.StatusType import StatusType
from model.Tree import Tree
from model.Wizard import Wizard
from model.World import World


class RemoteProcessClient:
    LITTLE_ENDIAN_BYTE_ORDER = True

    BYTE_ORDER_FORMAT_STRING = "<" if LITTLE_ENDIAN_BYTE_ORDER else ">"

    BYTE_FORMAT_STRING = BYTE_ORDER_FORMAT_STRING + "b"
    INT_FORMAT_STRING = BYTE_ORDER_FORMAT_STRING + "i"
    LONG_FORMAT_STRING = BYTE_ORDER_FORMAT_STRING + "q"
    DOUBLE_FORMAT_STRING = BYTE_ORDER_FORMAT_STRING + "d"

    SIGNED_BYTE_SIZE_BYTES = 1
    INTEGER_SIZE_BYTES = 4
    LONG_SIZE_BYTES = 8
    DOUBLE_SIZE_BYTES = 8

    def __init__(self, host, port):
        self.socket = _socket.socket()
        self.socket.setsockopt(_socket.IPPROTO_TCP, _socket.TCP_NODELAY, True)
        self.socket.connect((host, port))
        self.trees = None

    def write_token_message(self, token):
        self.write_enum(RemoteProcessClient.MessageType.AUTHENTICATION_TOKEN)
        self.write_string(token)

    def write_protocol_version_message(self):
        self.write_enum(RemoteProcessClient.MessageType.PROTOCOL_VERSION)
        self.write_int(1)

    def read_team_size_message(self):
        message_type = self.read_enum(RemoteProcessClient.MessageType)
        self.ensure_message_type(message_type, RemoteProcessClient.MessageType.TEAM_SIZE)
        return self.read_int()

    def read_game_context_message(self):
        message_type = self.read_enum(RemoteProcessClient.MessageType)
        self.ensure_message_type(message_type, RemoteProcessClient.MessageType.GAME_CONTEXT)
        return self.read_game()

    def read_player_context_message(self):
        message_type = self.read_enum(RemoteProcessClient.MessageType)
        if message_type == RemoteProcessClient.MessageType.GAME_OVER:
            return None

        self.ensure_message_type(message_type, RemoteProcessClient.MessageType.PLAYER_CONTEXT)
        return self.read_player_context()

    def write_moves_message(self, moves):
        self.write_enum(RemoteProcessClient.MessageType.MOVE)
        self.write_moves(moves)

    def close(self):
        self.socket.close()

    def read_bonus(self):
        if not self.read_boolean():
            return None

        return Bonus(
            self.read_long(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_enum(Faction), self.read_double(), self.read_enum(BonusType)
        )

    def write_bonus(self, bonus):
        if bonus is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_long(bonus.id)
            self.write_double(bonus.x)
            self.write_double(bonus.y)
            self.write_double(bonus.speed_x)
            self.write_double(bonus.speed_y)
            self.write_double(bonus.angle)
            self.write_enum(bonus.faction)
            self.write_double(bonus.radius)
            self.write_enum(bonus.type)

    def read_bonuses(self):
        bonus_count = self.read_int()
        if bonus_count < 0:
            return None

        bonuses = []

        for _ in range(bonus_count):
            bonuses.append(self.read_bonus())

        return bonuses

    def write_bonuses(self, bonuses):
        if bonuses is None:
            self.write_int(-1)
        else:
            self.write_int(bonuses.__len__())

            for bonus in bonuses:
                self.write_bonus(bonus)

    def read_building(self):
        if not self.read_boolean():
            return None

        return Building(
            self.read_long(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_enum(Faction), self.read_double(), self.read_int(), self.read_int(),
            self.read_statuses(), self.read_enum(BuildingType), self.read_double(), self.read_double(), self.read_int(),
            self.read_int(), self.read_int()
        )

    def write_building(self, building):
        if building is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_long(building.id)
            self.write_double(building.x)
            self.write_double(building.y)
            self.write_double(building.speed_x)
            self.write_double(building.speed_y)
            self.write_double(building.angle)
            self.write_enum(building.faction)
            self.write_double(building.radius)
            self.write_int(building.life)
            self.write_int(building.max_life)
            self.write_statuses(building.statuses)
            self.write_enum(building.type)
            self.write_double(building.vision_range)
            self.write_double(building.attack_range)
            self.write_int(building.damage)
            self.write_int(building.cooldown_ticks)
            self.write_int(building.remaining_action_cooldown_ticks)

    def read_buildings(self):
        building_count = self.read_int()
        if building_count < 0:
            return None

        buildings = []

        for _ in range(building_count):
            buildings.append(self.read_building())

        return buildings

    def write_buildings(self, buildings):
        if buildings is None:
            self.write_int(-1)
        else:
            self.write_int(buildings.__len__())

            for building in buildings:
                self.write_building(building)

    def read_game(self):
        if not self.read_boolean():
            return None

        return Game(
            self.read_long(), self.read_int(), self.read_double(), self.read_boolean(), self.read_boolean(),
            self.read_double(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_double(), self.read_double(), self.read_int(), self.read_double(),
            self.read_int(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_double(), self.read_double(), self.read_int(), self.read_int(),
            self.read_int(), self.read_int(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_double(), self.read_int(), self.read_int(), self.read_int(), self.read_int(),
            self.read_int(), self.read_int(), self.read_int(), self.read_int(), self.read_int(), self.read_int(),
            self.read_int(), self.read_int(), self.read_int(), self.read_int(), self.read_int(), self.read_double(),
            self.read_double(), self.read_ints(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_int(), self.read_int(), self.read_int(), self.read_int(), self.read_double(),
            self.read_double(), self.read_int(), self.read_double(), self.read_double(), self.read_double(),
            self.read_int(), self.read_int(), self.read_double(), self.read_double(), self.read_int(),
            self.read_double(), self.read_double(), self.read_int(), self.read_double(), self.read_double(),
            self.read_int(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_int(), self.read_int(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_int(), self.read_int(), self.read_double(), self.read_double(),
            self.read_double(), self.read_double(), self.read_int(), self.read_int(), self.read_int(), self.read_int(),
            self.read_int(), self.read_double(), self.read_int(), self.read_int(), self.read_double(),
            self.read_double(), self.read_double(), self.read_int(), self.read_double(), self.read_double(),
            self.read_double(), self.read_double(), self.read_int(), self.read_int(), self.read_double(),
            self.read_int()
        )

    def write_game(self, game):
        if game is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_long(game.random_seed)
            self.write_int(game.tick_count)
            self.write_double(game.map_size)
            self.write_boolean(game.skills_enabled)
            self.write_boolean(game.raw_messages_enabled)
            self.write_double(game.friendly_fire_damage_factor)
            self.write_double(game.building_damage_score_factor)
            self.write_double(game.building_elimination_score_factor)
            self.write_double(game.minion_damage_score_factor)
            self.write_double(game.minion_elimination_score_factor)
            self.write_double(game.wizard_damage_score_factor)
            self.write_double(game.wizard_elimination_score_factor)
            self.write_double(game.team_working_score_factor)
            self.write_int(game.victory_score)
            self.write_double(game.score_gain_range)
            self.write_int(game.raw_message_max_length)
            self.write_double(game.raw_message_transmission_speed)
            self.write_double(game.wizard_radius)
            self.write_double(game.wizard_cast_range)
            self.write_double(game.wizard_vision_range)
            self.write_double(game.wizard_forward_speed)
            self.write_double(game.wizard_backward_speed)
            self.write_double(game.wizard_strafe_speed)
            self.write_int(game.wizard_base_life)
            self.write_int(game.wizard_life_growth_per_level)
            self.write_int(game.wizard_base_mana)
            self.write_int(game.wizard_mana_growth_per_level)
            self.write_double(game.wizard_base_life_regeneration)
            self.write_double(game.wizard_life_regeneration_growth_per_level)
            self.write_double(game.wizard_base_mana_regeneration)
            self.write_double(game.wizard_mana_regeneration_growth_per_level)
            self.write_double(game.wizard_max_turn_angle)
            self.write_int(game.wizard_max_resurrection_delay_ticks)
            self.write_int(game.wizard_min_resurrection_delay_ticks)
            self.write_int(game.wizard_action_cooldown_ticks)
            self.write_int(game.staff_cooldown_ticks)
            self.write_int(game.magic_missile_cooldown_ticks)
            self.write_int(game.frost_bolt_cooldown_ticks)
            self.write_int(game.fireball_cooldown_ticks)
            self.write_int(game.haste_cooldown_ticks)
            self.write_int(game.shield_cooldown_ticks)
            self.write_int(game.magic_missile_manacost)
            self.write_int(game.frost_bolt_manacost)
            self.write_int(game.fireball_manacost)
            self.write_int(game.haste_manacost)
            self.write_int(game.shield_manacost)
            self.write_int(game.staff_damage)
            self.write_double(game.staff_sector)
            self.write_double(game.staff_range)
            self.write_ints(game.level_up_xp_values)
            self.write_double(game.minion_radius)
            self.write_double(game.minion_vision_range)
            self.write_double(game.minion_speed)
            self.write_double(game.minion_max_turn_angle)
            self.write_int(game.minion_life)
            self.write_int(game.faction_minion_appearance_interval_ticks)
            self.write_int(game.orc_woodcutter_action_cooldown_ticks)
            self.write_int(game.orc_woodcutter_damage)
            self.write_double(game.orc_woodcutter_attack_sector)
            self.write_double(game.orc_woodcutter_attack_range)
            self.write_int(game.fetish_blowdart_action_cooldown_ticks)
            self.write_double(game.fetish_blowdart_attack_range)
            self.write_double(game.fetish_blowdart_attack_sector)
            self.write_double(game.bonus_radius)
            self.write_int(game.bonus_appearance_interval_ticks)
            self.write_int(game.bonus_score_amount)
            self.write_double(game.dart_radius)
            self.write_double(game.dart_speed)
            self.write_int(game.dart_direct_damage)
            self.write_double(game.magic_missile_radius)
            self.write_double(game.magic_missile_speed)
            self.write_int(game.magic_missile_direct_damage)
            self.write_double(game.frost_bolt_radius)
            self.write_double(game.frost_bolt_speed)
            self.write_int(game.frost_bolt_direct_damage)
            self.write_double(game.fireball_radius)
            self.write_double(game.fireball_speed)
            self.write_double(game.fireball_explosion_max_damage_range)
            self.write_double(game.fireball_explosion_min_damage_range)
            self.write_int(game.fireball_explosion_max_damage)
            self.write_int(game.fireball_explosion_min_damage)
            self.write_double(game.guardian_tower_radius)
            self.write_double(game.guardian_tower_vision_range)
            self.write_double(game.guardian_tower_life)
            self.write_double(game.guardian_tower_attack_range)
            self.write_int(game.guardian_tower_damage)
            self.write_int(game.guardian_tower_cooldown_ticks)
            self.write_double(game.faction_base_radius)
            self.write_double(game.faction_base_vision_range)
            self.write_double(game.faction_base_life)
            self.write_double(game.faction_base_attack_range)
            self.write_int(game.faction_base_damage)
            self.write_int(game.faction_base_cooldown_ticks)
            self.write_int(game.burning_duration_ticks)
            self.write_int(game.burning_summary_damage)
            self.write_int(game.empowered_duration_ticks)
            self.write_double(game.empowered_damage_factor)
            self.write_int(game.frozen_duration_ticks)
            self.write_int(game.hastened_duration_ticks)
            self.write_double(game.hastened_bonus_duration_factor)
            self.write_double(game.hastened_movement_bonus_factor)
            self.write_double(game.hastened_rotation_bonus_factor)
            self.write_int(game.shielded_duration_ticks)
            self.write_double(game.shielded_bonus_duration_factor)
            self.write_double(game.shielded_direct_damage_absorption_factor)
            self.write_double(game.aura_skill_range)
            self.write_double(game.range_bonus_per_skill_level)
            self.write_int(game.magical_damage_bonus_per_skill_level)
            self.write_int(game.staff_damage_bonus_per_skill_level)
            self.write_double(game.movement_bonus_factor_per_skill_level)
            self.write_int(game.magical_damage_absorption_per_skill_level)

    def read_games(self):
        game_count = self.read_int()
        if game_count < 0:
            return None

        games = []

        for _ in range(game_count):
            games.append(self.read_game())

        return games

    def write_games(self, games):
        if games is None:
            self.write_int(-1)
        else:
            self.write_int(games.__len__())

            for game in games:
                self.write_game(game)

    def read_message(self):
        if not self.read_boolean():
            return None

        return Message(self.read_enum(LaneType), self.read_enum(SkillType), self.read_byte_array(False))

    def write_message(self, message):
        if message is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_enum(message.lane)
            self.write_enum(message.skill_to_learn)
            self.write_byte_array(message.raw_message)

    def read_messages(self):
        message_count = self.read_int()
        if message_count < 0:
            return None

        messages = []

        for _ in range(message_count):
            messages.append(self.read_message())

        return messages

    def write_messages(self, messages):
        if messages is None:
            self.write_int(-1)
        else:
            self.write_int(messages.__len__())

            for message in messages:
                self.write_message(message)

    def read_minion(self):
        if not self.read_boolean():
            return None

        return Minion(
            self.read_long(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_enum(Faction), self.read_double(), self.read_int(), self.read_int(),
            self.read_statuses(), self.read_enum(MinionType), self.read_double(), self.read_int(), self.read_int(),
            self.read_int()
        )

    def write_minion(self, minion):
        if minion is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_long(minion.id)
            self.write_double(minion.x)
            self.write_double(minion.y)
            self.write_double(minion.speed_x)
            self.write_double(minion.speed_y)
            self.write_double(minion.angle)
            self.write_enum(minion.faction)
            self.write_double(minion.radius)
            self.write_int(minion.life)
            self.write_int(minion.max_life)
            self.write_statuses(minion.statuses)
            self.write_enum(minion.type)
            self.write_double(minion.vision_range)
            self.write_int(minion.damage)
            self.write_int(minion.cooldown_ticks)
            self.write_int(minion.remaining_action_cooldown_ticks)

    def read_minions(self):
        minion_count = self.read_int()
        if minion_count < 0:
            return None

        minions = []

        for _ in range(minion_count):
            minions.append(self.read_minion())

        return minions

    def write_minions(self, minions):
        if minions is None:
            self.write_int(-1)
        else:
            self.write_int(minions.__len__())

            for minion in minions:
                self.write_minion(minion)

    def write_move(self, move):
        if move is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_double(move.speed)
            self.write_double(move.strafe_speed)
            self.write_double(move.turn)
            self.write_enum(move.action)
            self.write_double(move.cast_angle)
            self.write_double(move.min_cast_distance)
            self.write_double(move.max_cast_distance)
            self.write_long(move.status_target_id)
            self.write_enum(move.skill_to_learn)
            self.write_messages(move.messages)

    def write_moves(self, moves):
        if moves is None:
            self.write_int(-1)
        else:
            self.write_int(moves.__len__())

            for move in moves:
                self.write_move(move)

    def read_player(self):
        if not self.read_boolean():
            return None

        return Player(
            self.read_long(), self.read_boolean(), self.read_string(), self.read_boolean(), self.read_int(),
            self.read_enum(Faction)
        )

    def write_player(self, player):
        if player is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_long(player.id)
            self.write_boolean(player.me)
            self.write_string(player.name)
            self.write_boolean(player.strategy_crashed)
            self.write_int(player.score)
            self.write_enum(player.faction)

    def read_players(self):
        player_count = self.read_int()
        if player_count < 0:
            return None

        players = []

        for _ in range(player_count):
            players.append(self.read_player())

        return players

    def write_players(self, players):
        if players is None:
            self.write_int(-1)
        else:
            self.write_int(players.__len__())

            for player in players:
                self.write_player(player)

    def read_player_context(self):
        if not self.read_boolean():
            return None

        return PlayerContext(self.read_wizards(), self.read_world())

    def write_player_context(self, player_context):
        if player_context is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_wizards(player_context.wizards)
            self.write_world(player_context.world)

    def read_player_contexts(self):
        player_context_count = self.read_int()
        if player_context_count < 0:
            return None

        player_contexts = []

        for _ in range(player_context_count):
            player_contexts.append(self.read_player_context())

        return player_contexts

    def write_player_contexts(self, player_contexts):
        if player_contexts is None:
            self.write_int(-1)
        else:
            self.write_int(player_contexts.__len__())

            for player_context in player_contexts:
                self.write_player_context(player_context)

    def read_projectile(self):
        if not self.read_boolean():
            return None

        return Projectile(
            self.read_long(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_enum(Faction), self.read_double(), self.read_enum(ProjectileType),
            self.read_long(), self.read_long()
        )

    def write_projectile(self, projectile):
        if projectile is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_long(projectile.id)
            self.write_double(projectile.x)
            self.write_double(projectile.y)
            self.write_double(projectile.speed_x)
            self.write_double(projectile.speed_y)
            self.write_double(projectile.angle)
            self.write_enum(projectile.faction)
            self.write_double(projectile.radius)
            self.write_enum(projectile.type)
            self.write_long(projectile.owner_unit_id)
            self.write_long(projectile.owner_player_id)

    def read_projectiles(self):
        projectile_count = self.read_int()
        if projectile_count < 0:
            return None

        projectiles = []

        for _ in range(projectile_count):
            projectiles.append(self.read_projectile())

        return projectiles

    def write_projectiles(self, projectiles):
        if projectiles is None:
            self.write_int(-1)
        else:
            self.write_int(projectiles.__len__())

            for projectile in projectiles:
                self.write_projectile(projectile)

    def read_status(self):
        if not self.read_boolean():
            return None

        return Status(self.read_long(), self.read_enum(StatusType), self.read_long(), self.read_long(), self.read_int())

    def write_status(self, status):
        if status is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_long(status.id)
            self.write_enum(status.type)
            self.write_long(status.wizard_id)
            self.write_long(status.player_id)
            self.write_int(status.remaining_duration_ticks)

    def read_statuses(self):
        status_count = self.read_int()
        if status_count < 0:
            return None

        statuses = []

        for _ in range(status_count):
            statuses.append(self.read_status())

        return statuses

    def write_statuses(self, statuses):
        if statuses is None:
            self.write_int(-1)
        else:
            self.write_int(statuses.__len__())

            for status in statuses:
                self.write_status(status)

    def read_tree(self):
        if not self.read_boolean():
            return None

        return Tree(
            self.read_long(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_enum(Faction), self.read_double(), self.read_int(), self.read_int(),
            self.read_statuses()
        )

    def write_tree(self, tree):
        if tree is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_long(tree.id)
            self.write_double(tree.x)
            self.write_double(tree.y)
            self.write_double(tree.speed_x)
            self.write_double(tree.speed_y)
            self.write_double(tree.angle)
            self.write_enum(tree.faction)
            self.write_double(tree.radius)
            self.write_int(tree.life)
            self.write_int(tree.max_life)
            self.write_statuses(tree.statuses)

    def read_trees(self):
        tree_count = self.read_int()
        if tree_count < 0:
            return self.trees

        trees = []

        for _ in range(tree_count):
            trees.append(self.read_tree())

        self.trees = trees
        return trees

    def write_trees(self, trees):
        if trees is None:
            self.write_int(-1)
        else:
            self.write_int(trees.__len__())

            for tree in trees:
                self.write_tree(tree)

    def read_wizard(self):
        if not self.read_boolean():
            return None

        return Wizard(
            self.read_long(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_enum(Faction), self.read_double(), self.read_int(), self.read_int(),
            self.read_statuses(), self.read_long(), self.read_boolean(), self.read_int(), self.read_int(),
            self.read_double(), self.read_double(), self.read_int(), self.read_int(), self.read_enums(SkillType),
            self.read_int(), self.read_ints(), self.read_boolean(), self.read_messages()
        )

    def write_wizard(self, wizard):
        if wizard is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_long(wizard.id)
            self.write_double(wizard.x)
            self.write_double(wizard.y)
            self.write_double(wizard.speed_x)
            self.write_double(wizard.speed_y)
            self.write_double(wizard.angle)
            self.write_enum(wizard.faction)
            self.write_double(wizard.radius)
            self.write_int(wizard.life)
            self.write_int(wizard.max_life)
            self.write_statuses(wizard.statuses)
            self.write_long(wizard.owner_player_id)
            self.write_boolean(wizard.me)
            self.write_int(wizard.mana)
            self.write_int(wizard.max_mana)
            self.write_double(wizard.vision_range)
            self.write_double(wizard.cast_range)
            self.write_int(wizard.xp)
            self.write_int(wizard.level)
            self.write_enums(wizard.skills)
            self.write_int(wizard.remaining_action_cooldown_ticks)
            self.write_ints(wizard.remaining_cooldown_ticks_by_action)
            self.write_boolean(wizard.master)
            self.write_messages(wizard.messages)

    def read_wizards(self):
        wizard_count = self.read_int()
        if wizard_count < 0:
            return None

        wizards = []

        for _ in range(wizard_count):
            wizards.append(self.read_wizard())

        return wizards

    def write_wizards(self, wizards):
        if wizards is None:
            self.write_int(-1)
        else:
            self.write_int(wizards.__len__())

            for wizard in wizards:
                self.write_wizard(wizard)

    def read_world(self):
        if not self.read_boolean():
            return None

        return World(
            self.read_int(), self.read_int(), self.read_double(), self.read_double(), self.read_players(),
            self.read_wizards(), self.read_minions(), self.read_projectiles(), self.read_bonuses(),
            self.read_buildings(), self.read_trees()
        )

    def write_world(self, world):
        if world is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_int(world.tick_index)
            self.write_int(world.tick_count)
            self.write_double(world.width)
            self.write_double(world.height)
            self.write_players(world.players)
            self.write_wizards(world.wizards)
            self.write_minions(world.minions)
            self.write_projectiles(world.projectiles)
            self.write_bonuses(world.bonuses)
            self.write_buildings(world.buildings)
            self.write_trees(world.trees)

    def read_worlds(self):
        world_count = self.read_int()
        if world_count < 0:
            return None

        worlds = []

        for _ in range(world_count):
            worlds.append(self.read_world())

        return worlds

    def write_worlds(self, worlds):
        if worlds is None:
            self.write_int(-1)
        else:
            self.write_int(worlds.__len__())

            for world in worlds:
                self.write_world(world)

    @staticmethod
    def ensure_message_type(actual_type, expected_type):
        if actual_type != expected_type:
            raise ValueError("Received wrong message [actual=%s, expected=%s]." % (actual_type, expected_type))

    def read_enum(self, enum_class):
        byte_array = self.read_bytes(RemoteProcessClient.SIGNED_BYTE_SIZE_BYTES)
        value = struct.unpack(RemoteProcessClient.BYTE_FORMAT_STRING, byte_array)[0]

        for enum_key, enum_value in enum_class.__dict__.items():
            if not str(enum_key).startswith("__") and value == enum_value:
                return enum_value

        return None

    def read_byte_array(self, nullable):
        count = self.read_int()

        if nullable:
            if count < 0:
                return None
        else:
            if count <= 0:
                return bytes()

        return self.read_bytes(count)

    def write_byte_array(self, array):
        if array is None:
            self.write_int(-1)
        else:
            self.write_int(array.__len__())
            self.write_bytes(array)

    def read_enums(self, enum_class):
        count = self.read_int()
        if count < 0:
            return None

        enums = []

        for _ in range(count):
            enums.append(self.read_enum(enum_class))

        return enums

    def read_enums_2d(self, enum_class):
        count = self.read_int()
        if count < 0:
            return None

        enums_2d = []

        for _ in range(count):
            enums_2d.append(self.read_enums(enum_class))

        return enums_2d

    def write_enum(self, value):
        self.write_bytes(struct.pack(
            RemoteProcessClient.BYTE_FORMAT_STRING, -1 if value is None else value
        ))

    def write_enums(self, enums):
        if enums is None:
            self.write_int(-1)
        else:
            self.write_int(enums.__len__())

            for value in enums:
                self.write_enum(value)

    def write_enums_2d(self, enums_2d):
        if enums_2d is None:
            self.write_int(-1)
        else:
            self.write_int(enums_2d.__len__())

            for enums in enums_2d:
                self.write_enums(enums)

    def read_string(self):
        length = self.read_int()
        if length == -1:
            return None

        byte_array = self.read_bytes(length)
        return byte_array.decode()

    def write_string(self, value):
        if value is None:
            self.write_int(-1)
            return

        byte_array = value.encode()

        self.write_int(len(byte_array))
        self.write_bytes(byte_array)

    def read_boolean(self):
        byte_array = self.read_bytes(RemoteProcessClient.SIGNED_BYTE_SIZE_BYTES)
        return struct.unpack(RemoteProcessClient.BYTE_FORMAT_STRING, byte_array)[0] != 0

    def read_boolean_array(self, count):
        byte_array = self.read_bytes(count * RemoteProcessClient.SIGNED_BYTE_SIZE_BYTES)
        unpacked_bytes = struct.unpack(RemoteProcessClient.BYTE_ORDER_FORMAT_STRING + str(count) + "b", byte_array)

        return [unpacked_bytes[i] != 0 for i in range(count)]

    def write_boolean(self, value):
        self.write_bytes(struct.pack(RemoteProcessClient.BYTE_FORMAT_STRING, 1 if value else 0))

    def read_int(self):
        byte_array = self.read_bytes(RemoteProcessClient.INTEGER_SIZE_BYTES)
        return struct.unpack(RemoteProcessClient.INT_FORMAT_STRING, byte_array)[0]

    def read_ints(self):
        count = self.read_int()
        if count < 0:
            return None

        ints = []

        for _ in range(count):
            ints.append(self.read_int())

        return ints

    def read_ints_2d(self):
        count = self.read_int()
        if count < 0:
            return None

        ints_2d = []

        for _ in range(count):
            ints_2d.append(self.read_ints())

        return ints_2d

    def write_int(self, value):
        self.write_bytes(struct.pack(RemoteProcessClient.INT_FORMAT_STRING, value))

    def write_ints(self, ints):
        if ints is None:
            self.write_int(-1)
        else:
            self.write_int(ints.__len__())

            for value in ints:
                self.write_int(value)

    def write_ints_2d(self, ints_2d):
        if ints_2d is None:
            self.write_int(-1)
        else:
            self.write_int(ints_2d.__len__())

            for ints in ints_2d:
                self.write_ints(ints)

    def read_long(self):
        byte_array = self.read_bytes(RemoteProcessClient.LONG_SIZE_BYTES)
        return struct.unpack(RemoteProcessClient.LONG_FORMAT_STRING, byte_array)[0]

    def write_long(self, value):
        self.write_bytes(struct.pack(RemoteProcessClient.LONG_FORMAT_STRING, value))

    def read_double(self):
        byte_array = self.read_bytes(RemoteProcessClient.DOUBLE_SIZE_BYTES)
        return struct.unpack(RemoteProcessClient.DOUBLE_FORMAT_STRING, byte_array)[0]

    def write_double(self, value):
        self.write_bytes(struct.pack(RemoteProcessClient.DOUBLE_FORMAT_STRING, value))

    def read_bytes(self, byte_count):
        byte_array = bytes()

        while len(byte_array) < byte_count:
            chunk = self.socket.recv(byte_count - len(byte_array))

            if not len(chunk):
                raise IOError("Can't read %s bytes from input stream." % str(byte_count))

            byte_array += chunk

        return byte_array

    def write_bytes(self, byte_array):
        self.socket.sendall(byte_array)

    class MessageType:
        UNKNOWN = 0
        GAME_OVER = 1
        AUTHENTICATION_TOKEN = 2
        TEAM_SIZE = 3
        PROTOCOL_VERSION = 4
        GAME_CONTEXT = 5
        PLAYER_CONTEXT = 6
        MOVE = 7
