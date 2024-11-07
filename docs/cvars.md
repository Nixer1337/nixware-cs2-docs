# cvars

## Getting convars
You can do this by `cvars.CONVAR_NAME`
``` lua linenums="1"
print("Current sensitivity:" .. cvars.sensitivity:get_float())
```
Return type is {{ format_lua_type("convar_t") }}

## Convar list

{{ get_arguments_table([
    ["m_skeletonInstance", "convar_t"],
]) }}