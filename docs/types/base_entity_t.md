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
## Netvar Colors
Sometimes we need to change the color of some netvar value.  
Obviously we can do that this way:
!!! failure "Bad way"	
	```lua linenums="1"
	local m_vSmokeColor = engine.get_netvar_offset("client.dll", "C_SmokeGrenadeProjectile", "m_vSmokeColor")
	register_callback("paint", function() -- colored smoke
	    entitylist.get_entities("C_SmokeGrenadeProjectile", function(smoke)
	        local address = smoke[m_vSmokeColor]
	        print(address)
	        ffi.cast("float*", address)[0] = 255
	        ffi.cast("float*", address)[1] = 0
	        ffi.cast("float*", address)[2] = 0
	    end)
	end)
	```
And more preferrable will be:
!!! success "Good way"
	```lua linenums="1"
	register_callback("paint", function()
	    entitylist.get_entities("C_SmokeGrenadeProjectile", function(smoke)
	        smoke.m_vSmokeColor = vec3_t(255, 0, 0)
	    end)
	end)
	```
Basically we're doing exactly the same thing, but it is much shorter and simpler
## Netvar usage example
!!! example
	```lua linenums="1"
	local font = render.setup_font("C:/Windows/Fonts/verdana.ttf", 32, 0)
	register_callback("paint", function()
	    local pawn = entitylist.get_local_player_pawn()
	    if pawn == nil then return end

	    local game_scene_node = pawn.m_pGameSceneNode
	    if game_scene_node == nil then return end

	    local weapon_services = pawn.m_pWeaponServices
	    if weapon_services == nil then return end

	    local weapon = weapon_services.m_hActiveWeapon
	    if weapon == nil then return end

	    if weapon.m_bInReload then
	        local origin2 = render.world_to_screen(game_scene_node.m_vecAbsOrigin)
	        if origin2 ~= nil then
	            render.text("reloading", font, origin2, color_t(1, 1, 1, 1))
	        end
	    end
	end)
	```