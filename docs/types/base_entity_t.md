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
    This example will print money of all players
    ```lua linenums="1"
    entitylist.get_entities("C_CSPlayerPawn", function(entity)
        -- example
    end)
    ```
