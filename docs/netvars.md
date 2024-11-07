## CCSPlayer_MovementServices

{{ get_arguments_table([
    ["m_vecLadderNormal", "Vector"],
    ["m_nLadderSurfacePropIndex", "int32"],
    ["m_flDuckAmount", "float32"],
    ["m_flDuckSpeed", "float32"],
    ["m_bDuckOverride", "bool"],
    ["m_bDesiresDuck", "bool"],
    ["m_flDuckOffset", "float32"],
    ["m_nDuckTimeMsecs", "uint32"],
    ["m_nDuckJumpTimeMsecs", "uint32"],
    ["m_nJumpTimeMsecs", "uint32"],
    ["m_flLastDuckTime", "float32"],
    ["m_vecLastPositionAtFullCrouchSpeed", "Vector2D"],
    ["m_duckUntilOnGround", "bool"],
    ["m_bHasWalkMovedSinceLastJump", "bool"],
    ["m_bInStuckTest", "bool"],
    ["m_flStuckCheckTime", "float32[64][2]"],
    ["m_nTraceCount", "int32"],
    ["m_StuckLast", "int32"],
    ["m_bSpeedCropped", "bool"],
    ["m_flGroundMoveEfficiency", "float32"],
    ["m_nOldWaterLevel", "int32"],
    ["m_flWaterEntryTime", "float32"],
    ["m_vecForward", "Vector"],
    ["m_vecLeft", "Vector"],
    ["m_vecUp", "Vector"],
    ["m_nGameCodeHasMovedPlayerAfterCommand", "int32"],
    ["m_bOldJumpPressed", "bool"],
    ["m_flJumpPressedTime", "float32"],
    ["m_fStashGrenadeParameterWhen", "GameTime_t"],
    ["m_nButtonDownMaskPrev", "uint64"],
    ["m_flOffsetTickCompleteTime", "float32"],
    ["m_flOffsetTickStashedSpeed", "float32"],
    ["m_flStamina", "float32"],
    ["m_flHeightAtJumpStart", "float32"],
    ["m_flMaxJumpHeightThisJump", "float32"],
    ["m_flMaxJumpHeightLastJump", "float32"],
    ["m_flStaminaAtJumpStart", "float32"],
    ["m_flAccumulatedJumpError", "float32"],
]) }}

## sky3dparams_t

{{ get_arguments_table([
    ["scale", "int16"],
    ["origin", "Vector"],
    ["bClip3DSkyBoxNearToWorldFar", "bool"],
    ["flClip3DSkyBoxNearToWorldFarOffset", "float32"],
    ["fog", "fogparams_t"],
    ["m_nWorldGroupID", "WorldGroupId_t"],
]) }}

## C_Item

{{ get_arguments_table([
    ["m_pReticleHintTextName", "char[256]"],
]) }}

## C_SoundEventPathCornerEntity

{{ get_arguments_table([
    ["m_vecCornerPairsNetworked", "C_NetworkUtlVectorBase< SoundeventPathCornerPairNetworked_t >"],
]) }}

## C_CSGameRules

{{ get_arguments_table([
    ["m_bFreezePeriod", "bool"],
    ["m_bWarmupPeriod", "bool"],
    ["m_fWarmupPeriodEnd", "GameTime_t"],
    ["m_fWarmupPeriodStart", "GameTime_t"],
    ["m_bServerPaused", "bool"],
    ["m_bTerroristTimeOutActive", "bool"],
    ["m_bCTTimeOutActive", "bool"],
    ["m_flTerroristTimeOutRemaining", "float32"],
    ["m_flCTTimeOutRemaining", "float32"],
    ["m_nTerroristTimeOuts", "int32"],
    ["m_nCTTimeOuts", "int32"],
    ["m_bTechnicalTimeOut", "bool"],
    ["m_bMatchWaitingForResume", "bool"],
    ["m_iRoundTime", "int32"],
    ["m_fMatchStartTime", "float32"],
    ["m_fRoundStartTime", "GameTime_t"],
    ["m_flRestartRoundTime", "GameTime_t"],
    ["m_bGameRestart", "bool"],
    ["m_flGameStartTime", "float32"],
    ["m_timeUntilNextPhaseStarts", "float32"],
    ["m_gamePhase", "int32"],
    ["m_totalRoundsPlayed", "int32"],
    ["m_nRoundsPlayedThisPhase", "int32"],
    ["m_nOvertimePlaying", "int32"],
    ["m_iHostagesRemaining", "int32"],
    ["m_bAnyHostageReached", "bool"],
    ["m_bMapHasBombTarget", "bool"],
    ["m_bMapHasRescueZone", "bool"],
    ["m_bMapHasBuyZone", "bool"],
    ["m_bIsQueuedMatchmaking", "bool"],
    ["m_nQueuedMatchmakingMode", "int32"],
    ["m_bIsValveDS", "bool"],
    ["m_bLogoMap", "bool"],
    ["m_bPlayAllStepSoundsOnServer", "bool"],
    ["m_iSpectatorSlotCount", "int32"],
    ["m_MatchDevice", "int32"],
    ["m_bHasMatchStarted", "bool"],
    ["m_nNextMapInMapgroup", "int32"],
    ["m_szTournamentEventName", "char[512]"],
    ["m_szTournamentEventStage", "char[512]"],
    ["m_szMatchStatTxt", "char[512]"],
    ["m_szTournamentPredictionsTxt", "char[512]"],
    ["m_nTournamentPredictionsPct", "int32"],
    ["m_flCMMItemDropRevealStartTime", "GameTime_t"],
    ["m_flCMMItemDropRevealEndTime", "GameTime_t"],
    ["m_bIsDroppingItems", "bool"],
    ["m_bIsQuestEligible", "bool"],
    ["m_bIsHltvActive", "bool"],
    ["m_arrProhibitedItemIndices", "uint16[100]"],
    ["m_arrTournamentActiveCasterAccounts", "uint32[4]"],
    ["m_numBestOfMaps", "int32"],
    ["m_nHalloweenMaskListSeed", "int32"],
    ["m_bBombDropped", "bool"],
    ["m_bBombPlanted", "bool"],
    ["m_iRoundWinStatus", "int32"],
    ["m_eRoundWinReason", "int32"],
    ["m_bTCantBuy", "bool"],
    ["m_bCTCantBuy", "bool"],
    ["m_iMatchStats_RoundResults", "int32[30]"],
    ["m_iMatchStats_PlayersAlive_CT", "int32[30]"],
    ["m_iMatchStats_PlayersAlive_T", "int32[30]"],
    ["m_TeamRespawnWaveTimes", "float32[32]"],
    ["m_flNextRespawnWave", "GameTime_t[32]"],
    ["m_nServerQuestID", "int32"],
    ["m_vMinimapMins", "Vector"],
    ["m_vMinimapMaxs", "Vector"],
    ["m_MinimapVerticalSectionHeights", "float32[8]"],
    ["m_bSpawnedTerrorHuntHeavy", "bool"],
    ["m_nEndMatchMapGroupVoteTypes", "int32[10]"],
    ["m_nEndMatchMapGroupVoteOptions", "int32[10]"],
    ["m_nEndMatchMapVoteWinner", "int32"],
    ["m_iNumConsecutiveCTLoses", "int32"],
    ["m_iNumConsecutiveTerroristLoses", "int32"],
    ["m_bMarkClientStopRecordAtRoundEnd", "bool"],
    ["m_nMatchAbortedEarlyReason", "int32"],
    ["m_bHasTriggeredRoundStartMusic", "bool"],
    ["m_bSwitchingTeamsAtRoundReset", "bool"],
    ["m_pGameModeRules", "CCSGameModeRules*"],
    ["m_RetakeRules", "C_RetakeGameRules"],
    ["m_nMatchEndCount", "uint8"],
    ["m_nTTeamIntroVariant", "int32"],
    ["m_nCTTeamIntroVariant", "int32"],
    ["m_bTeamIntroPeriod", "bool"],
    ["m_iRoundEndWinnerTeam", "int32"],
    ["m_eRoundEndReason", "int32"],
    ["m_bRoundEndShowTimerDefend", "bool"],
    ["m_iRoundEndTimerTime", "int32"],
    ["m_sRoundEndFunFactToken", "CUtlString"],
    ["m_iRoundEndFunFactPlayerSlot", "CPlayerSlot"],
    ["m_iRoundEndFunFactData1", "int32"],
    ["m_iRoundEndFunFactData2", "int32"],
    ["m_iRoundEndFunFactData3", "int32"],
    ["m_sRoundEndMessage", "CUtlString"],
    ["m_iRoundEndPlayerCount", "int32"],
    ["m_bRoundEndNoMusic", "bool"],
    ["m_iRoundEndLegacy", "int32"],
    ["m_nRoundEndCount", "uint8"],
    ["m_iRoundStartRoundNumber", "int32"],
    ["m_nRoundStartCount", "uint8"],
    ["m_flLastPerfSampleTime", "float64"],
]) }}

## CBodyComponentSkeletonInstance

{{ get_arguments_table([
    ["m_skeletonInstance", "CSkeletonInstance"],
]) }}

## C_BaseModelEntity

{{ get_arguments_table([
    ["m_CRenderComponent", "CRenderComponent*"],
    ["m_CHitboxComponent", "CHitboxComponent"],
    ["m_LastHitGroup", "HitGroup_t"],
    ["m_bInitModelEffects", "bool"],
    ["m_bIsStaticProp", "bool"],
    ["m_nLastAddDecal", "int32"],
    ["m_nDecalsAdded", "int32"],
    ["m_iOldHealth", "int32"],
    ["m_nRenderMode", "RenderMode_t"],
    ["m_nRenderFX", "RenderFx_t"],
    ["m_bAllowFadeInView", "bool"],
    ["m_clrRender", "Color"],
    ["m_vecRenderAttributes", "C_UtlVectorEmbeddedNetworkVar< EntityRenderAttribute_t >"],
    ["m_bRenderToCubemaps", "bool"],
    ["m_bNoInterpolate", "bool"],
    ["m_Collision", "CCollisionProperty"],
    ["m_Glow", "CGlowProperty"],
    ["m_flGlowBackfaceMult", "float32"],
    ["m_fadeMinDist", "float32"],
    ["m_fadeMaxDist", "float32"],
    ["m_flFadeScale", "float32"],
    ["m_flShadowStrength", "float32"],
    ["m_nObjectCulling", "uint8"],
    ["m_nAddDecal", "int32"],
    ["m_vDecalPosition", "Vector"],
    ["m_vDecalForwardAxis", "Vector"],
    ["m_flDecalHealBloodRate", "float32"],
    ["m_flDecalHealHeightRate", "float32"],
    ["m_ConfigEntitiesToPropagateMaterialDecalsTo", "C_NetworkUtlVectorBase< CHandle< C_BaseModelEntity > >"],
    ["m_vecViewOffset", "CNetworkViewOffsetVector"],
    ["m_pClientAlphaProperty", "CClientAlphaProperty*"],
    ["m_ClientOverrideTint", "Color"],
    ["m_bUseClientOverrideTint", "bool"],
]) }}

## C_FootstepControl

{{ get_arguments_table([
    ["m_source", "CUtlSymbolLarge"],
    ["m_destination", "CUtlSymbolLarge"],
]) }}

## C_PointClientUIHUD

{{ get_arguments_table([
    ["m_bCheckCSSClasses", "bool"],
    ["m_bIgnoreInput", "bool"],
    ["m_flWidth", "float32"],
    ["m_flHeight", "float32"],
    ["m_flDPI", "float32"],
    ["m_flInteractDistance", "float32"],
    ["m_flDepthOffset", "float32"],
    ["m_unOwnerContext", "uint32"],
    ["m_unHorizontalAlign", "uint32"],
    ["m_unVerticalAlign", "uint32"],
    ["m_unOrientation", "uint32"],
    ["m_bAllowInteractionFromAllSceneWorlds", "bool"],
    ["m_vecCSSClasses", "C_NetworkUtlVectorBase< CUtlSymbolLarge >"],
]) }}

## C_SpotlightEnd

{{ get_arguments_table([
    ["m_flLightScale", "float32"],
    ["m_Radius", "float32"],
]) }}

## CEconItemAttribute

{{ get_arguments_table([
    ["m_iAttributeDefinitionIndex", "uint16"],
    ["m_flValue", "float32"],
    ["m_flInitialValue", "float32"],
    ["m_nRefundableCurrency", "int32"],
    ["m_bSetBonus", "bool"],
]) }}

## C_PointCamera

{{ get_arguments_table([
    ["m_FOV", "float32"],
    ["m_Resolution", "float32"],
    ["m_bFogEnable", "bool"],
    ["m_FogColor", "Color"],
    ["m_flFogStart", "float32"],
    ["m_flFogEnd", "float32"],
    ["m_flFogMaxDensity", "float32"],
    ["m_bActive", "bool"],
    ["m_bUseScreenAspectRatio", "bool"],
    ["m_flAspectRatio", "float32"],
    ["m_bNoSky", "bool"],
    ["m_fBrightness", "float32"],
    ["m_flZFar", "float32"],
    ["m_flZNear", "float32"],
    ["m_bCanHLTVUse", "bool"],
    ["m_bAlignWithParent", "bool"],
    ["m_bDofEnabled", "bool"],
    ["m_flDofNearBlurry", "float32"],
    ["m_flDofNearCrisp", "float32"],
    ["m_flDofFarCrisp", "float32"],
    ["m_flDofFarBlurry", "float32"],
    ["m_flDofTiltToGround", "float32"],
    ["m_TargetFOV", "float32"],
    ["m_DegreesPerSecond", "float32"],
    ["m_bIsOn", "bool"],
    ["m_pNext", "C_PointCamera*"],
]) }}

## C_EnvWind

{{ get_arguments_table([
    ["m_EnvWindShared", "C_EnvWindShared"],
]) }}

## C_BaseCombatCharacter

{{ get_arguments_table([
    ["m_hMyWearables", "C_NetworkUtlVectorBase< CHandle< C_EconWearable > >"],
    ["m_leftFootAttachment", "AttachmentHandle_t"],
    ["m_rightFootAttachment", "AttachmentHandle_t"],
    ["m_nWaterWakeMode", "C_BaseCombatCharacter::WaterWakeMode_t"],
    ["m_flWaterWorldZ", "float32"],
    ["m_flWaterNextTraceTime", "float32"],
]) }}

## C_SoundEventSphereEntity

{{ get_arguments_table([
    ["m_flRadius", "float32"],
]) }}

## C_SceneEntity

{{ get_arguments_table([
    ["m_bIsPlayingBack", "bool"],
    ["m_bPaused", "bool"],
    ["m_bMultiplayer", "bool"],
    ["m_bAutogenerated", "bool"],
    ["m_flForceClientTime", "float32"],
    ["m_nSceneStringIndex", "uint16"],
    ["m_bClientOnly", "bool"],
    ["m_hOwner", "CHandle< C_BaseFlex >"],
    ["m_hActorList", "C_NetworkUtlVectorBase< CHandle< C_BaseFlex > >"],
    ["m_bWasPlaying", "bool"],
    ["m_QueuedEvents", "CUtlVector< C_SceneEntity::QueuedEvents_t >"],
    ["m_flCurrentTime", "float32"],
]) }}

## CPlayer_CameraServices

{{ get_arguments_table([
    ["m_vecCsViewPunchAngle", "QAngle"],
    ["m_nCsViewPunchAngleTick", "GameTick_t"],
    ["m_flCsViewPunchAngleTickRatio", "float32"],
    ["m_PlayerFog", "C_fogplayerparams_t"],
    ["m_hColorCorrectionCtrl", "CHandle< C_ColorCorrection >"],
    ["m_hViewEntity", "CHandle< C_BaseEntity >"],
    ["m_hTonemapController", "CHandle< C_TonemapController2 >"],
    ["m_audio", "audioparams_t"],
    ["m_PostProcessingVolumes", "C_NetworkUtlVectorBase< CHandle< C_PostProcessingVolume > >"],
    ["m_flOldPlayerZ", "float32"],
    ["m_flOldPlayerViewOffsetZ", "float32"],
    ["m_CurrentFog", "fogparams_t"],
    ["m_hOldFogController", "CHandle< C_FogController >"],
    ["m_bOverrideFogColor", "bool[5]"],
    ["m_OverrideFogColor", "Color[5]"],
    ["m_bOverrideFogStartEnd", "bool[5]"],
    ["m_fOverrideFogStart", "float32[5]"],
    ["m_fOverrideFogEnd", "float32[5]"],
    ["m_hActivePostProcessingVolume", "CHandle< C_PostProcessingVolume >"],
    ["m_angDemoViewAngles", "QAngle"],
]) }}

## C_BaseCSGrenade

{{ get_arguments_table([
    ["m_bClientPredictDelete", "bool"],
    ["m_bRedraw", "bool"],
    ["m_bIsHeldByPlayer", "bool"],
    ["m_bPinPulled", "bool"],
    ["m_bJumpThrow", "bool"],
    ["m_bThrowAnimating", "bool"],
    ["m_fThrowTime", "GameTime_t"],
    ["m_flThrowStrength", "float32"],
    ["m_flThrowStrengthApproach", "float32"],
    ["m_fDropTime", "GameTime_t"],
    ["m_fPinPullTime", "GameTime_t"],
    ["m_bJustPulledPin", "bool"],
    ["m_nNextHoldTick", "GameTick_t"],
    ["m_flNextHoldFrac", "float32"],
    ["m_hSwitchToWeaponAfterThrow", "CHandle< C_CSWeaponBase >"],
]) }}

## C_FuncMonitor

{{ get_arguments_table([
    ["m_targetCamera", "CUtlString"],
    ["m_nResolutionEnum", "int32"],
    ["m_bRenderShadows", "bool"],
    ["m_bUseUniqueColorTarget", "bool"],
    ["m_brushModelName", "CUtlString"],
    ["m_hTargetCamera", "CHandle< C_BaseEntity >"],
    ["m_bEnabled", "bool"],
    ["m_bDraw3DSkybox", "bool"],
]) }}

## C_RopeKeyframe::CPhysicsDelegate

{{ get_arguments_table([
    ["m_pKeyframe", "C_RopeKeyframe*"],
]) }}

## CBodyComponent

{{ get_arguments_table([
    ["m_pSceneNode", "CGameSceneNode*"],
    ["__m_pChainEntity", "CNetworkVarChainer"],
]) }}

## C_SoundAreaEntitySphere

{{ get_arguments_table([
    ["m_flRadius", "float32"],
]) }}

## C_LightGlow

{{ get_arguments_table([
    ["m_nHorizontalSize", "uint32"],
    ["m_nVerticalSize", "uint32"],
    ["m_nMinDist", "uint32"],
    ["m_nMaxDist", "uint32"],
    ["m_nOuterMaxDist", "uint32"],
    ["m_flGlowProxySize", "float32"],
    ["m_flHDRColorScale", "float32"],
    ["m_GlowOverlay", "C_LightGlowOverlay"],
]) }}

## CountdownTimer

{{ get_arguments_table([
    ["m_duration", "float32"],
    ["m_timestamp", "GameTime_t"],
    ["m_timescale", "float32"],
    ["m_nWorldGroupId", "WorldGroupId_t"],
]) }}

## CGameSceneNodeHandle

{{ get_arguments_table([
    ["m_hOwner", "CEntityHandle"],
    ["m_name", "CUtlStringToken"],
]) }}

## PredictedDamageTag_t

{{ get_arguments_table([
    ["nTagTick", "GameTick_t"],
    ["flFlinchModSmall", "float32"],
    ["flFlinchModLarge", "float32"],
    ["flFriendlyFireDamageReductionRatio", "float32"],
]) }}

## C_ClientRagdoll

{{ get_arguments_table([
    ["m_bFadeOut", "bool"],
    ["m_bImportant", "bool"],
    ["m_flEffectTime", "GameTime_t"],
    ["m_gibDespawnTime", "GameTime_t"],
    ["m_iCurrentFriction", "int32"],
    ["m_iMinFriction", "int32"],
    ["m_iMaxFriction", "int32"],
    ["m_iFrictionAnimState", "int32"],
    ["m_bReleaseRagdoll", "bool"],
    ["m_iEyeAttachment", "AttachmentHandle_t"],
    ["m_bFadingOut", "bool"],
    ["m_flScaleEnd", "float32[10]"],
    ["m_flScaleTimeStart", "GameTime_t[10]"],
    ["m_flScaleTimeEnd", "GameTime_t[10]"],
]) }}

## C_GlobalLight

{{ get_arguments_table([
    ["m_WindClothForceHandle", "uint16"],
]) }}

## C_CSPlayerResource

{{ get_arguments_table([
    ["m_bHostageAlive", "bool[12]"],
    ["m_isHostageFollowingSomeone", "bool[12]"],
    ["m_iHostageEntityIDs", "CEntityIndex[12]"],
    ["m_bombsiteCenterA", "Vector"],
    ["m_bombsiteCenterB", "Vector"],
    ["m_hostageRescueX", "int32[4]"],
    ["m_hostageRescueY", "int32[4]"],
    ["m_hostageRescueZ", "int32[4]"],
    ["m_bEndMatchNextMapAllVoted", "bool"],
    ["m_foundGoalPositions", "bool"],
]) }}

## CSkeletonInstance

{{ get_arguments_table([
    ["m_modelState", "CModelState"],
    ["m_bIsAnimationEnabled", "bool"],
    ["m_bUseParentRenderBounds", "bool"],
    ["m_bDisableSolidCollisionsForHierarchy", "bool"],
    ["m_bDirtyMotionType", "bitfield:1"],
    ["m_bIsGeneratingLatchedParentSpaceState", "bitfield:1"],
    ["m_materialGroup", "CUtlStringToken"],
    ["m_nHitboxSet", "uint8"],
]) }}

## CBodyComponentBaseAnimGraph

{{ get_arguments_table([
    ["m_animationController", "CBaseAnimGraphController"],
]) }}

## CBodyComponentPoint

{{ get_arguments_table([
    ["m_sceneNode", "CGameSceneNode"],
]) }}

## C_SmokeGrenadeProjectile

