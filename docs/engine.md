# engine

{{ define_function("engine", "execute_client_cmd", [
    ["command", "string", "Command to execute"],
]) }}
??? example
    ``` lua linenums="1"
    register_callback("player_death", function(event)
        if event:get_pawn("attacker") == entitylist.get_local_player_pawn() then 
            engine.execute_client_cmd("say 1")
        end
    end)
    ```
---
{{ define_function("engine", "play_sound", [
    ["sound_name", "string", "Sound name"],
    ["volume", "number", "Volume in the range [0.0, 1.0]"],
]) }}
---
{{ define_function("engine", "chat_print", [
    ["text", "string", "Text to print"],
]) }}
---
{{ define_function("engine", "camera_in_thirdperson", [], "boolean") }}
---
{{ define_function("engine", "get_level_name", [], "string") }}
---
{{ define_function("engine", "get_product_version_string", [], "string") }}
---
{{ define_function("engine", "get_net_channel", [], "net_channel_t") }}
---
{{ define_function("engine", "get_netvar_offset", [
    ["module_name", "string", "Module name"],
    ["table_name", "string", "Name of the table"],
    ["prop_name", "string", "Name of the property"]
], "number") }}
---
{{ define_function("engine", "trace_bullet", [
    ["from_entity", "base_entity_t", "Player whose weapon will be used for this trace"],
    ["from", "vec3_t", "Position to start tracing from"],
    ["to", "vec3_t", "Position where the trace ends"]
], "number") }}
!!! info 
    Returns `nil` if bullet can't hit