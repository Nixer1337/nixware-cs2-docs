{{ get_arguments_table([
    ["pitch", "number"],
    ["yaw",   "number"],
    ["roll",  "number"],
]) }}

### **Constructor**

{{ define_constructor("angle_t", [
    ["pitch", "number"],
    ["yaw", "number"],
    ["roll", "number"],
]) }}

---

{{ define_function("angle", "__tostring", [], "string", True) }}