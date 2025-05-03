{{ get_arguments_table([
    ["interacts_with", "number", "Which interaction layers do I interact or collide with? (e.g. I collide with LAYER_INDEX_CONTENTS_PASS_BULLETS because I am not a bullet). NOTE: This is analogous to the `solid mask` or `trace mask` in source 1 (bit mask of CONTENTS_* or 1<<LAYER_INDEX_*)"],
    ["interacts_exclude", "number", "Which interaction layers do I _not_ interact or collide with?  If my exclusion layers match _interacts_as on the other object then no interaction happens."],
    ["interacts_as", "number", "Which interaction layers do I represent? (e.g. I am a LAYER_INDEX_CONTENTS_PLAYER_CLIP volume). NOTE: This is analogous to `contents` in source 1  (bit mask of CONTENTS_* or 1<<LAYER_INDEX_*)"],
    ["entity_ids_to_ignore", "number[2]", "This is the ID of the game entity which should be ignored"],
    ["owner_ids_to_ignore", "number[2]", "This is the ID of the owner of the game entity which should be ignored"],
    ["hierarchy_ids", "number[2]", "This is an ID for the hierarchy of game entities (used to disable collision among objects in a hierarchy)"],
    ["object_set_mask", "number", "Set of RnQueryObjectSet bits"],
    ["collision_group", "number", "One of the registered collision groups"],
    ["hit_solid", "boolean", "If true, then query will hit solid"],
    ["hit_solid_requires_generate_contacts", "boolean", "if true, the FCOLLISION_FUNC_ENABLE_SOLID_CONTACT flag will be checked to hit solid"],
    ["hit_trigger", "boolean", "if true, then query will hit tirgger"],
    ["should_ignore_disabled_pairs", "boolean", "If true, then ignores if the query and shape entity IDs are in collision pairs"],
    ["ignore_if_both_interact_with_hitboxes", "boolean", "If true, then ignores if both query and shape interact with LAYER_INDEX_CONTENTS_HITBOX"],
    ["force_hit_everything", "boolean", "If true, will hit any objects without any conditions"],
    ["unknown", "boolean", "Haven't found where this is used yet"],
    ["iterate_entities", "boolean", "If true then calls ShouldHitEntity for each hit entity"],
]) }}

### **Constructor**

{{ define_constructor("trace_filter_t", [
    ["interacts_with", "number"],
    ["collision_group", "number"],
    ["iterate_entities", "boolean"],
    ["should_hit_entity_callback", "function", "", true],
]) }}