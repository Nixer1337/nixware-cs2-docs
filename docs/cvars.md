{{define_cvar("testscript_debug")}}
Debug test scripts.

---
{{define_cvar("tools_stall_monitor_break_on_unknown_cause")}}
Break on unknown stall cause

---
{{define_cvar("net_async_job_random_sleep")}}
Sleep randomly 0..net_async_job_random_sleep ms in the parallel server jobs; sleep is per job

---
{{define_cvar("stats_display")}}
Displays perf statistics information

---
{{define_cvar("stats_collect_gpu")}}
While doing stats_display, collect GPU perf counters. Used for stats_print_gpu.

---
{{define_cvar("vprof_counters")}}

---
{{define_cvar("vprof_counters_show_minmax")}}

---
{{define_cvar("debug_draw_enable")}}

---
{{define_cvar("engine_rendersystem_used")}}
Rendersystem option in use (changing this does not change the rendersystem).

---
{{define_cvar("engine_rendersystem_init")}}
Rendersystem option requested (changing this does not change the rendersystem).

---
{{define_cvar("engine_rendersystem_shader_model")}}
Rendersystem shader model in use (changing this does not change the shader model).

---
{{define_cvar("engine_platform_name_extended")}}
Platform the engine is running on.

---
{{define_cvar("engine_ostype")}}
OS type the engine is running on.

---
{{define_cvar("engine_cpu_info_extended")}}
CPU the engine is running on.

---
{{define_cvar("cl_language")}}
Language

---
{{define_cvar("sys_minidumpspewlines")}}
Lines of crash dump console spew to keep.

---
{{define_cvar("sv_maxrate")}}
Max bandwidth rate allowed on server, 0 == unlimited

---
{{define_cvar("sv_minrate")}}
Min bandwidth rate allowed on server, 0 == unlimited

---
{{define_cvar("sys_minidumpexpandedspew")}}

---
{{define_cvar("report_connection_failure_percentage")}}

---
{{define_cvar("engine_no_focus_sleep")}}

---
{{define_cvar("engine_no_focus_sleep_vconsole_suppress")}}
When VConsole is in the foreground, don't trigger engine_no_focus_sleep behavior

---
{{define_cvar("engine_show_frame_pacing")}}

---
{{define_cvar("battery_saver")}}
OBSOLETE replaced by mobile_fps_* - Battery saver mode. 0=off, 1=on

---
{{define_cvar("mobile_fps_limit")}}
MOBILE_FPS_CONTROL: Mobile FPS limit - 15, 30, 60

---
{{define_cvar("mobile_fps_increase_during_touch")}}
MOBILE_FPS_CONTROL: If true we increase framerate limit during touch

---
{{define_cvar("mobile_fps_increase_during_charging")}}
MOBILE_FPS_CONTROL: If true we increase framerate limit while charging

---
{{define_cvar("mobile_fps_increase_during_hfr_animations")}}
MOBILE_FPS_CONTROL: If true we increase framerate limit during HFR-tagged animations and transitions.

---
{{define_cvar("fps_max")}}
Frame rate limiter.  0=no limit.  Does not apply to dedicated server.

---
{{define_cvar("fps_max_ui")}}
Frame rate limiter while the game UI is displayed.  0=no limit.  Does not apply to dedicated server.

---
{{define_cvar("fps_max_tools")}}
Additional frame rate limit while in tools mode and a window other than the game window has focus. Note that fps_max still applies, this only allows the maximum frame rate for tools mode to be lower. 0=no tools specific limit.

---
{{define_cvar("sv_fps_max")}}
Dedicated server frame rate limiter. 0=tick rate. Only applies to the dedicated server.

---
{{define_cvar("async_serialize")}}
Force async reads to serialize for profiling

---
{{define_cvar("con_logfile_suffix")}}
Suffix to append to the console log, may be changed to reopen the log

---
{{define_cvar("gameevents_showevents")}}
Dump game events to console. (1 = Show Signaling, 2 = Show Posting also).

---
{{define_cvar("gameevents_showeventlisteners")}}
Show listening addition/removals

---
{{define_cvar("sv_hoststate_quit_syscall")}}
When enabled, game server will quit immediately via syscall instead of running host states shutdown sequence

---
{{define_cvar("execute_command_every_frame")}}

---
{{define_cvar("engine_show_frame_dispatch")}}
show frame dispatch names.

---
{{define_cvar("engine_show_frame_ticks")}}

---
{{define_cvar("engine_max_ticks_to_simulate")}}
Max number of ticks to simulate per frame, after which simulation will start to slow down compared to real time.

---
{{define_cvar("engine_render_only")}}

---
{{define_cvar("engine_allow_multiple_ticks_per_frame")}}
When the client is catching up in low frame rate situations, should we run tick more than once a frame?

---
{{define_cvar("engine_allow_multiple_simulates_per_frame")}}
When the client is catching up in low frame rate situations, should we run client simulate more than once a frame?

---
{{define_cvar("engine_client_tick_pad_enable")}}

---
{{define_cvar("engine_low_latency_sleep_after_client_tick")}}
When r_low_latency is enabled, this moves the low latency sleep on tick frames to happen after client simulation.

---
{{define_cvar("engine_accurate_input_processing_delta_time")}}
When true, elapsed time given to the input processing will be the time elapsed since the last input processing. This is only relevant when input is processed multiple times per frame ( i.e. multiple ticks per frame)

---
{{define_cvar("cl_predict_after_every_createmove")}}
run prediction after every CreateMove instead of only after CreateMove for the final tick in a frame.

---
{{define_cvar("cl_tickpacket_send_every_tick")}}
Send a network packet each time we generate a new usercommand, even if our frame rate is slow and we generate multiple commands in one frame

---
{{define_cvar("cl_poll_network_early")}}
Enable polling for network messages every frame, instead of every tick

---
{{define_cvar("sv_long_frame_ms")}}
If a server frame takes longer than N ms, complain about it.  (Dedicated server only.)  See also engine_frametime_warnings_enable.

---
{{define_cvar("engine_frametime_warnings_enable")}}
Enable framerate-related warnings, such as sv_long_frame_ms.  Disabling warnings is useful when running in situations such a debug where a slow frame rate is expected

---
{{define_cvar("engine_frametime_amnesty_debug")}}
Enable logging about events that disable frame time warnings

---
{{define_cvar("host_force_frametime_to_equal_tick_interval")}}

---
{{define_cvar("host_force_max_frametime_to_tick_interval")}}

---
{{define_cvar("host_framerate")}}
Set to lock per-frame time elapse.

---
{{define_cvar("host_timescale")}}
Prescale the clock by this amount.

---
{{define_cvar("engine_max_resource_system_update_time")}}

---
{{define_cvar("r_experimental_lag_limiter")}}

---
{{define_cvar("vis_sunlight_enable")}}
Toggle whether to use sunlight PVS for sunlight views (0 = sky PVS, 1 = sunlight PVS)

---
{{define_cvar("vis_enable")}}
Enable precomputed visibility when true

---
{{define_cvar("r_indirectlighting")}}
Set to use indirect lighting

---
{{define_cvar("r_rendersun")}}
Render sun lighting

---
{{define_cvar("r_drawdecals")}}
Set to render decals

---
{{define_cvar("r_drawviewmodel")}}
Render view model

---
{{define_cvar("r_directlighting")}}
Set to use direct lighting

---
{{define_cvar("r_ssao")}}
Set to use screen-space ambient occlusion

---
{{define_cvar("r_force_zprepass")}}
0: Force z prepass off. 1: Force on. -1: Don't force

---
{{define_cvar("r_zprepass_normals")}}
0: Use normals reconstructed from depth. 1: Output correct normals in z prepass.

---
{{define_cvar("r_translucent")}}
Enable rendering of translucent geometry

---
{{define_cvar("r_showsunshadowdebugrendertargets")}}
Set to render sun shadow render targets

---
{{define_cvar("r_showdebugoverlays")}}
Set to render debug overlays

---
{{define_cvar("r_showsceneobjectbounds")}}
Show scenesystem object bounding boxes

---
{{define_cvar("r_showsunshadowdebugsplitvis")}}
Set to render sun shadow split visibility debugger

---
{{define_cvar("phys_highlight_expensive_objects")}}
Highlight expensive physics objects

---
{{define_cvar("phys_highlight_expensive_objects_strength")}}
Highlight expensive physics objects strength

---
{{define_cvar("r_showdebugrendertarget")}}
Set the debug render target to show, 0 == disable

---
{{define_cvar("fog_enable")}}
Enable fog

---
{{define_cvar("mat_wireframe")}}
0=Off, 1=Surface Wireframe, 2=Transparent Wireframe

---
{{define_cvar("mat_fullbright")}}
Debug rendering modes

---
{{define_cvar("mat_max_lighting_complexity")}}

---
{{define_cvar("mat_luxels")}}

---
{{define_cvar("mat_shadowmap_luxels")}}

---
{{define_cvar("mat_lpv_luxels")}}

---
{{define_cvar("r_drawskybox")}}
Render the 2d skybox.

---
{{define_cvar("r_size_cull_threshold_fade")}}
% above the screen size percentage where we will start fading out (==0 will disable fading).

---
{{define_cvar("r_size_cull_threshold")}}
Threshold of screen size percentage below which objects get culled

---
{{define_cvar("r_size_cull_threshold_shadow")}}
Threshold of shadow map size percentage below which objects get culled

---
{{define_cvar("r_drawblankworld")}}
Render blank instead of the game world

---
{{define_cvar("mat_show_distance_field")}}
0=Off, 1=Visualize trace from camera, 2=Visualize occlusion, 3=Visualize far field trace from camera

---
{{define_cvar("fog_override_enable")}}
Use fog_override convars instead of world fog data

---
{{define_cvar("fog_override_start")}}

---
{{define_cvar("fog_override_end")}}

---
{{define_cvar("fog_override_max_density")}}

---
{{define_cvar("fog_override_exponent")}}

---
{{define_cvar("r_dof_override")}}

---
{{define_cvar("r_dof_override_near_blurry")}}

---
{{define_cvar("r_dof_override_near_crisp")}}

---
{{define_cvar("r_dof_override_far_crisp")}}

---
{{define_cvar("r_dof_override_far_blurry")}}

---
{{define_cvar("r_dof_override_tilt_to_ground")}}

---
{{define_cvar("mat_shading_complexity")}}
Visualize shading complexity

---
{{define_cvar("mat_overdraw")}}
Visualize overdraw

---
{{define_cvar("tv_relay_hard_shutdown")}}

---
{{define_cvar("tv_secure_bypass")}}
Bypass secure challenge on TV port

---
{{define_cvar("tv_maxclients")}}
Maximum client number on SourceTV server.

---
{{define_cvar("tv_maxclients_relayreserved")}}
This number of relay client connections are reserved for SourceTV relays.

---
{{define_cvar("tv_update_hibernation_enabled")}}
Allow SourceTV to control server hibernation state.

---
{{define_cvar("tv_name")}}
SourceTV host name

---
{{define_cvar("tv_password")}}
SourceTV password for all clients of CSTV[0]

---
{{define_cvar("tv_password1")}}
SourceTV password for all clients of CSTV[1]. If empty, tv_password is used

---
{{define_cvar("tv_advertise_watchable")}}
GOTV advertises the match as watchable via game UI, clients watching via UI will not need to type password

---
{{define_cvar("tv_overridemaster")}}
Overrides the SourceTV master root address.

---
{{define_cvar("tv_dispatchmode")}}
Dispatch clients to relay proxies: 0=never, 1=if appropriate, 2=always

---
{{define_cvar("tv_debug")}}
SourceTV debug info.

---
{{define_cvar("tv_title")}}
Set title for SourceTV spectator UI

---
{{define_cvar("tv_relayvoice")}}
Relay voice data: 0=off, 1=on

---
{{define_cvar("tv_secret_code")}}
When enabled, this will use a uniquely generated server code to authenticate relay connections. This code is coordinated via the GC or some external means rather than by clients directly

---
{{define_cvar("tv_relay_secret_code")}}
When enabled, this will use a uniquely generated server code to authenticate relay to relay connections. This code is coordinated via the GC or some external means rather than by clients directly

---
{{define_cvar("tv_relay_quit_after_game")}}
Quit after a game has been relayed, do not hibernate

---
{{define_cvar("tv_relay_rate")}}
default rate for relays

---
{{define_cvar("spec_replay_leadup_time")}}
Replay time in seconds before the highlighted event

---
{{define_cvar("tv_threaded_merge_entity_deltas")}}
Enable SourceTV threading of delta merging

---
{{define_cvar("tv_broadcast_url")}}
URL of the broadcast relay

---
{{define_cvar("tv_broadcast_url1")}}
URL of the broadcast relay1

---
{{define_cvar("tv_autorecord")}}
Automatically records all games as SourceTV demos.

---
{{define_cvar("tv_broadcast")}}
Automatically broadcasts all games as GOTV demos through Steam.

---
{{define_cvar("tv_broadcast1")}}
Automatically broadcasts all games as GOTV[1] demos through Steam.

---
{{define_cvar("tv_extended_logging")}}

---
{{define_cvar("tv_window_size")}}
Specifies the number of seconds worth of frames that the tv replay system should keep in memory. Increasing this greatly increases the amount of memory consumed by the TV system

---
{{define_cvar("tv_enable_delta_frames")}}
Indicates whether or not the tv should use delta frames for storage of intermediate frames. This takes more CPU but significantly less memory.

---
{{define_cvar("tv_transmitall")}}
Transmit all entities (not only director view)

---
{{define_cvar("tv_deltacache")}}
Enable delta entity bit stream cache

---
{{define_cvar("tv_instant_replay_full_frame")}}
Send embedded full frames

---
{{define_cvar("tv_instant_replay_full_frame_time")}}
Seconds between full frame embeddeds

---
{{define_cvar("tv_instant_replay_full_frame_build_threaded")}}
Build the full frames on a seperate job thread

---
{{define_cvar("tv_record_immediate")}}
tv_record starting the moment tv_record was executed, not tv_delay earlier

---
{{define_cvar("r_drawpanorama")}}
Enable the rendering of panorama UI

---
{{define_cvar("input_downimpulsevalue")}}

---
{{define_cvar("input_upimpulsevalue")}}

---
{{define_cvar("input_filter_relative_analog_inputs")}}

---
{{define_cvar("bug_submitter_override")}}

---
{{define_cvar("r_skip_precache_validation_check")}}

---
{{define_cvar("sv_pause_on_console_open")}}
1 = Pause the game when pressing ~ to open the console. CTRL+~ opens the console without pause.

---
{{define_cvar("sv_unpause_on_console_close")}}
1 = Unpause the game when pressing ~ to close the console. 0 = Leave the game paused.

---
{{define_cvar("r_add_views_in_pre_output")}}

---
{{define_cvar("r_extra_render_frames")}}

---
{{define_cvar("con_enable")}}
Allows the console to be activated.

---
{{define_cvar("r_debug_draw_safe_area_insets")}}
Render safe area insets as wireframe.

---
{{define_cvar("input_forceuser")}}
Force user input to this split screen player.

---
{{define_cvar("mouse_disableinput")}}
Set to disable mouse input

---
{{define_cvar("input_button_code_is_scan_code_scd")}}
Bind keys based on keyboard position instead of key name

---
{{define_cvar("convars_echo_toggle_changes")}}
Echo to the console changes caused by toggling.

---
{{define_cvar("joy_axisx_relative")}}

---
{{define_cvar("joy_axisy_relative")}}

---
{{define_cvar("joy_axisz_relative")}}

---
{{define_cvar("joy_axisr_relative")}}

---
{{define_cvar("joy_axisu_relative")}}

---
{{define_cvar("joy_axisv_relative")}}

---
{{define_cvar("joy_axisx_deadzone")}}

---
{{define_cvar("joy_axisy_deadzone")}}

---
{{define_cvar("joy_axisz_deadzone")}}

---
{{define_cvar("joy_axisr_deadzone")}}

---
{{define_cvar("joy_axisu_deadzone")}}

---
{{define_cvar("joy_axisv_deadzone")}}

---
{{define_cvar("player0_using_joystick")}}

---
{{define_cvar("cl_usesocketsforloopback")}}
When connecting to local listen server (for example, using the 'map' command), default to loopback=false, which connects to '127.0.0.1' instead of 'loopback'.  This uses the network stack so that fake lag/loss can be simulated.

---
{{define_cvar("tv_enable_dynamic")}}
When enabled, changes in tv_enable convars cause immediate startup or shutdown of hltv server

---
{{define_cvar("tv_enable")}}
Activates SourceTV on server.

---
{{define_cvar("tv_enable1")}}
Activates SourceTV[1] on server.

---
{{define_cvar("clientport")}}
If non-zero, client binds port to specific address.  Usually you should leave this blank to use a different random system-assigned port for each connection.

---
{{define_cvar("hostport")}}
Host game server port

---
{{define_cvar("tv_port")}}
Host SourceTV[0] port

---
{{define_cvar("tv_port1")}}
Host SourceTV[1] port

---
{{define_cvar("r_vconsole_foregroundforcerender")}}
When VConsole is in the foreground, force all engine & tools to render

---
{{define_cvar("r_always_render_all_windows")}}
Always force all engine & tools to render

---
{{define_cvar("r_force_render_frame_count")}}
The number of frames to render when a

---
{{define_cvar("splitscreen_mode")}}

---
{{define_cvar("jpeg_quality")}}
Set jpeg screenshot quality. [1..100]

---
{{define_cvar("screenshot_subdir")}}
Set the screenshot directory.

---
{{define_cvar("screenshot_prefix")}}
Set the screenshot auto naming prefix.

---
{{define_cvar("screenshot_width")}}
Screenshot width. -1 for screen width.

---
{{define_cvar("screenshot_height")}}
Screenshot height. -1 for screen height.

---
{{define_cvar("cl_playback_screenshots")}}
Allows the client to playback screenshot and jpeg commands in demos.

---
{{define_cvar("voice_sequence_maximum_wait_time")}}
When receiving packets out of sequence, wait this many seconds for missing sequences to arrive

---
{{define_cvar("voice_always_sample_mic")}}
When enabled, open the voip audio input stream when the application launches.

---
{{define_cvar("snd_mute_losefocus")}}

---
{{define_cvar("voice_threshold_attack")}}
Amount of time we buffer outgoing audio to detect an onset.

---
{{define_cvar("voice_threshold_delay")}}
Amount of time the talker is silent before we infer that they are no longer talking.

---
{{define_cvar("voice_threshold_hold")}}
Amount of time after the talker starts talking we should keep listening regardless of how loud they are speaking.

---
{{define_cvar("voice_threshold_ramp_min_db")}}
A dB floor of when to stop transmitting packets, the volume between this and voice_threshold will still transmit packets to allow for volume ramping.

---
{{define_cvar("voice_threshold")}}
decibel threshold for how loud the talker's input signal is before we think they are talking.

---
{{define_cvar("reset_voice_on_input_stallout")}}
If true, resets the input device when there was a long enough hitch between callbacks.

---
{{define_cvar("voice_input_stallout")}}
Time before we consider a mic stalled out and need to reset it.

---
{{define_cvar("voice_in_process")}}

---
{{define_cvar("voice_noise_supression")}}

---
{{define_cvar("voice_bypass_noise_gate")}}

---
{{define_cvar("opus_encode_test_signal")}}

---
{{define_cvar("voice_loopback_no_networking")}}

---
{{define_cvar("voice_device_override")}}
Default device used for voice capture.

---
{{define_cvar("soundsystem_update_async")}}

---
{{define_cvar("host_readconfig_ignore_userconfig")}}
Whether we should ignore the user config file for reading/writing.

---
{{define_cvar("sv_mmqueue_reservation_timeout")}}
Time in seconds before mmqueue reservation expires.

---
{{define_cvar("sv_mmqueue_reservation_extended_timeout")}}
Extended time in seconds before mmqueue reservation expires.

---
{{define_cvar("spawngroup_ignore_timeouts")}}

---
{{define_cvar("sv_snapshot_unlimited")}}
For debugging, don't throw away old snapshots so that if you break in debugger (on remote client or server) it won't require an uncompressed update to resume.  You may run out of memory of course...

---
{{define_cvar("sv_timeout")}}
After this many seconds without a message from fully connected client, the client is dropped

---
{{define_cvar("spec_replay_enable")}}
Enable Killer Replay, requires hltv server running (0:off, 1:default, 2:force)

---
{{define_cvar("spec_replay_message_time")}}
How long to show the message about Killer Replay after death. The best setting is a bit shorter than spec_replay_autostart_delay + spec_replay_leadup_time + spec_replay_winddown_time

---
{{define_cvar("spec_replay_rate_limit")}}
Minimum allowable pause between replay requests in seconds

---
{{define_cvar("spec_replay_on_death")}}
When > 0, sets the mode whereas players see delayed replay, and are segregated into a domain of chat and voice separate from the alive players

---
{{define_cvar("replay_debug")}}

---
{{define_cvar("sv_max_unreliable_delta_size")}}
Maximum allowable entity delta size over unreliable delivery.

---
{{define_cvar("sv_disable_reliable_delta_retransmit")}}
Assume that a reliable entity delta will be ack'ed and send future deltas relative to the last reliable delta.

---
{{define_cvar("sv_maxclientframes")}}

---
{{define_cvar("sv_extra_client_connect_time")}}
Seconds after client connect during which extra frames are buffered to prevent non-delta'd update

---
{{define_cvar("sv_maxreplay")}}
Maximum replay time in seconds

---
{{define_cvar("sv_stressbots")}}
If set to 1, the server calculates data and fills packets to bots. Used for perf testing.

---
{{define_cvar("sv_sendtables")}}
Force full sendtable sending path.

---
{{define_cvar("ss_voice_hearpartner")}}
Route voice between splitscreen players on same system.

---
{{define_cvar("spec_replay_fullframe")}}
Send full frame on every hltv replay transition

---
{{define_cvar("net_async_clientconnect")}}
Enable async client connect optimization

---
{{define_cvar("sv_steamauth_enforce")}}
By default, player must maintain a reliable connection to Steam servers. When player Steam session drops, enforce it: 2 = instantly kick, 1 = kick at next spawn, 0 = do not kick.

---
{{define_cvar("sv_merge_changes_after_tick_with_calcdelta")}}
This fixes bugs where pure calcdelta is used due to recipient changing but it doesn't pick up a field change where the value was changed back to same value as the from snapshot even though the destination fields change list does note the change. Set to 2 to spew any changes merged in by this fix.

---
{{define_cvar("sv_dev_entitydeltapadding_min_size")}}
When encoding entity deltas, if the delta size is < N bytes, then shove in N dummy bytes.  This happens before sv_dev_entitydeltapadding_extra_min/sv_dev_entitydeltapadding_extra_max

---
{{define_cvar("sv_dev_entitydeltapadding_extra_min")}}
When encoding entity deltas, append on a random number of extra bytes.  This happens after sv_dev_entitydeltapadding_min_size.

---
{{define_cvar("sv_dev_entitydeltapadding_extra_max")}}
When encoding entity deltas, append on a random number of extra bytes.  This happens after sv_dev_entitydeltapadding_min_size.

---
{{define_cvar("sv_enable_donttransmit")}}
When encoding entity deltas, instead of unreliably deducing explicit deletions, actually send list of existing but not networked entities (dont_transmit list) to each client.

---
{{define_cvar("sv_ents_write_alarm")}}
Print callstack every time CNetworkGameServerBase::WriteEntityUpdate takes more than this amount of milliseconds

---
{{define_cvar("sv_filterban")}}
Set packet filtering by IP mode

---
{{define_cvar("sv_banid_enabled")}}
Whether server supports banid command

---
{{define_cvar("sv_banid_dev_enabled")}}

---
{{define_cvar("sv_max_queries_sec")}}
Maximum queries per second to respond to from a single IP address.

---
{{define_cvar("sv_max_queries_window")}}
Window over which to average queries per second averages.

---
{{define_cvar("sv_max_queries_sec_global")}}
Maximum queries per second to respond to from anywhere.

---
{{define_cvar("sv_logblocks")}}
If true when log when a query is blocked (can cause very large log files)

---
{{define_cvar("sv_logsdir")}}
Folder in the game directory where server logs will be stored.

---
{{define_cvar("sv_logfile")}}
Log server information in the log file.

---
{{define_cvar("sv_logflush")}}
Flush the log file to disk on each write (slow).

---
{{define_cvar("sv_logecho")}}
Echo log information to the console.

---
{{define_cvar("sv_log_onefile")}}
Log server information to only one file.

---
{{define_cvar("sv_logbans")}}
Log server bans in the server logs.

---
{{define_cvar("sv_parallel_packentities")}}
Set to 1 to use threaded snapshot sending on listen servers, 2 for dedicated servers.

---
{{define_cvar("sv_networkvar_validate")}}
Validate each StateChanged against known offsets.

---
{{define_cvar("sv_enable_delta_packing")}}
When enabled, this allows for entity packing to use the property changes for building up the data. This is many times faster, but can be disabled for error checking.

---
{{define_cvar("sv_usenetworkvars")}}
Use networkvar system.

---
{{define_cvar("sv_networkvar_perfieldtracking")}}
Track individual field offset changes, rather than a single dirty flag for the whole entity.

---
{{define_cvar("sv_enable_alternate_baselines")}}
Allow alternate baseline system, set to 2 for debugging spew.

---
{{define_cvar("sv_enable_pvs_vis_bits")}}

---
{{define_cvar("rcon_password")}}
remote console password.

---
{{define_cvar("rcon_connected_clients_allow")}}
Allow clients to use rcon commands on server.

---
{{define_cvar("vconsole_rcon_server_details")}}
when non-empty allows for easy vconsole connection to the dedicated server.

---
{{define_cvar("sv_rcon_banpenalty")}}
Number of minutes to ban users who fail rcon authentication

---
{{define_cvar("sv_rcon_maxfailures")}}
Max number of times a user can fail rcon authentication before being banned

---
{{define_cvar("sv_rcon_minfailures")}}
Number of times a user can fail rcon authentication in sv_rcon_minfailuretime before being banned

---
{{define_cvar("sv_rcon_minfailuretime")}}
Number of seconds to track failed rcon authentications

---
{{define_cvar("sv_rcon_log")}}
Enable/disable rcon logging.

---
{{define_cvar("closecaption")}}
Enable close captioning.

---
{{define_cvar("hostname")}}
Hostname for server.

---
{{define_cvar("hostname_in_client_status")}}
Show server hostname in client status.

---
{{define_cvar("developer")}}
Set developer message level.

---
{{define_cvar("violence_hblood")}}
Draw human blood

---
{{define_cvar("violence_hgibs")}}
Show human gib entities

---
{{define_cvar("violence_ablood")}}
Draw alien blood

---
{{define_cvar("violence_agibs")}}
Show alien gib entities

---
{{define_cvar("sv_unlockedchapters")}}
Highest unlocked game chapter.

---
{{define_cvar("name")}}

---
{{define_cvar("mem_test_quiet")}}
Don't print stats when memtesting

---
{{define_cvar("mem_test_each_frame")}}
Run heap check at end of every frame

---
{{define_cvar("mem_test_every_n_seconds")}}
Run heap check at a specified interval

---
{{define_cvar("engine_sse42")}}
turn on sse4.2 optimizations in the engine

---
{{define_cvar("sv_temp_baseline_string_table_buffer_size")}}
Buffer size for writing string table baselines

---
{{define_cvar("tv_playcast_delay_resync")}}
To alleviate intermittent network connectivity problems, this is the number of seconds to wait before actually re-syncing the stream after failure

---
{{define_cvar("tv_playcast_showerrors")}}
Set to display headers upon error (e.g. "CF-Ray,CF-Cache-Status,Body" )

---
{{define_cvar("tv_playcast_origin_auth")}}
Get request X-Origin-Auth string

---
{{define_cvar("tv_playcast_max_rcvage")}}

---
{{define_cvar("tv_playcast_max_rtdelay")}}

---
{{define_cvar("tv_playcast_delay_prediction")}}

---
{{define_cvar("tv_playcast_retry_timeout")}}
In case of intermittent network problems, how long should playcast retry fragment retrieval before resorting to resync

---
{{define_cvar("tv_broadcast_keyframe_interval")}}
The frequency, in seconds, of sending keyframes and delta fragments to the broadcast relay server

---
{{define_cvar("tv_broadcast_keyframe_interval1")}}
The frequency, in seconds, of sending keyframes and delta fragments to the broadcast1 relay server

---
{{define_cvar("tv_broadcast_startup_resend_interval")}}
The interval, in seconds, of re-sending startup data to the broadcast relay server (useful in case relay crashes, restarts or startup data http request fails)

---
{{define_cvar("tv_broadcast_max_requests")}}
Max number of broadcast http requests in flight. If there is a network issue, the requests may start piling up, degrading server performance. If more than the specified number of requests are in flight, the new requests are dropped.

---
{{define_cvar("tv_broadcast_max_requests1")}}
Max number of broadcast1 http requests in flight. If there is a network issue, the requests may start piling up, degrading server performance. If more than the specified number of requests are in flight, the new requests are dropped.

---
{{define_cvar("tv_broadcast_drop_fragments")}}
Drop every Nth fragment

---
{{define_cvar("tv_broadcast_terminate")}}
Terminate every broadcast with a stop command

---
{{define_cvar("tv_broadcast_origin_auth")}}
X-Origin-Auth header of the broadcast POSTs

---
{{define_cvar("tv_broadcast_origin_auth1")}}
X-Origin-Auth header of the broadcast1 POSTs

---
{{define_cvar("tv_broadcast_origin_delay")}}
Injection delay request for CDN rebroadcast frameworks, seconds

---
{{define_cvar("tv_maxrate")}}
Max SourceTV spectator bandwidth rate allowed, 0 == unlimited

---
{{define_cvar("tv_rate_multiplier")}}
Multiply requested rate by this value to adjust Dota TV send rate

---
{{define_cvar("tv_relaypassword")}}
SourceTV password for relay proxies

---
{{define_cvar("tv_chattimelimit")}}
Limits spectators to chat only every n seconds

---
{{define_cvar("tv_chatgroupsize")}}
Set the default chat group size

---
{{define_cvar("tv_grouprelaydatareliable")}}
When enabled, this will collect all information for relay sending into a single datagram to ensure that the data stays together through a potentially large number of relays

---
{{define_cvar("tv_grouprelaydataunreliable")}}
When enabled, this will collect all information for relay sending into a single datagram to ensure that the data stays together through a potentially large number of relays

---
{{define_cvar("tv_grouprelaydatavoice")}}
Similar to tv_grouprelaydata, but controls whether or not the voice channels should be routed into the grouped data for the relays

---
{{define_cvar("tv_autoretry")}}
Relay proxies retry connection after network timeout

---
{{define_cvar("tv_timeout")}}
SourceTV connection timeout in seconds.

---
{{define_cvar("demo_writefullupdate_rate")}}
Interval time in seconds to write full updates to demo.

---
{{define_cvar("sv_replaysdir")}}
Directory to store replays in

---
{{define_cvar("tv_demo_starttick")}}

---
{{define_cvar("entity_log_load_unserialize")}}
Output unserialization of entities on map load. 0 - off, 1 - client/server, 2 - server, 3 - client

---
{{define_cvar("demo_recordcommands")}}
Record commands typed at console into .dem files.

---
{{define_cvar("demo_quitafterplayback")}}
Quits game after demo playback.

---
{{define_cvar("demo_pauseatservertick")}}
Pauses demo playback at server tick

---
{{define_cvar("demo_usefastgoto")}}
Use fast frame skipping when available for demo_goto commands.

---
{{define_cvar("timedemo_start")}}
Starts timedemo on given tick.

---
{{define_cvar("timedemo_end")}}
Ends timedemo on given tick.

---
{{define_cvar("demo_flush")}}
Flush writing the demo file every network update

---
{{define_cvar("demo_allow_game_mismatch")}}
Allow playback of demo even if game directories are not matched [may crash or fail to load].

---
{{define_cvar("demo_debug")}}
Turn on demo debug spew.

---
{{define_cvar("cl_showdemooverlay")}}
How often to flash demo recording/playback overlay (0 - disable overlay, -1 - show always)

---
{{define_cvar("cl_flushentitypacket")}}
For debugging. Force the engine to flush an entity packet.

---
{{define_cvar("cl_parallel_readpacketentities")}}
Set to 1 to use threading snapshot reading (if game supports and server is sending bitcounts).

---
{{define_cvar("cl_parallel_readpacketentities_threshold")}}
Use parallel processing of snapshot reading if above this many entries.

---
{{define_cvar("instant_replay")}}
Enable instant replay recording.

---
{{define_cvar("instant_replay_history_limit")}}
Maximum amount of minutes to save history (0 is unlimited).

---
{{define_cvar("instant_replay_history_limit_low")}}
Maximum amount of minutes to save history on low memory (32 bit) systems (0 is unlimited).

---
{{define_cvar("rcon_address")}}
Address of remote server if sending unconnected rcon commands (format x.x.x.x:p) 

---
{{define_cvar("cl_resend")}}
Delay in seconds before the client will resend the 'connect' attempt

---
{{define_cvar("cl_connectionretrytime_p2p")}}
Number of seconds over which to spread retry attempts for P2P.

---
{{define_cvar("password")}}
Current server access password

---
{{define_cvar("cl_timeout")}}
After this many seconds without receiving a packet from the server, the client will disconnect itself

---
{{define_cvar("cl_disconnect_soundevent")}}
This soundevent is called to stop the desired soundevents when the game is disconnected.

---
{{define_cvar("cl_disconnect_voice_fade")}}
This is a fade of current voices that is called when the game is disconnected. -1.f for no fade on disconnect

---
{{define_cvar("tv_nochat")}}
Don't receive chat messages from other SourceTV spectators

---
{{define_cvar("cl_ignorepackets")}}
Force client to ignore packets (for debugging).

---
{{define_cvar("spec_replay_rate_base")}}
Base time scale of Killer Replay.Experimental.

---
{{define_cvar("rate")}}
Min bytes/sec the host can receive data

---
{{define_cvar("cl_usercmd_dbg")}}
show usercmd payload sizing info for packets with more than this many usercmds

---
{{define_cvar("cl_usercmd_max_per_movemsg ")}}
max number of CUserCmds to send in one client move message

---
{{define_cvar("cl_usercmd_showsize")}}

---
{{define_cvar("cl_force_next_signon_to_reset")}}

---
{{define_cvar("cl_clockdbg")}}

---
{{define_cvar("cl_clock_correction")}}
Enable/disable clock correction on the client.

---
{{define_cvar("cl_clockdrift_max_ticks")}}
Maximum number of ticks the clock is allowed to drift before the client snaps its clock to the server's.

---
{{define_cvar("cl_clock_recvmargin_desired")}}
Clock sync will try to maintain N ms margin between tick arrival and polling network.  The effective value is the sum of this and the time implied by cl_clock_buffer_ticks

---
{{define_cvar("cl_clock_recvmargin_minsamples_speedup")}}
Clock sync will not speed up unless we have N seconds of indicating samples

---
{{define_cvar("cl_clock_recvmargin_minsamples_slowdown")}}
Clock sync will not slow down unless we have N indicating samples

---
{{define_cvar("cl_clock_recvmargin_window")}}
Clock sync will use past N seconds

---
{{define_cvar("cl_clock_recvmargin_timeconstant_speedup")}}
Clock sync will remove 63.2% of the error in N seconds

---
{{define_cvar("cl_clock_recvmargin_timeconstant_slowdown")}}
Clock sync will remove 63.2% of the error in N seconds

---
{{define_cvar("cl_clock_recvmargin_adjust_limit_speedup")}}
Clock sync will not speed up time faster than N%

---
{{define_cvar("cl_clock_recvmargin_adjust_limit_slowdown")}}
Clock sync will not slow down time slower than N%

---
{{define_cvar("cl_clock_recvmargin_spew_interval")}}

---
{{define_cvar("cl_clock_buffer_ticks")}}
Clock sync will try to maintain an additional margin of N ticks.  This is intended to smooth over packet loss, and is a replacement for cl_interp_ratio / cl_interp.  This value is simply added to cl_clock_recvmargin_desired

---
{{define_cvar("cl_tickpacket_recvmargin_desired")}}
Recvmargin-based usercommand pacing will try to maintain N ms margin between user command arriving at the server and the server needing that user command.  See also cl_tickpacket_desired_queuelength.

---
{{define_cvar("cl_tickpacket_recvmargin_minsamples")}}
Recvmargin-based usercommand pacing will not take action unless we have N samples

---
{{define_cvar("cl_tickpacket_recvmargin_window")}}
Recvmargin-based usercommand pacing will use past N seconds

---
{{define_cvar("cl_tickpacket_recvmargin_timeconstant")}}
Recvmargin-based usercommand pacing will remove 63.2% of the error in N seconds

---
{{define_cvar("cl_tickpacket_recvmargin_adjust_limit")}}
Recvmargin-based usercommand pacing will not speed up or slow down command pacing by more than N% compared to realtime

---
{{define_cvar("cl_tickpacket_recvmargin_spew_interval")}}

---
{{define_cvar("cl_tickpacket_desired_queuelength")}}
This value, multiplied by the tick interval, is added to cl_tickpacket_recvmargin_desired to obtain the effective desired recv margin.

---
{{define_cvar("sv_cq_min_queue")}}
Server min buffer size.

---
{{define_cvar("cl_cq_min_queue")}}
Used by the client to inform the server of their desired queue length.  Derived from cl_tickpacket_recvmargin_desired and cl_tickpacket_desired_queuelength

---
{{define_cvar("cl_ticks_warning_level")}}
Print a message about problems with ticks and interpolation.  0=never, 1=warnings, 2=all, even if hidden by interpolation

---
{{define_cvar("cq_buffer_bloat_msecs_max")}}
Server will not allow the client to buffer up more than N ms of commands.

---
{{define_cvar("cl_jitter_bad_threshold_up")}}
When upstream packet jitter in a frame exceeds this threshold (ms), the frame is considered to have 'irregular delivery'.  This is a derived value and should not be modified manually

---
{{define_cvar("r_aspectratio")}}

---
{{define_cvar("cl_interpolate")}}
Interpolate entities on the client.

---
{{define_cvar("cl_cache_sendtable")}}
Cache sendtables

---
{{define_cvar("cl_sendtable_cache_filename")}}
Send tables cache file

---
{{define_cvar("cl_spawngroup_spewresources")}}
Spew all manifest add/updates.

---
{{define_cvar("cl_log_tick")}}
Log when a tick is received


---
{{define_cvar("cl_log_tick_skips")}}
Log when the tick delta >= this

---
{{define_cvar("cl_spawngroup_log")}}
Dump the contents of the next spawngroup manifest to file.

---
{{define_cvar("cl_debug_overlays_broadcast")}}
Render debug overlays from server.

---
{{define_cvar("sv_pausable_dev")}}
Whether listen server is pausable when running -dev and playing solo against bots

---
{{define_cvar("sv_pausable_dev_ds")}}
Whether dedicated server is pausable when running -dev and playing solo against bots

---
{{define_cvar("sv_pure_kick_clients")}}
If set to 1, the server will kick clients with mismatching files. Otherwise, it will issue a warning to the client.

---
{{define_cvar("sv_pure_trace")}}
If set to 1, the server will print a message whenever a client is verifying a CRC for a file.

---
{{define_cvar("sv_cheats")}}
Allow cheats on server

---
{{define_cvar("sv_lan")}}
Server is a lan server ( no heartbeat, no authentication, no non-class C addresses )

---
{{define_cvar("sv_pausable")}}
Is the server pausable.

---
{{define_cvar("sv_voicecodec")}}
Specifies which voice codec DLL to use in a game. Set to the name of the DLL without the extension.

---
{{define_cvar("sv_pvs_max_distance")}}
if set, adds a maximum range to PVS/PAS checks

---
{{define_cvar("sv_parallel_sendsnapshot")}}
0: run all send jobs on main thread; 1: send jobs run asynchronously (except on dedicated server); 2: send jobs asynchronously; 3: send jobs run in parallel but block to not overlap the next tick; 4: main server clients' send jobs run in parallel, then HLTV server jobs; this approximately matches pre-async profile for a single HLTV server configuration

---
{{define_cvar("sv_skyname")}}
Current name of the skybox texture

---
{{define_cvar("sv_debug_overlays_bandwidth")}}
Broadcast server debug overlays traffic

---
{{define_cvar("sv_debug_overlays_broadcast")}}
Broadcast server debug overlays

---
{{define_cvar("sv_voiceenable")}}

---
{{define_cvar("voice_debugfeedbackfrom")}}

---
{{define_cvar("sv_reserve_slots_for_reconnecting_players_kick_prior")}}
Kick a previously connected player with the same steamID if a replacement comes along

---
{{define_cvar("sv_memlimit")}}
If set, whenever a game ends, if the total memory used by the server is greater than this # of megabytes, the server will exit.

---
{{define_cvar("sv_hibernate_postgame_delay")}}

---
{{define_cvar("sv_hibernate_when_empty")}}
Puts the server into extremely low CPU usage mode when no clients connected

---
{{define_cvar("sv_shutdown_immediately_on_request")}}
The server will always shutdown on receiving the shutdown request, even if not hibernating

---
{{define_cvar("sv_search_key")}}

---
{{define_cvar("sv_region")}}
The region of the world to report this server in.

---
{{define_cvar("sv_cluster")}}
Data center cluster this server lives in.

---
{{define_cvar("sv_instancebaselines")}}
Enable instanced baselines. Saves network overhead.

---
{{define_cvar("sv_stats")}}
Collect CPU usage stats

---
{{define_cvar("sv_password")}}
Server password for entry into multiplayer games

---
{{define_cvar("sv_tags")}}
Server tags. Used to provide extra information to clients when they're browsing for servers. Separate tags with a comma.

---
{{define_cvar("sv_visiblemaxplayers")}}
Overrides the max players reported to prospective clients

---
{{define_cvar("sv_steamgroup")}}
The ID of the steam group that this server belongs to. You can find your group's ID on the admin profile page in the steam community.

---
{{define_cvar("sv_steamgroup_exclusive")}}
If set, only members of Steam group will be able to join the server when it's empty, public people will be able to join the server only if it has players.

---
{{define_cvar("sv_hosting_lobby")}}

---
{{define_cvar("sv_mmqueue_reservation")}}
Server queue reservation

---
{{define_cvar("fs_async_threads")}}
Number of IO threads in async filesystem (-1 == auto)

---
{{define_cvar("fs_report_async_io")}}

---
{{define_cvar("fs_report_sync_opens")}}
0:Off, 1:Always, 2:Not during load

---
{{define_cvar("fs_report_long_reads")}}
0:Off, 1:All (for tracking accumulated duplicate read times), >1:Microsecond threashold

---
{{define_cvar("fs_warning_mode")}}
0:Off, 1:Warn main thread, 2:Warn other threads

---
{{define_cvar("fs_fake_read_delay_ms")}}
Add N ms of delay to every low-level read operation, to simulate a slow disk

---
{{define_cvar("filesystem_buffer_size")}}
Size of per file buffers. 0 for none

---
{{define_cvar("filesystem_unbuffered_io")}}

---
{{define_cvar("filesystem_native")}}
Use native FS or STDIO

---
{{define_cvar("filesystem_max_stdio_read")}}

---
{{define_cvar("filesystem_report_buffered_io")}}

---
{{define_cvar("filesystem_fake_latency")}}

---
{{define_cvar("cl_cursor_scale")}}
Cursor size scaling factor.

---
{{define_cvar("cl_auto_cursor_scale")}}
Automatic cursor size scaling.

---
{{define_cvar("cl_input_enable_raw_keyboard")}}
Enable raw keyboard input

---
{{define_cvar("cl_joystick_enabled")}}
Enable joystick input

---
{{define_cvar("joy_axisbutton_threshold")}}
Analog axis range before a button press is registered.

---
{{define_cvar("resourcesystem_multiframe_finalize_time_msec")}}
Max time to spend finalizing resources per frame in miliseconds.

---
{{define_cvar("d3d_max_feature_level")}}
Report the maximum D3D feature level available.

---
{{define_cvar("r_low_latency")}}
NVIDIA Low Latency/AMD Anti-Lag 2 (0 = off, 1 = on, 2 = NV-only, on + boost)

---
{{define_cvar("r_low_latency_trigger_flash")}}
NVIDIA Low Latency Trigger Flash

---
{{define_cvar("r_suppress_redundant_state_changes")}}

---
{{define_cvar("r_draw_first_tri_only")}}

---
{{define_cvar("r_draw_instances")}}

---
{{define_cvar("r_texturefilteringquality")}}
0: Bilinear, 1: Trilinear, 2: Aniso 2x, 3: Aniso 4x, 4: Aniso 8x, 5: Aniso 16x

---
{{define_cvar("r_fullscreen_gamma")}}
Screen Gamma (only in fullscreen modes)

---
{{define_cvar("r_wait_on_present")}}

---
{{define_cvar("r_async_shader_compile_notify_frequency")}}

---
{{define_cvar("r_flush_on_pooled_ib_resize")}}

---
{{define_cvar("r_multigpu_num_gpus_found")}}

---
{{define_cvar("r_multigpu_num_gpus_used")}}

---
{{define_cvar("r_dx11_software_cmd_lists")}}
Enable Software Command lists for DX11 (Avoid using deferred contexts)

---
{{define_cvar("r_use_memory_budget_model")}}
Use a model of GPU memory use to determine budget rather than querying the OS.

---
{{define_cvar("r_renderdoc_open_captures")}}

---
{{define_cvar("r_renderdoc_validation_error_capture_limit")}}

---
{{define_cvar("r_timestamp_query_multiplier")}}
Set the TIMESTAMP query cycle multiplier, for drivers that lie

---
{{define_cvar("r_pipeline_stats_present_flush")}}
Experimental: Set to 1 to enable full GPU pipeline flushing after each present.

---
{{define_cvar("r_pipeline_stats_command_flush")}}
Experimental: Set to 1 to enable full GPU pipeline flushing after each command list.

---
{{define_cvar("r_pipeline_stats_use_flush_api")}}
Experimental: Set to 1 to use the ID3D11DeviceContext11::Flush() to flush the GPU pipeline instead of queries.

---
{{define_cvar("r_pipeline_stats_flush_before_sleeping")}}
Experimental: Set to 1 to enable GPU pipeline flushes right before the render thread sleeps to wait for more work.

---
{{define_cvar("r_frame_sync_enable")}}

---
{{define_cvar("r_force_no_present")}}
Force the render device to not present frames.

---
{{define_cvar("r_legacy_vsync")}}
Use legacy vsync mode -- for testing for a couple user machines.

---
{{define_cvar("multigpu_skip_transfers")}}

---
{{define_cvar("multigpu_skip_semaphores")}}

---
{{define_cvar("r_texture_pool_size")}}
Total size of the texture pool in MB

---
{{define_cvar("r_texture_stream_mip_bias")}}
Biases the mip level the texture streaming system choses to stream for each texture.

---
{{define_cvar("r_max_texture_pool_size")}}
Upper limit on texture pool size.

---
{{define_cvar("r_texture_nonstreaming_load")}}
Allow immediately loading mips of textures (when possible) when their headers are loaded, saving IO & reducing latency.

---
{{define_cvar("r_texture_hookup_uses_threadpool")}}
Async Texture hookup uses its own threadpool instead of the global pool.

---
{{define_cvar("r_texture_stream_max_resolution")}}
Maximum resolution for top mip level in streaming textures

---
{{define_cvar("r_texture_stream_resolution_bias")}}

---
{{define_cvar("r_validate_texture_streaming")}}
Dumps state of texture streaming at the next frame boundary.

---
{{define_cvar("r_texture_eager_eviction")}}

---
{{define_cvar("r_texture_stream_throttle_amount")}}

---
{{define_cvar("r_texture_stream_throttle_count")}}

---
{{define_cvar("r_texture_stream_throttle_count_over_budget")}}

---
{{define_cvar("r_texture_streamout_unthrottle_ms")}}
After hitting throttling limits for streamout, allow it to continue up to this number of milliseconds.

---
{{define_cvar("r_texture_streaming_timesliced")}}

---
{{define_cvar("r_texture_budget_dynamic")}}
Dynamically adjust texture streaming budget based on GPU memory usage.

---
{{define_cvar("r_texture_budget_update_period")}}
Time (in seconds) between updating texture memory budget.

---
{{define_cvar("r_texture_budget_threshold")}}
Reduce texture memory pool size when this percentage of the budget is full.

---
{{define_cvar("r_texture_pool_reduce_rate")}}
Reduce texture memory pool size by this many MB / s when over budget.

---
{{define_cvar("r_texture_pool_increase_rate")}}
Increase texture memory pool size by this many MB / s when under budget.

---
{{define_cvar("r_texture_stream_resolution_bias_update_period")}}

---
{{define_cvar("r_texture_stream_resolution_bias_increase_rate")}}

---
{{define_cvar("r_texture_stream_resolution_bias_decrease_rate")}}

---
{{define_cvar("r_texture_stream_resolution_bias_min")}}

---
{{define_cvar("mat_shader_cache")}}

---
{{define_cvar("mat_warn_bad_modes")}}

---
{{define_cvar("mat_assert_on_error_shader_use")}}

---
{{define_cvar("mat_hide_error_shader")}}

---
{{define_cvar("mat_skip_static_const_eval")}}

---
{{define_cvar("mat_shading_complexity_color")}}

---
{{define_cvar("mat_shading_complexity_max_instruction_count")}}

---
{{define_cvar("mat_shading_complexity_max_register_count")}}

---
{{define_cvar("mat_overdraw_color")}}

---
{{define_cvar("font_show_glyph_miss")}}

---
{{define_cvar("mat_colorcorrection")}}

---
{{define_cvar("mat_viewportscale")}}
Scale down the main viewport (to reduce GPU impact on CPU profiling)

---
{{define_cvar("panorama_disable_blur")}}

---
{{define_cvar("panorama_disable_box_shadow")}}

---
{{define_cvar("panorama_disable_render_callbacks")}}

---
{{define_cvar("panorama_disable_draw_fancy_quad")}}

---
{{define_cvar("panorama_disable_layer_clear")}}

---
{{define_cvar("panorama_disable_draw_text")}}

---
{{define_cvar("panorama_force_text_shadow_strength")}}

---
{{define_cvar("panorama_disable_draw_text_shadow")}}

---
{{define_cvar("panorama_disable_layer_cache")}}

---
{{define_cvar("panorama_use_backbuffer_directly")}}

---
{{define_cvar("panorama_highlight_composition_layers")}}

---
{{define_cvar("panorama_highlight_slow_operations")}}

---
{{define_cvar("panorama_highlight_bad_opacity_masks")}}

---
{{define_cvar("panorama_stats_log_time")}}

---
{{define_cvar("panorama_min_comp_layer_cache_cost")}}

---
{{define_cvar("panorama_comp_layer_lru_lifetime")}}

---
{{define_cvar("panorama_command_reordering")}}

---
{{define_cvar("panorama_composition_atlas")}}

---
{{define_cvar("panorama_temp_comp_layer_min_dimension")}}

---
{{define_cvar("panorama_disable_render_target_cache")}}

---
{{define_cvar("panorama_render_target_cache_max_size")}}

---
{{define_cvar("panorama_dash_len")}}

---
{{define_cvar("panorama_dash_gap_ratio")}}

---
{{define_cvar("snd_ui_spatialization_spread")}}

---
{{define_cvar("snd_ui_positional")}}

---
{{define_cvar("panorama_spew_async_event_substring")}}
If non-empty, print debug info about async event queue and dispatch behavior for events containing the substring.

---
{{define_cvar("panorama_js_minidumps")}}
Enable sending minidumps on JS Exceptions.

---
{{define_cvar("panorama_script_cache_enabled")}}
Enable script caching to speed up recompiling scripts multiple times.

---
{{define_cvar("panorama_max_fps")}}

---
{{define_cvar("panorama_max_overlay_fps")}}

---
{{define_cvar("panorama_max_oof_overlay_up_fps")}}

---
{{define_cvar("panorama_large_dispatch_event_queue")}}

---
{{define_cvar("panorama_reload_animations")}}

---
{{define_cvar("panorama_debug_overlay_opacity_min")}}

---
{{define_cvar("panorama_debug_overlay_opacity_max")}}

---
{{define_cvar("panorama_debug_overlay_opacity")}}

---
{{define_cvar("panorama_cache_command_list_repaint_threshold")}}

---
{{define_cvar("panorama_cache_command_list_size_threshold")}}

---
{{define_cvar("panorama_disallow_hover_styles")}}

---
{{define_cvar("panorama_debug_ready_for_display")}}

---
{{define_cvar("panorama_style_flag_force_invalidate")}}
Force style invalidation of the entire panel subtree when adding / removing style flags.

---
{{define_cvar("panorama_classes_force_invalidate")}}
Force style invalidation of the entire panel subtree when adding / removing classes.

---
{{define_cvar("panorama_assert_loading_panel_type")}}
Force style invalidation of the entire panel subtree when adding / removing classes.

---
{{define_cvar("panorama_show_fps")}}

---
{{define_cvar("panorama_show_fps_scale")}}

---
{{define_cvar("panorama_clear_frames_on_device_restore")}}

---
{{define_cvar("panorama_disable_descendant_filtering")}}
Disable descendant selector filtering

---
{{define_cvar("panorama_suspend_paint")}}

---
{{define_cvar("panorama_enable_secondary_layout_pass")}}

---
{{define_cvar("panorama_joystick_enabled")}}
Enable panorama joystick input

---
{{define_cvar("panorama_joystick_axis_repeat_interval_start")}}

---
{{define_cvar("panorama_joystick_axis_repeat_interval_end")}}

---
{{define_cvar("panorama_joystick_axis_repeat_curve_time")}}

---
{{define_cvar("panorama_joystick_button_repeat_interval_start")}}

---
{{define_cvar("panorama_joystick_button_repeat_interval_end")}}

---
{{define_cvar("panorama_joystick_button_repeat_curve_time")}}

---
{{define_cvar("panorama_dragscroll_affordance")}}
Minimum mouse movement in pixels before a move is treated as a drag scroll

---
{{define_cvar("panorama_dragscroll_mintime")}}
Minimum time that the mouse button must be down before a move is treated as a drag scroll

---
{{define_cvar("panorama_dragscroll_velocitymultiplier")}}
Multiplier for flick velocity off of actual measured velocity

---
{{define_cvar("panorama_force_active_controller_type")}}

---
{{define_cvar("panorama_spew_layout_invalidates")}}

---
{{define_cvar("panorama_transition_time_factor")}}
A float representing a scale factor for transitions. 1.0 is normal, 2.0 would be twice as fast as normal, 0.5 half as fast

---
{{define_cvar("panorama_max_text_shadow_strength")}}

---
{{define_cvar("panorama_allow_transitions")}}

---
{{define_cvar("panorama_2d_translate_no_comp_layer")}}

---
{{define_cvar("panorama_might_scroll_no_comp_layer")}}

---
{{define_cvar("panorama_box_shadow_no_comp_layer")}}

---
{{define_cvar("panorama_simple_borders_no_comp_layer")}}

---
{{define_cvar("panorama_allow_texture_composition_layer_fast_path")}}

---
{{define_cvar("panorama_transforms_no_comp_layer")}}

---
{{define_cvar("panorama_transform_parents_no_layer_for_perspective")}}

---
{{define_cvar("panorama_hsbc_through_fast_path")}}

---
{{define_cvar("panorama_track_render_commands")}}

---
{{define_cvar("lua_assert_on_error")}}

---
{{define_cvar("lua_shipping_assert_on_error")}}

---
{{define_cvar("net_max_polymorphic_spew")}}
Max polymorphic variants to spew when spewing a flattened serializer.

---
{{define_cvar("net_use_delta_property_fastpath")}}

---
{{define_cvar("net_culloptimization")}}
Enable optimization of slow path that makes HLTV CPU consumption high in AnimGraph-using mods. Will switch to this on by default soon.

---
{{define_cvar("net_filelogging")}}
Log packets to files

---
{{define_cvar("net_qosinterval_spew")}}
Spew QoS interval data as we gather it

---
{{define_cvar("net_qospacketloss_percentage_threshold")}}
Spew a warning if packet loss percentage is above this threshold

---
{{define_cvar("net_log_processing")}}
Log network processing

---
{{define_cvar("net_use_packet_compression")}}
Compress network traffic

---
{{define_cvar("net_showudp")}}
Dump UDP packets summary to console

---
{{define_cvar("net_showudp_remoteonly")}}
Dump non-loopback udp only

---
{{define_cvar("net_showmsg")}}
Show incoming message: <0|1|2|name> where 1 == all and 2 == all except net_NOP

---
{{define_cvar("net_showreliable")}}
Like net_showmsg, but only spew reliable messages

---
{{define_cvar("net_showpeaks")}}
Show messages for large packets only: <size>

---
{{define_cvar("net_showdrop")}}
Show dropped packets in console

---
{{define_cvar("net_compresspackets_minsize")}}
Don't bother compressing packets below this size.

---
{{define_cvar("net_restrict_showmsg_socket")}}
If set, only net_showmsg spew for data inbound on this socket name e.g. client, server, etc.

---
{{define_cvar("net_max_message_process_count")}}
Maximum number of messages to process from a client in a single frame (0 == no limit).

---
{{define_cvar("net_max_message_queue_size")}}
Maximum number of messages to allow waiting in queue after processing; exceeding this disconnects the client. 0 == no limit

---
{{define_cvar("net_detailed_canpacket_log")}}

---
{{define_cvar("net_showoob")}}
Show connectionless UDP traffic.

---
{{define_cvar("ip")}}
Overrides IP for multihomed hosts

---
{{define_cvar("hostip")}}
Host game server ip

---
{{define_cvar("net_public_adr")}}
For servers behind NAT/DHCP meant to be exposed to the public internet, this is the public facing ip address string: ("x.x.x.x" )

---
{{define_cvar("net_p2p_listen_dedicated")}}
Should dedicated server listen for new-style P2P?

---
{{define_cvar("net_limit_sv_recvbuffer_kb")}}
Server will not buffer more than N kb from connected clients

---
{{define_cvar("net_limit_sv_recvbuffer_msg")}}
Server will not buffer more than N messages from connected clients

---
{{define_cvar("net_limit_sv_recv_max_message_size_kb")}}
Server will reject message larger than N kb

---
{{define_cvar("net_limit_sv_recv_segments_per_packet")}}
Server will reject packets with more than N segments

---
{{define_cvar("net_fs_showindirections")}}

---
{{define_cvar("animgraph_force_full_network_updates")}}

---
{{define_cvar("animgraph_enable_dirty_netvar_optimization")}}

---
{{define_cvar("animgraph_verify_dirty_netvar_optimization")}}

---
{{define_cvar("animgraph_footlock_trace_ground_enabled")}}
Convar for toggling foot lock ground tracking.

---
{{define_cvar("animgraph_footlock_calculate_tilt")}}

---
{{define_cvar("animgraph_footlock_auto_ledge_detection")}}
Attempt to detect when the foot is partially hanging off a ledge and stop it tilting to reach the bottom

---
{{define_cvar("animgraph_footlock_auto_stair_detection")}}
Attempt to detect when the foot is on a stair and will stop it from tilting to reach the next step

---
{{define_cvar("animgraph_footlock_debug_foot_index")}}

---
{{define_cvar("animgraph_footlock_debug_type")}}

---
{{define_cvar("ik_debug_groundtraces")}}
Show IK trace related details

---
{{define_cvar("animgraph_ik_debug")}}

---
{{define_cvar("animgraph_slowdownonslopes_enabled")}}

---
{{define_cvar("animgraph_footlock_enabled")}}
A master convar that effectively disables the entire footlock node.

---
{{define_cvar("animgraph_footlock_hip_offset_enable")}}

---
{{define_cvar("animgraph_footlock_tilt_mode")}}

---
{{define_cvar("animgraph_footlock_use_hip_shift")}}

---
{{define_cvar("animgraph_footlock_draw_footbase")}}

---
{{define_cvar("animgraph_footlock_ik_enable")}}
Enable IK.

---
{{define_cvar("animgraph_motionmatching_print_compressionstats")}}

---
{{define_cvar("animgraph_footlock_ground_roll")}}

---
{{define_cvar("ik_debug_all_chains_unique_color_per_chain")}}

---
{{define_cvar("ik_debug_planetilt")}}

---
{{define_cvar("ik_debug_planetilt_axis_length")}}

---
{{define_cvar("ik_planetilt_enable")}}

---
{{define_cvar("ik_debug_constraints")}}

---
{{define_cvar("ik_final_fixup_enable")}}

---
{{define_cvar("ik_debug_targets")}}

---
{{define_cvar("ik_constraints_enabled")}}

---
{{define_cvar("ik_enable")}}
Enable IK.

---
{{define_cvar("ik_debug_fabrik_backwards_enabled")}}

---
{{define_cvar("ik_debug_fabrik_forwards_enabled")}}

---
{{define_cvar("ik_debug_fabrik_backwards_iterations")}}

---
{{define_cvar("ik_debug_fabrik_forwards_iterations")}}

---
{{define_cvar("ik_fabrik_align_chain")}}

---
{{define_cvar("ik_fabrik_override_num_iterations")}}

---
{{define_cvar("ik_fabrik_forwards_enabled")}}

---
{{define_cvar("ik_fabrik_backwards_enabled")}}

---
{{define_cvar("ik_debug_dogleg3bone")}}

---
{{define_cvar("ik_debug_dogleg3bone_enabled")}}

---
{{define_cvar("ik_debug_ccd")}}

---
{{define_cvar("labelled_debug_helper_show_text")}}

---
{{define_cvar("labelled_debug_helper_show_position")}}

---
{{define_cvar("labelled_debug_helper_arc_segments")}}

---
{{define_cvar("labelled_debug_helper_enabled")}}

---
{{define_cvar("labelled_debug_helper_scale")}}

---
{{define_cvar("labelled_debug_helper_skeleton_show_bone_names")}}

---
{{define_cvar("ik_debug_perlin_solver")}}

---
{{define_cvar("model_default_preview_sequence_name")}}

---
{{define_cvar("ik_debug_chain_to_filter_by")}}

---
{{define_cvar("ik_hinge_debug_bone_index")}}

---
{{define_cvar("mesh_calculate_curvature_smooth_pass_count")}}

---
{{define_cvar("mesh_calculate_curvature_smooth_invert")}}

---
{{define_cvar("mesh_calculate_curvature_smooth_weight")}}

---
{{define_cvar("anim_decode_forcewritealltransforms")}}
Force BatchAnimationDecode to write transformations for all bones

---
{{define_cvar("iv_debugbone")}}
Debug bone name for interpolation spew of CAnimationState.

---
{{define_cvar("skel_constraints_enable")}}

---
{{define_cvar("cl_skel_constraints_enable")}}

---
{{define_cvar("sv_skel_constraints_enable")}}

---
{{define_cvar("anim_resource_validate_on_load")}}
Validates the animation group channel list against the animations on load for every animation

---
{{define_cvar("phys_implicit_integarator")}}
Use implicit integrator for gyroscopic forces

---
{{define_cvar("phys_drag_multiplier")}}
Multiply air drag

---
{{define_cvar("phys_buoyancy_horizontal_damping_multiplier")}}
Multiply water damping for buoyancy affecting linear velocity in the horizontal plane

---
{{define_cvar("phys_buoyancy_vertical_damping_multiplier")}}
Multiply water damping for buoyancy affecting linear velocity in the vertical direction

---
{{define_cvar("phys_buoyancy_angular_damping_multiplier")}}
Multiply water damping for buoyancy affecting angular velocity

---
{{define_cvar("phys_buoyancy_drag_multiplier")}}
Multiply water drag (tries to equalize object velocity with the velocity of the water flow)

---
{{define_cvar("phys_buoyancy_max_acceleration")}}
Maximum acceleration that can be applied by water forces

---
{{define_cvar("phys_fastaddcloneshape")}}

---
{{define_cvar("phys_manifold_pool_enabled")}}

---
{{define_cvar("phys_joint_elasticity_min_rest")}}

---
{{define_cvar("phys_joint_elasticity_max_rest")}}

---
{{define_cvar("phys_joint_plasticity_threshold_min")}}

---
{{define_cvar("phys_joint_plasticity_threshold_max")}}

---
{{define_cvar("rubikon_joint_deepdebugging")}}

---
{{define_cvar("rubikon_joint_always_draw_at_pivot_point")}}

---
{{define_cvar("phys_debug_showdefaultmaterial")}}
If enabled, surfaces with default material are highlighted in physics debug geometry.

---
{{define_cvar("phys_enable_fallback_toi")}}

---
{{define_cvar("phys_build_mass")}}

---
{{define_cvar("phys_build_bounds")}}

---
{{define_cvar("physics_hull_sphere_cast_sat_experimental")}}

---
{{define_cvar("cloth_step")}}

---
{{define_cvar("cloth_sleep_threshold")}}

---
{{define_cvar("cloth_resim_after")}}

---
{{define_cvar("cloth_max_ticks_per_frame")}}

---
{{define_cvar("cloth_step_variability")}}

---
{{define_cvar("cloth_interpolation_strategy")}}

---
{{define_cvar("cloth_rigid_update")}}

---
{{define_cvar("cloth_quasistatic_iters")}}

---
{{define_cvar("cloth_sdf_antitunnel")}}

---
{{define_cvar("cloth_sdf_collision")}}

---
{{define_cvar("cloth_cdt_mul")}}

---
{{define_cvar("smooth_cloth_amax")}}

---
{{define_cvar("smooth_cloth_amin")}}

---
{{define_cvar("smooth_cloth_amul")}}

---
{{define_cvar("cloth_guard_threshold")}}

---
{{define_cvar("cloth_watch")}}

---
{{define_cvar("cloth_debug")}}

---
{{define_cvar("cloth_damping_multiplier")}}

---
{{define_cvar("cloth_damping_bias")}}

---
{{define_cvar("cloth_ground_plane_thickness")}}

---
{{define_cvar("cloth_node_debug_axis_length")}}

---
{{define_cvar("cloth_quad_smooth_rate")}}

---
{{define_cvar("cloth_rod_smooth_rate")}}

---
{{define_cvar("cloth_quad_smooth_iterations")}}

---
{{define_cvar("cloth_rod_smooth_iterations")}}

---
{{define_cvar("cloth_debug_draw_nodepth_alpha")}}

---
{{define_cvar("cloth_ground_offset")}}

---
{{define_cvar("cloth_legacy_stretch_force")}}

---
{{define_cvar("cloth_legacy_support")}}

---
{{define_cvar("cloth_wind")}}

---
{{define_cvar("cloth_wind_pitch")}}

---
{{define_cvar("cloth_dry_drag")}}

---
{{define_cvar("cloth_dry_drag_soften")}}

---
{{define_cvar("cloth_solver")}}

---
{{define_cvar("cloth_approximate_collide")}}

---
{{define_cvar("phys_validate")}}

---
{{define_cvar("phys2_debug_broadphase")}}

---
{{define_cvar("phys_solve_in_parallel_with_island_build")}}

---
{{define_cvar("phys_skip_creating_trivial_islands")}}

---
{{define_cvar("phys_deterministic")}}

---
{{define_cvar("cloth_simulate")}}

---
{{define_cvar("cloth_batch")}}

---
{{define_cvar("cl_jiggle_bone_debug")}}
Display physics-based 'jiggle bone' debugging information

---
{{define_cvar("cl_jiggle_bone_debug_yaw_constraints")}}
Display physics-based 'jiggle bone' debugging information

---
{{define_cvar("cl_jiggle_bone_debug_pitch_constraints")}}
Display physics-based 'jiggle bone' debugging information

---
{{define_cvar("cl_jiggle_bone_invert")}}

---
{{define_cvar("cl_jiggle_bone_sanity")}}
Prevent jiggle bones from pointing directly away from their target in case of numerical instability.

---
{{define_cvar("phys_jiggle_bone_enable")}}

---
{{define_cvar("phys_old_contact_draw")}}

---
{{define_cvar("phys2_contact_debug_draw_size")}}

---
{{define_cvar("phys_cull_internal_mesh_contacts")}}

---
{{define_cvar("phys_mesh_local_toi")}}

---
{{define_cvar("phys_enable_gjk_clipping")}}

---
{{define_cvar("phys_fast_report_contacts")}}
when 1, fast path for collision reporting is implemented making triggers faster in some cases

---
{{define_cvar("hullivr_edge_merge_tan")}}
Should we try to straighten two faces connected to this edge? (tangent)

---
{{define_cvar("hullivr_faceisland_merge_tan")}}
Should we try to straighten an island of faces deviating from their average normal (tangent)?

---
{{define_cvar("hullivr_faceisland_merge_disp")}}
Should we straighten face island if the displacement is this much? (inches)

---
{{define_cvar("hullivr_version")}}

---
{{define_cvar("vphysics_force_apply_magnitude")}}

---
{{define_cvar("vphysics_return_implicit_velocity")}}

---
{{define_cvar("cloth_filter_transform_stateless")}}
Enable the new, stateless version of FilterTransform

---
{{define_cvar("phys_position_iterations")}}

---
{{define_cvar("phys_velocity_iterations")}}

---
{{define_cvar("phys_dump_filter_solid_only")}}

---
{{define_cvar("phys_dump_filter_trace_callstack")}}

---
{{define_cvar("phys_dump_filter_body_name")}}

---
{{define_cvar("phys_min_motion_controller_count_to_run_in_job")}}

---
{{define_cvar("phys_intermediate_notify_remove_only")}}

---
{{define_cvar("vphys2_friction_factor")}}
Change global friction factor

---
{{define_cvar("vphys2_restitution_factor")}}
Change global restitution factor

---
{{define_cvar("phys_reload_immediately")}}
Set to 1 to reload resources and reconstruct physics of entities on the fly. May unexpectedly change behavior or crash the game, because game code is generally unaware of underlying resource reloads and may hold references to physics that may become invalid during resource reload. It is inherently harder for physics to deal with resource reloads because of persistent nature of objects being simulated (textures can be easily reloaded on the fly; if an entity holds a handle to a ragdoll body part, it may expect that handle to stay valid while the ragdoll exists)

---
{{define_cvar("cloth_reload_immediately")}}
Reload and reconstruct cloth on the fly after phsyics has been reloaded (usually due to having been recompiled). When set to 0, and the bones change, crashes may occur due to de-sychronization between animation/model state in the game, particles and rendering and cloth state

---
{{define_cvar("phys_step_threaded")}}

---
{{define_cvar("legacy_models_supported")}}
Whether to support legacy (pre-modeldoc) models

---
{{define_cvar("voice_initial_buffer_ms")}}

---
{{define_cvar("snd_sos_show_block_debug")}}
Spew data about the list of block entries.

---
{{define_cvar("snd_sos_show_entry_match_free")}}

---
{{define_cvar("snd_group_cluster_debug")}}

---
{{define_cvar("snd_group_priority_max_tolerance")}}

---
{{define_cvar("snd_group_priority_debug")}}

---
{{define_cvar("snd_op_test_convar")}}

---
{{define_cvar("snd_dsp_distance_min")}}

---
{{define_cvar("snd_dsp_distance_max")}}

---
{{define_cvar("snd_sos_report_entity_deleted")}}

---
{{define_cvar("snd_sos_calc_angle_debug")}}

---
{{define_cvar("snd_sos_show_mixgroup_path_errors")}}

---
{{define_cvar("snd_occlusion_debug")}}

---
{{define_cvar("cl_snd_cast_clear")}}

---
{{define_cvar("cl_snd_cast_retrigger")}}

---
{{define_cvar("snd_occlusion_min_wall_thickness")}}

---
{{define_cvar("snd_occlusion_report")}}

---
{{define_cvar("snd_occlusion_override")}}

---
{{define_cvar("snd_occlusion_visualize")}}

---
{{define_cvar("snd_use_baked_occlusion")}}

---
{{define_cvar("snd_occlusion_rays")}}

---
{{define_cvar("snd_occlusion_bounces")}}

---
{{define_cvar("snd_occlusion_indirect_radius")}}

---
{{define_cvar("snd_occlusion_debug_listener_pos")}}

---
{{define_cvar("snd_occlusion_indirect_min")}}

---
{{define_cvar("snd_occlusion_indirect_max")}}

---
{{define_cvar("snd_sos_show_operator_pause_entry")}}

---
{{define_cvar("snd_rear_stereo_scale")}}

---
{{define_cvar("snd_steamaudio_source_pathing_debug")}}
Enable path visualization for steam_audio_source operator.

---
{{define_cvar("snd_steamaudio_source_pathing_debug_duration")}}
Duration for which path remains visible. Should be close to update rate of the sound operator stack.

---
{{define_cvar("snd_steamaudio_source_pathing_enable_validation")}}
Enable real-time pathing validation against dynamic geometry.

---
{{define_cvar("snd_sos_show_operator_stop_entry")}}

---
{{define_cvar("snd_sos_limit_self")}}

---
{{define_cvar("snd_sos_show_queuetotrack")}}

---
{{define_cvar("snd_sos_show_voice_elapsed_time")}}

---
{{define_cvar("snd_sos_show_soundevent_start")}}

---
{{define_cvar("snd_sos_show_operator_init")}}

---
{{define_cvar("snd_sos_show_operator_updates")}}

---
{{define_cvar("snd_sos_show_operator_shutdown")}}

---
{{define_cvar("snd_sos_list_operator_updates")}}

---
{{define_cvar("snd_sos_show_operator_event_filter")}}

---
{{define_cvar("snd_sos_show_operator_operator_filter")}}

---
{{define_cvar("snd_sos_show_operator_not_executing")}}

---
{{define_cvar("snd_sos_show_operator_event_and_stack")}}

---
{{define_cvar("snd_sos_show_operator_field_filter")}}

---
{{define_cvar("snd_sos_print_full_field_info")}}

---
{{define_cvar("snd_sos_print_field_references")}}

---
{{define_cvar("snd_sos_show_soundevent_param_overwrite")}}

---
{{define_cvar("snd_sos_max_event_base_depth")}}

---
{{define_cvar("snd_sos_hide_simple_parameter_overwrite_warnings")}}

---
{{define_cvar("snd_sos_show_parameter_overwrite_warnings")}}

---
{{define_cvar("snd_sos_compare_kv3_native_stacks")}}

---
{{define_cvar("snd_sos_print_addfield_dupes")}}

---
{{define_cvar("snd_sos_opvar_debug")}}

---
{{define_cvar("snd_sos_show_opvar_updates")}}

---
{{define_cvar("snd_sos_show_opvar_updates_filter")}}

---
{{define_cvar("snd_sos_soundevent_filter")}}

---
{{define_cvar("snd_sos_print_table_arrays")}}

---
{{define_cvar("snd_sos_pause_system")}}

---
{{define_cvar("snd_sos_print_fps")}}

---
{{define_cvar("snd_sos_block_stop_global_stack")}}

---
{{define_cvar("snd_sos_block_global_stack")}}

---
{{define_cvar("snd_sos_ingame_debug")}}

---
{{define_cvar("snd_sos_show_track_list")}}

---
{{define_cvar("snd_sequencer_show_bpm")}}

---
{{define_cvar("snd_sequencer_show_events")}}

---
{{define_cvar("snd_sequencer_show_quantize_queue")}}

---
{{define_cvar("soundsystem_device_used")}}
Sound device in use (changing this does not change the soundsystem).

---
{{define_cvar("snd_diffusor_simd")}}
Enable SIMD code path for diffusor processor.

---
{{define_cvar("snd_boxverb_simd")}}
Enable SIMD code path for shoebox reverb processor.

---
{{define_cvar("snd_boxverb_simd_svf")}}
0 = use biquad instead of svf, 1 = use vectorized svf, 2 = use scalar svf

---
{{define_cvar("snd_enable_subgraph_log")}}

---
{{define_cvar("snd_enable_subgraph_corenull_passthrough")}}

---
{{define_cvar("audio_input_test_signal")}}
For testing the audio input pathway with a sine tone instead of SDL3.

---
{{define_cvar("dump_audio_input")}}

---
{{define_cvar("attached_output_stall_ms")}}

---
{{define_cvar("silence_dsp")}}
When on, silences all DSP mixes.

---
{{define_cvar("adsp_room_min")}}

---
{{define_cvar("adsp_duct_min")}}

---
{{define_cvar("adsp_hall_min")}}

---
{{define_cvar("adsp_tunnel_min")}}

---
{{define_cvar("adsp_street_min")}}

---
{{define_cvar("adsp_alley_min")}}

---
{{define_cvar("adsp_courtyard_min")}}

---
{{define_cvar("adsp_openspace_min")}}

---
{{define_cvar("adsp_openwall_min")}}

---
{{define_cvar("adsp_openstreet_min")}}

---
{{define_cvar("adsp_opencourtyard_min")}}

---
{{define_cvar("adsp_debug")}}

---
{{define_cvar("adsp_door_height")}}

---
{{define_cvar("adsp_wall_height")}}

---
{{define_cvar("adsp_low_ceiling")}}

---
{{define_cvar("snd_mergemethod")}}
Sound merge method (0 == sum and clip, 1 == max, 2 == avg).

---
{{define_cvar("snd_gamevolume")}}
Game volume

---
{{define_cvar("snd_voipvolume")}}
Voice volume

---
{{define_cvar("snd_gamevoicevolume")}}
Game v.o. volume

---
{{define_cvar("snd_delay_sound_ms_shift")}}
Sound device synchronization shift (ms)

---
{{define_cvar("snd_delay_sound_ms_max")}}
Sound device synchronization max delay (ms)

---
{{define_cvar("volume")}}
Sound volume

---
{{define_cvar("snd_toolvolume")}}
Volume of sounds in tools (e.g. Hammer, SFM)

---
{{define_cvar("snd_musicvolume")}}
Music volume

---
{{define_cvar("snd_autodetect_latency")}}

---
{{define_cvar("snd_mixahead")}}

---
{{define_cvar("snd_mix_async")}}

---
{{define_cvar("dsp_dist_min")}}

---
{{define_cvar("dsp_dist_max")}}

---
{{define_cvar("dsp_mix_min")}}

---
{{define_cvar("dsp_mix_max")}}

---
{{define_cvar("dsp_db_min")}}

---
{{define_cvar("dsp_db_mixdrop")}}

---
{{define_cvar("snd_showstart")}}

---
{{define_cvar("snd_filter")}}

---
{{define_cvar("dsp_automatic")}}

---
{{define_cvar("dsp_off")}}

---
{{define_cvar("dsp_volume")}}

---
{{define_cvar("dsp_vol_5ch")}}

---
{{define_cvar("dsp_vol_4ch")}}

---
{{define_cvar("dsp_vol_2ch")}}

---
{{define_cvar("snd_soundmixer_update_maximum_frame_rate")}}

---
{{define_cvar("snd_mixer_master_level")}}

---
{{define_cvar("snd_mixer_master_dsp")}}

---
{{define_cvar("snd_showclassname")}}

---
{{define_cvar("snd_list")}}

---
{{define_cvar("snd_disable_mixer_solo")}}

---
{{define_cvar("snd_soundmixer")}}

---
{{define_cvar("snd_disable_mixer_duck")}}

---
{{define_cvar("snd_soundmixer_version")}}

---
{{define_cvar("snd_async_spew_blocking")}}
Spew message to console any time async sound loading blocks on file i/o.

---
{{define_cvar("snd_refdist")}}
Reference distance for snd_refdb

---
{{define_cvar("snd_refdb")}}
Reference dB at snd_refdist

---
{{define_cvar("snd_gain")}}

---
{{define_cvar("snd_gain_max")}}

---
{{define_cvar("snd_gain_min")}}

---
{{define_cvar("snd_sos_default_update_stack")}}

---
{{define_cvar("snd_compare_KV_convert")}}

---
{{define_cvar("snd_sos_use_case_sensitive_soundevents")}}

---
{{define_cvar("snd_sos_show_soundevent_overwrites")}}

---
{{define_cvar("snd_sos_soundevent_deferred_interval_time")}}

---
{{define_cvar("snd_sos_soundevent_max_deferred_time")}}

---
{{define_cvar("speaker_config")}}

---
{{define_cvar("sound_device_override")}}
ID of the sound device to use

---
{{define_cvar("snd_spatialize_lerp")}}

---
{{define_cvar("update_voices_low_priority")}}

---
{{define_cvar("snd_enable_imgui")}}
Game/Sound System Debugger

---
{{define_cvar("snd_steamaudio_perspective_correction_front_only")}}
Use perspective correction for 3D audio only in the frontal directions.

---
{{define_cvar("snd_steamaudio_reverb_level_db")}}
Adjust overall volume (dB) of the output from Steam Audio Reverb processor.

---
{{define_cvar("snd_steamaudio_enable_reverb")}}
Enable Steam Audio Reverb processor.

---
{{define_cvar("snd_hrtf_distance_behind")}}
HRTF calculations will calculate the player as being this far behind the camera.

---
{{define_cvar("dota_enable_spatial_audio")}}
Flag to enable spatial audio in Dota 2.

---
{{define_cvar("dota_spatial_audio_mix")}}
Mix value to blend spatial and non-spatial audio in Dota 2.

---
{{define_cvar("snd_vmix_show_input_updates")}}
If set to 1, show all incoming updates to vmix inputs.


---
{{define_cvar("snd_vmix_override_mix_decay_time")}}
If set > 0, overrides how long the decay time is on all mix graphs (in seconds).


---
{{define_cvar("run_voicecontainer_async")}}

---
{{define_cvar("snd_report_verbose_error")}}
If set to 1, report more error found when playing sounds.


---
{{define_cvar("snd_envelope_rate")}}

---
{{define_cvar("snd_ducktovolume")}}

---
{{define_cvar("snd_duckerattacktime")}}

---
{{define_cvar("snd_duckerreleasetime")}}

---
{{define_cvar("snd_duckerthreshold")}}

---
{{define_cvar("voice_loopback")}}

---
{{define_cvar("voice_fadeouttime")}}

---
{{define_cvar("opus_decode_test_signal")}}

---
{{define_cvar("opus_unittest_test_signal")}}

---
{{define_cvar("voice_stall_ms")}}

---
{{define_cvar("voice_min_buffer_ms")}}

---
{{define_cvar("snd_steamaudio_max_occlusion_samples")}}
The maximum number of rays that can be traced for volumetric occlusion by Steam Audio.

---
{{define_cvar("snd_steamaudio_num_rays")}}
The number of rays to trace for reflection modeling by Steam Audio.

---
{{define_cvar("snd_steamaudio_num_diffuse_samples")}}
The number of directions considered for ray bounce by Steam Audio.

---
{{define_cvar("snd_steamaudio_num_bounces")}}
The maximum number of times any ray can bounce when using Steam Audio.

---
{{define_cvar("snd_steamaudio_num_threads")}}
Sets the number of threads used for realtime reflection by Steam Audio.

---
{{define_cvar("snd_steamaudio_ir_duration")}}
The time delay between a sound being emitted and the last audible reflection in Steam Audio.

---
{{define_cvar("snd_steamaudio_pathing_order")}}
The amount of directional detail in the simulated by Steam Audio.

---
{{define_cvar("snd_steamaudio_pathing_order_rendering")}}
The amount of directional detail in the rendered audio by Steam Audio.

---
{{define_cvar("snd_steamaudio_max_convolution_sources")}}
The maximum number of simultaneous sources that can be modeled by Steam Audio.

---
{{define_cvar("snd_steamaudio_invalid_path_length")}}
Path length of invalid path in inches. Set this to .0 to use direct distance as path length.

---
{{define_cvar("snd_steamaudio_reverb_order")}}
Ambisonics order to use for simulating reverb.

---
{{define_cvar("snd_steamaudio_reverb_order_rendering")}}
Ambisonics order to use for convolution reverb. 0th order = 1 channel, 1st order = 4 channels.

---
{{define_cvar("snd_steamaudio_hybrid_reverb_transition_time")}}
Set the transition time (in seconds) between convolution and parametric reverb.

---
{{define_cvar("snd_steamaudio_hybrid_reverb_overlap")}}
Set the overlap fraction (0 to 1) for hybrid reverb.

---
{{define_cvar("snd_steamaudio_reverb_update_rate")}}
Set the maximum update rate (in Hz) for reverb.

---
{{define_cvar("snd_steamaudio_enable_custom_hrtf")}}
Enable custom HRTF loading.

---
{{define_cvar("snd_steamaudio_active_hrtf")}}
Index of active HRTF.

---
{{define_cvar("snd_steamaudio_normalize_default_hrtf_volume")}}
Normalize volume of default HRTF dataset across all directions.

---
{{define_cvar("snd_steamaudio_default_hrtf_volume_gain")}}
Adjust overall volume of the default HRTF by the specified gain (dB).

---
{{define_cvar("snd_steamaudio_max_hrtf_normalization_gain_db")}}
Maximum gain any HRTF could have during volume normalization.

---
{{define_cvar("snd_steamaudio_enable_perspective_correction")}}
Enable perspective correction for 3D audio.

---
{{define_cvar("snd_steamaudio_perspective_correction_factor")}}
Perspective correction factor, ratio of screen size and view depth from screen, for 3D audio.

---
{{define_cvar("snd_steamaudio_enable_probeneighborhood_caching")}}
Enable caching listener probe neighborhood for pathing.

---
{{define_cvar("snd_steamaudio_pathing_enable_source_probe_interp")}}
If set, all the probes near a source withing probe range are used to find paths instead of nearest probe.

---
{{define_cvar("snd_steamaudio_enable_reverb_probe_caching_for_missing_probes")}}
Continue using previous prrobes if probe lookup for reverb fails.

---
{{define_cvar("snd_steamaudio_enable_pathing")}}
This variable is checked by soundstack to globally enabling pathing for audio processing.

---
{{define_cvar("snd_steamaudio_load_pathing_data")}}
If set, baked pathing data is loaded. Steam Audio Hammer entities can successfully use pathing in this case.

---
{{define_cvar("snd_steamaudio_load_reverb_data")}}
If set, baked reverb data is loaded. Reset it to zero during an format changes of baked data until all data is updated.

---
{{define_cvar("snd_steamaudio_max_probes_reverb")}}
Maximum number of probes to create when baking reverb.

---
{{define_cvar("snd_steamaudio_max_probes_pathing")}}
Maximum number of probes to create when baking paths.

---
{{define_cvar("snd_steamaudio_max_probes_customdata")}}
Maximum number of probes to create when baking custom data.

---
{{define_cvar("sc_keep_all_layers")}}

---
{{define_cvar("sc_batch_layer_cb_updates")}}

---
{{define_cvar("sc_spew_cmt_usage")}}

---
{{define_cvar("sc_disableThreading")}}

---
{{define_cvar("r_shadows")}}

---
{{define_cvar("debugoverlay_show_text_outline")}}
Toggle display of box around text

---
{{define_cvar("debugoverlay_force_respect_ttl")}}
Force respect TTL even when clearing scopes

---
{{define_cvar("screenmessage_show")}}
Enable display of console messages on screen. 1 = Enabled, 0 = Disabled, -1 = Enabled if vgui is not present

---
{{define_cvar("debugoverlay_text_scale")}}
Scale of the text used for 3d display

---
{{define_cvar("imgui_default_font_size")}}
Default imgui font size

---
{{define_cvar("sc_imgui_show_debug_log")}}
SceneSystem/Imgui/Show Debug Log

---
{{define_cvar("sc_imgui_show_metrics")}}
SceneSystem/Imgui/Show Metrics

---
{{define_cvar("sc_imgui_show_id_stack")}}
SceneSystem/Imgui/Show ID Stack Tool

---
{{define_cvar("r_reset_character_decals")}}

---
{{define_cvar("r_character_decal_resolution")}}
Resolution of character decal texture.

---
{{define_cvar("r_character_decal_renderdoc_capture")}}

---
{{define_cvar("r_fullscreen_quad_single_triangle")}}

---
{{define_cvar("r_haircull_percent")}}

---
{{define_cvar("r_hair_voxels")}}

---
{{define_cvar("r_force_thick_hair")}}

---
{{define_cvar("r_hairsort")}}

---
{{define_cvar("hairsim_reset")}}

---
{{define_cvar("hairsim_force_fixed_timestep")}}

---
{{define_cvar("r_shadowtile_waveops")}}

---
{{define_cvar("r_ssao_radius")}}

---
{{define_cvar("r_ssao_bias")}}

---
{{define_cvar("r_ssao_strength")}}

---
{{define_cvar("r_ssao_blur")}}

---
{{define_cvar("mat_tonemap_force_min")}}

---
{{define_cvar("mat_tonemap_force_max")}}

---
{{define_cvar("mat_tonemap_force_percent_target")}}
Override. Old default was 45.

---
{{define_cvar("mat_tonemap_force_percent_bright_pixels")}}
Override. Old value was 1.0

---
{{define_cvar("mat_tonemap_force_average_lum_min")}}
Override. Old default was 3.0

---
{{define_cvar("mat_tonemap_force_rate")}}

---
{{define_cvar("mat_tonemap_force_accelerate_exposure_down")}}

---
{{define_cvar("mat_tonemap_force_use_alpha")}}

---
{{define_cvar("mat_tonemap_force_scale")}}

---
{{define_cvar("mat_tonemap_uncap_exposure")}}

---
{{define_cvar("mat_tonemap_debug")}}

---
{{define_cvar("mat_tonemap_force_log_lum_min")}}

---
{{define_cvar("mat_tonemap_force_log_lum_max")}}

---
{{define_cvar("mat_tonemap_bloom_start_value")}}

---
{{define_cvar("mat_tonemap_bloom_scale")}}

---
{{define_cvar("sc_show_tonemap_visualizer")}}
SceneSystem/Tonemap Visualizer

---
{{define_cvar("volume_fog_enable_jitter")}}

---
{{define_cvar("volume_fog_dither_scale")}}

---
{{define_cvar("volume_fog_intermediate_textures_hdr")}}

---
{{define_cvar("volume_fog_width")}}

---
{{define_cvar("volume_fog_height")}}

---
{{define_cvar("volume_fog_depth")}}

---
{{define_cvar("volume_fog_density_scale")}}
Scale global volume fog density

---
{{define_cvar("volume_fog_temporal_filter")}}

---
{{define_cvar("volume_fog_temporal_weight")}}
Temporal filtering weight

---
{{define_cvar("volume_fog_shadow_penumbra_multiplier")}}
Penumbra size multiplier for shadow sampling, reduces fog shadow aliasing

---
{{define_cvar("volume_fog_debug_volumes")}}

---
{{define_cvar("volume_fog_depth_warp")}}

---
{{define_cvar("volume_fog_depth_warp_debug")}}

---
{{define_cvar("volume_fog_force_indirect_lpvs")}}
Force use of LPVs for indirect lighting in fog

---
{{define_cvar("lb_barnlight_shadowmap_scale")}}
Scale for computed barnlight shadowmap size

---
{{define_cvar("lb_barnlight_shadow_use_precomputed_vis")}}

---
{{define_cvar("lb_shadow_map_culling")}}

---
{{define_cvar("lb_shadow_map_cull_empty_mixed")}}
Don't render shadows for mixed shadowmaps with no dynamics objects in view

---
{{define_cvar("lb_allow_time_sliced_shadow_map_rendering")}}
Allow time-sliced shadow buffer rendering when enabled via gameinfo.gi

---
{{define_cvar("lb_convert_to_barn_lights_falloff_match_point")}}

---
{{define_cvar("lb_cubemap_normalization_max")}}

---
{{define_cvar("lb_cubemap_normalization_roughness_begin")}}

---
{{define_cvar("lb_override_barn_light_fade_sizes_enable")}}

---
{{define_cvar("lb_override_barn_light_fade_sizes")}}

---
{{define_cvar("lb_override_barn_light_shadow_fade_sizes")}}

---
{{define_cvar("r_directional_lightmaps")}}

---
{{define_cvar("sparseshadowtree_cs_debug_colors")}}
Output debug colors for SST CS.

---
{{define_cvar("r_pixelvisibility_partial")}}

---
{{define_cvar("r_dopixelvisibility")}}

---
{{define_cvar("r_pixelvisibility_spew")}}

---
{{define_cvar("r_drawpixelvisibility")}}
Show the occlusion proxies

---
{{define_cvar("sc_rendergraph_debug_visualizer")}}
SceneSystem/RenderGraph Visualizer

---
{{define_cvar("r_render_to_cubemap_debug")}}

---
{{define_cvar("r_draw_overlays")}}

---
{{define_cvar("sc_use_clear_subrect")}}

---
{{define_cvar("sc_enable_discard")}}

---
{{define_cvar("sc_disable_spotlight_shadows")}}

---
{{define_cvar("sc_shadow_depth_bias_state_override")}}

---
{{define_cvar("sc_shadow_depth_bias")}}

---
{{define_cvar("sc_shadow_slopescale_depth_bias")}}

---
{{define_cvar("sc_shadow_depth_bias_clamp")}}

---
{{define_cvar("sc_barnlight_enable_precomputed_vis")}}
Enable use of precomputed vis membership for lights (requires map restart)

---
{{define_cvar("r_light_probe_volume_debug_grid_prim")}}
0: spheres, 1: cubes

---
{{define_cvar("r_light_probe_volume_debug_grid_samplesize")}}
sphere radius (world) for LPV debug grid

---
{{define_cvar("r_light_probe_volume_debug_grid_roughness")}}
roughness for LPV debug grid

---
{{define_cvar("r_light_probe_volume_debug_grid_metalness")}}
metalness for LPV debug grid

---
{{define_cvar("r_light_probe_volume_debug_grid_albedo")}}
albedo for LPV debug grid

---
{{define_cvar("rtx_dynamic_blas")}}
Allow dynamic BLAS creation for geometry going through the compute shader skinning path.

---
{{define_cvar("rtx_force_default_hitgroup")}}
Forces all ray traced geometry to use default hit shaders instead of specialized ones.

---
{{define_cvar("csm_split_log_scalar")}}

---
{{define_cvar("csm_sst_shadow_focus_region_minz")}}

---
{{define_cvar("csm_sst_shadow_focus_region_maxz")}}

---
{{define_cvar("csm_shadow_worldview_align_x_to_u")}}

---
{{define_cvar("csm_shadow_worldview_shear_align_z_to_v")}}

---
{{define_cvar("csm_res_override_0")}}

---
{{define_cvar("csm_res_override_1")}}

---
{{define_cvar("csm_res_override_2")}}

---
{{define_cvar("csm_res_override_3")}}

---
{{define_cvar("csm_bias_override_0")}}

---
{{define_cvar("csm_bias_override_1")}}

---
{{define_cvar("csm_bias_override_2")}}

---
{{define_cvar("csm_bias_override_3")}}

---
{{define_cvar("csm_max_num_cascades_override")}}
Number of cascades in sunlight shadow

---
{{define_cvar("csm_max_shadow_dist_override")}}

---
{{define_cvar("csm_viewmodel_shadows")}}

---
{{define_cvar("csm_viewmodel_max_shadow_dist")}}

---
{{define_cvar("csm_viewmodel_nearz")}}

---
{{define_cvar("csm_viewmodel_farz")}}

---
{{define_cvar("csm_viewmodel_max_visible_dist")}}

---
{{define_cvar("csm_max_visible_dist")}}

---
{{define_cvar("csm_max_dist_between_caster_and_receiver")}}
default pushback

---
{{define_cvar("csm_sst_max_visible_dist")}}

---
{{define_cvar("csm_sst_pushback_distance")}}
default pushback

---
{{define_cvar("csm_viewdir_shadow_bias")}}

---
{{define_cvar("csm_cascade_viewdir_shadow_bias_scale")}}

---
{{define_cvar("csm_cascade0_override_dist")}}

---
{{define_cvar("csm_cascade1_override_dist")}}

---
{{define_cvar("csm_cascade2_override_dist")}}

---
{{define_cvar("csm_cascade3_override_dist")}}

---
{{define_cvar("r_stereo_multiview_instancing")}}
Use multiview instancing for stereo rendering.

---
{{define_cvar("sc_max_framebuffer_copies_per_layer")}}

---
{{define_cvar("sc_queue_reflection_views_to_layers")}}

---
{{define_cvar("sc_force_single_display_list_per_layer")}}

---
{{define_cvar("sc_no_cull")}}

---
{{define_cvar("sc_no_vis")}}

---
{{define_cvar("sc_bounds_group_cull")}}

---
{{define_cvar("sc_disable_culling_boxes")}}

---
{{define_cvar("sc_allow_dithered_lod")}}
Allow use of dithered lod transitions

---
{{define_cvar("sc_dithered_lod_transition_amt")}}
Percentage of the transition between two lods we will apply a dither

---
{{define_cvar("sc_layer_batch_threshold")}}

---
{{define_cvar("sc_layer_batch_threshold_fullsort")}}

---
{{define_cvar("sc_disable_shadow_materials")}}

---
{{define_cvar("sc_disable_shadow_fastpath")}}

---
{{define_cvar("sc_screen_size_lod_scale_override")}}

---
{{define_cvar("sc_extended_stats")}}

---
{{define_cvar("sc_show_view_profiler")}}
SceneSystem/View Profiler

---
{{define_cvar("sc_hdr_enabled_override")}}
Override default setting for HDR rendering. -1 default, 0 NoHdr, 1 Hdr, 2 Hdr 1010102 3 Hdr 111110

---
{{define_cvar("sc_show_cs_skinning_stats")}}
SceneSystem/Compute Skinning Stats

---
{{define_cvar("r_smooth_morph_normals")}}

---
{{define_cvar("sc_force_translation_in_projection")}}
If enabled, the camera's translation will be included in the projection matrix.

---
{{define_cvar("sc_dump_lists")}}

---
{{define_cvar("sc_disable_baked_lighting")}}

---
{{define_cvar("sc_check_world")}}

---
{{define_cvar("sc_fade_distance_scale_override")}}

---
{{define_cvar("r_fallback_texture_lod_scale")}}
Scale factor for requested texture size (texture streaming) - used for geo that doesn't have a precomputed UV density measure

---
{{define_cvar("r_texture_lod_scale")}}
Scale factor for requested texture size (texture streaming)

---
{{define_cvar("sc_force_lod_level")}}

---
{{define_cvar("sc_reject_all_objects")}}

---
{{define_cvar("sc_skip_traversal")}}

---
{{define_cvar("sc_disable_procedural_layer_rendering")}}

---
{{define_cvar("sc_only_render_shadowcasters")}}

---
{{define_cvar("sc_only_render_opaque")}}

---
{{define_cvar("sc_throw_away_all_layers")}}

---
{{define_cvar("sc_show_gpu_profiler")}}
SceneSystem/GPU Profiler

---
{{define_cvar("sc_show_texture_visualizer")}}
SceneSystem/Texture Visualizer

---
{{define_cvar("sc_draw_aggregate_meshes")}}
SceneSystem/Aggregates/Draw Aggregates

---
{{define_cvar("sc_aggregate_gpu_culling")}}
Toggles GPU culling of aggregate meshes

---
{{define_cvar("sc_aggregate_gpu_occlusion_culling")}}

---
{{define_cvar("sc_aggregate_gpu_vis_culling")}}

---
{{define_cvar("sc_aggregate_gpu_culling_show_culled")}}
SceneSystem/Aggregates/Show GPU Culled Meshes

---
{{define_cvar("sc_aggregate_gpu_culling_conservative_bounds")}}

---
{{define_cvar("sc_aggregate_show_outside_vis")}}

---
{{define_cvar("sc_aggregate_fragment_merging")}}

---
{{define_cvar("sc_aggregate_indirect_draw_compaction")}}
Use multidrawindirect...count if the driver/hardware supports it

---
{{define_cvar("sc_aggregate_indirect_draw_compaction_threshold")}}
Threshold of indirect draws when we will do compaction

---
{{define_cvar("sc_aggregate_debug_draw_meshlets")}}
SceneSystem/Aggregates/Visualize Meshlets

---
{{define_cvar("sc_aggregate_material_solo")}}

---
{{define_cvar("r_aoproxy_min_dist")}}

---
{{define_cvar("r_aoproxy_min_dist_box")}}

---
{{define_cvar("r_aoproxy_cull_dist")}}
Distance to cull the AO proxy as a factor of size

---
{{define_cvar("r_morphing_enabled")}}

---
{{define_cvar("r_skinning_enabled")}}

---
{{define_cvar("sc_clutter_draw")}}
SceneSystem/Aggregates/Draw Aggregates

---
{{define_cvar("sc_clutter_density_full_size")}}
Screen-size where clutter will be full density

---
{{define_cvar("sc_clutter_density_none_size")}}
Screen-size where clutter will be gone

---
{{define_cvar("sc_instanced_mesh_enable")}}
Toggles rendering instanced meshes

---
{{define_cvar("sc_instanced_mesh_gpu_culling")}}
Toggles GPU culling of instanced meshes

---
{{define_cvar("sc_instanced_mesh_gpu_occlusion_culling")}}
Toggles GPU occlusion of instanced meshes

---
{{define_cvar("sc_instanced_mesh_gpu_vis_culling")}}
Toggles GPU vis of instanced meshes

---
{{define_cvar("sc_instanced_mesh_motion_vectors")}}
Toggles motion vector support for instanced meshes

---
{{define_cvar("sc_instanced_mesh_lod_bias")}}
Bias for LOD selection of instanced meshes

---
{{define_cvar("sc_instanced_mesh_lod_bias_shadow")}}
Bias for LOD selection of instanced meshes in shadowmaps

---
{{define_cvar("sc_instanced_mesh_size_cull_bias")}}
Bias for size culling of instanced meshes

---
{{define_cvar("sc_instanced_mesh_size_cull_bias_shadow")}}
Bias for size culling instanced meshes in shadowmaps

---
{{define_cvar("sc_instanced_mesh_solo")}}

---
{{define_cvar("sc_instanced_material_solo")}}

---
{{define_cvar("sc_allow_dynamic_constant_batching")}}

---
{{define_cvar("sc_visualize_sceneobjects")}}
1 = visualize bounds, 2 = visualize sceneobject mesh materials, 3 = required texture size, 4 = bounds group, 5 = LOD, 6 == LPV Binding, 7 == instancing

---
{{define_cvar("sc_visualize_batches")}}
color per batch

---
{{define_cvar("sc_mesh_backface_culling")}}

---
{{define_cvar("sc_allow_write_depth_before_blend")}}

---
{{define_cvar("sc_force_materials_batchable")}}

---
{{define_cvar("sc_disable_world_materials")}}

---
{{define_cvar("fog_override")}}
Overrides the map's fog settings (-1 populates fog_ vars with map's values)

---
{{define_cvar("fog_color")}}

---
{{define_cvar("fog_hdrcolorscale")}}

---
{{define_cvar("r_light_probe_volume_debug_colors")}}

---
{{define_cvar("r_cubemap_debug_colors")}}

---
{{define_cvar("r_light_probe_volume_debug_grid")}}
Show LPV debug grid, 0: off, 1: closest only 2: closest and keep 3: all

---
{{define_cvar("r_light_probe_volume_debug_grid_bbox")}}
Show LPV bounding box when debug grid is on, 0: off, 1: on

---
{{define_cvar("sc_cache_envmap_lpv_lookup")}}

---
{{define_cvar("lb_enable_lights")}}
SceneSystem/LightBinner/Enable Lights

---
{{define_cvar("lb_enable_envmaps")}}
SceneSystem/LightBinner/Enable EnvMaps

---
{{define_cvar("lb_use_illumination_silhouette")}}
SceneSystem/LightBinner/Use Illumination Bounds

---
{{define_cvar("lb_use_ellipsoid_bounds")}}

---
{{define_cvar("lb_debug_silhouette")}}
SceneSystem/LightBinner/Debug Silhouettes

---
{{define_cvar("lb_debug_tiles")}}
SceneSystem/LightBinner/Debug Tiles

---
{{define_cvar("lb_debug_visualize_shadowed_lights")}}
SceneSystem/LightBinner/Debug Visualize Shadowed Lights

---
{{define_cvar("lb_debug_light_bounds")}}
SceneSystem/LightBinner/Debug Light Bounds

---
{{define_cvar("lb_debug_shadow_atlas")}}
SceneSystem/LightBinner/Debug Shadow Atlas

---
{{define_cvar("lb_debug_shadowtile_atlas")}}
SceneSystem/LightBinner/Debug ShadowTile Atlas

---
{{define_cvar("lb_allow_shadow_rotation")}}
SceneSystem/LightBinner/Shadow Rotation

---
{{define_cvar("lb_enable_stationary_lights")}}
Allows rendering stationary/mixed lights

---
{{define_cvar("lb_enable_dynamic_lights")}}
Allows rendering dynamic lights

---
{{define_cvar("lb_enable_shadow_casting")}}
Allow stationary/dynamic lights to cast shadows.

---
{{define_cvar("lb_enable_baked_shadows")}}
SceneSystem/LightBinner/Enable Baked Shadows

---
{{define_cvar("lb_mixed_shadows")}}
SceneSystem/LightBinner/Enable Mixed Shadows

---
{{define_cvar("lb_enable_fog_mixed_shadows")}}
SceneSystem/LightBinner/Enable Fog Mixed Shadows

---
{{define_cvar("lb_enable_binning")}}
SceneSystem/LightBinner/Enable Binning

---
{{define_cvar("lb_tile_pixels")}}

---
{{define_cvar("lb_bin_slices")}}

---
{{define_cvar("lb_shadow_texture_width_override")}}
Override width of shadow atlas texture

---
{{define_cvar("lb_shadow_texture_height_override")}}
Override height of shadow atlas texture

---
{{define_cvar("lb_csm_cascade_size_override")}}
Override width/height of individual cascades in the CSM

---
{{define_cvar("lb_csm_receiver_plane_depth_bias")}}
Shader depth bias applied to shadow receiver (Note this conflicts with renderstate depth bias, both now default to 0)

---
{{define_cvar("lb_csm_receiver_plane_depth_bias_transmissive_backface")}}
Depth bias applied to shadow receiver for transmissive backface geo (based on renderstate depthbias being 0)

---
{{define_cvar("lb_csm_draw_alpha_tested")}}

---
{{define_cvar("lb_csm_draw_translucent")}}

---
{{define_cvar("lb_csm_fov_override")}}

---
{{define_cvar("lb_csm_cross_fade_override")}}
Override CSM cross fade amount

---
{{define_cvar("lb_csm_distance_fade_override")}}
Override CSM distance fade

---
{{define_cvar("lb_csm_override_staticgeo_cascades")}}
Override Cascades that will render static objects with lb_csm_override_staticgeo_cascades_value

---
{{define_cvar("lb_csm_override_staticgeo_cascades_value")}}
If lb_csm_override_staticgeo_cascades, override value used to determine which cascades render static objects

---
{{define_cvar("lb_sun_csm_size_cull_threshold_texels")}}
Size, in texels, where we will cull an object in the shadowmap

---
{{define_cvar("lb_csm_override_bulb_radius")}}
Override bulb radius for CSM

---
{{define_cvar("lb_dynamic_shadow_penumbra")}}
Adjust shadow penumbra based on light size

---
{{define_cvar("lb_dynamic_shadow_resolution")}}
Dynamically adjust shadow resolution

---
{{define_cvar("lb_dynamic_shadow_resolution_base")}}
Base resolution for dynamic shadowmap sizing.  Shadowmap size of a screen sized light

---
{{define_cvar("lb_dynamic_shadow_resolution_quantization")}}
Quantization of dynamically computed shadow size

---
{{define_cvar("lb_dynamic_shadow_resolution_hysteresis")}}
Update hysteresis for shadow size

---
{{define_cvar("lb_dynamic_shadow_resolution_delay")}}
Update delay for shadow size

---
{{define_cvar("lb_timesliced_shadows_dynamic_size")}}

---
{{define_cvar("lb_enable_sunlight")}}
SceneSystem/LightBinner/Enable Sunlight

---
{{define_cvar("lb_low_quality_shader_fade_region_rescale")}}
For envmaps in low quality shader mode, how much of the fade region to scale the envmap box by.

---
{{define_cvar("lb_max_visible_envmaps_override")}}
Override maximum visible envmaps

---
{{define_cvar("lb_max_visible_barn_lights_override")}}
Override maximum visible barn lights

---
{{define_cvar("r_grass_vertex_lighting")}}

---
{{define_cvar("r_grass_alpha_test")}}

---
{{define_cvar("r_grass_start_fade")}}

---
{{define_cvar("r_grass_end_fade")}}

---
{{define_cvar("r_grass_density_mode")}}
0 = Density corresponds to blade existance, 1 = Density corresponds to blade height, 2 = Both 0 and 1

---
{{define_cvar("r_grass_quality")}}
0 = Off, 1 = Low, 2 = Med, 3 = high, 4 = ultra

---
{{define_cvar("r_grass_max_brightness_change")}}

---
{{define_cvar("r_grass_allow_flattening")}}

---
{{define_cvar("r_grass_parallel_load")}}

---
{{define_cvar("r_render_world_node_bounds")}}
Render world node bounds

---
{{define_cvar("r_lightmap_size")}}
Maximum lightmap resolution.

---
{{define_cvar("r_lightmap_size_directional_irradiance")}}
Maximum lightmap resolution for directional_irradiance channel. -1 = use value of r_lightmap_size

---
{{define_cvar("r_lightmap_set")}}
Lightmap set to use, only works on map load

---
{{define_cvar("sc_allow_precomputed_vismembers")}}

---
{{define_cvar("r_drawworld")}}
Render the world.

---
{{define_cvar("r_world_wind_strength")}}

---
{{define_cvar("r_world_wind_offset_speed")}}

---
{{define_cvar("r_world_wind_frequency_grass")}}

---
{{define_cvar("r_world_wind_frequency_trees")}}

---
{{define_cvar("r_world_wind_dir")}}

---
{{define_cvar("r_world_wind_smooth_time")}}

---
{{define_cvar("r_world_frame_load_threshold_ms")}}

---
{{define_cvar("v8_jitless")}}
Disable runtime allocation of executable memory for V8.

---
{{define_cvar("v8_stack_size")}}
Default size of stack region v8 is allowed to use (in kBytes)

---
{{define_cvar("v8_maximum_heap_size_mb")}}
Hard limit for the v8 heap size (in mBytes)

---
{{define_cvar("pulse_save_execution_history")}}
Keep a history of all instructions run on a per graph basis.

---
{{define_cvar("pulse_save_execution_history_limit")}}
Keep a history of all instructions run on a per graph basis.

---
{{define_cvar("r_particle_max_detail_level")}}
The maximum detail level of particle to create

---
{{define_cvar("particle_debug_creation_filter")}}

---
{{define_cvar("cl_max_particle_pvs_aabb_edge_length")}}

---
{{define_cvar("r_drawparticles")}}
Enable/disable particle rendering

---
{{define_cvar("r_draw_particle_children_with_parents")}}
Draw particle children with parents (-1=use gameinfo, 0=no, 1=yes)

---
{{define_cvar("r_particle_debug_filter")}}
Limit debug visualizations to substring match of effect name

---
{{define_cvar("r_particle_debug_randomseeds")}}
Use random seeds in debug

---
{{define_cvar("r_particle_fixedrandomseeds")}}
Use fixed seeds for easier debugging

---
{{define_cvar("r_particle_max_size_cull")}}
Particle systems larger than this in every dimension skip culling to save CPU.  They will be drawn anyway.

---
{{define_cvar("r_particle_render_test")}}
render particles 100 times and show perf

---
{{define_cvar("r_particle_render_refreshes_sleep_timer")}}
Disable to get a better look at what's happening offscreen

---
{{define_cvar("particles_multiplier")}}
Multiply # of rendered particles by this for perf testing

---
{{define_cvar("r_particle_warn_threshold_ms")}}
Threshold to warn about when rendering particles.

---
{{define_cvar("r_particle_min_timestep")}}
A minimum on particle simulation time, particle simulation happening more frequently than this will lerp.

---
{{define_cvar("r_particle_newinput")}}
Enable input path in particle ops

---
{{define_cvar("particle_snapshot_allow_combined_models")}}

---
{{define_cvar("r_particle_max_draw_distance")}}
The maximum distance that particles will render

---
{{define_cvar("particle_layer_id_whitelist")}}

---
{{define_cvar("cl_particle_batch_mode")}}

---
{{define_cvar("cl_particle_fallback_multiplier")}}
Multiplier for falling back to cheaper effects under load.

---
{{define_cvar("cl_particle_fallback_base")}}
Base for falling back to cheaper effects under load.

---
{{define_cvar("cl_particle_retire_cost")}}

---
{{define_cvar("cl_particle_simulate")}}
Enables/Disables Particle Simulation

---
{{define_cvar("cl_particle_max_count")}}

---
{{define_cvar("cl_aggregate_particles")}}

---
{{define_cvar("r_freezeparticles")}}
Pause particle simulation

---
{{define_cvar("r_threaded_particles")}}

---
{{define_cvar("r_limit_particle_job_duration")}}

---
{{define_cvar("r_particle_timescale")}}

---
{{define_cvar("r_particle_debug_force_simulation")}}
-1 for all asleep, 1 for all awake

---
{{define_cvar("cl_particle_log_creates")}}
Print debug message every time a particle collection is created

---
{{define_cvar("cl_particle_sim_fallback_threshold_ms")}}
Amount of simulation time that can elapse before new systems start falling back to cheaper versions

---
{{define_cvar("cl_particle_sim_fallback_base_multiplier")}}
How aggressive the switch to fallbacks will be depending on how far over the cl_particle_sim_fallback_threshold_ms the sim time is.  Higher numbers are more aggressive.

---
{{define_cvar("r_particle_cables_cast_shadows")}}

---
{{define_cvar("particle_powsimd_random_range_exp")}}

---
{{define_cvar("r_particle_max_texture_layers")}}

---
{{define_cvar("r_particle_gpu_implicit")}}

---
{{define_cvar("r_particle_gpu_implicit_debug_bricks")}}

---
{{define_cvar("r_particle_gpu_implicit_debug_wireframe")}}

---
{{define_cvar("r_particle_gpu_implicit_debug_stats")}}

---
{{define_cvar("r_particle_gpu_implicit_lds_cache")}}

---
{{define_cvar("r_particle_model_per_thread_count")}}

---
{{define_cvar("r_particle_model_old")}}

---
{{define_cvar("r_physics_particle_op_spawn_scale")}}

---
{{define_cvar("r_particle_mixed_resolution_viewstart")}}

---
{{define_cvar("r_particle_enable_fastpath")}}

---
{{define_cvar("r_particle_force_material_binds")}}

---
{{define_cvar("panorama_debugger_theme")}}

---
{{define_cvar("panorama_label_wrap_before_shrink")}}
Should labels try to wrap text before using text-overflow: shrink

---
{{define_cvar("panorama_debug_movies")}}

---
{{define_cvar("panorama_movie_async_load_size_bytes")}}

---
{{define_cvar("panorama_movie_force_not_ready_behavior")}}

---
{{define_cvar("panorama_console_position_and_size")}}

---
{{define_cvar("panorama_console_max_history")}}

---
{{define_cvar("panorama_console_max_autocomplete")}}

---
{{define_cvar("panorama_console_max_lines")}}

---
{{define_cvar("panorama_dragscroll_minflickvelocity")}}
Minimum velocity that the mouse must be moving as mouse up time to qualify as a drag scroll flick

---
{{define_cvar("panorama_dragscroll_maxflickvelocity")}}
Maximum velocity for a drag scroll flick

---
{{define_cvar("panorama_daisy_wheel")}}
Daisy wheel input mode: RS | ABXY

---
{{define_cvar("nav_smooth_relax_use_timesteps")}}

---
{{define_cvar("nav_curve_iter")}}

---
{{define_cvar("nav_curve_step")}}

---
{{define_cvar("nav_curve_max_step")}}

---
{{define_cvar("nav_curve_set")}}

---
{{define_cvar("nav_curve_lock")}}

---
{{define_cvar("nav_curve_alt")}}

---
{{define_cvar("nav_find_occluded_node_nozup_use_raycast")}}

---
{{define_cvar("navspace_debug_pathfind")}}

---
{{define_cvar("navspace_debug_stringpull")}}

---
{{define_cvar("navspace_debug_transition_calc")}}

---
{{define_cvar("navspace_path_use_water_level_locator")}}

---
{{define_cvar("population_distribution_debug")}}

---
{{define_cvar("nav_bfs_debug")}}

---
{{define_cvar("navspace_debug_trace")}}

---
{{define_cvar("navspace_create_water_transition_connections")}}

---
{{define_cvar("navspace_create_water_smooth_connections")}}

---
{{define_cvar("navspace_draw_water_changes")}}
Draw changes in water volumes

---
{{define_cvar("npcsolve_path_lookahead_const")}}

---
{{define_cvar("npcsolve_path_lookahead_dist")}}

---
{{define_cvar("npcsolve_path_close_const")}}

---
{{define_cvar("npcsolve_path_close_max_tension")}}

---
{{define_cvar("npcsolve_path_vel_const")}}

---
{{define_cvar("npcsolve_attract_draw")}}

---
{{define_cvar("npcsolve_drag_linear")}}

---
{{define_cvar("npcsolve_constraint_npc")}}

---
{{define_cvar("npcsolve_constraint_nav")}}

---
{{define_cvar("npcsolve_separation")}}

---
{{define_cvar("npcsolve_separation_const")}}

---
{{define_cvar("npcsolve_separation_dist")}}

---
{{define_cvar("npcsolve_separation_r2")}}

---
{{define_cvar("npcsolve_separation_jitter")}}

---
{{define_cvar("npcsolve_separation_draw")}}

---
{{define_cvar("npcsolve_forward")}}

---
{{define_cvar("npcsolve_forward_const")}}

---
{{define_cvar("npcsolve_forward_dist")}}

---
{{define_cvar("npcsolve_forward_margin")}}

---
{{define_cvar("fire_extinguishes_under_water")}}

---
{{define_cvar("nav_pathfind_debug_log")}}

---
{{define_cvar("nav_pathfind_draw")}}

---
{{define_cvar("nav_pathfind_draw_blocked")}}

---
{{define_cvar("nav_pathfind_draw_fail")}}

---
{{define_cvar("nav_pathfind_draw_costs")}}

---
{{define_cvar("nav_pathfind_draw_total_costs")}}

---
{{define_cvar("nav_pathfind_inadmissable_heuristic_factor")}}

---
{{define_cvar("nav_pathfind_multithread")}}

---
{{define_cvar("nav_volume_debug")}}
Draw or print debug information about nav volume queries.

---
{{define_cvar("cojob_max_no_yield_time_us")}}
Will spew if a job takes longer than the specified number of microseconds

---
{{define_cvar("cojob_lock_hold_warning_threshold_ms")}}
How long in milliseconds before we warn about lock hold duration

---
{{define_cvar("nav_test_bfs_lattice_simple")}}

---
{{define_cvar("nav_test_bfs_lattice_hex")}}
Demonstrates searching hexagonal lattice over nav mesh.

---
{{define_cvar("nav_test_detour")}}

---
{{define_cvar("nav_test_smooth")}}

---
{{define_cvar("nav_test_smooth_in_yaw")}}

---
{{define_cvar("nav_test_smooth_in_speed")}}

---
{{define_cvar("nav_test_smooth_path_speed")}}

---
{{define_cvar("nav_test_smooth_separating_dist")}}

---
{{define_cvar("nav_test_smooth_spring_const")}}

---
{{define_cvar("nav_test_smooth_spring_tension_max")}}

---
{{define_cvar("nav_test_smooth_extern_push")}}

---
{{define_cvar("nav_test_find_nearest")}}
Calculate the nearest point on the navmesh to the trace point.  Uses selection from nav_select_hull.

---
{{define_cvar("nav_test_find_nearest_clear")}}
Calculate the nearest point on the navmesh to the trace point.  Uses selection from nav_select_hull.

---
{{define_cvar("nav_test_find_z")}}

---
{{define_cvar("nav_test_multi_connection")}}

---
{{define_cvar("nav_test_split_obstacle")}}

---
{{define_cvar("nav_test_split_obstacle_size")}}

---
{{define_cvar("nav_test_split_obstacle_update_pos")}}

---
{{define_cvar("nav_test_split_obstacle_dirty")}}

---
{{define_cvar("nav_test_split_obstacle_leave")}}

---
{{define_cvar("nav_test_find_random_connected")}}
Demonstrates finding random points that are connected in the nav mesh to the start point.

---
{{define_cvar("nav_test_find_random_connected_dist_min")}}

---
{{define_cvar("nav_test_find_random_connected_dist_max")}}

---
{{define_cvar("nav_test_genrt")}}

---
{{define_cvar("nav_test_genrt_place")}}

---
{{define_cvar("nav_test_spline")}}

---
{{define_cvar("nav_test_curve_opt")}}

---
{{define_cvar("nav_test_force_npc_repath")}}

---
{{define_cvar("nav_test_npc_collision")}}

---
{{define_cvar("nav_test_npc_collision_range")}}

---
{{define_cvar("nav_test_npc_collision_show_geometry")}}

---
{{define_cvar("nav_test_npc_area")}}

---
{{define_cvar("nav_test_area_gravity")}}

---
{{define_cvar("nav_test_getnearestnav_gravity")}}

---
{{define_cvar("nav_test_getareaoverlapping_gravity")}}

---
{{define_cvar("nav_test_pos_name")}}

---
{{define_cvar("nav_test_pos_place")}}

---
{{define_cvar("nav_flow_map_enabled")}}

---
{{define_cvar("sv_no_navmesh")}}
Block loading of the navmesh. Unplayable, only used for memory sampling.

---
{{define_cvar("nav_genrt_no_split")}}

---
{{define_cvar("nav_genrt_no_splice")}}

---
{{define_cvar("nav_genrt_step")}}

---
{{define_cvar("nav_genrt_debug")}}

---
{{define_cvar("nav_obstacle_validate")}}

---
{{define_cvar("nav_obstruction_draw")}}

---
{{define_cvar("nav_obstruction_draw_dist")}}

---
{{define_cvar("nav_obstruction_draw_island")}}

---
{{define_cvar("nav_obstruction_draw_island_hull")}}

---
{{define_cvar("nav_obstruction_draw_movefail_blocking")}}

---
{{define_cvar("nav_debug_blocked")}}

---
{{define_cvar("nav_obstacle_genrt")}}

---
{{define_cvar("nav_obstruction_draw_change")}}

---
{{define_cvar("nav_avoid_obstacles")}}

---
{{define_cvar("nav_path_draw_arrow")}}

---
{{define_cvar("nav_path_draw_tick")}}

---
{{define_cvar("nav_path_draw_areas")}}

---
{{define_cvar("nav_path_draw_connected_areas")}}

---
{{define_cvar("nav_path_draw_ground_segments")}}

---
{{define_cvar("nav_path_draw_ladder_segments")}}

---
{{define_cvar("nav_path_draw_jump_segments")}}

---
{{define_cvar("nav_path_draw_climb_segments")}}

---
{{define_cvar("nav_path_draw_link_segments")}}

---
{{define_cvar("nav_path_debug_compute_with_open_goal")}}

---
{{define_cvar("nav_path_fixup_gap_segments")}}

---
{{define_cvar("nav_path_record_enable")}}

---
{{define_cvar("nav_path_record_draw_last_fail")}}

---
{{define_cvar("nav_path_optimize")}}

---
{{define_cvar("nav_path_optimize_portals")}}

---
{{define_cvar("nav_path_fixup_climb_up_segments")}}

---
{{define_cvar("nav_path_optimizer_debug")}}

---
{{define_cvar("nav_path_jump_process_debug")}}

---
{{define_cvar("nav_path_debug")}}

---
{{define_cvar("nav_smooth_enable")}}

---
{{define_cvar("nav_smooth_use_opt")}}

---
{{define_cvar("nav_smooth_constrain_results")}}

---
{{define_cvar("nav_smooth_constrain_results_relax")}}

---
{{define_cvar("nav_smooth_constrain_spring")}}

---
{{define_cvar("nav_smooth_constrain_spring_relax")}}

---
{{define_cvar("nav_smooth_draw_calc")}}

---
{{define_cvar("nav_smooth_draw_boundary")}}

---
{{define_cvar("nav_smooth_draw_constraint_spline")}}

---
{{define_cvar("nav_smooth_draw_constraint_spring")}}

---
{{define_cvar("nav_smooth_draw_speed")}}

---
{{define_cvar("nav_smooth_draw_accel")}}

---
{{define_cvar("nav_smooth_spring_enable")}}

---
{{define_cvar("nav_smooth_spring_const_override")}}

---
{{define_cvar("nav_smooth_spring_tension_max_override")}}

---
{{define_cvar("nav_smooth_spring_forward_dist_base")}}

---
{{define_cvar("nav_smooth_spring_forward_dist_time_limit")}}

---
{{define_cvar("nav_smooth_spring_factor_dist")}}

---
{{define_cvar("nav_smooth_spring_factor_deriv")}}

---
{{define_cvar("nav_smooth_spring_factor_speed")}}

---
{{define_cvar("nav_smooth_spring_max_dist")}}

---
{{define_cvar("nav_smooth_spring_timestep_min")}}

---
{{define_cvar("nav_smooth_spring_timestep_max")}}

---
{{define_cvar("nav_smooth_spring_timestep_factor_speed")}}

---
{{define_cvar("nav_smooth_spring_timestep_factor_accel")}}

---
{{define_cvar("nav_smooth_spring_yaw_rotation_speed")}}

---
{{define_cvar("nav_smooth_spring_yaw_threshold")}}

---
{{define_cvar("nav_smooth_relax")}}

---
{{define_cvar("snd_steamaudio_dynamicpathing_max_samples")}}

---
{{define_cvar("snd_steamaudio_pathing_enable_caching")}}

---
{{define_cvar("snd_steamaudio_pathing_caching_threshold")}}

---
{{define_cvar("snd_new_visualize")}}
Displays soundevent name played at it's 3d position

---
{{define_cvar("soundevent_check_networked_entity")}}

---
{{define_cvar("snd_disable_radar_visualize")}}

---
{{define_cvar("ai_debug_soundent")}}
Reports sounds being entered into the AI sound list. Set to 1 to see all sounds, set to 2 to only see DANGER sounds.

---
{{define_cvar("ai_debug_soundent_duration")}}
Length of time to display ai_debug_soundent visual displays.

---
{{define_cvar("soundpatch_captionlength")}}
How long looping soundpatch captions should display for.

---
{{define_cvar("phys_pushscale")}}

---
{{define_cvar("debug_takedamage_summaries")}}

---
{{define_cvar("tool_spawned_model_scales")}}

---
{{define_cvar("g_debug_transitions")}}
Set to 1 and restart the map to be warned if the map has no trigger_transition volumes. Set to 2 to see a dump of all entities & associated results during a transition.

---
{{define_cvar("snd_sos_debug_trigger_opvar")}}

---
{{define_cvar("teleport_trigger_debug")}}

---
{{define_cvar("sv_debug_client_not_in_pvs")}}
If set, draw failed client PVS checks with red box

---
{{define_cvar("sv_strict_notarget")}}
If set, notarget will cause entities to never think they are in the pvs

---
{{define_cvar("voice_serverdebug")}}

---
{{define_cvar("sv_alltalk")}}
Players can hear all other players' voice communication, no team restrictions

---
{{define_cvar("mp_tournament_whitelist")}}
Specifies the item whitelist file to use.

---
{{define_cvar("gc_secret_key")}}
Secret key for authenticating with the GC


---
{{define_cvar("nav_draw_area_filled")}}

---
{{define_cvar("nav_draw_area_ztest")}}

---
{{define_cvar("nav_draw_area_ids")}}

---
{{define_cvar("nav_draw_area_hull_support")}}

---
{{define_cvar("nav_draw_area_connections")}}

---
{{define_cvar("nav_draw_blocked")}}

---
{{define_cvar("nav_draw_blocked_connections")}}

---
{{define_cvar("nav_draw_connected_area_radius")}}

---
{{define_cvar("nav_draw_area_inset_margin")}}

---
{{define_cvar("nav_draw_area_should_be_destroyed")}}

---
{{define_cvar("nav_draw_area_split_by_obstacle_mgr")}}

---
{{define_cvar("nav_draw_area_split_by_nav_link_mgr")}}

---
{{define_cvar("nav_draw_externally_created")}}

---
{{define_cvar("nav_draw_area_normal")}}

---
{{define_cvar("nav_draw_area_ground")}}

---
{{define_cvar("nav_draw_area_gravity")}}

---
{{define_cvar("nav_edit")}}
Set to one to interactively edit the Navigation Mesh. Set to zero to leave edit mode.

---
{{define_cvar("nav_edit_validate")}}
Validate navmesh structures.

---
{{define_cvar("nav_space_select_dist")}}

---
{{define_cvar("nav_draw_mesh")}}

---
{{define_cvar("nav_draw_mesh_offset")}}
Vertical offset for drawing the mesh (useful for flat planes where the mesh is often a fixed offset from the physical ground

---
{{define_cvar("nav_draw_jump_links")}}

---
{{define_cvar("nav_draw_mesh_grid")}}
Draw the mesh's spatial grid structure around the edit cursor position.

---
{{define_cvar("nav_draw_markup")}}

---
{{define_cvar("nav_draw_space_swim")}}

---
{{define_cvar("nav_draw_space_fly")}}

---
{{define_cvar("nav_draw_space_radius")}}

---
{{define_cvar("nav_draw_space_neighbors")}}

---
{{define_cvar("nav_draw_space_portals")}}

---
{{define_cvar("nav_draw_space_cells")}}

---
{{define_cvar("nav_draw_space_scatter")}}

---
{{define_cvar("nav_draw_attribute_game")}}
Draw all nav areas with this game attribute

---
{{define_cvar("nav_draw_attribute_dynamic")}}
Draw all nav areas with this dynamic attribute

---
{{define_cvar("nav_draw_links")}}

---
{{define_cvar("nav_draw_link_alignment")}}

---
{{define_cvar("nav_draw_indirect_connections")}}

---
{{define_cvar("nav_show_area_info_font")}}

---
{{define_cvar("nav_show_area_info_font_size")}}

---
{{define_cvar("nav_show_area_info_font_voffset")}}

---
{{define_cvar("nav_show_area_connections")}}
Show connections to selected area when true

---
{{define_cvar("nav_show_area_verts")}}
Show area vertex positions

---
{{define_cvar("nav_show_area_water_info")}}

---
{{define_cvar("nav_select_hull")}}
Restrict area selection to areas that can support a hull of the given category

---
{{define_cvar("nav_select_allow_blocked")}}
When selecting an area under nav_edit, allow area marked as blocked.

---
{{define_cvar("nav_select_area_id")}}
Select nav area with matching ID.

---
{{define_cvar("nav_select_block_id")}}
Select nav space block with matching ID.

---
{{define_cvar("nav_draw_limit")}}
The maximum number of areas to draw in edit mode

---
{{define_cvar("nav_drag_selection_volume_zmax_offset")}}
The offset of the nav drag volume top from center

---
{{define_cvar("nav_drag_selection_volume_zmin_offset")}}
The offset of the nav drag volume bottom from center

---
{{define_cvar("nav_split_show_line")}}
Show the free split line.

---
{{define_cvar("nav_test_path")}}
Calculate and draw a path from player/camera position to the test position.

---
{{define_cvar("nav_test_path_space")}}
Should nav_test_path test 3d navigation?  1 = space to space, 2 = multi-modal space/ground

---
{{define_cvar("nav_test_path_space_fly")}}
Test flight paths

---
{{define_cvar("nav_test_path_space_swim")}}
Test swim paths

---
{{define_cvar("nav_test_path_lock_start")}}
Lock the pathfinding start to the current intersection point.

---
{{define_cvar("nav_test_path_lock_goal")}}
Lock the pathfinding goal to the current intersection point.

---
{{define_cvar("nav_test_path_opt")}}
Enable path optimization for nav_edit_path paths.

---
{{define_cvar("nav_test_path_opt_transitions")}}

---
{{define_cvar("nav_test_path_expansion_search")}}
Extend nav_test_path by doing an expansion search on that path.  Convar value defines dist.

---
{{define_cvar("nav_test_path_move")}}

---
{{define_cvar("nav_test_path_return")}}
Calculate a return path from cursor position to the path calculated by nav_test_path.

---
{{define_cvar("nav_test_rays")}}

---
{{define_cvar("nav_test_ray_space")}}

---
{{define_cvar("nav_test_boundary_zone_circle")}}

---
{{define_cvar("nav_test_boundary_zone_sphere")}}

---
{{define_cvar("nav_test_boundary_zone_path")}}

---
{{define_cvar("nav_test_boundary_zone_rays")}}

---
{{define_cvar("nav_test_boundary_zone_rays_random")}}

---
{{define_cvar("nav_test_boundary_zone_rays_margin")}}

---
{{define_cvar("nav_test_boundary_zone_force")}}

---
{{define_cvar("nav_test_boundary_zone_grid_dim")}}

---
{{define_cvar("nav_test_bfs_lattice_dist_0")}}

---
{{define_cvar("nav_test_bfs_lattice_spacing_0")}}

---
{{define_cvar("nav_test_bfs_lattice_dist_1")}}

---
{{define_cvar("nav_test_bfs_lattice_spacing_1")}}

---
{{define_cvar("nav_test_bfs_lattice_dist_2")}}

---
{{define_cvar("nav_test_bfs_lattice_spacing_2")}}

---
{{define_cvar("nav_test_bfs_lattice_mark")}}

---
{{define_cvar("nav_test_bfs_simple")}}

---
{{define_cvar("sv_rollspeed")}}

---
{{define_cvar("sv_rollangle")}}
Max view roll angle

---
{{define_cvar("sv_friction")}}
World friction.

---
{{define_cvar("sv_bounce")}}
Bounce multiplier for when physically simulated objects collide with other objects.

---
{{define_cvar("sv_maxvelocity")}}
Maximum speed any ballistically moving object is allowed to attain per axis.

---
{{define_cvar("sv_stepsize")}}

---
{{define_cvar("sv_backspeed")}}
How much to slow down backwards motion

---
{{define_cvar("sv_waterdist")}}
Vertical view fixup when eyes are near water plane.

---
{{define_cvar("sv_mover_pogofrequency")}}
The capsule pogo stick frequency [hz].

---
{{define_cvar("sv_mover_pogodampingratio")}}
The capsule pogo stick damping ratio [-]

---
{{define_cvar("sv_mover_maxslope")}}
The maximum slope the player can overcome [-]

---
{{define_cvar("r_JeepViewDampenFreq")}}

---
{{define_cvar("r_JeepViewDampenDamp")}}

---
{{define_cvar("r_JeepViewZHeight")}}

---
{{define_cvar("r_AirboatViewDampenFreq")}}

---
{{define_cvar("r_AirboatViewDampenDamp")}}

---
{{define_cvar("r_AirboatViewZHeight")}}

---
{{define_cvar("mp_restartgame")}}
If non-zero, game will restart in the specified number of seconds

---
{{define_cvar("sv_allchat")}}
Players can receive all other players' text chat, no death restrictions

---
{{define_cvar("spec_replay_bot")}}
Enable Spectator Hltv Replay when killed by bot

---
{{define_cvar("particle_test_file")}}
Name of the particle system to dynamically spawn

---
{{define_cvar("particle_test_attach_mode")}}
Possible Values: 'start_at_attachment', 'follow_attachment', 'start_at_origin', 'follow_origin'

---
{{define_cvar("particle_test_attach_attachment")}}
Attachment index for attachment mode

---
{{define_cvar("g_debug_constraint_sounds")}}
Enable debug printing about constraint sounds.

---
{{define_cvar("phys_use_block_solver")}}
Use block solving for constraint entities

---
{{define_cvar("phys_joint_teleport")}}
Teleport joint anchors if connected to world

---
{{define_cvar("phys_length_frequency")}}
Spring stiffness for length constraint

---
{{define_cvar("phys_length_damping_ratio")}}
Spring damping ratio for length constraint

---
{{define_cvar("vehicle_debug_impact_damage")}}

---
{{define_cvar("crowbar_impact_damage_scale")}}

---
{{define_cvar("crowbar_impact_damage_mass")}}

---
{{define_cvar("ent_debug_draw_thinkers")}}

---
{{define_cvar("think_limit")}}
Maximum think time in milliseconds, warning is printed if this is exceeded.

---
{{define_cvar("ragdoll_prop_sleepdisabletime")}}
Ragdoll is not allowed to physically sleep until this timer has elapsed.

---
{{define_cvar("ragdoll_prop_sleepaftertime")}}
After this many seconds of being basically stationary, the ragdoll will go to sleep.

---
{{define_cvar("ragdoll_prop_settle")}}
Enable more aggressive ragdoll settling

---
{{define_cvar("ragdoll_visualize_creation_skeleton")}}

---
{{define_cvar("ragdoll_visualize_targetpose")}}

---
{{define_cvar("ragdoll_validate_targetpose")}}

---
{{define_cvar("ragdoll_debug_item_detachment")}}

---
{{define_cvar("ragdoll_scale_sleep_tolerance")}}

---
{{define_cvar("ragdoll_override_root_orientation")}}

---
{{define_cvar("ragdoll_relax_limts")}}

---
{{define_cvar("prop_nav_ignore_mass")}}

---
{{define_cvar("prop_nav_ignore_edge_len")}}

---
{{define_cvar("prop_nav_obstacle_avoid_mass")}}

---
{{define_cvar("prop_nav_obstacle_avoid_use_connection_blocker")}}

---
{{define_cvar("prop_nav_obstacle_block_mass_a")}}

---
{{define_cvar("prop_nav_obstacle_block_edge_min_a")}}

---
{{define_cvar("prop_nav_obstacle_block_mass_b")}}

---
{{define_cvar("prop_nav_obstacle_block_edge_min_b")}}

---
{{define_cvar("prop_debug_collision")}}
Highlights props based on their collision group: COLLISION_GROUP_PROPS(white), COLLISION_GROUP_INTERACTIVE_DEBRIS(green), COLLISION_GROUP_DEBRIS and will return to COLLISION_GROUP_INTERACTIVE_DEBRIS on sleeping(bright red), COLLISION_GROUP_DEBRIS permanently (dark red), COLLISION_GROUP_DEBRIS(blue), OTHER(grey)

---
{{define_cvar("phys_shoot_speed")}}

---
{{define_cvar("phys_shoot_angular_speed")}}

---
{{define_cvar("debug_physimpact")}}

---
{{define_cvar("sv_unlag")}}
Enables player lag compensation

---
{{define_cvar("sv_showlagcompensation_rec")}}
If > 0, show lag compensation hitboxes as they're recorded. Value is for how long.

---
{{define_cvar("sv_lagcompensationforcerestore")}}
Don't test validity of a lag comp restore, just do it.

---
{{define_cvar("sv_unlag_fixstuck")}}
Disallow backtracking a player for lag compensation if it will cause them to become stuck

---
{{define_cvar("sv_unlag_debug")}}

---
{{define_cvar("physcannon_minforce")}}

---
{{define_cvar("physcannon_maxforce")}}

---
{{define_cvar("voice_player_speaking_delay_threshold")}}

---
{{define_cvar("cq_debug")}}
Verbose command queue logging.

---
{{define_cvar("cq_fake_starve")}}
if set, starve this many commands by discarding during process usercmds.

---
{{define_cvar("cq_logging")}}
command queue logging of events.

---
{{define_cvar("cq_logging_interval")}}
command queue logging per player stats every N seconds, 0 to disable.

---
{{define_cvar("cq_print_every_command")}}
print every command as we execute it

---
{{define_cvar("tv_include_usercommands")}}
HLTV streams will include player usercommands each tick

---
{{define_cvar("cq_max_starved_substitute_commands")}}
Server will stop generating substitute commands if client hasn't sent one, after N in a row

---
{{define_cvar("sv_cq_trim_bloat_remainder")}}
When trimming a bloated CQ, leave at least N more commands than the minimum

---
{{define_cvar("sv_cq_trim_bloat_space")}}
When trimming a bloated CQ, try to leave room for N more commands to be added.  0 will trim only what is needed to remove the immediate bloat, a very large value will reset the whole queue.

---
{{define_cvar("sv_cq_trim_catchup_remainder")}}
When trimming an overful CQ due to app 'catchup' request, leave at least N more commands than the minimum

---
{{define_cvar("cq_runtests")}}

---
{{define_cvar("cq_runtests_interval")}}

---
{{define_cvar("cq_runtests_broadcast_info")}}
send message to remote client console when tests change.

---
{{define_cvar("sv_remapper_range_multiplier")}}

---
{{define_cvar("sv_player_search_range")}}

---
{{define_cvar("sv_remapper_loopsoundfix")}}

---
{{define_cvar("g_debug_angularsensor")}}

---
{{define_cvar("sv_disable_querycache")}}
debug - disable trace query cache

---
{{define_cvar("g_ragdoll_maxcount")}}

---
{{define_cvar("ragdoll_lru_debug_removal")}}

---
{{define_cvar("sv_ragdoll_lru_debug")}}

---
{{define_cvar("ragdoll_lru_min_age")}}

---
{{define_cvar("g_ragdoll_important_maxcount")}}

---
{{define_cvar("scene_maxcaptionradius")}}
Only show closed captions if recipient is within this many units of speaking actor (0==disabled).

---
{{define_cvar("cc_showmissing")}}
Show missing closecaption entries.

---
{{define_cvar("cc_norepeat")}}
In multiplayer games, don't repeat captions more often than this many seconds.

---
{{define_cvar("scene_print")}}
When playing back a scene, print timing and event info to console.

---
{{define_cvar("scene_clientflex")}}
Do client side flex animation.

---
{{define_cvar("ai_debug_scripted_sequence")}}

---
{{define_cvar("sv_regeneration_force_on")}}
Cheat to test regenerative health systems

---
{{define_cvar("snd_opvar_set_point_debug")}}

---
{{define_cvar("snd_opvar_set_point_update_interval")}}

---
{{define_cvar("ai_force_serverside_ragdoll")}}

---
{{define_cvar("phys_stressbodyweights")}}

---
{{define_cvar("phys_impactforcescale")}}

---
{{define_cvar("phys_vehicleimpactforcescale")}}

---
{{define_cvar("phys_upimpactforcescale")}}

---
{{define_cvar("target_scan_use_query_cache")}}

---
{{define_cvar("ai_debug_los")}}
NPC Line-Of-Sight debug mode. If 1, solid entities that block NPC LOC will be highlighted with white bounding boxes. If 2, it'll show non-solid entities that would do it if they were solid.

---
{{define_cvar("ai_expression_optimization")}}
Disable npc background expressions when you can't see them.

---
{{define_cvar("ai_expression_frametime")}}
Maximum frametime to still play background expressions.

---
{{define_cvar("sv_regeneration_wait_time")}}

---
{{define_cvar("buddha")}}
Player takes damage but won't die

---
{{define_cvar("buddha_ignore_bots")}}
Bots always buddha 0

---
{{define_cvar("buddha_reset_hp")}}
HP to set when damaged below zero in Buddha Mode

---
{{define_cvar("sk_player_head")}}

---
{{define_cvar("sk_player_chest")}}

---
{{define_cvar("sk_player_stomach")}}

---
{{define_cvar("sk_player_arm")}}

---
{{define_cvar("sk_player_leg")}}

---
{{define_cvar("player_debug_print_damage")}}
When true, print amount and type of all damage received by player to console.

---
{{define_cvar("spec_replay_winddown_time")}}
The trailing time, in seconds, of replay past the event, including fade-out

---
{{define_cvar("vis_force")}}

---
{{define_cvar("g_debug_doors")}}

---
{{define_cvar("camera_datadriven_disable_cache")}}

---
{{define_cvar("tv_show_allchat")}}

---
{{define_cvar("commentary_available")}}
Automatically set by the game when a commentary file is available for the current map.

---
{{define_cvar("commentary")}}
Desired commentary mode state.

---
{{define_cvar("ai_debug_ragdoll_magnets")}}

---
{{define_cvar("debug_visibility_monitor")}}

---
{{define_cvar("vismon_poll_frequency")}}

---
{{define_cvar("vismon_trace_limit")}}

---
{{define_cvar("imgui_show_overlay_nav_editor")}}
Game/Nav Editor

---
{{define_cvar("r_decals_overide_fadestarttime_params")}}

---
{{define_cvar("fire_maxabsorb")}}

---
{{define_cvar("fire_absorbrate")}}

---
{{define_cvar("fire_extscale")}}

---
{{define_cvar("fire_extabsorb")}}

---
{{define_cvar("fire_heatscale")}}

---
{{define_cvar("fire_incomingheatscale")}}

---
{{define_cvar("fire_dmgscale")}}

---
{{define_cvar("fire_dmgbase")}}

---
{{define_cvar("fire_growthrate")}}

---
{{define_cvar("fire_dmginterval")}}

---
{{define_cvar("fish_dormant")}}
Turns off interactive fish behavior. Fish become immobile and unresponsive.

---
{{define_cvar("func_break_max_pieces")}}

---
{{define_cvar("func_break_reduction_factor")}}

---
{{define_cvar("sv_showladders")}}
Show bbox and dismount points for all ladders (must be set before level load.)


---
{{define_cvar("sv_ladder_slack_z_mult")}}
Difference in Z increases toward the middle of the slack ladder.


---
{{define_cvar("func_mover_debug")}}

---
{{define_cvar("func_mover_get_speed_override")}}

---
{{define_cvar("shatterglass_debug")}}

---
{{define_cvar("shatterglass_cleanup")}}

---
{{define_cvar("shatterglass_cleanup_max")}}

---
{{define_cvar("shatterglass_shard_lifetime")}}

---
{{define_cvar("shatterglass_hit_tolerance")}}

---
{{define_cvar("servercfgfile")}}

---
{{define_cvar("lservercfgfile")}}

---
{{define_cvar("mp_teamplay")}}

---
{{define_cvar("mp_forcerespawn")}}

---
{{define_cvar("decalfrequency")}}

---
{{define_cvar("check_transmit_dump_ents")}}

---
{{define_cvar("sv_parallel_checktransmit")}}
Set to 1 to use threaded checkentities for transmit/pvs on listen servers, 2 for dedicated servers.

---
{{define_cvar("sv_hide_ent_in_pvs")}}

---
{{define_cvar("sv_early_network_message_processing")}}
Processes network messages on the server before entities think, instead of at the end of the tick.

---
{{define_cvar("ent_steadystate_enable")}}

---
{{define_cvar("ent_bitvec_enable")}}

---
{{define_cvar("ent_steadystate_delay")}}
Time in seconds without network state changes until an entity is considered for trickle updates

---
{{define_cvar("net_debug_to_file")}}

---
{{define_cvar("motdfile")}}
The MOTD file to load.

---
{{define_cvar("hostfile")}}
The HOST file to load.

---
{{define_cvar("sv_shared_team_pvs")}}
PVS is shared between teams

---
{{define_cvar("sv_remove_ent_from_pvs")}}

---
{{define_cvar("sk_autoaim_mode")}}

---
{{define_cvar("mp_friendlyfire")}}
Allows team members to injure other members of their team

---
{{define_cvar("tv_delay")}}
SourceTV broadcast delay in seconds

---
{{define_cvar("tv_delay1")}}
SourceTV[instance 1] broadcast delay in seconds

---
{{define_cvar("tv_allow_static_shots")}}
Auto director uses fixed level cameras for shots

---
{{define_cvar("tv_allow_camera_man")}}
Auto director allows spectators to become camera man

---
{{define_cvar("tv_log_director_events")}}
Log game events being considered by the director

---
{{define_cvar("tv_allow_autorecording_index")}}
When >=0 restricts autorecording only to the specified TV index

---
{{define_cvar("pickup_check_period")}}

---
{{define_cvar("logic_npc_counter_debug")}}

---
{{define_cvar("markup_volume_ref_cone_angle")}}

---
{{define_cvar("sv_stopspeed")}}
Minimum stopping speed when on ground.

---
{{define_cvar("sv_noclipaccelerate")}}

---
{{define_cvar("sv_noclipspeed")}}

---
{{define_cvar("sv_noclipfriction")}}
Friction during noclip move.

---
{{define_cvar("sv_specaccelerate")}}

---
{{define_cvar("sv_specspeed")}}

---
{{define_cvar("sv_specnoclip")}}

---
{{define_cvar("sv_maxspeed")}}

---
{{define_cvar("sv_accelerate")}}

---
{{define_cvar("sv_airaccelerate")}}

---
{{define_cvar("sv_wateraccelerate")}}

---
{{define_cvar("sv_waterfriction")}}

---
{{define_cvar("sv_footsteps")}}
Play footstep sound for players

---
{{define_cvar("sv_client_min_interp_ratio")}}
This can be used to limit the value of cl_interp_ratio for connected clients (only while they are connected).


---
{{define_cvar("sv_client_max_interp_ratio")}}
This can be used to limit the value of cl_interp_ratio for connected clients (only while they are connected).

---
{{define_cvar("cq_enable")}}
Run one usercmd per server tick and maintain a buffer.  Client speeds up/slows down it's usercmd tick rate to maintain server command queue buffering.

---
{{define_cvar("cq_dilation_percentage")}}
When speeding up slowing down, this is how much

---
{{define_cvar("pawn_mimic_all")}}

---
{{define_cvar("sv_maxunlag")}}
Maximum lag compensation in seconds

---
{{define_cvar("sv_showhitregistration")}}
Display lag_compensated hitboxes. 0 = off, 1 = server only, 2 = client only, 3 = both server and client

---
{{define_cvar("disable_dynamic_prop_loading")}}
If non-zero when a map loads, dynamic props won't be loaded

---
{{define_cvar("breakable_multiplayer")}}

---
{{define_cvar("func_breakdmg_bullet")}}

---
{{define_cvar("func_breakdmg_club")}}

---
{{define_cvar("func_breakdmg_explosive")}}

---
{{define_cvar("ent_joint_axis_size")}}

---
{{define_cvar("ent_joint_names")}}

---
{{define_cvar("ent_joint_filter_substring")}}

---
{{define_cvar("ent_joint_use_bind_pose")}}

---
{{define_cvar("ent_joint_only_ik_joints")}}

---
{{define_cvar("ent_skeleton_only_ik_joints")}}

---
{{define_cvar("screenmessage_notifytime")}}
How long to display screen message text

---
{{define_cvar("imgui_domain")}}
1 == client, 2 == server

---
{{define_cvar("imgui_enable")}}
if imgui should display

---
{{define_cvar("imgui_temp_enable")}}
if imgui should display temporarily

---
{{define_cvar("imgui_enable_input")}}
if imgui should consume input

---
{{define_cvar("imgui_debug_draw_dashboard_window")}}
Dashboard/Show Dashboard

---
{{define_cvar("imgui_debug_draw_dashboard_window_toggle_focus")}}
Dashboard toggle focus

---
{{define_cvar("imgui_debug_draw_dashboard_toggle_pause")}}
Dashboard/Pause Game When Activated

---
{{define_cvar("imgui_ent_text_enable")}}
Show Entity Text in Window

---
{{define_cvar("sv_pause_on_tick")}}
Tick count to pause on

---
{{define_cvar("ent_showonlyattachment")}}

---
{{define_cvar("imgui_show_entity_browser")}}
Game/Show Entity Browser

---
{{define_cvar("imgui_entity_browser_size")}}

---
{{define_cvar("imgui_show_command_tool")}}
Game/Show Command Tool

---
{{define_cvar("imgui_show_sim_history_window")}}
Simulation History

---
{{define_cvar("imgui_show_entity_catalog")}}
Game/Show Entity Catalog

---
{{define_cvar("imgui_show_example_window")}}
Source2/Show Example Window

---
{{define_cvar("imgui_show_sound_window")}}
Source2/Show Sound Window

---
{{define_cvar("particle_cluster_debug")}}

---
{{define_cvar("particle_cluster_use_collision_hulls")}}

---
{{define_cvar("particle_cluster_nodraw")}}

---
{{define_cvar("particle_cluster_manager_search_dist")}}

---
{{define_cvar("save_async")}}

---
{{define_cvar("autosave_fully_async")}}
Set to 1 to have autosaves execute completely on the save thread, forces 'render only' mode while the save completes

---
{{define_cvar("save_fake_hitch")}}
Force a busy wait for the specified number of milliseconds during save to simulate a hitch

---
{{define_cvar("sv_autosave")}}
Set to 1 to autosave game on level transition. Does not affect autosave triggers.

---
{{define_cvar("save_screenshot")}}
0 = none, 1 = non-autosave, 2 = always, 3 = bug_only

---
{{define_cvar("save_history_count")}}
Keep this many old copies in history of autosaves and quicksaves.

---
{{define_cvar("save_spew")}}

---
{{define_cvar("save_maxarray_spew")}}
Max number of array entries to spew when using SaveRestoreIO spewing.

---
{{define_cvar("ent_messages_draw")}}
Visualizes all entity input/output activity.

---
{{define_cvar("net_showevents")}}
Dump game events to console (1=client only, 2=all).

---
{{define_cvar("net_showeventlisteners")}}
Show listening addition/removals

---
{{define_cvar("display_game_events")}}

---
{{define_cvar("phys_visualize_traces")}}

---
{{define_cvar("gamestats_file_output_directory")}}
When -gamestatsfileoutputonly is specified, file will be emitted here instead of to modpath


---
{{define_cvar("path_simple_closest_point_on_path_debug")}}

---
{{define_cvar("smoothstairs")}}
Smooth player eye z coordinate when traversing stairs.

---
{{define_cvar("sv_suppress_viewpunch")}}

---
{{define_cvar("in_button_double_press_window")}}
How short the time between presses needs to be for us to consider it a double-press

---
{{define_cvar("sv_late_commands_allowed")}}
Allow N late commands to run at 0 timescale prior to running an on-time command. Negative values for network round trip based calculation with a hard cap of the of absolute value

---
{{define_cvar("in_spewinput")}}
Spew input, 0 = off, 1 = server, 2 = client, 3 = both

---
{{define_cvar("in_spewbuttondelta")}}
Spew button deltas, 0 = off, 1 = server, 2 = client, 3 = both

---
{{define_cvar("in_spewbuttonhold")}}
Spew button hold times, 0 = off, 1 = server, 2 = client, 3 = both

---
{{define_cvar("in_spewent")}}
Which entity should we spew input for? (Useful for debugging bot input)

---
{{define_cvar("sv_condense_late_buttons")}}
When condensing late commands. Should we compress multiple moves of button presses into the target move?

---
{{define_cvar("sv_usercmd_custom_random_seed")}}
When enabled server will populate an additional random seed independent of the client

---
{{define_cvar("sv_noclipduringpause")}}
If cheats are enabled, then you can noclip with the game paused (for doing screenshots, etc.).

---
{{define_cvar("noclip_fixup")}}

---
{{define_cvar("mp_forcecamera")}}
Restricts spectator modes for dead players

---
{{define_cvar("mp_allowspectators")}}
toggles whether the server allows spectator mode or not

---
{{define_cvar("mp_fadetoblack")}}
fade a player's screen to black when he dies

---
{{define_cvar("sv_infinite_ammo")}}
Player's active weapon will never run out of ammo

---
{{define_cvar("skeleton_instance_scaleset_enable")}}

---
{{define_cvar("skeleton_instance_smear_boneflags")}}
Smear boneflags across the model.  Costs computation, but tests to make sure your bone flags are consistent.

---
{{define_cvar("phys_dynamic_scaling")}}

---
{{define_cvar("test_restoreonnewmodel")}}

---
{{define_cvar("anim_disable")}}

---
{{define_cvar("skeleton_instance_lod_optimization")}}
Compute LOD mask internally like since 2016, i.e. force all LOD groups' bones to compute

---
{{define_cvar("skel_debug")}}

---
{{define_cvar("sv_ent_showonlyhitbox")}}

---
{{define_cvar("debug_shared_random")}}

---
{{define_cvar("sv_vac_webapi_auth_key")}}
Key for when posting to vac related webapis.

---
{{define_cvar("ai_debug_speech")}}

---
{{define_cvar("rr_followup_maxdist")}}
'then ANY' or 'then ALL' response followups will be dispatched only to characters within this distance.

---
{{define_cvar("rr_thenany_score_slop")}}
When computing respondents for a 'THEN ANY' rule, all rule-matching scores within this much of the best score will be considered.

---
{{define_cvar("snd_foliage_db_loss")}}
foliage dB loss per 1200 units

---
{{define_cvar("player_debug_off_nav")}}

---
{{define_cvar("ai_off_nav_show_nearest")}}

---
{{define_cvar("ai_use_visibility_cache")}}
Sets whether or not NPCs can cache their Visibility checks against other entities. If set to 2, also tests to make sure that NPC->Target results match that of Target->NPC.

---
{{define_cvar("ai_use_visibility_cache_reciprocation")}}
Sets whether or not the visibility check cache should be reciprocal.

---
{{define_cvar("sv_standable_normal")}}

---
{{define_cvar("sv_ladder_dampen")}}
Amount to dampen perpendicular movement on a ladder

---
{{define_cvar("sv_ladder_angle")}}
Cos of angle of incidence to ladder perpendicular for applying ladder_dampen

---
{{define_cvar("sv_ladder_scale_speed")}}
Scale top speed on ladders

---
{{define_cvar("sv_falldamage_scale")}}

---
{{define_cvar("sv_water_slow_amount")}}

---
{{define_cvar("sv_jump_precision_enable")}}
Enable jump precision. Some game modes benefit from being able to turn this off.

---
{{define_cvar("bot_crouch")}}

---
{{define_cvar("sv_optimizedmovement")}}

---
{{define_cvar("sv_enablebunnyhopping")}}
Allow player speed to exceed maximum running speed

---
{{define_cvar("sv_autobunnyhopping")}}
Players automatically re-jump while holding jump button

---
{{define_cvar("dev_create_bhop_reports")}}
Whether we should create bhop reports when you jump. Reports are created for the client and server and are numbered monotonically

---
{{define_cvar("sv_showplayerhitboxes")}}
Show lag compensated hitboxes for the specified player index whenever a player fires.

---
{{define_cvar("sv_spec_use_tournament_content_standards")}}

---
{{define_cvar("slope_drop_debug")}}
Toggles a test dropping the view offset based on the slope

---
{{define_cvar("sv_server_verify_blood_on_player")}}

---
{{define_cvar("dev_cs_force_disable_move")}}
forcibly prevent players from moving

---
{{define_cvar("slope_drop_enable")}}
Toggles a test dropping the view offset based on the slope

---
{{define_cvar("slope_drop_max_offset")}}
The maximum distance to adjust the view height

---
{{define_cvar("slope_drop_off_ground_blend_speed")}}
The speed with which the slope drop is blended out when the entity leaves the ground

---
{{define_cvar("sv_cs_player_speed_has_hostage")}}

---
{{define_cvar("sv_min_jump_landing_sound")}}

---
{{define_cvar("cam_head_constraint_distance")}}
Distance to constrain first/thirdperson camera and head

---
{{define_cvar("cam_head_constraint_soft_transition")}}
Constraint soft transition distance

---
{{define_cvar("cam_head_constraint_debug")}}
Show camera head constraint debug info

---
{{define_cvar("dev_cs_ragdoll_progress_check_interval")}}

---
{{define_cvar("dev_cs_ragdoll_nudge_max_duration")}}

---
{{define_cvar("dev_cs_ragdoll_nudge_intensity")}}

---
{{define_cvar("dev_cs_ragdoll_head_ankle_delta_z_threshold")}}

---
{{define_cvar("camera_jolt_fix")}}
camera jolt fix

---
{{define_cvar("sv_max_distance_transmit_footsteps")}}
Maximum distance to transmit footstep sound effects.

---
{{define_cvar("mp_tagging_scale")}}
Scalar for player tagging modifier when hit. Lower values for greater tagging.

---
{{define_cvar("player_ping_token_cooldown")}}
Cooldown for how long it takes for a player's ping token to refresh allowing them to ping again (they get 5 tokens).

---
{{define_cvar("player_use_radius")}}

---
{{define_cvar("sv_debug_player_use")}}
Visualizes +use logic. Green cross=trace success, Red cross=trace too far, Green box=radius success

---
{{define_cvar("sv_weapon_swap_difficulty_near_hi_pri")}}
0 = Cone searches easily reach past high priority items to swap weapons. 1 = Cone searches are narrowed and require that the weapon is strictly closer. 2 = cone searches are disabled near high priority items

---
{{define_cvar("sv_use_hi_pri_context_switch_time")}}
+use search behaves as though high priority items are usable for this long after they become unusable to avoid players accidentally performing a different action.

---
{{define_cvar("sv_extract_ammo_from_dropped_weapons")}}

---
{{define_cvar("sv_guardian_refresh_ammo_for_items_on_waves")}}
List of additional weapons to refill ammo on waves.

---
{{define_cvar("mp_fists_replace_melee")}}
If enabled then when melee weapon is dropped player will have fists, when melee weapon is picked up then fists are unavailable

---
{{define_cvar("mp_weaponstay")}}

---
{{define_cvar("mp_drop_knife_enable")}}
Allows players to drop knives.

---
{{define_cvar("mp_drop_grenade_enable")}}
Allows players to drop grenades.

---
{{define_cvar("sv_sniper_tracer_mode")}}
Mode for sniper tracers. 0: legacy, 1: hide when more than sv_sniper_tracer_innacuracy inaccurate.

---
{{define_cvar("sv_sniper_tracer_innacuracy")}}
How inaccurate a sniper shot can be before we trip sv_sniper_tracer_mode behavior.

---
{{define_cvar("sv_sniper_tracer_innacuracy_length")}}
How far should the tracer draw if we trip sv_sniper_tracer_mode behavior.

---
{{define_cvar("sv_allow_ground_weapon_pickup")}}

---
{{define_cvar("sv_buymenu_open_prevents_opportunistic_pickup")}}

---
{{define_cvar("sv_allow_switching_weapon_handedness")}}

---
{{define_cvar("sv_weapon_require_use_grace_period")}}

---
{{define_cvar("sv_dev_damage_use_netvars")}}
Whether we should use network vars (true) or legacy messages (false).

---
{{define_cvar("mp_logmoney")}}
Enables money logging.  Values are: 0=off, 1=on

---
{{define_cvar("anim_dampedaccel16_timewindow")}}

---
{{define_cvar("anim_dampedaccel16_scale")}}

---
{{define_cvar("anim_damped_move_speed_timewindow")}}

---
{{define_cvar("anim_scale_wasd_input_hip_dip")}}

---
{{define_cvar("anim_scale_wasd_input_hip_swivel")}}

---
{{define_cvar("rr_debugrule")}}
If set to the name of the rule, that rule's score will be shown whenever a concept is passed into the response rules system.

---
{{define_cvar("rr_debugresponseconcept")}}
If set, rr_debugresponseconcept will print only responses testing for the specified concept

---
{{define_cvar("rr_debugresponses")}}
Show verbose matching output (1 for simple, 2 for rule scoring, 3 for noisy). If set to 4, it will only show response success/failure for npc_selected NPCs.

---
{{define_cvar("rr_debugclassname")}}
If set, rr_debugclassname will print only response tests where 'classname' corresponds to this variable. Use to filter for a specific character.

---
{{define_cvar("rr_dacmode")}}
If set to 1, enable special functionality for DAC

---
{{define_cvar("ragdoll_gravity_scale")}}

---
{{define_cvar("ragdoll_friction_scale")}}

---
{{define_cvar("ragdoll_resolve_initial_conflict")}}

---
{{define_cvar("ragdoll_resolve_separation")}}

---
{{define_cvar("ragdoll_move_entity")}}

---
{{define_cvar("ragdoll_update_from_weights")}}

---
{{define_cvar("ragdoll_parallel_pose_control")}}

---
{{define_cvar("animgraph_slope_enable")}}

---
{{define_cvar("phys_powered_ragdoll_debug")}}

---
{{define_cvar("footstep_audible_threshold")}}

---
{{define_cvar("animgraph_debug_tags")}}

---
{{define_cvar("animgraph_debug_set_filter_params")}}
Comma separated list of params to filter against when drawing debug text overlays

---
{{define_cvar("animgraph_debug_show_unreferenced_params")}}

---
{{define_cvar("footstep_debug")}}

---
{{define_cvar("footstep_force_volume")}}

---
{{define_cvar("sv_ag2_low_skel_lod")}}

---
{{define_cvar("animgraph_debug_variables")}}
Turn on to see animgraph variable changes for entities passing animgraph_debug_filterent.

---
{{define_cvar("animgraph_debug_variables_ignore_missing")}}
If set, animgraph_debug_variables won't show debug for warnings about sets to missing variables.

---
{{define_cvar("animgraph_debug_variables_ignore_nonchanges")}}
If set, animgraph_debug_variables won't show debug for variable sets that don't change the value.

---
{{define_cvar("animgraph_debug_filterent")}}
Filter setting for animgraph_debug_variables output. If set to -1, show debug for all entities. If set to 0, show debug for any NPCs that have been npc_selected. If set to >0, something other than 0, show debug for the entity with the matching entindex.

---
{{define_cvar("animgraph_enable")}}
Enable animation graph

---
{{define_cvar("animgraph_network_enable")}}
Enable animation graph networking. The setting is only read at graph creation time; to use please set on the command line.

---
{{define_cvar("animgraph_debug")}}
Debug animation graph

---
{{define_cvar("animgraph_debug_entindex")}}
The entity to specifically debug

---
{{define_cvar("animgraph_debug_animevents")}}
Print info about animevents emitted by AnimGraph

---
{{define_cvar("animgraph_record_all")}}
Automatically start recording AnimGraphs when they get created, and save them to disk when they are destroyed

---
{{define_cvar("sv_sequence_debug")}}

---
{{define_cvar("sv_sequence_debug2")}}

---
{{define_cvar("sv_sequence_model_substring")}}

---
{{define_cvar("ai_sequence_debug")}}

---
{{define_cvar("debug_destructible_parts")}}
Draw debug information for destructible parts.

---
{{define_cvar("fire_use_modifier")}}

---
{{define_cvar("sv_suppress_friendlyfire_decals")}}

---
{{define_cvar("sv_clockcorrection_msecs")}}
The server tries to keep each player's m_nTickBase withing this many msecs of the server absolute tickcount

---
{{define_cvar("sv_usercmd_execute_warning_ms")}}
Emit a warning if we spend more than N ms executing user commands for a single player

---
{{define_cvar("ent_steadystate_interval")}}
Rate at which entities can be trickled to players

---
{{define_cvar("ent_steadystate_batchsize")}}
Max number of entities to transmit to player

---
{{define_cvar("mp_plant_c4_anywhere")}}

---
{{define_cvar("mp_guardian_bomb_plant_custom_x_mark_location")}}
x,y,z to display an X for the bomb plant in guardian missions with custom bomb plant boundaries.

---
{{define_cvar("sv_c4_upright_constraint_enabled")}}
Use a constraint to keep C4 pointed upright when thrown

---
{{define_cvar("sv_c4_upright_constraint_strength")}}
How quickly the constraint converges

---
{{define_cvar("sv_c4_upright_constraint_damping")}}
Controls how much velocity is damped on the constraint. 0 = undamped wobbly spring, 1 = critically damped no wobble fast converge, >1 = over damped

---
{{define_cvar("sv_c4_center_of_mass_offset")}}
Shifts center-of-mass along z-axis from default

---
{{define_cvar("weapon_land_dip_amt")}}
The amount the gun should dip when the player lands after a jump.

---
{{define_cvar("weapon_accuracy_forcespread")}}
Force spread to the specified value.

---
{{define_cvar("weapon_accuracy_nospread")}}
Disable weapon inaccuracy spread

---
{{define_cvar("weapon_air_spread_scale")}}
Scale factor for jumping inaccuracy, set to 0 to make jumping accuracy equal to standing

---
{{define_cvar("weapon_reticle_knife_show")}}
When enabled will show knife reticle on clients. Used for game modes requiring target id display when holding a knife.

---
{{define_cvar("weapon_auto_cleanup_time")}}
If set to non-zero, weapons will delete themselves after the specified time (in seconds) if no players are near.

---
{{define_cvar("weapon_max_before_cleanup")}}
If set to non-zero, will remove the oldest dropped weapon to maintain the specified number of dropped weapons in the world.

---
{{define_cvar("weapon_sound_falloff_multiplier")}}
Scaling for falloff of weapon firing sounds

---
{{define_cvar("dev_cs_frame_firing_enable")}}
Enable that firing will pretend like it's happening on frames.

---
{{define_cvar("dev_cs_frame_firing_tick_offset_enable")}}
Should we offset the current frame to the tick

---
{{define_cvar("dev_cs_frame_firing_skip_first_frame_enable")}}
Should we skip the first frame of shooting to make the animation punchier?

---
{{define_cvar("dev_cs_frame_firing_insert_idle_pose_now")}}
Should we insert the idle pose at this time to make the animation interpolation punchier?

---
{{define_cvar("dev_cs_frame_firing_play_animevents")}}
Should we play the animevents that animgraph will skip over?

---
{{define_cvar("sv_turning_inaccuracy_enabled")}}

---
{{define_cvar("sv_turning_inaccuracy_angle_min")}}

---
{{define_cvar("sv_turning_inaccuracy_decay")}}

---
{{define_cvar("sv_strafing_inaccuracy_enabled")}}

---
{{define_cvar("sv_strafing_inaccuracy_bias")}}

---
{{define_cvar("sv_strafing_inaccuracy_scale")}}

---
{{define_cvar("weapon_skin_force_legacy")}}

---
{{define_cvar("weapon_accuracy_reset_on_deploy")}}
On deploy, forcibly reset weapon accuracy to zero.

---
{{define_cvar("mp_weapon_next_owner_touch_time")}}

---
{{define_cvar("mp_weapon_prev_owner_touch_time")}}

---
{{define_cvar("sv_csgo_shoot_log")}}

---
{{define_cvar("sv_csgo_shoot_log_attack_cmds_only")}}

---
{{define_cvar("sv_csgo_shoot_verify")}}

---
{{define_cvar("sv_csgo_shoot_assert_lagcompensation_error")}}

---
{{define_cvar("sv_csgo_shoot_lagcompensation_max_error")}}
Warn if lag compensated head hitbox position doesn't match that on client.

---
{{define_cvar("sv_csgo_shoot_verify_on_attack_only")}}
Only run lag compensation error check when primary attack goes down.

---
{{define_cvar("sv_csgo_shoot_use_full_interp")}}

---
{{define_cvar("sv_csgo_shoot_force_full_interp")}}

---
{{define_cvar("sv_csgo_shoot_force_use_target_time")}}

---
{{define_cvar("sv_fistpunch_damage")}}

---
{{define_cvar("sv_fistpunch_damage_to_player_multiplier")}}

---
{{define_cvar("sv_fistpunch_damage_hard")}}

---
{{define_cvar("sv_fistpunch_viewmove")}}

---
{{define_cvar("sv_fistpunch_impact_sounds")}}

---
{{define_cvar("sv_shield_explosive_damage_scale")}}

---
{{define_cvar("sv_shield_explosive_damage_mult")}}

---
{{define_cvar("sv_shield_explosive_damage_cap")}}

---
{{define_cvar("sv_shield_explosive_damage_mindist")}}

---
{{define_cvar("sv_shield_explosive_damage_crouch_bonus")}}

---
{{define_cvar("sv_shield_hitpoints")}}

---
{{define_cvar("sv_shield_bash_damage_to_players")}}

---
{{define_cvar("sv_shield_bash_damage_to_nonplayer")}}

---
{{define_cvar("mp_taser_recharge_time")}}
Determines recharge time for taser. -1 = disabled.

---
{{define_cvar("spec_freeze_time")}}
Time spend frozen in observer freeze cam.

---
{{define_cvar("spec_freeze_traveltime")}}
Time taken to zoom in to frame a target in observer freeze cam.

---
{{define_cvar("spec_freeze_time_lock")}}
Time players are prevented from skipping the freeze cam

---
{{define_cvar("spec_freeze_deathanim_time")}}
The time that the death cam will spend watching the player's ragdoll before going into the freeze death cam.

---
{{define_cvar("sv_spawn_afk_bomb_drop_time")}}
Players that have never moved since they spawned will drop the bomb after this amount of time.

---
{{define_cvar("sv_showimpacts_penetration")}}
Shows extra data when bullets penetrate. (use sv_showimpacts_time to increase time shown)

---
{{define_cvar("sv_showimpacts")}}
Shows client (red) and server (blue) bullet impact point (1=both, 2=client-only, 3=server-only)

---
{{define_cvar("sv_showimpacts_time")}}
Duration bullet impact indicators remain before disappearing

---
{{define_cvar("sv_showbullethits")}}
1=show hits and near misses, 2=show hits only

---
{{define_cvar("ff_damage_reduction_grenade")}}
How much to reduce damage done to teammates by a thrown grenade.  Range is from 0 - 1 (with 1 being damage equal to what is done to an enemy)

---
{{define_cvar("ff_damage_reduction_grenade_self")}}
How much to damage a player does to himself with his own grenade.  Range is from 0 - 1 (with 1 being damage equal to what is done to an enemy)

---
{{define_cvar("ff_damage_reduction_bullets")}}
How much to reduce damage done to teammates when shot.  Range is from 0 - 1 (with 1 being damage equal to what is done to an enemy)

---
{{define_cvar("ff_damage_reduction_other")}}
How much to reduce damage done to teammates by things other than bullets and grenades.  Range is from 0 - 1 (with 1 being damage equal to what is done to an enemy)

---
{{define_cvar("ff_damage_bullet_penetration")}}
If friendly fire is off, this will scale the penetration power and damage a bullet does when penetrating another friendly player

---
{{define_cvar("sv_clip_penetration_traces_to_players")}}

---
{{define_cvar("sv_autobuyammo")}}
Enable automatic ammo purchase when inside buy zones during buy periods

---
{{define_cvar("mp_promoted_item_enabled")}}
Allow the purchasing of the promoted item.

---
{{define_cvar("sv_limit_buyrandom_per_life")}}
Enable to limit buyrandom command to only run once per player life

---
{{define_cvar("sv_nomvp")}}
Disable MVP awards.

---
{{define_cvar("sv_disconnected_player_data_hold_time")}}
Duration, in seconds, to hold onto the data of disconnected players, for scoreboard display.

---
{{define_cvar("sv_runcmds")}}

---
{{define_cvar("sv_mute_players_with_social_penalties")}}

---
{{define_cvar("sv_damage_prediction_allowed")}}

---
{{define_cvar("sv_predictable_damage_tag_ticks")}}
Delay player slowdown when damaged by # ticks to reduce misprediction effects

---
{{define_cvar("healthshot_healthboost_damage_multiplier")}}

---
{{define_cvar("CS_WarnFriendlyDamageInterval")}}
Defines how frequently the server notifies clients that a player damaged a friend

---
{{define_cvar("mp_flinch_punch_scale")}}
Scalar for first person view punch when getting hit.

---
{{define_cvar("phys_playerscale")}}
This multiplies the bullet impact impuse on players for more dramatic results when players are shot.

---
{{define_cvar("phys_headshotscale")}}
Modifier for the headshot impulse hits on players

---
{{define_cvar("sv_guardian_extra_equipment_ct")}}
Extra starting equipment for CT players in guardian modes

---
{{define_cvar("sv_guardian_extra_equipment_t")}}
Extra starting equipment for Terrorist players in guardian modes

---
{{define_cvar("dev_create_move_report")}}
Whether we should create move reports when you push movement keys. Reports are created for the server and are numbered monotonically

---
{{define_cvar("sv_update_animgraph_movement_in_finish")}}
Whether we should update animgraph movement in FinishMove.

---
{{define_cvar("sv_staminajumpcost")}}
Stamina penalty for jumping

---
{{define_cvar("sv_staminalandcost")}}
Stamina penalty for landing

---
{{define_cvar("sv_staminarecoveryrate")}}
Rate at which stamina recovers (units/sec)

---
{{define_cvar("sv_staminamax")}}
Maximum stamina penalty

---
{{define_cvar("sv_jump_spam_penalty_time")}}
For subtick jumps, if this much time has elapsed since the last time the user has pressed the jump key, pretend they hadn't. Lowering this makes bunnyhopping easier.

---
{{define_cvar("sv_timebetweenducks")}}
Minimum time before recognizing consecutive duck key

---
{{define_cvar("sv_accelerate_use_weapon_speed")}}

---
{{define_cvar("sv_accelerate_debug_speed")}}

---
{{define_cvar("sv_show_move_collisions")}}
Enable this to visualize collisions between player and geometry.

---
{{define_cvar("sv_step_move_vel_min")}}
Min velocity for step move.

---
{{define_cvar("sv_extreme_strafe_accuracy_fishtail")}}
Number of degrees of aim 'fishtail' when making an extreme strafe direction change

---
{{define_cvar("sv_jump_impulse")}}
Initial upward velocity for player jumps; sqrt(2*gravity*height).

---
{{define_cvar("sv_air_max_wishspeed")}}

---
{{define_cvar("view_punch_decay")}}
Decay factor exponent for view punch

---
{{define_cvar("sv_walkable_normal")}}

---
{{define_cvar("mp_endmatch_votenextmap_wargames_nummaps")}}
Maximum number of maps to include in endmatch voting during War Games

---
{{define_cvar("mp_endmatch_votenextmap_wargames_nummodes")}}
Maximum number of other War Games to include in endmatch voting during War Games

---
{{define_cvar("cash_team_terrorist_win_bomb")}}

---
{{define_cvar("cash_team_elimination_hostage_map_t")}}

---
{{define_cvar("cash_team_elimination_hostage_map_ct")}}

---
{{define_cvar("cash_team_elimination_bomb_map")}}

---
{{define_cvar("cash_team_win_by_time_running_out_hostage")}}

---
{{define_cvar("cash_team_win_by_time_running_out_bomb")}}

---
{{define_cvar("cash_team_win_by_defusing_bomb")}}

---
{{define_cvar("cash_team_win_by_hostage_rescue")}}

---
{{define_cvar("cash_team_loser_bonus")}}

---
{{define_cvar("cash_team_loser_bonus_consecutive_rounds")}}

---
{{define_cvar("cash_team_winner_bonus_consecutive_rounds")}}

---
{{define_cvar("cash_team_rescued_hostage")}}

---
{{define_cvar("cash_team_hostage_alive")}}

---
{{define_cvar("cash_team_planted_bomb_but_defused")}}

---
{{define_cvar("cash_team_hostage_interaction")}}

---
{{define_cvar("cash_team_bonus_shorthanded")}}

---
{{define_cvar("cash_player_killed_teammate")}}

---
{{define_cvar("cash_player_killed_enemy_factor")}}

---
{{define_cvar("cash_player_killed_enemy_default")}}

---
{{define_cvar("cash_player_bomb_planted")}}

---
{{define_cvar("cash_player_bomb_defused")}}

---
{{define_cvar("cash_player_rescued_hostage")}}

---
{{define_cvar("cash_player_interact_with_hostage")}}

---
{{define_cvar("cash_player_damage_hostage")}}

---
{{define_cvar("cash_player_killed_hostage")}}

---
{{define_cvar("cash_player_respawn_amount")}}

---
{{define_cvar("cash_player_get_killed")}}

---
{{define_cvar("mp_solid_teammates")}}
How solid are teammates: 0 = transparent; 1 = fully solid; 2 = can stand on top of heads

---
{{define_cvar("mp_free_armor")}}
Determines whether kevlar (1+) and/or helmet (2+) are given automatically.

---
{{define_cvar("mp_max_armor")}}
Determines the highest level of armor allowed to be purchased. (0) None, (1) Kevlar, (2) Helmet

---
{{define_cvar("mp_halftime")}}
Determines whether the match switches sides in a halftime event.

---
{{define_cvar("mp_randomspawn")}}
Determines whether players are to spawn. 0 = default; 1 = both teams; 2 = Terrorists; 3 = CTs.

---
{{define_cvar("mp_randomspawn_los")}}
If using mp_randomspawn, determines whether to test Line of Sight when spawning.

---
{{define_cvar("mp_randomspawn_dist")}}
If using mp_randomspawn, determines whether to test distance when selecting this spot.

---
{{define_cvar("sv_competitive_minspec")}}
Enable to force certain client convars to minimum/maximum values to help prevent competitive advantages.

---
{{define_cvar("mp_retake_t_count")}}
Number of terrorists when playing retakes.

---
{{define_cvar("mp_retake_ct_count")}}
Number of CT's when playing retakes.

---
{{define_cvar("mp_retake_ct_loadout_default_pistol_round")}}
CT Loadouts for default pistol round when playing bomb site retake.

---
{{define_cvar("mp_retake_ct_loadout_upgraded_pistol_round")}}
CT Loadouts for upgraded pistol round when playing bomb site retake.

---
{{define_cvar("mp_retake_ct_loadout_light_buy_round")}}
CT Loadouts for force buy round when playing bomb site retake.

---
{{define_cvar("mp_retake_ct_loadout_full_buy_round")}}
CT Loadouts for full buy round when playing bomb site retake.

---
{{define_cvar("mp_retake_ct_loadout_bonus_card_availability")}}
CT bonus card availability pattern for full buy round when playing bomb site retake.

---
{{define_cvar("mp_retake_ct_loadout_bonus_card")}}
CT bonus card for full buy round when playing bomb site retake.

---
{{define_cvar("mp_retake_ct_loadout_enemy_card")}}
CT enemy card for full buy round when playing bomb site retake.

---
{{define_cvar("mp_retake_t_loadout_default_pistol_round")}}
T Loadouts for default pistol round when playing bomb site retake.

---
{{define_cvar("mp_retake_t_loadout_upgraded_pistol_round")}}
T Loadouts for upgraded pistol round when playing bomb site retake.

---
{{define_cvar("mp_retake_t_loadout_light_buy_round")}}
T Loadouts for force buy round when playing bomb site retake.

---
{{define_cvar("mp_retake_t_loadout_full_buy_round")}}
T Loadouts for full buy round when playing bomb site retake.

---
{{define_cvar("mp_retake_t_loadout_bonus_card_availability")}}
T bonus card availability pattern for full buy round when playing bomb site retake.

---
{{define_cvar("mp_retake_t_loadout_bonus_card")}}
T bonus card for full buy round when playing bomb site retake.

---
{{define_cvar("mp_retake_t_loadout_enemy_card")}}
T enemy card for full buy round when playing bomb site retake.

---
{{define_cvar("mp_retake_max_consecutive_rounds_same_target_site")}}
Limit the number of consecutive rounds targeting the same site.

---
{{define_cvar("mp_teammates_are_enemies")}}
When set, your teammates act as enemies and all players are valid targets.

---
{{define_cvar("mp_buy_anywhere")}}
When set, players can buy anywhere, not only in buyzones. 0 = default. 1 = both teams. 2 = Terrorists. 3 = Counter-Terrorists.

---
{{define_cvar("mp_buy_during_immunity")}}
When set, players can buy when immune, ignoring buytime. 0 = default. 1 = both teams. 2 = Terrorists. 3 = Counter-Terrorists.

---
{{define_cvar("mp_only_cts_rescue_hostages")}}

---
{{define_cvar("hostage_debug")}}
Show hostage AI debug information

---
{{define_cvar("hostage_is_silent")}}
When set, the hostage won't play any code driven response rules lines

---
{{define_cvar("sv_force_team_intro_variant")}}

---
{{define_cvar("sv_force_team_intro_random")}}

---
{{define_cvar("imgui_show_bullets")}}
CSGO/Bullets

---
{{define_cvar("imgui_show_grenades_window")}}
CS2/Show Grenades History

---
{{define_cvar("sv_pushaway_force")}}
How hard physics objects are pushed away from the players on the server.

---
{{define_cvar("sv_pushaway_min_player_speed")}}
If a player is moving slower than this, don't push away physics objects (enables ducking behind things).

---
{{define_cvar("sv_pushaway_max_force")}}
Maximum amount of force applied to physics objects by players.

---
{{define_cvar("sv_pushaway_clientside")}}
Clientside physics push away (0=off, 1=only localplayer, 1=all players)

---
{{define_cvar("sv_pushaway_player_force")}}
How hard the player is pushed away from physics objects (falls off with inverse square of distance).

---
{{define_cvar("sv_pushaway_max_player_force")}}
Maximum of how hard the player is pushed away from physics objects.

---
{{define_cvar("sv_turbophysics")}}
Turns on turbo physics

---
{{define_cvar("steamworks_sessionid_server")}}
The server session ID for the new steamworks gamestats.

---
{{define_cvar("sv_grenade_trajectory_time_spectator")}}
Length of time grenade trajectory remains visible as a spectator.

---
{{define_cvar("sv_grenade_trajectory_prac_trailtime")}}
Shows grenade trajectory practice visualization for this number of seconds.

---
{{define_cvar("sv_grenade_trajectory_prac_pipreview")}}
Shows grenade trajectory practice picture-in-picture preview.

---
{{define_cvar("vm_debug")}}

---
{{define_cvar("healthshot_health")}}

---
{{define_cvar("healthshot_healthboost_time")}}

---
{{define_cvar("healthshot_healthboost_speed_multiplier")}}

---
{{define_cvar("healthshot_allow_use_at_full")}}

---
{{define_cvar("sv_health_approach_enabled")}}

---
{{define_cvar("sv_health_approach_speed")}}

---
{{define_cvar("molotov_throw_detonate_time")}}

---
{{define_cvar("weapon_molotov_maxdetonateslope")}}
Maximum angle of slope on which the molotov will detonate

---
{{define_cvar("molotov_usethrow_direction")}}

---
{{define_cvar("cl_smoke_origin_height")}}

---
{{define_cvar("cl_smoke_torus_ring_radius")}}

---
{{define_cvar("cl_smoke_torus_ring_subradius")}}

---
{{define_cvar("cl_smoke_edge_feather")}}

---
{{define_cvar("cl_smoke_lower_speed")}}

---
{{define_cvar("smoke_grenade_custom_color")}}
0 = Gray (classic), 1 = Red, 2 = Orange, 3 = Skyblue, 4 = Yellow, 5 = Green, , 6 = Blue, 7 = Purple, 8 = pink 

---
{{define_cvar("smoke_grenade_ct_color")}}

---
{{define_cvar("smoke_grenade_t_color")}}

---
{{define_cvar("smoke_param1")}}

---
{{define_cvar("smoke_param2")}}

---
{{define_cvar("smoke_param3")}}

---
{{define_cvar("smoke_param4")}}

---
{{define_cvar("smoke_param5")}}

---
{{define_cvar("smoke_use_noise_texture")}}

---
{{define_cvar("sv_ignoregrenaderadio")}}
Turn off Fire in the hole messages

---
{{define_cvar("mp_match_end_changelevel")}}
At the end of the match, perform a changelevel even if next map is the same

---
{{define_cvar("mp_defuser_allocation")}}
How to allocate defusers to CTs at start or round: 0=none, 1=random, 2=everyone

---
{{define_cvar("mp_give_player_c4")}}
Whether this map should spawn a c4 bomb for a player or not.

---
{{define_cvar("mp_require_gun_use_to_acquire")}}
Whether guns must be +used to acquire or default is touch-to-pickup

---
{{define_cvar("mp_death_drop_gun")}}
Which gun to drop on player death: 0=none, 1=best, 2=current or best

---
{{define_cvar("mp_death_drop_c4")}}
Whether c4 is droppable

---
{{define_cvar("mp_death_drop_grenade")}}
Which grenade to drop on player death: 0=none, 1=best, 2=current or best, 3=all grenades

---
{{define_cvar("mp_death_drop_defuser")}}
Drop defuser on player death

---
{{define_cvar("mp_death_drop_taser")}}
Drop taser on player death

---
{{define_cvar("mp_death_drop_breachcharge")}}
Drop breachcharge on player death

---
{{define_cvar("mp_death_drop_healthshot")}}
Drop healthshot on player death

---
{{define_cvar("mp_force_pick_time")}}
The amount of time a player has on the team screen to make a selection before being auto-teamed

---
{{define_cvar("bot_autodifficulty_threshold_low")}}
Lower bound below Average Human Contribution Score that a bot must be below to change its difficulty

---
{{define_cvar("bot_autodifficulty_threshold_high")}}
Upper bound above Average Human Contribution Score that a bot must be above to change its difficulty

---
{{define_cvar("mp_equipment_reset_rounds")}}
Reset all player equipment every N rounds (0 for never)

---
{{define_cvar("mp_economy_reset_rounds")}}
Reset all player money every N rounds (0 for never)

---
{{define_cvar("mp_weapons_allow_zeus")}}
Determines how many Zeus purchases a player can make per round (0 to disallow, -1 to have no limit).

---
{{define_cvar("mp_weapons_allow_pistols")}}
Determines which team, if any, can purchase Pistols. -1 = any; 0 = non; 2 = Ts; 3 = CTs.

---
{{define_cvar("mp_weapons_allow_smgs")}}
Determines which team, if any, can purchase SMGs. -1 = any; 0 = non; 2 = Ts; 3 = CTs.

---
{{define_cvar("mp_weapons_allow_heavy")}}
Determines which team, if any, can purchase Heavy guns. -1 = any; 0 = non; 2 = Ts; 3 = CTs.

---
{{define_cvar("mp_weapons_allow_rifles")}}
Determines which team, if any, can purchase Rifles. -1 = any; 0 = non; 2 = Ts; 3 = CTs.

---
{{define_cvar("mp_weapons_allow_heavyassaultsuit")}}
Determines whether heavyassaultsuit is permitted.

---
{{define_cvar("mp_heavyassaultsuit_cooldown")}}
Determines cooldown of purchase.

---
{{define_cvar("mp_weapons_allow_typecount")}}
Determines how many purchases of each weapon type allowed per player per round (0 to disallow purchasing, -1 to have no limit).

---
{{define_cvar("mp_weapons_allow_map_placed")}}
If this convar is set, when a match starts, the game will not delete weapons placed in the map.

---
{{define_cvar("mp_default_team_winner_no_objective")}}
If the map doesn't define an objective (bomb, hostage, etc), the value of this convar will declare the winner when the time runs out in the round.

---
{{define_cvar("mp_respawn_on_death_t")}}
When set to 1, terrorists will respawn after dying.

---
{{define_cvar("mp_respawn_on_death_ct")}}
When set to 1, counter-terrorists will respawn after dying.

---
{{define_cvar("mp_use_respawn_waves")}}
When set to 1, and that player's team is set to respawn, they will respawn in waves. If set to 2, teams will respawn when the whole team is dead.

---
{{define_cvar("mp_items_prohibited")}}
Set this convar to a comma-delimited list of definition indices of weapons that should be prohibited from use.

---
{{define_cvar("mp_respawnwavetime_ct")}}
Time between respawn waves for CTs.

---
{{define_cvar("mp_respawnwavetime_t")}}
Time between respawn waves for Terrorists.

---
{{define_cvar("mp_competitive_endofmatch_extra_time")}}
After a competitive match finishes rematch voting extra time is given for rankings.

---
{{define_cvar("mp_endmatch_votenextmap")}}
Whether or not players vote for the next map at the end of the match when the final scoreboard comes up

---
{{define_cvar("mp_endmatch_votenextmap_keepcurrent")}}
If set, keeps the current map in the list of voting options.  If not set, the current map will not appear in the list of voting options.

---
{{define_cvar("mp_endmatch_votenextleveltime")}}
If mp_endmatch_votenextmap is set, players have this much time to vote on the next map at match end.

---
{{define_cvar("sv_endmatch_item_drop_interval")}}
The time between drops on the end match scoreboard 

---
{{define_cvar("sv_endmatch_item_drop_interval_rare")}}
The time between drops on the end match scoreboard for rare items 

---
{{define_cvar("sv_endmatch_item_drop_interval_mythical")}}
The time between drops on the end match scoreboard for mythical items 

---
{{define_cvar("sv_endmatch_item_drop_interval_legendary")}}
The time between drops on the end match scoreboard for legendary items 

---
{{define_cvar("sv_endmatch_item_drop_interval_ancient")}}
The time between drops on the end match scoreboard for ancient items 

---
{{define_cvar("sv_compute_per_bot_difficulty")}}
0 = compute all bot difficulties equally, 1 = compute unique bot difficulty for each bot 

---
{{define_cvar("sv_show_bot_difficulty_in_name")}}
0 = hide bot difficulty in bot name, 1 = show bot difficulty in bot name

---
{{define_cvar("sv_bot_difficulty_kbm")}}
Bot difficulty while playing with Keyboard/Mouse device

---
{{define_cvar("sv_kick_ban_duration")}}
How long should a kick ban from the server should last (in minutes)

---
{{define_cvar("sv_disable_immunity_alpha")}}
If set, clients won't slam the player model render settings each frame for immunity [mod authors use this]

---
{{define_cvar("sv_deadtalk")}}
Dead players can speak (voice, text) to the living

---
{{define_cvar("sv_full_alltalk")}}
Any player (including Spectator team) can speak to any other player

---
{{define_cvar("sv_talk_enemy_dead")}}
Dead players can hear all dead enemy communication (voice, chat)

---
{{define_cvar("sv_talk_enemy_living")}}
Living players can hear all living enemy communication (voice, chat)

---
{{define_cvar("sv_talk_after_dying_time")}}
The number of seconds a player can continue talking after dying as if they were still alive

---
{{define_cvar("sv_auto_full_alltalk_during_warmup_half_end")}}
When enabled will automatically turn on full all talk mode in warmup, at halftime and at the end of the match

---
{{define_cvar("sv_spec_hear")}}
Determines who spectators can hear: 0: only spectators; 1: all players; 2: spectated team; 3: self only; 4: nobody

---
{{define_cvar("mp_c4timer")}}
how long from when the C4 is armed until it blows

---
{{define_cvar("mp_damage_headshot_only")}}
Determines whether non-headshot hits do any damage.

---
{{define_cvar("mp_damage_scale_ct_body")}}
Scales the damage a CT player takes by this much when they take damage in the body. (1 == 100%, 0.5 == 50%)

---
{{define_cvar("mp_damage_scale_ct_head")}}
Scales the damage a CT player takes by this much when they take damage in the head (1 == 100%, 0.5 == 50%).  REMEMBER! headshots do 4x the damage of the body before this scaler is applied.

---
{{define_cvar("mp_damage_scale_t_body")}}
Scales the damage a T player takes by this much when they take damage in the body. (1 == 100%, 0.5 == 50%)

---
{{define_cvar("mp_damage_scale_t_head")}}
Scales the damage a T player takes by this much when they take damage in the head (1 == 100%, 0.5 == 50%).	 REMEMBER! headshots do 4x the damage of the body before this scaler is applied.

---
{{define_cvar("dev_reportmoneychanges")}}
Displays money account changes for players in the console

---
{{define_cvar("mp_roundtime")}}
How many minutes each round takes.

---
{{define_cvar("mp_roundtime_hostage")}}
How many minutes each round of Hostage Rescue takes. If 0 then use mp_roundtime instead.

---
{{define_cvar("mp_roundtime_defuse")}}
How many minutes each round of Bomb Defuse takes. If 0 then use mp_roundtime instead.

---
{{define_cvar("mp_team_intro_time")}}
How many seconds for team intro

---
{{define_cvar("mp_freezetime")}}
how many seconds to keep players frozen when the round starts

---
{{define_cvar("mp_limitteams")}}
Max # of players 1 team can have over another (0 disables check)

---
{{define_cvar("mp_tkpunish")}}
Will TK'ers and team damagers be punished in the next round?  {0=no,  1=yes}

---
{{define_cvar("mp_autokick")}}
Kick idle/team-killing/team-damaging players

---
{{define_cvar("mp_suicide_penalty")}}
Punish players for suicides

---
{{define_cvar("mp_spawnprotectiontime")}}
Kick players who team-kill within this many seconds of a round restart.

---
{{define_cvar("mp_td_spawndmgthreshold")}}
The damage threshold players have to exceed at the start of the round to be warned/kick.

---
{{define_cvar("mp_td_dmgtowarn")}}
The damage threshhold players have to exceed in a match to get warned that they are about to be kicked.

---
{{define_cvar("mp_td_dmgtokick")}}
The damage threshhold players have to exceed in a match to get kicked.

---
{{define_cvar("mp_humanteam")}}
Restricts human players to a single team {any, CT, T}

---
{{define_cvar("mp_ignore_round_win_conditions")}}
Ignore conditions which would end the current round

---
{{define_cvar("mp_dogtag_pickup_rule")}}
Who is eligible to pick up a dogtag (0 = killer only, 1 = killer's team, 2 = victim's team, 3 = killer & victim's team, 4 = anyone)

---
{{define_cvar("mp_dogtag_despawn_on_killer_death")}}
Whether dogtags should despawn when their killer dies

---
{{define_cvar("mp_dogtag_despawn_time")}}
How many seconds dogtags should stay around before despawning automatically (0 = infinite)

---
{{define_cvar("mp_weapon_self_inflict_amount")}}
If Set to non-0, will hurt the attacker by the specified fraction of max damage if they miss.

---
{{define_cvar("mp_damage_vampiric_amount")}}
If Set to non-0, will determine the fraction of damage dealt that will be given to attacker.

---
{{define_cvar("mp_global_damage_per_second")}}
If above 0, deal non-lethal damage to players over time.

---
{{define_cvar("contributionscore_assist_reqs")}}
extra requirements to earn contribution score for an assist

---
{{define_cvar("contributionscore_assist")}}
amount of contribution score added for an assist

---
{{define_cvar("contributionscore_kill_reqs")}}
extra requirements to earn contribution score for a kill

---
{{define_cvar("contributionscore_kill")}}
amount of contribution score added for a kill

---
{{define_cvar("contributionscore_objective_kill")}}
amount of contribution score added for an objective related kill

---
{{define_cvar("contributionscore_hostage_rescue_minor")}}
amount of contribution score added to all alive CTs per hostage rescued

---
{{define_cvar("contributionscore_hostage_rescue_major")}}
amount of contribution score added to rescuer per hostage rescued

---
{{define_cvar("contributionscore_bomb_defuse_minor")}}
amount of contribution score for defusing a bomb after eliminating enemy team

---
{{define_cvar("contributionscore_bomb_defuse_major")}}
amount of contribution score for defusing a bomb while at least one enemy remains alive

---
{{define_cvar("contributionscore_bomb_planted")}}
amount of contribution score for planting a bomb

---
{{define_cvar("contributionscore_bomb_exploded")}}
amount of contribution score awarded to bomb planter and terrorists remaining alive if bomb explosion wins the round

---
{{define_cvar("contributionscore_participation")}}
amount of contribution score awarded to players for active participation in the round

---
{{define_cvar("contributionscore_suicide")}}
amount of contribution score for a suicide, normally negative

---
{{define_cvar("contributionscore_team_kill")}}
amount of contribution score for a team kill, normally negative

---
{{define_cvar("contributionscore_hostage_kill")}}
amount of contribution score for killing a hostage, normally negative

---
{{define_cvar("contributionscore_cash_bundle")}}
amount of contribution score for picking up a cash bundle

---
{{define_cvar("contributionscore_crate_break")}}
amount of contribution score for breaking an item crate

---
{{define_cvar("contributionscore_kill_factor")}}
percentage of victim's contribution score to award to their killer as a bonus

---
{{define_cvar("mp_endmatch_votenextmap_wargames_modes")}}
Modes available for endmatch voting during War Games. Separate names with spaces.

---
{{define_cvar("mp_timelimit")}}
game time per map in minutes

---
{{define_cvar("mp_fraglimit")}}

---
{{define_cvar("nextmode")}}
Sets the game mode to be played when the next level loads

---
{{define_cvar("nextlevel")}}
If set to a valid map name, will trigger a changelevel to the specified map at the end of the round

---
{{define_cvar("mapcyclefile")}}
Name of the .txt file used to cycle the maps on multiplayer servers 

---
{{define_cvar("game_online")}}
The current game is online.

---
{{define_cvar("game_public")}}
The current game is public.

---
{{define_cvar("mp_teamname_1")}}
A non-empty string overrides the first team's name.

---
{{define_cvar("mp_teamname_2")}}
A non-empty string overrides the second team's name.

---
{{define_cvar("mp_teamflag_1")}}
Enter a country's alpha 2 code to show that flag next to team 1's name in the spectator scoreboard.

---
{{define_cvar("mp_teamflag_2")}}
Enter a country's alpha 2 code to show that flag next to team 2's name in the spectator scoreboard.

---
{{define_cvar("mp_teamlogo_1")}}
Enter a team's shorthand image name to display their logo. Images can be found here: 'resource/flash/econ/tournaments/teams'

---
{{define_cvar("mp_teamlogo_2")}}
Enter a team's shorthand image name to display their logo. Images can be found here: 'resource/flash/econ/tournaments/teams'

---
{{define_cvar("mp_teamprediction_txt")}}
A value between 1 and 99 will set predictions in favor of first team.

---
{{define_cvar("mp_teamprediction_pct")}}
A value between 1 and 99 will show predictions in favor of CT team.

---
{{define_cvar("mp_teammatchstat_txt")}}
A non-empty string sets the match stat description, e.g. 'Match 2 of 3'.

---
{{define_cvar("mp_teammatchstat_1")}}
A non-empty string sets first team's match stat.

---
{{define_cvar("mp_teammatchstat_2")}}
A non-empty string sets second team's match stat.

---
{{define_cvar("mp_teamscore_1")}}
A non-empty string for best-of-N maps won by the first team.

---
{{define_cvar("mp_teamscore_2")}}
A non-empty string for best-of-N maps won by the second team.

---
{{define_cvar("mp_teamscore_max")}}
How many maps to win the series (bo3 max=2; bo5 max=3; bo7 max=4)

---
{{define_cvar("mp_teammatchstat_holdtime")}}
Decide on a match stat and hold it additionally for at least so many seconds

---
{{define_cvar("mp_teammatchstat_cycletime")}}
Cycle match stats after so many seconds

---
{{define_cvar("mp_heavyassaultsuit_speed")}}
The max speed of a player when they are wearing the heavy assault suit

---
{{define_cvar("mp_heavybot_damage_reduction_scale")}}
How much damage should scale when the player wearing the heavy assault suit is shot (1.0 = no change, 0.5 = half damage)

---
{{define_cvar("mp_heavyassaultsuit_deploy_timescale")}}
How fast a player wearing the heavy assault suit will draw their weapon (1.0 = normal speed, 0.5 = half speed)

---
{{define_cvar("mp_heavyassaultsuit_aimpunch")}}
How much EXTRA aim punch will happen when a player wearing the assault suit gets when shot

---
{{define_cvar("mp_shield_speed_deployed")}}
The max speed of a player when they have a shield deployed

---
{{define_cvar("mp_shield_speed_holstered")}}
The max speed of a player when they have a shield holstered

---
{{define_cvar("mp_backup_round_auto")}}
If enabled will keep in-memory backups to handle reconnecting players even if the backup files aren't written to disk

---
{{define_cvar("mp_backup_round_file")}}
If set then server will save all played rounds information to files filename_date_time_team1_team2_mapname_roundnum_score1_score2.txt

---
{{define_cvar("mp_backup_round_file_pattern")}}
If set then server will save all played rounds information to files named by this pattern, e.g.'%prefix%_%date%_%time%_%team1%_%team2%_%map%_round%round%_score_%score1%_%score2%.txt'

---
{{define_cvar("mp_backup_round_file_last")}}
Every time a backup file is written the value of this convar gets updated to hold the name of the backup file.

---
{{define_cvar("mp_backup_restore_load_autopause")}}
Whether to automatically pause the match after restoring round data from backup

---
{{define_cvar("sv_gameinstructor_disable")}}
Force all clients to disable their game instructors.

---
{{define_cvar("cs_AssistDamageThreshold")}}
cs_AssistDamageThreshold defines the amount of damage needed to score an assist

---
{{define_cvar("sv_matchpause_auto_5v5")}}
When enabled will automatically pause the match at next freeze time if less than 5 players are connected on each team.

---
{{define_cvar("mp_spectators_max")}}
How many spectators are allowed in a match.

---
{{define_cvar("mp_buytime")}}
How many seconds after round start players can buy items for.

---
{{define_cvar("mp_buy_allow_grenades")}}
Whether players can purchase grenades from the buy menu or not.

---
{{define_cvar("mp_buy_allow_guns")}}
Whether players can purchase guns: pistols (1), SMGs (2), rifles (4), shotguns (8), sniper rifles (16), heavy MGs (32).

---
{{define_cvar("mp_warmup_online_enabled")}}
Whether or not to do a warmup period at the start of an online match.

---
{{define_cvar("mp_warmup_offline_enabled")}}
Whether or not to do a warmup period at the start of a match in an offline (bot) match.

---
{{define_cvar("mp_startmoney")}}
amount of money each player gets when they reset

---
{{define_cvar("mp_maxmoney")}}
maximum amount of money allowed in a player's account

---
{{define_cvar("mp_afterroundmoney")}}
amount of money awared to every player after each round

---
{{define_cvar("mp_playercashawards")}}
Players can earn money by performing in-game actions

---
{{define_cvar("mp_teamcashawards")}}
Teams can earn money by performing in-game actions

---
{{define_cvar("mp_overtime_enable")}}
If a match ends in a tie, use overtime rules to determine winner

---
{{define_cvar("mp_overtime_limit")}}
When overtime is enabled, only so many overtimes can be played

---
{{define_cvar("mp_overtime_maxrounds")}}
When overtime is enabled play additional rounds to determine winner

---
{{define_cvar("mp_overtime_startmoney")}}
Money assigned to all players at start of every overtime half

---
{{define_cvar("mp_hostages_takedamage")}}
Whether or not hostages can be hurt.

---
{{define_cvar("mp_hostages_rescuetowin")}}
0 == all alive, any other number is the number the CT's need to rescue to win the round.

---
{{define_cvar("mp_hostages_rescuetime")}}
Additional time added to round time if a hostage is reached by a CT.

---
{{define_cvar("mp_anyone_can_pickup_c4")}}
If set, everyone can pick up the c4, not just Ts.

---
{{define_cvar("mp_c4_cannot_be_defused")}}
If set, the planted c4 cannot be defused.

---
{{define_cvar("sv_coaching_enabled")}}
Allows spectating and communicating with a team ( 'coach t' or 'coach ct' )

---
{{define_cvar("sv_party_mode")}}
Party!!

---
{{define_cvar("sv_dz_hostage_rescue_reward")}}
Number of cash bundles to award for rescuing a hostage

---
{{define_cvar("sv_dz_squad_wipe_reward")}}
Number of cash bundles to award for eliminating a squad

---
{{define_cvar("mp_shorthanded_cash_bonus_round_delay")}}
number of previous rounds that a team needs to have been shorthanded before they are eligible for the short-handed bonus

---
{{define_cvar("mp_shorthanded_cash_bonus_ignore_kicked")}}
Determines whether kicked players are included in the assessment for short-handedness

---
{{define_cvar("mp_disconnect_kills_players")}}
When a player disconnects, kill them first (triggering item drops, stats, etc.)

---
{{define_cvar("mp_disconnect_kills_bots")}}
When a bot disconnects, kill them first.  Requires mp_disconnect_kills_players.

---
{{define_cvar("mp_verbose_changelevel_spew")}}

---
{{define_cvar("mp_warmuptime")}}
How long the warmup period lasts. Changing this value resets warmup.

---
{{define_cvar("mp_warmuptime_all_players_connected")}}
Warmup time to use when all players have connected. 0 to disable.

---
{{define_cvar("mp_warmuptime_match_cancelled")}}
Warmup time to use when the match will be cancelled (eg. due to a live VAC ban).

---
{{define_cvar("mp_endwarmup_player_count")}}
Number of players required to be connected to end warmup early. 0 to require maximum players for mode.

---
{{define_cvar("mp_warmup_pausetimer")}}
Set to 1 to stay in warmup indefinitely. Set to 0 to resume the timer.

---
{{define_cvar("mp_halftime_pausetimer")}}
Set to 1 to stay in halftime indefinitely. Set to 0 to resume the timer.

---
{{define_cvar("mp_halftime_pausematch")}}
Set to 1 to pause match after halftime countdown elapses. Match must be resumed by vote or admin.

---
{{define_cvar("mp_overtime_halftime_pausetimer")}}
If set to 1 will set mp_halftime_pausetimer to 1 before every half of overtime. Set mp_halftime_pausetimer to 0 to resume the timer.

---
{{define_cvar("mp_respawn_immunitytime")}}
How many seconds after respawn immunity lasts. Set to negative value to disable warmup immunity.

---
{{define_cvar("mp_playerid")}}
Controls what information player see in the status bar: 0 all names; 1 team names; 2 no names

---
{{define_cvar("mp_playerid_delay")}}
Number of seconds to delay showing information in the status bar

---
{{define_cvar("mp_playerid_hold")}}
Number of seconds to keep showing old information in the status bar

---
{{define_cvar("mp_round_restart_delay")}}
Number of seconds to delay before restarting a round after a win

---
{{define_cvar("mp_halftime_duration")}}
Target number of seconds that halftime lasts; shortened if team intros are active

---
{{define_cvar("mp_min_halftime_duration")}}
Minimum number of seconds that halftime lasts even if team intros are active

---
{{define_cvar("mp_match_can_clinch")}}
Can a team clinch and end the match by being so far ahead that the other team has no way to catching up?

---
{{define_cvar("mp_ct_default_melee")}}
The default melee weapon that the CTs will spawn with.	 Even if this is blank, a knife will be given.	To give a taser, it should look like this: 'weapon_knife weapon_taser'.	 Remember to set mp_weapons_allow_zeus to 1 if you want to give a taser!

---
{{define_cvar("mp_ct_default_secondary")}}
The default secondary (pistol) weapon that the CTs will spawn with

---
{{define_cvar("mp_ct_default_primary")}}
The default primary (rifle) weapon that the CTs will spawn with

---
{{define_cvar("mp_ct_default_grenades")}}
The default grenades that the CTs will spawn with.	 To give multiple grenades, separate each weapon class with a space like this: 'weapon_molotov weapon_hegrenade'

---
{{define_cvar("mp_t_default_melee")}}
The default melee weapon that the Ts will spawn with

---
{{define_cvar("mp_t_default_secondary")}}
The default secondary (pistol) weapon that the Ts will spawn with

---
{{define_cvar("mp_t_default_primary")}}
The default primary (rifle) weapon that the Ts will spawn with

---
{{define_cvar("mp_t_default_grenades")}}
The default grenades that the Ts will spawn with.	To give multiple grenades, separate each weapon class with a space like this: 'weapon_molotov weapon_hegrenade'

---
{{define_cvar("mp_join_grace_time")}}
Number of seconds after round start to allow a player to join a game

---
{{define_cvar("mp_win_panel_display_time")}}
The amount of time to show the win panel between matches / halfs

---
{{define_cvar("mp_dm_dogtag_score")}}
Points to award for picking up a dogtag in deathmatch.

---
{{define_cvar("mp_dm_teammode")}}
In deathmatch, enables team DM visuals & scoring (0: personal, 1: team mode, 2: use team contribution score)

---
{{define_cvar("mp_dm_teammode_kill_score")}}
Team deathmatch victory points to award for enemy kill

---
{{define_cvar("mp_dm_teammode_bonus_score")}}
Team deathmatch victory points to award for kill with bonus weapon

---
{{define_cvar("mp_dm_teammode_dogtag_score")}}
Team deathmatch victory points to award for collecting enemy dogtags

---
{{define_cvar("mp_dm_bonusweapon_dogtags")}}
Additional dogtags to drop when making a kill with the bonus weapon

---
{{define_cvar("mp_display_kill_assists")}}
Whether to display and score player assists

---
{{define_cvar("mp_match_end_restart")}}
At the end of the match, perform a restart instead of loading a new map

---
{{define_cvar("ammo_45acp_max")}}

---
{{define_cvar("ammo_357sig_max")}}

---
{{define_cvar("ammo_357sig_p250_max")}}

---
{{define_cvar("ammo_357sig_small_max")}}

---
{{define_cvar("ammo_357sig_min_max")}}

---
{{define_cvar("ammo_57mm_max")}}

---
{{define_cvar("ammo_grenade_limit_default")}}

---
{{define_cvar("ammo_grenade_limit_flashbang")}}

---
{{define_cvar("ammo_grenade_limit_total")}}

---
{{define_cvar("ammo_grenade_limit_snowballs")}}

---
{{define_cvar("ammo_grenade_limit_tripwirefire")}}

---
{{define_cvar("ammo_item_limit_adrenaline")}}

---
{{define_cvar("ammo_grenade_limit_breachcharge")}}

---
{{define_cvar("ammo_grenade_limit_bumpmine")}}

---
{{define_cvar("ammo_item_limit_healthshot")}}

---
{{define_cvar("ammo_50AE_impulse")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_762mm_impulse")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_556mm_impulse")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_556mm_box_impulse")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_338mag_impulse")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_9mm_impulse")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_buckshot_impulse")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_45acp_impulse")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_357sig_impulse")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_57mm_impulse")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_50AE_headshot_mult")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_762mm_headshot_mult")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_556mm_headshot_mult")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_556mm_box_headshot_mult")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_338mag_headshot_mult")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_9mm_headshot_mult")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_buckshot_headshot_mult")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_45acp_headshot_mult")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_357sig_headshot_mult")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("ammo_57mm_headshot_mult")}}
You must enable tweaking via tweak_ammo_impulses to use this value.

---
{{define_cvar("frag_grenade_blip_frequency")}}

---
{{define_cvar("mp_dm_time_between_bonus_min")}}
Minimum time a bonus time will start after the round start or after the last bonus (in seconds)

---
{{define_cvar("mp_dm_time_between_bonus_max")}}
Maximum time a bonus time will start after the round start or after the last bonus (in seconds)

---
{{define_cvar("mp_dm_bonus_length_min")}}
Minimum time the bonus time will last (in seconds)

---
{{define_cvar("mp_dm_bonus_length_max")}}
Maximum time the bonus time will last (in seconds)

---
{{define_cvar("mp_dm_healthshot_killcount")}}
Grant healthshots in deathmatch after n kills

---
{{define_cvar("mp_dm_kill_base_score")}}
Number of base points to award for a kill in deathmatch.  Cheaper weapons award 1 or 2 additional points.

---
{{define_cvar("mp_dm_bonus_percent")}}
Percent of points additionally awarded when someone gets a kill with the bonus weapon during the bonus period.

---
{{define_cvar("spec_replay_round_delay")}}
Round can be delayed by this much due to someone watching a replay; must be at least 3-4 seconds, otherwise the last replay will always be interrupted by round start, assuming normal pause between round_end and round_start events (7 seconds) and freezecam delay (2 seconds) and 7.4 second full replay (5.4 second pre-death and ~2 seconds post-death) and replay in/out switching (up to a second)

---
{{define_cvar("mp_footsteps_serverside")}}
Makes the server always play footstep sounds. Clients never calculate footstep sounds locally, instead relying on the server.

---
{{define_cvar("sv_reliableavatardata")}}
Use server overrides for steam avatars

---
{{define_cvar("sv_warmup_to_freezetime_delay")}}
Delay between end of warmup and start of match.

---
{{define_cvar("sv_disable_teamselect_menu")}}
Disable teamselect menu on clients

---
{{define_cvar("sv_human_autojoin_team")}}
Force human players on to a team. 0 to disable.

---
{{define_cvar("sv_server_graphic1")}}
A 360x60 (<16kb) image file in /csgo/ that will be displayed to spectators.

---
{{define_cvar("sv_server_graphic2")}}
A 220x45 (<16kb) image file in /csgo/ that will be displayed to spectators.

---
{{define_cvar("sv_disable_observer_interpolation")}}
Disallow interpolating between observer targets on this server.

---
{{define_cvar("sv_invites_only_mainmenu")}}
If turned on, will ignore all invites when user is playing a match

---
{{define_cvar("sv_teamid_overhead_always_prohibit")}}
Determines whether cl_teamid_overhead_always is prohibited.

---
{{define_cvar("sv_versus_screen_scene_id")}}
Determines which scene is used for the versus screen.

---
{{define_cvar("sv_disconnected_players_cleanup_delay")}}
Delay between player disconnecting and their corpse getting cleaned up.

---
{{define_cvar("sv_log_roundstats")}}

---
{{define_cvar("sv_autoexec_mapname_cfg")}}
Execute a mapname cfg file on the server automatically in custom game modes that require it.

---
{{define_cvar("sv_show_team_equipment_prohibit")}}
Determines whether +cl_show_team_equipment is prohibited.

---
{{define_cvar("sv_show_team_equipment_force_on")}}
Force on if not prohibited

---
{{define_cvar("sv_teamid_overhead_maxdist_spec")}}
If >0, server will override cl_teamid_overhead_maxdist_spec

---
{{define_cvar("sv_teamid_overhead_maxdist")}}
If >0, server will override cl_teamid_overhead_maxdist

---
{{define_cvar("sv_teamid_overhead")}}
Shows teamID over player's heads.  0 = off, 1 = on

---
{{define_cvar("sv_disable_radar")}}
0: regular radar; 1: always disabled; 2: disabled in warmup

---
{{define_cvar("sv_hide_roundtime_until_seconds")}}

---
{{define_cvar("sv_outofammo_indicator")}}

---
{{define_cvar("sv_falldamage_to_below_player_ratio")}}
Landing on a another player's head gives them this ratio of the damage.

---
{{define_cvar("sv_falldamage_to_below_player_multiplier")}}
Scale damage when distributed across two players

---
{{define_cvar("sv_chat_proximity")}}

---
{{define_cvar("sv_voice_proximity")}}

---
{{define_cvar("sv_highlight_duration")}}

---
{{define_cvar("sv_highlight_distance")}}

---
{{define_cvar("sv_fade_player_visibility_farz")}}

---
{{define_cvar("mp_consecutive_loss_max")}}

---
{{define_cvar("mp_starting_losses")}}
Determines what the initial loss streak is.

---
{{define_cvar("mp_consecutive_loss_aversion")}}
How loss streak is affected with round win: 0 = win fully resets loss bonus, 1 = first win steps down loss bonus, 2 = first win holds loss bonus and step down starting with second win

---
{{define_cvar("sv_kick_players_with_cooldown")}}
(0: do not kick on insecure servers; 1: kick players with Untrusted status or convicted by Overwatch; 2: kick players with any cooldown)

---
{{define_cvar("sv_matchend_drops_enabled")}}
Rewards gameplay time is always accumulated for players, but drops at the end of the match can be prevented

---
{{define_cvar("sv_buy_status_override")}}
Override for buy status map info. 0 = everyone can buy, 1 = ct only, 2 = t only 3 = nobody

---
{{define_cvar("sv_auto_adjust_bot_difficulty")}}
Adjust the difficulty of bots each round based on contribution score.

---
{{define_cvar("sv_bots_get_easier_each_win")}}
If > 0, some # of bots will lower thier difficulty each time they win. The argument defines how many will lower their difficulty each time.

---
{{define_cvar("tv_delaymapchange")}}
Delays map change until broadcast is complete

---
{{define_cvar("sv_game_mode_flags")}}
Dedicated server game mode flags to run

---
{{define_cvar("nextmap_print_enabled")}}
When enabled prints next map to clients

---
{{define_cvar("sv_skirmish_id")}}
Dedicated server skirmish id to run

---
{{define_cvar("ff_damage_decoy_explosion")}}
Enables or disables team damage from decoy detonation

---
{{define_cvar("mp_autoteambalance")}}

---
{{define_cvar("mp_maxrounds")}}
max number of rounds to play before server changes maps

---
{{define_cvar("mp_winlimit")}}
Max score one team can reach before server changes maps

---
{{define_cvar("mp_tournament")}}

---
{{define_cvar("mp_team_timeout_time")}}
Duration of each timeout.

---
{{define_cvar("mp_team_timeout_max")}}
Number of timeouts each team gets per match.

---
{{define_cvar("mp_team_timeout_ot_add_once")}}
Number of timeouts to add for each team when regulation time ends and match goes to overtime.

---
{{define_cvar("mp_team_timeout_ot_add_each")}}
Number of timeouts to add for each team when match goes to 2nd and each next overtime.

---
{{define_cvar("mp_team_timeout_ot_max")}}
Max number of timeouts each team can have per OT after all OT timeouts got added.

---
{{define_cvar("mp_technical_timeout_per_team")}}
How many technical timeouts are there per team?

---
{{define_cvar("mp_technical_timeout_duration_s")}}
How many seconds is a full technical timeout?

---
{{define_cvar("mp_weapons_max_gun_purchases_per_weapon_per_match")}}
Max number of times a player may purchase any weapon per match

---
{{define_cvar("mp_match_restart_delay")}}
Time (in seconds) until a match restarts.

---
{{define_cvar("mp_chattime")}}
amount of time players can chat after the game is over

---
{{define_cvar("inferno_velocity_normal_factor")}}

---
{{define_cvar("inferno_surface_offset")}}

---
{{define_cvar("inferno_child_spawn_max_depth")}}

---
{{define_cvar("inferno_max_trace_per_tick")}}

---
{{define_cvar("inferno_forward_reduction_factor")}}

---
{{define_cvar("inferno_smoke_volume_density")}}

---
{{define_cvar("inferno_damage_timer")}}
How long between times for the inferno to deal damage.

---
{{define_cvar("inferno_ct_experiment")}}
enable ct incendiary experiment

---
{{define_cvar("hostage_drop_time")}}
Time for the hostage before it fully drops to ground

---
{{define_cvar("sv_pushaway_hostage_force")}}
How hard the hostage is pushed away from physics objects (falls off with inverse square of distance).

---
{{define_cvar("sv_pushaway_max_hostage_force")}}
Maximum of how hard the hostage is pushed away from physics objects.

---
{{define_cvar("mp_hostages_max")}}
Maximum number of hostages to spawn.

---
{{define_cvar("mp_hostages_spawn_farthest")}}
When enabled will consistently force the farthest hostages to spawn.

---
{{define_cvar("mp_hostages_spawn_same_every_round")}}
0 = spawn hostages randomly every round, 1 = same spawns for entire match.

---
{{define_cvar("mp_hostages_spawn_force_positions")}}
Comma separated list of zero based indices to force spawn positions, e.g. '0,2' or '1,6'

---
{{define_cvar("mp_hostages_spawn_force_positions_xyz")}}
Comma separated list of xyz locations to force spawn positions, e.g. 'x1 y1 z1,x2 y2 z2'

---
{{define_cvar("mp_hostages_run_speed_modifier")}}
Default is 1.0, slow down hostages by setting this to < 1.0.

---
{{define_cvar("nav_approach_points_area_size_threshold")}}
Ignore nav areas with at least one side smaller than this amount during approach point calculation.

---
{{define_cvar("nav_draw_hidingspots")}}

---
{{define_cvar("nav_draw_dangerareas")}}

---
{{define_cvar("mp_guardian_target_site")}}
If set to the index of a bombsite, will cause random spawns to be only created near that site.

---
{{define_cvar("sv_hegrenade_damage_multiplier")}}

---
{{define_cvar("sv_hegrenade_radius_multiplier")}}

---
{{define_cvar("dota_overhead_on_received_item")}}
Emit an overhead particle effect on receiving an item from an ally.

---
{{define_cvar("ai_debug_shoot_positions")}}

---
{{define_cvar("ai_disabled")}}

---
{{define_cvar("filter_player_simulation_time")}}

---
{{define_cvar("sv_script_think_interval")}}

---
{{define_cvar("vprof_scope_entity_thinks")}}

---
{{define_cvar("vprof_think_limit")}}

---
{{define_cvar("ent_pivot_size")}}

---
{{define_cvar("debug_overlay_fullposition")}}

---
{{define_cvar("ent_text_no_name_really_i_mean_it")}}

---
{{define_cvar("ent_show_contexts")}}
Show entity contexts in ent_text display

---
{{define_cvar("ent_actornames_font")}}
ent_actornames font name

---
{{define_cvar("ent_actornames_fontsize")}}
ent_actornames font size

---
{{define_cvar("ent_text_flags_active")}}

---
{{define_cvar("phys_async_buoyancy_update")}}
If true, buoyancy motion controllers are updated in an async job after the tick has completed.

---
{{define_cvar("sv_pushaway_clientside_size")}}
Minimum size of pushback objects

---
{{define_cvar("props_break_max_pieces_perframe")}}
Maximum prop breakable piece count per frame (-1 = model default)

---
{{define_cvar("break_damage_inherit_scale")}}

---
{{define_cvar("break_invulnerable_spawn_duration")}}

---
{{define_cvar("props_break_apply_radial_forces")}}

---
{{define_cvar("props_break_radial_force_ratio")}}

---
{{define_cvar("props_breakable_debug_spawn")}}

---
{{define_cvar("snd_event_oriented_box_debug")}}

---
{{define_cvar("animgraph_enable_parallel_update")}}

---
{{define_cvar("animgraph_enable_parallel_op_evaluation")}}

---
{{define_cvar("animgraph_force_tick_all_graphs")}}

---
{{define_cvar("sv_skip_update_animations")}}
Enable to skip game animations

---
{{define_cvar("animgraph_slope_draw_raycasts")}}

---
{{define_cvar("animgraph_trace_static_only")}}

---
{{define_cvar("animgraph_draw_traces")}}

---
{{define_cvar("animgraph_trace_ignore_prop_physics")}}

---
{{define_cvar("cl_skip_hierarchy_update_for_unchanged_entities")}}
Skip updating hierarchy information in PostDataUpdate for entities that have not changed

---
{{define_cvar("sv_massreport")}}

---
{{define_cvar("ent_skeleton_duration")}}
Duration of ent_skeleton display

---
{{define_cvar("skill")}}
Game skill level.

---
{{define_cvar("sv_lightquery_debug")}}

---
{{define_cvar("lightquery_debug_direct_lighting")}}

---
{{define_cvar("lightquery_debug_indirect_lighting")}}

---
{{define_cvar("phys_active")}}
Whether PLAYER physics is actively simulated (ie. noclip)

---
{{define_cvar("sv_phys_enabled")}}
Enable all physics simulation

---
{{define_cvar("sv_phys_stop_at_collision")}}

---
{{define_cvar("sv_phys_sleep_enable")}}
Enable sleeping for dynamic physics bodies.

---
{{define_cvar("sv_phys_animated_hierarchy")}}

---
{{define_cvar("phys_show_stats")}}

---
{{define_cvar("phys_threaded_transform_update")}}

---
{{define_cvar("phys_threaded_kinematic_bone_update")}}

---
{{define_cvar("sv_gravity")}}
World gravity.

---
{{define_cvar("phys_timescale")}}
Scale time for physics

---
{{define_cvar("phys_continuous_kinematic_update")}}

---
{{define_cvar("phys_parallel_islands")}}
Enable/Disable Parallel Island Solving

---
{{define_cvar("sv_phys_visualize_awake")}}

---
{{define_cvar("phys_visualize_awake_dynamic_only")}}

---
{{define_cvar("phys_visualize_awake_unattached_only")}}

---
{{define_cvar("sv_phys_debug_callback_entities")}}
Print all entities that get touch callbacks. Each entity is printed only once.

---
{{define_cvar("phys_log_updaters_include")}}

---
{{define_cvar("phys_log_updaters_exclude")}}

---
{{define_cvar("phys_log_updaters")}}

---
{{define_cvar("sv_hitbox_debug")}}

---
{{define_cvar("sos_debug_emit")}}

---
{{define_cvar("snd_break_on_start_soundevent")}}
Use to debug break on any soundevent that is started matching this name

---
{{define_cvar("soundscape_debug")}}
When on, draws lines to all env_soundscape entities. Green lines show the active soundscape, red lines show soundscapes that aren't in range, and white lines show soundscapes that are in range, but not the active soundscape.

---
{{define_cvar("soundscape_update_include_bots")}}
Enable to calculate soundscape audio params for bots.

---
{{define_cvar("disable_source_soundscape_trace")}}
Bypasses lookup of soundscapes for indvidual audio sources when enabled.

---
{{define_cvar("script_break_in_native_debugger_on_error")}}

---
{{define_cvar("script_attach_debugger_at_startup")}}

---
{{define_cvar("ai_debug_dyninteractions")}}
Debug the NPC dynamic interaction system.

---
{{define_cvar("fog_volume_debug")}}
If enabled, prints diagnostic information about the current fog volume

---
{{define_cvar("ammo_50AE_max")}}

---
{{define_cvar("ammo_762mm_max")}}

---
{{define_cvar("ammo_556mm_max")}}

---
{{define_cvar("ammo_556mm_small_max")}}

---
{{define_cvar("ammo_556mm_box_max")}}

---
{{define_cvar("ammo_338mag_max")}}

---
{{define_cvar("ammo_9mm_max")}}

---
{{define_cvar("ammo_buckshot_max")}}

---
{{define_cvar("weapon_accuracy_logging")}}

---
{{define_cvar("weapon_near_empty_sound")}}

---
{{define_cvar("weapon_debug_max_inaccuracy")}}
Force all shots to have maximum inaccuracy

---
{{define_cvar("weapon_debug_inaccuracy_only_up")}}
Force weapon inaccuracy to be in exactly the up direction

---
{{define_cvar("snd_max_pitch_shift_inaccuracy")}}

---
{{define_cvar("weapon_accuracy_shotgun_spread_patterns")}}

---
{{define_cvar("use_fx_queue")}}
use_fx_queue

---
{{define_cvar("suspicious_hit_strategy")}}
What to do about suspicious hits. 0: Nothing. 1: Skip the bullet. 2: Skip the bullet and re-roll a new bullet.

---
{{define_cvar("suspicious_hit_player_radius")}}

---
{{define_cvar("suspicious_hit_odds_threshold")}}

---
{{define_cvar("debug_aim_angle")}}

---
{{define_cvar("nav_max_view_distance")}}
Maximum range for precomputed nav mesh visibility (0 = default 1500 units)

---
{{define_cvar("nav_potentially_visible_dot_tolerance")}}

---
{{define_cvar("logaddress_token_secret")}}
Set a secret string that will be hashed when using logaddress with explicit token hash.

---
{{define_cvar("sv_log_http_record_before_any_listeners")}}

---
{{define_cvar("bot_force_duck")}}

---
{{define_cvar("mp_coopmission_bot_difficulty_offset")}}
The difficulty offset modifier for bots during coop missions.

---
{{define_cvar("bot_traceview")}}
For internal testing purposes.

---
{{define_cvar("bot_stop")}}
bot_stop <1|all> | <not_bomber> | <t> | <ct>

---
{{define_cvar("bot_ignore_enemies")}}
If nonzero, bots will ignore enemies (for debugging).

---
{{define_cvar("bot_show_nav")}}
For internal testing purposes.

---
{{define_cvar("bot_walk")}}
If nonzero, bots can only walk, not run.

---
{{define_cvar("bot_difficulty")}}
Defines the skill of bots joining the game.  Values are: 0=easy, 1=normal, 2=hard, 3=expert.

---
{{define_cvar("bot_debug")}}
For internal testing purposes.

---
{{define_cvar("bot_debug_target")}}
For internal testing purposes.

---
{{define_cvar("bot_quota")}}
Determines the total number of bots in the game.

---
{{define_cvar("bot_quota_mode")}}
Determines the type of quota.
Allowed values: 'normal', 'fill', and 'match'.
If 'fill', the server will adjust bots to keep N players in the game, where N is bot_quota.
If 'match', the server will maintain a 1:N ratio of humans to bots, where N is bot_quota.

---
{{define_cvar("bot_prefix")}}
This string is prefixed to the name of all bots that join the game.
<difficulty> will be replaced with the bot's difficulty.
<weaponclass> will be replaced with the bot's desired weapon class.
<skill> will be replaced with a 0-100 representation of the bot's skill.

---
{{define_cvar("bot_allow_rogues")}}
If nonzero, bots may occasionally go 'rogue'. Rogue bots do not obey radio commands, nor pursue scenario goals.

---
{{define_cvar("bot_allow_pistols")}}
If nonzero, bots may use pistols.

---
{{define_cvar("bot_allow_shotguns")}}
If nonzero, bots may use shotguns.

---
{{define_cvar("bot_allow_sub_machine_guns")}}
If nonzero, bots may use sub-machine guns.

---
{{define_cvar("bot_allow_rifles")}}
If nonzero, bots may use rifles.

---
{{define_cvar("bot_allow_machine_guns")}}
If nonzero, bots may use the machine gun.

---
{{define_cvar("bot_allow_grenades")}}
If nonzero, bots may use grenades.

---
{{define_cvar("bot_allow_snipers")}}
If nonzero, bots may use sniper rifles.

---
{{define_cvar("bot_join_team")}}
Determines the team bots will join into. Allowed values: 'any', 'T', or 'CT'.

---
{{define_cvar("bot_join_after_player")}}
If nonzero, bots wait until a player joins before entering the game.

---
{{define_cvar("bot_auto_vacate")}}
If nonzero, bots will automatically leave to make room for human players.

---
{{define_cvar("bot_zombie")}}
If nonzero, bots will stay in idle mode and not attack.

---
{{define_cvar("bot_defer_to_human_goals")}}
If nonzero and there is a human on the team, the bots will not do the scenario tasks.

---
{{define_cvar("bot_defer_to_human_items")}}
If nonzero and there is a human on the team, the bots will not get scenario items.

---
{{define_cvar("bot_chatter")}}
Control how bots talk. Allowed values: 'off', 'radio', 'minimal', or 'normal'.

---
{{define_cvar("bot_dont_shoot")}}
If nonzero, bots will not fire weapons (for debugging).

---
{{define_cvar("bot_eco_limit")}}
If nonzero, bots will not buy if their money falls below this amount.

---
{{define_cvar("bot_auto_follow")}}
If nonzero, bots with high co-op may automatically follow a nearby human player.

---
{{define_cvar("bot_flipout")}}
If nonzero, bots use no CPU for AI. Instead, they run around randomly.

---
{{define_cvar("bot_controllable")}}
Determines whether bots can be controlled by players

---
{{define_cvar("mp_bot_ai_bt")}}
Use the specified behavior tree file to drive the bot behavior.

---
{{define_cvar("bot_show_occupy_time")}}
Show when each nav area can first be reached by each team.

---
{{define_cvar("bot_show_battlefront")}}
Show areas where rushing players will initially meet.

---
{{define_cvar("bot_join_delay")}}
Prevents bots from joining the server for this many seconds after a map change.

---
{{define_cvar("bot_join_in_warmup")}}
Prevents bots from joining the server while warmup phase is active.

---
{{define_cvar("throttle_expensive_ai")}}

---
{{define_cvar("csgo_nav_jump_link_detour_threshold")}}
don't traverse a jump link if there's a detour that costs less than this amount

---
{{define_cvar("mp_guardian_force_collect_hostages_timeout")}}
Force bots to collect hostages after this amount of time if no enemy has been seen.

---
{{define_cvar("bot_max_vision_distance_override")}}
Max distance bots can see targets.

---
{{define_cvar("bot_ignore_players")}}
Bots will not see non-bot players.

---
{{define_cvar("bot_coop_idle_max_vision_distance")}}
Max distance bots can see targets (in coop) when they are idle, dormant, hiding or asleep.

---
{{define_cvar("cv_bot_ai_bt_debug_target")}}
Draw the behavior tree of the given bot.

---
{{define_cvar("cv_bot_ai_bt_moveto_show_next_hiding_spot")}}
Draw the hiding spot the bot will check next.

---
{{define_cvar("cv_bot_ai_bt_hiding_spot_show")}}
Draw hiding spots.

---
{{define_cvar("sv_bot_parallel_threat_detection")}}
Perform bot threat detection in parallel

---
{{define_cvar("bot_max_visible_smoke_length")}}
Bots will see players through smoke clouds up to this length.

---
{{define_cvar("csgo_fatdemo_enable")}}

---
{{define_cvar("csgo_fatdemo_output")}}

---
{{define_cvar("bot_loadout")}}
bots are given these items at round start

---
{{define_cvar("bot_randombuy")}}
should bots ignore their prefered weapons and just buy weapons at random?

---
{{define_cvar("sv_bot_buy_grenade_chance")}}
Chance bots will buy a grenade with leftover money (after prim, sec and armor). Input as percent (0-100.0)

---
{{define_cvar("sv_bot_buy_smoke_weight")}}
Given a bot will buy a grenade, controls the odds of the grenade type. Proportional to all other sv_bot_buy_*_weight convars.

---
{{define_cvar("sv_bot_buy_flash_weight")}}
Given a bot will buy a grenade, controls the odds of the grenade type. Proportional to all other sv_bot_buy_*_weight convars.

---
{{define_cvar("sv_bot_buy_decoy_weight")}}
Given a bot will buy a grenade, controls the odds of the grenade type. Proportional to all other sv_bot_buy_*_weight convars.

---
{{define_cvar("sv_bot_buy_molotov_weight")}}
Given a bot will buy a grenade, controls the odds of the grenade type. Proportional to all other sv_bot_buy_*_weight convars.

---
{{define_cvar("sv_bot_buy_hegrenade_weight")}}
Given a bot will buy a grenade, controls the odds of the grenade type. Proportional to all other sv_bot_buy_*_weight convars.

---
{{define_cvar("devonly_chicken_feeler_distance")}}
Chicken feeler distance

---
{{define_cvar("devonly_chicken_feeler_height")}}
Chicken feeler height

---
{{define_cvar("devonly_chicken_feeler_pitch")}}
Chicken feeler pitch

---
{{define_cvar("devonly_chicken_blocktimer")}}
Chicken blockertimer

---
{{define_cvar("devonly_chicken_activity_debug")}}
Print chicken activity info to the console

---
{{define_cvar("debug_chicken")}}
Chicken debug info

---
{{define_cvar("glow_chickens")}}
Glow chickens with a green outline.

---
{{define_cvar("chicken_stop")}}

---
{{define_cvar("sv_minimum_desired_chicken_count")}}
Minimum number of chickens to attempt to spawn in the map

---
{{define_cvar("inferno_per_flame_spawn_duration")}}
Duration each new flame will attempt to spawn new flames

---
{{define_cvar("inferno_initial_spawn_interval")}}
Time between spawning flames for first fire

---
{{define_cvar("inferno_child_spawn_interval_multiplier")}}
Amount spawn interval increases for each child

---
{{define_cvar("inferno_max_child_spawn_interval")}}
Largest time interval for child flame spawning

---
{{define_cvar("inferno_spawn_angle")}}
Angular change from parent

---
{{define_cvar("inferno_max_flames")}}
Maximum number of flames that can be created

---
{{define_cvar("inferno_flame_spacing")}}
Minimum distance between separate flame spawns

---
{{define_cvar("inferno_flame_lifetime_incendiary")}}
Average lifetime of each flame in seconds (incgrenade)

---
{{define_cvar("inferno_flame_lifetime")}}
Average lifetime of each flame in seconds

---
{{define_cvar("inferno_friendly_fire_duration")}}
For this long, FF is credited back to the thrower.

---
{{define_cvar("inferno_debug")}}

---
{{define_cvar("inferno_damage")}}
Damage per second

---
{{define_cvar("inferno_damage_ct")}}
Damage per second from CT inferno

---
{{define_cvar("inferno_max_range")}}
Maximum distance flames can spread from their initial ignition point

---
{{define_cvar("inferno_max_range_ct")}}
Maximum distance flames can spread from their initial ignition point for an incendiary

---
{{define_cvar("inferno_velocity_factor")}}

---
{{define_cvar("inferno_velocity_decay_factor")}}

---
{{define_cvar("r_light_flickering_enabled")}}

---
{{define_cvar("r_mixed_shadows_fade_out_time")}}

---
{{define_cvar("r_mixed_shadows_fade_in_time")}}

---
{{define_cvar("sv_log_change_offsets")}}
Log change offsets to game/varchangeinfoN.log files.

---
{{define_cvar("sv_use_pvs_cache")}}

---
{{define_cvar("sv_pvs_cache_query_inflate_amount")}}

---
{{define_cvar("sv_watchtransmit")}}
Watch NetworkStateChanged info for this entity index.

---
{{define_cvar("sv_max_change_offsets")}}
How many network changes to track before requiring full diff check.

---
{{define_cvar("sv_pvs_entity")}}
If set, only allows this ent index to network (other than players and things that force sending).

---
{{define_cvar("sv_pvs_random")}}
If set, objects blink in/out of pvs randomly.

---
{{define_cvar("pvs_flowtype")}}
Flow through spawn groups for vis (0 == default, 1 == always visible, 2 == never visible.

---
{{define_cvar("pvs_debugentity")}}
Verbose spew for this entity when doing IsInPVS computation.

---
{{define_cvar("sv_workshop_allow_other_maps")}}
When hosting a workshop collection, users can play other workshop map on this server when it is empty and then mapcycle into this server collection.

---
{{define_cvar("tv_allow_camera_man_steamid")}}
Allows tournament production cameraman to run csgo.exe -interactivecaster on SteamID 7650123456XXX and be the camera man.

---
{{define_cvar("tv_allow_camera_man_steamid2")}}
Allows tournament production tv cameraman to run csgo.exe -interactivecaster on SteamID 7650123456XXX and be the tv camera man.

---
{{define_cvar("game_type")}}
The current game type. See GameModes.txt.

---
{{define_cvar("game_mode")}}
The current game mode (based on game type). See GameModes.txt.

---
{{define_cvar("sv_prime_accounts_only")}}
When this setting is enabled only prime users can connect to this game server.

---
{{define_cvar("sv_maxuptimelimit")}}
Number of hours to operate before trying sv_shutdown.

---
{{define_cvar("sv_auto_cstrafe_min_attempts")}}
The minimum number of counter-strafe attempts required for input automation detection. The player must be moving more than 135.2 units/s for their counter-strafe to be considered an attempt. An attempt is either considered a success (counter-strafing took place within a single tick), an overlap (both directions were held for 1+ ticks) or an underlap (neither direction was held for 1+ ticks).

---
{{define_cvar("sv_auto_cstrafe_attempt_window")}}
The length of the window of trailing counter-strafe attempts considered during input automation detection.

---
{{define_cvar("sv_auto_cstrafe_sequence_length")}}
The length of sequential counter-strafe attempts evaluated relative to the success threshold. Input automation detection considers the best sequence within the larger attempt window.

---
{{define_cvar("sv_auto_cstrafe_success_threshold")}}
The minimum number of successful counter-strafes within a best sequence that will trigger input automation detection. The number of successes that trigger input automation detection is interpolated between the success threshold and a 'perfect' sequence (all counter-strafes in a sequence are successes), depending on the player's percentage of overlapping counter-strafe attempts.

---
{{define_cvar("sv_auto_cstrafe_lower_overlap_pct_threshold")}}
The percentage of overlapping attempts in the attempt window below which input automation detection is triggered at the success threshold.

---
{{define_cvar("sv_auto_cstrafe_upper_overlap_pct_threshold")}}
The percentage of overlapping attempts in the attempt window below which input automation detection is triggered when all counter-strafes in a sequence are successes.

---
{{define_cvar("sv_auto_cstrafe_logging")}}
0: never, 1: every time counter-strafe input automation is detected, 2: every counter-strafe

---
{{define_cvar("sv_auto_cstrafe_kick")}}
Whether or not to kick players when counter-strafe input automation is detected.

---
{{define_cvar("radarvismethod")}}
0 for traditional method, 1 for more realistic method

---
{{define_cvar("radarvispow")}}
the degree to which you can point away from a target, and still see them on radar.

---
{{define_cvar("radarvisdistance")}}
at this distance and beyond you need to be point right at someone to see them

---
{{define_cvar("radarvismaxdot")}}
how closely you have to point at someone to see them beyond max distance

---
{{define_cvar("mp_logdetail")}}
Logs attacks.  Values are: 0=off, 1=enemy, 2=teammate, 3=both)

---
{{define_cvar("mp_logdetail_items")}}
Logs a line any time a player acquires or loses an item.

---
{{define_cvar("sv_nonemesis")}}
Disable nemesis and revenge.

---
{{define_cvar("sv_debugroundstats")}}

---
{{define_cvar("sv_record_item_time_data")}}
Turn on recording of per player item time data into the server log.

---
{{define_cvar("dev_add_onground_on_spawn")}}
Should we mess with the ground flag when we spawn? (I don't think we should). If we don't hit the assert in CCSPlayer_MovementServices::ProcessMovement, we should remove this by Dec 2022.

---
{{define_cvar("sv_guardian_min_wave_for_heavy")}}

---
{{define_cvar("sv_guardian_max_wave_for_heavy")}}

---
{{define_cvar("sv_guardian_heavy_count")}}

---
{{define_cvar("sv_guardian_heavy_all")}}

---
{{define_cvar("sv_guardian_starting_equipment_humans")}}
Extra starting equipment for human players in guardian modes

---
{{define_cvar("sv_guardian_health_refresh_per_wave")}}
Health given to survivors per wave in guardian mode.

---
{{define_cvar("sv_guardian_respawn_health")}}
Starting health of guardian players when respawned.

---
{{define_cvar("cs_logtouchexpansion")}}
cs_logtouchexpansion <ent index or -1 for all>. Log player touch expansion component.

---
{{define_cvar("sv_show_teammate_death_notification")}}
Show chat notification upon teammate death

---
{{define_cvar("bot_mimic_yaw_offset")}}

---
{{define_cvar("cs_ShowStateTransitions")}}
cs_ShowStateTransitions <ent index or -1 for all>. Show player state transitions.

---
{{define_cvar("sv_guardian_spawn_health_ct")}}
Starting health in guardian modes.

---
{{define_cvar("sv_guardian_spawn_health_t")}}
Starting health in guardian modes.

---
{{define_cvar("sv_nowinpanel")}}
Turn on/off win panel on server

---
{{define_cvar("sv_show_voip_indicator_for_enemies")}}
Makes it so the voip icon is shown over enemies as well as allies when they are talking

---
{{define_cvar("bot_mimic")}}
Bot uses usercmd of player by index.

---
{{define_cvar("bot_freeze")}}

---
{{define_cvar("cs_hostage_near_rescue_music_distance")}}

---
{{define_cvar("sv_dz_cash_bundle_size")}}
Size of a cash bundle

---
{{define_cvar("sv_dz_cash_mega_bundle_size")}}
Size of a mega cash bundle

---
{{define_cvar("sv_dz_contractkill_reward")}}
Cash bundles to award for a successful contract kill

---
{{define_cvar("mp_deathcam_skippable")}}
Determines whether a player can early-out of the deathcam.

---
{{define_cvar("sv_max_deathmatch_respawns_per_tick")}}

---
{{define_cvar("sv_radio_throttle_window")}}
The number of seconds before radio command tokens refresh.

---
{{define_cvar("tv_relayradio")}}
Relay team radio commands to TV: 0=off, 1=on

---
{{define_cvar("bot_chatter_use_rr")}}
0 = Use old bot chatter system, 1 = Use response rules

---
{{define_cvar("sv_playerradio_use_allowlist")}}
playerradio commands may only use responses from an allow list of commands.

---
{{define_cvar("sv_vote_timer_duration")}}
How long to allow voting on an issue

---
{{define_cvar("sv_vote_command_delay")}}
How long after a vote passes until the action happens

---
{{define_cvar("sv_allow_votes")}}
Allow voting?

---
{{define_cvar("sv_vote_failure_timer")}}
A vote that fails cannot be re-submitted for this long

---
{{define_cvar("sv_vote_creation_timer")}}
How often someone can individually call a vote.

---
{{define_cvar("sv_vote_quorum_ratio")}}
The minimum ratio of players needed to vote on an issue to resolve it.

---
{{define_cvar("sv_vote_allow_spectators")}}
Allow spectators to initiate votes?

---
{{define_cvar("sv_vote_count_spectator_votes")}}
Allow spectators to vote on issues?

---
{{define_cvar("sv_vote_allow_in_warmup")}}
Allow voting during warmup?

---
{{define_cvar("sv_vote_disallow_kick_on_match_point")}}
Disallow vote kicking on the match point round.

---
{{define_cvar("sv_mapvetopickvote_maps")}}
Which maps are used for map veto pick sequence

---
{{define_cvar("sv_mapvetopickvote_phase_duration")}}
How many seconds each phase lasts

---
{{define_cvar("sv_mapvetopickvote_rnd")}}
When enabled will shuffle veto pick maps list order every time

---
{{define_cvar("sv_vote_issue_restart_game_allowed")}}
Can people hold votes to restart the game?

---
{{define_cvar("sv_vote_issue_kick_allowed")}}
Can people hold votes to kick players from the server?

---
{{define_cvar("sv_vote_kick_ban_duration")}}
How long should a kick vote ban someone from the server? (in minutes)

---
{{define_cvar("sv_vote_issue_loadbackup_allowed")}}
Can people hold votes to load match from backup?

---
{{define_cvar("sv_vote_issue_loadbackup_spec_only")}}
When enabled, only admins load match from backup

---
{{define_cvar("sv_vote_issue_loadbackup_spec_safe")}}
When enabled, admins load match from backup in safe time of the round only

---
{{define_cvar("sv_vote_issue_loadbackup_spec_authoritative")}}
When enabled, admins load match from backup without players vote

---
{{define_cvar("sv_vote_issue_changelevel_allowed")}}
Can people hold votes to change levels?

---
{{define_cvar("sv_vote_to_changelevel_before_match_point")}}
Restricts vote to change level to rounds prior to match point (default 0, vote is never disallowed)

---
{{define_cvar("sv_vote_to_changelevel_rndmin")}}
When non-zero, restricts vote to change level to this many first rounds or minutes of the match (default 0, vote is not disallowed)

---
{{define_cvar("sv_vote_issue_nextlevel_allowed")}}
Can people hold votes to set the next level?

---
{{define_cvar("sv_vote_issue_nextlevel_choicesmode")}}
Present players with a list of lowest playtime maps to choose from?

---
{{define_cvar("sv_vote_issue_nextlevel_allowextend")}}
Allow players to extend the current map?

---
{{define_cvar("sv_vote_issue_nextlevel_prevent_change")}}
Not allowed to vote for a nextlevel if one has already been set.

---
{{define_cvar("sv_vote_issue_scramble_teams_allowed")}}
Can people hold votes to scramble the teams?

---
{{define_cvar("sv_vote_issue_pause_match_allowed")}}
Can people hold votes to pause/unpause the match?

---
{{define_cvar("sv_vote_issue_pause_match_spec_only")}}
When enabled, only admins start technical pause

---
{{define_cvar("sv_vote_issue_timeout_allowed")}}
Can people hold votes to time out?

---
{{define_cvar("sv_vote_issue_matchready_allowed")}}
Can people hold votes to ready/unready the match?

---
{{define_cvar("sv_vote_issue_swap_teams_allowed")}}
Can people hold votes to swap the teams?

---
{{define_cvar("sv_vote_issue_surrrender_allowed")}}
Can people hold votes to surrender?

---
{{define_cvar("sv_smoke_perf_test")}}

---
{{define_cvar("r_csgo_lowend_objects")}}
0 = Force disable, 1 = use video settings

---
{{define_cvar("r_refraction_clip_plane_adjust")}}

---
{{define_cvar("r_particle_shadows")}}

---
{{define_cvar("r_particle_shadows_cast_on_particles")}}

---
{{define_cvar("r_particle_shadows_cast_on_particles_scale")}}

---
{{define_cvar("r_particle_shadows_compute")}}

---
{{define_cvar("r_particle_shadows_cast_on_world")}}

---
{{define_cvar("r_particle_shadow_map_texture_size")}}

---
{{define_cvar("r_debug_particle_shadows")}}

---
{{define_cvar("r_csgo_fsr_upsample")}}
0 == bilinear upsampe, 1 == FSR upsample, 2 == FSR + RCAS upsample

---
{{define_cvar("r_csgo_fsr_rcas_sharpness")}}
RCAS sharpness when using FSR + RCAS upsample.

---
{{define_cvar("r_csgo_fsr_enable_mip_bias")}}
Apply negative mip bias when rendering with FSR.

---
{{define_cvar("r_csgo_enable_sunlight_check")}}
Enable vis tests for sunlight.

---
{{define_cvar("r_csgo_mixed_resolution_particles")}}

---
{{define_cvar("r_csgo_mixed_resolution_color_slices")}}

---
{{define_cvar("r_csgo_mixed_resolution_particles_scale")}}

---
{{define_cvar("r_csgo_mixed_resolution_particles_minmax")}}

---
{{define_cvar("r_csgo_mboit")}}

---
{{define_cvar("r_csgo_mboit_debug")}}

---
{{define_cvar("r_csgo_mboit_overestimation")}}

---
{{define_cvar("r_csgo_mboit_bias")}}

---
{{define_cvar("r_csgo_mboit_use_4_moments")}}

---
{{define_cvar("r_csgo_mboit_upscale_cs")}}

---
{{define_cvar("r_csgo_mboit_force_mixed_resolution")}}

---
{{define_cvar("r_csgo_joint_upscale_sigma")}}

---
{{define_cvar("r_csgo_upscale_depth_threshold")}}

---
{{define_cvar("r_csgo_volume_mboit_optimization")}}

---
{{define_cvar("r_csgo_cmaa_enable")}}

---
{{define_cvar("r_csgo_cmaa_quality")}}
0=low, 1=medium, 2=high, 3=ultra

---
{{define_cvar("r_csgo_cmaa_extra_sharp")}}
trade more sharpness for reduced antialiasing

---
{{define_cvar("r_csgo_cmaa_debug_edges")}}
debug visualize edges

---
{{define_cvar("r_csgo_gpu_culling")}}
CSGO/Graphics/GPU Culling

---
{{define_cvar("r_csgo_gpu_culling_two_pass")}}
CSGO/Graphics/GPU Culling (Two Pass)

---
{{define_cvar("r_csgo_gpu_culling_shadows")}}
CSGO/Graphics/GPU Cull Shadow Views

---
{{define_cvar("r_csgo_gpu_culling_camera_offset")}}

---
{{define_cvar("r_csgo_decals_use_msaa")}}

---
{{define_cvar("r_csgo_smoke_overlay_min_dt")}}

---
{{define_cvar("r_csgo_smoke_fullres_pass")}}
Does a full res pass to cover holes and artifacts in smoke low res

---
{{define_cvar("r_csgo_smoke_fullres_enhance")}}
Enhance edges of smokes to eliminate bad pixels

---
{{define_cvar("r_csgo_msaa_resolve_apply_exposure_scale")}}
0 - before, 1 - after fix for a2c fringing

---
{{define_cvar("r_csgo_resolve_dither_noise_amount")}}
Amount of screen space dither noise to apply during resolve (used/essential with R11G11B10_FLOAT RT)

---
{{define_cvar("r_csgo_resolve_dither_bluenoise_amount")}}
Equivalent to r_csgo_render_dither_scale, but purely to control bluenoise for R11G11B10 downsample dither (if r_csgo_r11g11b10_dither_mode = 2)

---
{{define_cvar("r_csgo_r11g11b10_dither_mode")}}
0 - disabled, 1 - regular dither noise, 2 - blue noise dither

---
{{define_cvar("r_csgo_cable_pixel_radius_clamp")}}
Minimum clamped size in pixels of a cable (if using F_CLAMP_MIN_RADIUS 1 in cable material)

---
{{define_cvar("r_csgo_override_global_time")}}

---
{{define_cvar("r_csgo_mouse_trace_coord")}}

---
{{define_cvar("r_csgo_smoke_shadow")}}

---
{{define_cvar("r_csgo_smoke_upscale_discard_pixels_behind")}}
When upsampling smoke discard pixels behind solid depth to avoid pixelated artifacts

---
{{define_cvar("r_csgo_reconstruct_normals")}}

---
{{define_cvar("r_csgo_reconstruct_normals_method")}}

---
{{define_cvar("r_csgo_smoke_avoid_flat")}}

---
{{define_cvar("r_csgo_smoke_clip_sniper")}}

---
{{define_cvar("r_csgo_viewmodel_near_plane")}}

---
{{define_cvar("r_csgo_viewmodel_far_plane")}}

---
{{define_cvar("r_csgo_viewmodel_csm_pushback_distance")}}

---
{{define_cvar("r_csgo_csm_pushback_distance")}}

---
{{define_cvar("csgo_3d_skybox")}}

---
{{define_cvar("csgo_use_fullsort_for_opaque")}}
fullsort the opaque pass when there wasn't a depth prepass

---
{{define_cvar("r_csgo_prewarm_particles")}}

---
{{define_cvar("r_show_build_info")}}
Build information. Leave this enabled when submitting bug screenshots and videos, please!

---
{{define_cvar("r_show_time_info")}}
Show real time, large.

---
{{define_cvar("r_csgo_preview_csm_pushback_distance")}}

---
{{define_cvar("r_csgo_preview_csm_max_visible_distance")}}

---
{{define_cvar("r_csgo_debug_reflection_rects")}}

---
{{define_cvar("r_csgo_depth_prepass_reflections_large")}}

---
{{define_cvar("r_csgo_depth_prepass_reflections_small")}}

---
{{define_cvar("r_csgo_water_reflections")}}

---
{{define_cvar("camera_datadriven_debug")}}

---
{{define_cvar("webapi_values_max_pool_size_mb")}}
Maximum size in bytes of the WebAPIValues buffer pool

---
{{define_cvar("webapi_values_init_buffer_size")}}
Initial buffer size for buffers in the WebAPIValues buffer pool

---
{{define_cvar("weapon_debug_spread_show")}}
Enables display of weapon accuracy; 1: show accuracy box, 3: show accuracy with dynamic crosshair

---
{{define_cvar("weapon_debug_spread_gap")}}

---
{{define_cvar("cl_crosshair_drawoutline")}}
Draws a black outline around the crosshair for better visibility

---
{{define_cvar("cl_crosshair_outlinethickness")}}
Set how thick you want your crosshair outline to draw (0-3)

---
{{define_cvar("cl_crosshair_dynamic_splitdist")}}
If using cl_crosshairstyle 2, this is the distance that the crosshair pips will split into 2. (default is 7)

---
{{define_cvar("cl_crosshair_dynamic_splitalpha_innermod")}}
If using cl_crosshairstyle 2, this is the alpha modification that will be used for the INNER crosshair pips once they've split. [0 - 1]

---
{{define_cvar("cl_crosshair_dynamic_splitalpha_outermod")}}
If using cl_crosshairstyle 2, this is the alpha modification that will be used for the OUTER crosshair pips once they've split. [0.3 - 1]

---
{{define_cvar("cl_crosshair_dynamic_maxdist_splitratio")}}
If using cl_crosshairstyle 2, this is the ratio used to determine how long the inner and outer xhair pips will be. [inner = cl_crosshairsize*(1-cl_crosshair_dynamic_maxdist_splitratio), outer = cl_crosshairsize*cl_crosshair_dynamic_maxdist_splitratio]  [0 - 1]

---
{{define_cvar("cl_show_observer_crosshair")}}
Show the crosshair of the player being observed. 0: off 1: friends and party 2: everyone 

---
{{define_cvar("cl_observed_bot_crosshair")}}
Control the crosshair shown when observing a bot. 0: Show player crosshair. 1: Show player crosshair only when bot can be taken over, otherwise show default.. 2: Always show default crosshair for bots.

---
{{define_cvar("cl_fixedcrosshairgap")}}
For crosshair style 1: How big to make the gap between the pips in the fixed crosshair

---
{{define_cvar("cl_crosshair_t")}}
T style crosshair

---
{{define_cvar("cl_show_quest_info")}}

---
{{define_cvar("cl_paintkit_override")}}

---
{{define_cvar("econ_enable_inventory_images")}}
allow inventory image rendering for use by scaleform

---
{{define_cvar("econ_inventory_image_pinboard")}}

---
{{define_cvar("cl_ignore_campaign_completion_requirements")}}
Ignores campaign progression requirements when granting quests.

---
{{define_cvar("cl_use_old_wearable_shoulddraw")}}

---
{{define_cvar("cl_hud_telemetry_frametime_show")}}
Show frame time (FPS) in the HUD.  0=never, 1=only if poor, 2=always

---
{{define_cvar("cl_hud_telemetry_frametime_poor")}}
Frame time greater than this is considered 'poor'.

---
{{define_cvar("cl_hud_telemetry_ping_show")}}
Show ping in the HUD.  0=never, 1=only in poor conditions, 2=always

---
{{define_cvar("cl_hud_telemetry_ping_poor")}}
Ping higher than this (ms) is considered 'poor'.

---
{{define_cvar("cl_hud_telemetry_net_misdelivery_show")}}
Show packet delivery anomaly (loss or out-of-order) rate in the HUD.  0=never, 1=only in poor conditions, 2=always

---
{{define_cvar("cl_hud_telemetry_net_misdelivery_poor")}}
Packet delivery anomaly rate (0..100) higher than this is considered 'poor'.

---
{{define_cvar("cl_hud_telemetry_net_quality_graph_show")}}
Show packet jitter and netframe loss/reordering in the HUD.  0=never, 1=only in poor conditions, 2=always

---
{{define_cvar("cl_hud_telemetry_serverrecvmargin_graph_show")}}
Show graph of the server recv margin in the HUD.  (How early/late user commands are arriving at the server before they are executed.)   0=never, 1=only when there are command queue problems, 2=always

---
{{define_cvar("dota_toast_manager_override_duration")}}

---
{{define_cvar("sticky_tooltips")}}
Don't ever hide tooltips. Helpful when debugging complicated tooltip layouts.

---
{{define_cvar("r_csgo_render_post_fxaa")}}

---
{{define_cvar("r_csgo_render_post_colorcorrection")}}

---
{{define_cvar("r_csgo_render_post_bloom")}}

---
{{define_cvar("r_csgo_render_post_film_grain")}}

---
{{define_cvar("r_csgo_render_dither_scale")}}

---
{{define_cvar("r_csgo_render_post_mirror_horizontal")}}

---
{{define_cvar("r_csgo_render_post_mirror_vertical")}}

---
{{define_cvar("glow_outline_width")}}
Width of glow outline effect in screen space.

---
{{define_cvar("r_bloom_tent_filter_radius")}}
bloom mip up-sample filtering radius (using 3x3 tent filter, radius in mip level texels), 0.0 radius => box (2x2) filter with (fixed) 1.0 radius

---
{{define_cvar("r_depth_of_field")}}
0 = off, 1 = enabled (high quality, circular bokeh, HDR)

---
{{define_cvar("r_dof2_radiusscale")}}

---
{{define_cvar("r_dof2_maxblursize")}}

---
{{define_cvar("mat_disable_normal_mapping")}}

---
{{define_cvar("r_csgo_enable_tonemapping")}}

---
{{define_cvar("r_csgo_enable_volume_fog")}}

---
{{define_cvar("r_csgo_enable_cubemap_fog")}}

---
{{define_cvar("r_csgo_enable_gradient_fog")}}

---
{{define_cvar("r_csgo_shadows_debug")}}

---
{{define_cvar("r_aoproxy_debug")}}

---
{{define_cvar("r_aoproxy_enable")}}

---
{{define_cvar("r_csgo_decal_debug")}}

---
{{define_cvar("r_csgo_depth_prepass")}}

---
{{define_cvar("r_csgo_depth_prepass_cull_threshold")}}

---
{{define_cvar("r_csgo_depth_prepass_small_cull_threshold")}}

---
{{define_cvar("r_csgo_depth_prepass_viewmodel")}}

---
{{define_cvar("r_csgo_depth_prepass_skybox_alpha_tested")}}

---
{{define_cvar("r_csgo_render_opaque")}}

---
{{define_cvar("r_csgo_render_overlays")}}

---
{{define_cvar("r_csgo_render_decals")}}

---
{{define_cvar("r_csgo_render_inferno_decals")}}

---
{{define_cvar("r_csgo_render_decals_on_translucent")}}

---
{{define_cvar("r_csgo_render_translucent")}}

---
{{define_cvar("r_csgo_readonly_depth_stencil_enable")}}

---
{{define_cvar("r_csgo_enable_glows")}}

---
{{define_cvar("r_csgo_outline_glow_scaledenom")}}

---
{{define_cvar("r_csgo_enable_translucent_screen_space")}}

---
{{define_cvar("r_csgo_render_dynamic_objects")}}

---
{{define_cvar("r_csgo_no_shader_resolve")}}

---
{{define_cvar("r_csgo_effects_bloom")}}

---
{{define_cvar("r_csgo_effects_bloom_when_smoked")}}

---
{{define_cvar("r_csgo_cubemap_normalization")}}

---
{{define_cvar("r_csgo_postprocess_enable")}}

---
{{define_cvar("r_csgo_enable_high_precision_lighting")}}

---
{{define_cvar("r_csgo_render_post_local_contrast")}}

---
{{define_cvar("r_csgo_directional_lightmaps")}}

---
{{define_cvar("r_csgo_multiscattering")}}

---
{{define_cvar("r_csgo_microshadowing")}}

---
{{define_cvar("r_csgo_viewmodel_envmap_position_bias")}}

---
{{define_cvar("r_csgo_viewmodel_envmap_clamp_plane_distance")}}

---
{{define_cvar("r_csgo_tools_vis_cubemap_roughness")}}

---
{{define_cvar("r_csgo_stencil_sniper_zoom")}}

---
{{define_cvar("r_csgo_firstpersonlegs_nearz_offset")}}

---
{{define_cvar("r_csgo_shadow_map_allocation_failure_policy")}}
What happens when a shadow map fails allocation? 0 = don't render, 1 = render unshadowed

---
{{define_cvar("r_csgo_water_effects")}}

---
{{define_cvar("r_csgo_reflection_min_far_plane")}}

---
{{define_cvar("r_csgo_water_refraction")}}

---
{{define_cvar("r_csgo_water_skybox_depth")}}

---
{{define_cvar("r_player_fog_maxdensity_multiplier")}}

---
{{define_cvar("r_player_fog_distance_multiplier")}}

---
{{define_cvar("r_player_visibility_mode")}}

---
{{define_cvar("r_player_visibility_strength")}}

---
{{define_cvar("r_player_visibility_stencil")}}

---
{{define_cvar("r_post_bloom_debug")}}
1 = bloom output (before thresholding), 2 = quarter res downsample, 3 = quarter res effects bloom 4 = quarter res effects raw

---
{{define_cvar("r_csgo_render_post_bloom_strength")}}

---
{{define_cvar("r_csgo_bloom_threshold_all_samples")}}
Execute bloom threshold once per sample during downsample (default enabled, higher quality, less bloom aliasing)

---
{{define_cvar("r_csgo_bloom_threshold_downsample_jimenez")}}
Custom downsample based on Jimenez14, (default enabled, higher quality, decreases bloom aliasing further)

---
{{define_cvar("r_render_to_cubemap_begin_mixing_roughness")}}

---
{{define_cvar("cl_loadout_saved_sort")}}

---
{{define_cvar("ui_lobby_draft_enabled")}}

---
{{define_cvar("gotv_theater_container")}}
Enables GOTV theater mode for the specified container, setting it to 'live' will play top live matches

---
{{define_cvar("cl_spec_stats")}}

---
{{define_cvar("cl_server_graphic1_enable")}}
When enabled, 360x60 (<16kb) image file will be displayed to on-server spectators.

---
{{define_cvar("cl_server_graphic2_enable")}}
When enabled, 220x45 (<16kb) image file will be displayed to on-server spectators.

---
{{define_cvar("ui_render_task_fps")}}

---
{{define_cvar("ui_render_task_file")}}

---
{{define_cvar("ui_render_task_generate_clips")}}

---
{{define_cvar("ui_render_task_clips_label")}}

---
{{define_cvar("partybrowser_throttle_data")}}

---
{{define_cvar("partybrowser_timeout")}}

---
{{define_cvar("cl_invites_only_friends")}}
If turned on, will ignore in-game invites from recent teammates or other non-friends

---
{{define_cvar("cl_invites_only_mainmenu")}}
If turned on, will ignore all invites when user is playing a match

---
{{define_cvar("cachedvalue_count_partybrowser")}}

---
{{define_cvar("cl_voip_lobby_audio_volume")}}
Lobby voip stream audio volume

---
{{define_cvar("cl_matchlist_controlroom_aid")}}

---
{{define_cvar("ui_nearbylobbies_filter3")}}

---
{{define_cvar("ui_playsettings_mode_listen")}}

---
{{define_cvar("ui_playsettings_mode_official_v20")}}

---
{{define_cvar("ui_playsettings_maps_official_casual")}}

---
{{define_cvar("ui_playsettings_maps_official_deathmatch")}}

---
{{define_cvar("ui_playsettings_maps_listen_competitive")}}

---
{{define_cvar("ui_playsettings_maps_listen_scrimcomp2v2")}}

---
{{define_cvar("ui_playsettings_maps_listen_skirmish")}}

---
{{define_cvar("ui_playsettings_maps_listen_casual")}}

---
{{define_cvar("ui_playsettings_maps_listen_deathmatch")}}

---
{{define_cvar("ui_playsettings_maps_official_gungameprogressive")}}

---
{{define_cvar("ui_playsettings_custom_preset")}}

---
{{define_cvar("ui_playsettings_flags_listen_scrimcomp2v2")}}

---
{{define_cvar("ui_playsettings_flags_listen_skirmish")}}

---
{{define_cvar("ui_playsettings_flags_listen_casual")}}

---
{{define_cvar("ui_playsettings_flags_listen_survival")}}

---
{{define_cvar("ui_playsettings_flags_listen_cooperative")}}

---
{{define_cvar("ui_playsettings_flags_listen_competitive")}}

---
{{define_cvar("ui_playsettings_flags_listen_deathmatch")}}

---
{{define_cvar("ui_playsettings_flags_official_scrimcomp2v2")}}

---
{{define_cvar("ui_playsettings_flags_official_skirmish")}}

---
{{define_cvar("ui_playsettings_flags_official_casual")}}

---
{{define_cvar("ui_playsettings_flags_official_survival")}}

---
{{define_cvar("ui_playsettings_flags_official_cooperative")}}

---
{{define_cvar("ui_playsettings_flags_official_competitive")}}

---
{{define_cvar("ui_playsettings_flags_official_deathmatch")}}

---
{{define_cvar("ui_playsettings_directchallengekey")}}

---
{{define_cvar("ui_playsettings_maps_workshop")}}

---
{{define_cvar("ui_vanitysetting_team")}}

---
{{define_cvar("ui_show_unlock_competitive_alert")}}

---
{{define_cvar("ui_vanitysetting_loadoutslot_ct")}}

---
{{define_cvar("ui_vanitysetting_loadoutslot_t")}}

---
{{define_cvar("ui_news_last_read_link")}}

---
{{define_cvar("ui_notification_tb_snooze")}}

---
{{define_cvar("ui_playsettings_warmup_map_name")}}

---
{{define_cvar("ui_playsettings_survival_solo")}}

---
{{define_cvar("ui_inventorysettings_recently_acknowledged")}}

---
{{define_cvar("player_botdifflast_s")}}

---
{{define_cvar("ui_deepstats_toplevel_mode")}}

---
{{define_cvar("ui_deepstats_radio_heat_tab")}}

---
{{define_cvar("ui_deepstats_radio_heat_team")}}

---
{{define_cvar("ui_deepstats_radio_heat_figurine")}}

---
{{define_cvar("ui_popup_weaponupdate_version")}}

---
{{define_cvar("ui_show_subscription_alert")}}

---
{{define_cvar("cl_redemption_reset_timestamp")}}

---
{{define_cvar("ui_mainmenu_bkgnd_movie_B0B70CFF")}}
Main menu background movie

---
{{define_cvar("ui_inspect_bkgnd_map_B0B70CFF")}}
Inspect background map

---
{{define_cvar("lobby_default_privacy_bits2")}}
Lobby default permissions (0: private, 1: public)

---
{{define_cvar("cl_clanid")}}
Current clan ID for name decoration

---
{{define_cvar("ui_setting_advertiseforhire_auto")}}
Whether users will automatically advertise for invites (0: off; 1: last; 2: auto)

---
{{define_cvar("ui_setting_advertiseforhire_auto_last")}}
Which game mode users last used to advertise for invites

---
{{define_cvar("install_dlc_workshoptools_cvar")}}
DLC Install Status

---
{{define_cvar("key_bind_version")}}

---
{{define_cvar("cl_net_buffer_ticks_use_interp")}}
If false, we smooth over packet loss by adjusting the clock synchronization to buffer packets.  If true, we process packets immediately and use cl_interp to delay their effects

---
{{define_cvar("cl_net_buffer_ticks")}}
Number of ticks of delay for server snapshots and user commands.  This value controls the value of cl_interp_ratio, which you should not modify directly.

---
{{define_cvar("cl_streams_request_url")}}
Number of streams requested for display

---
{{define_cvar("cl_streams_request_accept")}}
Header for api request

---
{{define_cvar("cl_streams_image_sfurl")}}
Format of Scaleform image representing the stream

---
{{define_cvar("cl_streams_refresh_interval")}}
How often to refresh streams list

---
{{define_cvar("cl_streams_write_response_file")}}
When set will save streams info file for diagnostics

---
{{define_cvar("cl_streams_mytwitchtv_nolink")}}
Twitch.tv account linking URL

---
{{define_cvar("cl_streams_mytwitchtv_channel")}}
Twitch.tv account channel URL

---
{{define_cvar("cachedvalue_count_teammates")}}

---
{{define_cvar("vm_draw_always")}}

---
{{define_cvar("vm_camera")}}

---
{{define_cvar("vm_camera_scale")}}

---
{{define_cvar("vm_camera_no_roll")}}

---
{{define_cvar("vm_camera_interp_speed")}}

---
{{define_cvar("cl_crosshairstyle")}}
0 = DEFAULT (DISABLED), 1 = DEFAULT STATIC (DISABLED), 2 = DEFAULT (accurate recoil/spread feedback with a fixed inner part), 3 = ACCURATE DYNAMIC (DISABLED) (accurate recoil/spread feedback), 4 = DEFAULT STATIC, 5 = LEGACY (fake recoil - inaccurate feedback)

---
{{define_cvar("cl_crosshaircolor")}}
Set crosshair color as defined in game_options.consoles.txt

---
{{define_cvar("cl_crosshairalpha")}}

---
{{define_cvar("cl_crosshairusealpha")}}

---
{{define_cvar("cl_crosshairgap")}}

---
{{define_cvar("cl_crosshairgap_useweaponvalue")}}
If set to 1, the gap will update dynamically based on which weapon is currently equipped

---
{{define_cvar("cl_crosshairsize")}}

---
{{define_cvar("cl_crosshairthickness")}}

---
{{define_cvar("cl_crosshairdot")}}

---
{{define_cvar("cl_crosshair_recoil")}}

---
{{define_cvar("cl_crosshaircolor_r")}}

---
{{define_cvar("cl_crosshaircolor_g")}}

---
{{define_cvar("cl_crosshaircolor_b")}}

---
{{define_cvar("cl_min_movie_time")}}

---
{{define_cvar("cl_min_china_movie_time")}}

---
{{define_cvar("csgo_vanity_defer_teleport")}}

---
{{define_cvar("cl_quickinventory_lastinv")}}

---
{{define_cvar("cl_quickinventory_line_update_speed")}}

---
{{define_cvar("cl_quickinventory_filename")}}

---
{{define_cvar("cl_radial_radio_tab")}}

---
{{define_cvar("cl_radial_radio_tab_0_text_1")}}

---
{{define_cvar("cl_radial_radio_tab_0_text_2")}}

---
{{define_cvar("cl_radial_radio_tab_0_text_3")}}

---
{{define_cvar("cl_radial_radio_tab_0_text_4")}}

---
{{define_cvar("cl_radial_radio_tab_0_text_5")}}

---
{{define_cvar("cl_radial_radio_tab_0_text_6")}}

---
{{define_cvar("cl_radial_radio_tab_0_text_7")}}

---
{{define_cvar("cl_radial_radio_tab_0_text_8")}}

---
{{define_cvar("cl_radial_radio_tab_1_text_1")}}

---
{{define_cvar("cl_radial_radio_tab_1_text_2")}}

---
{{define_cvar("cl_radial_radio_tab_1_text_3")}}

---
{{define_cvar("cl_radial_radio_tab_1_text_4")}}

---
{{define_cvar("cl_radial_radio_tab_1_text_5")}}

---
{{define_cvar("cl_radial_radio_tab_1_text_6")}}

---
{{define_cvar("cl_radial_radio_tab_1_text_7")}}

---
{{define_cvar("cl_radial_radio_tab_1_text_8")}}

---
{{define_cvar("cl_radial_radio_tab_2_text_1")}}

---
{{define_cvar("cl_radial_radio_tab_2_text_2")}}

---
{{define_cvar("cl_radial_radio_tab_2_text_3")}}

---
{{define_cvar("cl_radial_radio_tab_2_text_4")}}

---
{{define_cvar("cl_radial_radio_tab_2_text_5")}}

---
{{define_cvar("cl_radial_radio_tab_2_text_6")}}

---
{{define_cvar("cl_radial_radio_tab_2_text_7")}}

---
{{define_cvar("cl_radial_radio_tab_2_text_8")}}

---
{{define_cvar("cl_radial_radio_version_reset")}}

---
{{define_cvar("cl_radial_radio_tap_to_ping")}}
When tapping the radial radio button, leave a ping if nothing is selected within the time in seconds set in cl_radial_menu_tap_duration

---
{{define_cvar("cl_radialmenu_deadzone_size")}}

---
{{define_cvar("cl_radialmenu_deadzone_size_joystick")}}

---
{{define_cvar("cl_radial_menu_icon_radius")}}

---
{{define_cvar("cl_radial_menu_tap_duration")}}
If nothing in a radial menu is selected, and the button engaging the radial menu is released within this duration, fallback on the radial's tap functionality

---
{{define_cvar("cl_radial_coyote_time")}}
Selection lenience: How long in seconds the last selected radial segment is used if no segment is selected.

---
{{define_cvar("cl_scoreboard_survivors_always_on")}}

---
{{define_cvar("cl_ui_particles_destroy_when_not_painting")}}

---
{{define_cvar("r_dac_disable_portrait_world_renderer")}}

---
{{define_cvar("videocfg_shadow_quality")}}

---
{{define_cvar("videocfg_texture_detail")}}

---
{{define_cvar("videocfg_particle_detail")}}

---
{{define_cvar("videocfg_ao_detail")}}

---
{{define_cvar("videocfg_hdr_detail")}}

---
{{define_cvar("videocfg_fsr_detail")}}

---
{{define_cvar("debug_video_config_cvars")}}

---
{{define_cvar("safezonex")}}
The percentage of the screen width that is considered safe from overscan. Cannot result in a width less than the height.

---
{{define_cvar("safezoney")}}
The percentage of the screen height that is considered safe from overscan

---
{{define_cvar("hud_scaling")}}
Scales hud elements

---
{{define_cvar("demo_ui_mode")}}
UI mode for demo playback. 0 = disabled, 1 = minimal, 2 = full

---
{{define_cvar("demo_mouse_enable_binding")}}
Name of the binding to enable mouse on demo playback UI

---
{{define_cvar("cl_deathnotices_show_numbers")}}
0: default; 1: draw names as just numbers; 2: append number on killer and victim to the name

---
{{define_cvar("spec_death_panel_replay_position")}}

---
{{define_cvar("cl_deathcampanel_position_dynamic")}}
Turn on/off deathcam's kill panel dynamic Y movement

---
{{define_cvar("death_panel_delay_time")}}

---
{{define_cvar("death_panel_travel_time")}}

---
{{define_cvar("csgo_demoui_player_death_seek_lead_up_time")}}
Seek to a moment this amount of seconds leading up to a player death instead of the exact time of the death.

---
{{define_cvar("csgo_demoui_previous_event_search_offset")}}
Do not consider events that happened in the last specified number of seconds when a user clicks 'previous' on the UI.

---
{{define_cvar("csgo_demoui_playbeck_timestep_value")}}
Number of seconds to seek when using TimeStep buttons on demo playback controller.

---
{{define_cvar("hinttext_displaytime")}}

---
{{define_cvar("cl_fake_timeout")}}

---
{{define_cvar("cl_crosshair_friendly_warning")}}
0: off, 1: on

---
{{define_cvar("cl_ping_fade_deadzone")}}
Distance from the crosshair over which the ping is completely invisible

---
{{define_cvar("cl_ping_fade_distance")}}
Distance from the crosshair over which the ping fades

---
{{define_cvar("sv_dz_show_enemy_name_scope_range")}}

---
{{define_cvar("cl_teamcounter_playercount_instead_of_avatars")}}

---
{{define_cvar("cl_teammate_color_1")}}

---
{{define_cvar("cl_teammate_color_2")}}

---
{{define_cvar("cl_teammate_color_3")}}

---
{{define_cvar("cl_teammate_color_4")}}

---
{{define_cvar("cl_teammate_color_5")}}

---
{{define_cvar("cl_drawhud_specvote")}}
1: default; 0: disables vote UI for spectators

---
{{define_cvar("cl_disable_round_end_report")}}

---
{{define_cvar("player_competitive_maplist_8_10_0_CAE97738")}}

---
{{define_cvar("player_competitive_maplist_2v2_10_0_12FCB095")}}

---
{{define_cvar("player_wargames_list2_10_0_0")}}

---
{{define_cvar("player_survival_list_10_0_303")}}

---
{{define_cvar("cl_embedded_stream_audio_volume")}}
Embedded stream audio volume

---
{{define_cvar("cl_embedded_stream_audio_volume_xmaster")}}
Whether embedded stream audio volume gets multiplied by master volume

---
{{define_cvar("cl_embedded_stream_video_playing")}}
Embedded stream video playing state

---
{{define_cvar("cl_promoted_settings_acknowledged")}}

---
{{define_cvar("cl_graphics_driver_warning_dont_show_again")}}

---
{{define_cvar("cl_vrr_recommendation_dont_show_again")}}

---
{{define_cvar("cl_refresh_rate_recommendation_dont_show_again")}}

---
{{define_cvar("cl_low_latency_vsync_recommendation_dont_show_again")}}

---
{{define_cvar("cl_mute_player_after_reporting_abuse")}}
Mute players reported for abuse automatically.

---
{{define_cvar("cl_inventory_saved_filter2")}}

---
{{define_cvar("cl_inventory_saved_sort2")}}

---
{{define_cvar("cl_inventory_debug_tooltip")}}

---
{{define_cvar("cl_access_all_missions")}}

---
{{define_cvar("ui_leaderboards_top_public_appid")}}

---
{{define_cvar("damage_impact_medium")}}
Damage BELOW this value is considered light damage

---
{{define_cvar("steam_controller_haptics")}}

---
{{define_cvar("steamworks_sessionid_client")}}
The client session ID for the new steamworks gamestats.

---
{{define_cvar("r_drawchickens")}}
Render chickens

---
{{define_cvar("inferno_dlight_spacing")}}
Inferno dlights are at least this far apart

---
{{define_cvar("inferno_dlights")}}
Min FPS at which molotov dlights will be created

---
{{define_cvar("inferno_fire")}}

---
{{define_cvar("Inferno_concav_plane_threshold")}}

---
{{define_cvar("inferno_batched_rays")}}

---
{{define_cvar("snd_mainmenu_music_break_time_min")}}
Minimum amount of time to pause between playing main menu music

---
{{define_cvar("snd_mainmenu_music_break_time_max")}}
Maximum amount of time to pause between playing main menu music

---
{{define_cvar("snd_menumusic_volume")}}
Volume of Menu / Non-gameplay music

---
{{define_cvar("snd_roundstart_volume")}}
Volume of Round Start Music

---
{{define_cvar("snd_roundaction_volume")}}
Volume of Move Action Music

---
{{define_cvar("snd_roundend_volume")}}
Volume of Won/Lost Music

---
{{define_cvar("snd_mvp_volume")}}
Volume of MVP Music

---
{{define_cvar("snd_mapobjective_volume")}}
Volume of Map Objective Music

---
{{define_cvar("snd_tensecondwarning_volume")}}
Volume of Ten Second Warnings

---
{{define_cvar("snd_deathcamera_volume")}}
Volume of Deathcam Timers

---
{{define_cvar("player_nevershow_communityservermessage")}}

---
{{define_cvar("ui_steam_overlay_notification_position")}}
Steam overlay notification position

---
{{define_cvar("ui_steam_overlay_notification_position_horz")}}
Steam overlay notification position horizontal offset

---
{{define_cvar("ui_steam_overlay_notification_position_vert")}}
Steam overlay notification position vertical offset

---
{{define_cvar("connect_lobby")}}
Sets the lobby ID to connect to on start.

---
{{define_cvar("trusted_launch")}}
Trusted launch status

---
{{define_cvar("snd_headphone_eq")}}
Select Headphone EQ Preset

---
{{define_cvar("snd_headphone_eq_active")}}
Select Headphone EQ Preset

---
{{define_cvar("cl_hide_avatar_images")}}
Hide avatar images for other players. 
	0 - Off.
	1 - Block All
	2 - Block all but friends

---
{{define_cvar("cl_show_equipped_character_for_player_avatars")}}

---
{{define_cvar("cl_allow_animated_avatars")}}
Whether or not to allow animated avatars

---
{{define_cvar("cl_buywheel_nonumberpurchasing")}}
Set non-zero to prevent buy wheel from purchasing via number keys

---
{{define_cvar("cl_buywheel_donate_key")}}
Set the key to use for donation in the buy menu. 0: Left Control; 1: Left Alt; 2: Left Shift.

---
{{define_cvar("cl_buymenu_ct_nextround_high")}}

---
{{define_cvar("cl_buymenu_ct_nextround_low")}}

---
{{define_cvar("cl_buymenu_t_nextround_high")}}

---
{{define_cvar("cl_buymenu_t_nextround_low")}}

---
{{define_cvar("ui_party_msg_sound_enabled")}}
When enabled, lobby messages will play a short sound

---
{{define_cvar("cl_grenadecrosshair_keepusercrosshair")}}
Keep the user's crosshair when the grenade crosshair is enabled

---
{{define_cvar("cl_grenadecrosshair_tickinterval")}}

---
{{define_cvar("cl_grenadecrosshair_tickscaling")}}

---
{{define_cvar("cl_grenadecrosshair_ticklabels")}}

---
{{define_cvar("eom_local_player_defeat_anim_enabled")}}

---
{{define_cvar("cl_inventory_radial_immediate_select")}}
In inventory selection radials. Select weapons the moment the cursor highlights them. Otherwise, only select the selected item on exit.

---
{{define_cvar("cl_inventory_radial_tap_to_cycle")}}
In inventory selection radials. Select weapons the moment the cursor highlights them. Otherwise, only select the selected item on exit.

---
{{define_cvar("cl_itemimages_dynamically_generated")}}
2: use render-targets, fallback to cache and disk; 1: no render targets, but use cache and fallback to disk; 0: disk assets only

---
{{define_cvar("panorama_3dpanel_camera_preset_blend_time")}}
time to blend between camera presets

---
{{define_cvar("panorama_3dpanel_anim_fadeinout_time_scale")}}
temp scale factor for animation fade in/out time

---
{{define_cvar("panorama_3dpanel_anims_pivotlock")}}
default true.

---
{{define_cvar("panorama_3dpanel_loadout_rotate_scale")}}

---
{{define_cvar("panorama_3dpanel_loadout_rotate_drag")}}

---
{{define_cvar("panorama_3dpanel_loadout_rotate_grab_scale")}}

---
{{define_cvar("panorama_3dpanel_loadout_rotate_frametime_multiplier")}}

---
{{define_cvar("panorama_3dpanel_camera_rotate_azimuth_scale")}}

---
{{define_cvar("panorama_3dpanel_camera_rotate_altitude_scale")}}

---
{{define_cvar("panorama_3dpanel_light_rotate_azimuth_scale")}}

---
{{define_cvar("panorama_3dpanel_light_rotate_altitude_scale")}}

---
{{define_cvar("panorama_3dpanel_light_move_scale")}}

---
{{define_cvar("panorama_3dpanel_camera_inout_scale_kb")}}

---
{{define_cvar("panorama_3dpanel_camera_inout_scale")}}

---
{{define_cvar("panorama_3dpanel_camera_lookat_scale")}}

---
{{define_cvar("panorama_light_inout_scale")}}

---
{{define_cvar("panorama_3dpanel_debuginfo_manifest")}}

---
{{define_cvar("panorama_3dpanel_debuginfo_item")}}

---
{{define_cvar("panorama_3dpanel_debuginfo_cam")}}

---
{{define_cvar("panorama_3dpanel_debuginfo_paused")}}

---
{{define_cvar("panorama_3dpanel_debuginfo_player")}}

---
{{define_cvar("panorama_3dpanel_debuginfo_anim")}}

---
{{define_cvar("panorama_3dpanel_camera_blend_mode")}}

---
{{define_cvar("csgo_map_preview_scale")}}

---
{{define_cvar("keychain_preview_limit_step")}}

---
{{define_cvar("mapoverview_allow_client_draw")}}
Allow a client to draw on the map overview

---
{{define_cvar("mapoverview_icon_scale")}}
Sets the icon scale multiplier for the overview map. Valid values are 0.5 to 3.0.

---
{{define_cvar("csgo_disable_preview_maps")}}

---
{{define_cvar("cl_map_preview_debug_jitter")}}

---
{{define_cvar("csgo_mappreview_transparent_background_col_performance")}}

---
{{define_cvar("csgo_mappreview_transparent_background_col_quality")}}

---
{{define_cvar("snd_vol_competitive")}}

---
{{define_cvar("snd_vol_casual")}}

---
{{define_cvar("snd_vol_spectator")}}

---
{{define_cvar("snd_vol_warmup")}}

---
{{define_cvar("snd_eq_arms_race")}}

---
{{define_cvar("snd_eq_deathmatch")}}

---
{{define_cvar("snd_eq_competitive")}}

---
{{define_cvar("snd_eq_casual")}}

---
{{define_cvar("snd_eq_spectator")}}

---
{{define_cvar("snd_eq_warmup")}}

---
{{define_cvar("spec_replay_colorcorrection")}}
Amount of color correction in deathcam replay

---
{{define_cvar("cl_disable_postprocessing")}}

---
{{define_cvar("cl_instant_death_anim")}}

---
{{define_cvar("cl_disable_deathcam_audio_mix_fade_out")}}
When set to true, disables audio being silenced while the death cam fades out.

---
{{define_cvar("cl_deathcam_audio_mix_phase1_fade_time")}}
Sets the amount of time we fade out over.

---
{{define_cvar("cl_deathcam_audio_mix_phase1_fade_amount")}}
Sets the amount of ducking to do on death cam fade out. When set to 1, full DeathFadeLayer is applied.

---
{{define_cvar("cl_deathcam_audio_mix_phase2_fade_time")}}
Sets the amount of time we fade out over.

---
{{define_cvar("cl_deathcam_audio_mix_phase2_fade_amount")}}
Sets the amount of ducking to do on death cam fade out. When set to 1, full DeathFadeLayer is applied.

---
{{define_cvar("cl_scoreboard_mouse_enable_binding")}}
Name of the binding to enable mouse selection in the scoreboard

---
{{define_cvar("snd_mute_mvp_music_live_players")}}
If set, MVP music is muted if players from both teams are still alive.

---
{{define_cvar("force_spectator_only_tools")}}

---
{{define_cvar("cl_import_csgo_config")}}

---
{{define_cvar("cl_debug_client_gamestats")}}

---
{{define_cvar("steamworks_sessionid_lifetime_client")}}
The full client session ID for the new steamworks gamestats.

---
{{define_cvar("cl_debug_round_stat_submission")}}

---
{{define_cvar("cl_csgo_shoot_debugvis_show_rdp")}}

---
{{define_cvar("cl_csgo_shoot_debugvis_rdp_text_x")}}

---
{{define_cvar("cl_csgo_shoot_debugvis_rdp_text_l")}}

---
{{define_cvar("cl_csgo_shoot_debugvis_show_los")}}
Show line of last shot.

---
{{define_cvar("cl_csgo_shoot_trim_input_frames")}}

---
{{define_cvar("cl_scoreboard_toggle_enable")}}

---
{{define_cvar("cl_interp_ratio")}}
Set number of client simulation interpolation ticks.

---
{{define_cvar("cl_allow_multi_input_binds")}}

---
{{define_cvar("demo_skip_to_shot_seconds_before")}}
How many seconds before the shot to skip to when skipping to a specific shot ID.

---
{{define_cvar("demo_highlight_seconds_before")}}
How many seconds before the actual highlight event to show when viewing highlights.

---
{{define_cvar("demo_highlight_seconds_after")}}
How many seconds after the actual highlight event to show when viewing highlights.

---
{{define_cvar("demo_highlight_fade_duration")}}
Duration of the fade in and of the fade out transitions (fade in + fade out is 2x this value).

---
{{define_cvar("demo_movie_write_intervals")}}
Write highlight interval metadata along with movie files when recording.

---
{{define_cvar("demo_pause_at_end")}}
Pause demo playback when the end of the file is reached, otherwise quit to main menu.

---
{{define_cvar("r_cs2_show_icon_editor")}}
CSGO/Icon Editor

---
{{define_cvar("r_icon_rendering_4xnice")}}
icon rendering 4x nice

---
{{define_cvar("r_icon_rendering_msaa_mode")}}
MSAA mode used for icon rendering 0-none, 1-2xMSAA, 2-4xMSAA, 3-6X, 4-8X, etc

---
{{define_cvar("r_icon_rendering_width")}}
icon rendering width

---
{{define_cvar("r_icon_rendering_height")}}
icon rendering height

---
{{define_cvar("r_icon_generate_runtime_mips")}}
generate mips for runtime

---
{{define_cvar("r_icon_generate_offline_mips")}}
generate mips via sidecar file for offline

---
{{define_cvar("r_icon_max_mip_width")}}
r_icon_max_mip_width

---
{{define_cvar("r_icon_show_timing")}}
show timing in output

---
{{define_cvar("r_icon_csm_pushback_distance")}}
csm pushback distance, should be much shorter/disabled for icon rendering

---
{{define_cvar("net_client_steamdatagram_enable_override")}}
0: Use connect method requested by GC.  >0: Always use SDR if possible.  <0: Always use direct UDP if possible

---
{{define_cvar("cl_show_matchmaking_stat_spew")}}

---
{{define_cvar("cl_search_key_token")}}
Development search key token.

---
{{define_cvar("lobby_stats_fake")}}

---
{{define_cvar("lobby_gamesearch_fake")}}

---
{{define_cvar("cl_session")}}

---
{{define_cvar("cl_color")}}
Preferred teammate color

---
{{define_cvar("tv_spectator_port_offset")}}

---
{{define_cvar("cl_new_user_phase")}}
0: Not Started, 1: Needs Training, 2: Training Complete, -1: Disabled

---
{{define_cvar("cl_player_visibility_stencil_bloat_amount")}}

---
{{define_cvar("cl_player_visibility_show_stencil_proxy")}}

---
{{define_cvar("cl_player_visibility_stencil_proxy_min_dist")}}

---
{{define_cvar("cl_player_visibility_stencil_proxy_min_dist_box")}}

---
{{define_cvar("cl_player_visibility_stencil_proxy_type")}}
0 - box, 1 - dodecahedron

---
{{define_cvar("cl_player_visibility_near")}}
cull characters nearer than this

---
{{define_cvar("cl_player_visibility_far")}}
distance at which proxy scale is maximized

---
{{define_cvar("cl_player_visibility_far_scale")}}
proxy scale multiplier at max dist (is 1.0 at mindist)

---
{{define_cvar("cl_track_aim_head_threshold")}}
Notify render device when rendering a frame with enemy head within threshold distance

---
{{define_cvar("cl_track_aim_head_log_closest")}}
Log when closest distance to head was reached and what it was

---
{{define_cvar("cl_track_render_eye_angles")}}
Spew render eye angles

---
{{define_cvar("cl_lagcompensation_test_target")}}
Player whose head is tracked to test lag compensation.

---
{{define_cvar("cl_lagcompensation_test_auto_target")}}
Auto-pick value of cl_lagcompensation_test_target.

---
{{define_cvar("smoke_volume_lod_ratio_change")}}

---
{{define_cvar("cs_steamvideo_max_time_between_multikill_events")}}
Maximum time in seconds between consecutive kills for them to be combined into a multikill event

---
{{define_cvar("cs_steamvideo_multikill_padding_time")}}
Time in seconds to add before the first kill and after the last kill for multikill events

---
{{define_cvar("cs_steamvideo_max_kills_per_multikill")}}
Max number of kills for a single multikill event

---
{{define_cvar("cl_clutch_mode")}}
Silence voice and other distracting sounds until the end of round or next death.

---
{{define_cvar("cl_mute_enemy_team")}}
Block all communication from players on the enemy team.

---
{{define_cvar("cl_mute_all_but_friends_and_party")}}
Only allow communication from friends and matchmaking party members. Set to 1 to apply the in non-competitive game modes. Set to 2 will apply the setting in all modes.


---
{{define_cvar("cl_workshop_map_download_timeout")}}

---
{{define_cvar("r_drawdetailprops")}}

---
{{define_cvar("r_detail_lerp_znormal")}}

---
{{define_cvar("r_detailprop_lod_dist")}}

---
{{define_cvar("r_detailprop_fade_dist")}}

---
{{define_cvar("r_detailprop_force_probe")}}

---
{{define_cvar("cl_http_log_enable")}}
Allows sending HTTP log from client main menu.

---
{{define_cvar("damage_impact_heavy")}}
Damage ABOVE this value is considered heavy damage

---
{{define_cvar("r_decals")}}

---
{{define_cvar("cl_fasttempentcollision")}}

---
{{define_cvar("cl_tracer_whiz_distance")}}

---
{{define_cvar("cl_tracer_whiz_infront_distance")}}

---
{{define_cvar("fx_drawmetalspark")}}
Draw metal spark effects.

---
{{define_cvar("cl_playerspraydisable")}}
Disable player sprays.

---
{{define_cvar("r_icon_custommaterial_maxres")}}
maxres for custommaterials when rendering icons

---
{{define_cvar("r_icon_player_equip_gloves_from_loadout")}}
equip gloves on player for icon rendering from loadout, or use default gloves

---
{{define_cvar("r_icon_use_kv3_camera")}}
use test kv3 data for camera

---
{{define_cvar("r_icon_reload_map")}}
force reload map on new request

---
{{define_cvar("r_icon_highcontrast_postprocessing_weight")}}
if using high contrast postprocessing, use this weight (weight = 1.0 for characters)

---
{{define_cvar("spec_replay_outline")}}
Enable outline selecting victim in hltv replay: 0 - none; 1 - ouline YOU; 2 - outline YOU, with red ragdoll outline; 3 - normal spectator outlines

---
{{define_cvar("spec_glow_silent_factor")}}
Lurking player xray glow scaling.

---
{{define_cvar("spec_glow_spike_factor")}}
Noisy player xray glow scaling (pop when noise is made).  Make >1 to add a 'spike' to noise-making players

---
{{define_cvar("spec_glow_full_time")}}
Noisy players stay at full brightness for this long.

---
{{define_cvar("spec_glow_decay_time")}}
Time to decay glow from 1.0 to spec_glow_silent_factor after spec_glow_full_time.

---
{{define_cvar("spec_glow_spike_time")}}
Time for noisy player glow 'spike' to show that they made noise very recently.

---
{{define_cvar("spec_show_xray")}}
If set to 1, you can see player outlines and name IDs through walls - who you can see depends on your team and mode

---
{{define_cvar("cl_show_equipment_value")}}

---
{{define_cvar("cl_prefer_lefthanded")}}
Left handed preference

---
{{define_cvar("r_drawcsplayers")}}
Render CS players

---
{{define_cvar("cl_random_taser_bone_y")}}
The Y position used for the random taser force.

---
{{define_cvar("cl_random_taser_force_y")}}
The Y position used for the random taser force.

---
{{define_cvar("cl_random_taser_power")}}
Power used when applying the taser effect.

---
{{define_cvar("cl_ragdoll_workaround_threshold")}}
Mainly cosmetic, client-only effect: when client doesn't know the last position of another player that spawns a ragdoll, the ragdoll creation is simplified and ragdoll is created in the right place. If you increase this significantly, ragdoll positions on your client may be dramatically wrong, but it won't affect other clients

---
{{define_cvar("cl_ragdoll_physics_enable")}}
Enable/disable ragdoll physics.

---
{{define_cvar("cl_display_player_visibilty")}}

---
{{define_cvar("character_patches")}}

---
{{define_cvar("cl_player_proximity_debug")}}

---
{{define_cvar("cl_show_head_trajectory")}}

---
{{define_cvar("cl_show_camera_position")}}

---
{{define_cvar("sv_smoke_volume_blind_start")}}

---
{{define_cvar("cl_crosshair_sniper_width")}}
If >1 sniper scope cross lines gain extra width (1 for single-pixel hairline)

---
{{define_cvar("debug_entity_outline_highlight")}}

---
{{define_cvar("cl_player_lighting_origin_offset")}}

---
{{define_cvar("cl_inferno_bodyburn")}}

---
{{define_cvar("cl_display_flashbang_values")}}

---
{{define_cvar("cl_player_ragdolls_collide")}}

---
{{define_cvar("cl_borrow_music_from_player_slot")}}

---
{{define_cvar("cl_spec_show_bindings")}}
Toggle the visibility of the spectator bindings.

---
{{define_cvar("cl_teamid_overhead_maxdist")}}
max distance at which the overhead team id icons will show

---
{{define_cvar("cl_teamid_overhead_maxdist_spec")}}
max distance at which the overhead team id icons will show when a spectator

---
{{define_cvar("cl_show_clan_in_death_notice")}}
Is set, the clan name will show next to player names in the death notices.

---
{{define_cvar("cl_dm_buyrandomweapons")}}
Player will automatically receive a random weapon on spawn in deathmatch if this is set to 1 (otherwise, they will receive the last weapon)

---
{{define_cvar("cl_hud_color")}}
0 = team color, 1 =  white, 2 = bright white, 3 = light blue, 4 = blue, 5 = purple, 6 = red, 7 = orange, 8 = yellow, 9 = green, 10 = aqua, 11 = pink, 12 = teammate color.

---
{{define_cvar("cl_hud_radar_scale")}}

---
{{define_cvar("cl_use_entity_as_targetid")}}

---
{{define_cvar("cl_dangerzone_approaching_sound_radius")}}

---
{{define_cvar("cl_dangerzone_sound_volume")}}

---
{{define_cvar("cl_dangerzone_moving_sound_volume")}}

---
{{define_cvar("cl_weapon_pickup_lerp")}}

---
{{define_cvar("cl_firstperson_legs")}}

---
{{define_cvar("cl_smoke_player_particle_effect")}}

---
{{define_cvar("cl_weapon_clip_thinwalls")}}

---
{{define_cvar("cl_weapon_clip_thinwalls_debug")}}

---
{{define_cvar("cl_weapon_clip_thinwalls_lock")}}

---
{{define_cvar("cl_weapon_clip_thinwalls_pitchlimit_up")}}

---
{{define_cvar("cl_weapon_clip_thinwalls_pitchlimit_down")}}

---
{{define_cvar("cl_view_near_hud_player_eye_dist")}}

---
{{define_cvar("cl_view_near_other_player_eye_dist")}}

---
{{define_cvar("clDrawTargetIDTrace")}}
visualizing line trace for target ID

---
{{define_cvar("snd_report_c4_sounds")}}

---
{{define_cvar("viewmodel_presetpos")}}
1:"Desktop", 2:"Classic" 

---
{{define_cvar("crosshair")}}

---
{{define_cvar("lockMoveControllerRet")}}

---
{{define_cvar("hud_showtargetid")}}
Enables display of target names

---
{{define_cvar("cl_drawhud_force_teamid_overhead")}}
0: default; 1: draw teamid even if hud disabled; -1: force no teamid

---
{{define_cvar("cl_versus_intro")}}

---
{{define_cvar("cl_teamid_overhead_mode")}}
Always show team id over teammates. 0 = off, 1 = pips; 2 = +name, 3 = +equipment

---
{{define_cvar("cl_teamid_overhead_colors_show")}}
Show team overhead id in teammate color

---
{{define_cvar("cl_teamid_overhead_fade_near_crosshair")}}
The amount to fade teamid when near the crosshair. Range is 0.0-1.0. 0: off

---
{{define_cvar("cl_drawhud_force_deathnotices")}}
0: default; 1: draw deathnotices even if hud disabled; -1: force no deathnotices

---
{{define_cvar("cl_showloadout")}}
Toggles display of current loadout.

---
{{define_cvar("cl_draw_only_deathnotices")}}
For drawing only the crosshair and death notices (used for moviemaking)

---
{{define_cvar("cl_radar_square_with_scoreboard")}}
If set, the radar will toggle to square when the scoreboard is visible.

---
{{define_cvar("cl_radar_rotate")}}
1

---
{{define_cvar("cl_radar_scale")}}
Sets the radar scale. Valid values are 0.25 to 1.0.

---
{{define_cvar("cl_radar_scale_alternate")}}
Sets the alternate radar scale. Valid values are 0.25 to 1.0.

---
{{define_cvar("cl_radar_always_centered")}}
If set to 0, the radar is maximally used. Otherwise the player is always centered, even at map extents.

---
{{define_cvar("cl_radar_icon_scale_min")}}
Sets the minimum icon scale. Valid values are 0.4 to 1.25.

---
{{define_cvar("cl_drawhud_force_radar")}}
0: default; 1: draw radar even if hud disabled; -1: force no radar

---
{{define_cvar("cl_radar_fast_transforms")}}
Faster way of placing icons on the mini map.

---
{{define_cvar("default_fov")}}

---
{{define_cvar("player_teamplayedlast")}}

---
{{define_cvar("voice_vox")}}
Voice chat uses a vox-style always on

---
{{define_cvar("voice_vox_current_peak")}}
Current peak value (out of 64k) of the incoming voice stream

---
{{define_cvar("cl_autobuy")}}
The order in which autobuy will attempt to purchase items

---
{{define_cvar("cl_rebuy")}}
The order in which rebuy will attempt to repurchase items

---
{{define_cvar("snd_vol_per_game_mode")}}

---
{{define_cvar("snd_vol_arms_race")}}

---
{{define_cvar("snd_vol_deathmatch")}}

---
{{define_cvar("r_propsmaxdist")}}
Maximum visible distance

---
{{define_cvar("cl_showerror")}}
Show prediction errors, 2 for above plus detailed field deltas, 3 to filter out serverside known prediction errors, -entindex for specific entity.

---
{{define_cvar("cl_error_report_time")}}
Minimum time in seconds that must elapse before printing prediction error summary. 0 to disable.

---
{{define_cvar("cl_pdump")}}
Dump info about this entity to screen.

---
{{define_cvar("cl_pclass")}}
Dump entity by prediction classname.

---
{{define_cvar("cl_pred_optimize")}}
Optimize for not copying data if didn't receive a network update (1), and also for not repredicting if there were no errors (2).

---
{{define_cvar("cl_pred_print_every_cmd")}}
Print something every time we predict a command

---
{{define_cvar("cl_pred_always_latch")}}

---
{{define_cvar("cl_pred_parallel_postnetwork")}}

---
{{define_cvar("cl_true_sight_spectate")}}

---
{{define_cvar("cl_ragdoll_lru_debug")}}

---
{{define_cvar("cl_ragdoll_limit")}}
Maximum number of ragdolls to show (-1 disables limit)

---
{{define_cvar("snd_sound_areas_debug")}}

---
{{define_cvar("snd_sound_areas_debug_interval")}}

---
{{define_cvar("cl_snd_new_visualize")}}
Displays soundevent name played at it's 3d position

---
{{define_cvar("viewmodel_fov")}}
Viewmodel FOV

---
{{define_cvar("cl_leveloverview")}}

---
{{define_cvar("r_mapextents")}}
Set the max dimension for the map.  This determines the far clipping plane

---
{{define_cvar("gl_clear")}}

---
{{define_cvar("gl_clear_randomcolor")}}
Clear the back buffer to random colors every frame. Helps spot open seams in geometry.

---
{{define_cvar("gl_clear_gray")}}
Clear the back buffer to gray every frame.

---
{{define_cvar("r_nearz")}}
Override the near clipping plane. -1 means use the default.

---
{{define_cvar("r_farz")}}
Override the far clipping plane. -1 means to use the value in env_fog_controller.

---
{{define_cvar("cl_demoviewoverride")}}
Override view during demo playback

---
{{define_cvar("cl_demo_view_offset_left")}}
View offset during demo playback (+/- 1.25 is a good default for human average left/right eye offset)

---
{{define_cvar("cl_lock_camera")}}

---
{{define_cvar("_fov")}}
Automates fov command to server.

---
{{define_cvar("cl_demo_steadycam_enable")}}
Stabilize camera orientation/position during demo playback.  1 == remove roll, 2 == steadycam

---
{{define_cvar("cl_demo_steadycam_radius")}}
if camera moves this much from last anchor update anchor

---
{{define_cvar("cl_demo_steadycam_deflection")}}
if camera orientation changes this much update orientation

---
{{define_cvar("cl_demo_steadycam_blendframes")}}
blend over this many frames

---
{{define_cvar("fade_debug_splitscreen_slot")}}

---
{{define_cvar("shake_show")}}
Displays a list of the active screen shakes.

---
{{define_cvar("r_screen_size_expansion")}}

---
{{define_cvar("r_drawdevvisualizers")}}
Render dev visualizers

---
{{define_cvar("fog_start")}}

---
{{define_cvar("fog_end")}}

---
{{define_cvar("fog_startskybox")}}

---
{{define_cvar("fog_endskybox")}}

---
{{define_cvar("fog_maxdensityskybox")}}

---
{{define_cvar("fog_colorskybox")}}

---
{{define_cvar("fog_enableskybox")}}

---
{{define_cvar("fog_maxdensity")}}

---
{{define_cvar("fog_hdrcolorscaleskybox")}}

---
{{define_cvar("voice_modenable")}}
Enable/disable voice in this mod.

---
{{define_cvar("voice_clientdebug")}}

---
{{define_cvar("voice_all_icons")}}
Draw all players' voice icons

---
{{define_cvar("hud_fastswitch")}}

---
{{define_cvar("cc_linger_time")}}
Close caption linger time.

---
{{define_cvar("cc_delay_time")}}
Close caption delay before showing caption.

---
{{define_cvar("cc_captiontrace")}}
Show missing closecaptions (0 = no, 1 = devconsole, 2 = show in hud)

---
{{define_cvar("cc_log")}}
Log caption names and contents (0 = off, 1 = found captions, 2 = unfound captions, 3 = all captions)

---
{{define_cvar("cc_subtitles")}}
If set, don't show sound effect captions, just voice overs (i.e., won't help hearing impaired players).

---
{{define_cvar("english")}}
If set to 1, running the english language set of assets.

---
{{define_cvar("cc_vr_debug")}}
Debug visualization of VR closed caption placement

---
{{define_cvar("cc_vr_depth_test")}}
Have closed caption Panorama panel perform depth testing against the scene

---
{{define_cvar("cc_vr_forward_offset")}}
Subtitle offset distance (forward, in front of player)

---
{{define_cvar("cc_vr_vertical_offset")}}
Subtitle vertical offset distance (positive is up)

---
{{define_cvar("cc_vr_epsilon")}}
Epsilon to trigger movement of VR subtitle panel in world space

---
{{define_cvar("cc_vr_caption_catchup_interval")}}
Duration it takes for attached caption to ideal point

---
{{define_cvar("cc_vr_font_size")}}
0 = small, 1 = med (default), 2 = large

---
{{define_cvar("cc_vr_caption_speed")}}
0 = slow, 1 = medium (default), 2 = fast

---
{{define_cvar("cc_spectator_only")}}

---
{{define_cvar("cc_vr_width")}}
0 = narrow, 1 = med (default), 2 = wide

---
{{define_cvar("cc_lang")}}
Current close caption language (emtpy = use game UI language)

---
{{define_cvar("r_RainParticleDensity")}}
Density of Particle Rain 0-1

---
{{define_cvar("r_RainAllowInSplitScreen")}}
Allows rain in splitscreen

---
{{define_cvar("r_debug_precipitation")}}
Show precipitation volumes

---
{{define_cvar("r_flashlightfov")}}

---
{{define_cvar("r_flashlightoffsetright")}}

---
{{define_cvar("r_flashlightoffsetup")}}

---
{{define_cvar("r_flashlightoffsetforward")}}

---
{{define_cvar("r_flashlightnear")}}

---
{{define_cvar("r_flashlightfar")}}

---
{{define_cvar("r_flashlightconstant")}}

---
{{define_cvar("r_flashlightquadratic")}}

---
{{define_cvar("r_flashlightbrightness")}}

---
{{define_cvar("r_flashlightvisualizetrace")}}

---
{{define_cvar("r_flashlightambient")}}

---
{{define_cvar("r_flashlightshadowatten")}}

---
{{define_cvar("r_flashlightladderdist")}}

---
{{define_cvar("r_flashlightlinear")}}

---
{{define_cvar("r_muzzleflashlinear")}}

---
{{define_cvar("r_muzzleflashbrightness")}}

---
{{define_cvar("r_flashlightnearoffsetscale")}}

---
{{define_cvar("r_flashlighttracedistcutoff")}}

---
{{define_cvar("r_flashlightbacktraceoffset")}}

---
{{define_cvar("r_flashlighttracedistwatercutoff")}}

---
{{define_cvar("muzzle_flash_debug")}}

---
{{define_cvar("r_flashlightmuzzleflashfov")}}

---
{{define_cvar("cl_async_client_shatter")}}
spawn client glass shards asynchronously during demos or when remotely connected.

---
{{define_cvar("r_impacts_alt_orientation")}}

---
{{define_cvar("r_impacts_decal_grazing_incidence_cutoff")}}

---
{{define_cvar("r_impacts_decal_grazing_incidence_variance")}}

---
{{define_cvar("r_impact_ricochet_chance")}}

---
{{define_cvar("r_drawtracers")}}

---
{{define_cvar("r_drawtracers_firstperson")}}
Toggle visibility of first person weapon tracers

---
{{define_cvar("cl_show_splashes")}}

---
{{define_cvar("cl_frametime_summary_report_detailed")}}
When a perf report is dumped at the end of the session, should it be detailed?

---
{{define_cvar("glow_use_tolerance")}}

---
{{define_cvar("spec_autodirector")}}
Auto-director chooses best view modes while spectating

---
{{define_cvar("debug_hltv")}}
Print out hltv events

---
{{define_cvar("locator_topdown_style")}}
Topdown games set this to handle distance and offscreen location differently.

---
{{define_cvar("hidehud")}}
bitmask: 1=weapon selection, 2=flashlight, 4=all, 8=health, 16=player dead, 32=needssuit, 64=misc, 128=chat, 256=crosshair, 512=vehicle crosshair, 1024=in vehicle

---
{{define_cvar("joy_vehicle_turn_lowend")}}

---
{{define_cvar("joy_vehicle_turn_lowmap")}}

---
{{define_cvar("joy_sensitive_step0")}}

---
{{define_cvar("joy_sensitive_step1")}}

---
{{define_cvar("joy_sensitive_step2")}}

---
{{define_cvar("joy_lowend")}}

---
{{define_cvar("joy_lowmap")}}

---
{{define_cvar("joy_accelscale")}}

---
{{define_cvar("joy_accelmax")}}

---
{{define_cvar("joy_pegged")}}

---
{{define_cvar("joy_virtual_peg")}}

---
{{define_cvar("joy_accel_filter")}}

---
{{define_cvar("joy_response_look")}}

---
{{define_cvar("joy_response_move")}}

---
{{define_cvar("joy_response_move_vehicle")}}

---
{{define_cvar("joy_circle_correct_mode")}}

---
{{define_cvar("joy_circle_correct_mode_vehicle")}}

---
{{define_cvar("mouse_inverty")}}

---
{{define_cvar("joy_pitch_sensitivity")}}

---
{{define_cvar("joy_yaw_sensitivity")}}

---
{{define_cvar("joy_forward_sensitivity")}}

---
{{define_cvar("joy_side_sensitivity")}}

---
{{define_cvar("joy_autosprint")}}
Automatically sprint when moving with an analog joystick

---
{{define_cvar("sensitivity")}}
Mouse sensitivity.

---
{{define_cvar("m_yaw")}}
Mouse yaw factor.

---
{{define_cvar("m_pitch")}}
Mouse pitch factor.

---
{{define_cvar("joy_display_input")}}

---
{{define_cvar("dev_create_sensitivity_report")}}

---
{{define_cvar("r_drawropes")}}

---
{{define_cvar("r_ropetranslucent")}}

---
{{define_cvar("rope_wind_dist")}}
Don't use CPU applying small wind gusts to ropes when they're past this distance.

---
{{define_cvar("rope_averagelight")}}
Makes ropes use average of cubemap lighting instead of max intensity.

---
{{define_cvar("cl_sceneentity_debug")}}
Display all thinking scene entities and its data.

---
{{define_cvar("scene_vcdautosave")}}
Create a savegame before VCD playback

---
{{define_cvar("tv_listen_voice_indices")}}
Bitfield of playerslots to listen to voice messages from when connected to SourceTV, default is none

---
{{define_cvar("tv_listen_voice_indices_h")}}
High 32 bits of bitfield of playerslots to listen to voice messages from when connected to SourceTV, default is none

---
{{define_cvar("mic_listen_while_nonfocused")}}
Enables the ability for the mic to remain open if the window loses focus such as when a caster tabs out to adjust settings

---
{{define_cvar("soundscape_fadetime")}}
Time to crossfade sound effects between soundscapes

---
{{define_cvar("soundscape_message")}}

---
{{define_cvar("soundscape_radius_debug")}}
Prints current volume of radius sounds

---
{{define_cvar("freecamera_fog_start")}}
Fog start for Free Camera.

---
{{define_cvar("freecamera_fog_end")}}
Fog end for Free Camera.

---
{{define_cvar("freecamera_zfar")}}
Fog start for Free Camera.

---
{{define_cvar("freecamera_rotation_multiplier")}}
Tweak this parameter to adjust Free Camera mouse rotation.

---
{{define_cvar("freecamera_max_speed")}}
Tweak this parameter to adjust Free Camera movement max speed.

---
{{define_cvar("freecamera_accel")}}
Tweak this parameter to adjust Free Camera movement acceleration.

---
{{define_cvar("stats_highlight_interval")}}
Interval between hightlight screens in the transition stats panel

---
{{define_cvar("cl_change_callback_limit")}}
change callback msec warning limit

---
{{define_cvar("cl_ShowBoneSetupEnts")}}
Show which entities are having their bones setup each frame.

---
{{define_cvar("cpu_level")}}
CPU Level - Default: High

---
{{define_cvar("gpu_level")}}
GPU Level - Default: High

---
{{define_cvar("mem_level")}}
Memory Level - Default: High

---
{{define_cvar("gpu_mem_level")}}
Memory Level - Default: High

---
{{define_cvar("cl_dormant_spew")}}
Spew state on when client entities become dormant or active.

---
{{define_cvar("cl_showtextmsg")}}
Enable/disable text messages printing on the screen.

---
{{define_cvar("cl_chat_active")}}

---
{{define_cvar("cl_showfps")}}
Draw fps meter at top of screen (1 = fps, 2 = smooth fps, 3 = server MS, 4 = Show FPS and Log to file )

---
{{define_cvar("cl_showpos")}}
Draw current position at top of screen

---
{{define_cvar("cl_showmem")}}
Draw approximate memory use at top of screen

---
{{define_cvar("report_clientthinklist")}}
List all clientside entities thinking and time - will report and turn itself off.

---
{{define_cvar("vprof_scope_entity_clientthink")}}
Does nothing whatsoever.

---
{{define_cvar("cl_showusercmd")}}
Show user command encoding

---
{{define_cvar("cl_anglespeedkey")}}

---
{{define_cvar("cl_yawspeed")}}

---
{{define_cvar("cl_pitchspeed")}}

---
{{define_cvar("cl_pitchdown")}}

---
{{define_cvar("cl_pitchup")}}

---
{{define_cvar("joystick")}}
True if the joystick is enabled, false otherwise.

---
{{define_cvar("cl_boxmove")}}
run in a square, # represents how many usercommands to run before turning.

---
{{define_cvar("cl_boxmove_speed")}}
how fast to run (1 to use player max run speed).

---
{{define_cvar("cl_mouselook")}}
Set to 1 to use mouse for look, 0 for keyboard look. Cannot be set while connected to a server.

---
{{define_cvar("cl_debugviewangle")}}
Plots view angles yaw at various stages of the frame/tick in Tracy.

---
{{define_cvar("ss_mimic")}}
Split screen users mimic base player's CUserCmds

---
{{define_cvar("cam_snapto")}}

---
{{define_cvar("cam_ideallag")}}
Amount of lag used when matching offset to ideal angles in thirdperson view

---
{{define_cvar("cam_idealdelta")}}
Controls the speed when matching offset to ideal angles in thirdperson view

---
{{define_cvar("cam_idealyaw")}}

---
{{define_cvar("cam_idealpitch")}}

---
{{define_cvar("cam_idealdist")}}

---
{{define_cvar("cam_collision")}}
When in thirdperson and cam_collision is set to 1, an attempt is made to keep the camera from passing though walls.

---
{{define_cvar("cam_showangles")}}
When in thirdperson, print viewangles/idealangles/cameraoffsets to the console.

---
{{define_cvar("c_maxpitch")}}

---
{{define_cvar("c_minpitch")}}

---
{{define_cvar("c_maxyaw")}}

---
{{define_cvar("c_minyaw")}}

---
{{define_cvar("c_maxdistance")}}

---
{{define_cvar("c_mindistance")}}

---
{{define_cvar("c_orthowidth")}}

---
{{define_cvar("c_orthoheight")}}

---
{{define_cvar("c_thirdpersonshoulder")}}

---
{{define_cvar("c_thirdpersonshoulderoffset")}}

---
{{define_cvar("c_thirdpersonshoulderdist")}}

---
{{define_cvar("c_thirdpersonshoulderheight")}}

---
{{define_cvar("c_thirdpersonshoulderaimdist")}}

---
{{define_cvar("joy_name")}}

---
{{define_cvar("joy_advanced")}}

---
{{define_cvar("joy_advaxisx")}}

---
{{define_cvar("joy_advaxisy")}}

---
{{define_cvar("joy_advaxisz")}}

---
{{define_cvar("joy_advaxisr")}}

---
{{define_cvar("joy_advaxisu")}}

---
{{define_cvar("joy_advaxisv")}}

---
{{define_cvar("joy_sidesensitivity")}}

---
{{define_cvar("joy_pitchsensitivity")}}

---
{{define_cvar("joy_yawsensitivity")}}

---
{{define_cvar("joy_movement_stick")}}
Which stick controls movement (0 is left stick)

---
{{define_cvar("joy_xcontroller_cfg_loaded")}}
If 0, the 360controller.cfg file will be executed on startup & option changes.

---
{{define_cvar("cl_drawhud")}}
Enable the rendering of the hud

---
{{define_cvar("fov_desired")}}
Sets the base field-of-view.

---
{{define_cvar("cl_glow_item_far_r")}}

---
{{define_cvar("cl_glow_item_far_g")}}

---
{{define_cvar("cl_glow_item_far_b")}}

---
{{define_cvar("cl_glow_brightness")}}
Brightness of player halos

---
{{define_cvar("mat_colcorrection_editor")}}

---
{{define_cvar("compositematerial_showdebugwindow")}}
Source2/Composite Material Debug

---
{{define_cvar("r_decals_default_start_fade")}}

---
{{define_cvar("r_decals_default_fade_duration")}}

---
{{define_cvar("r_decals_overlap_threshold")}}

---
{{define_cvar("r_flashlightlockposition")}}

---
{{define_cvar("sparseshadowtree_unpack_direct_to_shadow_atlas")}}
unpack SST directly into shadow atlas cascade vs via staging texture PS copy (NOTE - rendersystem fix reqd for AMD + driver fix required for NV + VK only.

---
{{define_cvar("sparseshadowtree_cs_exclude_next_cascade_region")}}
Exclude the inner region of a cascade during CS unpack if there is a higher resolution cascade that will cover that area.

---
{{define_cvar("sparseshadowtree_cs_unpack_mode")}}
Unpack mode in cs, 0 - one leaf per thread (16 output pixels), 1 (default) - one leaf row per thread (4 output pixels), 2 - one pixel out per thread.

---
{{define_cvar("cl_interp_threadmodeticks")}}
Additional interpolation ticks to use when interpolating with threaded engine mode set.

---
{{define_cvar("report_cliententitysim")}}
List all clientside simulations and time - will report and turn itself off.

---
{{define_cvar("cl_extrapolate")}}
Enable/disable extrapolation if interpolation history runs out.

---
{{define_cvar("cl_interp_npcs")}}
Interpolate NPC positions starting this many seconds in past (or the value as per cl_interp_ratio, if greater)

---
{{define_cvar("cl_interp_all")}}
Disable interpolation list optimizations.

---
{{define_cvar("r_drawmodeldecals")}}

---
{{define_cvar("cl_simulate_dormant_entities")}}

---
{{define_cvar("cl_draw_simulating_entities")}}

---
{{define_cvar("cl_draw_simulating_entities_distance")}}

---
{{define_cvar("ent_test_interpolation")}}

---
{{define_cvar("cl_interp_animationvars")}}
Interpolate LATCH_ANIMATION_BIT vars if interpolation interval is greater than simulation interval

---
{{define_cvar("cl_interp_simulationvars")}}
Interpolate LATCH_SIMULATION_BIT vars if interpolation interval is greater than animation interval

---
{{define_cvar("iv_wrapped_parallel_latch")}}

---
{{define_cvar("iv_parallel_latch")}}

---
{{define_cvar("iv_parallel_restore")}}

---
{{define_cvar("cl_latch_report")}}
Enable to output stats about latching

---
{{define_cvar("cl_interpolate_report")}}
Enable to show interpolation profile timing


---
{{define_cvar("cl_interp_hermite")}}
Set to zero do disable hermite interpolation.

---
{{define_cvar("cl_extrapolate_amount")}}
Set how many seconds the client will extrapolate entities for.

---
{{define_cvar("phonemedelay")}}
Phoneme delay to account for sound system latency.

---
{{define_cvar("phonemefilter")}}
Time duration of box filter to pass over phonemes.

---
{{define_cvar("blink_duration")}}
How many seconds an eye blink will last.

---
{{define_cvar("cl_vsnd_morph_override_ease_enabled")}}
Controls whether the compiled in vsnd morph data ease in/out values are used or values set from the convars (cl_vsnd_morph_override_ease_in, cl_vsnd_morph_override_ease_out) are used

---
{{define_cvar("cl_vsnd_morph_override_ease_in")}}
If cl_enable_vsnd_morph_override_ease_enabled is true, ease into vsnd morph driven animation over the specified number of seconds.

---
{{define_cvar("cl_vsnd_morph_override_ease_out")}}
If cl_enable_vsnd_morph_override_ease_enabled is true, ease out of vsnd morph driven animation over the specified number of seconds.

---
{{define_cvar("cl_viewtarget_clamp")}}

---
{{define_cvar("cl_enable_eye_occlusion")}}

---
{{define_cvar("cl_eye_occlusion_debug")}}

---
{{define_cvar("enable_boneflex")}}

---
{{define_cvar("phonemesnap")}}
Lod at level at which visemes stops always considering two phonemes, regardless of duration.

---
{{define_cvar("cl_eye_target_override")}}

---
{{define_cvar("cl_eye_yaw_multiplier")}}

---
{{define_cvar("cl_eye_sin_wave")}}

---
{{define_cvar("cl_smooth")}}
Smooth view/eye origin after prediction errors

---
{{define_cvar("cl_smoothtime")}}
Smooth client's view after prediction error over this many seconds

---
{{define_cvar("cl_smooth_targetspeed")}}

---
{{define_cvar("zoom_sensitivity_ratio")}}
Additional mouse sensitivity scale factor applied when FOV is zoomed in.

---
{{define_cvar("ragdoll_impact_strength")}}

---
{{define_cvar("g_debug_ragdoll_visualize")}}

---
{{define_cvar("g_ragdoll_fadespeed")}}

---
{{define_cvar("g_ragdoll_lvfadespeed")}}

---
{{define_cvar("mat_colcorrection_disableentities")}}
Disable map color-correction entities

---
{{define_cvar("mat_colcorrection_forceentitiesclientside")}}
Forces color correction entities to be updated on the client

---
{{define_cvar("cl_retire_low_priority_lights")}}
Low priority dlights are replaced by high priority ones

---
{{define_cvar("cl_globallight_freeze")}}

---
{{define_cvar("cl_globallight_expansion")}}

---
{{define_cvar("cl_globallight_debug")}}

---
{{define_cvar("cl_globallight_shadow_mode")}}

---
{{define_cvar("mat_slopescaledepthbias_shadowmap")}}

---
{{define_cvar("mat_depthbias_shadowmap")}}

---
{{define_cvar("cl_globallight_orig_calc_frustum")}}

---
{{define_cvar("cl_globallight_world_bottom_height")}}

---
{{define_cvar("cl_globallight_world_top_height")}}

---
{{define_cvar("cl_globallight_use_alt_focus_region")}}

---
{{define_cvar("cl_globallight_slope_scale_depth_bias")}}

---
{{define_cvar("cl_globallight_depth_bias")}}

---
{{define_cvar("cl_globallight_use_shaadow_near_offset")}}

---
{{define_cvar("cl_cameraoverride_fade_in_amount")}}

---
{{define_cvar("cl_cameraoverride_shadow_depth_bias")}}

---
{{define_cvar("cl_cameraoverride_shadow_end")}}

---
{{define_cvar("cl_globallight_use_optimized_calc_frustum")}}

---
{{define_cvar("fish_debug")}}
Show debug info for fish

---
{{define_cvar("r_monitor_3dskybox")}}

---
{{define_cvar("gameinstructor_verbose")}}
Set to 1 for standard debugging or 2 (in combo with gameinstructor_verbose_lesson) to show update actions.

---
{{define_cvar("gameinstructor_verbose_lesson")}}
Display more verbose information for lessons have this name.

---
{{define_cvar("gameinstructor_find_errors")}}
Set to 1 and the game instructor will run EVERY scripted command to uncover errors.

---
{{define_cvar("gameinstructor_enable")}}
Display in game lessons that teach new players.

---
{{define_cvar("gameinstructor_start_sound_cooldown")}}
Number of seconds forced between similar lesson start sounds.

---
{{define_cvar("sv_gameinstructor_enable")}}
Force all clients to enable their game instructors.

---
{{define_cvar("cl_voiceenabled")}}

---
{{define_cvar("cl_debug_force_push_to_talk")}}

---
{{define_cvar("commentary_node_use_viewfacing")}}

---
{{define_cvar("rope_shake")}}

---
{{define_cvar("rope_subdiv")}}
Rope subdivision amount

---
{{define_cvar("rope_collide")}}
Collide rope with the world

---
{{define_cvar("rope_smooth_enlarge")}}
How much to enlarge ropes in screen space for antialiasing effect

---
{{define_cvar("rope_smooth_minwidth")}}
When using smoothing, this is the min screenspace width it lets a rope shrink to

---
{{define_cvar("rope_smooth_minalpha")}}
Alpha for rope antialiasing effect

---
{{define_cvar("rope_smooth_maxalphawidth")}}

---
{{define_cvar("rope_smooth_maxalpha")}}
Alpha for rope antialiasing effect

---
{{define_cvar("cl_ent_joint_axis_size")}}

---
{{define_cvar("cl_ent_joint_names")}}

---
{{define_cvar("cl_ent_joint_filter_substring")}}

---
{{define_cvar("cl_ent_joint_use_bind_pose")}}

---
{{define_cvar("cl_ent_joint_only_ik_joints")}}

---
{{define_cvar("cl_ent_skeleton_only_ik_joints")}}

---
{{define_cvar("cl_screenmessage_notifytime")}}
How long to display screen message text

---
{{define_cvar("cl_ent_showonlyattachment")}}

---
{{define_cvar("game_particle_manager_requeue_messages")}}

---
{{define_cvar("cl_hold_game_events_until_server_tick")}}
Holds game events until client has received the tick the event was fired on.

---
{{define_cvar("cl_hold_game_events_force_delay_ticks")}}
Debugging convar to force late dispatch of game events.

---
{{define_cvar("cl_net_showevents")}}
Dump game events to console (1=client only, 2=all).

---
{{define_cvar("cl_net_showeventlisteners")}}
Show listening addition/removals

---
{{define_cvar("cl_display_game_events")}}

---
{{define_cvar("ent_revert_dormancy_change")}}

---
{{define_cvar("r_draw3dskybox")}}

---
{{define_cvar("option_duck_method")}}
Input toggle control

---
{{define_cvar("spec_chasedistance")}}
Chase cam's ideal distance from target

---
{{define_cvar("spec_chasedistancespeed")}}
Chase cam's ideal distance from target

---
{{define_cvar("spec_centerchasecam")}}
Looks at the target player's center, instead of his eye position, in chase came mode

---
{{define_cvar("spec_track")}}
Tracks an entity in spec mode

---
{{define_cvar("bot_mimic_spec_buttons")}}
+attack, +jump etc are used for spectator control instead of being passed on to spectated bot

---
{{define_cvar("cl_skeleton_instance_smear_boneflags")}}
Smear boneflags across the model.  Costs computation, but tests to make sure your bone flags are consistent.

---
{{define_cvar("cl_phys_networked_start_sleep")}}

---
{{define_cvar("phys_expensive_shape_threshold")}}

---
{{define_cvar("cl_bone_cache_optimization")}}

---
{{define_cvar("cloth_iv_dump")}}

---
{{define_cvar("r_enable_rigid_animation")}}

---
{{define_cvar("cloth_iv_store_back")}}

---
{{define_cvar("cl_ent_showonlyhitbox")}}

---
{{define_cvar("sparseshadowtree_parallel_generation")}}
Split SST tile generation into threadjobs (0 - disabled, 1 - wait on readpixels for job batch, 2 - async readpixels).

---
{{define_cvar("sparseshadowtree_renderdoc_capture_generation")}}
Capture dual shadow maps during sparseshadowtree generation.

---
{{define_cvar("sparseshadowtree_debug_tile_range_xmin")}}
SST Tile range for renderdoc/debug capturing.

---
{{define_cvar("sparseshadowtree_debug_tile_range_xmax")}}
SST Tile range for renderdoc/debug capturing.

---
{{define_cvar("sparseshadowtree_debug_tile_range_ymin")}}
SST Tile range for renderdoc/debug capturing.

---
{{define_cvar("sparseshadowtree_debug_tile_range_ymax")}}
SST Tile range for renderdoc/debug capturing.

---
{{define_cvar("sparseshadowtree_leaf_precision")}}
precision for depth compression at SST leaf nodes.

---
{{define_cvar("sparseshadowtree_plane_max_error")}}
max error (distance away in depth) candidate plane is allowed before rejecting.

---
{{define_cvar("sparseshadowtree_plane_incr_per_step")}}
depth to increment candidate plane values per iteration to satisfy selection.

---
{{define_cvar("sparseshadowtree_plane_num_iter")}}
number of steps to push candidate plane behind depths.

---
{{define_cvar("sparseshadowtree_leaf_compress_scaleoffset")}}
Compress leaf node depths using scale & offset.

---
{{define_cvar("sparseshadowtree_render_cables")}}
Render cables into SST.

---
{{define_cvar("sparseshadowtree_leaf_precision_viewmodel")}}
(viewmodel) precision for depth compression at SST leaf nodes.

---
{{define_cvar("sparseshadowtree_plane_incr_per_step_viewmodel")}}
(viewmodel) depth to increment candidate plane values per iteration to satisfy selection.

---
{{define_cvar("sparseshadowtree_plane_max_error_viewmodel")}}
(viewmodel) max error (distance away in depth) candidate plane is allowed before rejecting.

---
{{define_cvar("sparseshadowtree_viewmodel_uses_cascade0")}}
Re-use cascade 0 SST for viewmodel to save on the significant extra memory. Flipping this invalidates generated SSTs if viewmodel SST not already generated.

---
{{define_cvar("sparseshadowtree_disable_for_viewmodel")}}
Disable SST generation and runtime for viewmodel (use original CSM rendering).

---
{{define_cvar("sparseshadowtree_uv_frac_offset_x")}}
uv x offset during copy to cascade.

---
{{define_cvar("sparseshadowtree_uv_frac_offset_y")}}
uv y offset during copy to cascade.

---
{{define_cvar("sparseshadowtree_enable_rendering")}}
Enable use of SST at runtime (static geo rendered into cascades via SST).

---
{{define_cvar("sparseshadowtree_copy_to_shadow_atlas_ps")}}
Copy layer from CS output to shadow atlas uses PS copy (vs CopyTexture).

---
{{define_cvar("option_speed_method")}}
Input toggle control

---
{{define_cvar("cl_pred_checkstuck")}}
Perform the additional 'stuck' traces on the client side during prediction.

---
{{define_cvar("cl_spec_use_tournament_content_standards")}}

---
{{define_cvar("cl_player_ping_mute")}}
If 1, player pinging will make a sound, if 0, pings will be silent

---
{{define_cvar("cl_tracer_frequency_override")}}
Override tracer frequency (-1 to disable)

---
{{define_cvar("cl_weapon_debug_print_accuracy")}}

---
{{define_cvar("cl_ragdoll_reload")}}

---
{{define_cvar("cl_ragdoll_default_scale")}}

---
{{define_cvar("cl_disable_ragdolls")}}

---
{{define_cvar("animated_material_attributes")}}

---
{{define_cvar("cl_sequence_debug")}}

---
{{define_cvar("cl_sequence_debug2")}}

---
{{define_cvar("cl_sequence_model_substring")}}

---
{{define_cvar("r_aoproxy_show")}}

---
{{define_cvar("weapon_all_stattrak")}}

---
{{define_cvar("weapon_all_nametag")}}

---
{{define_cvar("cl_debounce_zoom")}}
Whether or not to disable holding secondary fire to cycle zoom levels

---
{{define_cvar("cl_sniper_auto_rezoom")}}
Auto-rezoom snipers after a shot

---
{{define_cvar("econ_debug_loadout_ui")}}
Show debug data when players change their loadout.

---
{{define_cvar("spec_lock_to_accountid")}}
As an observer, lock the spectator target to the given accountid.

---
{{define_cvar("spec_usenumberkeys_nobinds")}}
If set to 1, map voting and spectator view use the raw number keys instead of the weapon binds (slot1, slot2, etc).

---
{{define_cvar("cl_obs_interp_enable")}}
Enables interpolation between observer targets

---
{{define_cvar("cl_obs_interp_pos_rate")}}

---
{{define_cvar("cl_obs_interp_pos_halflife")}}

---
{{define_cvar("cl_obs_interp_snap_dist")}}

---
{{define_cvar("cl_obs_interp_settle_dist")}}

---
{{define_cvar("cl_obs_interp_dist_to_turn_to_face")}}
Changing to a target further than this will cause the camera to face the direction of travel

---
{{define_cvar("cl_obs_interp_angle_progress_headstart")}}

---
{{define_cvar("cl_obs_interp_turn_to_face_start_frac")}}

---
{{define_cvar("cl_obs_interp_turn_to_face_end_frac")}}

---
{{define_cvar("cl_obs_interp_obstruction_behavior")}}

---
{{define_cvar("fov_cs_debug")}}
Sets the view fov if cheats are on.

---
{{define_cvar("fov_cs_near_z")}}

---
{{define_cvar("fov_cs_ultrawide_near_z")}}

---
{{define_cvar("fov_cs_super_ultrawide_near_z")}}

---
{{define_cvar("cl_sniper_delay_unscope")}}

---
{{define_cvar("death_chase_distance")}}

---
{{define_cvar("cl_sanitize_player_names")}}
Replace names of other players with something non-offensive.

---
{{define_cvar("cl_sanitize_muted_players")}}
Hide names and avatars of muted players.

---
{{define_cvar("cl_show_playernames_max_chars_console")}}
Shows all player names (including bots) as 16 W's.

---
{{define_cvar("cl_teammate_colors_show")}}
In competitive, 1 = show teammates as separate colors in the radar, scoreboard, etc., 2 = show colors and letters

---
{{define_cvar("cl_show_enemy_avatar_colors")}}

---
{{define_cvar("cl_predict_weapon_drop")}}

---
{{define_cvar("cs_minimap_create_output_size")}}
Size of minimap texture generated with cs_minimap_create (512 default)

---
{{define_cvar("cs_minimap_rendering_msaa_mode")}}
MSAA mode used for minimap rendering 0-none, 1-2xMSAA, 2-4xMSAA, 3-6X, 4-8X, etc

---
{{define_cvar("cs_minimap_renderdoc_capture_enabled")}}

---
{{define_cvar("composite_material_cache_count_max")}}

---
{{define_cvar("composite_material_use_gpu")}}

---
{{define_cvar("composite_material_use_bc7")}}

---
{{define_cvar("composite_material_use_gpu_perceptual_error_metric")}}

---
{{define_cvar("composite_material_use_gpu_endpoint_optimization")}}

---
{{define_cvar("composite_material_dump_images")}}

---
{{define_cvar("composite_material_save_to_disk")}}

---
{{define_cvar("viewmodel_offset_x")}}
viewmodel_offset_x

---
{{define_cvar("viewmodel_offset_y")}}
viewmodel_offset_y

---
{{define_cvar("viewmodel_offset_z")}}
viewmodel_offset_z

---
{{define_cvar("cl_gunlowerangle")}}

---
{{define_cvar("cl_gunlowerspeed")}}

---
{{define_cvar("cl_mantle_gunloweramt")}}

---
{{define_cvar("cl_mantle_gunlowerspeed")}}

---
{{define_cvar("cl_death_anim_viewmodel_drop_rate")}}

---
{{define_cvar("cl_death_anim_viewmodel_pitch_rate")}}

---
{{define_cvar("cl_viewmodel_reprediction_override")}}
Disable reprediction for CS2 viewmodels. 0 = Leave it as-is, 1 = allow prediction errors, 2 = ignore prediction errors, 3 = ignore prediction errors and copy corrections forward

---
{{define_cvar("cl_viewmodel_reprediction_override_restore_during_skips")}}
When skipping prediction for the viewmodel. Should we restore the predicted data for that predicted command?

---
{{define_cvar("cl_viewmodel_reprediction_override_early_prediction_handling")}}
Choose how to handle early predictions when disabling reprediction. 0 = allow reprediction of early commands, 1 = skip early prediction and wait for full predictions, 2 = early predictions are considered final predictions

---
{{define_cvar("cl_smoke_volumeprop")}}

---
{{define_cvar("cl_smoke_volume_growth")}}

---
{{define_cvar("cl_grenadecrosshair_fire")}}
Is the grenade crosshair enabled

---
{{define_cvar("cl_grenadecrosshair_smoke")}}
Is the grenade crosshair enabled

---
{{define_cvar("cl_grenadecrosshair_flash")}}
Is the grenade crosshair enabled

---
{{define_cvar("cl_grenadecrosshair_explosive")}}
Is the grenade crosshair enabled

---
{{define_cvar("cl_grenadecrosshair_decoy")}}
Is the grenade crosshair enabled

---
{{define_cvar("cl_grenadecrosshairdelay_fire")}}
How long should the pin be pulled for before showing the grenade crosshair

---
{{define_cvar("cl_grenadecrosshairdelay_smoke")}}
How long should the pin be pulled for before showing the grenade crosshair

---
{{define_cvar("cl_grenadecrosshairdelay_flash")}}
How long should the pin be pulled for before showing the grenade crosshair

---
{{define_cvar("cl_grenadecrosshairdelay_explosive")}}
How long should the pin be pulled for before showing the grenade crosshair

---
{{define_cvar("cl_grenadecrosshairdelay_decoy")}}
How long should the pin be pulled for before showing the grenade crosshair

---
{{define_cvar("cl_predict_bomb_defusal")}}

---
{{define_cvar("cl_viewmodelsclonedasworld")}}

---
{{define_cvar("cl_weapon_debug_show_accuracy")}}
Draws a circle representing the effective range with every shot.

---
{{define_cvar("cl_weapon_debug_show_accuracy_duration")}}

---
{{define_cvar("cl_wallbang_heavy_threshold")}}
The Threshold where to switch from Light to Heavy Wallbang tracer

---
{{define_cvar("weapon_skins")}}

---
{{define_cvar("weapon_skins_on_default")}}

---
{{define_cvar("weapon_random_stickers")}}

---
{{define_cvar("cl_use_opens_buy_menu")}}
Pressing the +use key will open the buy menu if in a buy zone (just as if you pressed the 'buy' key).

---
{{define_cvar("cl_silencer_mode")}}
0: cannot detach; 1: press secondary fire to detach

---
{{define_cvar("cl_autohelp")}}
Auto-help

---
{{define_cvar("cl_join_advertise")}}
Advertise joinable game in progress to Steam friends, otherwise need a Steam invite (2: all servers, 1: official servers, 0: none)

---
{{define_cvar("spec_autodirector_cameraman")}}

---
{{define_cvar("cl_script_break_in_native_debugger_on_error")}}

---
{{define_cvar("cl_script_attach_debugger_at_startup")}}

---
{{define_cvar("spec_replay_review_sound")}}
When set to non-0, a sound effect is played during Killer Replay

---
{{define_cvar("spec_replay_rate_slowdown")}}
The part of Killer Replay right before death is played at this rate

---
{{define_cvar("spec_replay_rate_slowdown_length")}}
The part of Killer Replay right before death is played at this rate

---
{{define_cvar("spec_replay_fadein")}}
Amount of time in seconds it takes to visually fade into replay, or into real-time after replay

---
{{define_cvar("spec_replay_fadeout")}}
Amount of time in seconds it takes to visually fade out of replay, or out of real-time before replay

---
{{define_cvar("spec_replay_sound_fadein")}}
Amount of time in seconds it takes to fade in the audio before or after replay

---
{{define_cvar("spec_replay_sound_fadeout")}}
Amount of time in seconds it takes to fade out the audio before or after replay

---
{{define_cvar("spec_replay_cache_ragdolls")}}
when set to 0, ragdolls will settle dynamically before and after Killer Replay

---
{{define_cvar("spec_replay_others_experimental")}}
Replay the last death of the round, if possible. Disabled on official servers by default. Experimental.

---
{{define_cvar("spec_replay_autostart")}}
Auto-start Killer Replay when available

---
{{define_cvar("spec_replay_victim_pov")}}
Killer Replay - replay from victim's point of view (1); the default is killer's (0). Experimental.

---
{{define_cvar("r_replay_post_effect")}}

---
{{define_cvar("leaderboards_cache_duration")}}

---
{{define_cvar("cl_predictioncopy_runs")}}

---
{{define_cvar("pwatchent")}}
Entity to watch for prediction system changes.

---
{{define_cvar("pwatchvar")}}
Entity variable to watch in prediction system for changes.

---
{{define_cvar("cl_pred_build_verbose")}}
Verbose spew when building prediction optimized data runs.

---
{{define_cvar("cl_panel_freeze_time_after_press")}}
time to freeze mouse/pointer motion after a mouse button press

---
{{define_cvar("r_dashboard_render_quality")}}

---
{{define_cvar("panorama_focus_world_panels")}}
when set request key focus when a world panel is enabled

---
{{define_cvar("panorama_async_compute_mipgen")}}
use asynchronous compute for mipmap generation.

---
{{define_cvar("panorama_worldpanel_update_culling")}}

---
{{define_cvar("panorama_worldpanel_update_cull_distance")}}

---
{{define_cvar("panorama_worldpanel_update_cull_size_threshold")}}

---
{{define_cvar("ui_hud_dist")}}
distance from the player to the hud

---
{{define_cvar("cl_ent_pivot_size")}}

---
{{define_cvar("cl_debug_overlay_fullposition")}}

---
{{define_cvar("cl_ent_text_no_name_really_i_mean_it")}}

---
{{define_cvar("cl_ent_show_contexts")}}
Show entity contexts in ent_text display

---
{{define_cvar("cl_ent_text_flags_active")}}

---
{{define_cvar("buildcubemaps_renderdoc_capture")}}
Capture a specific cubemap with RenderDoc during buildcubemaps.

---
{{define_cvar("show_visibility_boxes")}}
Enable or Disable debug display of visibility boxes

---
{{define_cvar("snd_log_empty_event_entities")}}
Logs the sound event entities that have empty names.

---
{{define_cvar("demo_playback_override_settings")}}

---
{{define_cvar("cl_skip_update_animations")}}
Enable to skip game animations

---
{{define_cvar("cl_animgraph_history_force_temporal_consistency")}}

---
{{define_cvar("cl_massreport")}}

---
{{define_cvar("cl_lightquery_debug")}}

---
{{define_cvar("cl_phys_enabled")}}
Enable all physics simulation

---
{{define_cvar("cl_phys_stop_at_collision")}}

---
{{define_cvar("cl_phys_sleep_enable")}}
Enable sleeping for dynamic physics bodies.

---
{{define_cvar("cl_phys_animated_hierarchy")}}

---
{{define_cvar("cl_phys_block_fraction")}}

---
{{define_cvar("cl_phys_block_dist")}}

---
{{define_cvar("cloth_sim_on_tick")}}

---
{{define_cvar("cloth_debug_draw")}}

---
{{define_cvar("cloth_update")}}

---
{{define_cvar("pred_cloth_substeps")}}

---
{{define_cvar("keychain_reactivity")}}

---
{{define_cvar("keychain_wmul")}}

---
{{define_cvar("pred_cloth_vmax")}}

---
{{define_cvar("pred_cloth_vw")}}

---
{{define_cvar("dev_create_smooth_motion_report")}}

---
{{define_cvar("cl_phys_timescale")}}
Scale time for physics

---
{{define_cvar("presettle_cloth_iterations")}}

---
{{define_cvar("pred_cloth_rot_multiplier")}}

---
{{define_cvar("pred_cloth_rot_low")}}

---
{{define_cvar("pred_cloth_rot_high")}}

---
{{define_cvar("pred_cloth_pos_strength")}}

---
{{define_cvar("pred_cloth_pos_multiplier")}}

---
{{define_cvar("pred_cloth_pos_max")}}

---
{{define_cvar("pred_cloth_smooth_motion")}}

---
{{define_cvar("keychain_animation_reactivity")}}

---
{{define_cvar("cl_phys_visualize_awake")}}

---
{{define_cvar("phys_batch_ray_test")}}

---
{{define_cvar("cl_phys_debug_callback_entities")}}
Print all entities that get touch callbacks. Each entity is printed only once.

---
{{define_cvar("cl_hitbox_debug")}}

---
{{define_cvar("r_strip_invisible_during_sceneobject_update")}}

---
{{define_cvar("r_threaded_scene_object_update")}}

---
{{define_cvar("r_freeze_sceneobjects")}}

---
{{define_cvar("r_late_particle_job_sync")}}

---
{{define_cvar("r_update_particles_on_render_only_frames")}}

---
{{define_cvar("mm_player_search_requests_limit")}}
How many friend requests are displayed.

---
{{define_cvar("mm_player_search_update_interval")}}
Interval between players searches.

---
{{define_cvar("mm_player_search_lan_ping_interval")}}
Interval between LAN discovery pings.

---
{{define_cvar("mm_player_search_lan_ping_duration")}}
Duration of LAN discovery ping phase.

---
{{define_cvar("mm_events_listeners_validation")}}

---
{{define_cvar("net_allow_multicast")}}

---
{{define_cvar("cl_names_debug")}}

---
{{define_cvar("mm_player_search_count")}}

---
{{define_cvar("mm_debug_friend_rp")}}

---
{{define_cvar("mm_use_p2p_for_listen_server")}}

---
{{define_cvar("mm_ignored_sessions_forget_time")}}

---
{{define_cvar("mm_ignored_sessions_forget_pass")}}

---
{{define_cvar("mm_server_search_update_interval")}}
Interval between servers updates.

---
{{define_cvar("mm_server_search_inet_ping_interval")}}
How long to wait between pinging internet server details.

---
{{define_cvar("mm_server_search_inet_ping_timeout")}}
How long to wait for internet server details.

---
{{define_cvar("mm_server_search_inet_ping_window")}}
How many servers can be pinged for server details in a batch.

---
{{define_cvar("mm_server_search_inet_ping_refresh")}}
How often to refresh a listed server.

---
{{define_cvar("mm_server_search_server_lifetime")}}
How long until a server is no longer returned by the master till we remove it.

---
{{define_cvar("mm_server_search_lan_ping_interval")}}
Interval between LAN discovery pings.

---
{{define_cvar("mm_server_search_lan_ping_duration")}}
Duration of LAN discovery ping phase.

---
{{define_cvar("mm_server_search_lan_ports")}}
Ports to scan during LAN games discovery. Also used to discover and correctly connect to dedicated LAN servers behind NATs.

---
{{define_cvar("mm_datacenter_update_interval")}}
Interval between datacenter stats updates.

---
{{define_cvar("mm_datacenter_retry_interval")}}
Interval between datacenter stats retries.

---
{{define_cvar("mm_datacenter_query_delay")}}
Delay after datacenter update is enabled before data is actually queried.

---
{{define_cvar("mm_session_sys_delay_create")}}

---
{{define_cvar("mm_session_sys_delay_create_host")}}

---
{{define_cvar("mm_session_sys_connect_timeout")}}

---
{{define_cvar("mm_session_team_res_timeout")}}

---
{{define_cvar("mm_session_voice_loading")}}

---
{{define_cvar("mm_session_sys_ranking_timeout")}}

---
{{define_cvar("mm_session_sys_slots_guaranteed")}}

---
{{define_cvar("mm_session_sys_pkey")}}

---
{{define_cvar("mm_session_sys_kick_ban_duration")}}

---
{{define_cvar("voice_test_log_send")}}

---
{{define_cvar("mm_dlcs_mask_fake")}}

---
{{define_cvar("mm_dlcs_mask_extras")}}

---
{{define_cvar("mm_tu_string")}}

---
{{define_cvar("mm_dedicated_allow")}}
1 = allow searches for dedicated servers

---
{{define_cvar("mm_dedicated_fake")}}
1 = pretend like search is going, but abort after some time

---
{{define_cvar("mm_dedicated_force_servers")}}
Comma delimited list of ip:port of servers used to search for dedicated servers instead of searching for public servers.
Use syntax `publicip1:port|privateip1:port,publicip2:port|privateip2:port` if your server is behind NAT.
If the server is behind NAT, you can specify `0.0.0.0|privateip:port` and if server port is in the list of `mm_server_search_lan_ports` its public address should be automatically detected.

---
{{define_cvar("mm_dedicated_ip")}}
IP address of dedicated servers to consider available

---
{{define_cvar("mm_dedicated_timeout_request")}}

---
{{define_cvar("mm_dedicated_search_maxping")}}
Longest preferred ping to dedicated servers for games

---
{{define_cvar("mm_dedicated_search_maxresults")}}

---
{{define_cvar("mm_teamsearch_errortime")}}
Time team search is in error state until it self-cancels

---
{{define_cvar("mm_teamsearch_nostart")}}
Team search will fake cancel before searching for server

---
{{define_cvar("sv_search_team_key")}}
When initiating team search, set this key to match with known opponents team

---
{{define_cvar("mm_session_search_num_results")}}

---
{{define_cvar("mm_session_search_qos_timeout")}}

---
{{define_cvar("mm_match_search_update_interval")}}
Interval between matchsearcher updates.

---
{{define_cvar("mm_sv_load_test")}}

---
{{define_cvar("mm_title_debug_version")}}
This matchmaking version will override .res file version for isolating matchmaking

---
{{define_cvar("mm_csgo_community_search_players_min")}}
When performing CSGO community matchmaking look for servers with at least so many human players

---
{{define_cvar("custom_bot_difficulty")}}
Bot difficulty for offline play.

---
{{define_cvar("diffcheck_playerslot")}}

---
{{define_cvar("diffcheck_spew")}}
Actually show diffcheck results.

---
{{define_cvar("diffcheck_spew_diff_only")}}
Show diff only.

---
{{define_cvar("diffcheck_spew_diff_filter")}}
Show diff with matching filter substring only.

---
{{define_cvar("diffcheck")}}
Activate diffcheck system.

---
{{define_cvar("nav_gen_true")}}
Always true

---
{{define_cvar("nav_gen_false")}}
Always false

---
{{define_cvar("nav_gen_match_ground")}}

---
{{define_cvar("nav_gen_opt_to_quads")}}

---
{{define_cvar("nav_gen_opt_to_quads_angle_limit")}}

---
{{define_cvar("nav_gen_opt_to_quads_planar_deviation_limit")}}

---
{{define_cvar("nav_gen_opt_to_quads_num_steps")}}

---
{{define_cvar("nav_gen_opt_to_quads_se_limit_start")}}

---
{{define_cvar("nav_gen_opt_to_quads_se_limit_end")}}

---
{{define_cvar("nav_gen_opt_to_quads_weld_limit_start")}}

---
{{define_cvar("nav_gen_opt_to_quads_weld_limit_end")}}

---
{{define_cvar("nav_gen_degen_limit")}}

---
{{define_cvar("nav_gen_markup_split_tol_base")}}

---
{{define_cvar("nav_gen_markup_split_tol_nonentity")}}

---
{{define_cvar("nav_gen_markup_split_tol_nonav")}}

---
{{define_cvar("nav_gen_markup_split_expand")}}

---
{{define_cvar("nav_gen_max_edge_len_do_clip")}}

---
{{define_cvar("nav_gen_max_edge_len")}}

---
{{define_cvar("nav_gen_max_edge_len_split_tol")}}

---
{{define_cvar("nav_gen_max_bottleneck_width_do_clip")}}

---
{{define_cvar("nav_gen_max_bottleneck_width")}}

---
{{define_cvar("nav_gen_island_removal")}}

---
{{define_cvar("nav_gen_island_removal_all_hulls")}}

---
{{define_cvar("nav_gen_connect_dist_a")}}

---
{{define_cvar("nav_gen_connect_dist_b")}}

---
{{define_cvar("nav_gen_connect_dist_z_mult")}}

---
{{define_cvar("nav_gen_connect_angle")}}

---
{{define_cvar("nav_gen_connect_angle_ignore_z")}}

---
{{define_cvar("nav_gen_connect_overlap")}}

---
{{define_cvar("nav_gen_connect_allow_multiple")}}

---
{{define_cvar("nav_gen_add_jumps")}}

---
{{define_cvar("nav_gen_vertical_limit")}}

---
{{define_cvar("nav_gen_remove_vertical_polys")}}

---
{{define_cvar("nav_gen_split_boundary_polys")}}

---
{{define_cvar("nav_gen_split_multi_connection_polys")}}

---
{{define_cvar("nav_gen_split_multi_connection_polys_tol")}}

---
{{define_cvar("nav_gen_clip_polys_to_clearance")}}

---
{{define_cvar("nav_gen_clip_polys_to_clearance_debug")}}

---
{{define_cvar("nav_gen_join_nonzup")}}

---
{{define_cvar("nav_gen_agent_radius_buffer")}}
Buffer to add to agent radius before passing to nav gen

---
{{define_cvar("nav_gen_jump_connection_min_overlap_ratio")}}
Minimum edge overlap required for jump connection consideration as a percentage of agent radius

---
{{define_cvar("recast_partitioning")}}
0 = watershed, 1 = monotone, 2 = layers

---
{{define_cvar("recast_mark_overhang")}}
Enable/disable overhang detection

---
{{define_cvar("nav_gen_oriented_angle_tol")}}
Max abrupt orientation difference an NPC can tolerate when moving through the mesh (degrees).

---
{{define_cvar("nav_gen_oriented_max_region_range")}}
Max orientation range allowed within a region before it gets further split.

---
{{define_cvar("nav_max_vis_delta_list_length")}}

---
{{define_cvar("nav_corner_adjust_adjacent")}}
radius used to raise/lower corners in nearby areas when raising/lowering corners.

---
{{define_cvar("nav_show_potentially_visible")}}
Show areas that are potentially visible from the current nav area

---
{{define_cvar("nav_validate")}}
Level of validation for nav system.  Higher will be slower.

---
{{define_cvar("animgraph_debug_max_poseop_count")}}

---
