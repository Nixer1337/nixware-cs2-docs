# math

!!! info
    This page describes only overridden and custom functions.  
    Other functions of the standard Lua environment haven't been changed in any aspect

{{ define_function("math", "calc_angle", [
    ["src", 'vec3_t', "Source vector"],
    ["dst", "vec3_t", "Destination vector"],
], "angle_t") }}
---
{{ define_function("math", "calc_fov", [
    ["src", 'angle_t', "Source angle"],
    ["dst", "angle_t", "Destination angle"],
], "number") }}
---
{{ define_function("math", "normalize_angle", [
    ["angle", 'number', "Angle"],
], "number") }}
---
{{ define_function("math", "vector_angles", [
    ["forward", 'vec3_t', "Vector"],
], "angle_t") }}
---
{{ define_function("math", "angle_vectors", [
    ["angles", 'angle_t', "Angles"],
], "[`forward`](/types/vec3_t/), [`right`](/types/vec3_t/), [`up`](/types/vec3_t/)") }}