{{ get_arguments_table([
    ["m_nSmokeEffectTickBegin", "int32"],
    ["m_bDidSmokeEffect", "bool"],
    ["m_nRandomSeed", "int32"],
    ["m_vSmokeColor", "Vector"],
    ["m_vSmokeDetonationPos", "Vector"],
    ["m_VoxelFrameData", "C_NetworkUtlVectorBase< uint8 >"],
    ["m_nVoxelFrameDataSize", "int32"],
    ["m_nVoxelUpdate", "int32"],
    ["m_bSmokeVolumeDataReceived", "bool"],
    ["m_bSmokeEffectSpawned", "bool"],
]) }}

## C_CSGO_MapPreviewCameraPath

{{ get_arguments_table([
    ["m_flZFar", "float32"],
    ["m_flZNear", "float32"],
    ["m_bLoop", "bool"],
    ["m_bVerticalFOV", "bool"],
    ["m_bConstantSpeed", "bool"],
    ["m_flDuration", "float32"],
    ["m_flPathLength", "float32"],
    ["m_flPathDuration", "float32"],
]) }}

## C_Inferno

{{ get_arguments_table([
    ["m_nfxFireDamageEffect", "ParticleIndex_t"],
    ["m_hInfernoPointsSnapshot", "CStrongHandle< InfoForResourceTypeIParticleSnapshot >"],
    ["m_hInfernoFillerPointsSnapshot", "CStrongHandle< InfoForResourceTypeIParticleSnapshot >"],
    ["m_hInfernoOutlinePointsSnapshot", "CStrongHandle< InfoForResourceTypeIParticleSnapshot >"],
    ["m_hInfernoClimbingOutlinePointsSnapshot", "CStrongHandle< InfoForResourceTypeIParticleSnapshot >"],
    ["m_hInfernoDecalsSnapshot", "CStrongHandle< InfoForResourceTypeIParticleSnapshot >"],
    ["m_firePositions", "Vector[64]"],
    ["m_fireParentPositions", "Vector[64]"],
    ["m_bFireIsBurning", "bool[64]"],
    ["m_BurnNormal", "Vector[64]"],
    ["m_fireCount", "int32"],
    ["m_nInfernoType", "int32"],
    ["m_nFireLifetime", "float32"],
    ["m_bInPostEffectTime", "bool"],
    ["m_lastFireCount", "int32"],
    ["m_nFireEffectTickBegin", "int32"],
    ["m_drawableCount", "int32"],
    ["m_blosCheck", "bool"],
    ["m_nlosperiod", "int32"],
    ["m_maxFireHalfWidth", "float32"],
    ["m_maxFireHeight", "float32"],
    ["m_minBounds", "Vector"],
    ["m_maxBounds", "Vector"],
    ["m_flLastGrassBurnThink", "float32"],
]) }}

## C_PlayerPing

{{ get_arguments_table([
    ["m_hPlayer", "CHandle< C_CSPlayerPawn >"],
    ["m_hPingedEntity", "CHandle< C_BaseEntity >"],
    ["m_iType", "int32"],
    ["m_bUrgent", "bool"],
    ["m_szPlaceName", "char[18]"],
]) }}

## C_CSTeam

{{ get_arguments_table([
    ["m_szTeamMatchStat", "char[512]"],
    ["m_numMapVictories", "int32"],
    ["m_bSurrendered", "bool"],
    ["m_scoreFirstHalf", "int32"],
    ["m_scoreSecondHalf", "int32"],
    ["m_scoreOvertime", "int32"],
    ["m_szClanTeamname", "char[129]"],
    ["m_iClanID", "uint32"],
    ["m_szTeamFlagImage", "char[8]"],
    ["m_szTeamLogoImage", "char[8]"],
]) }}

## C_CSGO_MapPreviewCameraPathNode

{{ get_arguments_table([
    ["m_szParentPathUniqueID", "CUtlSymbolLarge"],
    ["m_nPathIndex", "int32"],
    ["m_vInTangentLocal", "Vector"],
    ["m_vOutTangentLocal", "Vector"],
    ["m_flFOV", "float32"],
    ["m_flCameraSpeed", "float32"],
    ["m_flEaseIn", "float32"],
    ["m_flEaseOut", "float32"],
    ["m_vInTangentWorld", "Vector"],
    ["m_vOutTangentWorld", "Vector"],
]) }}

## C_CSPlayerPawn

{{ get_arguments_table([
    ["m_pBulletServices", "CCSPlayer_BulletServices*"],
    ["m_pHostageServices", "CCSPlayer_HostageServices*"],
    ["m_pBuyServices", "CCSPlayer_BuyServices*"],
    ["m_pGlowServices", "CCSPlayer_GlowServices*"],
    ["m_pActionTrackingServices", "CCSPlayer_ActionTrackingServices*"],
    ["m_pDamageReactServices", "CCSPlayer_DamageReactServices*"],
    ["m_flHealthShotBoostExpirationTime", "GameTime_t"],
    ["m_flLastFiredWeaponTime", "GameTime_t"],
    ["m_bHasFemaleVoice", "bool"],
    ["m_flLandingTimeSeconds", "float32"],
    ["m_flOldFallVelocity", "float32"],
    ["m_szLastPlaceName", "char[18]"],
    ["m_bPrevDefuser", "bool"],
    ["m_bPrevHelmet", "bool"],
    ["m_nPrevArmorVal", "int32"],
    ["m_nPrevGrenadeAmmoCount", "int32"],
    ["m_unPreviousWeaponHash", "uint32"],
    ["m_unWeaponHash", "uint32"],
    ["m_bInBuyZone", "bool"],
    ["m_bPreviouslyInBuyZone", "bool"],
    ["m_aimPunchAngle", "QAngle"],
    ["m_aimPunchAngleVel", "QAngle"],
    ["m_aimPunchTickBase", "int32"],
    ["m_aimPunchTickFraction", "float32"],
    ["m_aimPunchCache", "CUtlVector< QAngle >"],
    ["m_bInLanding", "bool"],
    ["m_flLandingStartTime", "float32"],
    ["m_bInHostageRescueZone", "bool"],
    ["m_bInBombZone", "bool"],
    ["m_bIsBuyMenuOpen", "bool"],
    ["m_flTimeOfLastInjury", "GameTime_t"],
    ["m_flNextSprayDecalTime", "GameTime_t"],
    ["m_iRetakesOffering", "int32"],
    ["m_iRetakesOfferingCard", "int32"],
    ["m_bRetakesHasDefuseKit", "bool"],
    ["m_bRetakesMVPLastRound", "bool"],
    ["m_iRetakesMVPBoostItem", "int32"],
    ["m_RetakesMVPBoostExtraUtility", "loadout_slot_t"],
    ["m_bNeedToReApplyGloves", "bool"],
    ["m_EconGloves", "C_EconItemView"],
    ["m_nEconGlovesChanged", "uint8"],
    ["m_bMustSyncRagdollState", "bool"],
    ["m_nRagdollDamageBone", "int32"],
    ["m_vRagdollDamageForce", "Vector"],
    ["m_vRagdollDamagePosition", "Vector"],
    ["m_szRagdollDamageWeaponName", "char[64]"],
    ["m_bRagdollDamageHeadshot", "bool"],
    ["m_vRagdollServerOrigin", "Vector"],
    ["m_bLastHeadBoneTransformIsValid", "bool"],
    ["m_lastLandTime", "GameTime_t"],
    ["m_bOnGroundLastTick", "bool"],
    ["m_qDeathEyeAngles", "QAngle"],
    ["m_bSkipOneHeadConstraintUpdate", "bool"],
    ["m_bLeftHanded", "bool"],
    ["m_fSwitchedHandednessTime", "GameTime_t"],
    ["m_flViewmodelOffsetX", "float32"],
    ["m_flViewmodelOffsetY", "float32"],
    ["m_flViewmodelOffsetZ", "float32"],
    ["m_flViewmodelFOV", "float32"],
    ["m_vecPlayerPatchEconIndices", "uint32[5]"],
    ["m_GunGameImmunityColor", "Color"],
    ["m_vecBulletHitModels", "CUtlVector< C_BulletHitModel* >"],
    ["m_bIsWalking", "bool"],
    ["m_thirdPersonHeading", "QAngle"],
    ["m_flSlopeDropOffset", "float32"],
    ["m_flSlopeDropHeight", "float32"],
    ["m_vHeadConstraintOffset", "Vector"],
    ["m_entitySpottedState", "EntitySpottedState_t"],
    ["m_bIsScoped", "bool"],
    ["m_bResumeZoom", "bool"],
    ["m_bIsDefusing", "bool"],
    ["m_bIsGrabbingHostage", "bool"],
    ["m_iBlockingUseActionInProgress", "CSPlayerBlockingUseAction_t"],
    ["m_flEmitSoundTime", "GameTime_t"],
    ["m_bInNoDefuseArea", "bool"],
    ["m_nWhichBombZone", "int32"],
    ["m_iShotsFired", "int32"],
    ["m_flFlinchStack", "float32"],
    ["m_flVelocityModifier", "float32"],
    ["m_flHitHeading", "float32"],
    ["m_nHitBodyPart", "int32"],
    ["m_bWaitForNoAttack", "bool"],
    ["m_ignoreLadderJumpTime", "float32"],
    ["m_bKilledByHeadshot", "bool"],
    ["m_ArmorValue", "int32"],
    ["m_unCurrentEquipmentValue", "uint16"],
    ["m_unRoundStartEquipmentValue", "uint16"],
    ["m_unFreezetimeEndEquipmentValue", "uint16"],
    ["m_nLastKillerIndex", "CEntityIndex"],
    ["m_bOldIsScoped", "bool"],
    ["m_bHasDeathInfo", "bool"],
    ["m_flDeathInfoTime", "float32"],
    ["m_vecDeathInfoOrigin", "Vector"],
    ["m_grenadeParameterStashTime", "GameTime_t"],
    ["m_bGrenadeParametersStashed", "bool"],
    ["m_angStashedShootAngles", "QAngle"],
    ["m_vecStashedGrenadeThrowPosition", "Vector"],
    ["m_vecStashedVelocity", "Vector"],
    ["m_angShootAngleHistory", "QAngle[2]"],
    ["m_vecThrowPositionHistory", "Vector[2]"],
    ["m_vecVelocityHistory", "Vector[2]"],
    ["m_PredictedDamageTags", "C_UtlVectorEmbeddedNetworkVar< PredictedDamageTag_t >"],
    ["m_nPrevHighestReceivedDamageTagTick", "GameTick_t"],
    ["m_nHighestAppliedDamageTagTick", "int32"],
]) }}

## C_RagdollPropAttached

{{ get_arguments_table([
    ["m_boneIndexAttached", "uint32"],
    ["m_ragdollAttachedObjectIndex", "uint32"],
    ["m_attachmentPointBoneSpace", "Vector"],
    ["m_attachmentPointRagdollSpace", "Vector"],
    ["m_vecOffset", "Vector"],
    ["m_parentTime", "float32"],
    ["m_bHasParent", "bool"],
]) }}

## C_BaseCSGrenadeProjectile

{{ get_arguments_table([
    ["m_vInitialPosition", "Vector"],
    ["m_vInitialVelocity", "Vector"],
    ["m_nBounces", "int32"],
    ["m_nExplodeEffectIndex", "CStrongHandle< InfoForResourceTypeIParticleSystemDefinition >"],
    ["m_nExplodeEffectTickBegin", "int32"],
    ["m_vecExplodeEffectOrigin", "Vector"],
    ["m_flSpawnTime", "GameTime_t"],
    ["vecLastTrailLinePos", "Vector"],
    ["flNextTrailLineTime", "GameTime_t"],
    ["m_bExplodeEffectBegan", "bool"],
    ["m_bCanCreateGrenadeTrail", "bool"],
    ["m_nSnapshotTrajectoryEffectIndex", "ParticleIndex_t"],
    ["m_hSnapshotTrajectoryParticleSnapshot", "CStrongHandle< InfoForResourceTypeIParticleSnapshot >"],
    ["m_arrTrajectoryTrailPoints", "CUtlVector< Vector >"],
    ["m_arrTrajectoryTrailPointCreationTimes", "CUtlVector< float32 >"],
    ["m_flTrajectoryTrailEffectCreationTime", "float32"],
]) }}

## C_BaseTrigger

{{ get_arguments_table([
    ["m_bDisabled", "bool"],
    ["m_bClientSidePredicted", "bool"],
]) }}

## C_WeaponBaseItem

{{ get_arguments_table([
    ["m_SequenceCompleteTimer", "CountdownTimer"],
    ["m_bRedraw", "bool"],
]) }}

## CEffectData

{{ get_arguments_table([
    ["m_vOrigin", "Vector"],
    ["m_vStart", "Vector"],
    ["m_vNormal", "Vector"],
    ["m_vAngles", "QAngle"],
    ["m_hEntity", "CEntityHandle"],
    ["m_hOtherEntity", "CEntityHandle"],
    ["m_flScale", "float32"],
    ["m_flMagnitude", "float32"],
    ["m_flRadius", "float32"],
    ["m_nSurfaceProp", "CUtlStringToken"],
    ["m_nEffectIndex", "CWeakHandle< InfoForResourceTypeIParticleSystemDefinition >"],
    ["m_nDamageType", "uint32"],
    ["m_nPenetrate", "uint8"],
    ["m_nMaterial", "uint16"],
    ["m_nHitBox", "uint16"],
    ["m_nColor", "uint8"],
    ["m_fFlags", "uint8"],
    ["m_nAttachmentIndex", "AttachmentHandle_t"],
    ["m_nAttachmentName", "CUtlStringToken"],
    ["m_iEffectName", "uint16"],
    ["m_nExplosionType", "uint8"],
]) }}

## C_BaseButton

{{ get_arguments_table([
    ["m_glowEntity", "CHandle< C_BaseModelEntity >"],
    ["m_usable", "bool"],
    ["m_szDisplayText", "CUtlSymbolLarge"],
]) }}

## CCSPlayer_ViewModelServices

{{ get_arguments_table([
    ["m_hViewModel", "CHandle< C_BaseViewModel >[3]"],
]) }}

## CPlayer_MovementServices_Humanoid

{{ get_arguments_table([
    ["m_flStepSoundTime", "float32"],
    ["m_flFallVelocity", "float32"],
    ["m_bInCrouch", "bool"],
    ["m_nCrouchState", "uint32"],
    ["m_flCrouchTransitionStartTime", "GameTime_t"],
    ["m_bDucked", "bool"],
    ["m_bDucking", "bool"],
    ["m_bInDuckJump", "bool"],
    ["m_groundNormal", "Vector"],
    ["m_flSurfaceFriction", "float32"],
    ["m_surfaceProps", "CUtlStringToken"],
    ["m_nStepside", "int32"],
]) }}

## C_PointClientUIWorldPanel

{{ get_arguments_table([
    ["m_bForceRecreateNextUpdate", "bool"],
    ["m_bMoveViewToPlayerNextThink", "bool"],
    ["m_bCheckCSSClasses", "bool"],
    ["m_anchorDeltaTransform", "CTransform"],
    ["m_pOffScreenIndicator", "CPointOffScreenIndicatorUi*"],
    ["m_bIgnoreInput", "bool"],
    ["m_bLit", "bool"],
    ["m_bFollowPlayerAcrossTeleport", "bool"],
    ["m_flWidth", "float32"],
    ["m_flHeight", "float32"],
    ["m_flDPI", "float32"],
    ["m_flInteractDistance", "float32"],
    ["m_flDepthOffset", "float32"],
    ["m_unOwnerContext", "uint32"],
    ["m_unHorizontalAlign", "uint32"],
    ["m_unVerticalAlign", "uint32"],
    ["m_unOrientation", "uint32"],
    ["m_bAllowInteractionFromAllSceneWorlds", "bool"],
    ["m_vecCSSClasses", "C_NetworkUtlVectorBase< CUtlSymbolLarge >"],
    ["m_bOpaque", "bool"],
    ["m_bNoDepth", "bool"],
    ["m_bRenderBackface", "bool"],
    ["m_bUseOffScreenIndicator", "bool"],
    ["m_bExcludeFromSaveGames", "bool"],
    ["m_bGrabbable", "bool"],
    ["m_bOnlyRenderToTexture", "bool"],
    ["m_bDisableMipGen", "bool"],
    ["m_nExplicitImageLayout", "int32"],
]) }}

## CCSGameModeRules_Deathmatch

{{ get_arguments_table([
    ["m_flDMBonusStartTime", "GameTime_t"],
    ["m_flDMBonusTimeLength", "float32"],
    ["m_sDMBonusWeapon", "CUtlString"],
]) }}

## C_GameRules

{{ get_arguments_table([
    ["__m_pChainEntity", "CNetworkVarChainer"],
    ["m_nTotalPausedTicks", "int32"],
    ["m_nPauseStartTick", "int32"],
    ["m_bGamePaused", "bool"],
]) }}

## C_Team

{{ get_arguments_table([
    ["m_aPlayerControllers", "C_NetworkUtlVectorBase< CHandle< CBasePlayerController > >"],
    ["m_aPlayers", "C_NetworkUtlVectorBase< CHandle< C_BasePlayerPawn > >"],
    ["m_iScore", "int32"],
    ["m_szTeamname", "char[129]"],
]) }}

## C_SoundAreaEntityOrientedBox

{{ get_arguments_table([
    ["m_vMin", "Vector"],
    ["m_vMax", "Vector"],
]) }}

## C_TextureBasedAnimatable

{{ get_arguments_table([
    ["m_bLoop", "bool"],
    ["m_flFPS", "float32"],
    ["m_hPositionKeys", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_hRotationKeys", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_vAnimationBoundsMin", "Vector"],
    ["m_vAnimationBoundsMax", "Vector"],
    ["m_flStartTime", "float32"],
    ["m_flStartFrame", "float32"],
]) }}

## CCSPlayer_WaterServices

{{ get_arguments_table([
    ["m_flWaterJumpTime", "float32"],
    ["m_vecWaterJumpVel", "Vector"],
    ["m_flSwimSoundTime", "float32"],
]) }}

## CSkyboxReference

{{ get_arguments_table([
    ["m_worldGroupId", "WorldGroupId_t"],
    ["m_hSkyCamera", "CHandle< C_SkyCamera >"],
]) }}

## CProjectedTextureBase

{{ get_arguments_table([
    ["m_hTargetEntity", "CHandle< C_BaseEntity >"],
    ["m_bState", "bool"],
    ["m_bAlwaysUpdate", "bool"],
    ["m_flLightFOV", "float32"],
    ["m_bEnableShadows", "bool"],
    ["m_bSimpleProjection", "bool"],
    ["m_bLightOnlyTarget", "bool"],
    ["m_bLightWorld", "bool"],
    ["m_bCameraSpace", "bool"],
    ["m_flBrightnessScale", "float32"],
    ["m_LightColor", "Color"],
    ["m_flIntensity", "float32"],
    ["m_flLinearAttenuation", "float32"],
    ["m_flQuadraticAttenuation", "float32"],
    ["m_bVolumetric", "bool"],
    ["m_flVolumetricIntensity", "float32"],
    ["m_flNoiseStrength", "float32"],
    ["m_flFlashlightTime", "float32"],
    ["m_nNumPlanes", "uint32"],
    ["m_flPlaneOffset", "float32"],
    ["m_flColorTransitionTime", "float32"],
    ["m_flAmbient", "float32"],
    ["m_SpotlightTextureName", "char[512]"],
    ["m_nSpotlightTextureFrame", "int32"],
    ["m_nShadowQuality", "uint32"],
    ["m_flNearZ", "float32"],
    ["m_flFarZ", "float32"],
    ["m_flProjectionSize", "float32"],
    ["m_flRotation", "float32"],
    ["m_bFlipHorizontal", "bool"],
]) }}

## CCSPlayerController_InventoryServices

{{ get_arguments_table([
    ["m_unMusicID", "uint16"],
    ["m_rank", "MedalRank_t[6]"],
    ["m_nPersonaDataPublicLevel", "int32"],
    ["m_nPersonaDataPublicCommendsLeader", "int32"],
    ["m_nPersonaDataPublicCommendsTeacher", "int32"],
    ["m_nPersonaDataPublicCommendsFriendly", "int32"],
    ["m_nPersonaDataXpTrailLevel", "int32"],
    ["m_vecServerAuthoritativeWeaponSlots", "C_UtlVectorEmbeddedNetworkVar< ServerAuthoritativeWeaponSlot_t >"],
]) }}

## C_CSGOViewModel

{{ get_arguments_table([
    ["m_bShouldIgnoreOffsetAndAccuracy", "bool"],
    ["m_nLastKnownAssociatedWeaponEntIndex", "CEntityIndex"],
    ["m_bNeedToQueueHighResComposite", "bool"],
    ["m_vLoweredWeaponOffset", "QAngle"],
]) }}

## CScriptComponent

{{ get_arguments_table([
    ["m_scriptClassName", "CUtlSymbolLarge"],
]) }}

## C_EnvLightProbeVolume

{{ get_arguments_table([
    ["m_Entity_hLightProbeTexture", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_Entity_hLightProbeDirectLightIndicesTexture", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_Entity_hLightProbeDirectLightScalarsTexture", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_Entity_hLightProbeDirectLightShadowsTexture", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_Entity_vBoxMins", "Vector"],
    ["m_Entity_vBoxMaxs", "Vector"],
    ["m_Entity_bMoveable", "bool"],
    ["m_Entity_nHandshake", "int32"],
    ["m_Entity_nPriority", "int32"],
    ["m_Entity_bStartDisabled", "bool"],
    ["m_Entity_nLightProbeSizeX", "int32"],
    ["m_Entity_nLightProbeSizeY", "int32"],
    ["m_Entity_nLightProbeSizeZ", "int32"],
    ["m_Entity_nLightProbeAtlasX", "int32"],
    ["m_Entity_nLightProbeAtlasY", "int32"],
    ["m_Entity_nLightProbeAtlasZ", "int32"],
    ["m_Entity_bEnabled", "bool"],
]) }}

## C_ViewmodelAttachmentModel

{{ get_arguments_table([
    ["m_bShouldFrontFaceCullLeftHanded", "bool"],
    ["m_bCreatedLeftHanded", "bool"],
]) }}

## CSPerRoundStats_t

