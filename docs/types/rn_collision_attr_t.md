{{ get_arguments_table([
    ["interacts_as", "number", "Which interaction layers do I represent? (e.g. I am a LAYER_INDEX_CONTENTS_PLAYER_CLIP volume). NOTE: This is analogous to `contents` in source 1  (bit mask of CONTENTS_* or 1<<LAYER_INDEX_*)"],
    ["interacts_with", "number", "Which interaction layers do I interact or collide with? (e.g. I collide with LAYER_INDEX_CONTENTS_PASS_BULLETS because I am not a bullet). NOTE: This is analogous to the `solid mask` or `trace mask` in source 1 (bit mask of CONTENTS_* or 1<<LAYER_INDEX_*)"],
    ["interacts_exclude", "number", "Which interaction layers do I _not_ interact or collide with?  If my exclusion layers match _interacts_as on the other object then no interaction happens."],
    ["entity_id", "number", "This is the ID of the game entity"],
    ["owner_id", "number", "This is the ID of the owner of the game entity"],
    ["hierarchy_id", "number", "This is an ID for the hierarchy of game entities (used to disable collision among objects in a hierarchy)"],
    ["collision_group", "number", "One of the registered collision groups"],
    ["collision_function_mask", "number", "Set of CollisionFunctionMask_t bits"],
]) }}