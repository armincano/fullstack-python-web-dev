
BEGIN;

CREATE TABLE IF NOT EXISTS public.characters
(
    character_id integer NOT NULL,
    first_name text NOT NULL,
    last_name text,
    character_type_id integer NOT NULL,
    damage_stat integer,
    "description" text NOT NULL,
    PRIMARY KEY (character_id)
);

CREATE TABLE IF NOT EXISTS public.arcs
(
    arc_id integer NOT NULL,
    arc_category_id integer NOT NULL,
    "name" text NOT NULL,
    "description" text NOT NULL,
    PRIMARY KEY (arc_id)
);

CREATE TABLE IF NOT EXISTS public.characters_types
(
    character_type_id integer NOT NULL,
    "type" text NOT NULL,
    PRIMARY KEY (character_type_id)
);

CREATE TABLE IF NOT EXISTS public.arcs_categories
(
    arc_category_id integer NOT NULL,
    "name" text NOT NULL,
    "description" text NOT NULL,
    PRIMARY KEY (arc_category_id)
);

CREATE TABLE IF NOT EXISTS public.arcs_characters
(
    arcs_characters_id serial NOT NULL,
    arc_id integer NOT NULL,
    character_id integer NOT NULL,
    PRIMARY KEY (arcs_characters_id)
);

ALTER TABLE IF EXISTS public.characters
    ADD CONSTRAINT fk_characters_characters_types_character_type_id FOREIGN KEY (character_type_id)
    REFERENCES public.characters_types (character_type_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.arcs
    ADD CONSTRAINT fk_arcs_arcs_categories_arc_category_id FOREIGN KEY (arc_category_id)
    REFERENCES public.arcs_categories (arc_category_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.arcs_characters
    ADD CONSTRAINT fk_arcs_characters_arcs_arc_id FOREIGN KEY (arc_id)
    REFERENCES public.arcs (arc_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.arcs_characters
    ADD CONSTRAINT fk_arcs_characters_characters_character_id FOREIGN KEY (character_id)
    REFERENCES public.characters (character_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;