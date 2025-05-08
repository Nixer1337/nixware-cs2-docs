# engine

{{ define_function("engine", "execute_client_cmd", [
    ["command", "string", "Command to execute"],
]) }}
??? example
    ``` lua linenums="1"
    register_callback("player_death", function(event)
        if event:get_pawn("attacker") == entitylist.get_local_player_pawn() then 
            engine.execute_client_cmd("say 1")
        end
    end)
    ```
---
{{ define_function("engine", "play_sound", [
    ["sound_name", "string", "Sound name"],
    ["volume", "number", "Volume in the range [0.0, 1.0]"],
]) }}
---
{{ define_function("engine", "chat_print", [
    ["text", "string", "Text to print"],
]) }}
---
{{ define_function("engine", "camera_in_thirdperson", [], "boolean") }}
---
{{ define_function("engine", "get_level_name", [], "string") }}
---
{{ define_function("engine", "get_product_version_string", [], "string") }}
---
{{ define_function("engine", "get_net_channel", [], "net_channel_t") }}
---
{{ define_function("engine", "get_hitbox_pos", [
    ["pawn", "base_entity_t", "Player pawn"],
    ["hitbox_index", "number", "Hitbox index"],
], "vec3_t") }}
!!! info 
    Returns `nil` if unsuccessful

---
{{ define_function("engine", "get_netvar_offset", [
    ["module_name", "string", "Module name"],
    ["table_name", "string", "Name of the table"],
    ["prop_name", "string", "Name of the property"]
], "number") }}
---
{{ define_function("engine", "trace_shape", [
    ["ray", "ray_t"],
    ["start", "vec3_t"],
    ["end", "vec3_t"],
    ["filter", "trace_filter_t"]
], "trace_t") }}
??? example
    ``` lua linenums="1"
    local g_camera_angles = angle_t(0, 0, 0)
    local g_camera_origin = vec3_t(0, 0, 0)
    register_callback('override_view', function(view) g_camera_angles = view.angles g_camera_origin = view.origin end)
    register_callback('paint', function()
        local forward, _, _ = math.angle_vectors(g_camera_angles)
        local filter = trace_filter_t(0x2800100001, 3, true)
        local trace = engine.trace_shape(ray_t(), g_camera_origin, g_camera_origin + (forward * 10000), filter)
        render.circle_3d(trace.end_pos, 5, color_t(1, 1, 1, 1), 1, trace.hit_normal)
    end)
    ```

---

{{ define_function("engine", "trace_bullet", [
    ["from_pawn", "base_entity_t", "Player whose weapon will be used for this trace"],
    ["from", "vec3_t", "Position to start tracing from"],
    ["to", "vec3_t", "Position where the trace ends"]
], "number") }}
!!! info 
    Returns `nil` if bullet can't hit
