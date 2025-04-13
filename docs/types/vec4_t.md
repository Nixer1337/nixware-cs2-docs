{{ get_arguments_table([
    ["x", "number"],
    ["y", "number"],
    ["z", "number"],
    ["w", "number"],
]) }}

{{ define_function("vec4", "__tostring", [], "string", True) }}