## Entity functions

{{ define_function("entity", "get_class_name", [], "string", True) }}
---
{{ define_function("entity", "get_entity_handle", [], "number", True) }}
---
## Getting FFI pointer
To get entity pointer you can use `entity[0]`  
Also you can use `entity[OFFSET]` to get the address pointing to specified offset of the entity
Hexadecimal and decimal number are both supported
!!! example
    This example will print local player health
    ```lua linenums="1"
    local offset = engine.get_netvar_offset("client.dll", "C_BaseEntity", "m_iHealth")
    local pawn = entitylist.get_local_player_pawn()
    if pawn ~= nil then
        print("Localplayer HP: " .. ffi.cast("int*", pawn[offset])[0])
    end
    ```
