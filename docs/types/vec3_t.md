{{ get_arguments_table([
    ["x", "number"],
    ["y", "number"],
    ["z", "number"],
]) }}

{{ define_function("vec3", "lerp", [
    ["other", "vec3_t", "Other vector"],
    ["fraction", "number", "Fraction"],
], "vec3_t", True) }}
---
{{ define_function("vec3", "length_2d", [], "number", True) }}
---
{{ define_function("vec3", "length", [], "number", True) }}
---
{{ define_function("vec3", "length_2d_sqr", [], "number", True) }}
---
{{ define_function("vec3", "length_sqr", [], "number", True) }}
---
{{ define_function("vec3", "dist_to_2d", [
    ["other", "vec3_t", "Other vector"],
], "number", True) }}
---
{{ define_function("vec3", "dist_to", [
    ["other", "vec3_t", "Other vector"],
], "number", True) }}
---
{{ define_function("vec3", "dot", [
    ["other", "vec3_t", "Other vector"],
], "number", True) }}
---
{{ define_function("vec3", "cross", [
    ["other", "vec3_t", "Other vector"],
], "vec3_t", True) }}
---
{{ define_function("vec3", "normalized", [], "vec3_t", True) }}
---
{{ define_function("vec3", "normalize", [], "number", True) }}