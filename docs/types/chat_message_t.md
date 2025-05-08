{{ define_function("msg", "is_team_chat", [], "boolean", True) }}
---
{{ define_function("msg", "get_entity", [], "base_entity_t", True) }}
---
{{ define_function("msg", "get_name", [], "string", True) }}
---
{{ define_function("msg", "get_message", [], "string", True) }}
---
{{ define_function("msg", "get_position", [], "string", True) }}
---
{{ define_function("msg", "set_name", [
    ["name", "string", "New name"],
], "", True) }}
---
{{ define_function("msg", "set_message", [
    ["message", "string", "New message"],
], "", True) }}
---
{{ define_function("msg", "set_position", [
    ["position", "string", "New position"],
], "", True) }}