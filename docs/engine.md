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
    ["volume", "string", "Volume"],
]) }}
---
{{ define_function("engine", "chat_print", [
    ["text", "string", "Text to print"],
]) }}
---
{{ define_function("engine", "get_level_name", []) }}
---
{{ define_function("engine", "get_netvar_offset", [
    ["module_name", "string", "Module name"],
    ["table_name", "string", "Name of the table"],
    ["prop_name", "string", "Name of the property"]
], "number") }}