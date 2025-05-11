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
		print("user typed:", cmd)
		if cmd == 'quit' then
			return false -- prevents quit
		end
	end)
	```
!!! important "Return value of the function"
	You can interrupt the in-game command execution by returning `false` from the function. So basically if you return `false`, the command will not be executed by the game. 

---
{{ define_function("", "player_chat", [
    ["msg", "chat_message_t", "Chat message"],
]) }}
!!! important "Return value of the function"
	You prevent chat print by returning `false` from the function. So basically if you return `false`, chat message will not print by the game. 

---

{{ define_function("", "string_cmd", [
    ["cmd", "string", "Command"],
]) }}
!!! example
	```lua linenums="1"
	register_callback('string_cmd', function(cmd)
		if cmd:find('say_team') then
			return nil --block team communication
		elseif cmd:find('say') then
			return 'say YOUR_MESSAGE'
		end
	end)
	```

---

{{ define_function("", "unload", []) }}