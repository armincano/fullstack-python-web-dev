-- Active: 1725460995925@@127.0.0.1@5432@pokemon_db
BEGIN;
COPY "pokemon" ("pokedex","name","evolutions_num","types_num","type1","type2","capt_rate","hp","attack","defense","special","speed","normal_dmg","fire_dmg","water_dmg","electric_dmg","grass_dmg","ice_dmg","fight_dmg","poison_dmg","ground_dmg","flying_dmg","psychic_dmg","bug_dmg","rock_dmg","ghost_dmg","dragon_dmg","is_legendary")
FROM '/Users/armin/Desktop/fullstack-python-web-dev/m5-database/pokemon-db/csv/first-gen-pokemons-compact-eng.csv' DELIMITER ','
CSV HEADER;
COPY "captures" ("pokedex","capt_date","location","was_egg","weight","height")
FROM '/Users/armin/Desktop/fullstack-python-web-dev/m5-database/pokemon-db/csv/captures-eng.csv' DELIMITER ','
CSV HEADER;
END;