{{ get_arguments_table([
    ["m_iKills", "int32"],
    ["m_iDeaths", "int32"],
    ["m_iAssists", "int32"],
    ["m_iDamage", "int32"],
    ["m_iEquipmentValue", "int32"],
    ["m_iMoneySaved", "int32"],
    ["m_iKillReward", "int32"],
    ["m_iLiveTime", "int32"],
    ["m_iHeadShotKills", "int32"],
    ["m_iObjective", "int32"],
    ["m_iCashEarned", "int32"],
    ["m_iUtilityDamage", "int32"],
    ["m_iEnemiesFlashed", "int32"],
]) }}

## CRagdollManager

{{ get_arguments_table([
    ["m_iCurrentMaxRagdollCount", "int8"],
]) }}

## C_TeamRoundTimer

{{ get_arguments_table([
    ["m_bTimerPaused", "bool"],
    ["m_flTimeRemaining", "float32"],
    ["m_flTimerEndTime", "GameTime_t"],
    ["m_bIsDisabled", "bool"],
    ["m_bShowInHUD", "bool"],
    ["m_nTimerLength", "int32"],
    ["m_nTimerInitialLength", "int32"],
    ["m_nTimerMaxLength", "int32"],
    ["m_bAutoCountdown", "bool"],
    ["m_nSetupTimeLength", "int32"],
    ["m_nState", "int32"],
    ["m_bStartPaused", "bool"],
    ["m_bInCaptureWatchState", "bool"],
    ["m_flTotalTime", "float32"],
    ["m_bStopWatchTimer", "bool"],
    ["m_bFireFinished", "bool"],
    ["m_bFire5MinRemain", "bool"],
    ["m_bFire4MinRemain", "bool"],
    ["m_bFire3MinRemain", "bool"],
    ["m_bFire2MinRemain", "bool"],
    ["m_bFire1MinRemain", "bool"],
    ["m_bFire30SecRemain", "bool"],
    ["m_bFire10SecRemain", "bool"],
    ["m_bFire5SecRemain", "bool"],
    ["m_bFire4SecRemain", "bool"],
    ["m_bFire3SecRemain", "bool"],
    ["m_bFire2SecRemain", "bool"],
    ["m_bFire1SecRemain", "bool"],
    ["m_nOldTimerLength", "int32"],
    ["m_nOldTimerState", "int32"],
]) }}

## WeaponPurchaseCount_t

{{ get_arguments_table([
    ["m_nItemDefIndex", "uint16"],
    ["m_nCount", "uint16"],
]) }}

## CPathSimple

{{ get_arguments_table([
    ["m_pathString", "CUtlString"],
]) }}

## CCSPlayerBase_CameraServices

{{ get_arguments_table([
    ["m_iFOV", "uint32"],
    ["m_iFOVStart", "uint32"],
    ["m_flFOVTime", "GameTime_t"],
    ["m_flFOVRate", "float32"],
    ["m_hZoomOwner", "CHandle< C_BaseEntity >"],
    ["m_flLastShotFOV", "float32"],
]) }}

## CPointOffScreenIndicatorUi

{{ get_arguments_table([
    ["m_bBeenEnabled", "bool"],
    ["m_bHide", "bool"],
    ["m_flSeenTargetTime", "float32"],
    ["m_pTargetPanel", "C_PointClientUIWorldPanel*"],
]) }}

## C_CSWeaponBaseGun

{{ get_arguments_table([
    ["m_zoomLevel", "int32"],
    ["m_iBurstShotsRemaining", "int32"],
    ["m_iSilencerBodygroup", "int32"],
    ["m_silencedModelIndex", "int32"],
    ["m_inPrecache", "bool"],
    ["m_bNeedsBoltAction", "bool"],
]) }}

## C_SkyCamera

{{ get_arguments_table([
    ["m_skyboxData", "sky3dparams_t"],
    ["m_skyboxSlotToken", "CUtlStringToken"],
    ["m_bUseAngles", "bool"],
    ["m_pNext", "C_SkyCamera*"],
]) }}

## C_EntityDissolve

{{ get_arguments_table([
    ["m_flStartTime", "GameTime_t"],
    ["m_flFadeInStart", "float32"],
    ["m_flFadeInLength", "float32"],
    ["m_flFadeOutModelStart", "float32"],
    ["m_flFadeOutModelLength", "float32"],
    ["m_flFadeOutStart", "float32"],
    ["m_flFadeOutLength", "float32"],
    ["m_flNextSparkTime", "GameTime_t"],
    ["m_nDissolveType", "EntityDisolveType_t"],
    ["m_vDissolverOrigin", "Vector"],
    ["m_nMagnitude", "uint32"],
    ["m_bCoreExplode", "bool"],
    ["m_bLinkedToServerEnt", "bool"],
]) }}

## C_fogplayerparams_t

{{ get_arguments_table([
    ["m_hCtrl", "CHandle< C_FogController >"],
    ["m_flTransitionTime", "float32"],
    ["m_OldColor", "Color"],
    ["m_flOldStart", "float32"],
    ["m_flOldEnd", "float32"],
    ["m_flOldMaxDensity", "float32"],
    ["m_flOldHDRColorScale", "float32"],
    ["m_flOldFarZ", "float32"],
    ["m_NewColor", "Color"],
    ["m_flNewStart", "float32"],
    ["m_flNewEnd", "float32"],
    ["m_flNewMaxDensity", "float32"],
    ["m_flNewHDRColorScale", "float32"],
    ["m_flNewFarZ", "float32"],
]) }}

## C_CSPlayerPawnBase

{{ get_arguments_table([
    ["m_pPingServices", "CCSPlayer_PingServices*"],
    ["m_pViewModelServices", "CPlayer_ViewModelServices*"],
    ["m_fRenderingClipPlane", "float32[4]"],
    ["m_nLastClipPlaneSetupFrame", "int32"],
    ["m_vecLastClipCameraPos", "Vector"],
    ["m_vecLastClipCameraForward", "Vector"],
    ["m_bClipHitStaticWorld", "bool"],
    ["m_bCachedPlaneIsValid", "bool"],
    ["m_pClippingWeapon", "C_CSWeaponBase*"],
    ["m_previousPlayerState", "CSPlayerState"],
    ["m_iPlayerState", "CSPlayerState"],
    ["m_bIsRescuing", "bool"],
    ["m_fImmuneToGunGameDamageTime", "GameTime_t"],
    ["m_fImmuneToGunGameDamageTimeLast", "GameTime_t"],
    ["m_bGunGameImmunity", "bool"],
    ["m_bHasMovedSinceSpawn", "bool"],
    ["m_fMolotovUseTime", "float32"],
    ["m_fMolotovDamageTime", "float32"],
    ["m_iThrowGrenadeCounter", "int32"],
    ["m_flLastSpawnTimeIndex", "GameTime_t"],
    ["m_iProgressBarDuration", "int32"],
    ["m_flProgressBarStartTime", "float32"],
    ["m_vecIntroStartEyePosition", "Vector"],
    ["m_vecIntroStartPlayerForward", "Vector"],
    ["m_flClientDeathTime", "GameTime_t"],
    ["m_bScreenTearFrameCaptured", "bool"],
    ["m_flFlashBangTime", "float32"],
    ["m_flFlashScreenshotAlpha", "float32"],
    ["m_flFlashOverlayAlpha", "float32"],
    ["m_bFlashBuildUp", "bool"],
    ["m_bFlashDspHasBeenCleared", "bool"],
    ["m_bFlashScreenshotHasBeenGrabbed", "bool"],
    ["m_flFlashMaxAlpha", "float32"],
    ["m_flFlashDuration", "float32"],
    ["m_iHealthBarRenderMaskIndex", "int32"],
    ["m_flHealthFadeValue", "float32"],
    ["m_flHealthFadeAlpha", "float32"],
    ["m_flDeathCCWeight", "float32"],
    ["m_flPrevRoundEndTime", "float32"],
    ["m_flPrevMatchEndTime", "float32"],
    ["m_angEyeAngles", "QAngle"],
    ["m_fNextThinkPushAway", "float32"],
    ["m_bShouldAutobuyDMWeapons", "bool"],
    ["m_bShouldAutobuyNow", "bool"],
    ["m_iIDEntIndex", "CEntityIndex"],
    ["m_delayTargetIDTimer", "CountdownTimer"],
    ["m_iTargetItemEntIdx", "CEntityIndex"],
    ["m_iOldIDEntIndex", "CEntityIndex"],
    ["m_holdTargetIDTimer", "CountdownTimer"],
    ["m_flCurrentMusicStartTime", "float32"],
    ["m_flMusicRoundStartTime", "float32"],
    ["m_bDeferStartMusicOnWarmup", "bool"],
    ["m_cycleLatch", "int32"],
    ["m_serverIntendedCycle", "float32"],
    ["m_flLastSmokeOverlayAlpha", "float32"],
    ["m_flLastSmokeAge", "float32"],
    ["m_vLastSmokeOverlayColor", "Vector"],
    ["m_nPlayerSmokedFx", "ParticleIndex_t"],
    ["m_nPlayerInfernoBodyFx", "ParticleIndex_t"],
    ["m_nPlayerInfernoFootFx", "ParticleIndex_t"],
    ["m_flNextMagDropTime", "float32"],
    ["m_nLastMagDropAttachmentIndex", "int32"],
    ["m_vecLastAliveLocalVelocity", "Vector"],
    ["m_bGuardianShouldSprayCustomXMark", "bool"],
    ["m_hOriginalController", "CHandle< CCSPlayerController >"],
]) }}

## C_EnvWindShared

{{ get_arguments_table([
    ["m_flStartTime", "GameTime_t"],
    ["m_iWindSeed", "uint32"],
    ["m_iMinWind", "uint16"],
    ["m_iMaxWind", "uint16"],
    ["m_windRadius", "int32"],
    ["m_iMinGust", "uint16"],
    ["m_iMaxGust", "uint16"],
    ["m_flMinGustDelay", "float32"],
    ["m_flMaxGustDelay", "float32"],
    ["m_flGustDuration", "float32"],
    ["m_iGustDirChange", "uint16"],
    ["m_location", "Vector"],
    ["m_iszGustSound", "int32"],
    ["m_iWindDir", "int32"],
    ["m_flWindSpeed", "float32"],
    ["m_currentWindVector", "Vector"],
    ["m_CurrentSwayVector", "Vector"],
    ["m_PrevSwayVector", "Vector"],
    ["m_iInitialWindDir", "uint16"],
    ["m_flInitialWindSpeed", "float32"],
    ["m_flVariationTime", "GameTime_t"],
    ["m_flSwayTime", "GameTime_t"],
    ["m_flSimTime", "GameTime_t"],
    ["m_flSwitchTime", "GameTime_t"],
    ["m_flAveWindSpeed", "float32"],
    ["m_bGusting", "bool"],
    ["m_flWindAngleVariation", "float32"],
    ["m_flWindSpeedVariation", "float32"],
    ["m_hEntOwner", "CHandle< C_BaseEntity >"],
]) }}

## C_PostProcessingVolume

{{ get_arguments_table([
    ["m_hPostSettings", "CStrongHandle< InfoForResourceTypeCPostProcessingResource >"],
    ["m_flFadeDuration", "float32"],
    ["m_flMinLogExposure", "float32"],
    ["m_flMaxLogExposure", "float32"],
    ["m_flMinExposure", "float32"],
    ["m_flMaxExposure", "float32"],
    ["m_flExposureCompensation", "float32"],
    ["m_flExposureFadeSpeedUp", "float32"],
    ["m_flExposureFadeSpeedDown", "float32"],
    ["m_flTonemapEVSmoothingRange", "float32"],
    ["m_bMaster", "bool"],
    ["m_bExposureControl", "bool"],
    ["m_flRate", "float32"],
    ["m_flTonemapPercentTarget", "float32"],
    ["m_flTonemapPercentBrightPixels", "float32"],
    ["m_flTonemapMinAvgLum", "float32"],
]) }}

## CCSPlayer_PingServices

{{ get_arguments_table([
    ["m_hPlayerPing", "CHandle< C_BaseEntity >"],
]) }}

## C_AttributeContainer

{{ get_arguments_table([
    ["m_Item", "C_EconItemView"],
    ["m_iExternalItemProviderRegisteredToken", "int32"],
    ["m_ullRegisteredAsItemID", "uint64"],
]) }}

## C_BaseFire

{{ get_arguments_table([
    ["m_flScale", "float32"],
    ["m_flStartScale", "float32"],
    ["m_flScaleTime", "float32"],
    ["m_nFlags", "uint32"],
]) }}

## CBasePlayerController

{{ get_arguments_table([
    ["m_nFinalPredictedTick", "int32"],
    ["m_CommandContext", "C_CommandContext"],
    ["m_nInButtonsWhichAreToggles", "uint64"],
    ["m_nTickBase", "uint32"],
    ["m_hPawn", "CHandle< C_BasePlayerPawn >"],
    ["m_bKnownTeamMismatch", "bool"],
    ["m_hPredictedPawn", "CHandle< C_BasePlayerPawn >"],
    ["m_nSplitScreenSlot", "CSplitScreenSlot"],
    ["m_hSplitOwner", "CHandle< CBasePlayerController >"],
    ["m_hSplitScreenPlayers", "CUtlVector< CHandle< CBasePlayerController > >"],
    ["m_bIsHLTV", "bool"],
    ["m_iConnected", "PlayerConnectedState"],
    ["m_iszPlayerName", "char[128]"],
    ["m_steamID", "uint64"],
    ["m_bIsLocalPlayerController", "bool"],
    ["m_iDesiredFOV", "uint32"],
]) }}

## C_DecoyProjectile

{{ get_arguments_table([
    ["m_nDecoyShotTick", "int32"],
    ["m_nClientLastKnownDecoyShotTick", "int32"],
    ["m_flTimeParticleEffectSpawn", "GameTime_t"],
]) }}

## C_CSGO_PreviewPlayer

{{ get_arguments_table([
    ["m_animgraph", "CUtlString"],
    ["m_animgraphCharacterModeString", "CGlobalSymbol"],
    ["m_flInitialModelScale", "float32"],
]) }}

## CBaseAnimGraphController

{{ get_arguments_table([
    ["m_animGraphNetworkedVars", "CAnimGraphNetworkedVariables"],
    ["m_bSequenceFinished", "bool"],
    ["m_flSoundSyncTime", "float32"],
    ["m_nActiveIKChainMask", "uint32"],
    ["m_hSequence", "HSequence"],
    ["m_flSeqStartTime", "GameTime_t"],
    ["m_flSeqFixedCycle", "float32"],
    ["m_nAnimLoopMode", "AnimLoopMode_t"],
    ["m_flPlaybackRate", "CNetworkedQuantizedFloat"],
    ["m_nNotifyState", "SequenceFinishNotifyState_t"],
    ["m_bNetworkedAnimationInputsChanged", "bool"],
    ["m_bNetworkedSequenceChanged", "bool"],
    ["m_bLastUpdateSkipped", "bool"],
    ["m_flPrevAnimUpdateTime", "GameTime_t"],
]) }}

## C_C4

{{ get_arguments_table([
    ["m_szScreenText", "char[32]"],
    ["m_activeLightParticleIndex", "ParticleIndex_t"],
    ["m_eActiveLightEffect", "C4LightEffect_t"],
    ["m_bStartedArming", "bool"],
    ["m_fArmedTime", "GameTime_t"],
    ["m_bBombPlacedAnimation", "bool"],
    ["m_bIsPlantingViaUse", "bool"],
    ["m_entitySpottedState", "EntitySpottedState_t"],
    ["m_nSpotRules", "int32"],
    ["m_bPlayedArmingBeeps", "bool[7]"],
    ["m_bBombPlanted", "bool"],
]) }}

## CBaseAnimGraph

{{ get_arguments_table([
    ["m_bInitiallyPopulateInterpHistory", "bool"],
    ["m_bSuppressAnimEventSounds", "bool"],
    ["m_bAnimGraphUpdateEnabled", "bool"],
    ["m_flMaxSlopeDistance", "float32"],
    ["m_vLastSlopeCheckPos", "Vector"],
    ["m_bAnimationUpdateScheduled", "bool"],
    ["m_vecForce", "Vector"],
    ["m_nForceBone", "int32"],
    ["m_pClientsideRagdoll", "CBaseAnimGraph*"],
    ["m_bBuiltRagdoll", "bool"],
    ["m_RagdollPose", "PhysicsRagdollPose_t"],
    ["m_bRagdollClientSide", "bool"],
    ["m_bHasAnimatedMaterialAttributes", "bool"],
]) }}

## C_PathParticleRope

{{ get_arguments_table([
    ["m_bStartActive", "bool"],
    ["m_flMaxSimulationTime", "float32"],
    ["m_iszEffectName", "CUtlSymbolLarge"],
    ["m_PathNodes_Name", "CUtlVector< CUtlSymbolLarge >"],
    ["m_flParticleSpacing", "float32"],
    ["m_flSlack", "float32"],
    ["m_flRadius", "float32"],
    ["m_ColorTint", "Color"],
    ["m_nEffectState", "int32"],
    ["m_iEffectIndex", "CStrongHandle< InfoForResourceTypeIParticleSystemDefinition >"],
    ["m_PathNodes_Position", "C_NetworkUtlVectorBase< Vector >"],
    ["m_PathNodes_TangentIn", "C_NetworkUtlVectorBase< Vector >"],
    ["m_PathNodes_TangentOut", "C_NetworkUtlVectorBase< Vector >"],
    ["m_PathNodes_Color", "C_NetworkUtlVectorBase< Vector >"],
    ["m_PathNodes_PinEnabled", "C_NetworkUtlVectorBase< bool >"],
    ["m_PathNodes_RadiusScale", "C_NetworkUtlVectorBase< float32 >"],
]) }}

## C_SoundEventAABBEntity

{{ get_arguments_table([
    ["m_vMins", "Vector"],
    ["m_vMaxs", "Vector"],
]) }}

## C_BasePlayerWeapon

{{ get_arguments_table([
    ["m_nNextPrimaryAttackTick", "GameTick_t"],
    ["m_flNextPrimaryAttackTickRatio", "float32"],
    ["m_nNextSecondaryAttackTick", "GameTick_t"],
    ["m_flNextSecondaryAttackTickRatio", "float32"],
    ["m_iClip1", "int32"],
    ["m_iClip2", "int32"],
    ["m_pReserveAmmo", "int32[2]"],
]) }}

## CBasePlayerWeaponVData

{{ get_arguments_table([
    ["m_szWorldModel", "CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >"],
    ["m_sToolsOnlyOwnerModelName", "CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >"],
    ["m_bBuiltRightHanded", "bool"],
    ["m_bAllowFlipping", "bool"],
    ["m_sMuzzleAttachment", "CAttachmentNameSymbolWithStorage"],
    ["m_szMuzzleFlashParticle", "CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >"],
    ["m_bLinkedCooldowns", "bool"],
    ["m_iFlags", "ItemFlagTypes_t"],
    ["m_nPrimaryAmmoType", "AmmoIndex_t"],
    ["m_nSecondaryAmmoType", "AmmoIndex_t"],
    ["m_iMaxClip1", "int32"],
    ["m_iMaxClip2", "int32"],
    ["m_iDefaultClip1", "int32"],
    ["m_iDefaultClip2", "int32"],
    ["m_bReserveAmmoAsClips", "bool"],
    ["m_iWeight", "int32"],
    ["m_bAutoSwitchTo", "bool"],
    ["m_bAutoSwitchFrom", "bool"],
    ["m_iRumbleEffect", "RumbleEffect_t"],
    ["m_iSlot", "int32"],
    ["m_iPosition", "int32"],
    ["m_aShootSounds", "CUtlOrderedMap< WeaponSound_t, CSoundEventName >"],
]) }}

## C_Fish

{{ get_arguments_table([
    ["m_pos", "Vector"],
    ["m_vel", "Vector"],
    ["m_angles", "QAngle"],
    ["m_localLifeState", "int32"],
    ["m_deathDepth", "float32"],
    ["m_deathAngle", "float32"],
    ["m_buoyancy", "float32"],
    ["m_wiggleTimer", "CountdownTimer"],
    ["m_wigglePhase", "float32"],
    ["m_wiggleRate", "float32"],
    ["m_actualPos", "Vector"],
    ["m_actualAngles", "QAngle"],
    ["m_poolOrigin", "Vector"],
    ["m_waterLevel", "float32"],
    ["m_gotUpdate", "bool"],
    ["m_x", "float32"],
    ["m_y", "float32"],
    ["m_z", "float32"],
    ["m_angle", "float32"],
    ["m_errorHistory", "float32[20]"],
    ["m_errorHistoryIndex", "int32"],
    ["m_errorHistoryCount", "int32"],
    ["m_averageError", "float32"],
]) }}

## CTimeline

{{ get_arguments_table([
    ["m_flValues", "float32[64]"],
    ["m_nValueCounts", "int32[64]"],
    ["m_nBucketCount", "int32"],
    ["m_flInterval", "float32"],
    ["m_flFinalValue", "float32"],
    ["m_nCompressionType", "TimelineCompression_t"],
    ["m_bStopped", "bool"],
]) }}

## C_BasePlayerPawn

{{ get_arguments_table([
    ["m_pWeaponServices", "CPlayer_WeaponServices*"],
    ["m_pItemServices", "CPlayer_ItemServices*"],
    ["m_pAutoaimServices", "CPlayer_AutoaimServices*"],
    ["m_pObserverServices", "CPlayer_ObserverServices*"],
    ["m_pWaterServices", "CPlayer_WaterServices*"],
    ["m_pUseServices", "CPlayer_UseServices*"],
    ["m_pFlashlightServices", "CPlayer_FlashlightServices*"],
    ["m_pCameraServices", "CPlayer_CameraServices*"],
    ["m_pMovementServices", "CPlayer_MovementServices*"],
    ["m_ServerViewAngleChanges", "C_UtlVectorEmbeddedNetworkVar< ViewAngleServerChange_t >"],
    ["m_nHighestConsumedServerViewAngleChangeIndex", "uint32"],
    ["v_angle", "QAngle"],
    ["v_anglePrevious", "QAngle"],
    ["m_iHideHUD", "uint32"],
    ["m_skybox3d", "sky3dparams_t"],
    ["m_flDeathTime", "GameTime_t"],
    ["m_vecPredictionError", "Vector"],
    ["m_flPredictionErrorTime", "GameTime_t"],
    ["m_vecLastCameraSetupLocalOrigin", "Vector"],
    ["m_flLastCameraSetupTime", "GameTime_t"],
    ["m_flFOVSensitivityAdjust", "float32"],
    ["m_flMouseSensitivity", "float32"],
    ["m_vOldOrigin", "Vector"],
    ["m_flOldSimulationTime", "float32"],
    ["m_nLastExecutedCommandNumber", "int32"],
    ["m_nLastExecutedCommandTick", "int32"],
    ["m_hController", "CHandle< CBasePlayerController >"],
    ["m_bIsSwappingToPredictableController", "bool"],
]) }}

