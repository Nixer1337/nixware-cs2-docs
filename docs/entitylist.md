# entitylist

{{ define_function("entitylist", "get_local_player_controller", [], "base_entity_t") }}
---
{{ define_function("entitylist", "get_local_player_pawn", [], "base_entity_t") }}
---
{{ define_function("entitylist", "get_entity_from_handle", [
    ["handle", "number", "Handle of the entity"],
], "base_entity_t") }}
---
### **get_entities**
=== "Return style"
    {{ get_function_table_and_definition("entitylist", "get_entities", [
        ["class_name", "string", "Name of the class.", true],
    ], "base_entity_t[]") }}

=== "Callback style"
    {{ get_function_table_and_definition("entitylist", "get_entities", [
        ["class_name", "string", "Name of the class.", true],
        ["callback", "function", "Callback function, that receives " + format_lua_type("base_entity_t") + " as an argument"]
    ]) }}
    ```lua linenums="1"
    entitylist.get_entities("C_CSPlayerPawn", function(entity)
        -- loop through all players
    end)
    ```