{{ define_function("entity", "__tostring", [], "string", True) }}
---
{{ define_function("entity", "get_abs_origin", [], "vec3_t", True) }}
---
{{ define_function("entity", "get_abs_rotation", [], "angle_t", True) }}
---
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

## Using netvars
!!! example
	```lua linenums="1"
	local font = render.setup_font("C:/Windows/Fonts/verdana.ttf", 25)
	register_callback("paint", function()
		local pawn = entitylist.get_local_player_pawn()
		if pawn == nil then return end

		local game_scene_node = pawn.m_pGameSceneNode
		if game_scene_node == nil then return end

		local weapon_services = pawn.m_pWeaponServices
		if weapon_services == nil then return end

		local weapon = weapon_services.m_hActiveWeapon
		if weapon == nil then return end

		local weapondata = weapon.m_pWeaponData
		if weapondata == nil then return end

		local origin2 = render.world_to_screen(game_scene_node.m_vecAbsOrigin)
		if origin2 ~= nil then
			render.text("weapon price: $" .. tostring(weapondata.m_nPrice), font, origin2, color_t(1, 1, 1, 1))
			if weapon.m_bInReload then
				render.text("reloading", font, origin2 + vec2_t(0, 20), color_t(1, 1, 1, 1))
			end
		end
	end)
	```