## CAttributeManager

{{ get_arguments_table([
    ["m_Providers", "CUtlVector< CHandle< C_BaseEntity > >"],
    ["m_iReapplyProvisionParity", "int32"],
    ["m_hOuter", "CHandle< C_BaseEntity >"],
    ["m_bPreventLoopback", "bool"],
    ["m_ProviderType", "attributeprovidertypes_t"],
    ["m_CachedResults", "CUtlVector< CAttributeManager::cached_attribute_float_t >"],
]) }}

## CAnimGraphNetworkedVariables

{{ get_arguments_table([
    ["m_PredNetBoolVariables", "C_NetworkUtlVectorBase< uint32 >"],
    ["m_PredNetByteVariables", "C_NetworkUtlVectorBase< uint8 >"],
    ["m_PredNetUInt16Variables", "C_NetworkUtlVectorBase< uint16 >"],
    ["m_PredNetIntVariables", "C_NetworkUtlVectorBase< int32 >"],
    ["m_PredNetUInt32Variables", "C_NetworkUtlVectorBase< uint32 >"],
    ["m_PredNetUInt64Variables", "C_NetworkUtlVectorBase< uint64 >"],
    ["m_PredNetFloatVariables", "C_NetworkUtlVectorBase< float32 >"],
    ["m_PredNetVectorVariables", "C_NetworkUtlVectorBase< Vector >"],
    ["m_PredNetQuaternionVariables", "C_NetworkUtlVectorBase< Quaternion >"],
    ["m_PredNetGlobalSymbolVariables", "C_NetworkUtlVectorBase< CGlobalSymbol >"],
    ["m_OwnerOnlyPredNetBoolVariables", "C_NetworkUtlVectorBase< uint32 >"],
    ["m_OwnerOnlyPredNetByteVariables", "C_NetworkUtlVectorBase< uint8 >"],
    ["m_OwnerOnlyPredNetUInt16Variables", "C_NetworkUtlVectorBase< uint16 >"],
    ["m_OwnerOnlyPredNetIntVariables", "C_NetworkUtlVectorBase< int32 >"],
    ["m_OwnerOnlyPredNetUInt32Variables", "C_NetworkUtlVectorBase< uint32 >"],
    ["m_OwnerOnlyPredNetUInt64Variables", "C_NetworkUtlVectorBase< uint64 >"],
    ["m_OwnerOnlyPredNetFloatVariables", "C_NetworkUtlVectorBase< float32 >"],
    ["m_OwnerOnlyPredNetVectorVariables", "C_NetworkUtlVectorBase< Vector >"],
    ["m_OwnerOnlyPredNetQuaternionVariables", "C_NetworkUtlVectorBase< Quaternion >"],
    ["m_OwnerOnlyPredNetGlobalSymbolVariables", "C_NetworkUtlVectorBase< CGlobalSymbol >"],
    ["m_nBoolVariablesCount", "int32"],
    ["m_nOwnerOnlyBoolVariablesCount", "int32"],
    ["m_nRandomSeedOffset", "int32"],
    ["m_flLastTeleportTime", "float32"],
]) }}

## C_TriggerBuoyancy

{{ get_arguments_table([
    ["m_BuoyancyHelper", "CBuoyancyHelper"],
    ["m_flFluidDensity", "float32"],
]) }}

## C_RopeKeyframe

{{ get_arguments_table([
    ["m_LinksTouchingSomething", "CBitVec< 10 >"],
    ["m_nLinksTouchingSomething", "int32"],
    ["m_bApplyWind", "bool"],
    ["m_fPrevLockedPoints", "int32"],
    ["m_iForcePointMoveCounter", "int32"],
    ["m_bPrevEndPointPos", "bool[2]"],
    ["m_vPrevEndPointPos", "Vector[2]"],
    ["m_flCurScroll", "float32"],
    ["m_flScrollSpeed", "float32"],
    ["m_RopeFlags", "uint16"],
    ["m_iRopeMaterialModelIndex", "CStrongHandle< InfoForResourceTypeIMaterial2 >"],
    ["m_LightValues", "Vector[10]"],
    ["m_nSegments", "uint8"],
    ["m_hStartPoint", "CHandle< C_BaseEntity >"],
    ["m_hEndPoint", "CHandle< C_BaseEntity >"],
    ["m_iStartAttachment", "AttachmentHandle_t"],
    ["m_iEndAttachment", "AttachmentHandle_t"],
    ["m_Subdiv", "uint8"],
    ["m_RopeLength", "int16"],
    ["m_Slack", "int16"],
    ["m_TextureScale", "float32"],
    ["m_fLockedPoints", "uint8"],
    ["m_nChangeCount", "uint8"],
    ["m_Width", "float32"],
    ["m_PhysicsDelegate", "C_RopeKeyframe::CPhysicsDelegate"],
    ["m_hMaterial", "CStrongHandle< InfoForResourceTypeIMaterial2 >"],
    ["m_TextureHeight", "int32"],
    ["m_vecImpulse", "Vector"],
    ["m_vecPreviousImpulse", "Vector"],
    ["m_flCurrentGustTimer", "float32"],
    ["m_flCurrentGustLifetime", "float32"],
    ["m_flTimeToNextGust", "float32"],
    ["m_vWindDir", "Vector"],
    ["m_vColorMod", "Vector"],
    ["m_vCachedEndPointAttachmentPos", "Vector[2]"],
    ["m_vCachedEndPointAttachmentAngle", "QAngle[2]"],
    ["m_bConstrainBetweenEndpoints", "bool"],
    ["m_bEndPointAttachmentPositionsDirty", "bitfield:1"],
    ["m_bEndPointAttachmentAnglesDirty", "bitfield:1"],
    ["m_bNewDataThisFrame", "bitfield:1"],
    ["m_bPhysicsInitted", "bitfield:1"],
]) }}

## C_GradientFog

