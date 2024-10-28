# engine

{{ define_function("engine", "execute_client_cmd", [
    ["command", "string", "Command to execute"],
]) }}
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