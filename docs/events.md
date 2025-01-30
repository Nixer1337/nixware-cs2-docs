# events

{{ define_function("", "paint", []) }}
---
{{ define_function("", "game_event", [
    ["event", "game_event_t", "Game event"],
]) }}
---
{{ define_function("", "override_view", [
    ["view_setup", "view_setup_t", "View setup"],
]) }}
---
{{ define_function("", "console_input", [
    ["cmd", "string", "Console command"],
]) }}
This event is called fired when user presses enter in console.  
First argument is the command that was entered.  
!!! example
	```lua linenums="1"
	register_callback('console_input', function(cmd)
		print("user typed: " .. cmd)
		return false
	end)
	```
!!! important "Return value of the function"
	Return value matters here. If the function returned `false`, the game will not execute the command, otherwise it will.   

---
{{ define_function("", "unload", []) }}