## Getters

{{ define_function("event", "get_name", [], "string", True) }}
---
{{ define_function("event", "get_int", [
    ["key_name", "string", "Key name"],
], "number", True) }}
---
{{ define_function("event", "get_float", [
    ["key_name", "string", "Key name"],
], "number", True) }}
---
{{ define_function("event", "get_string", [
    ["key_name", "string", "Key name"],
], "string", True) }}
---
{{ define_function("event", "get_pawn", [
    ["key_name", "string", "Key name"],
], "base_entity_t", True) }}
---
{{ define_function("event", "get_controller", [
    ["key_name", "string", "Key name"],
], "base_entity_t", True) }}
---

## Setters

{{ define_function("event", "set_int", [
    ["key_name", "string", "Key name"],
    ["value", "number", "Value"],
], "", True) }}
---
{{ define_function("event", "set_float", [
    ["key_name", "string", "Key name"],
    ["value", "number", "Value"],
], "", True) }}
---
{{ define_function("event", "set_string", [
    ["key_name", "string", "Key name"],
    ["value", "string", "Value"],
], "", True) }}