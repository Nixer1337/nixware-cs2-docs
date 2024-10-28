# render
## Functions

{{ define_function("render", "screen_size", [
], "vec2_t") }}
---
{{ define_function("render", "frame_count", [
], "number") }}
---
{{ define_function("render", "frame_time", [
], "number") }}
---
{{ define_function("render", "setup_texture", [
    ["filename", "string", "Path to the texture"],
], "texture_t") }}
!!! warning
    If you specify a texture that does not exist, return value will be `nil`.
??? example
    ``` lua linenums="1"
    local texture = render.setup_texture("C:/example.png")
    register_callback("paint", function()
        render.texture(texture, vec2_t(100, 100), vec2_t(200, 200))
    end)
    ```
---

{{ define_function("render", "setup_font", [
    ["filename", "string", "Path to the font"],
    ["size",     "number", "Font size"],
    ["flags",    "number", "Font flags", true],
], "font_t") }}
!!! warning
    If you specify a font that does not exist, return value will be `nil`.
??? example
    ``` lua linenums="1"
    local font = render.setup_font("C:/Windows/Fonts/verdana.ttf", 32, 0)
    register_callback("paint", function()
        render.text("hello from lua api!", font, vec2_t(100, 100), color_t(1, 1, 1, 1))
    end)
    ```
---
{{ define_function("render", "calc_text_size", [
    ["text", "string", "Text size of which will be calculated"],
    ["font", "font_t", "Font object"],
    ["size", "number", "Font size", true],
], "vec2_t") }}
!!! warning
    If you specify a font that does not exist, return value will be `nil`.
---
{{ define_function("render", "world_to_screen", [
    ["pos", "vec3_t", "World position"],
], "vec3_t") }}
!!! warning
    If world position is not on the screen, return value will be `nil`.
??? example
    ``` lua linenums="1"
    register_callback("paint", function()
        local w2s = render.world_to_screen(vec3_t(0, 0, 0))
        if w2s then
            render.circle_fade(w2s, 20, color_t(1, 0.25, 0.25, 0.5), color_t(0, 0, 0, 1))
        end
    end)
    ```
---
## Draw functions
{{ define_function("render", "texture", [
    ["texture",     "texture_t",    "Texture object"],
    ["from",        "vec2_t",       "Start position of the texture"],
    ["to",          "vec2_t",       "End position of the texture"],
    ["color",       "color_t",      "Texture color", true],
]) }}
---
{{ define_function("render", "text", [
    ["text",    "string",  "Text to render"],
    ["font",    "font_t",  "Font object, or `0` = default font, or `1` = pixel font"],
    ["pos",     "vec2_t",  "Position of where text will be rendered"],
    ["color",   "color_t", "Text color", true],
    ["size",    "number",  "Text size", true],
]) }}
---
{{ define_function("render", "line", [
    ["from",      "vec2_t",  "Start position of the line"],
    ["to",        "vec2_t",  "End position of the line"],
    ["color",     "color_t", "Color of the line"],
    ["thickness", "number",  "Thickness of the line", true],
]) }}
---
{{ define_function("render", "rect", [
    ["from",     "vec2_t",  "Start position of the rectangle"],
    ["to",       "vec2_t",  "End position of the rectangle"],
    ["color",    "color_t", "Color of the rectangle"],
    ["rounding", "number",  "Rounding of the rectangle", true],
    ["thickness","number",  "Thickness of the rectangle", true],
]) }}
---
{{ define_function("render", "rect_filled", [
    ["from",     "vec2_t",  "Start position of a rectangle"],
    ["to",       "vec2_t",  "End position of the rectangle"],
    ["color",    "color_t", "Color of the rectangle"],
    ["rounding", "number",  "Rounding of the rectangle", true],
]) }}
---
{{ define_function("render", "rect_filled_fade", [
    ["from",          "vec2_t",  "Start position of a rectangle"],
    ["to",            "vec2_t",  "Font object"],
    ["col_upr_left",  "color_t", "Color of the top left corner"],
    ["col_upr_right", "color_t", "Color of the top right corner"],
    ["col_bot_right", "color_t", "Color of the bottom right corner"],
    ["col_bot_left",  "color_t", "Color of the bottom left corner"],
]) }}
<!-- ["rounding",    "number",   "Rounding of the rectangle", true], -->
---
{{ define_function("render", "circle", [
    ["pos",      "vec2_t",  "Position of the circle"],
    ["radius",   "number",  "Radius of the circle"],
    ["segments", "number",  "Count of the circle segments"],
    ["color",    "color_t", "Color of the circle"],
    ["thickness","number",  "Thickness of the circle", true],
]) }}
---
{{ define_function("render", "circle_filled", [
    ["pos",      "vec2_t",  "Position of the circle"],
    ["radius",   "number",  "Radius of the circle"],
    ["segments", "number",  "Count of the circle segments"],
    ["color",    "color_t", "Color of the circle"],
]) }}
---
{{ define_function("render", "circle_fade", [
    ["pos",         "vec2_t",   "Position of the circle"],
    ["radius",      "number",   "Radius of the circle"],
    ["color_in",    "color_t",  "Color of the center of the circle"],
    ["color_out",   "color_t",  "Color of the edge of the circle"],
]) }}
---
{{ define_function("render", "filled_polygon", [
    ["points",  "vec2_t[]", "Array of screen positions"],
    ["color",   "color_t",  "Color of the polygon"],
]) }}
---
{{ define_function("render", "poly_line", [
    ["points",  "vec2_t[]", "Array of screen positions"],
    ["color",   "color_t",  "Color of the polyline"],
]) }}
---
{{ define_function("render", "push_clip_rect", [
    ["from",                                "vec2_t",   "Start position of the clip rect"],
    ["to",                                  "vec2_t",   "End position of the clip rect"],
    ["intersect_with_current_clip_rect",    "boolean",  "Allow intersections with other clips", true],
]) }}
---
{{ define_function("render", "pop_clip_rect", []) }}
---
## World draw functions
{{ define_function("render", "circle_3d", [
    ["pos",       "vec3_t",  "Position of the circle"],
    ["radius",    "number",  "Radius of the circle"],
    ["color",     "color_t", "Color of the circle"],
    ["thickness", "number",   "Thickness of the circle", true],
    ["normal",    "vec3_t",  "Rotation of the circle", true],
]) }}
---
{{ define_function("render", "circle_filled_3d", [
    ["pos",    "vec3_t",  "Position of the circle"],
    ["radius", "number",  "Radius of the circle"],
    ["color",  "color_t", "Color of the circle"],
    ["normal", "vec3_t",  "Rotation of the circle", true],
]) }}
---
{{ define_function("render", "circle_fade_3d", [
    ["pos",       "vec3_t",  "Position of the circle"],
    ["radius",    "number",  "Radius of the circle"],
    ["color_in",  "color_t", "Color of the center of the circle"],
    ["color_out", "color_t", "Color of the edge of the circle"],
    ["normal",    "vec3_t",  "Rotation of the circle", true],
]) }}