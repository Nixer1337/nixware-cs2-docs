{{ get_arguments_table([
    ["pitch", "number"],
    ["yaw",   "number"],
    ["roll",  "number"],
]) }}

{{ define_function("angle", "__tostring", [], "string", True) }}