from markdown_table_generator import generate_markdown, table_from_string_list, Alignment
import glob
from pathlib import Path
from textwrap import indent
# from math import floor

# parse types folder to get all types
types_paths = ["docs/types/*.md", "docs/menu/types/*.md"]
lua_types = {}
for path in types_paths:
    for file in glob.glob(path):
        #type name = file name without extension
        type_name = Path(file).stem
        p = Path(file)
        type_path = p.relative_to(*p.parts[:1]).with_suffix('').as_posix()
        lua_types[type_name] = type_path

def define_env(env):
    "Hook function"

    class argument():
        name: str
        type: str
        description: str
        is_optional: bool
        def __init__(self, table):
            self.name = table[0]
            self.type = table[1]
            if len(table) >= 3:
                self.description = table[2]
            else:
                self.description = ""
            if len(table) == 4:
                self.is_optional = table[3]
            else:
                self.is_optional = False

    def get_type_link(type_name) -> str:
        #if first characters of type_name matches a type, return that type
        lua_types_keys = list(lua_types.keys())
        for key in lua_types_keys:
            if type_name.startswith(key):
                return f"/{lua_types[key]}/"
        return ""
    
    @env.macro
    def format_lua_type(type_name) -> str:
        if type_name.startswith("["):
            return type_name
        type_link = get_type_link(type_name)
        if type_link != "":
            return f"[`{type_name}`]({type_link})"
        return f"`{type_name}`"
    
    @env.macro
    def get_arguments_table(temp_args: list[list]):
        if len(temp_args) <= 0:
            return ""
        description_present = False
        markdown_arguments_list: list[list[str | None]] = [["Name", "Type", "Description"]]
        for temp_arg in temp_args:
            arg = argument(temp_arg)
            if arg.description != "":
                description_present = True
            if arg.is_optional:
                arg.description = f"Optional. {arg.description}"
            if arg.type[0] == '"' or arg.type[0] == "'":
                pass
            else:
                markdown_arguments_list.append([f"**{arg.name}**", format_lua_type(arg.type), arg.description])
        
        if not description_present:
            markdown_arguments_list[0][2] = None
        
        return generate_markdown(table_from_string_list(rows=markdown_arguments_list))
    
    @env.macro
    def get_function_definition(table_name: str, func_name: str, temp_args: list[list], return_type: str = "", is_not_static: bool = False):
        argument_list: list[str] = []
        for temp_arg in temp_args:
            arg = argument(temp_arg)
            if arg.is_optional:
                arg.name = f"{arg.name}?"
            if arg.type[0] == '"' or arg.type[0] == "'":
                argument_list.append(f"{arg.type}")
            else:  
                argument_list.append(f"{arg.name}: {arg.type}")
        return_colon = ""
        if return_type != "":
            return_colon = ":"
            return_type = " " + format_lua_type(return_type)
        function_separator = "."
        if is_not_static:
            function_separator = ":"
        if table_name == "":
            function_separator = ""
        return f"""
<font size=5>`:::typescript {table_name}{function_separator}{func_name}({", ".join(argument_list)}){return_colon}`{return_type}</font>        
"""

    @env.macro
    def get_function_table_and_definition(table_name: str, func_name: str, temp_args: list[list], return_type: str = "", is_not_static: bool = False, indentation: int = 1):
        return indent(f"""

{ get_function_definition(table_name, func_name, temp_args, return_type, is_not_static) }
{ get_arguments_table(temp_args) }

""", " " * indentation * 4)

    @env.macro
    def define_function(table_name: str, func_name: str, temp_args: list[list], return_type: str = "", is_not_static: bool = False):
        return f"""

### **{func_name}**

{ get_function_table_and_definition(table_name, func_name, temp_args, return_type, is_not_static, 0) }

"""
    
    @env.macro
    def element_getters(table_name):
        return f"""

{ define_function(table_name, "is_visible", [], "boolean", True) }

---

{ define_function(table_name, "get_label", [], "string", True) }

"""
    @env.macro
    def element_setters(table_name):
        return f"""

{ define_function(table_name, "set_visible", [
    ["visibility", "boolean", "Will the element be visible"]
], "", True) }

---

{ define_function(table_name, "set_label", [
    ["label", "string", "The new label"]
], "", True) }

"""
    @env.macro
    def define_cvar(var_name: str):
        return f"""

### **{var_name}**

<font size=5>`:::typescript cvars.{var_name}:` `convar_t`</font>

"""