{{ get_arguments_table([
    ["m_hGradientFogTexture", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_flFogStartDistance", "float32"],
    ["m_flFogEndDistance", "float32"],
    ["m_bHeightFogEnabled", "bool"],
    ["m_flFogStartHeight", "float32"],
    ["m_flFogEndHeight", "float32"],
    ["m_flFarZ", "float32"],
    ["m_flFogMaxOpacity", "float32"],
    ["m_flFogFalloffExponent", "float32"],
    ["m_flFogVerticalExponent", "float32"],
    ["m_fogColor", "Color"],
    ["m_flFogStrength", "float32"],
    ["m_flFadeTime", "float32"],
    ["m_bStartDisabled", "bool"],
    ["m_bIsEnabled", "bool"],
    ["m_bGradientFogNeedsTextures", "bool"],
]) }}

## EntitySpottedState_t

{{ get_arguments_table([
    ["m_bSpotted", "bool"],
    ["m_bSpottedByMask", "uint32[2]"],
]) }}

## C_CSGO_TeamPreviewCamera

{{ get_arguments_table([
    ["m_nVariant", "int32"],
    ["m_bDofEnabled", "bool"],
    ["m_flDofNearBlurry", "float32"],
    ["m_flDofNearCrisp", "float32"],
    ["m_flDofFarCrisp", "float32"],
    ["m_flDofFarBlurry", "float32"],
    ["m_flDofTiltToGround", "float32"],
]) }}

## CCSPlayer_CameraServices

{{ get_arguments_table([
    ["m_flDeathCamTilt", "float32"],
    ["m_vClientScopeInaccuracy", "Vector"],
]) }}

## C_EconWearable

{{ get_arguments_table([
    ["m_nForceSkin", "int32"],
    ["m_bAlwaysAllow", "bool"],
]) }}

## CSMatchStats_t

{{ get_arguments_table([
    ["m_iEnemy5Ks", "int32"],
    ["m_iEnemy4Ks", "int32"],
    ["m_iEnemy3Ks", "int32"],
    ["m_iEnemyKnifeKills", "int32"],
    ["m_iEnemyTaserKills", "int32"],
]) }}

## C_EnvVolumetricFogVolume

{{ get_arguments_table([
    ["m_bActive", "bool"],
    ["m_vBoxMins", "Vector"],
    ["m_vBoxMaxs", "Vector"],
    ["m_bStartDisabled", "bool"],
    ["m_flStrength", "float32"],
    ["m_nFalloffShape", "int32"],
    ["m_flFalloffExponent", "float32"],
    ["m_flHeightFogDepth", "float32"],
    ["m_fHeightFogEdgeWidth", "float32"],
    ["m_fIndirectLightStrength", "float32"],
    ["m_fSunLightStrength", "float32"],
    ["m_fNoiseStrength", "float32"],
    ["m_bOverrideIndirectLightStrength", "bool"],
    ["m_bOverrideSunLightStrength", "bool"],
    ["m_bOverrideNoiseStrength", "bool"],
    ["m_bAllowLPVIndirect", "bool"],
]) }}

## C_FireSmoke

{{ get_arguments_table([
    ["m_nFlameModelIndex", "int32"],
    ["m_nFlameFromAboveModelIndex", "int32"],
    ["m_flScaleRegister", "float32"],
    ["m_flScaleStart", "float32"],
    ["m_flScaleEnd", "float32"],
    ["m_flScaleTimeStart", "GameTime_t"],
    ["m_flScaleTimeEnd", "GameTime_t"],
    ["m_flChildFlameSpread", "float32"],
    ["m_flClipPerc", "float32"],
    ["m_bClipTested", "bool"],
    ["m_bFadingOut", "bool"],
    ["m_tParticleSpawn", "TimedEvent"],
    ["m_pFireOverlay", "CFireOverlay*"],
]) }}

## C_EnvCombinedLightProbeVolume

{{ get_arguments_table([
    ["m_Entity_Color", "Color"],
    ["m_Entity_flBrightness", "float32"],
    ["m_Entity_hCubemapTexture", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_Entity_bCustomCubemapTexture", "bool"],
    ["m_Entity_hLightProbeTexture", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_Entity_hLightProbeDirectLightIndicesTexture", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_Entity_hLightProbeDirectLightScalarsTexture", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_Entity_hLightProbeDirectLightShadowsTexture", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_Entity_vBoxMins", "Vector"],
    ["m_Entity_vBoxMaxs", "Vector"],
    ["m_Entity_bMoveable", "bool"],
    ["m_Entity_nHandshake", "int32"],
    ["m_Entity_nEnvCubeMapArrayIndex", "int32"],
    ["m_Entity_nPriority", "int32"],
    ["m_Entity_bStartDisabled", "bool"],
    ["m_Entity_flEdgeFadeDist", "float32"],
    ["m_Entity_vEdgeFadeDists", "Vector"],
    ["m_Entity_nLightProbeSizeX", "int32"],
    ["m_Entity_nLightProbeSizeY", "int32"],
    ["m_Entity_nLightProbeSizeZ", "int32"],
    ["m_Entity_nLightProbeAtlasX", "int32"],
    ["m_Entity_nLightProbeAtlasY", "int32"],
    ["m_Entity_nLightProbeAtlasZ", "int32"],
    ["m_Entity_bEnabled", "bool"],
]) }}

## ActiveModelConfig_t

{{ get_arguments_table([
    ["m_Handle", "ModelConfigHandle_t"],
    ["m_Name", "CUtlSymbolLarge"],
    ["m_AssociatedEntities", "C_NetworkUtlVectorBase< CHandle< C_BaseModelEntity > >"],
    ["m_AssociatedEntityNames", "C_NetworkUtlVectorBase< CUtlSymbolLarge >"],
]) }}

## CCSPlayer_BulletServices

{{ get_arguments_table([
    ["m_totalHitsOnServer", "int32"],
]) }}

## CLogicRelay

{{ get_arguments_table([
    ["m_OnTrigger", "CEntityIOOutput"],
    ["m_OnSpawn", "CEntityIOOutput"],
    ["m_bDisabled", "bool"],
    ["m_bWaitForRefire", "bool"],
    ["m_bTriggerOnce", "bool"],
    ["m_bFastRetrigger", "bool"],
    ["m_bPassthoughCaller", "bool"],
]) }}

## C_PointCameraVFOV

{{ get_arguments_table([
    ["m_flVerticalFOV", "float32"],
]) }}

## CCSPlayer_ItemServices

{{ get_arguments_table([
    ["m_bHasDefuser", "bool"],
    ["m_bHasHelmet", "bool"],
    ["m_bHasHeavyArmor", "bool"],
]) }}

## C_BarnLight

{{ get_arguments_table([
    ["m_bEnabled", "bool"],
    ["m_nColorMode", "int32"],
    ["m_Color", "Color"],
    ["m_flColorTemperature", "float32"],
    ["m_flBrightness", "float32"],
    ["m_flBrightnessScale", "float32"],
    ["m_nDirectLight", "int32"],
    ["m_nBakedShadowIndex", "int32"],
    ["m_nLuminaireShape", "int32"],
    ["m_flLuminaireSize", "float32"],
    ["m_flLuminaireAnisotropy", "float32"],
    ["m_LightStyleString", "CUtlString"],
    ["m_flLightStyleStartTime", "GameTime_t"],
    ["m_QueuedLightStyleStrings", "C_NetworkUtlVectorBase< CUtlString >"],
    ["m_LightStyleEvents", "C_NetworkUtlVectorBase< CUtlString >"],
    ["m_LightStyleTargets", "C_NetworkUtlVectorBase< CHandle< C_BaseModelEntity > >"],
    ["m_StyleEvent", "CEntityIOOutput[4]"],
    ["m_hLightCookie", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_flShape", "float32"],
    ["m_flSoftX", "float32"],
    ["m_flSoftY", "float32"],
    ["m_flSkirt", "float32"],
    ["m_flSkirtNear", "float32"],
    ["m_vSizeParams", "Vector"],
    ["m_flRange", "float32"],
    ["m_vShear", "Vector"],
    ["m_nBakeSpecularToCubemaps", "int32"],
    ["m_vBakeSpecularToCubemapsSize", "Vector"],
    ["m_nCastShadows", "int32"],
    ["m_nShadowMapSize", "int32"],
    ["m_nShadowPriority", "int32"],
    ["m_bContactShadow", "bool"],
    ["m_nBounceLight", "int32"],
    ["m_flBounceScale", "float32"],
    ["m_flMinRoughness", "float32"],
    ["m_vAlternateColor", "Vector"],
    ["m_fAlternateColorBrightness", "float32"],
    ["m_nFog", "int32"],
    ["m_flFogStrength", "float32"],
    ["m_nFogShadows", "int32"],
    ["m_flFogScale", "float32"],
    ["m_bFogMixedShadows", "bool"],
    ["m_flFadeSizeStart", "float32"],
    ["m_flFadeSizeEnd", "float32"],
    ["m_flShadowFadeSizeStart", "float32"],
    ["m_flShadowFadeSizeEnd", "float32"],
    ["m_bPrecomputedFieldsValid", "bool"],
    ["m_vPrecomputedBoundsMins", "Vector"],
    ["m_vPrecomputedBoundsMaxs", "Vector"],
    ["m_vPrecomputedOBBOrigin", "Vector"],
    ["m_vPrecomputedOBBAngles", "QAngle"],
    ["m_vPrecomputedOBBExtent", "Vector"],
    ["m_nPrecomputedSubFrusta", "int32"],
    ["m_vPrecomputedOBBOrigin0", "Vector"],
    ["m_vPrecomputedOBBAngles0", "QAngle"],
    ["m_vPrecomputedOBBExtent0", "Vector"],
    ["m_vPrecomputedOBBOrigin1", "Vector"],
    ["m_vPrecomputedOBBAngles1", "QAngle"],
    ["m_vPrecomputedOBBExtent1", "Vector"],
    ["m_vPrecomputedOBBOrigin2", "Vector"],
    ["m_vPrecomputedOBBAngles2", "QAngle"],
    ["m_vPrecomputedOBBExtent2", "Vector"],
    ["m_vPrecomputedOBBOrigin3", "Vector"],
    ["m_vPrecomputedOBBAngles3", "QAngle"],
    ["m_vPrecomputedOBBExtent3", "Vector"],
    ["m_vPrecomputedOBBOrigin4", "Vector"],
    ["m_vPrecomputedOBBAngles4", "QAngle"],
    ["m_vPrecomputedOBBExtent4", "Vector"],
    ["m_vPrecomputedOBBOrigin5", "Vector"],
    ["m_vPrecomputedOBBAngles5", "QAngle"],
    ["m_vPrecomputedOBBExtent5", "Vector"],
    ["m_bInitialBoneSetup", "bool"],
    ["m_VisClusters", "C_NetworkUtlVectorBase< uint16 >"],
]) }}

## C_TonemapController2

{{ get_arguments_table([
    ["m_flAutoExposureMin", "float32"],
    ["m_flAutoExposureMax", "float32"],
    ["m_flTonemapPercentTarget", "float32"],
    ["m_flTonemapPercentBrightPixels", "float32"],
    ["m_flTonemapMinAvgLum", "float32"],
    ["m_flExposureAdaptationSpeedUp", "float32"],
    ["m_flExposureAdaptationSpeedDown", "float32"],
    ["m_flTonemapEVSmoothingRange", "float32"],
]) }}

## CFuncWater

{{ get_arguments_table([
    ["m_BuoyancyHelper", "CBuoyancyHelper"],
]) }}

## C_EconEntity

{{ get_arguments_table([
    ["m_flFlexDelayTime", "float32"],
    ["m_flFlexDelayedWeight", "float32*"],
    ["m_bAttributesInitialized", "bool"],
    ["m_AttributeManager", "C_AttributeContainer"],
    ["m_OriginalOwnerXuidLow", "uint32"],
    ["m_OriginalOwnerXuidHigh", "uint32"],
    ["m_nFallbackPaintKit", "int32"],
    ["m_nFallbackSeed", "int32"],
    ["m_flFallbackWear", "float32"],
    ["m_nFallbackStatTrak", "int32"],
    ["m_bClientside", "bool"],
    ["m_bParticleSystemsCreated", "bool"],
    ["m_vecAttachedParticles", "CUtlVector< int32 >"],
    ["m_hViewmodelAttachment", "CHandle< CBaseAnimGraph >"],
    ["m_iOldTeam", "int32"],
    ["m_bAttachmentDirty", "bool"],
    ["m_nUnloadedModelIndex", "int32"],
    ["m_iNumOwnerValidationRetries", "int32"],
    ["m_hOldProvidee", "CHandle< C_BaseEntity >"],
    ["m_vecAttachedModels", "CUtlVector< C_EconEntity::AttachedModelData_t >"],
]) }}

## C_RectLight

{{ get_arguments_table([
    ["m_bShowLight", "bool"],
]) }}

## C_ParticleSystem

{{ get_arguments_table([
    ["m_szSnapshotFileName", "char[512]"],
    ["m_bActive", "bool"],
    ["m_bFrozen", "bool"],
    ["m_flFreezeTransitionDuration", "float32"],
    ["m_nStopType", "int32"],
    ["m_bAnimateDuringGameplayPause", "bool"],
    ["m_iEffectIndex", "CStrongHandle< InfoForResourceTypeIParticleSystemDefinition >"],
    ["m_flStartTime", "GameTime_t"],
    ["m_flPreSimTime", "float32"],
    ["m_vServerControlPoints", "Vector[4]"],
    ["m_iServerControlPointAssignments", "uint8[4]"],
    ["m_hControlPointEnts", "CHandle< C_BaseEntity >[64]"],
    ["m_bNoSave", "bool"],
    ["m_bNoFreeze", "bool"],
    ["m_bNoRamp", "bool"],
    ["m_bStartActive", "bool"],
    ["m_iszEffectName", "CUtlSymbolLarge"],
    ["m_iszControlPointNames", "CUtlSymbolLarge[64]"],
    ["m_nDataCP", "int32"],
    ["m_vecDataCPValue", "Vector"],
    ["m_nTintCP", "int32"],
    ["m_clrTint", "Color"],
    ["m_bOldActive", "bool"],
    ["m_bOldFrozen", "bool"],
]) }}

## C_CSGameRulesProxy

{{ get_arguments_table([
    ["m_pGameRules", "C_CSGameRules*"],
]) }}

## CPlayer_ObserverServices

{{ get_arguments_table([
    ["m_iObserverMode", "uint8"],
    ["m_hObserverTarget", "CHandle< C_BaseEntity >"],
    ["m_iObserverLastMode", "ObserverMode_t"],
    ["m_bForcedObserverMode", "bool"],
    ["m_flObserverChaseDistance", "float32"],
    ["m_flObserverChaseDistanceCalcTime", "GameTime_t"],
]) }}

## SequenceHistory_t

{{ get_arguments_table([
    ["m_hSequence", "HSequence"],
    ["m_flSeqStartTime", "GameTime_t"],
    ["m_flSeqFixedCycle", "float32"],
    ["m_nSeqLoopMode", "AnimLoopMode_t"],
    ["m_flPlaybackRate", "float32"],
    ["m_flCyclesPerSecond", "float32"],
]) }}

## C_Multimeter

{{ get_arguments_table([
    ["m_hTargetC4", "CHandle< C_PlantedC4 >"],
]) }}

## C_CsmFovOverride

{{ get_arguments_table([
    ["m_cameraName", "CUtlString"],
    ["m_flCsmFovOverrideValue", "float32"],
]) }}

## C_EnvDecal

{{ get_arguments_table([
    ["m_hDecalMaterial", "CStrongHandle< InfoForResourceTypeIMaterial2 >"],
    ["m_flWidth", "float32"],
    ["m_flHeight", "float32"],
    ["m_flDepth", "float32"],
    ["m_nRenderOrder", "uint32"],
    ["m_bProjectOnWorld", "bool"],
    ["m_bProjectOnCharacters", "bool"],
    ["m_bProjectOnWater", "bool"],
    ["m_flDepthSortBias", "float32"],
]) }}

## C_ColorCorrection

{{ get_arguments_table([
    ["m_vecOrigin", "Vector"],
    ["m_MinFalloff", "float32"],
    ["m_MaxFalloff", "float32"],
    ["m_flFadeInDuration", "float32"],
    ["m_flFadeOutDuration", "float32"],
    ["m_flMaxWeight", "float32"],
    ["m_flCurWeight", "float32"],
    ["m_netlookupFilename", "char[512]"],
    ["m_bEnabled", "bool"],
    ["m_bMaster", "bool"],
    ["m_bClientSide", "bool"],
    ["m_bExclusive", "bool"],
    ["m_bEnabledOnClient", "bool[1]"],
    ["m_flCurWeightOnClient", "float32[1]"],
    ["m_bFadingIn", "bool[1]"],
    ["m_flFadeStartWeight", "float32[1]"],
    ["m_flFadeStartTime", "float32[1]"],
    ["m_flFadeDuration", "float32[1]"],
]) }}

## CModelState

{{ get_arguments_table([
    ["m_hModel", "CStrongHandle< InfoForResourceTypeCModel >"],
    ["m_ModelName", "CUtlSymbolLarge"],
    ["m_bClientClothCreationSuppressed", "bool"],
    ["m_MeshGroupMask", "uint64"],
    ["m_nIdealMotionType", "int8"],
    ["m_nForceLOD", "int8"],
    ["m_nClothUpdateFlags", "int8"],
]) }}

## C_EconEntity::AttachedModelData_t

{{ get_arguments_table([
    ["m_iModelDisplayFlags", "int32"],
]) }}

## CAttributeList

{{ get_arguments_table([
    ["m_Attributes", "C_UtlVectorEmbeddedNetworkVar< CEconItemAttribute >"],
    ["m_pManager", "CAttributeManager*"],
]) }}

## C_BaseDoor

{{ get_arguments_table([
    ["m_bIsUsable", "bool"],
]) }}

## CGrenadeTracer

{{ get_arguments_table([
    ["m_flTracerDuration", "float32"],
    ["m_nType", "GrenadeType_t"],
]) }}

## CBombTarget

{{ get_arguments_table([
    ["m_bBombPlantedHere", "bool"],
]) }}

## C_PointClientUIDialog

{{ get_arguments_table([
    ["m_hActivator", "CHandle< C_BaseEntity >"],
    ["m_bStartEnabled", "bool"],
]) }}

## CCSGameModeRules_ArmsRace

{{ get_arguments_table([
    ["m_WeaponSequence", "C_NetworkUtlVectorBase< CUtlString >"],
]) }}

## CPointChildModifier

{{ get_arguments_table([
    ["m_bOrphanInsteadOfDeletingChildrenOnRemove", "bool"],
]) }}

## CDamageRecord

{{ get_arguments_table([
    ["m_PlayerDamager", "CHandle< C_CSPlayerPawn >"],
    ["m_PlayerRecipient", "CHandle< C_CSPlayerPawn >"],
    ["m_hPlayerControllerDamager", "CHandle< CCSPlayerController >"],
    ["m_hPlayerControllerRecipient", "CHandle< CCSPlayerController >"],
    ["m_szPlayerDamagerName", "CUtlString"],
    ["m_szPlayerRecipientName", "CUtlString"],
    ["m_DamagerXuid", "uint64"],
    ["m_RecipientXuid", "uint64"],
    ["m_iBulletsDamage", "int32"],
    ["m_iDamage", "int32"],
    ["m_iActualHealthRemoved", "int32"],
    ["m_iNumHits", "int32"],
    ["m_iLastBulletUpdate", "int32"],
    ["m_bIsOtherEnemy", "bool"],
    ["m_killType", "EKillTypes_t"],
]) }}

## CCSPlayerController_DamageServices

{{ get_arguments_table([
    ["m_nSendUpdate", "int32"],
    ["m_DamageList", "C_UtlVectorEmbeddedNetworkVar< CDamageRecord >"],
]) }}

## CRenderComponent

{{ get_arguments_table([
    ["__m_pChainEntity", "CNetworkVarChainer"],
    ["m_bIsRenderingWithViewModels", "bool"],
    ["m_nSplitscreenFlags", "uint32"],
    ["m_bEnableRendering", "bool"],
    ["m_bInterpolationReadyToDraw", "bool"],
]) }}

## CEnvSoundscapeProxy

{{ get_arguments_table([
    ["m_MainSoundscapeName", "CUtlSymbolLarge"],
]) }}

## C_SoundEventOBBEntity

{{ get_arguments_table([
    ["m_vMins", "Vector"],
    ["m_vMaxs", "Vector"],
]) }}

## CLightComponent

{{ get_arguments_table([
    ["__m_pChainEntity", "CNetworkVarChainer"],
    ["m_Color", "Color"],
    ["m_SecondaryColor", "Color"],
    ["m_flBrightness", "float32"],
    ["m_flBrightnessScale", "float32"],
    ["m_flBrightnessMult", "float32"],
    ["m_flRange", "float32"],
    ["m_flFalloff", "float32"],
    ["m_flAttenuation0", "float32"],
    ["m_flAttenuation1", "float32"],
    ["m_flAttenuation2", "float32"],
    ["m_flTheta", "float32"],
    ["m_flPhi", "float32"],
    ["m_hLightCookie", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_nCascades", "int32"],
    ["m_nCastShadows", "int32"],
    ["m_nShadowWidth", "int32"],
    ["m_nShadowHeight", "int32"],
    ["m_bRenderDiffuse", "bool"],
    ["m_nRenderSpecular", "int32"],
    ["m_bRenderTransmissive", "bool"],
    ["m_flOrthoLightWidth", "float32"],
    ["m_flOrthoLightHeight", "float32"],
    ["m_nStyle", "int32"],
    ["m_Pattern", "CUtlString"],
    ["m_nCascadeRenderStaticObjects", "int32"],
    ["m_flShadowCascadeCrossFade", "float32"],
    ["m_flShadowCascadeDistanceFade", "float32"],
    ["m_flShadowCascadeDistance0", "float32"],
    ["m_flShadowCascadeDistance1", "float32"],
    ["m_flShadowCascadeDistance2", "float32"],
    ["m_flShadowCascadeDistance3", "float32"],
    ["m_nShadowCascadeResolution0", "int32"],
    ["m_nShadowCascadeResolution1", "int32"],
    ["m_nShadowCascadeResolution2", "int32"],
    ["m_nShadowCascadeResolution3", "int32"],
    ["m_bUsesBakedShadowing", "bool"],
    ["m_nShadowPriority", "int32"],
    ["m_nBakedShadowIndex", "int32"],
    ["m_bRenderToCubemaps", "bool"],
    ["m_nDirectLight", "int32"],
    ["m_nIndirectLight", "int32"],
    ["m_flFadeMinDist", "float32"],
    ["m_flFadeMaxDist", "float32"],
    ["m_flShadowFadeMinDist", "float32"],
    ["m_flShadowFadeMaxDist", "float32"],
    ["m_bEnabled", "bool"],
    ["m_bFlicker", "bool"],
    ["m_bPrecomputedFieldsValid", "bool"],
    ["m_vPrecomputedBoundsMins", "Vector"],
    ["m_vPrecomputedBoundsMaxs", "Vector"],
    ["m_vPrecomputedOBBOrigin", "Vector"],
    ["m_vPrecomputedOBBAngles", "QAngle"],
    ["m_vPrecomputedOBBExtent", "Vector"],
    ["m_flPrecomputedMaxRange", "float32"],
    ["m_nFogLightingMode", "int32"],
    ["m_flFogContributionStength", "float32"],
    ["m_flNearClipPlane", "float32"],
    ["m_SkyColor", "Color"],
    ["m_flSkyIntensity", "float32"],
    ["m_SkyAmbientBounce", "Color"],
    ["m_bUseSecondaryColor", "bool"],
    ["m_bMixedShadows", "bool"],
    ["m_flLightStyleStartTime", "GameTime_t"],
    ["m_flCapsuleLength", "float32"],
    ["m_flMinRoughness", "float32"],
]) }}

## C_EconItemView

{{ get_arguments_table([
    ["m_bInventoryImageRgbaRequested", "bool"],
    ["m_bInventoryImageTriedCache", "bool"],
    ["m_nInventoryImageRgbaWidth", "int32"],
    ["m_nInventoryImageRgbaHeight", "int32"],
    ["m_szCurrentLoadCachedFileName", "char[260]"],
    ["m_bRestoreCustomMaterialAfterPrecache", "bool"],
    ["m_iItemDefinitionIndex", "uint16"],
    ["m_iEntityQuality", "int32"],
    ["m_iEntityLevel", "uint32"],
    ["m_iItemID", "uint64"],
    ["m_iItemIDHigh", "uint32"],
    ["m_iItemIDLow", "uint32"],
    ["m_iAccountID", "uint32"],
    ["m_iInventoryPosition", "uint32"],
    ["m_bInitialized", "bool"],
    ["m_bDisallowSOC", "bool"],
    ["m_bIsStoreItem", "bool"],
    ["m_bIsTradeItem", "bool"],
    ["m_iEntityQuantity", "int32"],
    ["m_iRarityOverride", "int32"],
    ["m_iQualityOverride", "int32"],
    ["m_iOriginOverride", "int32"],
    ["m_unClientFlags", "uint8"],
    ["m_unOverrideStyle", "uint8"],
    ["m_AttributeList", "CAttributeList"],
    ["m_NetworkedDynamicAttributes", "CAttributeList"],
    ["m_szCustomName", "char[161]"],
    ["m_szCustomNameOverride", "char[161]"],
    ["m_bInitializedTags", "bool"],
]) }}

## C_HandleTest

{{ get_arguments_table([
    ["m_Handle", "CHandle< C_BaseEntity >"],
    ["m_bSendHandle", "bool"],
]) }}

## C_EnvWindClientside

{{ get_arguments_table([
    ["m_EnvWindShared", "C_EnvWindShared"],
]) }}

## C_WeaponShield

{{ get_arguments_table([
    ["m_flDisplayHealth", "float32"],
]) }}

## C_PointClientUIWorldTextPanel

{{ get_arguments_table([
    ["m_messageText", "char[512]"],
]) }}

## CPlayer_MovementServices

{{ get_arguments_table([
    ["m_nImpulse", "int32"],
    ["m_nButtons", "CInButtonState"],
    ["m_nQueuedButtonDownMask", "uint64"],
    ["m_nQueuedButtonChangeMask", "uint64"],
    ["m_nButtonDoublePressed", "uint64"],
    ["m_pButtonPressedCmdNumber", "uint32[64]"],
    ["m_nLastCommandNumberProcessed", "uint32"],
    ["m_nToggleButtonDownMask", "uint64"],
    ["m_flMaxspeed", "float32"],
    ["m_arrForceSubtickMoveWhen", "float32[4]"],
    ["m_flForwardMove", "float32"],
    ["m_flLeftMove", "float32"],
    ["m_flUpMove", "float32"],
    ["m_vecLastMovementImpulses", "Vector"],
    ["m_vecOldViewAngles", "QAngle"],
]) }}

## CEnvSoundscape

{{ get_arguments_table([
    ["m_OnPlay", "CEntityIOOutput"],
    ["m_flRadius", "float32"],
    ["m_soundEventName", "CUtlSymbolLarge"],
    ["m_bOverrideWithEvent", "bool"],
    ["m_soundscapeIndex", "int32"],
    ["m_soundscapeEntityListId", "int32"],
    ["m_positionNames", "CUtlSymbolLarge[8]"],
    ["m_hProxySoundscape", "CHandle< CEnvSoundscape >"],
    ["m_bDisabled", "bool"],
    ["m_soundscapeName", "CUtlSymbolLarge"],
    ["m_soundEventHash", "uint32"],
]) }}

## CBasePlayerVData

{{ get_arguments_table([
    ["m_sModelName", "CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >"],
    ["m_flHeadDamageMultiplier", "CSkillFloat"],
    ["m_flChestDamageMultiplier", "CSkillFloat"],
    ["m_flStomachDamageMultiplier", "CSkillFloat"],
    ["m_flArmDamageMultiplier", "CSkillFloat"],
    ["m_flLegDamageMultiplier", "CSkillFloat"],
    ["m_flHoldBreathTime", "float32"],
    ["m_flDrowningDamageInterval", "float32"],
    ["m_nDrowningDamageInitial", "int32"],
    ["m_nDrowningDamageMax", "int32"],
    ["m_nWaterSpeed", "int32"],
    ["m_flUseRange", "float32"],
    ["m_flUseAngleTolerance", "float32"],
    ["m_flCrouchTime", "float32"],
]) }}

## CCSPlayerController_InGameMoneyServices

{{ get_arguments_table([
    ["m_iAccount", "int32"],
    ["m_iStartAccount", "int32"],
    ["m_iTotalCashSpent", "int32"],
    ["m_iCashSpentThisRound", "int32"],
]) }}

## C_EnvWindShared::WindVariationEvent_t

{{ get_arguments_table([
    ["m_flWindAngleVariation", "float32"],
    ["m_flWindSpeedVariation", "float32"],
]) }}

## C_EnvParticleGlow

{{ get_arguments_table([
    ["m_flAlphaScale", "float32"],
    ["m_flRadiusScale", "float32"],
    ["m_flSelfIllumScale", "float32"],
    ["m_ColorTint", "Color"],
    ["m_hTextureOverride", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
]) }}

## C_SoundEventEntity

{{ get_arguments_table([
    ["m_bStartOnSpawn", "bool"],
    ["m_bToLocalPlayer", "bool"],
    ["m_bStopOnNew", "bool"],
    ["m_bSaveRestore", "bool"],
    ["m_bSavedIsPlaying", "bool"],
    ["m_flSavedElapsedTime", "float32"],
    ["m_iszSourceEntityName", "CUtlSymbolLarge"],
    ["m_iszAttachmentName", "CUtlSymbolLarge"],
    ["m_onGUIDChanged", "CEntityOutputTemplate< uint64 >"],
    ["m_onSoundFinished", "CEntityIOOutput"],
    ["m_flClientCullRadius", "float32"],
    ["m_iszSoundName", "CUtlSymbolLarge"],
    ["m_hSource", "CEntityHandle"],
    ["m_nEntityIndexSelection", "int32"],
    ["m_bClientSideOnly", "bitfield:1"],
]) }}

## C_Sun

{{ get_arguments_table([
    ["m_fxSSSunFlareEffectIndex", "ParticleIndex_t"],
    ["m_fxSunFlareEffectIndex", "ParticleIndex_t"],
    ["m_fdistNormalize", "float32"],
    ["m_vSunPos", "Vector"],
    ["m_vDirection", "Vector"],
    ["m_iszEffectName", "CUtlSymbolLarge"],
    ["m_iszSSEffectName", "CUtlSymbolLarge"],
    ["m_clrOverlay", "Color"],
    ["m_bOn", "bool"],
    ["m_bmaxColor", "bool"],
    ["m_flSize", "float32"],
    ["m_flHazeScale", "float32"],
    ["m_flRotation", "float32"],
    ["m_flHDRColorScale", "float32"],
    ["m_flAlphaHaze", "float32"],
    ["m_flAlphaScale", "float32"],
    ["m_flAlphaHdr", "float32"],
    ["m_flFarZScale", "float32"],
]) }}

## CCSPlayerController_ActionTrackingServices

{{ get_arguments_table([
    ["m_perRoundStats", "C_UtlVectorEmbeddedNetworkVar< CSPerRoundStats_t >"],
    ["m_matchStats", "CSMatchStats_t"],
    ["m_iNumRoundKills", "int32"],
    ["m_iNumRoundKillsHeadshots", "int32"],
    ["m_unTotalRoundDamageDealt", "uint32"],
]) }}

## CHitboxComponent

{{ get_arguments_table([
    ["m_bvDisabledHitGroups", "uint32[1]"],
]) }}

## C_ColorCorrectionVolume

{{ get_arguments_table([
    ["m_LastEnterWeight", "float32"],
    ["m_LastEnterTime", "float32"],
    ["m_LastExitWeight", "float32"],
    ["m_LastExitTime", "float32"],
    ["m_bEnabled", "bool"],
    ["m_MaxWeight", "float32"],
    ["m_FadeDuration", "float32"],
    ["m_Weight", "float32"],
    ["m_lookupFilename", "char[512]"],
]) }}

## C_BulletHitModel

{{ get_arguments_table([
    ["m_matLocal", "matrix3x4_t"],
    ["m_iBoneIndex", "int32"],
    ["m_hPlayerParent", "CHandle< C_BaseEntity >"],
    ["m_bIsHit", "bool"],
    ["m_flTimeCreated", "float32"],
    ["m_vecStartPos", "Vector"],
]) }}

## C_MapVetoPickController

{{ get_arguments_table([
    ["m_nDraftType", "int32"],
    ["m_nTeamWinningCoinToss", "int32"],
    ["m_nTeamWithFirstChoice", "int32[64]"],
    ["m_nVoteMapIdsList", "int32[7]"],
    ["m_nAccountIDs", "int32[64]"],
    ["m_nMapId0", "int32[64]"],
    ["m_nMapId1", "int32[64]"],
    ["m_nMapId2", "int32[64]"],
    ["m_nMapId3", "int32[64]"],
    ["m_nMapId4", "int32[64]"],
    ["m_nMapId5", "int32[64]"],
    ["m_nStartingSide0", "int32[64]"],
    ["m_nCurrentPhase", "int32"],
    ["m_nPhaseStartTick", "int32"],
    ["m_nPhaseDurationTicks", "int32"],
    ["m_nPostDataUpdateTick", "int32"],
    ["m_bDisabledHud", "bool"],
]) }}

## C_OmniLight

{{ get_arguments_table([
    ["m_flInnerAngle", "float32"],
    ["m_flOuterAngle", "float32"],
    ["m_bShowLight", "bool"],
]) }}

## WeaponPurchaseTracker_t

{{ get_arguments_table([
    ["m_weaponPurchases", "C_UtlVectorEmbeddedNetworkVar< WeaponPurchaseCount_t >"],
]) }}

## C_RetakeGameRules

{{ get_arguments_table([
    ["m_nMatchSeed", "int32"],
    ["m_bBlockersPresent", "bool"],
    ["m_bRoundInProgress", "bool"],
    ["m_iFirstSecondHalfRound", "int32"],
    ["m_iBombSite", "int32"],
]) }}

## EngineCountdownTimer

{{ get_arguments_table([
    ["m_duration", "float32"],
    ["m_timestamp", "float32"],
    ["m_timescale", "float32"],
]) }}

## C_BaseFlex::Emphasized_Phoneme

{{ get_arguments_table([
    ["m_sClassName", "CUtlString"],
    ["m_flAmount", "float32"],
    ["m_bRequired", "bool"],
    ["m_bBasechecked", "bool"],
    ["m_bValid", "bool"],
]) }}

## IntervalTimer

{{ get_arguments_table([
    ["m_timestamp", "GameTime_t"],
    ["m_nWorldGroupId", "WorldGroupId_t"],
]) }}

## C_FuncLadder

{{ get_arguments_table([
    ["m_vecLadderDir", "Vector"],
    ["m_Dismounts", "CUtlVector< CHandle< C_InfoLadderDismount > >"],
    ["m_vecLocalTop", "Vector"],
    ["m_vecPlayerMountPositionTop", "Vector"],
    ["m_vecPlayerMountPositionBottom", "Vector"],
    ["m_flAutoRideSpeed", "float32"],
    ["m_bDisabled", "bool"],
    ["m_bFakeLadder", "bool"],
    ["m_bHasSlack", "bool"],
]) }}

## CPlayer_WeaponServices

{{ get_arguments_table([
    ["m_hMyWeapons", "C_NetworkUtlVectorBase< CHandle< C_BasePlayerWeapon > >"],
    ["m_hActiveWeapon", "CHandle< C_BasePlayerWeapon >"],
    ["m_hLastWeapon", "CHandle< C_BasePlayerWeapon >"],
    ["m_iAmmo", "uint16[32]"],
]) }}

## CAttributeManager::cached_attribute_float_t

{{ get_arguments_table([
    ["flIn", "float32"],
    ["iAttribHook", "CUtlSymbolLarge"],
    ["flOut", "float32"],
]) }}

## C_BaseGrenade

{{ get_arguments_table([
    ["m_bHasWarnedAI", "bool"],
    ["m_bIsSmokeGrenade", "bool"],
    ["m_bIsLive", "bool"],
    ["m_DmgRadius", "float32"],
    ["m_flDetonateTime", "GameTime_t"],
    ["m_flWarnAITime", "float32"],
    ["m_flDamage", "float32"],
    ["m_iszBounceSound", "CUtlSymbolLarge"],
    ["m_ExplosionSound", "CUtlString"],
    ["m_hThrower", "CHandle< C_CSPlayerPawn >"],
    ["m_flNextAttack", "GameTime_t"],
    ["m_hOriginalThrower", "CHandle< C_CSPlayerPawn >"],
]) }}

## CCSGameModeRules

{{ get_arguments_table([
    ["__m_pChainEntity", "CNetworkVarChainer"],
]) }}

## VPhysicsCollisionAttribute_t

{{ get_arguments_table([
    ["m_nInteractsAs", "uint64"],
    ["m_nInteractsWith", "uint64"],
    ["m_nInteractsExclude", "uint64"],
    ["m_nEntityId", "uint32"],
    ["m_nOwnerId", "uint32"],
    ["m_nHierarchyId", "uint16"],
    ["m_nCollisionGroup", "uint8"],
    ["m_nCollisionFunctionMask", "uint8"],
]) }}

## C_EnvVolumetricFogController

{{ get_arguments_table([
    ["m_flScattering", "float32"],
    ["m_flAnisotropy", "float32"],
    ["m_flFadeSpeed", "float32"],
    ["m_flDrawDistance", "float32"],
    ["m_flFadeInStart", "float32"],
    ["m_flFadeInEnd", "float32"],
    ["m_flIndirectStrength", "float32"],
    ["m_nVolumeDepth", "int32"],
    ["m_fFirstVolumeSliceThickness", "float32"],
    ["m_nIndirectTextureDimX", "int32"],
    ["m_nIndirectTextureDimY", "int32"],
    ["m_nIndirectTextureDimZ", "int32"],
    ["m_vBoxMins", "Vector"],
    ["m_vBoxMaxs", "Vector"],
    ["m_bActive", "bool"],
    ["m_flStartAnisoTime", "GameTime_t"],
    ["m_flStartScatterTime", "GameTime_t"],
    ["m_flStartDrawDistanceTime", "GameTime_t"],
    ["m_flStartAnisotropy", "float32"],
    ["m_flStartScattering", "float32"],
    ["m_flStartDrawDistance", "float32"],
    ["m_flDefaultAnisotropy", "float32"],
    ["m_flDefaultScattering", "float32"],
    ["m_flDefaultDrawDistance", "float32"],
    ["m_bStartDisabled", "bool"],
    ["m_bEnableIndirect", "bool"],
    ["m_bIndirectUseLPVs", "bool"],
    ["m_bIsMaster", "bool"],
    ["m_hFogIndirectTexture", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_nForceRefreshCount", "int32"],
    ["m_fNoiseSpeed", "float32"],
    ["m_fNoiseStrength", "float32"],
    ["m_vNoiseScale", "Vector"],
    ["m_bFirstTime", "bool"],
]) }}

## C_PointCommentaryNode

{{ get_arguments_table([
    ["m_bActive", "bool"],
    ["m_bWasActive", "bool"],
    ["m_flEndTime", "GameTime_t"],
    ["m_flStartTime", "GameTime_t"],
    ["m_flStartTimeInCommentary", "float32"],
    ["m_iszCommentaryFile", "CUtlSymbolLarge"],
    ["m_iszTitle", "CUtlSymbolLarge"],
    ["m_iszSpeakers", "CUtlSymbolLarge"],
    ["m_iNodeNumber", "int32"],
    ["m_iNodeNumberMax", "int32"],
    ["m_bListenedTo", "bool"],
    ["m_hViewPosition", "CHandle< C_BaseEntity >"],
    ["m_bRestartAfterRestore", "bool"],
]) }}

## audioparams_t

{{ get_arguments_table([
    ["localSound", "Vector[8]"],
    ["soundscapeIndex", "int32"],
    ["localBits", "uint8"],
    ["soundscapeEntityListIndex", "int32"],
    ["soundEventHash", "uint32"],
]) }}

## C_InfoVisibilityBox

{{ get_arguments_table([
    ["m_nMode", "int32"],
    ["m_vBoxSize", "Vector"],
    ["m_bEnabled", "bool"],
]) }}

## C_FireSprite

{{ get_arguments_table([
    ["m_vecMoveDir", "Vector"],
    ["m_bFadeFromAbove", "bool"],
]) }}

## C_Precipitation

{{ get_arguments_table([
    ["m_flDensity", "float32"],
    ["m_flParticleInnerDist", "float32"],
    ["m_pParticleDef", "char*"],
    ["m_tParticlePrecipTraceTimer", "TimedEvent[1]"],
    ["m_bActiveParticlePrecipEmitter", "bool[1]"],
    ["m_bParticlePrecipInitialized", "bool"],
    ["m_bHasSimulatedSinceLastSceneObjectUpdate", "bool"],
    ["m_nAvailableSheetSequencesMaxIndex", "int32"],
]) }}

## CPrecipitationVData

{{ get_arguments_table([
    ["m_szParticlePrecipitationEffect", "CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >"],
    ["m_flInnerDistance", "float32"],
    ["m_nAttachType", "ParticleAttachment_t"],
    ["m_bBatchSameVolumeType", "bool"],
    ["m_nRTEnvCP", "int32"],
    ["m_nRTEnvCPComponent", "int32"],
    ["m_szModifier", "CUtlString"],
]) }}

## CBuoyancyHelper

{{ get_arguments_table([
    ["m_nFluidType", "CUtlStringToken"],
    ["m_flFluidDensity", "float32"],
    ["m_vecFractionOfWheelSubmergedForWheelFriction", "CUtlVector< float32 >"],
    ["m_vecWheelFrictionScales", "CUtlVector< float32 >"],
    ["m_vecFractionOfWheelSubmergedForWheelDrag", "CUtlVector< float32 >"],
    ["m_vecWheelDrag", "CUtlVector< float32 >"],
]) }}

## C_BaseClientUIEntity

{{ get_arguments_table([
    ["m_bEnabled", "bool"],
    ["m_DialogXMLName", "CUtlSymbolLarge"],
    ["m_PanelClassName", "CUtlSymbolLarge"],
    ["m_PanelID", "CUtlSymbolLarge"],
]) }}

## C_FuncTrackTrain

{{ get_arguments_table([
    ["m_nLongAxis", "int32"],
    ["m_flRadius", "float32"],
    ["m_flLineLength", "float32"],
]) }}

## CCSPlayer_ActionTrackingServices

{{ get_arguments_table([
    ["m_hLastWeaponBeforeC4AutoSwitch", "CHandle< C_BasePlayerWeapon >"],
    ["m_bIsRescuing", "bool"],
    ["m_weaponPurchasesThisMatch", "WeaponPurchaseTracker_t"],
    ["m_weaponPurchasesThisRound", "WeaponPurchaseTracker_t"],
]) }}

## shard_model_desc_t

{{ get_arguments_table([
    ["m_nModelID", "int32"],
    ["m_hMaterialBase", "CStrongHandle< InfoForResourceTypeIMaterial2 >"],
    ["m_hMaterialDamageOverlay", "CStrongHandle< InfoForResourceTypeIMaterial2 >"],
    ["m_solid", "ShardSolid_t"],
    ["m_vecPanelSize", "Vector2D"],
    ["m_vecStressPositionA", "Vector2D"],
    ["m_vecStressPositionB", "Vector2D"],
    ["m_vecPanelVertices", "C_NetworkUtlVectorBase< Vector2D >"],
    ["m_vInitialPanelVertices", "C_NetworkUtlVectorBase< Vector4D >"],
    ["m_flGlassHalfThickness", "float32"],
    ["m_bHasParent", "bool"],
    ["m_bParentFrozen", "bool"],
    ["m_SurfacePropStringToken", "CUtlStringToken"],
]) }}

## C_SceneEntity::QueuedEvents_t

{{ get_arguments_table([
    ["starttime", "float32"],
]) }}

## CBaseProp

{{ get_arguments_table([
    ["m_bModelOverrodeBlockLOS", "bool"],
    ["m_iShapeType", "int32"],
    ["m_bConformToCollisionBounds", "bool"],
    ["m_mPreferredCatchTransform", "matrix3x4_t"],
]) }}

## CPointTemplate

{{ get_arguments_table([
    ["m_iszWorldName", "CUtlSymbolLarge"],
    ["m_iszSource2EntityLumpName", "CUtlSymbolLarge"],
    ["m_iszEntityFilterName", "CUtlSymbolLarge"],
    ["m_flTimeoutInterval", "float32"],
    ["m_bAsynchronouslySpawnEntities", "bool"],
    ["m_pOutputOnSpawned", "CEntityIOOutput"],
    ["m_clientOnlyEntityBehavior", "PointTemplateClientOnlyEntityBehavior_t"],
    ["m_ownerSpawnGroupType", "PointTemplateOwnerSpawnGroupType_t"],
    ["m_createdSpawnGroupHandles", "CUtlVector< uint32 >"],
    ["m_SpawnedEntityHandles", "CUtlVector< CEntityHandle >"],
    ["m_ScriptSpawnCallback", "HSCRIPT"],
    ["m_ScriptCallbackScope", "HSCRIPT"],
]) }}

## C_CSGO_PreviewModel

{{ get_arguments_table([
    ["m_animgraph", "CUtlString"],
    ["m_animgraphCharacterModeString", "CGlobalSymbol"],
    ["m_defaultAnim", "CUtlString"],
    ["m_nDefaultAnimLoopMode", "AnimLoopMode_t"],
    ["m_flInitialModelScale", "float32"],
    ["m_sInitialWeaponState", "CUtlString"],
]) }}

## CInfoDynamicShadowHint

{{ get_arguments_table([
    ["m_bDisabled", "bool"],
    ["m_flRange", "float32"],
    ["m_nImportance", "int32"],
    ["m_nLightChoice", "int32"],
    ["m_hLight", "CHandle< C_BaseEntity >"],
]) }}

## CGlowProperty

{{ get_arguments_table([
    ["m_fGlowColor", "Vector"],
    ["m_iGlowType", "int32"],
    ["m_iGlowTeam", "int32"],
    ["m_nGlowRange", "int32"],
    ["m_nGlowRangeMin", "int32"],
    ["m_glowColorOverride", "Color"],
    ["m_bFlashing", "bool"],
    ["m_flGlowTime", "float32"],
    ["m_flGlowStartTime", "float32"],
    ["m_bEligibleForScreenHighlight", "bool"],
    ["m_bGlowing", "bool"],
]) }}

## C_TriggerPhysics

{{ get_arguments_table([
    ["m_gravityScale", "float32"],
    ["m_linearLimit", "float32"],
    ["m_linearDamping", "float32"],
    ["m_angularLimit", "float32"],
    ["m_angularDamping", "float32"],
    ["m_linearForce", "float32"],
    ["m_flFrequency", "float32"],
    ["m_flDampingRatio", "float32"],
    ["m_vecLinearForcePointAt", "Vector"],
    ["m_bCollapseToForcePoint", "bool"],
    ["m_vecLinearForcePointAtWorld", "Vector"],
    ["m_vecLinearForceDirection", "Vector"],
    ["m_bConvertToDebrisWhenPossible", "bool"],
]) }}

## CCSPlayer_HostageServices

{{ get_arguments_table([
    ["m_hCarriedHostage", "CHandle< C_BaseEntity >"],
    ["m_hCarriedHostageProp", "CHandle< C_BaseEntity >"],
]) }}

## C_EnvCubemap

{{ get_arguments_table([
    ["m_Entity_hCubemapTexture", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_Entity_bCustomCubemapTexture", "bool"],
    ["m_Entity_flInfluenceRadius", "float32"],
    ["m_Entity_vBoxProjectMins", "Vector"],
    ["m_Entity_vBoxProjectMaxs", "Vector"],
    ["m_Entity_bMoveable", "bool"],
    ["m_Entity_nHandshake", "int32"],
    ["m_Entity_nEnvCubeMapArrayIndex", "int32"],
    ["m_Entity_nPriority", "int32"],
    ["m_Entity_flEdgeFadeDist", "float32"],
    ["m_Entity_vEdgeFadeDists", "Vector"],
    ["m_Entity_flDiffuseScale", "float32"],
    ["m_Entity_bStartDisabled", "bool"],
    ["m_Entity_bDefaultEnvMap", "bool"],
    ["m_Entity_bDefaultSpecEnvMap", "bool"],
    ["m_Entity_bIndoorCubeMap", "bool"],
    ["m_Entity_bCopyDiffuseFromDefaultCubemap", "bool"],
    ["m_Entity_bEnabled", "bool"],
]) }}

## C_PredictedViewModel

{{ get_arguments_table([
    ["m_vPredictedLagOffset", "Vector"],
    ["m_targetSpeed", "QAngle"],
    ["m_currentSpeed", "QAngle"],
]) }}

## C_PointValueRemapper

{{ get_arguments_table([
    ["m_bDisabled", "bool"],
    ["m_bDisabledOld", "bool"],
    ["m_bUpdateOnClient", "bool"],
    ["m_nInputType", "ValueRemapperInputType_t"],
    ["m_hRemapLineStart", "CHandle< C_BaseEntity >"],
    ["m_hRemapLineEnd", "CHandle< C_BaseEntity >"],
    ["m_flMaximumChangePerSecond", "float32"],
    ["m_flDisengageDistance", "float32"],
    ["m_flEngageDistance", "float32"],
    ["m_bRequiresUseKey", "bool"],
    ["m_nOutputType", "ValueRemapperOutputType_t"],
    ["m_hOutputEntities", "C_NetworkUtlVectorBase< CHandle< C_BaseEntity > >"],
    ["m_nHapticsType", "ValueRemapperHapticsType_t"],
    ["m_nMomentumType", "ValueRemapperMomentumType_t"],
    ["m_flMomentumModifier", "float32"],
    ["m_flSnapValue", "float32"],
    ["m_flCurrentMomentum", "float32"],
    ["m_nRatchetType", "ValueRemapperRatchetType_t"],
    ["m_flRatchetOffset", "float32"],
    ["m_flInputOffset", "float32"],
    ["m_bEngaged", "bool"],
    ["m_bFirstUpdate", "bool"],
    ["m_flPreviousValue", "float32"],
    ["m_flPreviousUpdateTickTime", "GameTime_t"],
    ["m_vecPreviousTestPoint", "Vector"],
]) }}

## C_Knife

{{ get_arguments_table([
    ["m_bFirstAttack", "bool"],
]) }}

## C_ItemDogtags

{{ get_arguments_table([
    ["m_OwningPlayer", "CHandle< C_CSPlayerPawn >"],
    ["m_KillingPlayer", "CHandle< C_CSPlayerPawn >"],
]) }}

## C_SoundOpvarSetPointBase

{{ get_arguments_table([
    ["m_iszStackName", "CUtlSymbolLarge"],
    ["m_iszOperatorName", "CUtlSymbolLarge"],
    ["m_iszOpvarName", "CUtlSymbolLarge"],
    ["m_iOpvarIndex", "int32"],
    ["m_bUseAutoCompare", "bool"],
]) }}

## CCSPlayer_BuyServices

{{ get_arguments_table([
    ["m_vecSellbackPurchaseEntries", "C_UtlVectorEmbeddedNetworkVar< SellbackPurchaseEntry_t >"],
]) }}

## C_WeaponTaser

{{ get_arguments_table([
    ["m_fFireTime", "GameTime_t"],
    ["m_nLastAttackTick", "int32"],
]) }}

## C_Fists

{{ get_arguments_table([
    ["m_bPlayingUninterruptableAct", "bool"],
    ["m_nUninterruptableActivity", "PlayerAnimEvent_t"],
]) }}

## CInfoDynamicShadowHintBox

{{ get_arguments_table([
    ["m_vBoxMins", "Vector"],
    ["m_vBoxMaxs", "Vector"],
]) }}

## C_EnvCubemapFog

{{ get_arguments_table([
    ["m_flEndDistance", "float32"],
    ["m_flStartDistance", "float32"],
    ["m_flFogFalloffExponent", "float32"],
    ["m_bHeightFogEnabled", "bool"],
    ["m_flFogHeightWidth", "float32"],
    ["m_flFogHeightEnd", "float32"],
    ["m_flFogHeightStart", "float32"],
    ["m_flFogHeightExponent", "float32"],
    ["m_flLODBias", "float32"],
    ["m_bActive", "bool"],
    ["m_bStartDisabled", "bool"],
    ["m_flFogMaxOpacity", "float32"],
    ["m_nCubemapSourceType", "int32"],
    ["m_hSkyMaterial", "CStrongHandle< InfoForResourceTypeIMaterial2 >"],
    ["m_iszSkyEntity", "CUtlSymbolLarge"],
    ["m_hFogCubemapTexture", "CStrongHandle< InfoForResourceTypeCTextureBase >"],
    ["m_bHasHeightFogEnd", "bool"],
    ["m_bFirstTime", "bool"],
]) }}

## CCollisionProperty

{{ get_arguments_table([
    ["m_collisionAttribute", "VPhysicsCollisionAttribute_t"],
    ["m_vecMins", "Vector"],
    ["m_vecMaxs", "Vector"],
    ["m_usSolidFlags", "uint8"],
    ["m_nSolidType", "SolidType_t"],
    ["m_triggerBloat", "uint8"],
    ["m_nSurroundType", "SurroundingBoundsType_t"],
    ["m_CollisionGroup", "uint8"],
    ["m_nEnablePhysics", "uint8"],
    ["m_flBoundingRadius", "float32"],
    ["m_vecSpecifiedSurroundingMins", "Vector"],
    ["m_vecSpecifiedSurroundingMaxs", "Vector"],
    ["m_vecSurroundingMaxs", "Vector"],
    ["m_vecSurroundingMins", "Vector"],
    ["m_vCapsuleCenter1", "Vector"],
    ["m_vCapsuleCenter2", "Vector"],
    ["m_flCapsuleRadius", "float32"],
]) }}

## CNetworkedSequenceOperation

{{ get_arguments_table([
    ["m_hSequence", "HSequence"],
    ["m_flPrevCycle", "float32"],
    ["m_flCycle", "float32"],
    ["m_flWeight", "CNetworkedQuantizedFloat"],
    ["m_bSequenceChangeNetworked", "bool"],
    ["m_bDiscontinuity", "bool"],
    ["m_flPrevCycleFromDiscontinuity", "float32"],
    ["m_flPrevCycleForAnimEventDetection", "float32"],
]) }}

## C_PlayerSprayDecal

{{ get_arguments_table([
    ["m_nUniqueID", "int32"],
    ["m_unAccountID", "uint32"],
    ["m_unTraceID", "uint32"],
    ["m_rtGcTime", "uint32"],
    ["m_vecEndPos", "Vector"],
    ["m_vecStart", "Vector"],
    ["m_vecLeft", "Vector"],
    ["m_vecNormal", "Vector"],
    ["m_nPlayer", "int32"],
    ["m_nEntity", "int32"],
    ["m_nHitbox", "int32"],
    ["m_flCreationTime", "float32"],
    ["m_nTintID", "int32"],
    ["m_nVersion", "uint8"],
    ["m_ubSignature", "uint8[128]"],
    ["m_SprayRenderHelper", "CPlayerSprayDecalRenderHelper"],
]) }}

## EntityRenderAttribute_t

{{ get_arguments_table([
    ["m_ID", "CUtlStringToken"],
    ["m_Values", "Vector4D"],
]) }}

## C_ShatterGlassShardPhysics

{{ get_arguments_table([
    ["m_ShardDesc", "shard_model_desc_t"],
]) }}

## C_LightEntity

{{ get_arguments_table([
    ["m_CLightComponent", "CLightComponent*"],
]) }}

## C_PlayerVisibility

{{ get_arguments_table([
    ["m_flVisibilityStrength", "float32"],
    ["m_flFogDistanceMultiplier", "float32"],
    ["m_flFogMaxDensityMultiplier", "float32"],
    ["m_flFadeTime", "float32"],
    ["m_bStartDisabled", "bool"],
    ["m_bIsEnabled", "bool"],
]) }}

## fogparams_t

{{ get_arguments_table([
    ["dirPrimary", "Vector"],
    ["colorPrimary", "Color"],
    ["colorSecondary", "Color"],
    ["colorPrimaryLerpTo", "Color"],
    ["colorSecondaryLerpTo", "Color"],
    ["start", "float32"],
    ["end", "float32"],
    ["farz", "float32"],
    ["maxdensity", "float32"],
    ["exponent", "float32"],
    ["HDRColorScale", "float32"],
    ["skyboxFogFactor", "float32"],
    ["skyboxFogFactorLerpTo", "float32"],
    ["startLerpTo", "float32"],
    ["endLerpTo", "float32"],
    ["maxdensityLerpTo", "float32"],
    ["lerptime", "GameTime_t"],
    ["duration", "float32"],
    ["blendtobackground", "float32"],
    ["scattering", "float32"],
    ["locallightscale", "float32"],
    ["enable", "bool"],
    ["blend", "bool"],
    ["m_bNoReflectionFog", "bool"],
    ["m_bPadding", "bool"],
]) }}

## C_BaseFlex

{{ get_arguments_table([
    ["m_flexWeight", "C_NetworkUtlVectorBase< float32 >"],
    ["m_vLookTargetPosition", "Vector"],
    ["m_blinktoggle", "bool"],
    ["m_nLastFlexUpdateFrameCount", "int32"],
    ["m_CachedViewTarget", "Vector"],
    ["m_nNextSceneEventId", "SceneEventId_t"],
    ["m_iBlink", "int32"],
    ["m_blinktime", "float32"],
    ["m_prevblinktoggle", "bool"],
    ["m_iJawOpen", "int32"],
    ["m_flJawOpenAmount", "float32"],
    ["m_flBlinkAmount", "float32"],
    ["m_iMouthAttachment", "AttachmentHandle_t"],
    ["m_iEyeAttachment", "AttachmentHandle_t"],
    ["m_bResetFlexWeightsOnModelChange", "bool"],
    ["m_nEyeOcclusionRendererBone", "int32"],
    ["m_mEyeOcclusionRendererCameraToBoneTransform", "matrix3x4_t"],
    ["m_vEyeOcclusionRendererHalfExtent", "Vector"],
    ["m_PhonemeClasses", "C_BaseFlex::Emphasized_Phoneme[3]"],
]) }}

## C_EnvSky

{{ get_arguments_table([
    ["m_hSkyMaterial", "CStrongHandle< InfoForResourceTypeIMaterial2 >"],
    ["m_hSkyMaterialLightingOnly", "CStrongHandle< InfoForResourceTypeIMaterial2 >"],
    ["m_bStartDisabled", "bool"],
    ["m_vTintColor", "Color"],
    ["m_vTintColorLightingOnly", "Color"],
    ["m_flBrightnessScale", "float32"],
    ["m_nFogType", "int32"],
    ["m_flFogMinStart", "float32"],
    ["m_flFogMinEnd", "float32"],
    ["m_flFogMaxStart", "float32"],
    ["m_flFogMaxEnd", "float32"],
    ["m_bEnabled", "bool"],
]) }}

## C_DynamicProp

{{ get_arguments_table([
    ["m_bUseHitboxesForRenderBox", "bool"],
    ["m_bUseAnimGraph", "bool"],
    ["m_pOutputAnimBegun", "CEntityIOOutput"],
    ["m_pOutputAnimOver", "CEntityIOOutput"],
    ["m_pOutputAnimLoopCycleOver", "CEntityIOOutput"],
    ["m_OnAnimReachedStart", "CEntityIOOutput"],
    ["m_OnAnimReachedEnd", "CEntityIOOutput"],
    ["m_iszIdleAnim", "CUtlSymbolLarge"],
    ["m_nIdleAnimLoopMode", "AnimLoopMode_t"],
    ["m_bRandomizeCycle", "bool"],
    ["m_bStartDisabled", "bool"],
    ["m_bFiredStartEndOutput", "bool"],
    ["m_bForceNpcExclude", "bool"],
    ["m_bCreateNonSolid", "bool"],
    ["m_bIsOverrideProp", "bool"],
    ["m_iInitialGlowState", "int32"],
    ["m_nGlowRange", "int32"],
    ["m_nGlowRangeMin", "int32"],
    ["m_glowColor", "Color"],
    ["m_nGlowTeam", "int32"],
    ["m_iCachedFrameCount", "int32"],
    ["m_vecCachedRenderMins", "Vector"],
    ["m_vecCachedRenderMaxs", "Vector"],
]) }}

## CPropDataComponent

{{ get_arguments_table([
    ["m_flDmgModBullet", "float32"],
    ["m_flDmgModClub", "float32"],
    ["m_flDmgModExplosive", "float32"],
    ["m_flDmgModFire", "float32"],
    ["m_iszPhysicsDamageTableName", "CUtlSymbolLarge"],
    ["m_iszBasePropData", "CUtlSymbolLarge"],
    ["m_nInteractions", "int32"],
    ["m_bSpawnMotionDisabled", "bool"],
    ["m_nDisableTakePhysicsDamageSpawnFlag", "int32"],
    ["m_nMotionDisabledSpawnFlag", "int32"],
]) }}

## C_KeychainModule

{{ get_arguments_table([
    ["m_nKeychainDefID", "uint32"],
    ["m_nKeychainSeed", "uint32"],
]) }}

## CCitadelSoundOpvarSetOBB

{{ get_arguments_table([
    ["m_iszStackName", "CUtlSymbolLarge"],
    ["m_iszOperatorName", "CUtlSymbolLarge"],
    ["m_iszOpvarName", "CUtlSymbolLarge"],
    ["m_vDistanceInnerMins", "Vector"],
    ["m_vDistanceInnerMaxs", "Vector"],
    ["m_vDistanceOuterMins", "Vector"],
    ["m_vDistanceOuterMaxs", "Vector"],
    ["m_nAABBDirection", "int32"],
]) }}

## SellbackPurchaseEntry_t

{{ get_arguments_table([
    ["m_unDefIdx", "uint16"],
    ["m_nCost", "int32"],
    ["m_nPrevArmor", "int32"],
    ["m_bPrevHelmet", "bool"],
    ["m_hItem", "CEntityHandle"],
]) }}

## C_LocalTempEntity

{{ get_arguments_table([
    ["flags", "int32"],
    ["die", "GameTime_t"],
    ["m_flFrameMax", "float32"],
    ["x", "float32"],
    ["y", "float32"],
    ["fadeSpeed", "float32"],
    ["bounceFactor", "float32"],
    ["hitSound", "int32"],
    ["priority", "int32"],
    ["tentOffset", "Vector"],
    ["m_vecTempEntAngVelocity", "QAngle"],
    ["tempent_renderamt", "int32"],
    ["m_vecNormal", "Vector"],
    ["m_flSpriteScale", "float32"],
    ["m_nFlickerFrame", "int32"],
    ["m_flFrameRate", "float32"],
    ["m_flFrame", "float32"],
    ["m_pszImpactEffect", "char*"],
    ["m_pszParticleEffect", "char*"],
    ["m_bParticleCollision", "bool"],
    ["m_iLastCollisionFrame", "int32"],
    ["m_vLastCollisionOrigin", "Vector"],
    ["m_vecTempEntVelocity", "Vector"],
    ["m_vecPrevAbsOrigin", "Vector"],
    ["m_vecTempEntAcceleration", "Vector"],
]) }}

## C_EnvWindShared::WindAveEvent_t

{{ get_arguments_table([
    ["m_flStartWindSpeed", "float32"],
    ["m_flAveWindSpeed", "float32"],
]) }}

## C_MolotovProjectile

{{ get_arguments_table([
    ["m_bIsIncGrenade", "bool"],
]) }}

## CInfoOffscreenPanoramaTexture

{{ get_arguments_table([
    ["m_bDisabled", "bool"],
    ["m_nResolutionX", "int32"],
    ["m_nResolutionY", "int32"],
    ["m_szLayoutFileName", "CUtlSymbolLarge"],
    ["m_RenderAttrName", "CUtlSymbolLarge"],
    ["m_TargetEntities", "C_NetworkUtlVectorBase< CHandle< C_BaseModelEntity > >"],
    ["m_nTargetChangeCount", "int32"],
    ["m_vecCSSClasses", "C_NetworkUtlVectorBase< CUtlSymbolLarge >"],
    ["m_bCheckCSSClasses", "bool"],
]) }}

## C_DynamicLight

{{ get_arguments_table([
    ["m_Flags", "uint8"],
    ["m_LightStyle", "uint8"],
    ["m_Radius", "float32"],
    ["m_Exponent", "int32"],
    ["m_InnerAngle", "float32"],
    ["m_OuterAngle", "float32"],
    ["m_SpotRadius", "float32"],
]) }}

## C_CSWeaponBase

{{ get_arguments_table([
    ["m_flFireSequenceStartTime", "float32"],
    ["m_nFireSequenceStartTimeChange", "int32"],
    ["m_nFireSequenceStartTimeAck", "int32"],
    ["m_ePlayerFireEvent", "PlayerAnimEvent_t"],
    ["m_ePlayerFireEventAttackType", "WeaponAttackType_t"],
    ["m_seqIdle", "HSequence"],
    ["m_seqFirePrimary", "HSequence"],
    ["m_seqFireSecondary", "HSequence"],
    ["m_thirdPersonFireSequences", "CUtlVector< HSequence >"],
    ["m_hCurrentThirdPersonSequence", "HSequence"],
    ["m_nSilencerBoneIndex", "int32"],
    ["m_thirdPersonSequences", "HSequence[7]"],
    ["m_ClientPreviousWeaponState", "CSWeaponState_t"],
    ["m_iState", "CSWeaponState_t"],
    ["m_flCrosshairDistance", "float32"],
    ["m_iAmmoLastCheck", "int32"],
    ["m_iAlpha", "int32"],
    ["m_iScopeTextureID", "int32"],
    ["m_iCrosshairTextureID", "int32"],
    ["m_flGunAccuracyPositionDeprecated", "float32"],
    ["m_nLastEmptySoundCmdNum", "int32"],
    ["m_nViewModelIndex", "uint32"],
    ["m_bReloadsWithClips", "bool"],
    ["m_flTimeWeaponIdle", "GameTime_t"],
    ["m_bFireOnEmpty", "bool"],
    ["m_OnPlayerPickup", "CEntityIOOutput"],
    ["m_weaponMode", "CSWeaponMode"],
    ["m_flTurningInaccuracyDelta", "float32"],
    ["m_vecTurningInaccuracyEyeDirLast", "Vector"],
    ["m_flTurningInaccuracy", "float32"],
    ["m_fAccuracyPenalty", "float32"],
    ["m_flLastAccuracyUpdateTime", "GameTime_t"],
    ["m_fAccuracySmoothedForZoom", "float32"],
    ["m_fScopeZoomEndTime", "GameTime_t"],
    ["m_iRecoilIndex", "int32"],
    ["m_flRecoilIndex", "float32"],
    ["m_bBurstMode", "bool"],
    ["m_flLastBurstModeChangeTime", "GameTime_t"],
    ["m_nPostponeFireReadyTicks", "GameTick_t"],
    ["m_flPostponeFireReadyFrac", "float32"],
    ["m_bInReload", "bool"],
    ["m_bReloadVisuallyComplete", "bool"],
    ["m_flDroppedAtTime", "GameTime_t"],
    ["m_bIsHauledBack", "bool"],
    ["m_bSilencerOn", "bool"],
    ["m_flTimeSilencerSwitchComplete", "GameTime_t"],
    ["m_iOriginalTeamNumber", "int32"],
    ["m_iMostRecentTeamNumber", "int32"],
    ["m_bDroppedNearBuyZone", "bool"],
    ["m_flNextAttackRenderTimeOffset", "float32"],
    ["m_bClearWeaponIdentifyingUGC", "bool"],
    ["m_bVisualsDataSet", "bool"],
    ["m_bOldFirstPersonSpectatedState", "bool"],
    ["m_bUIWeapon", "bool"],
    ["m_nCustomEconReloadEventId", "int32"],
    ["m_nextPrevOwnerUseTime", "GameTime_t"],
    ["m_hPrevOwner", "CHandle< C_CSPlayerPawn >"],
    ["m_nDropTick", "GameTick_t"],
    ["m_donated", "bool"],
    ["m_fLastShotTime", "GameTime_t"],
    ["m_bWasOwnedByCT", "bool"],
    ["m_bWasOwnedByTerrorist", "bool"],
    ["m_gunHeat", "float32"],
    ["m_smokeAttachments", "uint32"],
    ["m_lastSmokeTime", "GameTime_t"],
    ["m_flNextClientFireBulletTime", "float32"],
    ["m_flNextClientFireBulletTime_Repredict", "float32"],
    ["m_IronSightController", "C_IronSightController"],
    ["m_iIronSightMode", "int32"],
    ["m_flLastLOSTraceFailureTime", "GameTime_t"],
    ["m_iNumEmptyAttacks", "int32"],
    ["m_flLastMagDropRequestTime", "GameTime_t"],
    ["m_flWatTickOffset", "float32"],
]) }}

## C_FuncElectrifiedVolume

{{ get_arguments_table([
    ["m_nAmbientEffect", "ParticleIndex_t"],
    ["m_EffectName", "CUtlSymbolLarge"],
    ["m_bState", "bool"],
]) }}

## CCSPlayer_WeaponServices

{{ get_arguments_table([
    ["m_flNextAttack", "GameTime_t"],
    ["m_bIsLookingAtWeapon", "bool"],
    ["m_bIsHoldingLookAtWeapon", "bool"],
    ["m_nOldShootPositionHistoryCount", "uint32"],
    ["m_nOldInputHistoryCount", "uint32"],
]) }}

## C_EnvDetailController

{{ get_arguments_table([
    ["m_flFadeStartDist", "float32"],
    ["m_flFadeEndDist", "float32"],
]) }}

## C_BaseEntity

{{ get_arguments_table([
    ["m_CBodyComponent", "CBodyComponent*"],
    ["m_NetworkTransmitComponent", "CNetworkTransmitComponent"],
    ["m_nLastThinkTick", "GameTick_t"],
    ["m_pGameSceneNode", "CGameSceneNode*"],
    ["m_pRenderComponent", "CRenderComponent*"],
    ["m_pCollision", "CCollisionProperty*"],
    ["m_iMaxHealth", "int32"],
    ["m_iHealth", "int32"],
    ["m_lifeState", "uint8"],
    ["m_bTakesDamage", "bool"],
    ["m_nTakeDamageFlags", "TakeDamageFlags_t"],
    ["m_nPlatformType", "EntityPlatformTypes_t"],
    ["m_ubInterpolationFrame", "uint8"],
    ["m_hSceneObjectController", "CHandle< C_BaseEntity >"],
    ["m_nNoInterpolationTick", "int32"],
    ["m_nVisibilityNoInterpolationTick", "int32"],
    ["m_flProxyRandomValue", "float32"],
    ["m_iEFlags", "int32"],
    ["m_nWaterType", "uint8"],
    ["m_bInterpolateEvenWithNoModel", "bool"],
    ["m_bPredictionEligible", "bool"],
    ["m_bApplyLayerMatchIDToModel", "bool"],
    ["m_tokLayerMatchID", "CUtlStringToken"],
    ["m_nSubclassID", "CUtlStringToken"],
    ["m_nSimulationTick", "int32"],
    ["m_iCurrentThinkContext", "int32"],
    ["m_aThinkFunctions", "CUtlVector< thinkfunc_t >"],
    ["m_bDisabledContextThinks", "bool"],
    ["m_flAnimTime", "float32"],
    ["m_flSimulationTime", "float32"],
    ["m_nSceneObjectOverrideFlags", "uint8"],
    ["m_bHasSuccessfullyInterpolated", "bool"],
    ["m_bHasAddedVarsToInterpolation", "bool"],
    ["m_bRenderEvenWhenNotSuccessfullyInterpolated", "bool"],
    ["m_nInterpolationLatchDirtyFlags", "int32[2]"],
    ["m_ListEntry", "uint16[11]"],
    ["m_flCreateTime", "GameTime_t"],
    ["m_flSpeed", "float32"],
    ["m_EntClientFlags", "uint16"],
    ["m_bClientSideRagdoll", "bool"],
    ["m_iTeamNum", "uint8"],
    ["m_spawnflags", "uint32"],
    ["m_nNextThinkTick", "GameTick_t"],
    ["m_fFlags", "uint32"],
    ["m_vecAbsVelocity", "Vector"],
    ["m_vecVelocity", "CNetworkVelocityVector"],
    ["m_vecBaseVelocity", "Vector"],
    ["m_hEffectEntity", "CHandle< C_BaseEntity >"],
    ["m_hOwnerEntity", "CHandle< C_BaseEntity >"],
    ["m_MoveCollide", "MoveCollide_t"],
    ["m_MoveType", "MoveType_t"],
    ["m_nActualMoveType", "MoveType_t"],
    ["m_flWaterLevel", "float32"],
    ["m_fEffects", "uint32"],
    ["m_hGroundEntity", "CHandle< C_BaseEntity >"],
    ["m_nGroundBodyIndex", "int32"],
    ["m_flFriction", "float32"],
    ["m_flElasticity", "float32"],
    ["m_flGravityScale", "float32"],
    ["m_flTimeScale", "float32"],
    ["m_bAnimatedEveryTick", "bool"],
    ["m_flNavIgnoreUntilTime", "GameTime_t"],
    ["m_hThink", "uint16"],
    ["m_fBBoxVisFlags", "uint8"],
    ["m_bPredictable", "bool"],
    ["m_bRenderWithViewModels", "bool"],
    ["m_nSplitUserPlayerPredictionSlot", "CSplitScreenSlot"],
    ["m_nFirstPredictableCommand", "int32"],
    ["m_nLastPredictableCommand", "int32"],
    ["m_hOldMoveParent", "CHandle< C_BaseEntity >"],
    ["m_Particles", "CParticleProperty"],
    ["m_vecPredictedScriptFloats", "CUtlVector< float32 >"],
    ["m_vecPredictedScriptFloatIDs", "CUtlVector< int32 >"],
    ["m_nNextScriptVarRecordID", "int32"],
    ["m_vecAngVelocity", "QAngle"],
    ["m_DataChangeEventRef", "int32"],
    ["m_dependencies", "CUtlVector< CEntityHandle >"],
    ["m_nCreationTick", "int32"],
    ["m_bAnimTimeChanged", "bool"],
    ["m_bSimulationTimeChanged", "bool"],
    ["m_sUniqueHammerID", "CUtlString"],
    ["m_nBloodType", "BloodType"],
]) }}

## CEntityIdentity

{{ get_arguments_table([
    ["m_nameStringableIndex", "int32"],
    ["m_name", "CUtlSymbolLarge"],
    ["m_designerName", "CUtlSymbolLarge"],
    ["m_flags", "uint32"],
    ["m_worldGroupId", "WorldGroupId_t"],
    ["m_fDataObjectTypes", "uint32"],
    ["m_PathIndex", "ChangeAccessorFieldPathIndex_t"],
    ["m_pPrev", "CEntityIdentity*"],
    ["m_pNext", "CEntityIdentity*"],
    ["m_pPrevByClass", "CEntityIdentity*"],
    ["m_pNextByClass", "CEntityIdentity*"],
]) }}

## C_StattrakModule

{{ get_arguments_table([
    ["m_bKnife", "bool"],
]) }}

## C_PhysicsProp

{{ get_arguments_table([
    ["m_bAwake", "bool"],
]) }}

## C_BreakableProp

{{ get_arguments_table([
    ["m_CPropDataComponent", "CPropDataComponent"],
    ["m_OnBreak", "CEntityIOOutput"],
    ["m_OnHealthChanged", "CEntityOutputTemplate< float32 >"],
    ["m_OnTakeDamage", "CEntityIOOutput"],
    ["m_impactEnergyScale", "float32"],
    ["m_iMinHealthDmg", "int32"],
    ["m_flPressureDelay", "float32"],
    ["m_flDefBurstScale", "float32"],
    ["m_vDefBurstOffset", "Vector"],
    ["m_hBreaker", "CHandle< C_BaseEntity >"],
    ["m_PerformanceMode", "PerformanceMode_t"],
    ["m_flPreventDamageBeforeTime", "GameTime_t"],
    ["m_BreakableContentsType", "BreakableContentsType_t"],
    ["m_strBreakableContentsPropGroupOverride", "CUtlString"],
    ["m_strBreakableContentsParticleOverride", "CUtlString"],
    ["m_bHasBreakPiecesOrCommands", "bool"],
    ["m_explodeDamage", "float32"],
    ["m_explodeRadius", "float32"],
    ["m_explosionDelay", "float32"],
    ["m_explosionBuildupSound", "CUtlSymbolLarge"],
    ["m_explosionCustomEffect", "CUtlSymbolLarge"],
    ["m_explosionCustomSound", "CUtlSymbolLarge"],
    ["m_explosionModifier", "CUtlSymbolLarge"],
    ["m_hPhysicsAttacker", "CHandle< C_BasePlayerPawn >"],
    ["m_flLastPhysicsInfluenceTime", "GameTime_t"],
    ["m_flDefaultFadeScale", "float32"],
    ["m_hLastAttacker", "CHandle< C_BaseEntity >"],
    ["m_hFlareEnt", "CHandle< C_BaseEntity >"],
    ["m_noGhostCollision", "bool"],
]) }}

## C_Beam

{{ get_arguments_table([
    ["m_flFrameRate", "float32"],
    ["m_flHDRColorScale", "float32"],
    ["m_flFireTime", "GameTime_t"],
    ["m_flDamage", "float32"],
    ["m_nNumBeamEnts", "uint8"],
    ["m_queryHandleHalo", "int32"],
    ["m_hBaseMaterial", "CStrongHandle< InfoForResourceTypeIMaterial2 >"],
    ["m_nHaloIndex", "CStrongHandle< InfoForResourceTypeIMaterial2 >"],
    ["m_nBeamType", "BeamType_t"],
    ["m_nBeamFlags", "uint32"],
    ["m_hAttachEntity", "CHandle< C_BaseEntity >[10]"],
    ["m_nAttachIndex", "AttachmentHandle_t[10]"],
    ["m_fWidth", "float32"],
    ["m_fEndWidth", "float32"],
    ["m_fFadeLength", "float32"],
    ["m_fHaloScale", "float32"],
    ["m_fAmplitude", "float32"],
    ["m_fStartFrame", "float32"],
    ["m_fSpeed", "float32"],
    ["m_flFrame", "float32"],
    ["m_nClipStyle", "BeamClipStyle_t"],
    ["m_bTurnedOff", "bool"],
    ["m_vecEndPos", "Vector"],
    ["m_hEndEntity", "CHandle< C_BaseEntity >"],
]) }}

## C_CSGO_TeamPreviewCharacterPosition

{{ get_arguments_table([
    ["m_nVariant", "int32"],
    ["m_nRandom", "int32"],
    ["m_nOrdinal", "int32"],
    ["m_sWeaponName", "CUtlString"],
    ["m_xuid", "uint64"],
    ["m_agentItem", "C_EconItemView"],
    ["m_glovesItem", "C_EconItemView"],
    ["m_weaponItem", "C_EconItemView"],
]) }}

## C_EnvScreenOverlay

{{ get_arguments_table([
    ["m_iszOverlayNames", "CUtlSymbolLarge[10]"],
    ["m_flOverlayTimes", "float32[10]"],
    ["m_flStartTime", "GameTime_t"],
    ["m_iDesiredOverlay", "int32"],
    ["m_bIsActive", "bool"],
    ["m_bWasActive", "bool"],
    ["m_iCachedDesiredOverlay", "int32"],
    ["m_iCurrentOverlay", "int32"],
    ["m_flCurrentOverlayTime", "GameTime_t"],
]) }}

## CCSWeaponBaseVData

{{ get_arguments_table([
    ["m_WeaponType", "CSWeaponType"],
    ["m_WeaponCategory", "CSWeaponCategory"],
    ["m_szViewModel", "CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >"],
    ["m_szPlayerModel", "CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >"],
    ["m_szWorldDroppedModel", "CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >"],
    ["m_szAimsightLensMaskModel", "CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >"],
    ["m_szMagazineModel", "CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >"],
    ["m_szHeatEffect", "CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >"],
    ["m_szEjectBrassEffect", "CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >"],
    ["m_szMuzzleFlashParticleAlt", "CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >"],
    ["m_szMuzzleFlashThirdPersonParticle", "CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >"],
    ["m_szMuzzleFlashThirdPersonParticleAlt", "CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >"],
    ["m_szTracerParticle", "CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >"],
    ["m_GearSlot", "gear_slot_t"],
    ["m_GearSlotPosition", "int32"],
    ["m_DefaultLoadoutSlot", "loadout_slot_t"],
    ["m_sWrongTeamMsg", "CUtlString"],
    ["m_nPrice", "int32"],
    ["m_nKillAward", "int32"],
    ["m_nPrimaryReserveAmmoMax", "int32"],
    ["m_nSecondaryReserveAmmoMax", "int32"],
    ["m_bMeleeWeapon", "bool"],
    ["m_bHasBurstMode", "bool"],
    ["m_bIsRevolver", "bool"],
    ["m_bCannotShootUnderwater", "bool"],
    ["m_szName", "CGlobalSymbol"],
    ["m_szAnimExtension", "CUtlString"],
    ["m_eSilencerType", "CSWeaponSilencerType"],
    ["m_nCrosshairMinDistance", "int32"],
    ["m_nCrosshairDeltaDistance", "int32"],
    ["m_bIsFullAuto", "bool"],
    ["m_nNumBullets", "int32"],
    ["m_flCycleTime", "CFiringModeFloat"],
    ["m_flMaxSpeed", "CFiringModeFloat"],
    ["m_flSpread", "CFiringModeFloat"],
    ["m_flInaccuracyCrouch", "CFiringModeFloat"],
    ["m_flInaccuracyStand", "CFiringModeFloat"],
    ["m_flInaccuracyJump", "CFiringModeFloat"],
    ["m_flInaccuracyLand", "CFiringModeFloat"],
    ["m_flInaccuracyLadder", "CFiringModeFloat"],
    ["m_flInaccuracyFire", "CFiringModeFloat"],
    ["m_flInaccuracyMove", "CFiringModeFloat"],
    ["m_flRecoilAngle", "CFiringModeFloat"],
    ["m_flRecoilAngleVariance", "CFiringModeFloat"],
    ["m_flRecoilMagnitude", "CFiringModeFloat"],
    ["m_flRecoilMagnitudeVariance", "CFiringModeFloat"],
    ["m_nTracerFrequency", "CFiringModeInt"],
    ["m_flInaccuracyJumpInitial", "float32"],
    ["m_flInaccuracyJumpApex", "float32"],
    ["m_flInaccuracyReload", "float32"],
    ["m_nRecoilSeed", "int32"],
    ["m_nSpreadSeed", "int32"],
    ["m_flTimeToIdleAfterFire", "float32"],
    ["m_flIdleInterval", "float32"],
    ["m_flAttackMovespeedFactor", "float32"],
    ["m_flHeatPerShot", "float32"],
    ["m_flInaccuracyPitchShift", "float32"],
    ["m_flInaccuracyAltSoundThreshold", "float32"],
    ["m_flBotAudibleRange", "float32"],
    ["m_szUseRadioSubtitle", "CUtlString"],
    ["m_bUnzoomsAfterShot", "bool"],
    ["m_bHideViewModelWhenZoomed", "bool"],
    ["m_nZoomLevels", "int32"],
    ["m_nZoomFOV1", "int32"],
    ["m_nZoomFOV2", "int32"],
    ["m_flZoomTime0", "float32"],
    ["m_flZoomTime1", "float32"],
    ["m_flZoomTime2", "float32"],
    ["m_flIronSightPullUpSpeed", "float32"],
    ["m_flIronSightPutDownSpeed", "float32"],
    ["m_flIronSightFOV", "float32"],
    ["m_flIronSightPivotForward", "float32"],
    ["m_flIronSightLooseness", "float32"],
    ["m_angPivotAngle", "QAngle"],
    ["m_vecIronSightEyePos", "Vector"],
    ["m_nDamage", "int32"],
    ["m_flHeadshotMultiplier", "float32"],
    ["m_flArmorRatio", "float32"],
    ["m_flPenetration", "float32"],
    ["m_flRange", "float32"],
    ["m_flRangeModifier", "float32"],
    ["m_flFlinchVelocityModifierLarge", "float32"],
    ["m_flFlinchVelocityModifierSmall", "float32"],
    ["m_flRecoveryTimeCrouch", "float32"],
    ["m_flRecoveryTimeStand", "float32"],
    ["m_flRecoveryTimeCrouchFinal", "float32"],
    ["m_flRecoveryTimeStandFinal", "float32"],
    ["m_nRecoveryTransitionStartBullet", "int32"],
    ["m_nRecoveryTransitionEndBullet", "int32"],
    ["m_flThrowVelocity", "float32"],
    ["m_vSmokeColor", "Vector"],
    ["m_szAnimClass", "CGlobalSymbol"],
]) }}

## C_PointWorldText

{{ get_arguments_table([
    ["m_bForceRecreateNextUpdate", "bool"],
    ["m_messageText", "char[512]"],
    ["m_FontName", "char[64]"],
    ["m_bEnabled", "bool"],
    ["m_bFullbright", "bool"],
    ["m_flWorldUnitsPerPx", "float32"],
    ["m_flFontSize", "float32"],
    ["m_flDepthOffset", "float32"],
    ["m_Color", "Color"],
    ["m_nJustifyHorizontal", "PointWorldTextJustifyHorizontal_t"],
    ["m_nJustifyVertical", "PointWorldTextJustifyVertical_t"],
    ["m_nReorientMode", "PointWorldTextReorientMode_t"],
]) }}

## CCSPlayerController

{{ get_arguments_table([
    ["m_pInGameMoneyServices", "CCSPlayerController_InGameMoneyServices*"],
    ["m_pInventoryServices", "CCSPlayerController_InventoryServices*"],
    ["m_pActionTrackingServices", "CCSPlayerController_ActionTrackingServices*"],
    ["m_pDamageServices", "CCSPlayerController_DamageServices*"],
    ["m_iPing", "uint32"],
    ["m_bHasCommunicationAbuseMute", "bool"],
    ["m_szCrosshairCodes", "CUtlSymbolLarge"],
    ["m_iPendingTeamNum", "uint8"],
    ["m_flForceTeamTime", "GameTime_t"],
    ["m_iCompTeammateColor", "int32"],
    ["m_bEverPlayedOnTeam", "bool"],
    ["m_flPreviousForceJoinTeamTime", "GameTime_t"],
    ["m_szClan", "CUtlSymbolLarge"],
    ["m_sSanitizedPlayerName", "CUtlString"],
    ["m_iCoachingTeam", "int32"],
    ["m_nPlayerDominated", "uint64"],
    ["m_nPlayerDominatingMe", "uint64"],
    ["m_iCompetitiveRanking", "int32"],
    ["m_iCompetitiveWins", "int32"],
    ["m_iCompetitiveRankType", "int8"],
    ["m_iCompetitiveRankingPredicted_Win", "int32"],
    ["m_iCompetitiveRankingPredicted_Loss", "int32"],
    ["m_iCompetitiveRankingPredicted_Tie", "int32"],
    ["m_nEndMatchNextMapVote", "int32"],
    ["m_unActiveQuestId", "uint16"],
    ["m_nQuestProgressReason", "QuestProgress::Reason"],
    ["m_unPlayerTvControlFlags", "uint32"],
    ["m_iDraftIndex", "int32"],
    ["m_msQueuedModeDisconnectionTimestamp", "uint32"],
    ["m_uiAbandonRecordedReason", "uint32"],
    ["m_bCannotBeKicked", "bool"],
    ["m_bEverFullyConnected", "bool"],
    ["m_bAbandonAllowsSurrender", "bool"],
    ["m_bAbandonOffersInstantSurrender", "bool"],
    ["m_bDisconnection1MinWarningPrinted", "bool"],
    ["m_bScoreReported", "bool"],
    ["m_nDisconnectionTick", "int32"],
    ["m_bControllingBot", "bool"],
    ["m_bHasControlledBotThisRound", "bool"],
    ["m_bHasBeenControlledByPlayerThisRound", "bool"],
    ["m_nBotsControlledThisRound", "int32"],
    ["m_bCanControlObservedBot", "bool"],
    ["m_hPlayerPawn", "CHandle< C_CSPlayerPawn >"],
    ["m_hObserverPawn", "CHandle< C_CSObserverPawn >"],
    ["m_bPawnIsAlive", "bool"],
    ["m_iPawnHealth", "uint32"],
    ["m_iPawnArmor", "int32"],
    ["m_bPawnHasDefuser", "bool"],
    ["m_bPawnHasHelmet", "bool"],
    ["m_nPawnCharacterDefIndex", "uint16"],
    ["m_iPawnLifetimeStart", "int32"],
    ["m_iPawnLifetimeEnd", "int32"],
    ["m_iPawnBotDifficulty", "int32"],
    ["m_hOriginalControllerOfCurrentPawn", "CHandle< CCSPlayerController >"],
    ["m_iScore", "int32"],
    ["m_recentKillQueue", "uint8[8]"],
    ["m_nFirstKill", "uint8"],
    ["m_nKillCount", "uint8"],
    ["m_bMvpNoMusic", "bool"],
    ["m_eMvpReason", "int32"],
    ["m_iMusicKitID", "int32"],
    ["m_iMusicKitMVPs", "int32"],
    ["m_iMVPs", "int32"],
    ["m_bIsPlayerNameDirty", "bool"],
]) }}

## C_BasePropDoor

{{ get_arguments_table([
    ["m_eDoorState", "DoorState_t"],
    ["m_modelChanged", "bool"],
    ["m_bLocked", "bool"],
    ["m_closedPosition", "Vector"],
    ["m_closedAngles", "QAngle"],
    ["m_hMaster", "CHandle< C_BasePropDoor >"],
    ["m_vWhereToSetLightingOrigin", "Vector"],
]) }}

## C_NametagModule

{{ get_arguments_table([
    ["m_strNametagString", "CUtlString"],
]) }}

## C_PhysPropClientside

{{ get_arguments_table([
    ["m_flTouchDelta", "GameTime_t"],
    ["m_fDeathTime", "GameTime_t"],
    ["m_inertiaScale", "float32"],
    ["m_vecDamagePosition", "Vector"],
    ["m_vecDamageDirection", "Vector"],
    ["m_nDamageType", "DamageTypes_t"],
]) }}

## C_SoundAreaEntityBase

{{ get_arguments_table([
    ["m_bDisabled", "bool"],
    ["m_bWasEnabled", "bool"],
    ["m_iszSoundAreaType", "CUtlSymbolLarge"],
    ["m_vPos", "Vector"],
]) }}

## C_FogController

{{ get_arguments_table([
    ["m_fog", "fogparams_t"],
    ["m_bUseAngles", "bool"],
    ["m_iChangedVariables", "int32"],
]) }}

## CInfoWorldLayer

{{ get_arguments_table([
    ["m_pOutputOnEntitiesSpawned", "CEntityIOOutput"],
    ["m_worldName", "CUtlSymbolLarge"],
    ["m_layerName", "CUtlSymbolLarge"],
    ["m_bWorldLayerVisible", "bool"],
    ["m_bEntitiesSpawned", "bool"],
    ["m_bCreateAsChildSpawnGroup", "bool"],
    ["m_hLayerSpawnGroup", "uint32"],
    ["m_bWorldLayerActuallyVisible", "bool"],
]) }}

## C_PhysMagnet

{{ get_arguments_table([
    ["m_aAttachedObjectsFromServer", "CUtlVector< int32 >"],
    ["m_aAttachedObjects", "CUtlVector< CHandle< C_BaseEntity > >"],
]) }}

## C_FuncConveyor

{{ get_arguments_table([
    ["m_vecMoveDirEntitySpace", "Vector"],
    ["m_flTargetSpeed", "float32"],
    ["m_nTransitionStartTick", "GameTick_t"],
    ["m_nTransitionDurationTicks", "int32"],
    ["m_flTransitionStartSpeed", "float32"],
    ["m_hConveyorModels", "C_NetworkUtlVectorBase< CHandle< C_BaseEntity > >"],
    ["m_flCurrentConveyorOffset", "float32"],
    ["m_flCurrentConveyorSpeed", "float32"],
]) }}

## CEntityInstance

{{ get_arguments_table([
    ["m_iszPrivateVScripts", "CUtlSymbolLarge"],
    ["m_pEntity", "CEntityIdentity*"],
    ["m_CScriptComponent", "CScriptComponent*"],
    ["m_bVisibleinPVS", "bool"],
]) }}

## ServerAuthoritativeWeaponSlot_t

{{ get_arguments_table([
    ["unClass", "uint16"],
    ["unSlot", "uint16"],
    ["unItemDefIdx", "uint16"],
]) }}

## C_BaseViewModel

{{ get_arguments_table([
    ["m_vecLastFacing", "Vector"],
    ["m_nViewModelIndex", "uint32"],
    ["m_nAnimationParity", "uint32"],
    ["m_flAnimationStartTime", "float32"],
    ["m_hWeapon", "CHandle< C_BasePlayerWeapon >"],
    ["m_sVMName", "CUtlSymbolLarge"],
    ["m_sAnimationPrefix", "CUtlSymbolLarge"],
    ["m_iCameraAttachment", "AttachmentHandle_t"],
    ["m_vecLastCameraAngles", "QAngle"],
    ["m_previousElapsedDuration", "float32"],
    ["m_previousCycle", "float32"],
    ["m_nOldAnimationParity", "int32"],
    ["m_hOldLayerSequence", "HSequence"],
    ["m_oldLayer", "int32"],
    ["m_oldLayerStartTime", "float32"],
    ["m_hControlPanel", "CHandle< C_BaseEntity >"],
]) }}

## CGameSceneNode

{{ get_arguments_table([
    ["m_nodeToWorld", "CTransform"],
    ["m_pOwner", "CEntityInstance*"],
    ["m_pParent", "CGameSceneNode*"],
    ["m_pChild", "CGameSceneNode*"],
    ["m_pNextSibling", "CGameSceneNode*"],
    ["m_hParent", "CGameSceneNodeHandle"],
    ["m_vecOrigin", "CNetworkOriginCellCoordQuantizedVector"],
    ["m_angRotation", "QAngle"],
    ["m_flScale", "float32"],
    ["m_vecAbsOrigin", "Vector"],
    ["m_angAbsRotation", "QAngle"],
    ["m_flAbsScale", "float32"],
    ["m_nParentAttachmentOrBone", "int16"],
    ["m_bDebugAbsOriginChanges", "bool"],
    ["m_bDormant", "bool"],
    ["m_bForceParentToBeNetworked", "bool"],
    ["m_bDirtyHierarchy", "bitfield:1"],
    ["m_bDirtyBoneMergeInfo", "bitfield:1"],
    ["m_bNetworkedPositionChanged", "bitfield:1"],
    ["m_bNetworkedAnglesChanged", "bitfield:1"],
    ["m_bNetworkedScaleChanged", "bitfield:1"],
    ["m_bWillBeCallingPostDataUpdate", "bitfield:1"],
    ["m_bBoneMergeFlex", "bitfield:1"],
    ["m_nLatchAbsOrigin", "bitfield:2"],
    ["m_bDirtyBoneMergeBoneToRoot", "bitfield:1"],
    ["m_nHierarchicalDepth", "uint8"],
    ["m_nHierarchyType", "uint8"],
    ["m_nDoNotSetAnimTimeInInvalidatePhysicsCount", "uint8"],
    ["m_name", "CUtlStringToken"],
    ["m_hierarchyAttachName", "CUtlStringToken"],
    ["m_flZOffset", "float32"],
    ["m_flClientLocalScale", "float32"],
    ["m_vRenderOrigin", "Vector"],
]) }}

## CCSPointScript

{{ get_arguments_table([
    ["m_pParent", "CCSPointScriptEntity*"],
]) }}

## C_CSObserverPawn

{{ get_arguments_table([
    ["m_hDetectParentChange", "CEntityHandle"],
]) }}

## C_EntityFlame

{{ get_arguments_table([
    ["m_hEntAttached", "CHandle< C_BaseEntity >"],
    ["m_hOldAttached", "CHandle< C_BaseEntity >"],
    ["m_bCheapEffect", "bool"],
]) }}

## CCSObserver_ObserverServices

{{ get_arguments_table([
    ["m_hLastObserverTarget", "CEntityHandle"],
    ["m_vecObserverInterpolateOffset", "Vector"],
    ["m_vecObserverInterpStartPos", "Vector"],
    ["m_flObsInterp_PathLength", "float32"],
    ["m_qObsInterp_OrientationStart", "Quaternion"],
    ["m_qObsInterp_OrientationTravelDir", "Quaternion"],
    ["m_obsInterpState", "ObserverInterpState_t"],
    ["m_bObserverInterpolationNeedsDeferredSetup", "bool"],
]) }}

## C_Hostage

{{ get_arguments_table([
    ["m_entitySpottedState", "EntitySpottedState_t"],
    ["m_leader", "CHandle< C_BaseEntity >"],
    ["m_reuseTimer", "CountdownTimer"],
    ["m_vel", "Vector"],
    ["m_isRescued", "bool"],
    ["m_jumpedThisFrame", "bool"],
    ["m_nHostageState", "int32"],
    ["m_bHandsHaveBeenCut", "bool"],
    ["m_hHostageGrabber", "CHandle< C_CSPlayerPawn >"],
    ["m_fLastGrabTime", "GameTime_t"],
    ["m_vecGrabbedPos", "Vector"],
    ["m_flRescueStartTime", "GameTime_t"],
    ["m_flGrabSuccessTime", "GameTime_t"],
    ["m_flDropStartTime", "GameTime_t"],
    ["m_flDeadOrRescuedTime", "GameTime_t"],
    ["m_blinkTimer", "CountdownTimer"],
    ["m_lookAt", "Vector"],
    ["m_lookAroundTimer", "CountdownTimer"],
    ["m_isInit", "bool"],
    ["m_eyeAttachment", "AttachmentHandle_t"],
    ["m_chestAttachment", "AttachmentHandle_t"],
    ["m_pPredictionOwner", "CBasePlayerController*"],
    ["m_fNewestAlphaThinkTime", "GameTime_t"],
]) }}

## C_Sprite

{{ get_arguments_table([
    ["m_hSpriteMaterial", "CStrongHandle< InfoForResourceTypeIMaterial2 >"],
    ["m_hAttachedToEntity", "CHandle< C_BaseEntity >"],
    ["m_nAttachment", "AttachmentHandle_t"],
    ["m_flSpriteFramerate", "float32"],
    ["m_flFrame", "float32"],
    ["m_flDieTime", "GameTime_t"],
    ["m_nBrightness", "uint32"],
    ["m_flBrightnessDuration", "float32"],
    ["m_flSpriteScale", "float32"],
    ["m_flScaleDuration", "float32"],
    ["m_bWorldSpaceScale", "bool"],
    ["m_flGlowProxySize", "float32"],
    ["m_flHDRColorScale", "float32"],
    ["m_flLastTime", "GameTime_t"],
    ["m_flMaxFrame", "float32"],
    ["m_flStartScale", "float32"],
    ["m_flDestScale", "float32"],
    ["m_flScaleTimeStart", "GameTime_t"],
    ["m_nStartBrightness", "int32"],
    ["m_nDestBrightness", "int32"],
    ["m_flBrightnessTimeStart", "GameTime_t"],
    ["m_hOldSpriteMaterial", "CWeakHandle< InfoForResourceTypeIMaterial2 >"],
    ["m_nSpriteWidth", "int32"],
    ["m_nSpriteHeight", "int32"],
]) }}

## C_PlantedC4

{{ get_arguments_table([
    ["m_bBombTicking", "bool"],
    ["m_nBombSite", "int32"],
    ["m_nSourceSoundscapeHash", "int32"],
    ["m_entitySpottedState", "EntitySpottedState_t"],
    ["m_flNextGlow", "GameTime_t"],
    ["m_flNextBeep", "GameTime_t"],
    ["m_flC4Blow", "GameTime_t"],
    ["m_bCannotBeDefused", "bool"],
    ["m_bHasExploded", "bool"],
    ["m_flTimerLength", "float32"],
    ["m_bBeingDefused", "bool"],
    ["m_bTriggerWarning", "float32"],
    ["m_bExplodeWarning", "float32"],
    ["m_bC4Activated", "bool"],
    ["m_bTenSecWarning", "bool"],
    ["m_flDefuseLength", "float32"],
    ["m_flDefuseCountDown", "GameTime_t"],
    ["m_bBombDefused", "bool"],
    ["m_hBombDefuser", "CHandle< C_CSPlayerPawn >"],
    ["m_hControlPanel", "CHandle< C_BaseEntity >"],
    ["m_AttributeManager", "C_AttributeContainer"],
    ["m_hDefuserMultimeter", "CHandle< C_Multimeter >"],
    ["m_flNextRadarFlashTime", "GameTime_t"],
    ["m_bRadarFlash", "bool"],
    ["m_pBombDefuser", "CHandle< C_CSPlayerPawn >"],
    ["m_fLastDefuseTime", "GameTime_t"],
    ["m_pPredictionOwner", "CBasePlayerController*"],
    ["m_vecC4ExplodeSpectatePos", "Vector"],
    ["m_vecC4ExplodeSpectateAng", "QAngle"],
    ["m_flC4ExplodeSpectateDuration", "float32"],
]) }}

## C_RagdollProp

{{ get_arguments_table([
    ["m_ragPos", "C_NetworkUtlVectorBase< Vector >"],
    ["m_ragAngles", "C_NetworkUtlVectorBase< QAngle >"],
    ["m_flBlendWeight", "float32"],
    ["m_hRagdollSource", "CHandle< C_BaseEntity >"],
    ["m_iEyeAttachment", "AttachmentHandle_t"],
    ["m_flBlendWeightCurrent", "float32"],
    ["m_parentPhysicsBoneIndices", "CUtlVector< int32 >"],
    ["m_worldSpaceBoneComputationOrder", "CUtlVector< int32 >"],
]) }}

## C_VoteController

{{ get_arguments_table([
    ["m_iActiveIssueIndex", "int32"],
    ["m_iOnlyTeamToVote", "int32"],
    ["m_nVoteOptionCount", "int32[5]"],
    ["m_nPotentialVotes", "int32"],
    ["m_bVotesDirty", "bool"],
    ["m_bTypeDirty", "bool"],
    ["m_bIsYesNoVote", "bool"],
]) }}

## ViewAngleServerChange_t

{{ get_arguments_table([
    ["nType", "FixAngleSet_t"],
    ["qAngle", "QAngle"],
    ["nIndex", "uint32"],
]) }}

## C_Chicken

{{ get_arguments_table([
    ["m_hHolidayHatAddon", "CHandle< CBaseAnimGraph >"],
    ["m_jumpedThisFrame", "bool"],
    ["m_leader", "CHandle< C_CSPlayerPawn >"],
    ["m_AttributeManager", "C_AttributeContainer"],
    ["m_bAttributesInitialized", "bool"],
    ["m_hWaterWakeParticles", "ParticleIndex_t"],
    ["m_bIsPreviewModel", "bool"],
]) }}

## PhysicsRagdollPose_t

{{ get_arguments_table([
    ["m_Transforms", "C_NetworkUtlVectorBase< CTransform >"],
    ["m_hOwner", "CHandle< C_BaseEntity >"],
]) }}

