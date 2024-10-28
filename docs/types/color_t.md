{{ get_arguments_table([
    ["r", "number"],
    ["g", "number"],
    ["b", "number"],
    ["a", "number"],
]) }}

## Functions

{{ define_function("color", "lerp", [
    ["other", "color_t", "Other color"],
    ["fraction", "number", "Fraction"],
], "color_t", True) }}