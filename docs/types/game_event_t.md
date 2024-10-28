## Getters

{{ define_function("event", "get_name", [], "string", True) }}
---
{{ define_function("event", "get_pawn", [
    ["key_name", "string", "Key name"],
], "base_entity_t", True) }}
---
{{ define_function("event", "get_int64", [
    ["key_name", "string", "Key name"],
], "number", True) }}