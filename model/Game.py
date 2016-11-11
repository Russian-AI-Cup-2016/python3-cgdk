class Game:
    def __init__(self, random_seed, tick_count, map_size, skills_enabled, raw_messages_enabled,
                 friendly_fire_damage_factor, building_damage_score_factor, building_elimination_score_factor,
                 minion_damage_score_factor, minion_elimination_score_factor, wizard_damage_score_factor,
                 wizard_elimination_score_factor, team_working_score_factor, victory_score, score_gain_range,
                 raw_message_max_length, raw_message_transmission_speed, wizard_radius, wizard_cast_range,
                 wizard_vision_range, wizard_forward_speed, wizard_backward_speed, wizard_strafe_speed,
                 wizard_base_life, wizard_life_growth_per_level, wizard_base_mana, wizard_mana_growth_per_level,
                 wizard_base_life_regeneration, wizard_life_regeneration_growth_per_level,
                 wizard_base_mana_regeneration, wizard_mana_regeneration_growth_per_level, wizard_max_turn_angle,
                 wizard_max_resurrection_delay_ticks, wizard_min_resurrection_delay_ticks, wizard_action_cooldown_ticks,
                 staff_cooldown_ticks, magic_missile_cooldown_ticks, frost_bolt_cooldown_ticks, fireball_cooldown_ticks,
                 haste_cooldown_ticks, shield_cooldown_ticks, magic_missile_manacost, frost_bolt_manacost,
                 fireball_manacost, haste_manacost, shield_manacost, staff_damage, staff_sector, staff_range,
                 level_up_xp_values, minion_radius, minion_vision_range, minion_speed, minion_max_turn_angle,
                 minion_life, faction_minion_appearance_interval_ticks, orc_woodcutter_action_cooldown_ticks,
                 orc_woodcutter_damage, orc_woodcutter_attack_sector, orc_woodcutter_attack_range,
                 fetish_blowdart_action_cooldown_ticks, fetish_blowdart_attack_range, fetish_blowdart_attack_sector,
                 bonus_radius, bonus_appearance_interval_ticks, bonus_score_amount, dart_radius, dart_speed,
                 dart_direct_damage, magic_missile_radius, magic_missile_speed, magic_missile_direct_damage,
                 frost_bolt_radius, frost_bolt_speed, frost_bolt_direct_damage, fireball_radius, fireball_speed,
                 fireball_explosion_max_damage_range, fireball_explosion_min_damage_range,
                 fireball_explosion_max_damage, fireball_explosion_min_damage, guardian_tower_radius,
                 guardian_tower_vision_range, guardian_tower_life, guardian_tower_attack_range, guardian_tower_damage,
                 guardian_tower_cooldown_ticks, faction_base_radius, faction_base_vision_range, faction_base_life,
                 faction_base_attack_range, faction_base_damage, faction_base_cooldown_ticks, burning_duration_ticks,
                 burning_summary_damage, empowered_duration_ticks, empowered_damage_factor, frozen_duration_ticks,
                 hastened_duration_ticks, hastened_bonus_duration_factor, hastened_movement_bonus_factor,
                 hastened_rotation_bonus_factor, shielded_duration_ticks, shielded_bonus_duration_factor,
                 shielded_direct_damage_absorption_factor, aura_skill_range, range_bonus_per_skill_level,
                 magical_damage_bonus_per_skill_level, staff_damage_bonus_per_skill_level,
                 movement_bonus_factor_per_skill_level, magical_damage_absorption_per_skill_level):
        self.random_seed = random_seed
        self.tick_count = tick_count
        self.map_size = map_size
        self.skills_enabled = skills_enabled
        self.raw_messages_enabled = raw_messages_enabled
        self.friendly_fire_damage_factor = friendly_fire_damage_factor
        self.building_damage_score_factor = building_damage_score_factor
        self.building_elimination_score_factor = building_elimination_score_factor
        self.minion_damage_score_factor = minion_damage_score_factor
        self.minion_elimination_score_factor = minion_elimination_score_factor
        self.wizard_damage_score_factor = wizard_damage_score_factor
        self.wizard_elimination_score_factor = wizard_elimination_score_factor
        self.team_working_score_factor = team_working_score_factor
        self.victory_score = victory_score
        self.score_gain_range = score_gain_range
        self.raw_message_max_length = raw_message_max_length
        self.raw_message_transmission_speed = raw_message_transmission_speed
        self.wizard_radius = wizard_radius
        self.wizard_cast_range = wizard_cast_range
        self.wizard_vision_range = wizard_vision_range
        self.wizard_forward_speed = wizard_forward_speed
        self.wizard_backward_speed = wizard_backward_speed
        self.wizard_strafe_speed = wizard_strafe_speed
        self.wizard_base_life = wizard_base_life
        self.wizard_life_growth_per_level = wizard_life_growth_per_level
        self.wizard_base_mana = wizard_base_mana
        self.wizard_mana_growth_per_level = wizard_mana_growth_per_level
        self.wizard_base_life_regeneration = wizard_base_life_regeneration
        self.wizard_life_regeneration_growth_per_level = wizard_life_regeneration_growth_per_level
        self.wizard_base_mana_regeneration = wizard_base_mana_regeneration
        self.wizard_mana_regeneration_growth_per_level = wizard_mana_regeneration_growth_per_level
        self.wizard_max_turn_angle = wizard_max_turn_angle
        self.wizard_max_resurrection_delay_ticks = wizard_max_resurrection_delay_ticks
        self.wizard_min_resurrection_delay_ticks = wizard_min_resurrection_delay_ticks
        self.wizard_action_cooldown_ticks = wizard_action_cooldown_ticks
        self.staff_cooldown_ticks = staff_cooldown_ticks
        self.magic_missile_cooldown_ticks = magic_missile_cooldown_ticks
        self.frost_bolt_cooldown_ticks = frost_bolt_cooldown_ticks
        self.fireball_cooldown_ticks = fireball_cooldown_ticks
        self.haste_cooldown_ticks = haste_cooldown_ticks
        self.shield_cooldown_ticks = shield_cooldown_ticks
        self.magic_missile_manacost = magic_missile_manacost
        self.frost_bolt_manacost = frost_bolt_manacost
        self.fireball_manacost = fireball_manacost
        self.haste_manacost = haste_manacost
        self.shield_manacost = shield_manacost
        self.staff_damage = staff_damage
        self.staff_sector = staff_sector
        self.staff_range = staff_range
        self.level_up_xp_values = level_up_xp_values
        self.minion_radius = minion_radius
        self.minion_vision_range = minion_vision_range
        self.minion_speed = minion_speed
        self.minion_max_turn_angle = minion_max_turn_angle
        self.minion_life = minion_life
        self.faction_minion_appearance_interval_ticks = faction_minion_appearance_interval_ticks
        self.orc_woodcutter_action_cooldown_ticks = orc_woodcutter_action_cooldown_ticks
        self.orc_woodcutter_damage = orc_woodcutter_damage
        self.orc_woodcutter_attack_sector = orc_woodcutter_attack_sector
        self.orc_woodcutter_attack_range = orc_woodcutter_attack_range
        self.fetish_blowdart_action_cooldown_ticks = fetish_blowdart_action_cooldown_ticks
        self.fetish_blowdart_attack_range = fetish_blowdart_attack_range
        self.fetish_blowdart_attack_sector = fetish_blowdart_attack_sector
        self.bonus_radius = bonus_radius
        self.bonus_appearance_interval_ticks = bonus_appearance_interval_ticks
        self.bonus_score_amount = bonus_score_amount
        self.dart_radius = dart_radius
        self.dart_speed = dart_speed
        self.dart_direct_damage = dart_direct_damage
        self.magic_missile_radius = magic_missile_radius
        self.magic_missile_speed = magic_missile_speed
        self.magic_missile_direct_damage = magic_missile_direct_damage
        self.frost_bolt_radius = frost_bolt_radius
        self.frost_bolt_speed = frost_bolt_speed
        self.frost_bolt_direct_damage = frost_bolt_direct_damage
        self.fireball_radius = fireball_radius
        self.fireball_speed = fireball_speed
        self.fireball_explosion_max_damage_range = fireball_explosion_max_damage_range
        self.fireball_explosion_min_damage_range = fireball_explosion_min_damage_range
        self.fireball_explosion_max_damage = fireball_explosion_max_damage
        self.fireball_explosion_min_damage = fireball_explosion_min_damage
        self.guardian_tower_radius = guardian_tower_radius
        self.guardian_tower_vision_range = guardian_tower_vision_range
        self.guardian_tower_life = guardian_tower_life
        self.guardian_tower_attack_range = guardian_tower_attack_range
        self.guardian_tower_damage = guardian_tower_damage
        self.guardian_tower_cooldown_ticks = guardian_tower_cooldown_ticks
        self.faction_base_radius = faction_base_radius
        self.faction_base_vision_range = faction_base_vision_range
        self.faction_base_life = faction_base_life
        self.faction_base_attack_range = faction_base_attack_range
        self.faction_base_damage = faction_base_damage
        self.faction_base_cooldown_ticks = faction_base_cooldown_ticks
        self.burning_duration_ticks = burning_duration_ticks
        self.burning_summary_damage = burning_summary_damage
        self.empowered_duration_ticks = empowered_duration_ticks
        self.empowered_damage_factor = empowered_damage_factor
        self.frozen_duration_ticks = frozen_duration_ticks
        self.hastened_duration_ticks = hastened_duration_ticks
        self.hastened_bonus_duration_factor = hastened_bonus_duration_factor
        self.hastened_movement_bonus_factor = hastened_movement_bonus_factor
        self.hastened_rotation_bonus_factor = hastened_rotation_bonus_factor
        self.shielded_duration_ticks = shielded_duration_ticks
        self.shielded_bonus_duration_factor = shielded_bonus_duration_factor
        self.shielded_direct_damage_absorption_factor = shielded_direct_damage_absorption_factor
        self.aura_skill_range = aura_skill_range
        self.range_bonus_per_skill_level = range_bonus_per_skill_level
        self.magical_damage_bonus_per_skill_level = magical_damage_bonus_per_skill_level
        self.staff_damage_bonus_per_skill_level = staff_damage_bonus_per_skill_level
        self.movement_bonus_factor_per_skill_level = movement_bonus_factor_per_skill_level
        self.magical_damage_absorption_per_skill_level = magical_damage_absorption_per_skill_level
