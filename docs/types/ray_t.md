### **Constructors**

{{ define_constructor("ray_t", []) }}

{{ define_constructor("ray_t", [
    ["start_offset", "vec3_t"],
]) }}

{{ define_constructor("ray_t", [
    ["start_offset", "vec3_t"],
    ["radius", "number"],
]) }}

{{ define_constructor("ray_t", [
    ["mins", "vec3_t"],
    ["maxs", "vec3_t"],
]) }}

{{ define_constructor("ray_t", [
    ["center_a", "vec3_t"],
    ["center_b", "vec3_t"],
    ["radius", "number"],
]) }}

{{ define_constructor("ray_t", [
    ["center_a", "vec3_t"],
    ["center_b", "vec3_t"],
    ["radius", "number"],
]) }}