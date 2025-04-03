## C_CSGO_TeamSelectCharacterPosition
Derived from: [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_HEGrenade
Derived from: [C_BaseCSGrenade](#c_basecsgrenade), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_FuncMover
Derived from: [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_TriggerLerpObject
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPlayer_MovementServices
Derived from: [CPlayer_MovementServices_Humanoid](#cplayer_movementservices_humanoid), [CPlayer_MovementServices](#cplayer_movementservices)

Type | Name
------------ | -------------
`Vector` | m_vecLadderNormal
`int32` | m_nLadderSurfacePropIndex
`float32` | m_flDuckAmount
`float32` | m_flDuckSpeed
`bool` | m_bDuckOverride
`bool` | m_bDesiresDuck
`float32` | m_flDuckOffset
`uint32` | m_nDuckTimeMsecs
`uint32` | m_nDuckJumpTimeMsecs
`uint32` | m_nJumpTimeMsecs
`float32` | m_flLastDuckTime
`Vector2D` | m_vecLastPositionAtFullCrouchSpeed
`bool` | m_duckUntilOnGround
`bool` | m_bHasWalkMovedSinceLastJump
`bool` | m_bInStuckTest
`float32[64][2]` | m_flStuckCheckTime
`int32` | m_nTraceCount
`int32` | m_StuckLast
`bool` | m_bSpeedCropped
`float32` | m_flGroundMoveEfficiency
`int32` | m_nOldWaterLevel
`float32` | m_flWaterEntryTime
`Vector` | m_vecForward
`Vector` | m_vecLeft
`Vector` | m_vecUp
`int32` | m_nGameCodeHasMovedPlayerAfterCommand
`bool` | m_bOldJumpPressed
`float32` | m_flJumpPressedTime
`GameTime_t` | m_fStashGrenadeParameterWhen
`uint64` | m_nButtonDownMaskPrev
`float32` | m_flOffsetTickCompleteTime
`float32` | m_flOffsetTickStashedSpeed
`float32` | m_flStamina
`float32` | m_flHeightAtJumpStart
`float32` | m_flMaxJumpHeightThisJump
`float32` | m_flMaxJumpHeightLastJump
`float32` | m_flStaminaAtJumpStart
`float32` | m_flAccumulatedJumpError

---

## sky3dparams_t

Type | Name
------------ | -------------
`int16` | scale
`Vector` | origin
`bool` | bClip3DSkyBoxNearToWorldFar
`float32` | flClip3DSkyBoxNearToWorldFarOffset
`fogparams_t` | fog
`WorldGroupId_t` | m_nWorldGroupID

---

## C_WeaponM4A1
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_Item
Derived from: [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`char[256]` | m_pReticleHintTextName

---

## C_SoundEventPathCornerEntity
Derived from: [C_SoundEventEntity](#c_soundevententity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`C_NetworkUtlVectorBase< SoundeventPathCornerPairNetworked_t >` | m_vecCornerPairsNetworked

---

## C_WeaponM249
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGameRules
Derived from: [C_TeamplayRules](#c_teamplayrules), [C_MultiplayRules](#c_multiplayrules), [C_GameRules](#c_gamerules)

Type | Name
------------ | -------------
`bool` | m_bFreezePeriod
`bool` | m_bWarmupPeriod
`GameTime_t` | m_fWarmupPeriodEnd
`GameTime_t` | m_fWarmupPeriodStart
`bool` | m_bServerPaused
`bool` | m_bTerroristTimeOutActive
`bool` | m_bCTTimeOutActive
`float32` | m_flTerroristTimeOutRemaining
`float32` | m_flCTTimeOutRemaining
`int32` | m_nTerroristTimeOuts
`int32` | m_nCTTimeOuts
`bool` | m_bTechnicalTimeOut
`bool` | m_bMatchWaitingForResume
`int32` | m_iRoundTime
`float32` | m_fMatchStartTime
`GameTime_t` | m_fRoundStartTime
`GameTime_t` | m_flRestartRoundTime
`bool` | m_bGameRestart
`float32` | m_flGameStartTime
`float32` | m_timeUntilNextPhaseStarts
`int32` | m_gamePhase
`int32` | m_totalRoundsPlayed
`int32` | m_nRoundsPlayedThisPhase
`int32` | m_nOvertimePlaying
`int32` | m_iHostagesRemaining
`bool` | m_bAnyHostageReached
`bool` | m_bMapHasBombTarget
`bool` | m_bMapHasRescueZone
`bool` | m_bMapHasBuyZone
`bool` | m_bIsQueuedMatchmaking
`int32` | m_nQueuedMatchmakingMode
`bool` | m_bIsValveDS
`bool` | m_bLogoMap
`bool` | m_bPlayAllStepSoundsOnServer
`int32` | m_iSpectatorSlotCount
`int32` | m_MatchDevice
`bool` | m_bHasMatchStarted
`int32` | m_nNextMapInMapgroup
`char[512]` | m_szTournamentEventName
`char[512]` | m_szTournamentEventStage
`char[512]` | m_szMatchStatTxt
`char[512]` | m_szTournamentPredictionsTxt
`int32` | m_nTournamentPredictionsPct
`GameTime_t` | m_flCMMItemDropRevealStartTime
`GameTime_t` | m_flCMMItemDropRevealEndTime
`bool` | m_bIsDroppingItems
`bool` | m_bIsQuestEligible
`bool` | m_bIsHltvActive
`uint16[100]` | m_arrProhibitedItemIndices
`uint32[4]` | m_arrTournamentActiveCasterAccounts
`int32` | m_numBestOfMaps
`int32` | m_nHalloweenMaskListSeed
`bool` | m_bBombDropped
`bool` | m_bBombPlanted
`int32` | m_iRoundWinStatus
`int32` | m_eRoundWinReason
`bool` | m_bTCantBuy
`bool` | m_bCTCantBuy
`int32[30]` | m_iMatchStats_RoundResults
`int32[30]` | m_iMatchStats_PlayersAlive_CT
`int32[30]` | m_iMatchStats_PlayersAlive_T
`float32[32]` | m_TeamRespawnWaveTimes
`GameTime_t[32]` | m_flNextRespawnWave
`int32` | m_nServerQuestID
`Vector` | m_vMinimapMins
`Vector` | m_vMinimapMaxs
`float32[8]` | m_MinimapVerticalSectionHeights
`bool` | m_bSpawnedTerrorHuntHeavy
`uint64` | m_ullLocalMatchID
`int32[10]` | m_nEndMatchMapGroupVoteTypes
`int32[10]` | m_nEndMatchMapGroupVoteOptions
`int32` | m_nEndMatchMapVoteWinner
`int32` | m_iNumConsecutiveCTLoses
`int32` | m_iNumConsecutiveTerroristLoses
`bool` | m_bMarkClientStopRecordAtRoundEnd
`int32` | m_nMatchAbortedEarlyReason
`bool` | m_bHasTriggeredRoundStartMusic
`bool` | m_bSwitchingTeamsAtRoundReset
`CCSGameModeRules*` | m_pGameModeRules
`C_RetakeGameRules` | m_RetakeRules
`uint8` | m_nMatchEndCount
`int32` | m_nTTeamIntroVariant
`int32` | m_nCTTeamIntroVariant
`bool` | m_bTeamIntroPeriod
`int32` | m_iRoundEndWinnerTeam
`int32` | m_eRoundEndReason
`bool` | m_bRoundEndShowTimerDefend
`int32` | m_iRoundEndTimerTime
`CUtlString` | m_sRoundEndFunFactToken
`CPlayerSlot` | m_iRoundEndFunFactPlayerSlot
`int32` | m_iRoundEndFunFactData1
`int32` | m_iRoundEndFunFactData2
`int32` | m_iRoundEndFunFactData3
`CUtlString` | m_sRoundEndMessage
`int32` | m_iRoundEndPlayerCount
`bool` | m_bRoundEndNoMusic
`int32` | m_iRoundEndLegacy
`uint8` | m_nRoundEndCount
`int32` | m_iRoundStartRoundNumber
`uint8` | m_nRoundStartCount
`float64` | m_flLastPerfSampleTime

---

## CBodyComponentSkeletonInstance
Derived from: [CBodyComponent](#cbodycomponent), [CEntityComponent](#centitycomponent)

Type | Name
------------ | -------------
`CSkeletonInstance` | m_skeletonInstance

---

## C_WeaponCZ75a
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BaseModelEntity
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CRenderComponent*` | m_CRenderComponent
`CHitboxComponent` | m_CHitboxComponent
`HitGroup_t` | m_LastHitGroup
`bool` | m_bInitModelEffects
`bool` | m_bIsStaticProp
`int32` | m_nLastAddDecal
`int32` | m_nDecalsAdded
`int32` | m_iOldHealth
`RenderMode_t` | m_nRenderMode
`RenderFx_t` | m_nRenderFX
`bool` | m_bAllowFadeInView
`Color` | m_clrRender
`C_UtlVectorEmbeddedNetworkVar< EntityRenderAttribute_t >` | m_vecRenderAttributes
`bool` | m_bRenderToCubemaps
`bool` | m_bNoInterpolate
`CCollisionProperty` | m_Collision
`CGlowProperty` | m_Glow
`float32` | m_flGlowBackfaceMult
`float32` | m_fadeMinDist
`float32` | m_fadeMaxDist
`float32` | m_flFadeScale
`float32` | m_flShadowStrength
`uint8` | m_nObjectCulling
`int32` | m_nAddDecal
`Vector` | m_vDecalPosition
`Vector` | m_vDecalForwardAxis
`float32` | m_flDecalHealBloodRate
`float32` | m_flDecalHealHeightRate
`C_NetworkUtlVectorBase< CHandle< C_BaseModelEntity > >` | m_ConfigEntitiesToPropagateMaterialDecalsTo
`CNetworkViewOffsetVector` | m_vecViewOffset
`CClientAlphaProperty*` | m_pClientAlphaProperty
`Color` | m_ClientOverrideTint
`bool` | m_bUseClientOverrideTint

---

## C_FootstepControl
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CUtlSymbolLarge` | m_source
`CUtlSymbolLarge` | m_destination

---

## C_PointClientUIHUD
Derived from: [C_BaseClientUIEntity](#c_baseclientuientity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bCheckCSSClasses
`bool` | m_bIgnoreInput
`float32` | m_flWidth
`float32` | m_flHeight
`float32` | m_flDPI
`float32` | m_flInteractDistance
`float32` | m_flDepthOffset
`uint32` | m_unOwnerContext
`uint32` | m_unHorizontalAlign
`uint32` | m_unVerticalAlign
`uint32` | m_unOrientation
`bool` | m_bAllowInteractionFromAllSceneWorlds
`C_NetworkUtlVectorBase< CUtlSymbolLarge >` | m_vecCSSClasses

---

## C_SpotlightEnd
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flLightScale
`float32` | m_Radius

---

## CEconItemAttribute

Type | Name
------------ | -------------
`uint16` | m_iAttributeDefinitionIndex
`float32` | m_flValue
`float32` | m_flInitialValue
`int32` | m_nRefundableCurrency
`bool` | m_bSetBonus

---

## C_PointCamera
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_FOV
`float32` | m_Resolution
`bool` | m_bFogEnable
`Color` | m_FogColor
`float32` | m_flFogStart
`float32` | m_flFogEnd
`float32` | m_flFogMaxDensity
`bool` | m_bActive
`bool` | m_bUseScreenAspectRatio
`float32` | m_flAspectRatio
`bool` | m_bNoSky
`float32` | m_fBrightness
`float32` | m_flZFar
`float32` | m_flZNear
`bool` | m_bCanHLTVUse
`bool` | m_bAlignWithParent
`bool` | m_bDofEnabled
`float32` | m_flDofNearBlurry
`float32` | m_flDofNearCrisp
`float32` | m_flDofFarCrisp
`float32` | m_flDofFarBlurry
`float32` | m_flDofTiltToGround
`float32` | m_TargetFOV
`float32` | m_DegreesPerSecond
`bool` | m_bIsOn
`C_PointCamera*` | m_pNext

---

## CCSPointScriptExtensions_weapon_cs_base

---

## C_LightSpotEntity
Derived from: [C_LightEntity](#c_lightentity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EnvWind
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`C_EnvWindShared` | m_EnvWindShared

---

## C_GameRulesProxy
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BaseCombatCharacter
Derived from: [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`C_NetworkUtlVectorBase< CHandle< C_EconWearable > >` | m_hMyWearables
`AttachmentHandle_t` | m_leftFootAttachment
`AttachmentHandle_t` | m_rightFootAttachment
`C_BaseCombatCharacter::WaterWakeMode_t` | m_nWaterWakeMode
`float32` | m_flWaterWorldZ
`float32` | m_flWaterNextTraceTime

---

## C_FlashbangProjectile
Derived from: [C_BaseCSGrenadeProjectile](#c_basecsgrenadeprojectile), [C_BaseGrenade](#c_basegrenade), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CEnvSoundscapeTriggerable
Derived from: [CEnvSoundscape](#cenvsoundscape), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_SoundEventSphereEntity
Derived from: [C_SoundEventEntity](#c_soundevententity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flRadius

---

## CPlayer_ViewModelServices


---

## CCSGO_WingmanIntroCounterTerroristPosition
Derived from: [CCSGO_WingmanIntroCharacterPosition](#ccsgo_wingmanintrocharacterposition), [C_CSGO_TeamIntroCharacterPosition](#c_csgo_teamintrocharacterposition), [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_DynamicPropAlias_cable_dynamic
Derived from: [C_DynamicProp](#c_dynamicprop), [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_InfoInstructorHintHostageRescueZone
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_SceneEntity
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bIsPlayingBack
`bool` | m_bPaused
`bool` | m_bMultiplayer
`bool` | m_bAutogenerated
`float32` | m_flForceClientTime
`uint16` | m_nSceneStringIndex
`bool` | m_bClientOnly
`CHandle< C_BaseFlex >` | m_hOwner
`C_NetworkUtlVectorBase< CHandle< C_BaseFlex > >` | m_hActorList
`bool` | m_bWasPlaying
`CUtlVector< C_SceneEntity::QueuedEvents_t >` | m_QueuedEvents
`float32` | m_flCurrentTime

---

## CPlayer_CameraServices


Type | Name
------------ | -------------
`QAngle` | m_vecCsViewPunchAngle
`GameTick_t` | m_nCsViewPunchAngleTick
`float32` | m_flCsViewPunchAngleTickRatio
`C_fogplayerparams_t` | m_PlayerFog
`CHandle< C_ColorCorrection >` | m_hColorCorrectionCtrl
`CHandle< C_BaseEntity >` | m_hViewEntity
`CHandle< C_TonemapController2 >` | m_hTonemapController
`audioparams_t` | m_audio
`C_NetworkUtlVectorBase< CHandle< C_PostProcessingVolume > >` | m_PostProcessingVolumes
`float32` | m_flOldPlayerZ
`float32` | m_flOldPlayerViewOffsetZ
`fogparams_t` | m_CurrentFog
`CHandle< C_FogController >` | m_hOldFogController
`bool[5]` | m_bOverrideFogColor
`Color[5]` | m_OverrideFogColor
`bool[5]` | m_bOverrideFogStartEnd
`float32[5]` | m_fOverrideFogStart
`float32[5]` | m_fOverrideFogEnd
`CHandle< C_PostProcessingVolume >` | m_hActivePostProcessingVolume
`QAngle` | m_angDemoViewAngles

---

## C_BaseCSGrenade
Derived from: [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bClientPredictDelete
`bool` | m_bRedraw
`bool` | m_bIsHeldByPlayer
`bool` | m_bPinPulled
`bool` | m_bJumpThrow
`bool` | m_bThrowAnimating
`GameTime_t` | m_fThrowTime
`float32` | m_flThrowStrength
`float32` | m_flThrowStrengthApproach
`GameTime_t` | m_fDropTime
`GameTime_t` | m_fPinPullTime
`bool` | m_bJustPulledPin
`GameTick_t` | m_nNextHoldTick
`float32` | m_flNextHoldFrac
`CHandle< C_CSWeaponBase >` | m_hSwitchToWeaponAfterThrow

---

## C_FuncMonitor
Derived from: [C_FuncBrush](#c_funcbrush), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CUtlString` | m_targetCamera
`int32` | m_nResolutionEnum
`bool` | m_bRenderShadows
`bool` | m_bUseUniqueColorTarget
`CUtlString` | m_brushModelName
`CHandle< C_BaseEntity >` | m_hTargetCamera
`bool` | m_bEnabled
`bool` | m_bDraw3DSkybox

---

## C_TriggerMultiple
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_RopeKeyframe::CPhysicsDelegate

Type | Name
------------ | -------------
`C_RopeKeyframe*` | m_pKeyframe

---

## CBodyComponent
Derived from: [CEntityComponent](#centitycomponent)

Type | Name
------------ | -------------
`CGameSceneNode*` | m_pSceneNode
`CNetworkVarChainer` | __m_pChainEntity

---

## C_SoundAreaEntitySphere
Derived from: [C_SoundAreaEntityBase](#c_soundareaentitybase), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flRadius

---

## CCSObserver_MovementServices
Derived from: [CPlayer_MovementServices](#cplayer_movementservices)

---

## C_LightGlow
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`uint32` | m_nHorizontalSize
`uint32` | m_nVerticalSize
`uint32` | m_nMinDist
`uint32` | m_nMaxDist
`uint32` | m_nOuterMaxDist
`float32` | m_flGlowProxySize
`float32` | m_flHDRColorScale
`C_LightGlowOverlay` | m_GlowOverlay

---

## CountdownTimer

Type | Name
------------ | -------------
`float32` | m_duration
`GameTime_t` | m_timestamp
`float32` | m_timescale
`WorldGroupId_t` | m_nWorldGroupId

---

## CGameSceneNodeHandle

Type | Name
------------ | -------------
`CEntityHandle` | m_hOwner
`CUtlStringToken` | m_name

---

## PredictedDamageTag_t

Type | Name
------------ | -------------
`GameTick_t` | nTagTick
`float32` | flFlinchModSmall
`float32` | flFlinchModLarge
`float32` | flFriendlyFireDamageReductionRatio

---

## C_ClientRagdoll
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bFadeOut
`bool` | m_bImportant
`GameTime_t` | m_flEffectTime
`GameTime_t` | m_gibDespawnTime
`int32` | m_iCurrentFriction
`int32` | m_iMinFriction
`int32` | m_iMaxFriction
`int32` | m_iFrictionAnimState
`bool` | m_bReleaseRagdoll
`AttachmentHandle_t` | m_iEyeAttachment
`bool` | m_bFadingOut
`float32[10]` | m_flScaleEnd
`GameTime_t[10]` | m_flScaleTimeStart
`GameTime_t[10]` | m_flScaleTimeEnd

---

## C_GlobalLight
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`uint16` | m_WindClothForceHandle

---

## C_CSPlayerResource
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool[12]` | m_bHostageAlive
`bool[12]` | m_isHostageFollowingSomeone
`CEntityIndex[12]` | m_iHostageEntityIDs
`Vector` | m_bombsiteCenterA
`Vector` | m_bombsiteCenterB
`int32[4]` | m_hostageRescueX
`int32[4]` | m_hostageRescueY
`int32[4]` | m_hostageRescueZ
`bool` | m_bEndMatchNextMapAllVoted
`bool` | m_foundGoalPositions

---

## CSkeletonInstance
Derived from: [CGameSceneNode](#cgamescenenode)

Type | Name
------------ | -------------
`CModelState` | m_modelState
`bool` | m_bIsAnimationEnabled
`bool` | m_bUseParentRenderBounds
`bool` | m_bDisableSolidCollisionsForHierarchy
`bitfield:1` | m_bDirtyMotionType
`bitfield:1` | m_bIsGeneratingLatchedParentSpaceState
`CUtlStringToken` | m_materialGroup
`uint8` | m_nHitboxSet

---

## CBodyComponentBaseAnimGraph
Derived from: [CBodyComponentSkeletonInstance](#cbodycomponentskeletoninstance), [CBodyComponent](#cbodycomponent), [CEntityComponent](#centitycomponent)

Type | Name
------------ | -------------
`CBaseAnimGraphController` | m_animationController

---

## CBodyComponentPoint
Derived from: [CBodyComponent](#cbodycomponent), [CEntityComponent](#centitycomponent)

Type | Name
------------ | -------------
`CGameSceneNode` | m_sceneNode

---

## C_SmokeGrenadeProjectile
Derived from: [C_BaseCSGrenadeProjectile](#c_basecsgrenadeprojectile), [C_BaseGrenade](#c_basegrenade), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`int32` | m_nSmokeEffectTickBegin
`bool` | m_bDidSmokeEffect
`int32` | m_nRandomSeed
`Vector` | m_vSmokeColor
`Vector` | m_vSmokeDetonationPos
`C_NetworkUtlVectorBase< uint8 >` | m_VoxelFrameData
`int32` | m_nVoxelFrameDataSize
`int32` | m_nVoxelUpdate
`bool` | m_bSmokeVolumeDataReceived
`bool` | m_bSmokeEffectSpawned

---

## C_SoundEventEntityAlias_snd_event_point
Derived from: [C_SoundEventEntity](#c_soundevententity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_MapPreviewCameraPath
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flZFar
`float32` | m_flZNear
`bool` | m_bLoop
`bool` | m_bVerticalFOV
`bool` | m_bConstantSpeed
`float32` | m_flDuration
`float32` | m_flPathLength
`float32` | m_flPathDuration

---

## CCSGO_WingmanIntroTerroristPosition
Derived from: [CCSGO_WingmanIntroCharacterPosition](#ccsgo_wingmanintrocharacterposition), [C_CSGO_TeamIntroCharacterPosition](#c_csgo_teamintrocharacterposition), [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_Inferno
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`ParticleIndex_t` | m_nfxFireDamageEffect
`CStrongHandle< InfoForResourceTypeIParticleSnapshot >` | m_hInfernoPointsSnapshot
`CStrongHandle< InfoForResourceTypeIParticleSnapshot >` | m_hInfernoFillerPointsSnapshot
`CStrongHandle< InfoForResourceTypeIParticleSnapshot >` | m_hInfernoOutlinePointsSnapshot
`CStrongHandle< InfoForResourceTypeIParticleSnapshot >` | m_hInfernoClimbingOutlinePointsSnapshot
`CStrongHandle< InfoForResourceTypeIParticleSnapshot >` | m_hInfernoDecalsSnapshot
`Vector[64]` | m_firePositions
`Vector[64]` | m_fireParentPositions
`bool[64]` | m_bFireIsBurning
`Vector[64]` | m_BurnNormal
`int32` | m_fireCount
`int32` | m_nInfernoType
`float32` | m_nFireLifetime
`bool` | m_bInPostEffectTime
`int32` | m_lastFireCount
`int32` | m_nFireEffectTickBegin
`int32` | m_drawableCount
`bool` | m_blosCheck
`int32` | m_nlosperiod
`float32` | m_maxFireHalfWidth
`float32` | m_maxFireHeight
`Vector` | m_minBounds
`Vector` | m_maxBounds
`float32` | m_flLastGrassBurnThink

---

## C_HostageCarriableProp
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_TerroristWingmanIntroCamera
Derived from: [C_CSGO_TeamPreviewCamera](#c_csgo_teampreviewcamera), [C_CSGO_MapPreviewCameraPath](#c_csgo_mappreviewcamerapath), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_PlayerPing
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CHandle< C_CSPlayerPawn >` | m_hPlayer
`CHandle< C_BaseEntity >` | m_hPingedEntity
`int32` | m_iType
`bool` | m_bUrgent
`char[18]` | m_szPlaceName

---

## C_WeaponMP7
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSTeam
Derived from: [C_Team](#c_team), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`char[512]` | m_szTeamMatchStat
`int32` | m_numMapVictories
`bool` | m_bSurrendered
`int32` | m_scoreFirstHalf
`int32` | m_scoreSecondHalf
`int32` | m_scoreOvertime
`char[129]` | m_szClanTeamname
`uint32` | m_iClanID
`char[8]` | m_szTeamFlagImage
`char[8]` | m_szTeamLogoImage

---

## C_CSGO_MapPreviewCameraPathNode
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CUtlSymbolLarge` | m_szParentPathUniqueID
`int32` | m_nPathIndex
`Vector` | m_vInTangentLocal
`Vector` | m_vOutTangentLocal
`float32` | m_flFOV
`float32` | m_flCameraSpeed
`float32` | m_flEaseIn
`float32` | m_flEaseOut
`Vector` | m_vInTangentWorld
`Vector` | m_vOutTangentWorld

---

## C_WeaponMag7
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_DEagle
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSPlayerPawn
Derived from: [C_CSPlayerPawnBase](#c_csplayerpawnbase), [C_BasePlayerPawn](#c_baseplayerpawn), [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CCSPlayer_BulletServices*` | m_pBulletServices
`CCSPlayer_HostageServices*` | m_pHostageServices
`CCSPlayer_BuyServices*` | m_pBuyServices
`CCSPlayer_GlowServices*` | m_pGlowServices
`CCSPlayer_ActionTrackingServices*` | m_pActionTrackingServices
`CCSPlayer_DamageReactServices*` | m_pDamageReactServices
`GameTime_t` | m_flHealthShotBoostExpirationTime
`GameTime_t` | m_flLastFiredWeaponTime
`bool` | m_bHasFemaleVoice
`float32` | m_flLandingTimeSeconds
`float32` | m_flOldFallVelocity
`char[18]` | m_szLastPlaceName
`bool` | m_bPrevDefuser
`bool` | m_bPrevHelmet
`int32` | m_nPrevArmorVal
`int32` | m_nPrevGrenadeAmmoCount
`uint32` | m_unPreviousWeaponHash
`uint32` | m_unWeaponHash
`bool` | m_bInBuyZone
`bool` | m_bPreviouslyInBuyZone
`QAngle` | m_aimPunchAngle
`QAngle` | m_aimPunchAngleVel
`int32` | m_aimPunchTickBase
`float32` | m_aimPunchTickFraction
`CUtlVector< QAngle >` | m_aimPunchCache
`bool` | m_bInLanding
`float32` | m_flLandingStartTime
`bool` | m_bInHostageRescueZone
`bool` | m_bInBombZone
`bool` | m_bIsBuyMenuOpen
`GameTime_t` | m_flTimeOfLastInjury
`GameTime_t` | m_flNextSprayDecalTime
`int32` | m_iRetakesOffering
`int32` | m_iRetakesOfferingCard
`bool` | m_bRetakesHasDefuseKit
`bool` | m_bRetakesMVPLastRound
`int32` | m_iRetakesMVPBoostItem
`loadout_slot_t` | m_RetakesMVPBoostExtraUtility
`bool` | m_bNeedToReApplyGloves
`C_EconItemView` | m_EconGloves
`uint8` | m_nEconGlovesChanged
`bool` | m_bMustSyncRagdollState
`int32` | m_nRagdollDamageBone
`Vector` | m_vRagdollDamageForce
`Vector` | m_vRagdollDamagePosition
`char[64]` | m_szRagdollDamageWeaponName
`bool` | m_bRagdollDamageHeadshot
`Vector` | m_vRagdollServerOrigin
`bool` | m_bLastHeadBoneTransformIsValid
`GameTime_t` | m_lastLandTime
`bool` | m_bOnGroundLastTick
`QAngle` | m_qDeathEyeAngles
`bool` | m_bSkipOneHeadConstraintUpdate
`bool` | m_bLeftHanded
`GameTime_t` | m_fSwitchedHandednessTime
`float32` | m_flViewmodelOffsetX
`float32` | m_flViewmodelOffsetY
`float32` | m_flViewmodelOffsetZ
`float32` | m_flViewmodelFOV
`uint32[5]` | m_vecPlayerPatchEconIndices
`Color` | m_GunGameImmunityColor
`CUtlVector< C_BulletHitModel* >` | m_vecBulletHitModels
`bool` | m_bIsWalking
`QAngle` | m_thirdPersonHeading
`float32` | m_flSlopeDropOffset
`float32` | m_flSlopeDropHeight
`Vector` | m_vHeadConstraintOffset
`EntitySpottedState_t` | m_entitySpottedState
`bool` | m_bIsScoped
`bool` | m_bResumeZoom
`bool` | m_bIsDefusing
`bool` | m_bIsGrabbingHostage
`CSPlayerBlockingUseAction_t` | m_iBlockingUseActionInProgress
`GameTime_t` | m_flEmitSoundTime
`bool` | m_bInNoDefuseArea
`int32` | m_nWhichBombZone
`int32` | m_iShotsFired
`float32` | m_flFlinchStack
`float32` | m_flVelocityModifier
`float32` | m_flHitHeading
`int32` | m_nHitBodyPart
`bool` | m_bWaitForNoAttack
`float32` | m_ignoreLadderJumpTime
`bool` | m_bKilledByHeadshot
`int32` | m_ArmorValue
`uint16` | m_unCurrentEquipmentValue
`uint16` | m_unRoundStartEquipmentValue
`uint16` | m_unFreezetimeEndEquipmentValue
`CEntityIndex` | m_nLastKillerIndex
`bool` | m_bOldIsScoped
`bool` | m_bHasDeathInfo
`float32` | m_flDeathInfoTime
`Vector` | m_vecDeathInfoOrigin
`GameTime_t` | m_grenadeParameterStashTime
`bool` | m_bGrenadeParametersStashed
`QAngle` | m_angStashedShootAngles
`Vector` | m_vecStashedGrenadeThrowPosition
`Vector` | m_vecStashedVelocity
`QAngle[2]` | m_angShootAngleHistory
`Vector[2]` | m_vecThrowPositionHistory
`Vector[2]` | m_vecVelocityHistory
`C_UtlVectorEmbeddedNetworkVar< PredictedDamageTag_t >` | m_PredictedDamageTags
`GameTick_t` | m_nPrevHighestReceivedDamageTagTick
`int32` | m_nHighestAppliedDamageTagTick

---

## C_RagdollPropAttached
Derived from: [C_RagdollProp](#c_ragdollprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`uint32` | m_boneIndexAttached
`uint32` | m_ragdollAttachedObjectIndex
`Vector` | m_attachmentPointBoneSpace
`Vector` | m_attachmentPointRagdollSpace
`Vector` | m_vecOffset
`float32` | m_parentTime
`bool` | m_bHasParent

---

## C_BaseCSGrenadeProjectile
Derived from: [C_BaseGrenade](#c_basegrenade), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`Vector` | m_vInitialPosition
`Vector` | m_vInitialVelocity
`int32` | m_nBounces
`CStrongHandle< InfoForResourceTypeIParticleSystemDefinition >` | m_nExplodeEffectIndex
`int32` | m_nExplodeEffectTickBegin
`Vector` | m_vecExplodeEffectOrigin
`GameTime_t` | m_flSpawnTime
`Vector` | vecLastTrailLinePos
`GameTime_t` | flNextTrailLineTime
`bool` | m_bExplodeEffectBegan
`bool` | m_bCanCreateGrenadeTrail
`ParticleIndex_t` | m_nSnapshotTrajectoryEffectIndex
`CStrongHandle< InfoForResourceTypeIParticleSnapshot >` | m_hSnapshotTrajectoryParticleSnapshot
`CUtlVector< Vector >` | m_arrTrajectoryTrailPoints
`CUtlVector< float32 >` | m_arrTrajectoryTrailPointCreationTimes
`float32` | m_flTrajectoryTrailEffectCreationTime

---

## C_BaseTrigger
Derived from: [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bDisabled
`bool` | m_bClientSidePredicted

---

## C_WeaponBaseItem
Derived from: [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CountdownTimer` | m_SequenceCompleteTimer
`bool` | m_bRedraw

---

## CEffectData

Type | Name
------------ | -------------
`Vector` | m_vOrigin
`Vector` | m_vStart
`Vector` | m_vNormal
`QAngle` | m_vAngles
`CEntityHandle` | m_hEntity
`CEntityHandle` | m_hOtherEntity
`float32` | m_flScale
`float32` | m_flMagnitude
`float32` | m_flRadius
`CUtlStringToken` | m_nSurfaceProp
`CWeakHandle< InfoForResourceTypeIParticleSystemDefinition >` | m_nEffectIndex
`uint32` | m_nDamageType
`uint8` | m_nPenetrate
`uint16` | m_nMaterial
`uint16` | m_nHitBox
`uint8` | m_nColor
`uint8` | m_fFlags
`AttachmentHandle_t` | m_nAttachmentIndex
`CUtlStringToken` | m_nAttachmentName
`uint16` | m_iEffectName
`uint8` | m_nExplosionType

---

## C_MolotovGrenade
Derived from: [C_BaseCSGrenade](#c_basecsgrenade), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BaseButton
Derived from: [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CHandle< C_BaseModelEntity >` | m_glowEntity
`bool` | m_usable
`CUtlSymbolLarge` | m_szDisplayText

---

## CCSPlayer_ViewModelServices
Derived from: [CPlayer_ViewModelServices](#cplayer_viewmodelservices)

Type | Name
------------ | -------------
`CHandle< C_BaseViewModel >[3]` | m_hViewModel

---

## CInfoParticleTarget
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPlayer_MovementServices_Humanoid
Derived from: [CPlayer_MovementServices](#cplayer_movementservices)

Type | Name
------------ | -------------
`float32` | m_flStepSoundTime
`float32` | m_flFallVelocity
`bool` | m_bInCrouch
`uint32` | m_nCrouchState
`GameTime_t` | m_flCrouchTransitionStartTime
`bool` | m_bDucked
`bool` | m_bDucking
`bool` | m_bInDuckJump
`Vector` | m_groundNormal
`float32` | m_flSurfaceFriction
`CUtlStringToken` | m_surfaceProps
`int32` | m_nStepside

---

## C_WeaponAug
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CEnvSoundscapeProxyAlias_snd_soundscape_proxy
Derived from: [CEnvSoundscapeProxy](#cenvsoundscapeproxy), [CEnvSoundscape](#cenvsoundscape), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_PointClientUIWorldPanel
Derived from: [C_BaseClientUIEntity](#c_baseclientuientity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bForceRecreateNextUpdate
`bool` | m_bMoveViewToPlayerNextThink
`bool` | m_bCheckCSSClasses
`CTransform` | m_anchorDeltaTransform
`CPointOffScreenIndicatorUi*` | m_pOffScreenIndicator
`bool` | m_bIgnoreInput
`bool` | m_bLit
`bool` | m_bFollowPlayerAcrossTeleport
`float32` | m_flWidth
`float32` | m_flHeight
`float32` | m_flDPI
`float32` | m_flInteractDistance
`float32` | m_flDepthOffset
`uint32` | m_unOwnerContext
`uint32` | m_unHorizontalAlign
`uint32` | m_unVerticalAlign
`uint32` | m_unOrientation
`bool` | m_bAllowInteractionFromAllSceneWorlds
`C_NetworkUtlVectorBase< CUtlSymbolLarge >` | m_vecCSSClasses
`bool` | m_bOpaque
`bool` | m_bNoDepth
`bool` | m_bRenderBackface
`bool` | m_bUseOffScreenIndicator
`bool` | m_bExcludeFromSaveGames
`bool` | m_bGrabbable
`bool` | m_bOnlyRenderToTexture
`bool` | m_bDisableMipGen
`int32` | m_nExplicitImageLayout

---

## C_CSMinimapBoundary
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSGameModeRules_Deathmatch
Derived from: [CCSGameModeRules](#ccsgamemoderules)

Type | Name
------------ | -------------
`GameTime_t` | m_flDMBonusStartTime
`float32` | m_flDMBonusTimeLength
`CUtlString` | m_sDMBonusWeapon

---

## C_CSGO_EndOfMatchCharacterPosition
Derived from: [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_SoundOpvarSetAABBEntity
Derived from: [C_SoundOpvarSetPointEntity](#c_soundopvarsetpointentity), [C_SoundOpvarSetPointBase](#c_soundopvarsetpointbase), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_GameRules

Type | Name
------------ | -------------
`CNetworkVarChainer` | __m_pChainEntity
`int32` | m_nTotalPausedTicks
`int32` | m_nPauseStartTick
`bool` | m_bGamePaused

---

## C_PropDoorRotating
Derived from: [C_BasePropDoor](#c_basepropdoor), [C_DynamicProp](#c_dynamicprop), [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_Team
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`C_NetworkUtlVectorBase< CHandle< CBasePlayerController > >` | m_aPlayerControllers
`C_NetworkUtlVectorBase< CHandle< C_BasePlayerPawn > >` | m_aPlayers
`int32` | m_iScore
`char[129]` | m_szTeamname

---

## C_SoundAreaEntityOrientedBox
Derived from: [C_SoundAreaEntityBase](#c_soundareaentitybase), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`Vector` | m_vMin
`Vector` | m_vMax

---

## C_TextureBasedAnimatable
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bLoop
`float32` | m_flFPS
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_hPositionKeys
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_hRotationKeys
`Vector` | m_vAnimationBoundsMin
`Vector` | m_vAnimationBoundsMax
`float32` | m_flStartTime
`float32` | m_flStartFrame

---

## C_SoundOpvarSetPointEntity
Derived from: [C_SoundOpvarSetPointBase](#c_soundopvarsetpointbase), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_LightOrthoEntity
Derived from: [C_LightEntity](#c_lightentity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPlayer_WaterServices
Derived from: [CPlayer_WaterServices](#cplayer_waterservices)

Type | Name
------------ | -------------
`float32` | m_flWaterJumpTime
`Vector` | m_vecWaterJumpVel
`float32` | m_flSwimSoundTime

---

## CSkyboxReference
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`WorldGroupId_t` | m_worldGroupId
`CHandle< C_SkyCamera >` | m_hSkyCamera

---

## C_TonemapController2Alias_env_tonemap_controller2
Derived from: [C_TonemapController2](#c_tonemapcontroller2), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CProjectedTextureBase

Type | Name
------------ | -------------
`CHandle< C_BaseEntity >` | m_hTargetEntity
`bool` | m_bState
`bool` | m_bAlwaysUpdate
`float32` | m_flLightFOV
`bool` | m_bEnableShadows
`bool` | m_bSimpleProjection
`bool` | m_bLightOnlyTarget
`bool` | m_bLightWorld
`bool` | m_bCameraSpace
`float32` | m_flBrightnessScale
`Color` | m_LightColor
`float32` | m_flIntensity
`float32` | m_flLinearAttenuation
`float32` | m_flQuadraticAttenuation
`bool` | m_bVolumetric
`float32` | m_flVolumetricIntensity
`float32` | m_flNoiseStrength
`float32` | m_flFlashlightTime
`uint32` | m_nNumPlanes
`float32` | m_flPlaneOffset
`float32` | m_flColorTransitionTime
`float32` | m_flAmbient
`char[512]` | m_SpotlightTextureName
`int32` | m_nSpotlightTextureFrame
`uint32` | m_nShadowQuality
`float32` | m_flNearZ
`float32` | m_flFarZ
`float32` | m_flProjectionSize
`float32` | m_flRotation
`bool` | m_bFlipHorizontal

---

## CCSPlayerController_InventoryServices


Type | Name
------------ | -------------
`uint16` | m_unMusicID
`MedalRank_t[6]` | m_rank
`int32` | m_nPersonaDataPublicLevel
`int32` | m_nPersonaDataPublicCommendsLeader
`int32` | m_nPersonaDataPublicCommendsTeacher
`int32` | m_nPersonaDataPublicCommendsFriendly
`int32` | m_nPersonaDataXpTrailLevel
`C_UtlVectorEmbeddedNetworkVar< ServerAuthoritativeWeaponSlot_t >` | m_vecServerAuthoritativeWeaponSlots

---

## C_PathParticleRopeAlias_path_particle_rope_clientside
Derived from: [C_PathParticleRope](#c_pathparticlerope), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPlayer_UseServices


---

## C_CSGOViewModel
Derived from: [C_PredictedViewModel](#c_predictedviewmodel), [C_BaseViewModel](#c_baseviewmodel), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bShouldIgnoreOffsetAndAccuracy
`CEntityIndex` | m_nLastKnownAssociatedWeaponEntIndex
`bool` | m_bNeedToQueueHighResComposite
`QAngle` | m_vLoweredWeaponOffset

---

## CScriptComponent
Derived from: [CEntityComponent](#centitycomponent)

Type | Name
------------ | -------------
`CUtlSymbolLarge` | m_scriptClassName

---

## C_EnvLightProbeVolume
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_Entity_hLightProbeTexture
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_Entity_hLightProbeDirectLightIndicesTexture
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_Entity_hLightProbeDirectLightScalarsTexture
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_Entity_hLightProbeDirectLightShadowsTexture
`Vector` | m_Entity_vBoxMins
`Vector` | m_Entity_vBoxMaxs
`bool` | m_Entity_bMoveable
`int32` | m_Entity_nHandshake
`int32` | m_Entity_nPriority
`bool` | m_Entity_bStartDisabled
`int32` | m_Entity_nLightProbeSizeX
`int32` | m_Entity_nLightProbeSizeY
`int32` | m_Entity_nLightProbeSizeZ
`int32` | m_Entity_nLightProbeAtlasX
`int32` | m_Entity_nLightProbeAtlasY
`int32` | m_Entity_nLightProbeAtlasZ
`bool` | m_Entity_bEnabled

---

## C_ViewmodelAttachmentModel
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bShouldFrontFaceCullLeftHanded
`bool` | m_bCreatedLeftHanded

---

## CCSPointScriptExtensions_player_controller

---

## C_Flashbang
Derived from: [C_BaseCSGrenade](#c_basecsgrenade), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CSPerRoundStats_t

Type | Name
------------ | -------------
`int32` | m_iKills
`int32` | m_iDeaths
`int32` | m_iAssists
`int32` | m_iDamage
`int32` | m_iEquipmentValue
`int32` | m_iMoneySaved
`int32` | m_iKillReward
`int32` | m_iLiveTime
`int32` | m_iHeadShotKills
`int32` | m_iObjective
`int32` | m_iCashEarned
`int32` | m_iUtilityDamage
`int32` | m_iEnemiesFlashed

---

## CRagdollManager
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`int8` | m_iCurrentMaxRagdollCount

---

## C_TeamRoundTimer
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bTimerPaused
`float32` | m_flTimeRemaining
`GameTime_t` | m_flTimerEndTime
`bool` | m_bIsDisabled
`bool` | m_bShowInHUD
`int32` | m_nTimerLength
`int32` | m_nTimerInitialLength
`int32` | m_nTimerMaxLength
`bool` | m_bAutoCountdown
`int32` | m_nSetupTimeLength
`int32` | m_nState
`bool` | m_bStartPaused
`bool` | m_bInCaptureWatchState
`float32` | m_flTotalTime
`bool` | m_bStopWatchTimer
`bool` | m_bFireFinished
`bool` | m_bFire5MinRemain
`bool` | m_bFire4MinRemain
`bool` | m_bFire3MinRemain
`bool` | m_bFire2MinRemain
`bool` | m_bFire1MinRemain
`bool` | m_bFire30SecRemain
`bool` | m_bFire10SecRemain
`bool` | m_bFire5SecRemain
`bool` | m_bFire4SecRemain
`bool` | m_bFire3SecRemain
`bool` | m_bFire2SecRemain
`bool` | m_bFire1SecRemain
`int32` | m_nOldTimerLength
`int32` | m_nOldTimerState

---

## WeaponPurchaseCount_t

Type | Name
------------ | -------------
`uint16` | m_nItemDefIndex
`uint16` | m_nCount

---

## C_SmokeGrenade
Derived from: [C_BaseCSGrenade](#c_basecsgrenade), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WeaponGalilAR
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WorldModelGloves
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EnvProjectedTexture
Derived from: [C_ModelPointEntity](#c_modelpointentity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPathSimple
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CUtlString` | m_pathString

---

## CCSPlayerBase_CameraServices
Derived from: [CPlayer_CameraServices](#cplayer_cameraservices)

Type | Name
------------ | -------------
`uint32` | m_iFOV
`uint32` | m_iFOVStart
`GameTime_t` | m_flFOVTime
`float32` | m_flFOVRate
`CHandle< C_BaseEntity >` | m_hZoomOwner
`float32` | m_flLastShotFOV

---

## CPointOffScreenIndicatorUi
Derived from: [C_PointClientUIWorldPanel](#c_pointclientuiworldpanel), [C_BaseClientUIEntity](#c_baseclientuientity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bBeenEnabled
`bool` | m_bHide
`float32` | m_flSeenTargetTime
`C_PointClientUIWorldPanel*` | m_pTargetPanel

---

## CCSPointScriptExtensions_entity

---

## CBodyComponentBaseModelEntity
Derived from: [CBodyComponentSkeletonInstance](#cbodycomponentskeletoninstance), [CBodyComponent](#cbodycomponent), [CEntityComponent](#centitycomponent)

---

## C_CSWeaponBaseGun
Derived from: [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`int32` | m_zoomLevel
`int32` | m_iBurstShotsRemaining
`int32` | m_iSilencerBodygroup
`int32` | m_silencedModelIndex
`bool` | m_inPrecache
`bool` | m_bNeedsBoltAction

---

## C_SkyCamera
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`sky3dparams_t` | m_skyboxData
`CUtlStringToken` | m_skyboxSlotToken
`bool` | m_bUseAngles
`C_SkyCamera*` | m_pNext

---

## C_World
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EntityDissolve
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`GameTime_t` | m_flStartTime
`float32` | m_flFadeInStart
`float32` | m_flFadeInLength
`float32` | m_flFadeOutModelStart
`float32` | m_flFadeOutModelLength
`float32` | m_flFadeOutStart
`float32` | m_flFadeOutLength
`GameTime_t` | m_flNextSparkTime
`EntityDisolveType_t` | m_nDissolveType
`Vector` | m_vDissolverOrigin
`uint32` | m_nMagnitude
`bool` | m_bCoreExplode
`bool` | m_bLinkedToServerEnt

---

## CCSObserver_UseServices
Derived from: [CPlayer_UseServices](#cplayer_useservices)

---

## C_fogplayerparams_t

Type | Name
------------ | -------------
`CHandle< C_FogController >` | m_hCtrl
`float32` | m_flTransitionTime
`Color` | m_OldColor
`float32` | m_flOldStart
`float32` | m_flOldEnd
`float32` | m_flOldMaxDensity
`float32` | m_flOldHDRColorScale
`float32` | m_flOldFarZ
`Color` | m_NewColor
`float32` | m_flNewStart
`float32` | m_flNewEnd
`float32` | m_flNewMaxDensity
`float32` | m_flNewHDRColorScale
`float32` | m_flNewFarZ

---

## C_CSPlayerPawnBase
Derived from: [C_BasePlayerPawn](#c_baseplayerpawn), [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CCSPlayer_PingServices*` | m_pPingServices
`CPlayer_ViewModelServices*` | m_pViewModelServices
`float32[4]` | m_fRenderingClipPlane
`int32` | m_nLastClipPlaneSetupFrame
`Vector` | m_vecLastClipCameraPos
`Vector` | m_vecLastClipCameraForward
`bool` | m_bClipHitStaticWorld
`bool` | m_bCachedPlaneIsValid
`C_CSWeaponBase*` | m_pClippingWeapon
`CSPlayerState` | m_previousPlayerState
`CSPlayerState` | m_iPlayerState
`bool` | m_bIsRescuing
`GameTime_t` | m_fImmuneToGunGameDamageTime
`GameTime_t` | m_fImmuneToGunGameDamageTimeLast
`bool` | m_bGunGameImmunity
`bool` | m_bHasMovedSinceSpawn
`float32` | m_fMolotovUseTime
`float32` | m_fMolotovDamageTime
`int32` | m_iThrowGrenadeCounter
`GameTime_t` | m_flLastSpawnTimeIndex
`int32` | m_iProgressBarDuration
`float32` | m_flProgressBarStartTime
`Vector` | m_vecIntroStartEyePosition
`Vector` | m_vecIntroStartPlayerForward
`GameTime_t` | m_flClientDeathTime
`bool` | m_bScreenTearFrameCaptured
`float32` | m_flFlashBangTime
`float32` | m_flFlashScreenshotAlpha
`float32` | m_flFlashOverlayAlpha
`bool` | m_bFlashBuildUp
`bool` | m_bFlashDspHasBeenCleared
`bool` | m_bFlashScreenshotHasBeenGrabbed
`float32` | m_flFlashMaxAlpha
`float32` | m_flFlashDuration
`int32` | m_iHealthBarRenderMaskIndex
`float32` | m_flHealthFadeValue
`float32` | m_flHealthFadeAlpha
`float32` | m_flDeathCCWeight
`float32` | m_flPrevRoundEndTime
`float32` | m_flPrevMatchEndTime
`QAngle` | m_angEyeAngles
`float32` | m_fNextThinkPushAway
`bool` | m_bShouldAutobuyDMWeapons
`bool` | m_bShouldAutobuyNow
`CEntityIndex` | m_iIDEntIndex
`CountdownTimer` | m_delayTargetIDTimer
`CEntityIndex` | m_iTargetItemEntIdx
`CEntityIndex` | m_iOldIDEntIndex
`CountdownTimer` | m_holdTargetIDTimer
`float32` | m_flCurrentMusicStartTime
`float32` | m_flMusicRoundStartTime
`bool` | m_bDeferStartMusicOnWarmup
`int32` | m_cycleLatch
`float32` | m_serverIntendedCycle
`float32` | m_flLastSmokeOverlayAlpha
`float32` | m_flLastSmokeAge
`Vector` | m_vLastSmokeOverlayColor
`ParticleIndex_t` | m_nPlayerSmokedFx
`ParticleIndex_t` | m_nPlayerInfernoBodyFx
`ParticleIndex_t` | m_nPlayerInfernoFootFx
`float32` | m_flNextMagDropTime
`int32` | m_nLastMagDropAttachmentIndex
`Vector` | m_vecLastAliveLocalVelocity
`bool` | m_bGuardianShouldSprayCustomXMark
`CHandle< CCSPlayerController >` | m_hOriginalController

---

## C_Item_Healthshot
Derived from: [C_WeaponBaseItem](#c_weaponbaseitem), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EnvWindShared

Type | Name
------------ | -------------
`GameTime_t` | m_flStartTime
`uint32` | m_iWindSeed
`uint16` | m_iMinWind
`uint16` | m_iMaxWind
`int32` | m_windRadius
`uint16` | m_iMinGust
`uint16` | m_iMaxGust
`float32` | m_flMinGustDelay
`float32` | m_flMaxGustDelay
`float32` | m_flGustDuration
`uint16` | m_iGustDirChange
`Vector` | m_location
`int32` | m_iszGustSound
`int32` | m_iWindDir
`float32` | m_flWindSpeed
`Vector` | m_currentWindVector
`Vector` | m_CurrentSwayVector
`Vector` | m_PrevSwayVector
`uint16` | m_iInitialWindDir
`float32` | m_flInitialWindSpeed
`GameTime_t` | m_flVariationTime
`GameTime_t` | m_flSwayTime
`GameTime_t` | m_flSimTime
`GameTime_t` | m_flSwitchTime
`float32` | m_flAveWindSpeed
`bool` | m_bGusting
`float32` | m_flWindAngleVariation
`float32` | m_flWindSpeedVariation
`CHandle< C_BaseEntity >` | m_hEntOwner

---

## C_PostProcessingVolume
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CStrongHandle< InfoForResourceTypeCPostProcessingResource >` | m_hPostSettings
`float32` | m_flFadeDuration
`float32` | m_flMinLogExposure
`float32` | m_flMaxLogExposure
`float32` | m_flMinExposure
`float32` | m_flMaxExposure
`float32` | m_flExposureCompensation
`float32` | m_flExposureFadeSpeedUp
`float32` | m_flExposureFadeSpeedDown
`float32` | m_flTonemapEVSmoothingRange
`bool` | m_bMaster
`bool` | m_bExposureControl
`float32` | m_flRate
`float32` | m_flTonemapPercentTarget
`float32` | m_flTonemapPercentBrightPixels
`float32` | m_flTonemapMinAvgLum

---

## CCSPlayer_PingServices


Type | Name
------------ | -------------
`CHandle< C_BaseEntity >` | m_hPlayerPing

---

## CPlayer_FlashlightServices


---

## CServerOnlyModelEntity
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_AttributeContainer
Derived from: [CAttributeManager](#cattributemanager)

Type | Name
------------ | -------------
`C_EconItemView` | m_Item
`int32` | m_iExternalItemProviderRegisteredToken
`uint64` | m_ullRegisteredAsItemID

---

## C_FuncRotating
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BaseFire
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flScale
`float32` | m_flStartScale
`float32` | m_flScaleTime
`uint32` | m_nFlags

---

## CBasePlayerController
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`int32` | m_nFinalPredictedTick
`C_CommandContext` | m_CommandContext
`uint64` | m_nInButtonsWhichAreToggles
`uint32` | m_nTickBase
`CHandle< C_BasePlayerPawn >` | m_hPawn
`bool` | m_bKnownTeamMismatch
`CHandle< C_BasePlayerPawn >` | m_hPredictedPawn
`CSplitScreenSlot` | m_nSplitScreenSlot
`CHandle< CBasePlayerController >` | m_hSplitOwner
`CUtlVector< CHandle< CBasePlayerController > >` | m_hSplitScreenPlayers
`bool` | m_bIsHLTV
`PlayerConnectedState` | m_iConnected
`char[128]` | m_iszPlayerName
`uint64` | m_steamID
`bool` | m_bIsLocalPlayerController
`uint32` | m_iDesiredFOV

---

## CPointTemplateAPI

---

## C_DecoyProjectile
Derived from: [C_BaseCSGrenadeProjectile](#c_basecsgrenadeprojectile), [C_BaseGrenade](#c_basegrenade), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`int32` | m_nDecoyShotTick
`int32` | m_nClientLastKnownDecoyShotTick
`GameTime_t` | m_flTimeParticleEffectSpawn

---

## C_WaterBullet
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_PreviewPlayer
Derived from: [C_CSPlayerPawn](#c_csplayerpawn), [C_CSPlayerPawnBase](#c_csplayerpawnbase), [C_BasePlayerPawn](#c_baseplayerpawn), [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CUtlString` | m_animgraph
`CGlobalSymbol` | m_animgraphCharacterModeString
`float32` | m_flInitialModelScale

---

## CBaseAnimGraphController


Type | Name
------------ | -------------
`CAnimGraphNetworkedVariables` | m_animGraphNetworkedVars
`bool` | m_bSequenceFinished
`float32` | m_flSoundSyncTime
`uint32` | m_nActiveIKChainMask
`HSequence` | m_hSequence
`GameTime_t` | m_flSeqStartTime
`float32` | m_flSeqFixedCycle
`AnimLoopMode_t` | m_nAnimLoopMode
`CNetworkedQuantizedFloat` | m_flPlaybackRate
`SequenceFinishNotifyState_t` | m_nNotifyState
`bool` | m_bNetworkedAnimationInputsChanged
`bool` | m_bNetworkedSequenceChanged
`bool` | m_bLastUpdateSkipped
`GameTime_t` | m_flPrevAnimUpdateTime

---

## CCSPointScriptEntity
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_C4
Derived from: [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`char[32]` | m_szScreenText
`ParticleIndex_t` | m_activeLightParticleIndex
`C4LightEffect_t` | m_eActiveLightEffect
`bool` | m_bStartedArming
`GameTime_t` | m_fArmedTime
`bool` | m_bBombPlacedAnimation
`bool` | m_bIsPlantingViaUse
`EntitySpottedState_t` | m_entitySpottedState
`int32` | m_nSpotRules
`bool[7]` | m_bPlayedArmingBeeps
`bool` | m_bBombPlanted

---

## CBaseAnimGraph
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bInitiallyPopulateInterpHistory
`bool` | m_bSuppressAnimEventSounds
`bool` | m_bAnimGraphUpdateEnabled
`float32` | m_flMaxSlopeDistance
`Vector` | m_vLastSlopeCheckPos
`bool` | m_bAnimationUpdateScheduled
`Vector` | m_vecForce
`int32` | m_nForceBone
`CBaseAnimGraph*` | m_pClientsideRagdoll
`bool` | m_bBuiltRagdoll
`PhysicsRagdollPose_t` | m_RagdollPose
`bool` | m_bRagdollClientSide
`bool` | m_bHasAnimatedMaterialAttributes

---

## C_PointEntity
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_MultiplayRules
Derived from: [C_GameRules](#c_gamerules)

---

## CBasePlayerControllerAPI

---

## C_PathParticleRope
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bStartActive
`float32` | m_flMaxSimulationTime
`CUtlSymbolLarge` | m_iszEffectName
`CUtlVector< CUtlSymbolLarge >` | m_PathNodes_Name
`float32` | m_flParticleSpacing
`float32` | m_flSlack
`float32` | m_flRadius
`Color` | m_ColorTint
`int32` | m_nEffectState
`CStrongHandle< InfoForResourceTypeIParticleSystemDefinition >` | m_iEffectIndex
`C_NetworkUtlVectorBase< Vector >` | m_PathNodes_Position
`C_NetworkUtlVectorBase< Vector >` | m_PathNodes_TangentIn
`C_NetworkUtlVectorBase< Vector >` | m_PathNodes_TangentOut
`C_NetworkUtlVectorBase< Vector >` | m_PathNodes_Color
`C_NetworkUtlVectorBase< bool >` | m_PathNodes_PinEnabled
`C_NetworkUtlVectorBase< float32 >` | m_PathNodes_RadiusScale

---

## CCSPointScriptExtensions_CCSWeaponBaseVData

---

## C_SoundEventAABBEntity
Derived from: [C_SoundEventEntity](#c_soundevententity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`Vector` | m_vMins
`Vector` | m_vMaxs

---

## C_WeaponP90
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CEnvSoundscapeAlias_snd_soundscape
Derived from: [CEnvSoundscape](#cenvsoundscape), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BasePlayerWeapon
Derived from: [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`GameTick_t` | m_nNextPrimaryAttackTick
`float32` | m_flNextPrimaryAttackTickRatio
`GameTick_t` | m_nNextSecondaryAttackTick
`float32` | m_flNextSecondaryAttackTickRatio
`int32` | m_iClip1
`int32` | m_iClip2
`int32[2]` | m_pReserveAmmo

---

## CBasePlayerWeaponVData


Type | Name
------------ | -------------
`CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >` | m_szWorldModel
`CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >` | m_sToolsOnlyOwnerModelName
`bool` | m_bBuiltRightHanded
`bool` | m_bAllowFlipping
`CAttachmentNameSymbolWithStorage` | m_sMuzzleAttachment
`CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >` | m_szMuzzleFlashParticle
`bool` | m_bLinkedCooldowns
`ItemFlagTypes_t` | m_iFlags
`AmmoIndex_t` | m_nPrimaryAmmoType
`AmmoIndex_t` | m_nSecondaryAmmoType
`int32` | m_iMaxClip1
`int32` | m_iMaxClip2
`int32` | m_iDefaultClip1
`int32` | m_iDefaultClip2
`bool` | m_bReserveAmmoAsClips
`int32` | m_iWeight
`bool` | m_bAutoSwitchTo
`bool` | m_bAutoSwitchFrom
`RumbleEffect_t` | m_iRumbleEffect
`int32` | m_iSlot
`int32` | m_iPosition
`CUtlOrderedMap< WeaponSound_t, CSoundEventName >` | m_aShootSounds

---

## C_Fish
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`Vector` | m_pos
`Vector` | m_vel
`QAngle` | m_angles
`int32` | m_localLifeState
`float32` | m_deathDepth
`float32` | m_deathAngle
`float32` | m_buoyancy
`CountdownTimer` | m_wiggleTimer
`float32` | m_wigglePhase
`float32` | m_wiggleRate
`Vector` | m_actualPos
`QAngle` | m_actualAngles
`Vector` | m_poolOrigin
`float32` | m_waterLevel
`bool` | m_gotUpdate
`float32` | m_x
`float32` | m_y
`float32` | m_z
`float32` | m_angle
`float32[20]` | m_errorHistory
`int32` | m_errorHistoryIndex
`int32` | m_errorHistoryCount
`float32` | m_averageError

---

## CTimeline
Derived from: [IntervalTimer](#intervaltimer)

Type | Name
------------ | -------------
`float32[64]` | m_flValues
`int32[64]` | m_nValueCounts
`int32` | m_nBucketCount
`float32` | m_flInterval
`float32` | m_flFinalValue
`TimelineCompression_t` | m_nCompressionType
`bool` | m_bStopped

---

## C_WeaponAWP
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BasePlayerPawn
Derived from: [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CPlayer_WeaponServices*` | m_pWeaponServices
`CPlayer_ItemServices*` | m_pItemServices
`CPlayer_AutoaimServices*` | m_pAutoaimServices
`CPlayer_ObserverServices*` | m_pObserverServices
`CPlayer_WaterServices*` | m_pWaterServices
`CPlayer_UseServices*` | m_pUseServices
`CPlayer_FlashlightServices*` | m_pFlashlightServices
`CPlayer_CameraServices*` | m_pCameraServices
`CPlayer_MovementServices*` | m_pMovementServices
`C_UtlVectorEmbeddedNetworkVar< ViewAngleServerChange_t >` | m_ServerViewAngleChanges
`uint32` | m_nHighestConsumedServerViewAngleChangeIndex
`QAngle` | v_angle
`QAngle` | v_anglePrevious
`uint32` | m_iHideHUD
`sky3dparams_t` | m_skybox3d
`GameTime_t` | m_flDeathTime
`Vector` | m_vecPredictionError
`GameTime_t` | m_flPredictionErrorTime
`Vector` | m_vecLastCameraSetupLocalOrigin
`GameTime_t` | m_flLastCameraSetupTime
`float32` | m_flFOVSensitivityAdjust
`float32` | m_flMouseSensitivity
`Vector` | m_vOldOrigin
`float32` | m_flOldSimulationTime
`int32` | m_nLastExecutedCommandNumber
`int32` | m_nLastExecutedCommandTick
`CHandle< CBasePlayerController >` | m_hController
`bool` | m_bIsSwappingToPredictableController

---

## CAttributeManager

Type | Name
------------ | -------------
`CUtlVector< CHandle< C_BaseEntity > >` | m_Providers
`int32` | m_iReapplyProvisionParity
`CHandle< C_BaseEntity >` | m_hOuter
`bool` | m_bPreventLoopback
`attributeprovidertypes_t` | m_ProviderType
`CUtlVector< CAttributeManager::cached_attribute_float_t >` | m_CachedResults

---

## CLogicalEntity
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CAnimGraphNetworkedVariables

Type | Name
------------ | -------------
`C_NetworkUtlVectorBase< uint32 >` | m_PredNetBoolVariables
`C_NetworkUtlVectorBase< uint8 >` | m_PredNetByteVariables
`C_NetworkUtlVectorBase< uint16 >` | m_PredNetUInt16Variables
`C_NetworkUtlVectorBase< int32 >` | m_PredNetIntVariables
`C_NetworkUtlVectorBase< uint32 >` | m_PredNetUInt32Variables
`C_NetworkUtlVectorBase< uint64 >` | m_PredNetUInt64Variables
`C_NetworkUtlVectorBase< float32 >` | m_PredNetFloatVariables
`C_NetworkUtlVectorBase< Vector >` | m_PredNetVectorVariables
`C_NetworkUtlVectorBase< Quaternion >` | m_PredNetQuaternionVariables
`C_NetworkUtlVectorBase< CGlobalSymbol >` | m_PredNetGlobalSymbolVariables
`C_NetworkUtlVectorBase< uint32 >` | m_OwnerOnlyPredNetBoolVariables
`C_NetworkUtlVectorBase< uint8 >` | m_OwnerOnlyPredNetByteVariables
`C_NetworkUtlVectorBase< uint16 >` | m_OwnerOnlyPredNetUInt16Variables
`C_NetworkUtlVectorBase< int32 >` | m_OwnerOnlyPredNetIntVariables
`C_NetworkUtlVectorBase< uint32 >` | m_OwnerOnlyPredNetUInt32Variables
`C_NetworkUtlVectorBase< uint64 >` | m_OwnerOnlyPredNetUInt64Variables
`C_NetworkUtlVectorBase< float32 >` | m_OwnerOnlyPredNetFloatVariables
`C_NetworkUtlVectorBase< Vector >` | m_OwnerOnlyPredNetVectorVariables
`C_NetworkUtlVectorBase< Quaternion >` | m_OwnerOnlyPredNetQuaternionVariables
`C_NetworkUtlVectorBase< CGlobalSymbol >` | m_OwnerOnlyPredNetGlobalSymbolVariables
`int32` | m_nBoolVariablesCount
`int32` | m_nOwnerOnlyBoolVariablesCount
`int32` | m_nRandomSeedOffset
`float32` | m_flLastTeleportTime

---

## C_TriggerBuoyancy
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CBuoyancyHelper` | m_BuoyancyHelper
`float32` | m_flFluidDensity

---

## C_RopeKeyframe
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CBitVec< 10 >` | m_LinksTouchingSomething
`int32` | m_nLinksTouchingSomething
`bool` | m_bApplyWind
`int32` | m_fPrevLockedPoints
`int32` | m_iForcePointMoveCounter
`bool[2]` | m_bPrevEndPointPos
`Vector[2]` | m_vPrevEndPointPos
`float32` | m_flCurScroll
`float32` | m_flScrollSpeed
`uint16` | m_RopeFlags
`CStrongHandle< InfoForResourceTypeIMaterial2 >` | m_iRopeMaterialModelIndex
`Vector[10]` | m_LightValues
`uint8` | m_nSegments
`CHandle< C_BaseEntity >` | m_hStartPoint
`CHandle< C_BaseEntity >` | m_hEndPoint
`AttachmentHandle_t` | m_iStartAttachment
`AttachmentHandle_t` | m_iEndAttachment
`uint8` | m_Subdiv
`int16` | m_RopeLength
`int16` | m_Slack
`float32` | m_TextureScale
`uint8` | m_fLockedPoints
`uint8` | m_nChangeCount
`float32` | m_Width
`C_RopeKeyframe::CPhysicsDelegate` | m_PhysicsDelegate
`CStrongHandle< InfoForResourceTypeIMaterial2 >` | m_hMaterial
`int32` | m_TextureHeight
`Vector` | m_vecImpulse
`Vector` | m_vecPreviousImpulse
`float32` | m_flCurrentGustTimer
`float32` | m_flCurrentGustLifetime
`float32` | m_flTimeToNextGust
`Vector` | m_vWindDir
`Vector` | m_vColorMod
`Vector[2]` | m_vCachedEndPointAttachmentPos
`QAngle[2]` | m_vCachedEndPointAttachmentAngle
`bool` | m_bConstrainBetweenEndpoints
`bitfield:1` | m_bEndPointAttachmentPositionsDirty
`bitfield:1` | m_bEndPointAttachmentAnglesDirty
`bitfield:1` | m_bNewDataThisFrame
`bitfield:1` | m_bPhysicsInitted

---

## C_GradientFog
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_hGradientFogTexture
`float32` | m_flFogStartDistance
`float32` | m_flFogEndDistance
`bool` | m_bHeightFogEnabled
`float32` | m_flFogStartHeight
`float32` | m_flFogEndHeight
`float32` | m_flFarZ
`float32` | m_flFogMaxOpacity
`float32` | m_flFogFalloffExponent
`float32` | m_flFogVerticalExponent
`Color` | m_fogColor
`float32` | m_flFogStrength
`float32` | m_flFadeTime
`bool` | m_bStartDisabled
`bool` | m_bIsEnabled
`bool` | m_bGradientFogNeedsTextures

---

## EntitySpottedState_t

Type | Name
------------ | -------------
`bool` | m_bSpotted
`uint32[2]` | m_bSpottedByMask

---

## C_CSGO_TeamPreviewCamera
Derived from: [C_CSGO_MapPreviewCameraPath](#c_csgo_mappreviewcamerapath), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`int32` | m_nVariant
`bool` | m_bDofEnabled
`float32` | m_flDofNearBlurry
`float32` | m_flDofNearCrisp
`float32` | m_flDofFarCrisp
`float32` | m_flDofFarBlurry
`float32` | m_flDofTiltToGround

---

## CCSPlayer_CameraServices
Derived from: [CCSPlayerBase_CameraServices](#ccsplayerbase_cameraservices), [CPlayer_CameraServices](#cplayer_cameraservices)

Type | Name
------------ | -------------
`float32` | m_flDeathCamTilt
`Vector` | m_vClientScopeInaccuracy

---

## C_CSGO_TeamSelectCounterTerroristPosition
Derived from: [C_CSGO_TeamSelectCharacterPosition](#c_csgo_teamselectcharacterposition), [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EconWearable
Derived from: [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`int32` | m_nForceSkin
`bool` | m_bAlwaysAllow

---

## CCSGO_WingmanIntroCharacterPosition
Derived from: [C_CSGO_TeamIntroCharacterPosition](#c_csgo_teamintrocharacterposition), [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CSMatchStats_t
Derived from: [CSPerRoundStats_t](#csperroundstats_t)

Type | Name
------------ | -------------
`int32` | m_iEnemy5Ks
`int32` | m_iEnemy4Ks
`int32` | m_iEnemy3Ks
`int32` | m_iEnemyKnifeKills
`int32` | m_iEnemyTaserKills

---

## C_BaseToggle
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EnvVolumetricFogVolume
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bActive
`Vector` | m_vBoxMins
`Vector` | m_vBoxMaxs
`bool` | m_bStartDisabled
`float32` | m_flStrength
`int32` | m_nFalloffShape
`float32` | m_flFalloffExponent
`float32` | m_flHeightFogDepth
`float32` | m_fHeightFogEdgeWidth
`float32` | m_fIndirectLightStrength
`float32` | m_fSunLightStrength
`float32` | m_fNoiseStrength
`bool` | m_bOverrideIndirectLightStrength
`bool` | m_bOverrideSunLightStrength
`bool` | m_bOverrideNoiseStrength
`bool` | m_bAllowLPVIndirect

---

## CWaterSplasher
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_ModelPointEntity
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSObserver_ViewModelServices
Derived from: [CPlayer_ViewModelServices](#cplayer_viewmodelservices)

---

## C_FireSmoke
Derived from: [C_BaseFire](#c_basefire), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`int32` | m_nFlameModelIndex
`int32` | m_nFlameFromAboveModelIndex
`float32` | m_flScaleRegister
`float32` | m_flScaleStart
`float32` | m_flScaleEnd
`GameTime_t` | m_flScaleTimeStart
`GameTime_t` | m_flScaleTimeEnd
`float32` | m_flChildFlameSpread
`float32` | m_flClipPerc
`bool` | m_bClipTested
`bool` | m_bFadingOut
`TimedEvent` | m_tParticleSpawn
`CFireOverlay*` | m_pFireOverlay

---

## C_WeaponRevolver
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_FireFromAboveSprite
Derived from: [C_Sprite](#c_sprite), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EnvCombinedLightProbeVolume
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`Color` | m_Entity_Color
`float32` | m_Entity_flBrightness
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_Entity_hCubemapTexture
`bool` | m_Entity_bCustomCubemapTexture
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_Entity_hLightProbeTexture
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_Entity_hLightProbeDirectLightIndicesTexture
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_Entity_hLightProbeDirectLightScalarsTexture
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_Entity_hLightProbeDirectLightShadowsTexture
`Vector` | m_Entity_vBoxMins
`Vector` | m_Entity_vBoxMaxs
`bool` | m_Entity_bMoveable
`int32` | m_Entity_nHandshake
`int32` | m_Entity_nEnvCubeMapArrayIndex
`int32` | m_Entity_nPriority
`bool` | m_Entity_bStartDisabled
`float32` | m_Entity_flEdgeFadeDist
`Vector` | m_Entity_vEdgeFadeDists
`int32` | m_Entity_nLightProbeSizeX
`int32` | m_Entity_nLightProbeSizeY
`int32` | m_Entity_nLightProbeSizeZ
`int32` | m_Entity_nLightProbeAtlasX
`int32` | m_Entity_nLightProbeAtlasY
`int32` | m_Entity_nLightProbeAtlasZ
`bool` | m_Entity_bEnabled

---

## C_SoundOpvarSetOBBWindEntity
Derived from: [C_SoundOpvarSetPointBase](#c_soundopvarsetpointbase), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## ActiveModelConfig_t

Type | Name
------------ | -------------
`ModelConfigHandle_t` | m_Handle
`CUtlSymbolLarge` | m_Name
`C_NetworkUtlVectorBase< CHandle< C_BaseModelEntity > >` | m_AssociatedEntities
`C_NetworkUtlVectorBase< CUtlSymbolLarge >` | m_AssociatedEntityNames

---

## C_WeaponMP5SD
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_DynamicPropAlias_dynamic_prop
Derived from: [C_DynamicProp](#c_dynamicprop), [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPlayer_BulletServices


Type | Name
------------ | -------------
`int32` | m_totalHitsOnServer

---

## CLogicRelay
Derived from: [CLogicalEntity](#clogicalentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CEntityIOOutput` | m_OnTrigger
`CEntityIOOutput` | m_OnSpawn
`bool` | m_bDisabled
`bool` | m_bWaitForRefire
`bool` | m_bTriggerOnce
`bool` | m_bFastRetrigger
`bool` | m_bPassthoughCaller

---

## C_PointCameraVFOV
Derived from: [C_PointCamera](#c_pointcamera), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flVerticalFOV

---

## CCSPlayer_ItemServices
Derived from: [CPlayer_ItemServices](#cplayer_itemservices)

Type | Name
------------ | -------------
`bool` | m_bHasDefuser
`bool` | m_bHasHelmet
`bool` | m_bHasHeavyArmor

---

## C_BarnLight
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bEnabled
`int32` | m_nColorMode
`Color` | m_Color
`float32` | m_flColorTemperature
`float32` | m_flBrightness
`float32` | m_flBrightnessScale
`int32` | m_nDirectLight
`int32` | m_nBakedShadowIndex
`int32` | m_nLuminaireShape
`float32` | m_flLuminaireSize
`float32` | m_flLuminaireAnisotropy
`CUtlString` | m_LightStyleString
`GameTime_t` | m_flLightStyleStartTime
`C_NetworkUtlVectorBase< CUtlString >` | m_QueuedLightStyleStrings
`C_NetworkUtlVectorBase< CUtlString >` | m_LightStyleEvents
`C_NetworkUtlVectorBase< CHandle< C_BaseModelEntity > >` | m_LightStyleTargets
`CEntityIOOutput[4]` | m_StyleEvent
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_hLightCookie
`float32` | m_flShape
`float32` | m_flSoftX
`float32` | m_flSoftY
`float32` | m_flSkirt
`float32` | m_flSkirtNear
`Vector` | m_vSizeParams
`float32` | m_flRange
`Vector` | m_vShear
`int32` | m_nBakeSpecularToCubemaps
`Vector` | m_vBakeSpecularToCubemapsSize
`int32` | m_nCastShadows
`int32` | m_nShadowMapSize
`int32` | m_nShadowPriority
`bool` | m_bContactShadow
`int32` | m_nBounceLight
`float32` | m_flBounceScale
`float32` | m_flMinRoughness
`Vector` | m_vAlternateColor
`float32` | m_fAlternateColorBrightness
`int32` | m_nFog
`float32` | m_flFogStrength
`int32` | m_nFogShadows
`float32` | m_flFogScale
`bool` | m_bFogMixedShadows
`float32` | m_flFadeSizeStart
`float32` | m_flFadeSizeEnd
`float32` | m_flShadowFadeSizeStart
`float32` | m_flShadowFadeSizeEnd
`bool` | m_bPrecomputedFieldsValid
`Vector` | m_vPrecomputedBoundsMins
`Vector` | m_vPrecomputedBoundsMaxs
`Vector` | m_vPrecomputedOBBOrigin
`QAngle` | m_vPrecomputedOBBAngles
`Vector` | m_vPrecomputedOBBExtent
`int32` | m_nPrecomputedSubFrusta
`Vector` | m_vPrecomputedOBBOrigin0
`QAngle` | m_vPrecomputedOBBAngles0
`Vector` | m_vPrecomputedOBBExtent0
`Vector` | m_vPrecomputedOBBOrigin1
`QAngle` | m_vPrecomputedOBBAngles1
`Vector` | m_vPrecomputedOBBExtent1
`Vector` | m_vPrecomputedOBBOrigin2
`QAngle` | m_vPrecomputedOBBAngles2
`Vector` | m_vPrecomputedOBBExtent2
`Vector` | m_vPrecomputedOBBOrigin3
`QAngle` | m_vPrecomputedOBBAngles3
`Vector` | m_vPrecomputedOBBExtent3
`Vector` | m_vPrecomputedOBBOrigin4
`QAngle` | m_vPrecomputedOBBAngles4
`Vector` | m_vPrecomputedOBBExtent4
`Vector` | m_vPrecomputedOBBOrigin5
`QAngle` | m_vPrecomputedOBBAngles5
`Vector` | m_vPrecomputedOBBExtent5
`bool` | m_bInitialBoneSetup
`C_NetworkUtlVectorBase< uint16 >` | m_VisClusters

---

## C_TonemapController2
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flAutoExposureMin
`float32` | m_flAutoExposureMax
`float32` | m_flTonemapPercentTarget
`float32` | m_flTonemapPercentBrightPixels
`float32` | m_flTonemapMinAvgLum
`float32` | m_flExposureAdaptationSpeedUp
`float32` | m_flExposureAdaptationSpeedDown
`float32` | m_flTonemapEVSmoothingRange

---

## C_WeaponG3SG1
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CFuncWater
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CBuoyancyHelper` | m_BuoyancyHelper

---

## C_SoundOpvarSetAutoRoomEntity
Derived from: [C_SoundOpvarSetPointEntity](#c_soundopvarsetpointentity), [C_SoundOpvarSetPointBase](#c_soundopvarsetpointbase), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EconEntity
Derived from: [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flFlexDelayTime
`float32*` | m_flFlexDelayedWeight
`bool` | m_bAttributesInitialized
`C_AttributeContainer` | m_AttributeManager
`uint32` | m_OriginalOwnerXuidLow
`uint32` | m_OriginalOwnerXuidHigh
`int32` | m_nFallbackPaintKit
`int32` | m_nFallbackSeed
`float32` | m_flFallbackWear
`int32` | m_nFallbackStatTrak
`bool` | m_bClientside
`bool` | m_bParticleSystemsCreated
`CUtlVector< int32 >` | m_vecAttachedParticles
`CHandle< CBaseAnimGraph >` | m_hViewmodelAttachment
`int32` | m_iOldTeam
`bool` | m_bAttachmentDirty
`int32` | m_nUnloadedModelIndex
`int32` | m_iNumOwnerValidationRetries
`CHandle< C_BaseEntity >` | m_hOldProvidee
`CUtlVector< C_EconEntity::AttachedModelData_t >` | m_vecAttachedModels

---

## C_WeaponSG556
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_RectLight
Derived from: [C_BarnLight](#c_barnlight), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bShowLight

---

## C_ParticleSystem
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`char[512]` | m_szSnapshotFileName
`bool` | m_bActive
`bool` | m_bFrozen
`float32` | m_flFreezeTransitionDuration
`int32` | m_nStopType
`bool` | m_bAnimateDuringGameplayPause
`CStrongHandle< InfoForResourceTypeIParticleSystemDefinition >` | m_iEffectIndex
`GameTime_t` | m_flStartTime
`float32` | m_flPreSimTime
`Vector[4]` | m_vServerControlPoints
`uint8[4]` | m_iServerControlPointAssignments
`CHandle< C_BaseEntity >[64]` | m_hControlPointEnts
`bool` | m_bNoSave
`bool` | m_bNoFreeze
`bool` | m_bNoRamp
`bool` | m_bStartActive
`CUtlSymbolLarge` | m_iszEffectName
`CUtlSymbolLarge[64]` | m_iszControlPointNames
`int32` | m_nDataCP
`Vector` | m_vecDataCPValue
`int32` | m_nTintCP
`Color` | m_clrTint
`bool` | m_bOldActive
`bool` | m_bOldFrozen

---

## C_CSGO_TeamPreviewModel
Derived from: [C_CSGO_PreviewPlayer](#c_csgo_previewplayer), [C_CSPlayerPawn](#c_csplayerpawn), [C_CSPlayerPawnBase](#c_csplayerpawnbase), [C_BasePlayerPawn](#c_baseplayerpawn), [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WeaponGlock
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CEnvSoundscapeTriggerableAlias_snd_soundscape_triggerable
Derived from: [CEnvSoundscapeTriggerable](#cenvsoundscapetriggerable), [CEnvSoundscape](#cenvsoundscape), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGameRulesProxy
Derived from: [C_GameRulesProxy](#c_gamerulesproxy), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`C_CSGameRules*` | m_pGameRules

---

## CPlayer_ObserverServices


Type | Name
------------ | -------------
`uint8` | m_iObserverMode
`CHandle< C_BaseEntity >` | m_hObserverTarget
`ObserverMode_t` | m_iObserverLastMode
`bool` | m_bForcedObserverMode
`float32` | m_flObserverChaseDistance
`GameTime_t` | m_flObserverChaseDistanceCalcTime

---

## CPlayer_WaterServices


---

## C_CSGO_EndOfMatchLineupEnd
Derived from: [C_CSGO_EndOfMatchLineupEndpoint](#c_csgo_endofmatchlineupendpoint), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## SequenceHistory_t

Type | Name
------------ | -------------
`HSequence` | m_hSequence
`GameTime_t` | m_flSeqStartTime
`float32` | m_flSeqFixedCycle
`AnimLoopMode_t` | m_nSeqLoopMode
`float32` | m_flPlaybackRate
`float32` | m_flCyclesPerSecond

---

## C_Multimeter
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CHandle< C_PlantedC4 >` | m_hTargetC4

---

## C_CsmFovOverride
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CUtlString` | m_cameraName
`float32` | m_flCsmFovOverrideValue

---

## C_EnvDecal
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CStrongHandle< InfoForResourceTypeIMaterial2 >` | m_hDecalMaterial
`float32` | m_flWidth
`float32` | m_flHeight
`float32` | m_flDepth
`uint32` | m_nRenderOrder
`bool` | m_bProjectOnWorld
`bool` | m_bProjectOnCharacters
`bool` | m_bProjectOnWater
`float32` | m_flDepthSortBias

---

## CCSGameModeRules_Noop
Derived from: [CCSGameModeRules](#ccsgamemoderules)

---

## C_ColorCorrection
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`Vector` | m_vecOrigin
`float32` | m_MinFalloff
`float32` | m_MaxFalloff
`float32` | m_flFadeInDuration
`float32` | m_flFadeOutDuration
`float32` | m_flMaxWeight
`float32` | m_flCurWeight
`char[512]` | m_netlookupFilename
`bool` | m_bEnabled
`bool` | m_bMaster
`bool` | m_bClientSide
`bool` | m_bExclusive
`bool[1]` | m_bEnabledOnClient
`float32[1]` | m_flCurWeightOnClient
`bool[1]` | m_bFadingIn
`float32[1]` | m_flFadeStartWeight
`float32[1]` | m_flFadeStartTime
`float32[1]` | m_flFadeDuration

---

## CHostageRescueZoneShim
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CModelState

Type | Name
------------ | -------------
`CStrongHandle< InfoForResourceTypeCModel >` | m_hModel
`CUtlSymbolLarge` | m_ModelName
`bool` | m_bClientClothCreationSuppressed
`uint64` | m_MeshGroupMask
`int8` | m_nIdealMotionType
`int8` | m_nForceLOD
`int8` | m_nClothUpdateFlags

---

## C_WeaponP250
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EconEntity::AttachedModelData_t

Type | Name
------------ | -------------
`int32` | m_iModelDisplayFlags

---

## CAttributeList

Type | Name
------------ | -------------
`C_UtlVectorEmbeddedNetworkVar< CEconItemAttribute >` | m_Attributes
`CAttributeManager*` | m_pManager

---

## C_TeamplayRules
Derived from: [C_MultiplayRules](#c_multiplayrules), [C_GameRules](#c_gamerules)

---

## C_CSGO_CounterTerroristWingmanIntroCamera
Derived from: [C_CSGO_TeamPreviewCamera](#c_csgo_teampreviewcamera), [C_CSGO_MapPreviewCameraPath](#c_csgo_mappreviewcamerapath), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WeaponNOVA
Derived from: [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_HEGrenadeProjectile
Derived from: [C_BaseCSGrenadeProjectile](#c_basecsgrenadeprojectile), [C_BaseGrenade](#c_basegrenade), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BaseDoor
Derived from: [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bIsUsable

---

## CGrenadeTracer
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flTracerDuration
`GrenadeType_t` | m_nType

---

## CBombTarget
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bBombPlantedHere

---

## C_PointClientUIDialog
Derived from: [C_BaseClientUIEntity](#c_baseclientuientity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CHandle< C_BaseEntity >` | m_hActivator
`bool` | m_bStartEnabled

---

## CCSGameModeRules_ArmsRace
Derived from: [CCSGameModeRules](#ccsgamemoderules)

Type | Name
------------ | -------------
`C_NetworkUtlVectorBase< CUtlString >` | m_WeaponSequence

---

## CPointChildModifier
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bOrphanInsteadOfDeletingChildrenOnRemove

---

## CDamageRecord

Type | Name
------------ | -------------
`CHandle< C_CSPlayerPawn >` | m_PlayerDamager
`CHandle< C_CSPlayerPawn >` | m_PlayerRecipient
`CHandle< CCSPlayerController >` | m_hPlayerControllerDamager
`CHandle< CCSPlayerController >` | m_hPlayerControllerRecipient
`CUtlString` | m_szPlayerDamagerName
`CUtlString` | m_szPlayerRecipientName
`uint64` | m_DamagerXuid
`uint64` | m_RecipientXuid
`int32` | m_iBulletsDamage
`int32` | m_iDamage
`int32` | m_iActualHealthRemoved
`int32` | m_iNumHits
`int32` | m_iLastBulletUpdate
`bool` | m_bIsOtherEnemy
`EKillTypes_t` | m_killType

---

## C_InfoLadderDismount
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPlayerController_DamageServices


Type | Name
------------ | -------------
`int32` | m_nSendUpdate
`C_UtlVectorEmbeddedNetworkVar< CDamageRecord >` | m_DamageList

---

## CRenderComponent
Derived from: [CEntityComponent](#centitycomponent)

Type | Name
------------ | -------------
`CNetworkVarChainer` | __m_pChainEntity
`bool` | m_bIsRenderingWithViewModels
`uint32` | m_nSplitscreenFlags
`bool` | m_bEnableRendering
`bool` | m_bInterpolationReadyToDraw

---

## CEnvSoundscapeProxy
Derived from: [CEnvSoundscape](#cenvsoundscape), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CUtlSymbolLarge` | m_MainSoundscapeName

---

## C_SoundEventOBBEntity
Derived from: [C_SoundEventEntity](#c_soundevententity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`Vector` | m_vMins
`Vector` | m_vMaxs

---

## CLightComponent
Derived from: [CEntityComponent](#centitycomponent)

Type | Name
------------ | -------------
`CNetworkVarChainer` | __m_pChainEntity
`Color` | m_Color
`Color` | m_SecondaryColor
`float32` | m_flBrightness
`float32` | m_flBrightnessScale
`float32` | m_flBrightnessMult
`float32` | m_flRange
`float32` | m_flFalloff
`float32` | m_flAttenuation0
`float32` | m_flAttenuation1
`float32` | m_flAttenuation2
`float32` | m_flTheta
`float32` | m_flPhi
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_hLightCookie
`int32` | m_nCascades
`int32` | m_nCastShadows
`int32` | m_nShadowWidth
`int32` | m_nShadowHeight
`bool` | m_bRenderDiffuse
`int32` | m_nRenderSpecular
`bool` | m_bRenderTransmissive
`float32` | m_flOrthoLightWidth
`float32` | m_flOrthoLightHeight
`int32` | m_nStyle
`CUtlString` | m_Pattern
`int32` | m_nCascadeRenderStaticObjects
`float32` | m_flShadowCascadeCrossFade
`float32` | m_flShadowCascadeDistanceFade
`float32` | m_flShadowCascadeDistance0
`float32` | m_flShadowCascadeDistance1
`float32` | m_flShadowCascadeDistance2
`float32` | m_flShadowCascadeDistance3
`int32` | m_nShadowCascadeResolution0
`int32` | m_nShadowCascadeResolution1
`int32` | m_nShadowCascadeResolution2
`int32` | m_nShadowCascadeResolution3
`bool` | m_bUsesBakedShadowing
`int32` | m_nShadowPriority
`int32` | m_nBakedShadowIndex
`bool` | m_bRenderToCubemaps
`int32` | m_nDirectLight
`int32` | m_nIndirectLight
`float32` | m_flFadeMinDist
`float32` | m_flFadeMaxDist
`float32` | m_flShadowFadeMinDist
`float32` | m_flShadowFadeMaxDist
`bool` | m_bEnabled
`bool` | m_bFlicker
`bool` | m_bPrecomputedFieldsValid
`Vector` | m_vPrecomputedBoundsMins
`Vector` | m_vPrecomputedBoundsMaxs
`Vector` | m_vPrecomputedOBBOrigin
`QAngle` | m_vPrecomputedOBBAngles
`Vector` | m_vPrecomputedOBBExtent
`float32` | m_flPrecomputedMaxRange
`int32` | m_nFogLightingMode
`float32` | m_flFogContributionStength
`float32` | m_flNearClipPlane
`Color` | m_SkyColor
`float32` | m_flSkyIntensity
`Color` | m_SkyAmbientBounce
`bool` | m_bUseSecondaryColor
`bool` | m_bMixedShadows
`GameTime_t` | m_flLightStyleStartTime
`float32` | m_flCapsuleLength
`float32` | m_flMinRoughness

---

## C_CSGO_CounterTerroristTeamIntroCamera
Derived from: [C_CSGO_TeamPreviewCamera](#c_csgo_teampreviewcamera), [C_CSGO_MapPreviewCameraPath](#c_csgo_mappreviewcamerapath), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CEntityComponent

---

## C_EconItemView


Type | Name
------------ | -------------
`bool` | m_bInventoryImageRgbaRequested
`bool` | m_bInventoryImageTriedCache
`int32` | m_nInventoryImageRgbaWidth
`int32` | m_nInventoryImageRgbaHeight
`char[260]` | m_szCurrentLoadCachedFileName
`bool` | m_bRestoreCustomMaterialAfterPrecache
`uint16` | m_iItemDefinitionIndex
`int32` | m_iEntityQuality
`uint32` | m_iEntityLevel
`uint64` | m_iItemID
`uint32` | m_iItemIDHigh
`uint32` | m_iItemIDLow
`uint32` | m_iAccountID
`uint32` | m_iInventoryPosition
`bool` | m_bInitialized
`bool` | m_bDisallowSOC
`bool` | m_bIsStoreItem
`bool` | m_bIsTradeItem
`int32` | m_iEntityQuantity
`int32` | m_iRarityOverride
`int32` | m_iQualityOverride
`int32` | m_iOriginOverride
`uint8` | m_unClientFlags
`uint8` | m_unOverrideStyle
`CAttributeList` | m_AttributeList
`CAttributeList` | m_NetworkedDynamicAttributes
`char[161]` | m_szCustomName
`char[161]` | m_szCustomNameOverride
`bool` | m_bInitializedTags

---

## C_HandleTest
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CHandle< C_BaseEntity >` | m_Handle
`bool` | m_bSendHandle

---

## C_EnvWindClientside
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`C_EnvWindShared` | m_EnvWindShared

---

## C_WeaponMAC10
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_PointClientUIWorldTextPanel
Derived from: [C_PointClientUIWorldPanel](#c_pointclientuiworldpanel), [C_BaseClientUIEntity](#c_baseclientuientity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`char[512]` | m_messageText

---

## CCSPlayer_UseServices
Derived from: [CPlayer_UseServices](#cplayer_useservices)

---

## CPlayer_MovementServices


Type | Name
------------ | -------------
`int32` | m_nImpulse
`CInButtonState` | m_nButtons
`uint64` | m_nQueuedButtonDownMask
`uint64` | m_nQueuedButtonChangeMask
`uint64` | m_nButtonDoublePressed
`uint32[64]` | m_pButtonPressedCmdNumber
`uint32` | m_nLastCommandNumberProcessed
`uint64` | m_nToggleButtonDownMask
`float32` | m_flMaxspeed
`float32[4]` | m_arrForceSubtickMoveWhen
`float32` | m_flForwardMove
`float32` | m_flLeftMove
`float32` | m_flUpMove
`Vector` | m_vecLastMovementImpulses
`QAngle` | m_vecOldViewAngles

---

## CEnvSoundscape
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CEntityIOOutput` | m_OnPlay
`float32` | m_flRadius
`CUtlSymbolLarge` | m_soundEventName
`bool` | m_bOverrideWithEvent
`int32` | m_soundscapeIndex
`int32` | m_soundscapeEntityListId
`CUtlSymbolLarge[8]` | m_positionNames
`CHandle< CEnvSoundscape >` | m_hProxySoundscape
`bool` | m_bDisabled
`CUtlSymbolLarge` | m_soundscapeName
`uint32` | m_soundEventHash

---

## CBasePlayerVData


Type | Name
------------ | -------------
`CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >` | m_sModelName
`CSkillFloat` | m_flHeadDamageMultiplier
`CSkillFloat` | m_flChestDamageMultiplier
`CSkillFloat` | m_flStomachDamageMultiplier
`CSkillFloat` | m_flArmDamageMultiplier
`CSkillFloat` | m_flLegDamageMultiplier
`float32` | m_flHoldBreathTime
`float32` | m_flDrowningDamageInterval
`int32` | m_nDrowningDamageInitial
`int32` | m_nDrowningDamageMax
`int32` | m_nWaterSpeed
`float32` | m_flUseRange
`float32` | m_flUseAngleTolerance
`float32` | m_flCrouchTime

---

## CCSPlayerController_InGameMoneyServices


Type | Name
------------ | -------------
`int32` | m_iAccount
`int32` | m_iStartAccount
`int32` | m_iTotalCashSpent
`int32` | m_iCashSpentThisRound

---

## C_EnvWindShared::WindVariationEvent_t

Type | Name
------------ | -------------
`float32` | m_flWindAngleVariation
`float32` | m_flWindSpeedVariation

---

## C_WeaponUSPSilencer
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CSpriteOriented
Derived from: [C_Sprite](#c_sprite), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_EndOfMatchLineupStart
Derived from: [C_CSGO_EndOfMatchLineupEndpoint](#c_csgo_endofmatchlineupendpoint), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WeaponFamas
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EnvParticleGlow
Derived from: [C_ParticleSystem](#c_particlesystem), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flAlphaScale
`float32` | m_flRadiusScale
`float32` | m_flSelfIllumScale
`Color` | m_ColorTint
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_hTextureOverride

---

## C_SoundEventEntity
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bStartOnSpawn
`bool` | m_bToLocalPlayer
`bool` | m_bStopOnNew
`bool` | m_bSaveRestore
`bool` | m_bSavedIsPlaying
`float32` | m_flSavedElapsedTime
`CUtlSymbolLarge` | m_iszSourceEntityName
`CUtlSymbolLarge` | m_iszAttachmentName
`CEntityOutputTemplate< uint64 >` | m_onGUIDChanged
`CEntityIOOutput` | m_onSoundFinished
`float32` | m_flClientCullRadius
`CUtlSymbolLarge` | m_iszSoundName
`CEntityHandle` | m_hSource
`int32` | m_nEntityIndexSelection
`bitfield:1` | m_bClientSideOnly

---

## C_CSGO_TeamIntroCharacterPosition
Derived from: [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_PreviewModelAlias_csgo_item_previewmodel
Derived from: [C_CSGO_PreviewModel](#c_csgo_previewmodel), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_Sun
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`ParticleIndex_t` | m_fxSSSunFlareEffectIndex
`ParticleIndex_t` | m_fxSunFlareEffectIndex
`float32` | m_fdistNormalize
`Vector` | m_vSunPos
`Vector` | m_vDirection
`CUtlSymbolLarge` | m_iszEffectName
`CUtlSymbolLarge` | m_iszSSEffectName
`Color` | m_clrOverlay
`bool` | m_bOn
`bool` | m_bmaxColor
`float32` | m_flSize
`float32` | m_flHazeScale
`float32` | m_flRotation
`float32` | m_flHDRColorScale
`float32` | m_flAlphaHaze
`float32` | m_flAlphaScale
`float32` | m_flAlphaHdr
`float32` | m_flFarZScale

---

## C_CSGO_EndOfMatchLineupEndpoint
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPlayerController_ActionTrackingServices


Type | Name
------------ | -------------
`C_UtlVectorEmbeddedNetworkVar< CSPerRoundStats_t >` | m_perRoundStats
`CSMatchStats_t` | m_matchStats
`int32` | m_iNumRoundKills
`int32` | m_iNumRoundKillsHeadshots
`uint32` | m_unTotalRoundDamageDealt

---

## CHitboxComponent
Derived from: [CEntityComponent](#centitycomponent)

Type | Name
------------ | -------------
`uint32[1]` | m_bvDisabledHitGroups

---

## C_ColorCorrectionVolume
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_LastEnterWeight
`float32` | m_LastEnterTime
`float32` | m_LastExitWeight
`float32` | m_LastExitTime
`bool` | m_bEnabled
`float32` | m_MaxWeight
`float32` | m_FadeDuration
`float32` | m_Weight
`char[512]` | m_lookupFilename

---

## C_PrecipitationBlocker
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BulletHitModel
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`matrix3x4_t` | m_matLocal
`int32` | m_iBoneIndex
`CHandle< C_BaseEntity >` | m_hPlayerParent
`bool` | m_bIsHit
`float32` | m_flTimeCreated
`Vector` | m_vecStartPos

---

## C_MapVetoPickController
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`int32` | m_nDraftType
`int32` | m_nTeamWinningCoinToss
`int32[64]` | m_nTeamWithFirstChoice
`int32[7]` | m_nVoteMapIdsList
`int32[64]` | m_nAccountIDs
`int32[64]` | m_nMapId0
`int32[64]` | m_nMapId1
`int32[64]` | m_nMapId2
`int32[64]` | m_nMapId3
`int32[64]` | m_nMapId4
`int32[64]` | m_nMapId5
`int32[64]` | m_nStartingSide0
`int32` | m_nCurrentPhase
`int32` | m_nPhaseStartTick
`int32` | m_nPhaseDurationTicks
`int32` | m_nPostDataUpdateTick
`bool` | m_bDisabledHud

---

## CSharedGapTypeQueryRegistration

---

## C_OmniLight
Derived from: [C_BarnLight](#c_barnlight), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flInnerAngle
`float32` | m_flOuterAngle
`bool` | m_bShowLight

---

## C_FireCrackerBlast
Derived from: [C_Inferno](#c_inferno), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WeaponMP9
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## WeaponPurchaseTracker_t

Type | Name
------------ | -------------
`C_UtlVectorEmbeddedNetworkVar< WeaponPurchaseCount_t >` | m_weaponPurchases

---

## C_RetakeGameRules

Type | Name
------------ | -------------
`int32` | m_nMatchSeed
`bool` | m_bBlockersPresent
`bool` | m_bRoundInProgress
`int32` | m_iFirstSecondHalfRound
`int32` | m_iBombSite

---

## EngineCountdownTimer

Type | Name
------------ | -------------
`float32` | m_duration
`float32` | m_timestamp
`float32` | m_timescale

---

## CCSPlayer_GlowServices


---

## C_BaseFlex::Emphasized_Phoneme

Type | Name
------------ | -------------
`CUtlString` | m_sClassName
`float32` | m_flAmount
`bool` | m_bRequired
`bool` | m_bBasechecked
`bool` | m_bValid

---

## IntervalTimer

Type | Name
------------ | -------------
`GameTime_t` | m_timestamp
`WorldGroupId_t` | m_nWorldGroupId

---

## C_WeaponSSG08
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_FuncLadder
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`Vector` | m_vecLadderDir
`CUtlVector< CHandle< C_InfoLadderDismount > >` | m_Dismounts
`Vector` | m_vecLocalTop
`Vector` | m_vecPlayerMountPositionTop
`Vector` | m_vecPlayerMountPositionBottom
`float32` | m_flAutoRideSpeed
`bool` | m_bDisabled
`bool` | m_bFakeLadder
`bool` | m_bHasSlack

---

## C_SoundOpvarSetOBBEntity
Derived from: [C_SoundOpvarSetAABBEntity](#c_soundopvarsetaabbentity), [C_SoundOpvarSetPointEntity](#c_soundopvarsetpointentity), [C_SoundOpvarSetPointBase](#c_soundopvarsetpointbase), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPlayer_WeaponServices


Type | Name
------------ | -------------
`C_NetworkUtlVectorBase< CHandle< C_BasePlayerWeapon > >` | m_hMyWeapons
`CHandle< C_BasePlayerWeapon >` | m_hActiveWeapon
`CHandle< C_BasePlayerWeapon >` | m_hLastWeapon
`uint16[32]` | m_iAmmo

---

## CAttributeManager::cached_attribute_float_t

Type | Name
------------ | -------------
`float32` | flIn
`CUtlSymbolLarge` | iAttribHook
`float32` | flOut

---

## C_BaseGrenade
Derived from: [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bHasWarnedAI
`bool` | m_bIsSmokeGrenade
`bool` | m_bIsLive
`float32` | m_DmgRadius
`GameTime_t` | m_flDetonateTime
`float32` | m_flWarnAITime
`float32` | m_flDamage
`CUtlSymbolLarge` | m_iszBounceSound
`CUtlString` | m_ExplosionSound
`CHandle< C_CSPlayerPawn >` | m_hThrower
`GameTime_t` | m_flNextAttack
`CHandle< C_CSPlayerPawn >` | m_hOriginalThrower

---

## CCSGameModeRules

Type | Name
------------ | -------------
`CNetworkVarChainer` | __m_pChainEntity

---

## VPhysicsCollisionAttribute_t

Type | Name
------------ | -------------
`uint64` | m_nInteractsAs
`uint64` | m_nInteractsWith
`uint64` | m_nInteractsExclude
`uint32` | m_nEntityId
`uint32` | m_nOwnerId
`uint16` | m_nHierarchyId
`uint8` | m_nCollisionGroup
`uint8` | m_nCollisionFunctionMask

---

## C_EnvVolumetricFogController
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flScattering
`float32` | m_flAnisotropy
`float32` | m_flFadeSpeed
`float32` | m_flDrawDistance
`float32` | m_flFadeInStart
`float32` | m_flFadeInEnd
`float32` | m_flIndirectStrength
`int32` | m_nVolumeDepth
`float32` | m_fFirstVolumeSliceThickness
`int32` | m_nIndirectTextureDimX
`int32` | m_nIndirectTextureDimY
`int32` | m_nIndirectTextureDimZ
`Vector` | m_vBoxMins
`Vector` | m_vBoxMaxs
`bool` | m_bActive
`GameTime_t` | m_flStartAnisoTime
`GameTime_t` | m_flStartScatterTime
`GameTime_t` | m_flStartDrawDistanceTime
`float32` | m_flStartAnisotropy
`float32` | m_flStartScattering
`float32` | m_flStartDrawDistance
`float32` | m_flDefaultAnisotropy
`float32` | m_flDefaultScattering
`float32` | m_flDefaultDrawDistance
`bool` | m_bStartDisabled
`bool` | m_bEnableIndirect
`bool` | m_bIndirectUseLPVs
`bool` | m_bIsMaster
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_hFogIndirectTexture
`int32` | m_nForceRefreshCount
`float32` | m_fNoiseSpeed
`float32` | m_fNoiseStrength
`Vector` | m_vNoiseScale
`bool` | m_bFirstTime

---

## C_WeaponTec9
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_PointCommentaryNode
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bActive
`bool` | m_bWasActive
`GameTime_t` | m_flEndTime
`GameTime_t` | m_flStartTime
`float32` | m_flStartTimeInCommentary
`CUtlSymbolLarge` | m_iszCommentaryFile
`CUtlSymbolLarge` | m_iszTitle
`CUtlSymbolLarge` | m_iszSpeakers
`int32` | m_iNodeNumber
`int32` | m_iNodeNumberMax
`bool` | m_bListenedTo
`CHandle< C_BaseEntity >` | m_hViewPosition
`bool` | m_bRestartAfterRestore

---

## CCSObserver_CameraServices
Derived from: [CCSPlayerBase_CameraServices](#ccsplayerbase_cameraservices), [CPlayer_CameraServices](#cplayer_cameraservices)

---

## CCSClientPointScriptEntity
Derived from: [CCSPointScriptEntity](#ccspointscriptentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## audioparams_t

Type | Name
------------ | -------------
`Vector[8]` | localSound
`int32` | soundscapeIndex
`uint8` | localBits
`int32` | soundscapeEntityListIndex
`uint32` | soundEventHash

---

## C_CS2WeaponModuleBase
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_InfoVisibilityBox
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`int32` | m_nMode
`Vector` | m_vBoxSize
`bool` | m_bEnabled

---

## C_FireSprite
Derived from: [C_Sprite](#c_sprite), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`Vector` | m_vecMoveDir
`bool` | m_bFadeFromAbove

---

## C_CSGO_TeamIntroTerroristPosition
Derived from: [C_CSGO_TeamIntroCharacterPosition](#c_csgo_teamintrocharacterposition), [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_Precipitation
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flDensity
`float32` | m_flParticleInnerDist
`char*` | m_pParticleDef
`TimedEvent[1]` | m_tParticlePrecipTraceTimer
`bool[1]` | m_bActiveParticlePrecipEmitter
`bool` | m_bParticlePrecipInitialized
`bool` | m_bHasSimulatedSinceLastSceneObjectUpdate
`int32` | m_nAvailableSheetSequencesMaxIndex

---

## CPrecipitationVData


Type | Name
------------ | -------------
`CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >` | m_szParticlePrecipitationEffect
`float32` | m_flInnerDistance
`ParticleAttachment_t` | m_nAttachType
`bool` | m_bBatchSameVolumeType
`int32` | m_nRTEnvCP
`int32` | m_nRTEnvCPComponent
`CUtlString` | m_szModifier

---

## CBuoyancyHelper

Type | Name
------------ | -------------
`CUtlStringToken` | m_nFluidType
`float32` | m_flFluidDensity
`CUtlVector< float32 >` | m_vecFractionOfWheelSubmergedForWheelFriction
`CUtlVector< float32 >` | m_vecWheelFrictionScales
`CUtlVector< float32 >` | m_vecFractionOfWheelSubmergedForWheelDrag
`CUtlVector< float32 >` | m_vecWheelDrag

---

## C_BaseClientUIEntity
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bEnabled
`CUtlSymbolLarge` | m_DialogXMLName
`CUtlSymbolLarge` | m_PanelClassName
`CUtlSymbolLarge` | m_PanelID

---

## C_FuncTrackTrain
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`int32` | m_nLongAxis
`float32` | m_flRadius
`float32` | m_flLineLength

---

## CCSPlayer_ActionTrackingServices


Type | Name
------------ | -------------
`CHandle< C_BasePlayerWeapon >` | m_hLastWeaponBeforeC4AutoSwitch
`bool` | m_bIsRescuing
`WeaponPurchaseTracker_t` | m_weaponPurchasesThisMatch
`WeaponPurchaseTracker_t` | m_weaponPurchasesThisRound

---

## shard_model_desc_t

Type | Name
------------ | -------------
`int32` | m_nModelID
`CStrongHandle< InfoForResourceTypeIMaterial2 >` | m_hMaterialBase
`CStrongHandle< InfoForResourceTypeIMaterial2 >` | m_hMaterialDamageOverlay
`ShardSolid_t` | m_solid
`Vector2D` | m_vecPanelSize
`Vector2D` | m_vecStressPositionA
`Vector2D` | m_vecStressPositionB
`C_NetworkUtlVectorBase< Vector2D >` | m_vecPanelVertices
`C_NetworkUtlVectorBase< Vector4D >` | m_vInitialPanelVertices
`float32` | m_flGlassHalfThickness
`bool` | m_bHasParent
`bool` | m_bParentFrozen
`CUtlStringToken` | m_SurfacePropStringToken

---

## C_SceneEntity::QueuedEvents_t

Type | Name
------------ | -------------
`float32` | starttime

---

## CBaseProp
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bModelOverrodeBlockLOS
`int32` | m_iShapeType
`bool` | m_bConformToCollisionBounds
`matrix3x4_t` | m_mPreferredCatchTransform

---

## C_CSGO_PreviewPlayerAlias_csgo_player_previewmodel
Derived from: [C_CSGO_PreviewPlayer](#c_csgo_previewplayer), [C_CSPlayerPawn](#c_csplayerpawn), [C_CSPlayerPawnBase](#c_csplayerpawnbase), [C_BasePlayerPawn](#c_baseplayerpawn), [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPointScriptExtensions_observer

---

## CPointTemplate
Derived from: [CLogicalEntity](#clogicalentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CUtlSymbolLarge` | m_iszWorldName
`CUtlSymbolLarge` | m_iszSource2EntityLumpName
`CUtlSymbolLarge` | m_iszEntityFilterName
`float32` | m_flTimeoutInterval
`bool` | m_bAsynchronouslySpawnEntities
`CEntityIOOutput` | m_pOutputOnSpawned
`PointTemplateClientOnlyEntityBehavior_t` | m_clientOnlyEntityBehavior
`PointTemplateOwnerSpawnGroupType_t` | m_ownerSpawnGroupType
`CUtlVector< uint32 >` | m_createdSpawnGroupHandles
`CUtlVector< CEntityHandle >` | m_SpawnedEntityHandles
`HSCRIPT` | m_ScriptSpawnCallback
`HSCRIPT` | m_ScriptCallbackScope

---

## C_WeaponHKP2000
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_PreviewModel
Derived from: [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CUtlString` | m_animgraph
`CGlobalSymbol` | m_animgraphCharacterModeString
`CUtlString` | m_defaultAnim
`AnimLoopMode_t` | m_nDefaultAnimLoopMode
`float32` | m_flInitialModelScale
`CUtlString` | m_sInitialWeaponState

---

## CInfoDynamicShadowHint
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bDisabled
`float32` | m_flRange
`int32` | m_nImportance
`int32` | m_nLightChoice
`CHandle< C_BaseEntity >` | m_hLight

---

## CTakeDamageInfoAPI

---

## C_BaseEntityAPI

---

## C_WeaponXM1014
Derived from: [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_MapPreviewParticleSystem
Derived from: [C_ParticleSystem](#c_particlesystem), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CGlowProperty

Type | Name
------------ | -------------
`Vector` | m_fGlowColor
`int32` | m_iGlowType
`int32` | m_iGlowTeam
`int32` | m_nGlowRange
`int32` | m_nGlowRangeMin
`Color` | m_glowColorOverride
`bool` | m_bFlashing
`float32` | m_flGlowTime
`float32` | m_flGlowStartTime
`bool` | m_bEligibleForScreenHighlight
`bool` | m_bGlowing

---

## C_TriggerPhysics
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_gravityScale
`float32` | m_linearLimit
`float32` | m_linearDamping
`float32` | m_angularLimit
`float32` | m_angularDamping
`float32` | m_linearForce
`float32` | m_flFrequency
`float32` | m_flDampingRatio
`Vector` | m_vecLinearForcePointAt
`bool` | m_bCollapseToForcePoint
`Vector` | m_vecLinearForcePointAtWorld
`Vector` | m_vecLinearForceDirection
`bool` | m_bConvertToDebrisWhenPossible

---

## CCSPlayer_HostageServices


Type | Name
------------ | -------------
`CHandle< C_BaseEntity >` | m_hCarriedHostage
`CHandle< C_BaseEntity >` | m_hCarriedHostageProp

---

## C_LightDirectionalEntity
Derived from: [C_LightEntity](#c_lightentity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EnvCubemap
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_Entity_hCubemapTexture
`bool` | m_Entity_bCustomCubemapTexture
`float32` | m_Entity_flInfluenceRadius
`Vector` | m_Entity_vBoxProjectMins
`Vector` | m_Entity_vBoxProjectMaxs
`bool` | m_Entity_bMoveable
`int32` | m_Entity_nHandshake
`int32` | m_Entity_nEnvCubeMapArrayIndex
`int32` | m_Entity_nPriority
`float32` | m_Entity_flEdgeFadeDist
`Vector` | m_Entity_vEdgeFadeDists
`float32` | m_Entity_flDiffuseScale
`bool` | m_Entity_bStartDisabled
`bool` | m_Entity_bDefaultEnvMap
`bool` | m_Entity_bDefaultSpecEnvMap
`bool` | m_Entity_bIndoorCubeMap
`bool` | m_Entity_bCopyDiffuseFromDefaultCubemap
`bool` | m_Entity_bEnabled

---

## C_PredictedViewModel
Derived from: [C_BaseViewModel](#c_baseviewmodel), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`Vector` | m_vPredictedLagOffset
`QAngle` | m_targetSpeed
`QAngle` | m_currentSpeed

---

## C_WeaponBizon
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_AK47
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_PointValueRemapper
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bDisabled
`bool` | m_bDisabledOld
`bool` | m_bUpdateOnClient
`ValueRemapperInputType_t` | m_nInputType
`CHandle< C_BaseEntity >` | m_hRemapLineStart
`CHandle< C_BaseEntity >` | m_hRemapLineEnd
`float32` | m_flMaximumChangePerSecond
`float32` | m_flDisengageDistance
`float32` | m_flEngageDistance
`bool` | m_bRequiresUseKey
`ValueRemapperOutputType_t` | m_nOutputType
`C_NetworkUtlVectorBase< CHandle< C_BaseEntity > >` | m_hOutputEntities
`ValueRemapperHapticsType_t` | m_nHapticsType
`ValueRemapperMomentumType_t` | m_nMomentumType
`float32` | m_flMomentumModifier
`float32` | m_flSnapValue
`float32` | m_flCurrentMomentum
`ValueRemapperRatchetType_t` | m_nRatchetType
`float32` | m_flRatchetOffset
`float32` | m_flInputOffset
`bool` | m_bEngaged
`bool` | m_bFirstUpdate
`float32` | m_flPreviousValue
`GameTime_t` | m_flPreviousUpdateTickTime
`Vector` | m_vecPreviousTestPoint

---

## C_Knife
Derived from: [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bFirstAttack

---

## C_EnvCubemapBox
Derived from: [C_EnvCubemap](#c_envcubemap), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_ItemDogtags
Derived from: [C_Item](#c_item), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CHandle< C_CSPlayerPawn >` | m_OwningPlayer
`CHandle< C_CSPlayerPawn >` | m_KillingPlayer

---

## C_CSGO_EndOfMatchCamera
Derived from: [C_CSGO_TeamPreviewCamera](#c_csgo_teampreviewcamera), [C_CSGO_MapPreviewCameraPath](#c_csgo_mappreviewcamerapath), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_SoundOpvarSetPointBase
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CUtlSymbolLarge` | m_iszStackName
`CUtlSymbolLarge` | m_iszOperatorName
`CUtlSymbolLarge` | m_iszOpvarName
`int32` | m_iOpvarIndex
`bool` | m_bUseAutoCompare

---

## C_PhysBox
Derived from: [C_Breakable](#c_breakable), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPlayer_BuyServices


Type | Name
------------ | -------------
`C_UtlVectorEmbeddedNetworkVar< SellbackPurchaseEntry_t >` | m_vecSellbackPurchaseEntries

---

## CPathSimpleAPI

---

## C_WeaponTaser
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`GameTime_t` | m_fFireTime
`int32` | m_nLastAttackTick

---

## C_PhysicsPropMultiplayer
Derived from: [C_PhysicsProp](#c_physicsprop), [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CInfoDynamicShadowHintBox
Derived from: [CInfoDynamicShadowHint](#cinfodynamicshadowhint), [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`Vector` | m_vBoxMins
`Vector` | m_vBoxMaxs

---

## C_SoundOpvarSetPathCornerEntity
Derived from: [C_SoundOpvarSetPointEntity](#c_soundopvarsetpointentity), [C_SoundOpvarSetPointBase](#c_soundopvarsetpointbase), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EnvCubemapFog
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flEndDistance
`float32` | m_flStartDistance
`float32` | m_flFogFalloffExponent
`bool` | m_bHeightFogEnabled
`float32` | m_flFogHeightWidth
`float32` | m_flFogHeightEnd
`float32` | m_flFogHeightStart
`float32` | m_flFogHeightExponent
`float32` | m_flLODBias
`bool` | m_bActive
`bool` | m_bStartDisabled
`float32` | m_flFogMaxOpacity
`int32` | m_nCubemapSourceType
`CStrongHandle< InfoForResourceTypeIMaterial2 >` | m_hSkyMaterial
`CUtlSymbolLarge` | m_iszSkyEntity
`CStrongHandle< InfoForResourceTypeCTextureBase >` | m_hFogCubemapTexture
`bool` | m_bHasHeightFogEnd
`bool` | m_bFirstTime

---

## C_WeaponSawedoff
Derived from: [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCollisionProperty

Type | Name
------------ | -------------
`VPhysicsCollisionAttribute_t` | m_collisionAttribute
`Vector` | m_vecMins
`Vector` | m_vecMaxs
`uint8` | m_usSolidFlags
`SolidType_t` | m_nSolidType
`uint8` | m_triggerBloat
`SurroundingBoundsType_t` | m_nSurroundType
`uint8` | m_CollisionGroup
`uint8` | m_nEnablePhysics
`float32` | m_flBoundingRadius
`Vector` | m_vecSpecifiedSurroundingMins
`Vector` | m_vecSpecifiedSurroundingMaxs
`Vector` | m_vecSurroundingMaxs
`Vector` | m_vecSurroundingMins
`Vector` | m_vCapsuleCenter1
`Vector` | m_vCapsuleCenter2
`float32` | m_flCapsuleRadius

---

## CNetworkedSequenceOperation

Type | Name
------------ | -------------
`HSequence` | m_hSequence
`float32` | m_flPrevCycle
`float32` | m_flCycle
`CNetworkedQuantizedFloat` | m_flWeight
`bool` | m_bSequenceChangeNetworked
`bool` | m_bDiscontinuity
`float32` | m_flPrevCycleFromDiscontinuity
`float32` | m_flPrevCycleForAnimEventDetection

---

## C_PlayerSprayDecal
Derived from: [C_ModelPointEntity](#c_modelpointentity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`int32` | m_nUniqueID
`uint32` | m_unAccountID
`uint32` | m_unTraceID
`uint32` | m_rtGcTime
`Vector` | m_vecEndPos
`Vector` | m_vecStart
`Vector` | m_vecLeft
`Vector` | m_vecNormal
`int32` | m_nPlayer
`int32` | m_nEntity
`int32` | m_nHitbox
`float32` | m_flCreationTime
`int32` | m_nTintID
`uint8` | m_nVersion
`uint8[128]` | m_ubSignature
`CPlayerSprayDecalRenderHelper` | m_SprayRenderHelper

---

## EntityRenderAttribute_t

Type | Name
------------ | -------------
`CUtlStringToken` | m_ID
`Vector4D` | m_Values

---

## C_ShatterGlassShardPhysics
Derived from: [C_PhysicsProp](#c_physicsprop), [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`shard_model_desc_t` | m_ShardDesc

---

## C_WeaponElite
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_LightEntity
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CLightComponent*` | m_CLightComponent

---

## C_PlayerVisibility
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flVisibilityStrength
`float32` | m_flFogDistanceMultiplier
`float32` | m_flFogMaxDensityMultiplier
`float32` | m_flFadeTime
`bool` | m_bStartDisabled
`bool` | m_bIsEnabled

---

## fogparams_t

Type | Name
------------ | -------------
`Vector` | dirPrimary
`Color` | colorPrimary
`Color` | colorSecondary
`Color` | colorPrimaryLerpTo
`Color` | colorSecondaryLerpTo
`float32` | start
`float32` | end
`float32` | farz
`float32` | maxdensity
`float32` | exponent
`float32` | HDRColorScale
`float32` | skyboxFogFactor
`float32` | skyboxFogFactorLerpTo
`float32` | startLerpTo
`float32` | endLerpTo
`float32` | maxdensityLerpTo
`GameTime_t` | lerptime
`float32` | duration
`float32` | blendtobackground
`float32` | scattering
`float32` | locallightscale
`bool` | enable
`bool` | blend
`bool` | m_bNoReflectionFog
`bool` | m_bPadding

---

## C_BaseFlex
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`C_NetworkUtlVectorBase< float32 >` | m_flexWeight
`Vector` | m_vLookTargetPosition
`bool` | m_blinktoggle
`int32` | m_nLastFlexUpdateFrameCount
`Vector` | m_CachedViewTarget
`SceneEventId_t` | m_nNextSceneEventId
`int32` | m_iBlink
`float32` | m_blinktime
`bool` | m_prevblinktoggle
`int32` | m_iJawOpen
`float32` | m_flJawOpenAmount
`float32` | m_flBlinkAmount
`AttachmentHandle_t` | m_iMouthAttachment
`AttachmentHandle_t` | m_iEyeAttachment
`bool` | m_bResetFlexWeightsOnModelChange
`int32` | m_nEyeOcclusionRendererBone
`matrix3x4_t` | m_mEyeOcclusionRendererCameraToBoneTransform
`Vector` | m_vEyeOcclusionRendererHalfExtent
`C_BaseFlex::Emphasized_Phoneme[3]` | m_PhonemeClasses

---

## C_EnvSky
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CStrongHandle< InfoForResourceTypeIMaterial2 >` | m_hSkyMaterial
`CStrongHandle< InfoForResourceTypeIMaterial2 >` | m_hSkyMaterialLightingOnly
`bool` | m_bStartDisabled
`Color` | m_vTintColor
`Color` | m_vTintColorLightingOnly
`float32` | m_flBrightnessScale
`int32` | m_nFogType
`float32` | m_flFogMinStart
`float32` | m_flFogMinEnd
`float32` | m_flFogMaxStart
`float32` | m_flFogMaxEnd
`bool` | m_bEnabled

---

## CInfoTarget
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_TeamIntroCounterTerroristPosition
Derived from: [C_CSGO_TeamIntroCharacterPosition](#c_csgo_teamintrocharacterposition), [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_DynamicProp
Derived from: [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bUseHitboxesForRenderBox
`bool` | m_bUseAnimGraph
`CEntityIOOutput` | m_pOutputAnimBegun
`CEntityIOOutput` | m_pOutputAnimOver
`CEntityIOOutput` | m_pOutputAnimLoopCycleOver
`CEntityIOOutput` | m_OnAnimReachedStart
`CEntityIOOutput` | m_OnAnimReachedEnd
`CUtlSymbolLarge` | m_iszIdleAnim
`AnimLoopMode_t` | m_nIdleAnimLoopMode
`bool` | m_bRandomizeCycle
`bool` | m_bStartDisabled
`bool` | m_bFiredStartEndOutput
`bool` | m_bForceNpcExclude
`bool` | m_bCreateNonSolid
`bool` | m_bIsOverrideProp
`int32` | m_iInitialGlowState
`int32` | m_nGlowRange
`int32` | m_nGlowRangeMin
`Color` | m_glowColor
`int32` | m_nGlowTeam
`int32` | m_iCachedFrameCount
`Vector` | m_vecCachedRenderMins
`Vector` | m_vecCachedRenderMaxs

---

## CPropDataComponent
Derived from: [CEntityComponent](#centitycomponent)

Type | Name
------------ | -------------
`float32` | m_flDmgModBullet
`float32` | m_flDmgModClub
`float32` | m_flDmgModExplosive
`float32` | m_flDmgModFire
`CUtlSymbolLarge` | m_iszPhysicsDamageTableName
`CUtlSymbolLarge` | m_iszBasePropData
`int32` | m_nInteractions
`bool` | m_bSpawnMotionDisabled
`int32` | m_nDisableTakePhysicsDamageSpawnFlag
`int32` | m_nMotionDisabledSpawnFlag

---

## C_WeaponSCAR20
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_DecoyGrenade
Derived from: [C_BaseCSGrenade](#c_basecsgrenade), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPointScriptExtensions_player

---

## C_KeychainModule
Derived from: [C_CS2WeaponModuleBase](#c_cs2weaponmodulebase), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`uint32` | m_nKeychainDefID
`uint32` | m_nKeychainSeed

---

## CCitadelSoundOpvarSetOBB
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CUtlSymbolLarge` | m_iszStackName
`CUtlSymbolLarge` | m_iszOperatorName
`CUtlSymbolLarge` | m_iszOpvarName
`Vector` | m_vDistanceInnerMins
`Vector` | m_vDistanceInnerMaxs
`Vector` | m_vDistanceOuterMins
`Vector` | m_vDistanceOuterMaxs
`int32` | m_nAABBDirection

---

## SellbackPurchaseEntry_t

Type | Name
------------ | -------------
`uint16` | m_unDefIdx
`int32` | m_nCost
`int32` | m_nPrevArmor
`bool` | m_bPrevHelmet
`CEntityHandle` | m_hItem

---

## C_SingleplayRules
Derived from: [C_GameRules](#c_gamerules)

---

## C_LocalTempEntity
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`int32` | flags
`GameTime_t` | die
`float32` | m_flFrameMax
`float32` | x
`float32` | y
`float32` | fadeSpeed
`float32` | bounceFactor
`int32` | hitSound
`int32` | priority
`Vector` | tentOffset
`QAngle` | m_vecTempEntAngVelocity
`int32` | tempent_renderamt
`Vector` | m_vecNormal
`float32` | m_flSpriteScale
`int32` | m_nFlickerFrame
`float32` | m_flFrameRate
`float32` | m_flFrame
`char*` | m_pszImpactEffect
`char*` | m_pszParticleEffect
`bool` | m_bParticleCollision
`int32` | m_iLastCollisionFrame
`Vector` | m_vLastCollisionOrigin
`Vector` | m_vecTempEntVelocity
`Vector` | m_vecPrevAbsOrigin
`Vector` | m_vecTempEntAcceleration

---

## C_EnvWindShared::WindAveEvent_t

Type | Name
------------ | -------------
`float32` | m_flStartWindSpeed
`float32` | m_flAveWindSpeed

---

## C_MolotovProjectile
Derived from: [C_BaseCSGrenadeProjectile](#c_basecsgrenadeprojectile), [C_BaseGrenade](#c_basegrenade), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bIsIncGrenade

---

## C_LightEnvironmentEntity
Derived from: [C_LightDirectionalEntity](#c_lightdirectionalentity), [C_LightEntity](#c_lightentity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WeaponUMP45
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CInfoOffscreenPanoramaTexture
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bDisabled
`int32` | m_nResolutionX
`int32` | m_nResolutionY
`CUtlSymbolLarge` | m_szLayoutFileName
`CUtlSymbolLarge` | m_RenderAttrName
`C_NetworkUtlVectorBase< CHandle< C_BaseModelEntity > >` | m_TargetEntities
`int32` | m_nTargetChangeCount
`C_NetworkUtlVectorBase< CUtlSymbolLarge >` | m_vecCSSClasses
`bool` | m_bCheckCSSClasses

---

## C_DynamicLight
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`uint8` | m_Flags
`uint8` | m_LightStyle
`float32` | m_Radius
`int32` | m_Exponent
`float32` | m_InnerAngle
`float32` | m_OuterAngle
`float32` | m_SpotRadius

---

## C_CSWeaponBase
Derived from: [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flFireSequenceStartTime
`int32` | m_nFireSequenceStartTimeChange
`int32` | m_nFireSequenceStartTimeAck
`PlayerAnimEvent_t` | m_ePlayerFireEvent
`WeaponAttackType_t` | m_ePlayerFireEventAttackType
`HSequence` | m_seqIdle
`HSequence` | m_seqFirePrimary
`HSequence` | m_seqFireSecondary
`CUtlVector< HSequence >` | m_thirdPersonFireSequences
`HSequence` | m_hCurrentThirdPersonSequence
`int32` | m_nSilencerBoneIndex
`HSequence[7]` | m_thirdPersonSequences
`CSWeaponState_t` | m_ClientPreviousWeaponState
`CSWeaponState_t` | m_iState
`float32` | m_flCrosshairDistance
`int32` | m_iAmmoLastCheck
`int32` | m_iAlpha
`int32` | m_iScopeTextureID
`int32` | m_iCrosshairTextureID
`float32` | m_flGunAccuracyPositionDeprecated
`int32` | m_nLastEmptySoundCmdNum
`uint32` | m_nViewModelIndex
`bool` | m_bReloadsWithClips
`GameTime_t` | m_flTimeWeaponIdle
`bool` | m_bFireOnEmpty
`CEntityIOOutput` | m_OnPlayerPickup
`CSWeaponMode` | m_weaponMode
`float32` | m_flTurningInaccuracyDelta
`Vector` | m_vecTurningInaccuracyEyeDirLast
`float32` | m_flTurningInaccuracy
`float32` | m_fAccuracyPenalty
`GameTime_t` | m_flLastAccuracyUpdateTime
`float32` | m_fAccuracySmoothedForZoom
`GameTime_t` | m_fScopeZoomEndTime
`int32` | m_iRecoilIndex
`float32` | m_flRecoilIndex
`bool` | m_bBurstMode
`GameTime_t` | m_flLastBurstModeChangeTime
`GameTick_t` | m_nPostponeFireReadyTicks
`float32` | m_flPostponeFireReadyFrac
`bool` | m_bInReload
`bool` | m_bReloadVisuallyComplete
`GameTime_t` | m_flDroppedAtTime
`bool` | m_bIsHauledBack
`bool` | m_bSilencerOn
`GameTime_t` | m_flTimeSilencerSwitchComplete
`int32` | m_iOriginalTeamNumber
`int32` | m_iMostRecentTeamNumber
`bool` | m_bDroppedNearBuyZone
`float32` | m_flNextAttackRenderTimeOffset
`bool` | m_bClearWeaponIdentifyingUGC
`bool` | m_bVisualsDataSet
`bool` | m_bOldFirstPersonSpectatedState
`bool` | m_bUIWeapon
`int32` | m_nCustomEconReloadEventId
`GameTime_t` | m_nextPrevOwnerUseTime
`CHandle< C_CSPlayerPawn >` | m_hPrevOwner
`GameTick_t` | m_nDropTick
`bool` | m_donated
`GameTime_t` | m_fLastShotTime
`bool` | m_bWasOwnedByCT
`bool` | m_bWasOwnedByTerrorist
`float32` | m_gunHeat
`uint32` | m_smokeAttachments
`GameTime_t` | m_lastSmokeTime
`float32` | m_flNextClientFireBulletTime
`float32` | m_flNextClientFireBulletTime_Repredict
`C_IronSightController` | m_IronSightController
`int32` | m_iIronSightMode
`GameTime_t` | m_flLastLOSTraceFailureTime
`int32` | m_iNumEmptyAttacks
`GameTime_t` | m_flLastMagDropRequestTime
`float32` | m_flWatTickOffset

---

## C_TriggerVolume
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_FuncElectrifiedVolume
Derived from: [C_FuncBrush](#c_funcbrush), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`ParticleIndex_t` | m_nAmbientEffect
`CUtlSymbolLarge` | m_EffectName
`bool` | m_bState

---

## CCSPlayer_WeaponServices
Derived from: [CPlayer_WeaponServices](#cplayer_weaponservices)

Type | Name
------------ | -------------
`GameTime_t` | m_flNextAttack
`bool` | m_bIsLookingAtWeapon
`bool` | m_bIsHoldingLookAtWeapon
`uint32` | m_nOldShootPositionHistoryCount
`uint32` | m_nOldInputHistoryCount

---

## C_EnvDetailController
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flFadeStartDist
`float32` | m_flFadeEndDist

---

## C_BaseEntity
Derived from: [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CBodyComponent*` | m_CBodyComponent
`CNetworkTransmitComponent` | m_NetworkTransmitComponent
`GameTick_t` | m_nLastThinkTick
`CGameSceneNode*` | m_pGameSceneNode
`CRenderComponent*` | m_pRenderComponent
`CCollisionProperty*` | m_pCollision
`int32` | m_iMaxHealth
`int32` | m_iHealth
`uint8` | m_lifeState
`bool` | m_bTakesDamage
`TakeDamageFlags_t` | m_nTakeDamageFlags
`EntityPlatformTypes_t` | m_nPlatformType
`uint8` | m_ubInterpolationFrame
`CHandle< C_BaseEntity >` | m_hSceneObjectController
`int32` | m_nNoInterpolationTick
`int32` | m_nVisibilityNoInterpolationTick
`float32` | m_flProxyRandomValue
`int32` | m_iEFlags
`uint8` | m_nWaterType
`bool` | m_bInterpolateEvenWithNoModel
`bool` | m_bPredictionEligible
`bool` | m_bApplyLayerMatchIDToModel
`CUtlStringToken` | m_tokLayerMatchID
`CUtlStringToken` | m_nSubclassID
`int32` | m_nSimulationTick
`int32` | m_iCurrentThinkContext
`CUtlVector< thinkfunc_t >` | m_aThinkFunctions
`bool` | m_bDisabledContextThinks
`float32` | m_flAnimTime
`float32` | m_flSimulationTime
`uint8` | m_nSceneObjectOverrideFlags
`bool` | m_bHasSuccessfullyInterpolated
`bool` | m_bHasAddedVarsToInterpolation
`bool` | m_bRenderEvenWhenNotSuccessfullyInterpolated
`int32[2]` | m_nInterpolationLatchDirtyFlags
`uint16[11]` | m_ListEntry
`GameTime_t` | m_flCreateTime
`float32` | m_flSpeed
`uint16` | m_EntClientFlags
`bool` | m_bClientSideRagdoll
`uint8` | m_iTeamNum
`uint32` | m_spawnflags
`GameTick_t` | m_nNextThinkTick
`uint32` | m_fFlags
`Vector` | m_vecAbsVelocity
`CNetworkVelocityVector` | m_vecVelocity
`Vector` | m_vecBaseVelocity
`CHandle< C_BaseEntity >` | m_hEffectEntity
`CHandle< C_BaseEntity >` | m_hOwnerEntity
`MoveCollide_t` | m_MoveCollide
`MoveType_t` | m_MoveType
`MoveType_t` | m_nActualMoveType
`float32` | m_flWaterLevel
`uint32` | m_fEffects
`CHandle< C_BaseEntity >` | m_hGroundEntity
`int32` | m_nGroundBodyIndex
`float32` | m_flFriction
`float32` | m_flElasticity
`float32` | m_flGravityScale
`float32` | m_flTimeScale
`bool` | m_bAnimatedEveryTick
`GameTime_t` | m_flNavIgnoreUntilTime
`uint16` | m_hThink
`uint8` | m_fBBoxVisFlags
`bool` | m_bPredictable
`bool` | m_bRenderWithViewModels
`CSplitScreenSlot` | m_nSplitUserPlayerPredictionSlot
`int32` | m_nFirstPredictableCommand
`int32` | m_nLastPredictableCommand
`CHandle< C_BaseEntity >` | m_hOldMoveParent
`CParticleProperty` | m_Particles
`CUtlVector< float32 >` | m_vecPredictedScriptFloats
`CUtlVector< int32 >` | m_vecPredictedScriptFloatIDs
`int32` | m_nNextScriptVarRecordID
`QAngle` | m_vecAngVelocity
`int32` | m_DataChangeEventRef
`CUtlVector< CEntityHandle >` | m_dependencies
`int32` | m_nCreationTick
`bool` | m_bAnimTimeChanged
`bool` | m_bSimulationTimeChanged
`CUtlString` | m_sUniqueHammerID
`BloodType` | m_nBloodType

---

## CEntityIdentity

Type | Name
------------ | -------------
`int32` | m_nameStringableIndex
`CUtlSymbolLarge` | m_name
`CUtlSymbolLarge` | m_designerName
`uint32` | m_flags
`WorldGroupId_t` | m_worldGroupId
`uint32` | m_fDataObjectTypes
`ChangeAccessorFieldPathIndex_t` | m_PathIndex
`CEntityIdentity*` | m_pPrev
`CEntityIdentity*` | m_pNext
`CEntityIdentity*` | m_pPrevByClass
`CEntityIdentity*` | m_pNextByClass

---

## C_StattrakModule
Derived from: [C_CS2WeaponModuleBase](#c_cs2weaponmodulebase), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bKnife

---

## C_PhysicsProp
Derived from: [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bAwake

---

## C_BreakableProp
Derived from: [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CPropDataComponent` | m_CPropDataComponent
`CEntityIOOutput` | m_OnBreak
`CEntityOutputTemplate< float32 >` | m_OnHealthChanged
`CEntityIOOutput` | m_OnTakeDamage
`float32` | m_impactEnergyScale
`int32` | m_iMinHealthDmg
`float32` | m_flPressureDelay
`float32` | m_flDefBurstScale
`Vector` | m_vDefBurstOffset
`CHandle< C_BaseEntity >` | m_hBreaker
`PerformanceMode_t` | m_PerformanceMode
`GameTime_t` | m_flPreventDamageBeforeTime
`BreakableContentsType_t` | m_BreakableContentsType
`CUtlString` | m_strBreakableContentsPropGroupOverride
`CUtlString` | m_strBreakableContentsParticleOverride
`bool` | m_bHasBreakPiecesOrCommands
`float32` | m_explodeDamage
`float32` | m_explodeRadius
`float32` | m_explosionDelay
`CUtlSymbolLarge` | m_explosionBuildupSound
`CUtlSymbolLarge` | m_explosionCustomEffect
`CUtlSymbolLarge` | m_explosionCustomSound
`CUtlSymbolLarge` | m_explosionModifier
`CHandle< C_BasePlayerPawn >` | m_hPhysicsAttacker
`GameTime_t` | m_flLastPhysicsInfluenceTime
`float32` | m_flDefaultFadeScale
`CHandle< C_BaseEntity >` | m_hLastAttacker
`CHandle< C_BaseEntity >` | m_hFlareEnt
`bool` | m_noGhostCollision

---

## C_FuncMoveLinear
Derived from: [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_Beam
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`float32` | m_flFrameRate
`float32` | m_flHDRColorScale
`GameTime_t` | m_flFireTime
`float32` | m_flDamage
`uint8` | m_nNumBeamEnts
`int32` | m_queryHandleHalo
`CStrongHandle< InfoForResourceTypeIMaterial2 >` | m_hBaseMaterial
`CStrongHandle< InfoForResourceTypeIMaterial2 >` | m_nHaloIndex
`BeamType_t` | m_nBeamType
`uint32` | m_nBeamFlags
`CHandle< C_BaseEntity >[10]` | m_hAttachEntity
`AttachmentHandle_t[10]` | m_nAttachIndex
`float32` | m_fWidth
`float32` | m_fEndWidth
`float32` | m_fFadeLength
`float32` | m_fHaloScale
`float32` | m_fAmplitude
`float32` | m_fStartFrame
`float32` | m_fSpeed
`float32` | m_flFrame
`BeamClipStyle_t` | m_nClipStyle
`bool` | m_bTurnedOff
`Vector` | m_vecEndPos
`CHandle< C_BaseEntity >` | m_hEndEntity

---

## C_CSGO_TeamPreviewCharacterPosition
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`int32` | m_nVariant
`int32` | m_nRandom
`int32` | m_nOrdinal
`CUtlString` | m_sWeaponName
`uint64` | m_xuid
`C_EconItemView` | m_agentItem
`C_EconItemView` | m_glovesItem
`C_EconItemView` | m_weaponItem

---

## C_DynamicPropAlias_prop_dynamic_override
Derived from: [C_DynamicProp](#c_dynamicprop), [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EnvScreenOverlay
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CUtlSymbolLarge[10]` | m_iszOverlayNames
`float32[10]` | m_flOverlayTimes
`GameTime_t` | m_flStartTime
`int32` | m_iDesiredOverlay
`bool` | m_bIsActive
`bool` | m_bWasActive
`int32` | m_iCachedDesiredOverlay
`int32` | m_iCurrentOverlay
`GameTime_t` | m_flCurrentOverlayTime

---

## CCSWeaponBaseVData
Derived from: [CBasePlayerWeaponVData](#cbaseplayerweaponvdata)

Type | Name
------------ | -------------
`CSWeaponType` | m_WeaponType
`CSWeaponCategory` | m_WeaponCategory
`CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >` | m_szViewModel
`CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >` | m_szPlayerModel
`CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >` | m_szWorldDroppedModel
`CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >` | m_szAimsightLensMaskModel
`CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >` | m_szMagazineModel
`CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >` | m_szHeatEffect
`CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >` | m_szEjectBrassEffect
`CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >` | m_szMuzzleFlashParticleAlt
`CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >` | m_szMuzzleFlashThirdPersonParticle
`CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >` | m_szMuzzleFlashThirdPersonParticleAlt
`CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >` | m_szTracerParticle
`gear_slot_t` | m_GearSlot
`int32` | m_GearSlotPosition
`loadout_slot_t` | m_DefaultLoadoutSlot
`CUtlString` | m_sWrongTeamMsg
`int32` | m_nPrice
`int32` | m_nKillAward
`int32` | m_nPrimaryReserveAmmoMax
`int32` | m_nSecondaryReserveAmmoMax
`bool` | m_bMeleeWeapon
`bool` | m_bHasBurstMode
`bool` | m_bIsRevolver
`bool` | m_bCannotShootUnderwater
`CGlobalSymbol` | m_szName
`CUtlString` | m_szAnimExtension
`CSWeaponSilencerType` | m_eSilencerType
`int32` | m_nCrosshairMinDistance
`int32` | m_nCrosshairDeltaDistance
`bool` | m_bIsFullAuto
`int32` | m_nNumBullets
`CFiringModeFloat` | m_flCycleTime
`CFiringModeFloat` | m_flMaxSpeed
`CFiringModeFloat` | m_flSpread
`CFiringModeFloat` | m_flInaccuracyCrouch
`CFiringModeFloat` | m_flInaccuracyStand
`CFiringModeFloat` | m_flInaccuracyJump
`CFiringModeFloat` | m_flInaccuracyLand
`CFiringModeFloat` | m_flInaccuracyLadder
`CFiringModeFloat` | m_flInaccuracyFire
`CFiringModeFloat` | m_flInaccuracyMove
`CFiringModeFloat` | m_flRecoilAngle
`CFiringModeFloat` | m_flRecoilAngleVariance
`CFiringModeFloat` | m_flRecoilMagnitude
`CFiringModeFloat` | m_flRecoilMagnitudeVariance
`CFiringModeInt` | m_nTracerFrequency
`float32` | m_flInaccuracyJumpInitial
`float32` | m_flInaccuracyJumpApex
`float32` | m_flInaccuracyReload
`int32` | m_nRecoilSeed
`int32` | m_nSpreadSeed
`float32` | m_flTimeToIdleAfterFire
`float32` | m_flIdleInterval
`float32` | m_flAttackMovespeedFactor
`float32` | m_flHeatPerShot
`float32` | m_flInaccuracyPitchShift
`float32` | m_flInaccuracyAltSoundThreshold
`float32` | m_flBotAudibleRange
`CUtlString` | m_szUseRadioSubtitle
`bool` | m_bUnzoomsAfterShot
`bool` | m_bHideViewModelWhenZoomed
`int32` | m_nZoomLevels
`int32` | m_nZoomFOV1
`int32` | m_nZoomFOV2
`float32` | m_flZoomTime0
`float32` | m_flZoomTime1
`float32` | m_flZoomTime2
`float32` | m_flIronSightPullUpSpeed
`float32` | m_flIronSightPutDownSpeed
`float32` | m_flIronSightFOV
`float32` | m_flIronSightPivotForward
`float32` | m_flIronSightLooseness
`QAngle` | m_angPivotAngle
`Vector` | m_vecIronSightEyePos
`int32` | m_nDamage
`float32` | m_flHeadshotMultiplier
`float32` | m_flArmorRatio
`float32` | m_flPenetration
`float32` | m_flRange
`float32` | m_flRangeModifier
`float32` | m_flFlinchVelocityModifierLarge
`float32` | m_flFlinchVelocityModifierSmall
`float32` | m_flRecoveryTimeCrouch
`float32` | m_flRecoveryTimeStand
`float32` | m_flRecoveryTimeCrouchFinal
`float32` | m_flRecoveryTimeStandFinal
`int32` | m_nRecoveryTransitionStartBullet
`int32` | m_nRecoveryTransitionEndBullet
`float32` | m_flThrowVelocity
`Vector` | m_vSmokeColor
`CGlobalSymbol` | m_szAnimClass

---

## C_PointWorldText
Derived from: [C_ModelPointEntity](#c_modelpointentity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bForceRecreateNextUpdate
`char[512]` | m_messageText
`char[64]` | m_FontName
`char[64]` | m_BackgroundMaterialName
`bool` | m_bEnabled
`bool` | m_bFullbright
`float32` | m_flWorldUnitsPerPx
`float32` | m_flFontSize
`float32` | m_flDepthOffset
`bool` | m_bDrawBackground
`float32` | m_flBackgroundBorderWidth
`float32` | m_flBackgroundBorderHeight
`float32` | m_flBackgroundWorldToUV
`Color` | m_Color
`PointWorldTextJustifyHorizontal_t` | m_nJustifyHorizontal
`PointWorldTextJustifyVertical_t` | m_nJustifyVertical
`PointWorldTextReorientMode_t` | m_nReorientMode

---

## CCSPlayerController
Derived from: [CBasePlayerController](#cbaseplayercontroller), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CCSPlayerController_InGameMoneyServices*` | m_pInGameMoneyServices
`CCSPlayerController_InventoryServices*` | m_pInventoryServices
`CCSPlayerController_ActionTrackingServices*` | m_pActionTrackingServices
`CCSPlayerController_DamageServices*` | m_pDamageServices
`uint32` | m_iPing
`bool` | m_bHasCommunicationAbuseMute
`CUtlSymbolLarge` | m_szCrosshairCodes
`uint8` | m_iPendingTeamNum
`GameTime_t` | m_flForceTeamTime
`int32` | m_iCompTeammateColor
`bool` | m_bEverPlayedOnTeam
`GameTime_t` | m_flPreviousForceJoinTeamTime
`CUtlSymbolLarge` | m_szClan
`CUtlString` | m_sSanitizedPlayerName
`int32` | m_iCoachingTeam
`uint64` | m_nPlayerDominated
`uint64` | m_nPlayerDominatingMe
`int32` | m_iCompetitiveRanking
`int32` | m_iCompetitiveWins
`int8` | m_iCompetitiveRankType
`int32` | m_iCompetitiveRankingPredicted_Win
`int32` | m_iCompetitiveRankingPredicted_Loss
`int32` | m_iCompetitiveRankingPredicted_Tie
`int32` | m_nEndMatchNextMapVote
`uint16` | m_unActiveQuestId
`QuestProgress::Reason` | m_nQuestProgressReason
`uint32` | m_unPlayerTvControlFlags
`int32` | m_iDraftIndex
`uint32` | m_msQueuedModeDisconnectionTimestamp
`uint32` | m_uiAbandonRecordedReason
`uint32` | m_eNetworkDisconnectionReason
`bool` | m_bCannotBeKicked
`bool` | m_bEverFullyConnected
`bool` | m_bAbandonAllowsSurrender
`bool` | m_bAbandonOffersInstantSurrender
`bool` | m_bDisconnection1MinWarningPrinted
`bool` | m_bScoreReported
`int32` | m_nDisconnectionTick
`bool` | m_bControllingBot
`bool` | m_bHasControlledBotThisRound
`bool` | m_bHasBeenControlledByPlayerThisRound
`int32` | m_nBotsControlledThisRound
`bool` | m_bCanControlObservedBot
`CHandle< C_CSPlayerPawn >` | m_hPlayerPawn
`CHandle< C_CSObserverPawn >` | m_hObserverPawn
`bool` | m_bPawnIsAlive
`uint32` | m_iPawnHealth
`int32` | m_iPawnArmor
`bool` | m_bPawnHasDefuser
`bool` | m_bPawnHasHelmet
`uint16` | m_nPawnCharacterDefIndex
`int32` | m_iPawnLifetimeStart
`int32` | m_iPawnLifetimeEnd
`int32` | m_iPawnBotDifficulty
`CHandle< CCSPlayerController >` | m_hOriginalControllerOfCurrentPawn
`int32` | m_iScore
`uint8[8]` | m_recentKillQueue
`uint8` | m_nFirstKill
`uint8` | m_nKillCount
`bool` | m_bMvpNoMusic
`int32` | m_eMvpReason
`int32` | m_iMusicKitID
`int32` | m_iMusicKitMVPs
`int32` | m_iMVPs
`bool` | m_bIsPlayerNameDirty
`bool` | m_bFireBulletsSeedSynchronized

---

## C_WeaponFiveSeven
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BasePropDoor
Derived from: [C_DynamicProp](#c_dynamicprop), [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`DoorState_t` | m_eDoorState
`bool` | m_modelChanged
`bool` | m_bLocked
`Vector` | m_closedPosition
`QAngle` | m_closedAngles
`CHandle< C_BasePropDoor >` | m_hMaster
`Vector` | m_vWhereToSetLightingOrigin

---

## C_CSGO_TeamSelectTerroristPosition
Derived from: [C_CSGO_TeamSelectCharacterPosition](#c_csgo_teamselectcharacterposition), [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_NametagModule
Derived from: [C_CS2WeaponModuleBase](#c_cs2weaponmodulebase), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CUtlString` | m_strNametagString

---

## C_PhysPropClientside
Derived from: [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`GameTime_t` | m_flTouchDelta
`GameTime_t` | m_fDeathTime
`float32` | m_inertiaScale
`Vector` | m_vecDamagePosition
`Vector` | m_vecDamageDirection
`DamageTypes_t` | m_nDamageType

---

## C_CSGO_TeamSelectCamera
Derived from: [C_CSGO_TeamPreviewCamera](#c_csgo_teampreviewcamera), [C_CSGO_MapPreviewCameraPath](#c_csgo_mappreviewcamerapath), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_SoundAreaEntityBase
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bDisabled
`bool` | m_bWasEnabled
`CUtlSymbolLarge` | m_iszSoundAreaType
`Vector` | m_vPos

---

## C_FogController
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`fogparams_t` | m_fog
`bool` | m_bUseAngles
`int32` | m_iChangedVariables

---

## CPlayer_ItemServices


---

## C_FuncBrush
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CInfoWorldLayer
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CEntityIOOutput` | m_pOutputOnEntitiesSpawned
`CUtlSymbolLarge` | m_worldName
`CUtlSymbolLarge` | m_layerName
`bool` | m_bWorldLayerVisible
`bool` | m_bEntitiesSpawned
`bool` | m_bCreateAsChildSpawnGroup
`uint32` | m_hLayerSpawnGroup
`bool` | m_bWorldLayerActuallyVisible

---

## C_NetTestBaseCombatCharacter
Derived from: [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_PhysMagnet
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CUtlVector< int32 >` | m_aAttachedObjectsFromServer
`CUtlVector< CHandle< C_BaseEntity > >` | m_aAttachedObjects

---

## C_FuncConveyor
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`Vector` | m_vecMoveDirEntitySpace
`float32` | m_flTargetSpeed
`GameTick_t` | m_nTransitionStartTick
`int32` | m_nTransitionDurationTicks
`float32` | m_flTransitionStartSpeed
`C_NetworkUtlVectorBase< CHandle< C_BaseEntity > >` | m_hConveyorModels
`float32` | m_flCurrentConveyorOffset
`float32` | m_flCurrentConveyorSpeed

---

## CEntityInstance

Type | Name
------------ | -------------
`CUtlSymbolLarge` | m_iszPrivateVScripts
`CEntityIdentity*` | m_pEntity
`CScriptComponent*` | m_CScriptComponent
`bool` | m_bVisibleinPVS

---

## ServerAuthoritativeWeaponSlot_t

Type | Name
------------ | -------------
`uint16` | unClass
`uint16` | unSlot
`uint16` | unItemDefIdx

---

## CCSPlayer_DamageReactServices


---

## C_BaseViewModel
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`Vector` | m_vecLastFacing
`uint32` | m_nViewModelIndex
`uint32` | m_nAnimationParity
`float32` | m_flAnimationStartTime
`CHandle< C_BasePlayerWeapon >` | m_hWeapon
`CUtlSymbolLarge` | m_sVMName
`CUtlSymbolLarge` | m_sAnimationPrefix
`AttachmentHandle_t` | m_iCameraAttachment
`QAngle` | m_vecLastCameraAngles
`float32` | m_previousElapsedDuration
`float32` | m_previousCycle
`int32` | m_nOldAnimationParity
`HSequence` | m_hOldLayerSequence
`int32` | m_oldLayer
`float32` | m_oldLayerStartTime
`CHandle< C_BaseEntity >` | m_hControlPanel

---

## C_PortraitWorldCallbackHandler
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CHostageRescueZone
Derived from: [CHostageRescueZoneShim](#chostagerescuezoneshim), [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WeaponNegev
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CGameSceneNode

Type | Name
------------ | -------------
`CTransform` | m_nodeToWorld
`CEntityInstance*` | m_pOwner
`CGameSceneNode*` | m_pParent
`CGameSceneNode*` | m_pChild
`CGameSceneNode*` | m_pNextSibling
`CGameSceneNodeHandle` | m_hParent
`CNetworkOriginCellCoordQuantizedVector` | m_vecOrigin
`QAngle` | m_angRotation
`float32` | m_flScale
`Vector` | m_vecAbsOrigin
`QAngle` | m_angAbsRotation
`float32` | m_flAbsScale
`int16` | m_nParentAttachmentOrBone
`bool` | m_bDebugAbsOriginChanges
`bool` | m_bDormant
`bool` | m_bForceParentToBeNetworked
`bitfield:1` | m_bDirtyHierarchy
`bitfield:1` | m_bDirtyBoneMergeInfo
`bitfield:1` | m_bNetworkedPositionChanged
`bitfield:1` | m_bNetworkedAnglesChanged
`bitfield:1` | m_bNetworkedScaleChanged
`bitfield:1` | m_bWillBeCallingPostDataUpdate
`bitfield:1` | m_bBoneMergeFlex
`bitfield:2` | m_nLatchAbsOrigin
`bitfield:1` | m_bDirtyBoneMergeBoneToRoot
`uint8` | m_nHierarchicalDepth
`uint8` | m_nHierarchyType
`uint8` | m_nDoNotSetAnimTimeInInvalidatePhysicsCount
`CUtlStringToken` | m_name
`CUtlStringToken` | m_hierarchyAttachName
`float32` | m_flZOffset
`float32` | m_flClientLocalScale
`Vector` | m_vRenderOrigin

---

## C_IncendiaryGrenade
Derived from: [C_MolotovGrenade](#c_molotovgrenade), [C_BaseCSGrenade](#c_basecsgrenade), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPointScript


Type | Name
------------ | -------------
`CCSPointScriptEntity*` | m_pParent

---

## C_CSObserverPawn
Derived from: [C_CSPlayerPawnBase](#c_csplayerpawnbase), [C_BasePlayerPawn](#c_baseplayerpawn), [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CEntityHandle` | m_hDetectParentChange

---

## C_EntityFlame
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CHandle< C_BaseEntity >` | m_hEntAttached
`CHandle< C_BaseEntity >` | m_hOldAttached
`bool` | m_bCheapEffect

---

## C_Breakable
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSObserver_ObserverServices
Derived from: [CPlayer_ObserverServices](#cplayer_observerservices)

Type | Name
------------ | -------------
`CEntityHandle` | m_hLastObserverTarget
`Vector` | m_vecObserverInterpolateOffset
`Vector` | m_vecObserverInterpStartPos
`float32` | m_flObsInterp_PathLength
`Quaternion` | m_qObsInterp_OrientationStart
`Quaternion` | m_qObsInterp_OrientationTravelDir
`ObserverInterpState_t` | m_obsInterpState
`bool` | m_bObserverInterpolationNeedsDeferredSetup

---

## C_TintController
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPlayer_AutoaimServices


---

## C_Hostage
Derived from: [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`EntitySpottedState_t` | m_entitySpottedState
`CHandle< C_BaseEntity >` | m_leader
`CountdownTimer` | m_reuseTimer
`Vector` | m_vel
`bool` | m_isRescued
`bool` | m_jumpedThisFrame
`int32` | m_nHostageState
`bool` | m_bHandsHaveBeenCut
`CHandle< C_CSPlayerPawn >` | m_hHostageGrabber
`GameTime_t` | m_fLastGrabTime
`Vector` | m_vecGrabbedPos
`GameTime_t` | m_flRescueStartTime
`GameTime_t` | m_flGrabSuccessTime
`GameTime_t` | m_flDropStartTime
`GameTime_t` | m_flDeadOrRescuedTime
`CountdownTimer` | m_blinkTimer
`Vector` | m_lookAt
`CountdownTimer` | m_lookAroundTimer
`bool` | m_isInit
`AttachmentHandle_t` | m_eyeAttachment
`AttachmentHandle_t` | m_chestAttachment
`CBasePlayerController*` | m_pPredictionOwner
`GameTime_t` | m_fNewestAlphaThinkTime

---

## C_Sprite
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CStrongHandle< InfoForResourceTypeIMaterial2 >` | m_hSpriteMaterial
`CHandle< C_BaseEntity >` | m_hAttachedToEntity
`AttachmentHandle_t` | m_nAttachment
`float32` | m_flSpriteFramerate
`float32` | m_flFrame
`GameTime_t` | m_flDieTime
`uint32` | m_nBrightness
`float32` | m_flBrightnessDuration
`float32` | m_flSpriteScale
`float32` | m_flScaleDuration
`bool` | m_bWorldSpaceScale
`float32` | m_flGlowProxySize
`float32` | m_flHDRColorScale
`GameTime_t` | m_flLastTime
`float32` | m_flMaxFrame
`float32` | m_flStartScale
`float32` | m_flDestScale
`GameTime_t` | m_flScaleTimeStart
`int32` | m_nStartBrightness
`int32` | m_nDestBrightness
`GameTime_t` | m_flBrightnessTimeStart
`CWeakHandle< InfoForResourceTypeIMaterial2 >` | m_hOldSpriteMaterial
`int32` | m_nSpriteWidth
`int32` | m_nSpriteHeight

---

## C_WeaponM4A1Silencer
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CMapInfo
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`int32` | m_iBuyingStatus
`float32` | m_flBombRadius
`int32` | m_iPetPopulation
`bool` | m_bUseNormalSpawnsForDM
`bool` | m_bDisableAutoGeneratedDMSpawns
`float32` | m_flBotMaxVisionDistance
`int32` | m_iHostageCount
`bool` | m_bFadePlayerVisibilityFarZ
`bool` | m_bRainTraceToSkyEnabled

---

## C_PlantedC4
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`bool` | m_bBombTicking
`int32` | m_nBombSite
`int32` | m_nSourceSoundscapeHash
`EntitySpottedState_t` | m_entitySpottedState
`GameTime_t` | m_flNextGlow
`GameTime_t` | m_flNextBeep
`GameTime_t` | m_flC4Blow
`bool` | m_bCannotBeDefused
`bool` | m_bHasExploded
`float32` | m_flTimerLength
`bool` | m_bBeingDefused
`float32` | m_bTriggerWarning
`float32` | m_bExplodeWarning
`bool` | m_bC4Activated
`bool` | m_bTenSecWarning
`float32` | m_flDefuseLength
`GameTime_t` | m_flDefuseCountDown
`bool` | m_bBombDefused
`CHandle< C_CSPlayerPawn >` | m_hBombDefuser
`CHandle< C_BaseEntity >` | m_hControlPanel
`C_AttributeContainer` | m_AttributeManager
`CHandle< C_Multimeter >` | m_hDefuserMultimeter
`GameTime_t` | m_flNextRadarFlashTime
`bool` | m_bRadarFlash
`CHandle< C_CSPlayerPawn >` | m_pBombDefuser
`GameTime_t` | m_fLastDefuseTime
`CBasePlayerController*` | m_pPredictionOwner
`Vector` | m_vecC4ExplodeSpectatePos
`QAngle` | m_vecC4ExplodeSpectateAng
`float32` | m_flC4ExplodeSpectateDuration

---

## C_RagdollProp
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`C_NetworkUtlVectorBase< Vector >` | m_ragPos
`C_NetworkUtlVectorBase< QAngle >` | m_ragAngles
`float32` | m_flBlendWeight
`CHandle< C_BaseEntity >` | m_hRagdollSource
`AttachmentHandle_t` | m_iEyeAttachment
`float32` | m_flBlendWeightCurrent
`CUtlVector< int32 >` | m_parentPhysicsBoneIndices
`CUtlVector< int32 >` | m_worldSpaceBoneComputationOrder

---

## C_CSGO_TerroristTeamIntroCamera
Derived from: [C_CSGO_TeamPreviewCamera](#c_csgo_teampreviewcamera), [C_CSGO_MapPreviewCameraPath](#c_csgo_mappreviewcamerapath), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_VoteController
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`int32` | m_iActiveIssueIndex
`int32` | m_iOnlyTeamToVote
`int32[5]` | m_nVoteOptionCount
`int32` | m_nPotentialVotes
`bool` | m_bVotesDirty
`bool` | m_bTypeDirty
`bool` | m_bIsYesNoVote

---

## ViewAngleServerChange_t

Type | Name
------------ | -------------
`FixAngleSet_t` | nType
`QAngle` | qAngle
`uint32` | nIndex

---

## C_Chicken
Derived from: [C_DynamicProp](#c_dynamicprop), [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Type | Name
------------ | -------------
`CHandle< CBaseAnimGraph >` | m_hHolidayHatAddon
`bool` | m_jumpedThisFrame
`CHandle< C_CSPlayerPawn >` | m_leader
`C_AttributeContainer` | m_AttributeManager
`bool` | m_bAttributesInitialized
`ParticleIndex_t` | m_hWaterWakeParticles
`bool` | m_bIsPreviewModel

---

## PhysicsRagdollPose_t

Type | Name
------------ | -------------
`C_NetworkUtlVectorBase< CTransform >` | m_Transforms
`CHandle< C_BaseEntity >` | m_hOwner

