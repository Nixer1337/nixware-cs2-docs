{{ get_arguments_table([
    ["x", "number"],
    ["y", "number"],
]) }}

### **Constructor**

{{ define_constructor("vec2_t", [
    ["x", "number"],
    ["y", "number"],
]) }}

---

{{ define_function("vec2", "__tostring", [], "string", True) }}