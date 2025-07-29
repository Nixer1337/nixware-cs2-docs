## C_CSGO_TeamIntroCharacterPosition
Derived from: [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_FireCrackerBlast
Derived from: [C_Inferno](#c_inferno), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSGO_WingmanIntroCounterTerroristPosition
Derived from: [CCSGO_WingmanIntroCharacterPosition](#ccsgo_wingmanintrocharacterposition), [C_CSGO_TeamIntroCharacterPosition](#c_csgo_teamintrocharacterposition), [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPulseCell_WaitForCursorsWithTag
Derived from: [CPulseCell_WaitForCursorsWithTagBase](#cpulsecell_waitforcursorswithtagbase), [CPulseCell_BaseYieldingInflow](#cpulsecell_baseyieldinginflow), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_bTagSelfWhenComplete | `bool`
m_nDesiredKillPriority | `PulseCursorCancelPriority_t`

---

## C_SceneEntity::QueuedEvents_t

Name | Type
------------ | -------------
starttime | `float32`

---

## CCSPlayer_PingServices


Name | Type
------------ | -------------
m_hPlayerPing | `CHandle< C_BaseEntity >`

---

## CEconItemAttribute

Name | Type
------------ | -------------
m_iAttributeDefinitionIndex | `uint16`
m_flValue | `float32`
m_flInitialValue | `float32`
m_nRefundableCurrency | `int32`
m_bSetBonus | `bool`

---

## CBaseTriggerAPI

---

## PredictedDamageTag_t

Name | Type
------------ | -------------
nTagTick | `GameTick_t`
flFlinchModSmall | `float32`
flFlinchModLarge | `float32`
flFriendlyFireDamageReductionRatio | `float32`

---

## C_EnvWindShared

Name | Type
------------ | -------------
m_flStartTime | `GameTime_t`
m_iWindSeed | `uint32`
m_iMinWind | `uint16`
m_iMaxWind | `uint16`
m_windRadius | `int32`
m_iMinGust | `uint16`
m_iMaxGust | `uint16`
m_flMinGustDelay | `float32`
m_flMaxGustDelay | `float32`
m_flGustDuration | `float32`
m_iGustDirChange | `uint16`
m_iInitialWindDir | `uint16`
m_flInitialWindSpeed | `float32`
m_location | `Vector`
m_hEntOwner | `CHandle< C_BaseEntity >`

---

## C_SkyCamera
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_skyboxData | `sky3dparams_t`
m_skyboxSlotToken | `CUtlStringToken`
m_bUseAngles | `bool`
m_pNext | `C_SkyCamera*`

---

## CPulseCell_Base

Name | Type
------------ | -------------
m_nEditorNodeID | `PulseDocNodeID_t`

---

## C_FuncRotating
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_SoundOpvarSetPointBase
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_iszStackName | `CUtlSymbolLarge`
m_iszOperatorName | `CUtlSymbolLarge`
m_iszOpvarName | `CUtlSymbolLarge`
m_iOpvarIndex | `int32`
m_bUseAutoCompare | `bool`

---

## C_EnvCubemapFog
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flEndDistance | `float32`
m_flStartDistance | `float32`
m_flFogFalloffExponent | `float32`
m_bHeightFogEnabled | `bool`
m_flFogHeightWidth | `float32`
m_flFogHeightEnd | `float32`
m_flFogHeightStart | `float32`
m_flFogHeightExponent | `float32`
m_flLODBias | `float32`
m_bActive | `bool`
m_bStartDisabled | `bool`
m_flFogMaxOpacity | `float32`
m_nCubemapSourceType | `int32`
m_hSkyMaterial | `CStrongHandle< InfoForResourceTypeIMaterial2 >`
m_iszSkyEntity | `CUtlSymbolLarge`
m_hFogCubemapTexture | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_bHasHeightFogEnd | `bool`
m_bFirstTime | `bool`

---

## C_CSGO_TeamSelectTerroristPosition
Derived from: [C_CSGO_TeamSelectCharacterPosition](#c_csgo_teamselectcharacterposition), [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BaseFlex::Emphasized_Phoneme

Name | Type
------------ | -------------
m_sClassName | `CUtlString`
m_flAmount | `float32`
m_bRequired | `bool`
m_bBasechecked | `bool`
m_bValid | `bool`

---

## C_EnvParticleGlow
Derived from: [C_ParticleSystem](#c_particlesystem), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flAlphaScale | `float32`
m_flRadiusScale | `float32`
m_flSelfIllumScale | `float32`
m_ColorTint | `Color`
m_hTextureOverride | `CStrongHandle< InfoForResourceTypeCTextureBase >`

---

## CCS_PortraitWorldCallbackHandler
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPlayerController_InventoryServices


Name | Type
------------ | -------------
m_unMusicID | `uint16`
m_rank | `MedalRank_t[6]`
m_nPersonaDataPublicLevel | `int32`
m_nPersonaDataPublicCommendsLeader | `int32`
m_nPersonaDataPublicCommendsTeacher | `int32`
m_nPersonaDataPublicCommendsFriendly | `int32`
m_nPersonaDataXpTrailLevel | `int32`
m_vecServerAuthoritativeWeaponSlots | `C_UtlVectorEmbeddedNetworkVar< ServerAuthoritativeWeaponSlot_t >`

---

## C_EconEntity::AttachedModelData_t

Name | Type
------------ | -------------
m_iModelDisplayFlags | `int32`

---

## CPulse_ResumePoint
Derived from: [CPulse_OutflowConnection](#cpulse_outflowconnection)

---

## CTriggerFan
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_vFanOrigin | `Vector`
m_vFanOriginOffset | `Vector`
m_vFanEnd | `Vector`
m_vNoiseDirectionTarget | `Vector`
m_vDirection | `Vector`
m_bPushTowardsInfoTarget | `bool`
m_bPushAwayFromInfoTarget | `bool`
m_qNoiseDelta | `Quaternion`
m_hInfoFan | `CHandle< CInfoFan >`
m_flForce | `float32`
m_bFalloff | `bool`
m_RampTimer | `CountdownTimer`

---

## C_HostageCarriableProp
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BulletHitModel
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_matLocal | `matrix3x4_t`
m_iBoneIndex | `int32`
m_hPlayerParent | `CHandle< C_BaseEntity >`
m_bIsHit | `bool`
m_flTimeCreated | `float32`
m_vecStartPos | `Vector`

---

## C_FuncElectrifiedVolume
Derived from: [C_FuncBrush](#c_funcbrush), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_nAmbientEffect | `ParticleIndex_t`
m_EffectName | `CUtlSymbolLarge`
m_bState | `bool`

---

## C_MapVetoPickController
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_nDraftType | `int32`
m_nTeamWinningCoinToss | `int32`
m_nTeamWithFirstChoice | `int32[64]`
m_nVoteMapIdsList | `int32[7]`
m_nAccountIDs | `int32[64]`
m_nMapId0 | `int32[64]`
m_nMapId1 | `int32[64]`
m_nMapId2 | `int32[64]`
m_nMapId3 | `int32[64]`
m_nMapId4 | `int32[64]`
m_nMapId5 | `int32[64]`
m_nStartingSide0 | `int32[64]`
m_nCurrentPhase | `int32`
m_nPhaseStartTick | `int32`
m_nPhaseDurationTicks | `int32`
m_nPostDataUpdateTick | `int32`
m_bDisabledHud | `bool`

---

## C_EnvVolumetricFogVolume
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bActive | `bool`
m_vBoxMins | `Vector`
m_vBoxMaxs | `Vector`
m_bStartDisabled | `bool`
m_bIndirectUseLPVs | `bool`
m_flStrength | `float32`
m_nFalloffShape | `int32`
m_flFalloffExponent | `float32`
m_flHeightFogDepth | `float32`
m_fHeightFogEdgeWidth | `float32`
m_fIndirectLightStrength | `float32`
m_fSunLightStrength | `float32`
m_fNoiseStrength | `float32`
m_TintColor | `Color`
m_bOverrideTintColor | `bool`
m_bOverrideIndirectLightStrength | `bool`
m_bOverrideSunLightStrength | `bool`
m_bOverrideNoiseStrength | `bool`

---

## C_CSGO_EndOfMatchCharacterPosition
Derived from: [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPulseCell_PlaySequence
Derived from: [CPulseCell_BaseYieldingInflow](#cpulsecell_baseyieldinginflow), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_SequenceName | `CUtlString`
m_PulseAnimEvents | `PulseNodeDynamicOutflows_t`
m_OnFinished | `CPulse_ResumePoint`
m_OnCanceled | `CPulse_ResumePoint`

---

## C_BaseEntityAPI

---

## C_BarnLight
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bEnabled | `bool`
m_nColorMode | `int32`
m_Color | `Color`
m_flColorTemperature | `float32`
m_flBrightness | `float32`
m_flBrightnessScale | `float32`
m_nDirectLight | `int32`
m_nBakedShadowIndex | `int32`
m_nLightPathUniqueId | `int32`
m_nLightMapUniqueId | `int32`
m_nLuminaireShape | `int32`
m_flLuminaireSize | `float32`
m_flLuminaireAnisotropy | `float32`
m_LightStyleString | `CUtlString`
m_flLightStyleStartTime | `GameTime_t`
m_QueuedLightStyleStrings | `C_NetworkUtlVectorBase< CUtlString >`
m_LightStyleEvents | `C_NetworkUtlVectorBase< CUtlString >`
m_LightStyleTargets | `C_NetworkUtlVectorBase< CHandle< C_BaseModelEntity > >`
m_StyleEvent | `CEntityIOOutput[4]`
m_hLightCookie | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_flShape | `float32`
m_flSoftX | `float32`
m_flSoftY | `float32`
m_flSkirt | `float32`
m_flSkirtNear | `float32`
m_vSizeParams | `Vector`
m_flRange | `float32`
m_vShear | `Vector`
m_nBakeSpecularToCubemaps | `int32`
m_vBakeSpecularToCubemapsSize | `Vector`
m_nCastShadows | `int32`
m_nShadowMapSize | `int32`
m_nShadowPriority | `int32`
m_bContactShadow | `bool`
m_bForceShadowsEnabled | `bool`
m_nBounceLight | `int32`
m_flBounceScale | `float32`
m_flMinRoughness | `float32`
m_vAlternateColor | `Vector`
m_fAlternateColorBrightness | `float32`
m_nFog | `int32`
m_flFogStrength | `float32`
m_nFogShadows | `int32`
m_flFogScale | `float32`
m_bFogMixedShadows | `bool`
m_flFadeSizeStart | `float32`
m_flFadeSizeEnd | `float32`
m_flShadowFadeSizeStart | `float32`
m_flShadowFadeSizeEnd | `float32`
m_bPrecomputedFieldsValid | `bool`
m_vPrecomputedBoundsMins | `Vector`
m_vPrecomputedBoundsMaxs | `Vector`
m_vPrecomputedOBBOrigin | `Vector`
m_vPrecomputedOBBAngles | `QAngle`
m_vPrecomputedOBBExtent | `Vector`
m_nPrecomputedSubFrusta | `int32`
m_vPrecomputedOBBOrigin0 | `Vector`
m_vPrecomputedOBBAngles0 | `QAngle`
m_vPrecomputedOBBExtent0 | `Vector`
m_vPrecomputedOBBOrigin1 | `Vector`
m_vPrecomputedOBBAngles1 | `QAngle`
m_vPrecomputedOBBExtent1 | `Vector`
m_vPrecomputedOBBOrigin2 | `Vector`
m_vPrecomputedOBBAngles2 | `QAngle`
m_vPrecomputedOBBExtent2 | `Vector`
m_vPrecomputedOBBOrigin3 | `Vector`
m_vPrecomputedOBBAngles3 | `QAngle`
m_vPrecomputedOBBExtent3 | `Vector`
m_vPrecomputedOBBOrigin4 | `Vector`
m_vPrecomputedOBBAngles4 | `QAngle`
m_vPrecomputedOBBExtent4 | `Vector`
m_vPrecomputedOBBOrigin5 | `Vector`
m_vPrecomputedOBBAngles5 | `QAngle`
m_vPrecomputedOBBExtent5 | `Vector`
m_bInitialBoneSetup | `bool`
m_VisClusters | `C_NetworkUtlVectorBase< uint16 >`

---

## CPulseCell_LerpCameraSettings
Derived from: [CPulseCell_BaseLerp](#cpulsecell_baselerp), [CPulseCell_BaseYieldingInflow](#cpulsecell_baseyieldinginflow), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_flSeconds | `float32`
m_Start | `PointCameraSettings_t`
m_End | `PointCameraSettings_t`

---

## CPointOffScreenIndicatorUi
Derived from: [C_PointClientUIWorldPanel](#c_pointclientuiworldpanel), [C_BaseClientUIEntity](#c_baseclientuientity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bBeenEnabled | `bool`
m_bHide | `bool`
m_flSeenTargetTime | `float32`
m_pTargetPanel | `C_PointClientUIWorldPanel*`

---

## CCSObserver_UseServices
Derived from: [CPlayer_UseServices](#cplayer_useservices)

---

## C_PostProcessingVolume
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_hPostSettings | `CStrongHandle< InfoForResourceTypeCPostProcessingResource >`
m_flFadeDuration | `float32`
m_flMinLogExposure | `float32`
m_flMaxLogExposure | `float32`
m_flMinExposure | `float32`
m_flMaxExposure | `float32`
m_flExposureCompensation | `float32`
m_flExposureFadeSpeedUp | `float32`
m_flExposureFadeSpeedDown | `float32`
m_flTonemapEVSmoothingRange | `float32`
m_bMaster | `bool`
m_bExposureControl | `bool`

---

## CCSPlayer_UseServices
Derived from: [CPlayer_UseServices](#cplayer_useservices)

---

## C_CSGO_CounterTerroristWingmanIntroCamera
Derived from: [C_CSGO_TeamPreviewCamera](#c_csgo_teampreviewcamera), [C_CSGO_MapPreviewCameraPath](#c_csgo_mappreviewcamerapath), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPulseCell_PickBestOutflowSelector
Derived from: [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_nCheckType | `PulseBestOutflowRules_t`
m_OutflowList | `PulseSelectorOutflowList_t`

---

## CInfoFan
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_fFanForceMaxRadius | `float32`
m_fFanForceMinRadius | `float32`
m_flCurveDistRange | `float32`
m_FanForceCurveString | `CUtlSymbolLarge`

---

## C_VoteController
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_iActiveIssueIndex | `int32`
m_iOnlyTeamToVote | `int32`
m_nVoteOptionCount | `int32[5]`
m_nPotentialVotes | `int32`
m_bVotesDirty | `bool`
m_bTypeDirty | `bool`
m_bIsYesNoVote | `bool`

---

## C_CSPlayerPawnBase
Derived from: [C_BasePlayerPawn](#c_baseplayerpawn), [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_pPingServices | `CCSPlayer_PingServices*`
m_fRenderingClipPlane | `float32[4]`
m_nLastClipPlaneSetupFrame | `int32`
m_vecLastClipCameraPos | `Vector`
m_vecLastClipCameraForward | `Vector`
m_bClipHitStaticWorld | `bool`
m_bCachedPlaneIsValid | `bool`
m_pClippingWeapon | `C_CSWeaponBase*`
m_previousPlayerState | `CSPlayerState`
m_iPlayerState | `CSPlayerState`
m_bIsRescuing | `bool`
m_bHasMovedSinceSpawn | `bool`
m_fMolotovUseTime | `float32`
m_iThrowGrenadeCounter | `int32`
m_flLastSpawnTimeIndex | `GameTime_t`
m_iProgressBarDuration | `int32`
m_flProgressBarStartTime | `float32`
m_vecIntroStartEyePosition | `Vector`
m_vecIntroStartPlayerForward | `Vector`
m_flClientDeathTime | `GameTime_t`
m_bScreenTearFrameCaptured | `bool`
m_flFlashBangTime | `float32`
m_flFlashScreenshotAlpha | `float32`
m_flFlashOverlayAlpha | `float32`
m_bFlashBuildUp | `bool`
m_bFlashDspHasBeenCleared | `bool`
m_bFlashScreenshotHasBeenGrabbed | `bool`
m_flFlashMaxAlpha | `float32`
m_flFlashDuration | `float32`
m_flClientHealthFadeChangeTimestamp | `GameTime_t`
m_nClientHealthFadeParityValue | `int32`
m_flDeathCCWeight | `float32`
m_flPrevRoundEndTime | `float32`
m_flPrevMatchEndTime | `float32`
m_angEyeAngles | `QAngle`
m_fNextThinkPushAway | `float32`
m_iIDEntIndex | `CEntityIndex`
m_delayTargetIDTimer | `CountdownTimer`
m_iTargetItemEntIdx | `CEntityIndex`
m_iOldIDEntIndex | `CEntityIndex`
m_holdTargetIDTimer | `CountdownTimer`
m_flCurrentMusicStartTime | `float32`
m_flMusicRoundStartTime | `float32`
m_bDeferStartMusicOnWarmup | `bool`
m_cycleLatch | `int32`
m_serverIntendedCycle | `float32`
m_flLastSmokeOverlayAlpha | `float32`
m_flLastSmokeAge | `float32`
m_vLastSmokeOverlayColor | `Vector`
m_nPlayerInfernoBodyFx | `ParticleIndex_t`
m_nPlayerInfernoFootFx | `ParticleIndex_t`
m_flNextMagDropTime | `float32`
m_nLastMagDropAttachmentIndex | `int32`
m_vecLastAliveLocalVelocity | `Vector`
m_bGuardianShouldSprayCustomXMark | `bool`
m_hOriginalController | `CHandle< CCSPlayerController >`

---

## C_C4
Derived from: [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_activeLightParticleIndex | `ParticleIndex_t`
m_eActiveLightEffect | `C4LightEffect_t`
m_bStartedArming | `bool`
m_fArmedTime | `GameTime_t`
m_bBombPlacedAnimation | `bool`
m_bIsPlantingViaUse | `bool`
m_entitySpottedState | `EntitySpottedState_t`
m_nSpotRules | `int32`
m_bPlayedArmingBeeps | `bool[7]`
m_bBombPlanted | `bool`

---

## CCSClientPointScriptEntity
Derived from: [CCSPointScriptEntity](#ccspointscriptentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BreakableProp
Derived from: [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_CPropDataComponent | `CPropDataComponent`
m_OnStartDeath | `CEntityIOOutput`
m_OnBreak | `CEntityIOOutput`
m_OnHealthChanged | `CEntityOutputTemplate< float32 >`
m_OnTakeDamage | `CEntityIOOutput`
m_impactEnergyScale | `float32`
m_iMinHealthDmg | `int32`
m_flPressureDelay | `float32`
m_flDefBurstScale | `float32`
m_vDefBurstOffset | `Vector`
m_hBreaker | `CHandle< C_BaseEntity >`
m_PerformanceMode | `PerformanceMode_t`
m_flPreventDamageBeforeTime | `GameTime_t`
m_BreakableContentsType | `BreakableContentsType_t`
m_strBreakableContentsPropGroupOverride | `CUtlString`
m_strBreakableContentsParticleOverride | `CUtlString`
m_bHasBreakPiecesOrCommands | `bool`
m_explodeDamage | `float32`
m_explodeRadius | `float32`
m_explosionDelay | `float32`
m_explosionBuildupSound | `CUtlSymbolLarge`
m_explosionCustomEffect | `CUtlSymbolLarge`
m_explosionCustomSound | `CUtlSymbolLarge`
m_explosionModifier | `CUtlSymbolLarge`
m_hPhysicsAttacker | `CHandle< C_BasePlayerPawn >`
m_flLastPhysicsInfluenceTime | `GameTime_t`
m_flDefaultFadeScale | `float32`
m_hLastAttacker | `CHandle< C_BaseEntity >`

---

## CCSGO_WingmanIntroTerroristPosition
Derived from: [CCSGO_WingmanIntroCharacterPosition](#ccsgo_wingmanintrocharacterposition), [C_CSGO_TeamIntroCharacterPosition](#c_csgo_teamintrocharacterposition), [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPrecipitationVData


Name | Type
------------ | -------------
m_szParticlePrecipitationEffect | `CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >`
m_flInnerDistance | `float32`
m_nAttachType | `ParticleAttachment_t`
m_bBatchSameVolumeType | `bool`
m_nRTEnvCP | `int32`
m_nRTEnvCPComponent | `int32`
m_szModifier | `CUtlString`

---

## C_RetakeGameRules

Name | Type
------------ | -------------
m_nMatchSeed | `int32`
m_bBlockersPresent | `bool`
m_bRoundInProgress | `bool`
m_iFirstSecondHalfRound | `int32`
m_iBombSite | `int32`

---

## C_SoundAreaEntitySphere
Derived from: [C_SoundAreaEntityBase](#c_soundareaentitybase), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flRadius | `float32`

---

## CPulseCell_Step_EntFire
Derived from: [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_Input | `CUtlString`

---

## C_WeaponAWP
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BaseButton
Derived from: [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_glowEntity | `CHandle< C_BaseModelEntity >`
m_usable | `bool`
m_szDisplayText | `CUtlSymbolLarge`

---

## CCSObserver_ObserverServices
Derived from: [CPlayer_ObserverServices](#cplayer_observerservices)

Name | Type
------------ | -------------
m_hLastObserverTarget | `CEntityHandle`
m_vecObserverInterpolateOffset | `Vector`
m_vecObserverInterpStartPos | `Vector`
m_flObsInterp_PathLength | `float32`
m_qObsInterp_OrientationStart | `Quaternion`
m_qObsInterp_OrientationTravelDir | `Quaternion`
m_obsInterpState | `ObserverInterpState_t`
m_bObserverInterpolationNeedsDeferredSetup | `bool`

---

## CHitboxComponent
Derived from: [CEntityComponent](#centitycomponent)

Name | Type
------------ | -------------
m_bvDisabledHitGroups | `uint32[1]`

---

## C_CSMinimapBoundary
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPathQueryComponent
Derived from: [CEntityComponent](#centitycomponent)

---

## C_Precipitation
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flDensity | `float32`
m_flParticleInnerDist | `float32`
m_pParticleDef | `char*`
m_tParticlePrecipTraceTimer | `TimedEvent[1]`
m_bActiveParticlePrecipEmitter | `bool[1]`
m_bParticlePrecipInitialized | `bool`
m_bHasSimulatedSinceLastSceneObjectUpdate | `bool`
m_nAvailableSheetSequencesMaxIndex | `int32`

---

## CLogicRelay
Derived from: [CLogicalEntity](#clogicalentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bDisabled | `bool`
m_bWaitForRefire | `bool`
m_bTriggerOnce | `bool`
m_bFastRetrigger | `bool`
m_bPassthoughCaller | `bool`

---

## SequenceHistory_t

Name | Type
------------ | -------------
m_hSequence | `HSequence`
m_flSeqStartTime | `GameTime_t`
m_flSeqFixedCycle | `float32`
m_nSeqLoopMode | `AnimLoopMode_t`
m_flPlaybackRate | `float32`
m_flCyclesPerSecond | `float32`

---

## CPlayer_ItemServices


---

## CPulse_OutflowConnection

Name | Type
------------ | -------------
m_SourceOutflowName | `PulseSymbol_t`
m_nDestChunk | `PulseRuntimeChunkIndex_t`
m_nInstruction | `int32`
m_OutflowRegisterMap | `PulseRegisterMap_t`

---

## C_WeaponUMP45
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WeaponG3SG1
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_SpotlightEnd
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flLightScale | `float32`
m_Radius | `float32`

---

## C_Fish
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_pos | `Vector`
m_vel | `Vector`
m_angles | `QAngle`
m_localLifeState | `int32`
m_deathDepth | `float32`
m_deathAngle | `float32`
m_buoyancy | `float32`
m_wiggleTimer | `CountdownTimer`
m_wigglePhase | `float32`
m_wiggleRate | `float32`
m_actualPos | `Vector`
m_actualAngles | `QAngle`
m_poolOrigin | `Vector`
m_waterLevel | `float32`
m_gotUpdate | `bool`
m_x | `float32`
m_y | `float32`
m_z | `float32`
m_angle | `float32`
m_errorHistory | `float32[20]`
m_errorHistoryIndex | `int32`
m_errorHistoryCount | `int32`
m_averageError | `float32`

---

## C_WeaponFamas
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EnvVolumetricFogController
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flScattering | `float32`
m_TintColor | `Color`
m_flAnisotropy | `float32`
m_flFadeSpeed | `float32`
m_flDrawDistance | `float32`
m_flFadeInStart | `float32`
m_flFadeInEnd | `float32`
m_flIndirectStrength | `float32`
m_nVolumeDepth | `int32`
m_fFirstVolumeSliceThickness | `float32`
m_nIndirectTextureDimX | `int32`
m_nIndirectTextureDimY | `int32`
m_nIndirectTextureDimZ | `int32`
m_vBoxMins | `Vector`
m_vBoxMaxs | `Vector`
m_bActive | `bool`
m_flStartAnisoTime | `GameTime_t`
m_flStartScatterTime | `GameTime_t`
m_flStartDrawDistanceTime | `GameTime_t`
m_flStartAnisotropy | `float32`
m_flStartScattering | `float32`
m_flStartDrawDistance | `float32`
m_flDefaultAnisotropy | `float32`
m_flDefaultScattering | `float32`
m_flDefaultDrawDistance | `float32`
m_bStartDisabled | `bool`
m_bEnableIndirect | `bool`
m_bIsMaster | `bool`
m_hFogIndirectTexture | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_nForceRefreshCount | `int32`
m_fNoiseSpeed | `float32`
m_fNoiseStrength | `float32`
m_vNoiseScale | `Vector`
m_fWindSpeed | `float32`
m_vWindDirection | `Vector`
m_bFirstTime | `bool`

---

## CPulseGraphDef

Name | Type
------------ | -------------
m_DomainIdentifier | `PulseSymbol_t`
m_DomainSubType | `CPulseValueFullType`
m_ParentMapName | `PulseSymbol_t`
m_ParentXmlName | `PulseSymbol_t`
m_Chunks | `CUtlVector< CPulse_Chunk* >`
m_Cells | `CUtlVector< CPulseCell_Base* >`
m_Vars | `CUtlVector< CPulse_Variable >`
m_PublicOutputs | `CUtlVector< CPulse_PublicOutput >`
m_InvokeBindings | `CUtlVector< CPulse_InvokeBinding* >`
m_CallInfos | `CUtlVector< CPulse_CallInfo* >`
m_Constants | `CUtlVector< CPulse_Constant >`
m_DomainValues | `CUtlVector< CPulse_DomainValue >`
m_BlackboardReferences | `CUtlVector< CPulse_BlackboardReference >`
m_OutputConnections | `CUtlVector< CPulse_OutputConnection* >`

---

## C_EnvDetailController
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flFadeStartDist | `float32`
m_flFadeEndDist | `float32`

---

## C_EnvWindVolume
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bActive | `bool`
m_vBoxMins | `Vector`
m_vBoxMaxs | `Vector`
m_bStartDisabled | `bool`
m_nShape | `int32`
m_fWindSpeedMultiplier | `float32`
m_fWindTurbulenceMultiplier | `float32`
m_fWindSpeedVariationMultiplier | `float32`
m_fWindDirectionVariationMultiplier | `float32`

---

## CBasePlayerControllerAPI

---

## CHostageRescueZoneShim
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CEnvSoundscapeAlias_snd_soundscape
Derived from: [CEnvSoundscape](#cenvsoundscape), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPlayer_HostageServices


Name | Type
------------ | -------------
m_hCarriedHostage | `CHandle< C_BaseEntity >`
m_hCarriedHostageProp | `CHandle< C_BaseEntity >`

---

## C_GameRulesProxy
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CRenderComponent
Derived from: [CEntityComponent](#centitycomponent)

Name | Type
------------ | -------------
__m_pChainEntity | `CNetworkVarChainer`
m_bIsRenderingWithViewModels | `bool`
m_nSplitscreenFlags | `uint32`
m_bEnableRendering | `bool`
m_bInterpolationReadyToDraw | `bool`

---

## C_Team
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_aPlayerControllers | `C_NetworkUtlVectorBase< CHandle< CBasePlayerController > >`
m_aPlayers | `C_NetworkUtlVectorBase< CHandle< C_BasePlayerPawn > >`
m_iScore | `int32`
m_szTeamname | `char[129]`

---

## C_PathParticleRopeAlias_path_particle_rope_clientside
Derived from: [C_PathParticleRope](#c_pathparticlerope), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPointChildModifier
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bOrphanInsteadOfDeletingChildrenOnRemove | `bool`

---

## C_WeaponNOVA
Derived from: [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_DEagle
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CS2HudModelAddon
Derived from: [C_LateUpdatedAnimating](#c_lateupdatedanimating), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_TriggerMultiple
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_TeamPreviewCamera
Derived from: [C_CSGO_MapPreviewCameraPath](#c_csgo_mappreviewcamerapath), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_nVariant | `int32`

---

## C_TeamRoundTimer
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bTimerPaused | `bool`
m_flTimeRemaining | `float32`
m_flTimerEndTime | `GameTime_t`
m_bIsDisabled | `bool`
m_bShowInHUD | `bool`
m_nTimerLength | `int32`
m_nTimerInitialLength | `int32`
m_nTimerMaxLength | `int32`
m_bAutoCountdown | `bool`
m_nSetupTimeLength | `int32`
m_nState | `int32`
m_bStartPaused | `bool`
m_bInCaptureWatchState | `bool`
m_flTotalTime | `float32`
m_bStopWatchTimer | `bool`
m_bFireFinished | `bool`
m_bFire5MinRemain | `bool`
m_bFire4MinRemain | `bool`
m_bFire3MinRemain | `bool`
m_bFire2MinRemain | `bool`
m_bFire1MinRemain | `bool`
m_bFire30SecRemain | `bool`
m_bFire10SecRemain | `bool`
m_bFire5SecRemain | `bool`
m_bFire4SecRemain | `bool`
m_bFire3SecRemain | `bool`
m_bFire2SecRemain | `bool`
m_bFire1SecRemain | `bool`
m_nOldTimerLength | `int32`
m_nOldTimerState | `int32`

---

## C_ColorCorrectionVolume
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_LastEnterWeight | `float32`
m_LastEnterTime | `GameTime_t`
m_LastExitWeight | `float32`
m_LastExitTime | `GameTime_t`
m_bEnabled | `bool`
m_MaxWeight | `float32`
m_FadeDuration | `float32`
m_Weight | `float32`
m_lookupFilename | `char[512]`

---

## CPlayer_MovementServices


Name | Type
------------ | -------------
m_nImpulse | `int32`
m_nButtons | `CInButtonState`
m_nQueuedButtonDownMask | `uint64`
m_nQueuedButtonChangeMask | `uint64`
m_nButtonDoublePressed | `uint64`
m_pButtonPressedCmdNumber | `uint32[64]`
m_nLastCommandNumberProcessed | `uint32`
m_nToggleButtonDownMask | `uint64`
m_flMaxspeed | `float32`
m_arrForceSubtickMoveWhen | `float32[4]`
m_flForwardMove | `float32`
m_flLeftMove | `float32`
m_flUpMove | `float32`
m_vecLastMovementImpulses | `Vector`
m_vecLastFinishTickViewAngles | `QAngle`
m_vecOldViewAngles | `QAngle`

---

## CInfoDynamicShadowHintBox
Derived from: [CInfoDynamicShadowHint](#cinfodynamicshadowhint), [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_vBoxMins | `Vector`
m_vBoxMaxs | `Vector`

---

## CBaseAnimGraphController


Name | Type
------------ | -------------
m_animGraphNetworkedVars | `CAnimGraphNetworkedVariables`
m_bSequenceFinished | `bool`
m_flSoundSyncTime | `float32`
m_nActiveIKChainMask | `uint32`
m_hSequence | `HSequence`
m_flSeqStartTime | `GameTime_t`
m_flSeqFixedCycle | `float32`
m_nAnimLoopMode | `AnimLoopMode_t`
m_flPlaybackRate | `CNetworkedQuantizedFloat`
m_nNotifyState | `SequenceFinishNotifyState_t`
m_bNetworkedAnimationInputsChanged | `bool`
m_bNetworkedSequenceChanged | `bool`
m_bLastUpdateSkipped | `bool`
m_flPrevAnimUpdateTime | `GameTime_t`
m_hGraphDefinitionAG2 | `CStrongHandle< InfoForResourceTypeCNmGraphDefinition >`
m_bIsUsingAG2 | `bool`
m_serializedPoseRecipeAG2 | `C_NetworkUtlVectorBase< uint8 >`
m_nSerializePoseRecipeSizeAG2 | `int32`
m_nGraphCreationFlagsAG2 | `uint8`
m_nServerGraphDefReloadCountAG2 | `int32`

---

## C_ColorCorrection
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_vecOrigin | `Vector`
m_MinFalloff | `float32`
m_MaxFalloff | `float32`
m_flFadeInDuration | `float32`
m_flFadeOutDuration | `float32`
m_flMaxWeight | `float32`
m_flCurWeight | `float32`
m_netlookupFilename | `char[512]`
m_bEnabled | `bool`
m_bMaster | `bool`
m_bClientSide | `bool`
m_bExclusive | `bool`
m_bEnabledOnClient | `bool[1]`
m_flCurWeightOnClient | `float32[1]`
m_bFadingIn | `bool[1]`
m_flFadeStartWeight | `float32[1]`
m_flFadeStartTime | `float32[1]`
m_flFadeDuration | `float32[1]`

---

## CBuoyancyHelper

Name | Type
------------ | -------------
m_nFluidType | `CUtlStringToken`
m_flFluidDensity | `float32`
m_flNeutrallyBuoyantGravity | `float32`
m_flNeutrallyBuoyantLinearDamping | `float32`
m_flNeutrallyBuoyantAngularDamping | `float32`
m_bNeutrallyBuoyant | `bool`
m_vecFractionOfWheelSubmergedForWheelFriction | `CUtlVector< float32 >`
m_vecWheelFrictionScales | `CUtlVector< float32 >`
m_vecFractionOfWheelSubmergedForWheelDrag | `CUtlVector< float32 >`
m_vecWheelDrag | `CUtlVector< float32 >`

---

## C_PhysBox
Derived from: [C_Breakable](#c_breakable), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPlayer_CameraServices
Derived from: [CCSPlayerBase_CameraServices](#ccsplayerbase_cameraservices), [CPlayer_CameraServices](#cplayer_cameraservices)

Name | Type
------------ | -------------
m_flDeathCamTilt | `float32`
m_vClientScopeInaccuracy | `Vector`

---

## CProjectedTextureBase

Name | Type
------------ | -------------
m_hTargetEntity | `CHandle< C_BaseEntity >`
m_bState | `bool`
m_bAlwaysUpdate | `bool`
m_flLightFOV | `float32`
m_bEnableShadows | `bool`
m_bSimpleProjection | `bool`
m_bLightOnlyTarget | `bool`
m_bLightWorld | `bool`
m_bCameraSpace | `bool`
m_flBrightnessScale | `float32`
m_LightColor | `Color`
m_flIntensity | `float32`
m_flLinearAttenuation | `float32`
m_flQuadraticAttenuation | `float32`
m_bVolumetric | `bool`
m_flVolumetricIntensity | `float32`
m_flNoiseStrength | `float32`
m_flFlashlightTime | `float32`
m_nNumPlanes | `uint32`
m_flPlaneOffset | `float32`
m_flColorTransitionTime | `float32`
m_flAmbient | `float32`
m_SpotlightTextureName | `char[512]`
m_nSpotlightTextureFrame | `int32`
m_nShadowQuality | `uint32`
m_flNearZ | `float32`
m_flFarZ | `float32`
m_flProjectionSize | `float32`
m_flRotation | `float32`
m_bFlipHorizontal | `bool`

---

## CFilterMultiple
Derived from: [CBaseFilter](#cbasefilter), [CLogicalEntity](#clogicalentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_nFilterType | `filter_t`
m_iFilterName | `CUtlSymbolLarge[10]`
m_hFilter | `CHandle< C_BaseEntity >[10]`

---

## CPulseCell_FireCursors
Derived from: [CPulseCell_BaseYieldingInflow](#cpulsecell_baseyieldinginflow), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_Outflows | `CUtlVector< CPulse_OutflowConnection >`
m_bWaitForChildOutflows | `bool`
m_OnFinished | `CPulse_ResumePoint`
m_OnCanceled | `CPulse_ResumePoint`

---

## CEnvSoundscape
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_OnPlay | `CEntityIOOutput`
m_flRadius | `float32`
m_soundEventName | `CUtlSymbolLarge`
m_bOverrideWithEvent | `bool`
m_soundscapeIndex | `int32`
m_soundscapeEntityListId | `int32`
m_positionNames | `CUtlSymbolLarge[8]`
m_hProxySoundscape | `CHandle< CEnvSoundscape >`
m_bDisabled | `bool`
m_soundscapeName | `CUtlSymbolLarge`
m_soundEventHash | `uint32`

---

## C_SoundEventEntityAlias_snd_event_point
Derived from: [C_SoundEventEntity](#c_soundevententity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_FogController
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_fog | `fogparams_t`
m_bUseAngles | `bool`
m_iChangedVariables | `int32`

---

## C_SoundOpvarSetOBBWindEntity
Derived from: [C_SoundOpvarSetPointBase](#c_soundopvarsetpointbase), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_MolotovGrenade
Derived from: [C_BaseCSGrenade](#c_basecsgrenade), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_NetTestBaseCombatCharacter
Derived from: [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CBodyComponentPoint
Derived from: [CBodyComponent](#cbodycomponent), [CEntityComponent](#centitycomponent)

Name | Type
------------ | -------------
m_sceneNode | `CGameSceneNode`

---

## C_WeaponM4A1Silencer
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EconItemView


Name | Type
------------ | -------------
m_bInventoryImageRgbaRequested | `bool`
m_bInventoryImageTriedCache | `bool`
m_nInventoryImageRgbaWidth | `int32`
m_nInventoryImageRgbaHeight | `int32`
m_szCurrentLoadCachedFileName | `char[260]`
m_bRestoreCustomMaterialAfterPrecache | `bool`
m_iItemDefinitionIndex | `uint16`
m_iEntityQuality | `int32`
m_iEntityLevel | `uint32`
m_iItemID | `uint64`
m_iItemIDHigh | `uint32`
m_iItemIDLow | `uint32`
m_iAccountID | `uint32`
m_iInventoryPosition | `uint32`
m_bInitialized | `bool`
m_bDisallowSOC | `bool`
m_bIsStoreItem | `bool`
m_bIsTradeItem | `bool`
m_iEntityQuantity | `int32`
m_iRarityOverride | `int32`
m_iQualityOverride | `int32`
m_iOriginOverride | `int32`
m_ubStyleOverride | `uint8`
m_unClientFlags | `uint8`
m_AttributeList | `CAttributeList`
m_NetworkedDynamicAttributes | `CAttributeList`
m_szCustomName | `char[161]`
m_szCustomNameOverride | `char[161]`
m_bInitializedTags | `bool`

---

## CPulseCell_Timeline::TimelineEvent_t

Name | Type
------------ | -------------
m_flTimeFromPrevious | `float32`
m_EventOutflow | `CPulse_OutflowConnection`

---

## CPulseCell_IntervalTimer::CursorState_t

Name | Type
------------ | -------------
m_StartTime | `GameTime_t`
m_EndTime | `GameTime_t`
m_flWaitInterval | `float32`
m_flWaitIntervalHigh | `float32`
m_bCompleteOnNextWake | `bool`

---

## CPulseCell_BaseRequirement
Derived from: [CPulseCell_Base](#cpulsecell_base)

---

## CPulseCell_BaseState
Derived from: [CPulseCell_BaseYieldingInflow](#cpulsecell_baseyieldinginflow), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

---

## OutflowWithRequirements_t

Name | Type
------------ | -------------
m_Connection | `CPulse_OutflowConnection`
m_DestinationFlowNodeID | `PulseDocNodeID_t`
m_RequirementNodeIDs | `CUtlVector< PulseDocNodeID_t >`
m_nCursorStateBlockIndex | `CUtlVector< int32 >`

---

## CPulseCell_IsRequirementValid
Derived from: [CPulseCell_BaseRequirement](#cpulsecell_baserequirement), [CPulseCell_Base](#cpulsecell_base)

---

## C_SoundEventPathCornerEntity
Derived from: [C_SoundEventEntity](#c_soundevententity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_vecCornerPairsNetworked | `C_NetworkUtlVectorBase< SoundeventPathCornerPairNetworked_t >`

---

## C_InfoVisibilityBox
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_nMode | `int32`
m_vBoxSize | `Vector`
m_bEnabled | `bool`

---

## CCSPlayer_ItemServices
Derived from: [CPlayer_ItemServices](#cplayer_itemservices)

Name | Type
------------ | -------------
m_bHasDefuser | `bool`
m_bHasHelmet | `bool`

---

## CPulseCell_Value_Gradient
Derived from: [CPulseCell_BaseValue](#cpulsecell_basevalue), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_Gradient | `CColorGradient`

---

## IntervalTimer

Name | Type
------------ | -------------
m_timestamp | `GameTime_t`
m_nWorldGroupId | `WorldGroupId_t`

---

## audioparams_t

Name | Type
------------ | -------------
localSound | `Vector[8]`
soundscapeIndex | `int32`
localBits | `uint8`
soundscapeEntityListIndex | `int32`
soundEventHash | `uint32`

---

## C_PathParticleRope
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bStartActive | `bool`
m_flMaxSimulationTime | `float32`
m_iszEffectName | `CUtlSymbolLarge`
m_PathNodes_Name | `CUtlVector< CUtlSymbolLarge >`
m_flParticleSpacing | `float32`
m_flSlack | `float32`
m_flRadius | `float32`
m_ColorTint | `Color`
m_nEffectState | `int32`
m_iEffectIndex | `CStrongHandle< InfoForResourceTypeIParticleSystemDefinition >`
m_PathNodes_Position | `C_NetworkUtlVectorBase< Vector >`
m_PathNodes_TangentIn | `C_NetworkUtlVectorBase< Vector >`
m_PathNodes_TangentOut | `C_NetworkUtlVectorBase< Vector >`
m_PathNodes_Color | `C_NetworkUtlVectorBase< Vector >`
m_PathNodes_PinEnabled | `C_NetworkUtlVectorBase< bool >`
m_PathNodes_RadiusScale | `C_NetworkUtlVectorBase< float32 >`

---

## C_DecoyProjectile
Derived from: [C_BaseCSGrenadeProjectile](#c_basecsgrenadeprojectile), [C_BaseGrenade](#c_basegrenade), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_nDecoyShotTick | `int32`
m_nClientLastKnownDecoyShotTick | `int32`
m_flTimeParticleEffectSpawn | `GameTime_t`

---

## C_AttributeContainer
Derived from: [CAttributeManager](#cattributemanager)

Name | Type
------------ | -------------
m_Item | `C_EconItemView`
m_iExternalItemProviderRegisteredToken | `int32`
m_ullRegisteredAsItemID | `uint64`

---

## C_CSWeaponBase
Derived from: [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_thirdPersonFireSequences | `CUtlVector< HSequence >`
m_hCurrentThirdPersonSequence | `HSequence`
m_thirdPersonSequences | `HSequence[7]`
m_iWeaponGameplayAnimState | `WeaponGameplayAnimState`
m_flWeaponGameplayAnimStateTimestamp | `GameTime_t`
m_flInspectCancelCompleteTime | `GameTime_t`
m_bInspectPending | `bool`
m_bInspectShouldLoop | `bool`
m_flCrosshairDistance | `float32`
m_iAmmoLastCheck | `int32`
m_nLastEmptySoundCmdNum | `int32`
m_bFireOnEmpty | `bool`
m_OnPlayerPickup | `CEntityIOOutput`
m_weaponMode | `CSWeaponMode`
m_flTurningInaccuracyDelta | `float32`
m_vecTurningInaccuracyEyeDirLast | `Vector`
m_flTurningInaccuracy | `float32`
m_fAccuracyPenalty | `float32`
m_flLastAccuracyUpdateTime | `GameTime_t`
m_fAccuracySmoothedForZoom | `float32`
m_iRecoilIndex | `int32`
m_flRecoilIndex | `float32`
m_bBurstMode | `bool`
m_flLastBurstModeChangeTime | `GameTime_t`
m_nPostponeFireReadyTicks | `GameTick_t`
m_flPostponeFireReadyFrac | `float32`
m_bInReload | `bool`
m_flDroppedAtTime | `GameTime_t`
m_bIsHauledBack | `bool`
m_bSilencerOn | `bool`
m_flTimeSilencerSwitchComplete | `GameTime_t`
m_iOriginalTeamNumber | `int32`
m_iMostRecentTeamNumber | `int32`
m_bDroppedNearBuyZone | `bool`
m_flNextAttackRenderTimeOffset | `float32`
m_bClearWeaponIdentifyingUGC | `bool`
m_bVisualsDataSet | `bool`
m_bUIWeapon | `bool`
m_nCustomEconReloadEventId | `int32`
m_nextPrevOwnerUseTime | `GameTime_t`
m_hPrevOwner | `CHandle< C_CSPlayerPawn >`
m_nDropTick | `GameTick_t`
m_bWasActiveWeaponWhenDropped | `bool`
m_donated | `bool`
m_fLastShotTime | `GameTime_t`
m_bWasOwnedByCT | `bool`
m_bWasOwnedByTerrorist | `bool`
m_flNextClientFireBulletTime | `float32`
m_flNextClientFireBulletTime_Repredict | `float32`
m_IronSightController | `C_IronSightController`
m_iIronSightMode | `int32`
m_flLastLOSTraceFailureTime | `GameTime_t`
m_flWatTickOffset | `float32`

---

## CTimeline
Derived from: [IntervalTimer](#intervaltimer)

Name | Type
------------ | -------------
m_flValues | `float32[64]`
m_nValueCounts | `int32[64]`
m_nBucketCount | `int32`
m_flInterval | `float32`
m_flFinalValue | `float32`
m_nCompressionType | `TimelineCompression_t`
m_bStopped | `bool`

---

## CPulseCursorFuncs

---

## C_TonemapController2
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flAutoExposureMin | `float32`
m_flAutoExposureMax | `float32`
m_flExposureAdaptationSpeedUp | `float32`
m_flExposureAdaptationSpeedDown | `float32`
m_flTonemapEVSmoothingRange | `float32`

---

## CountdownTimer

Name | Type
------------ | -------------
m_duration | `float32`
m_timestamp | `GameTime_t`
m_timescale | `float32`
m_nWorldGroupId | `WorldGroupId_t`

---

## PulseNodeDynamicOutflows_t::DynamicOutflow_t

Name | Type
------------ | -------------
m_OutflowID | `CGlobalSymbol`
m_Connection | `CPulse_OutflowConnection`

---

## C_WeaponMag7
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## WeaponPurchaseCount_t

Name | Type
------------ | -------------
m_nItemDefIndex | `uint16`
m_nCount | `uint16`

---

## CBasePulseGraphInstance

---

## FilterHealth
Derived from: [CBaseFilter](#cbasefilter), [CLogicalEntity](#clogicalentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bAdrenalineActive | `bool`
m_iHealthMin | `int32`
m_iHealthMax | `int32`

---

## C_PointClientUIHUD
Derived from: [C_BaseClientUIEntity](#c_baseclientuientity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bCheckCSSClasses | `bool`
m_bIgnoreInput | `bool`
m_flWidth | `float32`
m_flHeight | `float32`
m_flDPI | `float32`
m_flInteractDistance | `float32`
m_flDepthOffset | `float32`
m_unOwnerContext | `uint32`
m_unHorizontalAlign | `uint32`
m_unVerticalAlign | `uint32`
m_unOrientation | `uint32`
m_bAllowInteractionFromAllSceneWorlds | `bool`
m_vecCSSClasses | `C_NetworkUtlVectorBase< CUtlSymbolLarge >`

---

## CPulseCell_Inflow_GraphHook
Derived from: [CPulseCell_Inflow_BaseEntrypoint](#cpulsecell_inflow_baseentrypoint), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_HookName | `PulseSymbol_t`

---

## SignatureOutflow_Resume
Derived from: [CPulse_ResumePoint](#cpulse_resumepoint), [CPulse_OutflowConnection](#cpulse_outflowconnection)

---

## CPathSimpleAPI

---

## C_InfoLadderDismount
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_PointCommentaryNode
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bActive | `bool`
m_bWasActive | `bool`
m_flEndTime | `GameTime_t`
m_flStartTime | `GameTime_t`
m_flStartTimeInCommentary | `float32`
m_iszCommentaryFile | `CUtlSymbolLarge`
m_iszTitle | `CUtlSymbolLarge`
m_iszSpeakers | `CUtlSymbolLarge`
m_iNodeNumber | `int32`
m_iNodeNumberMax | `int32`
m_bListenedTo | `bool`
m_hViewPosition | `CHandle< C_BaseEntity >`
m_bRestartAfterRestore | `bool`

---

## CSpriteOriented
Derived from: [C_Sprite](#c_sprite), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## shard_model_desc_t

Name | Type
------------ | -------------
m_nModelID | `int32`
m_hMaterialBase | `CStrongHandle< InfoForResourceTypeIMaterial2 >`
m_hMaterialDamageOverlay | `CStrongHandle< InfoForResourceTypeIMaterial2 >`
m_solid | `ShardSolid_t`
m_vecPanelSize | `Vector2D`
m_vecStressPositionA | `Vector2D`
m_vecStressPositionB | `Vector2D`
m_vecPanelVertices | `C_NetworkUtlVectorBase< Vector2D >`
m_vInitialPanelVertices | `C_NetworkUtlVectorBase< Vector4D >`
m_flGlassHalfThickness | `float32`
m_bHasParent | `bool`
m_bParentFrozen | `bool`
m_SurfacePropStringToken | `CUtlStringToken`

---

## C_KeychainModule
Derived from: [C_CS2WeaponModuleBase](#c_cs2weaponmodulebase), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_nKeychainDefID | `uint32`
m_nKeychainSeed | `uint32`

---

## CFuncWater
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_BuoyancyHelper | `CBuoyancyHelper`

---

## CCSPlayer_GlowServices


---

## CCSGameModeRules

Name | Type
------------ | -------------
__m_pChainEntity | `CNetworkVarChainer`

---

## C_Flashbang
Derived from: [C_BaseCSGrenade](#c_basecsgrenade), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_PointClientUIWorldTextPanel
Derived from: [C_PointClientUIWorldPanel](#c_pointclientuiworldpanel), [C_BaseClientUIEntity](#c_baseclientuientity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_messageText | `char[512]`

---

## CCSPlayer_WaterServices
Derived from: [CPlayer_WaterServices](#cplayer_waterservices)

Name | Type
------------ | -------------
m_flWaterJumpTime | `float32`
m_vecWaterJumpVel | `Vector`
m_flSwimSoundTime | `float32`

---

## C_CSObserverPawn
Derived from: [C_CSPlayerPawnBase](#c_csplayerpawnbase), [C_BasePlayerPawn](#c_baseplayerpawn), [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_hDetectParentChange | `CEntityHandle`

---

## ViewAngleServerChange_t

Name | Type
------------ | -------------
nType | `FixAngleSet_t`
qAngle | `QAngle`
nIndex | `uint32`

---

## C_FuncLadder
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_vecLadderDir | `Vector`
m_Dismounts | `CUtlVector< CHandle< C_InfoLadderDismount > >`
m_vecLocalTop | `Vector`
m_vecPlayerMountPositionTop | `Vector`
m_vecPlayerMountPositionBottom | `Vector`
m_flAutoRideSpeed | `float32`
m_bDisabled | `bool`
m_bFakeLadder | `bool`
m_bHasSlack | `bool`

---

## C_WeaponMP5SD
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_World
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_TeamSelectCounterTerroristPosition
Derived from: [C_CSGO_TeamSelectCharacterPosition](#c_csgo_teamselectcharacterposition), [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WeaponGalilAR
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPlayerBase_CameraServices
Derived from: [CPlayer_CameraServices](#cplayer_cameraservices)

Name | Type
------------ | -------------
m_iFOV | `uint32`
m_iFOVStart | `uint32`
m_flFOVTime | `GameTime_t`
m_flFOVRate | `float32`
m_hZoomOwner | `CHandle< C_BaseEntity >`
m_flLastShotFOV | `float32`

---

## C_TeamplayRules
Derived from: [C_MultiplayRules](#c_multiplayrules), [C_GameRules](#c_gamerules)

---

## CPulseCell_Inflow_BaseEntrypoint
Derived from: [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_EntryChunk | `PulseRuntimeChunkIndex_t`
m_RegisterMap | `PulseRegisterMap_t`

---

## C_WeaponSG556
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSPlayerPawn
Derived from: [C_CSPlayerPawnBase](#c_csplayerpawnbase), [C_BasePlayerPawn](#c_baseplayerpawn), [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_pBulletServices | `CCSPlayer_BulletServices*`
m_pHostageServices | `CCSPlayer_HostageServices*`
m_pBuyServices | `CCSPlayer_BuyServices*`
m_pGlowServices | `CCSPlayer_GlowServices*`
m_pActionTrackingServices | `CCSPlayer_ActionTrackingServices*`
m_pDamageReactServices | `CCSPlayer_DamageReactServices*`
m_flHealthShotBoostExpirationTime | `GameTime_t`
m_flLastFiredWeaponTime | `GameTime_t`
m_bHasFemaleVoice | `bool`
m_flLandingTimeSeconds | `float32`
m_flOldFallVelocity | `float32`
m_szLastPlaceName | `char[18]`
m_bPrevDefuser | `bool`
m_bPrevHelmet | `bool`
m_nPrevArmorVal | `int32`
m_nPrevGrenadeAmmoCount | `int32`
m_unPreviousWeaponHash | `uint32`
m_unWeaponHash | `uint32`
m_bInBuyZone | `bool`
m_bPreviouslyInBuyZone | `bool`
m_aimPunchAngle | `QAngle`
m_aimPunchAngleVel | `QAngle`
m_aimPunchTickBase | `int32`
m_aimPunchTickFraction | `float32`
m_aimPunchCache | `CUtlVector< QAngle >`
m_bInLanding | `bool`
m_flLandingStartTime | `float32`
m_bInHostageRescueZone | `bool`
m_bInBombZone | `bool`
m_bIsBuyMenuOpen | `bool`
m_flTimeOfLastInjury | `GameTime_t`
m_flNextSprayDecalTime | `GameTime_t`
m_iRetakesOffering | `int32`
m_iRetakesOfferingCard | `int32`
m_bRetakesHasDefuseKit | `bool`
m_bRetakesMVPLastRound | `bool`
m_iRetakesMVPBoostItem | `int32`
m_RetakesMVPBoostExtraUtility | `loadout_slot_t`
m_bNeedToReApplyGloves | `bool`
m_EconGloves | `C_EconItemView`
m_nEconGlovesChanged | `uint8`
m_bMustSyncRagdollState | `bool`
m_nRagdollDamageBone | `int32`
m_vRagdollDamageForce | `Vector`
m_vRagdollDamagePosition | `Vector`
m_szRagdollDamageWeaponName | `char[64]`
m_bRagdollDamageHeadshot | `bool`
m_vRagdollServerOrigin | `Vector`
m_bLastHeadBoneTransformIsValid | `bool`
m_lastLandTime | `GameTime_t`
m_bOnGroundLastTick | `bool`
m_hHudModelArms | `CHandle< C_CS2HudModelArms >`
m_qDeathEyeAngles | `QAngle`
m_bSkipOneHeadConstraintUpdate | `bool`
m_bLeftHanded | `bool`
m_fSwitchedHandednessTime | `GameTime_t`
m_flViewmodelOffsetX | `float32`
m_flViewmodelOffsetY | `float32`
m_flViewmodelOffsetZ | `float32`
m_flViewmodelFOV | `float32`
m_vecPlayerPatchEconIndices | `uint32[5]`
m_GunGameImmunityColor | `Color`
m_vecBulletHitModels | `CUtlVector< C_BulletHitModel* >`
m_bIsWalking | `bool`
m_thirdPersonHeading | `QAngle`
m_flSlopeDropOffset | `float32`
m_flSlopeDropHeight | `float32`
m_vHeadConstraintOffset | `Vector`
m_entitySpottedState | `EntitySpottedState_t`
m_bIsScoped | `bool`
m_bResumeZoom | `bool`
m_bIsDefusing | `bool`
m_bIsGrabbingHostage | `bool`
m_iBlockingUseActionInProgress | `CSPlayerBlockingUseAction_t`
m_flEmitSoundTime | `GameTime_t`
m_bInNoDefuseArea | `bool`
m_nWhichBombZone | `int32`
m_iShotsFired | `int32`
m_flFlinchStack | `float32`
m_flVelocityModifier | `float32`
m_flHitHeading | `float32`
m_nHitBodyPart | `int32`
m_bWaitForNoAttack | `bool`
m_ignoreLadderJumpTime | `float32`
m_bKilledByHeadshot | `bool`
m_ArmorValue | `int32`
m_unCurrentEquipmentValue | `uint16`
m_unRoundStartEquipmentValue | `uint16`
m_unFreezetimeEndEquipmentValue | `uint16`
m_nLastKillerIndex | `CEntityIndex`
m_bOldIsScoped | `bool`
m_bHasDeathInfo | `bool`
m_flDeathInfoTime | `float32`
m_vecDeathInfoOrigin | `Vector`
m_grenadeParameterStashTime | `GameTime_t`
m_bGrenadeParametersStashed | `bool`
m_angStashedShootAngles | `QAngle`
m_vecStashedGrenadeThrowPosition | `Vector`
m_vecStashedVelocity | `Vector`
m_angShootAngleHistory | `QAngle[2]`
m_vecThrowPositionHistory | `Vector[2]`
m_vecVelocityHistory | `Vector[2]`
m_PredictedDamageTags | `C_UtlVectorEmbeddedNetworkVar< PredictedDamageTag_t >`
m_nPrevHighestReceivedDamageTagTick | `GameTick_t`
m_nHighestAppliedDamageTagTick | `int32`
m_bShouldAutobuyDMWeapons | `bool`
m_fImmuneToGunGameDamageTime | `GameTime_t`
m_bGunGameImmunity | `bool`
m_fImmuneToGunGameDamageTimeLast | `GameTime_t`
m_fMolotovDamageTime | `float32`

---

## C_CSGO_TeamIntroTerroristPosition
Derived from: [C_CSGO_TeamIntroCharacterPosition](#c_csgo_teamintrocharacterposition), [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPulseCell_WaitForCursorsWithTagBase
Derived from: [CPulseCell_BaseYieldingInflow](#cpulsecell_baseyieldinginflow), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_nCursorsAllowedToWait | `int32`
m_WaitComplete | `CPulse_ResumePoint`

---

## C_Hostage
Derived from: [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_entitySpottedState | `EntitySpottedState_t`
m_leader | `CHandle< C_BaseEntity >`
m_reuseTimer | `CountdownTimer`
m_vel | `Vector`
m_isRescued | `bool`
m_jumpedThisFrame | `bool`
m_nHostageState | `int32`
m_bHandsHaveBeenCut | `bool`
m_hHostageGrabber | `CHandle< C_CSPlayerPawn >`
m_fLastGrabTime | `GameTime_t`
m_vecGrabbedPos | `Vector`
m_flRescueStartTime | `GameTime_t`
m_flGrabSuccessTime | `GameTime_t`
m_flDropStartTime | `GameTime_t`
m_flDeadOrRescuedTime | `GameTime_t`
m_blinkTimer | `CountdownTimer`
m_lookAt | `Vector`
m_lookAroundTimer | `CountdownTimer`
m_isInit | `bool`
m_eyeAttachment | `AttachmentHandle_t`
m_chestAttachment | `AttachmentHandle_t`
m_pPredictionOwner | `CBasePlayerController*`
m_fNewestAlphaThinkTime | `GameTime_t`

---

## CCSPointScriptExtensions_entity

---

## C_fogplayerparams_t

Name | Type
------------ | -------------
m_hCtrl | `CHandle< C_FogController >`
m_flTransitionTime | `float32`
m_OldColor | `Color`
m_flOldStart | `float32`
m_flOldEnd | `float32`
m_flOldMaxDensity | `float32`
m_flOldHDRColorScale | `float32`
m_flOldFarZ | `float32`
m_NewColor | `Color`
m_flNewStart | `float32`
m_flNewEnd | `float32`
m_flNewMaxDensity | `float32`
m_flNewHDRColorScale | `float32`
m_flNewFarZ | `float32`

---

## CGameSceneNode

Name | Type
------------ | -------------
m_nodeToWorld | `CTransform`
m_pOwner | `CEntityInstance*`
m_pParent | `CGameSceneNode*`
m_pChild | `CGameSceneNode*`
m_pNextSibling | `CGameSceneNode*`
m_hParent | `CGameSceneNodeHandle`
m_vecOrigin | `CNetworkOriginCellCoordQuantizedVector`
m_angRotation | `QAngle`
m_flScale | `float32`
m_vecAbsOrigin | `Vector`
m_angAbsRotation | `QAngle`
m_flAbsScale | `float32`
m_nParentAttachmentOrBone | `int16`
m_bDebugAbsOriginChanges | `bool`
m_bDormant | `bool`
m_bForceParentToBeNetworked | `bool`
m_bDirtyHierarchy | `bitfield:1`
m_bDirtyBoneMergeInfo | `bitfield:1`
m_bNetworkedPositionChanged | `bitfield:1`
m_bNetworkedAnglesChanged | `bitfield:1`
m_bNetworkedScaleChanged | `bitfield:1`
m_bWillBeCallingPostDataUpdate | `bitfield:1`
m_bBoneMergeFlex | `bitfield:1`
m_nLatchAbsOrigin | `bitfield:2`
m_bDirtyBoneMergeBoneToRoot | `bitfield:1`
m_nHierarchicalDepth | `uint8`
m_nHierarchyType | `uint8`
m_nDoNotSetAnimTimeInInvalidatePhysicsCount | `uint8`
m_name | `CUtlStringToken`
m_hierarchyAttachName | `CUtlStringToken`
m_flZOffset | `float32`
m_flClientLocalScale | `float32`
m_vRenderOrigin | `Vector`

---

## CPlayer_ObserverServices


Name | Type
------------ | -------------
m_iObserverMode | `uint8`
m_hObserverTarget | `CHandle< C_BaseEntity >`
m_iObserverLastMode | `ObserverMode_t`
m_bForcedObserverMode | `bool`
m_flObserverChaseDistance | `float32`
m_flObserverChaseDistanceCalcTime | `GameTime_t`

---

## C_SoundAreaEntityBase
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bDisabled | `bool`
m_bWasEnabled | `bool`
m_iszSoundAreaType | `CUtlSymbolLarge`
m_vPos | `Vector`

---

## C_PlayerVisibility
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flVisibilityStrength | `float32`
m_flFogDistanceMultiplier | `float32`
m_flFogMaxDensityMultiplier | `float32`
m_flFadeTime | `float32`
m_bStartDisabled | `bool`
m_bIsEnabled | `bool`

---

## CAttributeManager::cached_attribute_float_t

Name | Type
------------ | -------------
flIn | `float32`
iAttribHook | `CUtlSymbolLarge`
flOut | `float32`

---

## C_BasePlayerWeapon
Derived from: [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_nNextPrimaryAttackTick | `GameTick_t`
m_flNextPrimaryAttackTickRatio | `float32`
m_nNextSecondaryAttackTick | `GameTick_t`
m_flNextSecondaryAttackTickRatio | `float32`
m_iClip1 | `int32`
m_iClip2 | `int32`
m_pReserveAmmo | `int32[2]`

---

## CRagdollManager
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_iCurrentMaxRagdollCount | `int8`

---

## C_HEGrenade
Derived from: [C_BaseCSGrenade](#c_basecsgrenade), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EnvSky
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_hSkyMaterial | `CStrongHandle< InfoForResourceTypeIMaterial2 >`
m_hSkyMaterialLightingOnly | `CStrongHandle< InfoForResourceTypeIMaterial2 >`
m_bStartDisabled | `bool`
m_vTintColor | `Color`
m_vTintColorLightingOnly | `Color`
m_flBrightnessScale | `float32`
m_nFogType | `int32`
m_flFogMinStart | `float32`
m_flFogMinEnd | `float32`
m_flFogMaxStart | `float32`
m_flFogMaxEnd | `float32`
m_bEnabled | `bool`

---

## CPulse_InvokeBinding

Name | Type
------------ | -------------
m_RegisterMap | `PulseRegisterMap_t`
m_FuncName | `PulseSymbol_t`
m_nCellIndex | `PulseRuntimeCellIndex_t`
m_nSrcChunk | `PulseRuntimeChunkIndex_t`
m_nSrcInstruction | `int32`

---

## C_EnvWindController
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_EnvWindShared | `C_EnvWindShared`
m_fDirectionVariation | `float32`
m_fSpeedVariation | `float32`
m_fTurbulence | `float32`
m_fVolumeHalfExtentXY | `float32`
m_fVolumeHalfExtentZ | `float32`
m_nVolumeResolutionXY | `int32`
m_nVolumeResolutionZ | `int32`
m_nClipmapLevels | `int32`
m_bIsMaster | `bool`
m_bFirstTime | `bool`

---

## C_GameRules

Name | Type
------------ | -------------
__m_pChainEntity | `CNetworkVarChainer`
m_nTotalPausedTicks | `int32`
m_nPauseStartTick | `int32`
m_bGamePaused | `bool`

---

## C_WeaponMAC10
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_MapPreviewCameraPath
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flZFar | `float32`
m_flZNear | `float32`
m_bLoop | `bool`
m_bVerticalFOV | `bool`
m_bConstantSpeed | `bool`
m_flDuration | `float32`
m_flPathLength | `float32`
m_flPathDuration | `float32`
m_bDofEnabled | `bool`
m_flDofNearBlurry | `float32`
m_flDofNearCrisp | `float32`
m_flDofFarCrisp | `float32`
m_flDofFarBlurry | `float32`
m_flDofTiltToGround | `float32`

---

## C_PointWorldText
Derived from: [C_ModelPointEntity](#c_modelpointentity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bForceRecreateNextUpdate | `bool`
m_messageText | `char[512]`
m_FontName | `char[64]`
m_BackgroundMaterialName | `char[64]`
m_bEnabled | `bool`
m_bFullbright | `bool`
m_flWorldUnitsPerPx | `float32`
m_flFontSize | `float32`
m_flDepthOffset | `float32`
m_bDrawBackground | `bool`
m_flBackgroundBorderWidth | `float32`
m_flBackgroundBorderHeight | `float32`
m_flBackgroundWorldToUV | `float32`
m_Color | `Color`
m_nJustifyHorizontal | `PointWorldTextJustifyHorizontal_t`
m_nJustifyVertical | `PointWorldTextJustifyVertical_t`
m_nReorientMode | `PointWorldTextReorientMode_t`

---

## C_RopeKeyframe
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_LinksTouchingSomething | `CBitVec< 10 >`
m_nLinksTouchingSomething | `int32`
m_bApplyWind | `bool`
m_fPrevLockedPoints | `int32`
m_iForcePointMoveCounter | `int32`
m_bPrevEndPointPos | `bool[2]`
m_vPrevEndPointPos | `Vector[2]`
m_flCurScroll | `float32`
m_flScrollSpeed | `float32`
m_RopeFlags | `uint16`
m_iRopeMaterialModelIndex | `CStrongHandle< InfoForResourceTypeIMaterial2 >`
m_nSegments | `uint8`
m_hStartPoint | `CHandle< C_BaseEntity >`
m_hEndPoint | `CHandle< C_BaseEntity >`
m_iStartAttachment | `AttachmentHandle_t`
m_iEndAttachment | `AttachmentHandle_t`
m_Subdiv | `uint8`
m_RopeLength | `int16`
m_Slack | `int16`
m_TextureScale | `float32`
m_fLockedPoints | `uint8`
m_nChangeCount | `uint8`
m_Width | `float32`
m_PhysicsDelegate | `C_RopeKeyframe::CPhysicsDelegate`
m_hMaterial | `CStrongHandle< InfoForResourceTypeIMaterial2 >`
m_TextureHeight | `int32`
m_vecImpulse | `Vector`
m_vecPreviousImpulse | `Vector`
m_flCurrentGustTimer | `float32`
m_flCurrentGustLifetime | `float32`
m_flTimeToNextGust | `float32`
m_vWindDir | `Vector`
m_vColorMod | `Vector`
m_vCachedEndPointAttachmentPos | `Vector[2]`
m_vCachedEndPointAttachmentAngle | `QAngle[2]`
m_bConstrainBetweenEndpoints | `bool`
m_bEndPointAttachmentPositionsDirty | `bitfield:1`
m_bEndPointAttachmentAnglesDirty | `bitfield:1`
m_bNewDataThisFrame | `bitfield:1`
m_bPhysicsInitted | `bitfield:1`

---

## C_BaseToggle
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EnvCubemapBox
Derived from: [C_EnvCubemap](#c_envcubemap), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EnvCombinedLightProbeVolumeAlias_func_combined_light_probe_volume
Derived from: [C_EnvCombinedLightProbeVolume](#c_envcombinedlightprobevolume), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_RopeKeyframe::CPhysicsDelegate

Name | Type
------------ | -------------
m_pKeyframe | `C_RopeKeyframe*`

---

## CInfoDynamicShadowHint
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bDisabled | `bool`
m_flRange | `float32`
m_nImportance | `int32`
m_nLightChoice | `int32`
m_hLight | `CHandle< C_BaseEntity >`

---

## CCSPointScriptExtensions_observer

---

## C_FuncMoveLinear
Derived from: [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CServerOnlyModelEntity
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_TeamSelectCamera
Derived from: [C_CSGO_TeamPreviewCamera](#c_csgo_teampreviewcamera), [C_CSGO_MapPreviewCameraPath](#c_csgo_mappreviewcamerapath), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPulseCell_IntervalTimer
Derived from: [CPulseCell_BaseYieldingInflow](#cpulsecell_baseyieldinginflow), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_Completed | `CPulse_ResumePoint`
m_OnInterval | `SignatureOutflow_Continue`

---

## C_WeaponXM1014
Derived from: [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WorldModelGloves
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_PhysicsPropMultiplayer
Derived from: [C_PhysicsProp](#c_physicsprop), [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_SoundEventOBBEntity
Derived from: [C_SoundEventEntity](#c_soundevententity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_vMins | `Vector`
m_vMaxs | `Vector`

---

## CPulseTestScriptLib

---

## CCSPointScriptExtensions_player_controller

---

## CPulseCell_BaseLerp
Derived from: [CPulseCell_BaseYieldingInflow](#cpulsecell_baseyieldinginflow), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_WakeResume | `CPulse_ResumePoint`

---

## C_WeaponAug
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BasePropDoor
Derived from: [C_DynamicProp](#c_dynamicprop), [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_eDoorState | `DoorState_t`
m_modelChanged | `bool`
m_bLocked | `bool`
m_bNoNPCs | `bool`
m_closedPosition | `Vector`
m_closedAngles | `QAngle`
m_hMaster | `CHandle< C_BasePropDoor >`
m_vWhereToSetLightingOrigin | `Vector`

---

## CNetworkedSequenceOperation

Name | Type
------------ | -------------
m_hSequence | `HSequence`
m_flPrevCycle | `float32`
m_flCycle | `float32`
m_flWeight | `CNetworkedQuantizedFloat`
m_bSequenceChangeNetworked | `bool`
m_bDiscontinuity | `bool`
m_flPrevCycleFromDiscontinuity | `float32`
m_flPrevCycleForAnimEventDetection | `float32`

---

## C_Item_Healthshot
Derived from: [C_WeaponBaseItem](#c_weaponbaseitem), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CEntityInstance

Name | Type
------------ | -------------
m_iszPrivateVScripts | `CUtlSymbolLarge`
m_pEntity | `CEntityIdentity*`
m_CScriptComponent | `CScriptComponent*`

---

## C_BaseModelEntity
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_CRenderComponent | `CRenderComponent*`
m_CHitboxComponent | `CHitboxComponent`
m_pDestructiblePartsSystemComponent | `CDestructiblePartsSystemComponent*`
m_LastHitGroup | `HitGroup_t`
m_sLastDamageSourceName | `CGlobalSymbol`
m_vLastDamagePosition | `Vector`
m_bInitModelEffects | `bool`
m_bIsStaticProp | `bool`
m_nLastAddDecal | `int32`
m_nDecalsAdded | `int32`
m_iOldHealth | `int32`
m_nRenderMode | `RenderMode_t`
m_nRenderFX | `RenderFx_t`
m_bAllowFadeInView | `bool`
m_clrRender | `Color`
m_vecRenderAttributes | `C_UtlVectorEmbeddedNetworkVar< EntityRenderAttribute_t >`
m_bRenderToCubemaps | `bool`
m_bNoInterpolate | `bool`
m_Collision | `CCollisionProperty`
m_Glow | `CGlowProperty`
m_flGlowBackfaceMult | `float32`
m_fadeMinDist | `float32`
m_fadeMaxDist | `float32`
m_flFadeScale | `float32`
m_flShadowStrength | `float32`
m_nObjectCulling | `uint8`
m_nAddDecal | `int32`
m_vDecalPosition | `Vector`
m_vDecalForwardAxis | `Vector`
m_flDecalHealBloodRate | `float32`
m_flDecalHealHeightRate | `float32`
m_ConfigEntitiesToPropagateMaterialDecalsTo | `C_NetworkUtlVectorBase< CHandle< C_BaseModelEntity > >`
m_vecViewOffset | `CNetworkViewOffsetVector`
m_pClientAlphaProperty | `CClientAlphaProperty*`
m_ClientOverrideTint | `Color`
m_bUseClientOverrideTint | `bool`

---

## CCSPlayer_BulletServices


Name | Type
------------ | -------------
m_totalHitsOnServer | `int32`

---

## C_SoundOpvarSetAutoRoomEntity
Derived from: [C_SoundOpvarSetPointEntity](#c_soundopvarsetpointentity), [C_SoundOpvarSetPointBase](#c_soundopvarsetpointbase), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EnvCombinedLightProbeVolume
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_Entity_Color | `Color`
m_Entity_flBrightness | `float32`
m_Entity_hCubemapTexture | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_bCustomCubemapTexture | `bool`
m_Entity_hLightProbeTexture_AmbientCube | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_hLightProbeTexture_SDF | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_hLightProbeTexture_SH2_DC | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_hLightProbeTexture_SH2_R | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_hLightProbeTexture_SH2_G | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_hLightProbeTexture_SH2_B | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_hLightProbeDirectLightIndicesTexture | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_hLightProbeDirectLightScalarsTexture | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_hLightProbeDirectLightShadowsTexture | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_vBoxMins | `Vector`
m_Entity_vBoxMaxs | `Vector`
m_Entity_bMoveable | `bool`
m_Entity_nHandshake | `int32`
m_Entity_nEnvCubeMapArrayIndex | `int32`
m_Entity_nPriority | `int32`
m_Entity_bStartDisabled | `bool`
m_Entity_flEdgeFadeDist | `float32`
m_Entity_vEdgeFadeDists | `Vector`
m_Entity_nLightProbeSizeX | `int32`
m_Entity_nLightProbeSizeY | `int32`
m_Entity_nLightProbeSizeZ | `int32`
m_Entity_nLightProbeAtlasX | `int32`
m_Entity_nLightProbeAtlasY | `int32`
m_Entity_nLightProbeAtlasZ | `int32`
m_Entity_bEnabled | `bool`

---

## C_MultiplayRules
Derived from: [C_GameRules](#c_gamerules)

---

## CPlayer_AutoaimServices


---

## C_LightDirectionalEntity
Derived from: [C_LightEntity](#c_lightentity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BaseEntity
Derived from: [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_CBodyComponent | `CBodyComponent*`
m_NetworkTransmitComponent | `CNetworkTransmitComponent`
m_nLastThinkTick | `GameTick_t`
m_pGameSceneNode | `CGameSceneNode*`
m_pRenderComponent | `CRenderComponent*`
m_pCollision | `CCollisionProperty*`
m_iMaxHealth | `int32`
m_iHealth | `int32`
m_lifeState | `uint8`
m_bTakesDamage | `bool`
m_nTakeDamageFlags | `TakeDamageFlags_t`
m_nPlatformType | `EntityPlatformTypes_t`
m_ubInterpolationFrame | `uint8`
m_hSceneObjectController | `CHandle< C_BaseEntity >`
m_nNoInterpolationTick | `int32`
m_nVisibilityNoInterpolationTick | `int32`
m_flProxyRandomValue | `float32`
m_iEFlags | `int32`
m_nWaterType | `uint8`
m_bInterpolateEvenWithNoModel | `bool`
m_bPredictionEligible | `bool`
m_bApplyLayerMatchIDToModel | `bool`
m_tokLayerMatchID | `CUtlStringToken`
m_nSubclassID | `CUtlStringToken`
m_nSimulationTick | `int32`
m_iCurrentThinkContext | `int32`
m_aThinkFunctions | `CUtlVector< thinkfunc_t >`
m_bDisabledContextThinks | `bool`
m_flAnimTime | `float32`
m_flSimulationTime | `float32`
m_nSceneObjectOverrideFlags | `uint8`
m_bHasSuccessfullyInterpolated | `bool`
m_bHasAddedVarsToInterpolation | `bool`
m_bRenderEvenWhenNotSuccessfullyInterpolated | `bool`
m_nInterpolationLatchDirtyFlags | `int32[2]`
m_ListEntry | `uint16[11]`
m_flCreateTime | `GameTime_t`
m_flSpeed | `float32`
m_EntClientFlags | `uint16`
m_bClientSideRagdoll | `bool`
m_iTeamNum | `uint8`
m_spawnflags | `uint32`
m_nNextThinkTick | `GameTick_t`
m_fFlags | `uint32`
m_vecAbsVelocity | `Vector`
m_vecServerVelocity | `CNetworkVelocityVector`
m_vecVelocity | `CNetworkVelocityVector`
m_vecBaseVelocity | `Vector`
m_hEffectEntity | `CHandle< C_BaseEntity >`
m_hOwnerEntity | `CHandle< C_BaseEntity >`
m_MoveCollide | `MoveCollide_t`
m_MoveType | `MoveType_t`
m_nActualMoveType | `MoveType_t`
m_flWaterLevel | `float32`
m_fEffects | `uint32`
m_hGroundEntity | `CHandle< C_BaseEntity >`
m_nGroundBodyIndex | `int32`
m_flFriction | `float32`
m_flElasticity | `float32`
m_flGravityScale | `float32`
m_flTimeScale | `float32`
m_bAnimatedEveryTick | `bool`
m_bGravityDisabled | `bool`
m_flNavIgnoreUntilTime | `GameTime_t`
m_hThink | `uint16`
m_fBBoxVisFlags | `uint8`
m_flActualGravityScale | `float32`
m_bGravityActuallyDisabled | `bool`
m_bPredictable | `bool`
m_bRenderWithViewModels | `bool`
m_nFirstPredictableCommand | `int32`
m_nLastPredictableCommand | `int32`
m_hOldMoveParent | `CHandle< C_BaseEntity >`
m_Particles | `CParticleProperty`
m_vecAngVelocity | `QAngle`
m_DataChangeEventRef | `int32`
m_dependencies | `CUtlVector< CEntityHandle >`
m_nCreationTick | `int32`
m_bAnimTimeChanged | `bool`
m_bSimulationTimeChanged | `bool`
m_sUniqueHammerID | `CUtlString`
m_nBloodType | `BloodType`

---

## ActiveModelConfig_t

Name | Type
------------ | -------------
m_Handle | `ModelConfigHandle_t`
m_Name | `CUtlSymbolLarge`
m_AssociatedEntities | `C_NetworkUtlVectorBase< CHandle< C_BaseModelEntity > >`
m_AssociatedEntityNames | `C_NetworkUtlVectorBase< CUtlSymbolLarge >`

---

## C_WeaponSSG08
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPulseCell_Value_Curve
Derived from: [CPulseCell_BaseValue](#cpulsecell_basevalue), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_Curve | `CPiecewiseCurve`

---

## C_BasePlayerPawn
Derived from: [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_pWeaponServices | `CPlayer_WeaponServices*`
m_pItemServices | `CPlayer_ItemServices*`
m_pAutoaimServices | `CPlayer_AutoaimServices*`
m_pObserverServices | `CPlayer_ObserverServices*`
m_pWaterServices | `CPlayer_WaterServices*`
m_pUseServices | `CPlayer_UseServices*`
m_pFlashlightServices | `CPlayer_FlashlightServices*`
m_pCameraServices | `CPlayer_CameraServices*`
m_pMovementServices | `CPlayer_MovementServices*`
m_ServerViewAngleChanges | `C_UtlVectorEmbeddedNetworkVar< ViewAngleServerChange_t >`
v_angle | `QAngle`
v_anglePrevious | `QAngle`
m_iHideHUD | `uint32`
m_skybox3d | `sky3dparams_t`
m_flDeathTime | `GameTime_t`
m_vecPredictionError | `Vector`
m_flPredictionErrorTime | `GameTime_t`
m_vecLastCameraSetupLocalOrigin | `Vector`
m_flLastCameraSetupTime | `GameTime_t`
m_flFOVSensitivityAdjust | `float32`
m_flMouseSensitivity | `float32`
m_vOldOrigin | `Vector`
m_flOldSimulationTime | `float32`
m_nLastExecutedCommandNumber | `int32`
m_nLastExecutedCommandTick | `int32`
m_hController | `CHandle< CBasePlayerController >`
m_hDefaultController | `CHandle< CBasePlayerController >`
m_bIsSwappingToPredictableController | `bool`

---

## C_Chicken
Derived from: [C_DynamicProp](#c_dynamicprop), [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_hHolidayHatAddon | `CHandle< CBaseAnimGraph >`
m_jumpedThisFrame | `bool`
m_leader | `CHandle< C_CSPlayerPawn >`
m_AttributeManager | `C_AttributeContainer`
m_bAttributesInitialized | `bool`
m_hWaterWakeParticles | `ParticleIndex_t`
m_bIsPreviewModel | `bool`

---

## C_SoundOpvarSetAABBEntity
Derived from: [C_SoundOpvarSetPointEntity](#c_soundopvarsetpointentity), [C_SoundOpvarSetPointBase](#c_soundopvarsetpointbase), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPointScriptExtensions_weapon_cs_base

---

## C_WeaponBizon
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_StattrakModule
Derived from: [C_CS2WeaponModuleBase](#c_cs2weaponmodulebase), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bKnife | `bool`

---

## CCSObserver_CameraServices
Derived from: [CCSPlayerBase_CameraServices](#ccsplayerbase_cameraservices), [CPlayer_CameraServices](#cplayer_cameraservices)

---

## CTakeDamageInfoAPI

---

## CEnvSoundscapeProxy
Derived from: [CEnvSoundscape](#cenvsoundscape), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_MainSoundscapeName | `CUtlSymbolLarge`

---

## C_SoundEventEntity
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bStartOnSpawn | `bool`
m_bToLocalPlayer | `bool`
m_bStopOnNew | `bool`
m_bSaveRestore | `bool`
m_bSavedIsPlaying | `bool`
m_flSavedElapsedTime | `float32`
m_iszSourceEntityName | `CUtlSymbolLarge`
m_iszAttachmentName | `CUtlSymbolLarge`
m_onGUIDChanged | `CEntityOutputTemplate< uint64 >`
m_onSoundFinished | `CEntityIOOutput`
m_flClientCullRadius | `float32`
m_iszSoundName | `CUtlSymbolLarge`
m_hSource | `CEntityHandle`
m_nEntityIndexSelection | `int32`
m_bClientSideOnly | `bitfield:1`

---

## CPulseCell_Inflow_EventHandler
Derived from: [CPulseCell_Inflow_BaseEntrypoint](#cpulsecell_inflow_baseentrypoint), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_EventName | `PulseSymbol_t`

---

## C_LightOrthoEntity
Derived from: [C_LightEntity](#c_lightentity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPointScriptEntity
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPulseCell_BaseFlow
Derived from: [CPulseCell_Base](#cpulsecell_base)

---

## CBombTarget
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bBombPlantedHere | `bool`

---

## C_Knife
Derived from: [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bFirstAttack | `bool`

---

## C_CSGO_TerroristWingmanIntroCamera
Derived from: [C_CSGO_TeamPreviewCamera](#c_csgo_teampreviewcamera), [C_CSGO_MapPreviewCameraPath](#c_csgo_mappreviewcamerapath), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CSkeletonInstance
Derived from: [CGameSceneNode](#cgamescenenode)

Name | Type
------------ | -------------
m_modelState | `CModelState`
m_bIsAnimationEnabled | `bool`
m_bUseParentRenderBounds | `bool`
m_bDisableSolidCollisionsForHierarchy | `bool`
m_bDirtyMotionType | `bitfield:1`
m_bIsGeneratingLatchedParentSpaceState | `bitfield:1`
m_materialGroup | `CUtlStringToken`
m_nHitboxSet | `uint8`

---

## CEntityComponent

---

## C_ItemDogtags
Derived from: [C_Item](#c_item), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_OwningPlayer | `CHandle< C_CSPlayerPawn >`
m_KillingPlayer | `CHandle< C_CSPlayerPawn >`

---

## C_LateUpdatedAnimating
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPointScriptExtensions_player

---

## CPulseCell_Outflow_CycleShuffled::InstanceState_t

Name | Type
------------ | -------------
m_Shuffle | `CUtlVectorFixedGrowable< uint8, 8 >`
m_nNextShuffle | `int32`

---

## CPulseCell_BaseLerp::CursorState_t

Name | Type
------------ | -------------
m_StartTime | `GameTime_t`
m_EndTime | `GameTime_t`

---

## CSharedPulseTypeQueryRegistration

---

## CPulseAnimFuncs

---

## C_BaseClientUIEntity
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bEnabled | `bool`
m_DialogXMLName | `CUtlSymbolLarge`
m_PanelClassName | `CUtlSymbolLarge`
m_PanelID | `CUtlSymbolLarge`

---

## CPulseCell_WaitForCursorsWithTagBase::CursorState_t

Name | Type
------------ | -------------
m_TagName | `PulseSymbol_t`

---

## CPulseArraylib

---

## C_WeaponUSPSilencer
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_MolotovProjectile
Derived from: [C_BaseCSGrenadeProjectile](#c_basecsgrenadeprojectile), [C_BaseGrenade](#c_basegrenade), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bIsIncGrenade | `bool`

---

## C_TriggerLerpObject
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPointTemplateAPI

---

## C_WeaponRevolver
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WeaponElite
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_DynamicPropAlias_cable_dynamic
Derived from: [C_DynamicProp](#c_dynamicprop), [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CBaseProp
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bModelOverrodeBlockLOS | `bool`
m_iShapeType | `int32`
m_bConformToCollisionBounds | `bool`
m_mPreferredCatchTransform | `CTransform`

---

## CInfoOffscreenPanoramaTexture
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bDisabled | `bool`
m_nResolutionX | `int32`
m_nResolutionY | `int32`
m_szLayoutFileName | `CUtlSymbolLarge`
m_RenderAttrName | `CUtlSymbolLarge`
m_TargetEntities | `C_NetworkUtlVectorBase< CHandle< C_BaseModelEntity > >`
m_nTargetChangeCount | `int32`
m_vecCSSClasses | `C_NetworkUtlVectorBase< CUtlSymbolLarge >`
m_bCheckCSSClasses | `bool`

---

## CCSWeaponBaseVData
Derived from: [CBasePlayerWeaponVData](#cbaseplayerweaponvdata)

Name | Type
------------ | -------------
m_WeaponType | `CSWeaponType`
m_WeaponCategory | `CSWeaponCategory`
m_szModel_AG2 | `CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >`
m_szAnimSkeleton | `CResourceNameTyped< CWeakHandle< InfoForResourceTypeCNmSkeleton > >`
m_vecMuzzlePos0 | `Vector`
m_vecMuzzlePos1 | `Vector`
m_szTracerParticle | `CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >`
m_GearSlot | `gear_slot_t`
m_GearSlotPosition | `int32`
m_DefaultLoadoutSlot | `loadout_slot_t`
m_nPrice | `int32`
m_nKillAward | `int32`
m_nPrimaryReserveAmmoMax | `int32`
m_nSecondaryReserveAmmoMax | `int32`
m_bMeleeWeapon | `bool`
m_bHasBurstMode | `bool`
m_bIsRevolver | `bool`
m_bCannotShootUnderwater | `bool`
m_szName | `CGlobalSymbol`
m_eSilencerType | `CSWeaponSilencerType`
m_nCrosshairMinDistance | `int32`
m_nCrosshairDeltaDistance | `int32`
m_bIsFullAuto | `bool`
m_nNumBullets | `int32`
m_bReloadsSingleShells | `bool`
m_flCycleTime | `CFiringModeFloat`
m_flMaxSpeed | `CFiringModeFloat`
m_flSpread | `CFiringModeFloat`
m_flInaccuracyCrouch | `CFiringModeFloat`
m_flInaccuracyStand | `CFiringModeFloat`
m_flInaccuracyJump | `CFiringModeFloat`
m_flInaccuracyLand | `CFiringModeFloat`
m_flInaccuracyLadder | `CFiringModeFloat`
m_flInaccuracyFire | `CFiringModeFloat`
m_flInaccuracyMove | `CFiringModeFloat`
m_flRecoilAngle | `CFiringModeFloat`
m_flRecoilAngleVariance | `CFiringModeFloat`
m_flRecoilMagnitude | `CFiringModeFloat`
m_flRecoilMagnitudeVariance | `CFiringModeFloat`
m_nTracerFrequency | `CFiringModeInt`
m_flInaccuracyJumpInitial | `float32`
m_flInaccuracyJumpApex | `float32`
m_flInaccuracyReload | `float32`
m_flDeployDuration | `float32`
m_flDisallowAttackAfterReloadStartDuration | `float32`
m_nRecoilSeed | `int32`
m_nSpreadSeed | `int32`
m_flAttackMovespeedFactor | `float32`
m_flInaccuracyPitchShift | `float32`
m_flInaccuracyAltSoundThreshold | `float32`
m_szUseRadioSubtitle | `CUtlString`
m_bUnzoomsAfterShot | `bool`
m_bHideViewModelWhenZoomed | `bool`
m_nZoomLevels | `int32`
m_nZoomFOV1 | `int32`
m_nZoomFOV2 | `int32`
m_flZoomTime0 | `float32`
m_flZoomTime1 | `float32`
m_flZoomTime2 | `float32`
m_flIronSightPullUpSpeed | `float32`
m_flIronSightPutDownSpeed | `float32`
m_flIronSightFOV | `float32`
m_flIronSightPivotForward | `float32`
m_flIronSightLooseness | `float32`
m_nDamage | `int32`
m_flHeadshotMultiplier | `float32`
m_flArmorRatio | `float32`
m_flPenetration | `float32`
m_flRange | `float32`
m_flRangeModifier | `float32`
m_flFlinchVelocityModifierLarge | `float32`
m_flFlinchVelocityModifierSmall | `float32`
m_flRecoveryTimeCrouch | `float32`
m_flRecoveryTimeStand | `float32`
m_flRecoveryTimeCrouchFinal | `float32`
m_flRecoveryTimeStandFinal | `float32`
m_nRecoveryTransitionStartBullet | `int32`
m_nRecoveryTransitionEndBullet | `int32`
m_flThrowVelocity | `float32`
m_vSmokeColor | `Vector`
m_szAnimClass | `CGlobalSymbol`

---

## CAttributeManager

Name | Type
------------ | -------------
m_Providers | `CUtlVector< CHandle< C_BaseEntity > >`
m_iReapplyProvisionParity | `int32`
m_hOuter | `CHandle< C_BaseEntity >`
m_bPreventLoopback | `bool`
m_ProviderType | `attributeprovidertypes_t`
m_CachedResults | `CUtlVector< CAttributeManager::cached_attribute_float_t >`

---

## SignatureOutflow_Continue
Derived from: [CPulse_OutflowConnection](#cpulse_outflowconnection)

---

## CInfoTarget
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPlayer_CameraServices


Name | Type
------------ | -------------
m_vecCsViewPunchAngle | `QAngle`
m_nCsViewPunchAngleTick | `GameTick_t`
m_flCsViewPunchAngleTickRatio | `float32`
m_PlayerFog | `C_fogplayerparams_t`
m_hColorCorrectionCtrl | `CHandle< C_ColorCorrection >`
m_hViewEntity | `CHandle< C_BaseEntity >`
m_hTonemapController | `CHandle< C_TonemapController2 >`
m_audio | `audioparams_t`
m_PostProcessingVolumes | `C_NetworkUtlVectorBase< CHandle< C_PostProcessingVolume > >`
m_flOldPlayerZ | `float32`
m_flOldPlayerViewOffsetZ | `float32`
m_CurrentFog | `fogparams_t`
m_hOldFogController | `CHandle< C_FogController >`
m_bOverrideFogColor | `bool[5]`
m_OverrideFogColor | `Color[5]`
m_bOverrideFogStartEnd | `bool[5]`
m_fOverrideFogStart | `float32[5]`
m_fOverrideFogEnd | `float32[5]`
m_hActivePostProcessingVolume | `CHandle< C_PostProcessingVolume >`
m_angDemoViewAngles | `QAngle`

---

## CPulseCell_Timeline
Derived from: [CPulseCell_BaseYieldingInflow](#cpulsecell_baseyieldinginflow), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_TimelineEvents | `CUtlVector< CPulseCell_Timeline::TimelineEvent_t >`
m_bWaitForChildOutflows | `bool`
m_OnFinished | `CPulse_ResumePoint`
m_OnCanceled | `CPulse_ResumePoint`

---

## CPulseCell_Inflow_EntOutputHandler
Derived from: [CPulseCell_Inflow_BaseEntrypoint](#cpulsecell_inflow_baseentrypoint), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_SourceEntity | `PulseSymbol_t`
m_SourceOutput | `PulseSymbol_t`
m_ExpectedParamType | `CPulseValueFullType`

---

## C_BaseCSGrenade
Derived from: [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bClientPredictDelete | `bool`
m_bRedraw | `bool`
m_bIsHeldByPlayer | `bool`
m_bPinPulled | `bool`
m_bJumpThrow | `bool`
m_bThrowAnimating | `bool`
m_fThrowTime | `GameTime_t`
m_flThrowStrength | `float32`
m_fDropTime | `GameTime_t`
m_fPinPullTime | `GameTime_t`
m_bJustPulledPin | `bool`
m_nNextHoldTick | `GameTick_t`
m_flNextHoldFrac | `float32`
m_hSwitchToWeaponAfterThrow | `CHandle< C_CSWeaponBase >`

---

## CFilterAttributeInt
Derived from: [CBaseFilter](#cbasefilter), [CLogicalEntity](#clogicalentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_sAttributeName | `CUtlSymbolLarge`

---

## CPointTemplate
Derived from: [CLogicalEntity](#clogicalentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_iszWorldName | `CUtlSymbolLarge`
m_iszSource2EntityLumpName | `CUtlSymbolLarge`
m_iszEntityFilterName | `CUtlSymbolLarge`
m_flTimeoutInterval | `float32`
m_bAsynchronouslySpawnEntities | `bool`
m_clientOnlyEntityBehavior | `PointTemplateClientOnlyEntityBehavior_t`
m_ownerSpawnGroupType | `PointTemplateOwnerSpawnGroupType_t`
m_createdSpawnGroupHandles | `CUtlVector< uint32 >`
m_SpawnedEntityHandles | `CUtlVector< CEntityHandle >`
m_ScriptSpawnCallback | `HSCRIPT`
m_ScriptCallbackScope | `HSCRIPT`

---

## CPlayer_FlashlightServices


---

## CCSPlayerController
Derived from: [CBasePlayerController](#cbaseplayercontroller), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_pInGameMoneyServices | `CCSPlayerController_InGameMoneyServices*`
m_pInventoryServices | `CCSPlayerController_InventoryServices*`
m_pActionTrackingServices | `CCSPlayerController_ActionTrackingServices*`
m_pDamageServices | `CCSPlayerController_DamageServices*`
m_iPing | `uint32`
m_bHasCommunicationAbuseMute | `bool`
m_uiCommunicationMuteFlags | `uint32`
m_szCrosshairCodes | `CUtlSymbolLarge`
m_iPendingTeamNum | `uint8`
m_flForceTeamTime | `GameTime_t`
m_iCompTeammateColor | `int32`
m_bEverPlayedOnTeam | `bool`
m_flPreviousForceJoinTeamTime | `GameTime_t`
m_szClan | `CUtlSymbolLarge`
m_sSanitizedPlayerName | `CUtlString`
m_iCoachingTeam | `int32`
m_nPlayerDominated | `uint64`
m_nPlayerDominatingMe | `uint64`
m_iCompetitiveRanking | `int32`
m_iCompetitiveWins | `int32`
m_iCompetitiveRankType | `int8`
m_iCompetitiveRankingPredicted_Win | `int32`
m_iCompetitiveRankingPredicted_Loss | `int32`
m_iCompetitiveRankingPredicted_Tie | `int32`
m_nEndMatchNextMapVote | `int32`
m_unActiveQuestId | `uint16`
m_rtActiveMissionPeriod | `uint32`
m_nQuestProgressReason | `QuestProgress::Reason`
m_unPlayerTvControlFlags | `uint32`
m_iDraftIndex | `int32`
m_msQueuedModeDisconnectionTimestamp | `uint32`
m_uiAbandonRecordedReason | `uint32`
m_eNetworkDisconnectionReason | `uint32`
m_bCannotBeKicked | `bool`
m_bEverFullyConnected | `bool`
m_bAbandonAllowsSurrender | `bool`
m_bAbandonOffersInstantSurrender | `bool`
m_bDisconnection1MinWarningPrinted | `bool`
m_bScoreReported | `bool`
m_nDisconnectionTick | `int32`
m_bControllingBot | `bool`
m_bHasControlledBotThisRound | `bool`
m_bHasBeenControlledByPlayerThisRound | `bool`
m_nBotsControlledThisRound | `int32`
m_bCanControlObservedBot | `bool`
m_hPlayerPawn | `CHandle< C_CSPlayerPawn >`
m_hObserverPawn | `CHandle< C_CSObserverPawn >`
m_bPawnIsAlive | `bool`
m_iPawnHealth | `uint32`
m_iPawnArmor | `int32`
m_bPawnHasDefuser | `bool`
m_bPawnHasHelmet | `bool`
m_nPawnCharacterDefIndex | `uint16`
m_iPawnLifetimeStart | `int32`
m_iPawnLifetimeEnd | `int32`
m_iPawnBotDifficulty | `int32`
m_hOriginalControllerOfCurrentPawn | `CHandle< CCSPlayerController >`
m_iScore | `int32`
m_recentKillQueue | `uint8[8]`
m_nFirstKill | `uint8`
m_nKillCount | `uint8`
m_bMvpNoMusic | `bool`
m_eMvpReason | `int32`
m_iMusicKitID | `int32`
m_iMusicKitMVPs | `int32`
m_iMVPs | `int32`
m_bIsPlayerNameDirty | `bool`
m_bFireBulletsSeedSynchronized | `bool`

---

## C_CSGO_TeamIntroCounterTerroristPosition
Derived from: [C_CSGO_TeamIntroCharacterPosition](#c_csgo_teamintrocharacterposition), [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_PreviewModel
Derived from: [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_animgraph | `CUtlString`
m_animgraphCharacterModeString | `CGlobalSymbol`
m_defaultAnim | `CUtlString`
m_nDefaultAnimLoopMode | `AnimLoopMode_t`
m_flInitialModelScale | `float32`
m_sInitialWeaponState | `CUtlString`

---

## C_CSGO_TeamSelectCharacterPosition
Derived from: [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPulseCell_Outflow_CycleOrdered::InstanceState_t

Name | Type
------------ | -------------
m_nNextIndex | `int32`

---

## C_SoundEventAABBEntity
Derived from: [C_SoundEventEntity](#c_soundevententity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_vMins | `Vector`
m_vMaxs | `Vector`

---

## CCSPlayer_MovementServices
Derived from: [CPlayer_MovementServices_Humanoid](#cplayer_movementservices_humanoid), [CPlayer_MovementServices](#cplayer_movementservices)

Name | Type
------------ | -------------
m_vecLadderNormal | `Vector`
m_nLadderSurfacePropIndex | `int32`
m_flDuckAmount | `float32`
m_flDuckSpeed | `float32`
m_bDuckOverride | `bool`
m_bDesiresDuck | `bool`
m_flDuckOffset | `float32`
m_nDuckTimeMsecs | `uint32`
m_nDuckJumpTimeMsecs | `uint32`
m_nJumpTimeMsecs | `uint32`
m_flLastDuckTime | `float32`
m_vecLastPositionAtFullCrouchSpeed | `Vector2D`
m_duckUntilOnGround | `bool`
m_bHasWalkMovedSinceLastJump | `bool`
m_bInStuckTest | `bool`
m_nTraceCount | `int32`
m_StuckLast | `int32`
m_bSpeedCropped | `bool`
m_flGroundMoveEfficiency | `float32`
m_nOldWaterLevel | `int32`
m_flWaterEntryTime | `float32`
m_vecForward | `Vector`
m_vecLeft | `Vector`
m_vecUp | `Vector`
m_nGameCodeHasMovedPlayerAfterCommand | `int32`
m_bOldJumpPressed | `bool`
m_flJumpPressedTime | `float32`
m_fStashGrenadeParameterWhen | `GameTime_t`
m_nButtonDownMaskPrev | `uint64`
m_flOffsetTickCompleteTime | `float32`
m_flOffsetTickStashedSpeed | `float32`
m_flStamina | `float32`
m_flHeightAtJumpStart | `float32`
m_flMaxJumpHeightThisJump | `float32`
m_flMaxJumpHeightLastJump | `float32`
m_flStaminaAtJumpStart | `float32`
m_flAccumulatedJumpError | `float32`
m_flTicksSinceLastSurfingDetected | `float32`
m_bWasSurfing | `bool`

---

## SellbackPurchaseEntry_t

Name | Type
------------ | -------------
m_unDefIdx | `uint16`
m_nCost | `int32`
m_nPrevArmor | `int32`
m_bPrevHelmet | `bool`
m_hItem | `CEntityHandle`

---

## C_TintController
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WeaponBaseItem
Derived from: [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_SequenceCompleteTimer | `CountdownTimer`
m_bRedraw | `bool`

---

## CWaterSplasher
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_FuncBrush
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPulseCell_Outflow_StringSwitch
Derived from: [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_DefaultCaseOutflow | `CPulse_OutflowConnection`
m_CaseOutflows | `CUtlVector< CPulse_OutflowConnection >`

---

## PhysicsRagdollPose_t

Name | Type
------------ | -------------
m_Transforms | `C_NetworkUtlVectorBase< CTransform >`
m_hOwner | `CHandle< C_BaseEntity >`
m_bSetFromDebugHistory | `bool`

---

## CPropDataComponent
Derived from: [CEntityComponent](#centitycomponent)

Name | Type
------------ | -------------
m_flDmgModBullet | `float32`
m_flDmgModClub | `float32`
m_flDmgModExplosive | `float32`
m_flDmgModFire | `float32`
m_iszPhysicsDamageTableName | `CUtlSymbolLarge`
m_iszBasePropData | `CUtlSymbolLarge`
m_nInteractions | `int32`
m_bSpawnMotionDisabled | `bool`
m_nDisableTakePhysicsDamageSpawnFlag | `int32`
m_nMotionDisabledSpawnFlag | `int32`

---

## CPulseCell_LimitCount::InstanceState_t

Name | Type
------------ | -------------
m_nCurrentCount | `int32`

---

## C_WeaponCZ75a
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bMagazineRemoved | `bool`

---

## C_DynamicLight
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_Flags | `uint8`
m_LightStyle | `uint8`
m_Radius | `float32`
m_Exponent | `int32`
m_InnerAngle | `float32`
m_OuterAngle | `float32`
m_SpotRadius | `float32`

---

## EngineCountdownTimer

Name | Type
------------ | -------------
m_duration | `float32`
m_timestamp | `float32`
m_timescale | `float32`

---

## C_SoundEventSphereEntity
Derived from: [C_SoundEventEntity](#c_soundevententity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flRadius | `float32`

---

## CCSPlayerController_DamageServices


Name | Type
------------ | -------------
m_nSendUpdate | `int32`
m_DamageList | `C_UtlVectorEmbeddedNetworkVar< CDamageRecord >`

---

## C_CSGO_TeamPreviewModel
Derived from: [C_CSGO_PreviewPlayer](#c_csgo_previewplayer), [C_CSPlayerPawn](#c_csplayerpawn), [C_CSPlayerPawnBase](#c_csplayerpawnbase), [C_BasePlayerPawn](#c_baseplayerpawn), [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_TonemapController2Alias_env_tonemap_controller2
Derived from: [C_TonemapController2](#c_tonemapcontroller2), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_Inferno
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_nfxFireDamageEffect | `ParticleIndex_t`
m_hInfernoPointsSnapshot | `CStrongHandle< InfoForResourceTypeIParticleSnapshot >`
m_hInfernoFillerPointsSnapshot | `CStrongHandle< InfoForResourceTypeIParticleSnapshot >`
m_hInfernoOutlinePointsSnapshot | `CStrongHandle< InfoForResourceTypeIParticleSnapshot >`
m_hInfernoClimbingOutlinePointsSnapshot | `CStrongHandle< InfoForResourceTypeIParticleSnapshot >`
m_hInfernoDecalsSnapshot | `CStrongHandle< InfoForResourceTypeIParticleSnapshot >`
m_firePositions | `Vector[64]`
m_fireParentPositions | `Vector[64]`
m_bFireIsBurning | `bool[64]`
m_BurnNormal | `Vector[64]`
m_fireCount | `int32`
m_nInfernoType | `int32`
m_nFireLifetime | `float32`
m_bInPostEffectTime | `bool`
m_lastFireCount | `int32`
m_nFireEffectTickBegin | `int32`
m_drawableCount | `int32`
m_blosCheck | `bool`
m_nlosperiod | `int32`
m_maxFireHalfWidth | `float32`
m_maxFireHeight | `float32`
m_minBounds | `Vector`
m_maxBounds | `Vector`
m_flLastGrassBurnThink | `float32`

---

## CFilterLOS
Derived from: [CBaseFilter](#cbasefilter), [CLogicalEntity](#clogicalentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPointOrient
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_iszSpawnTargetName | `CUtlSymbolLarge`
m_hTarget | `CHandle< C_BaseEntity >`
m_bActive | `bool`
m_nGoalDirection | `PointOrientGoalDirectionType_t`
m_nConstraint | `PointOrientConstraint_t`
m_flMaxTurnRate | `float32`
m_flLastGameTime | `GameTime_t`

---

## C_GlobalLight
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_WindClothForceHandle | `uint16`

---

## C_EnvWindClientside
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_EnvWindShared | `C_EnvWindShared`

---

## CCSPointScript
Derived from: [CBasePulseGraphInstance](#cbasepulsegraphinstance)

Name | Type
------------ | -------------
m_pParent | `CCSPointScriptEntity*`

---

## sky3dparams_t

Name | Type
------------ | -------------
scale | `int16`
origin | `Vector`
bClip3DSkyBoxNearToWorldFar | `bool`
flClip3DSkyBoxNearToWorldFarOffset | `float32`
fog | `fogparams_t`
m_nWorldGroupID | `WorldGroupId_t`

---

## C_FlashbangProjectile
Derived from: [C_BaseCSGrenadeProjectile](#c_basecsgrenadeprojectile), [C_BaseGrenade](#c_basegrenade), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WeaponP90
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_EnvWind
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_EnvWindShared | `C_EnvWindShared`

---

## C_CSGO_TerroristTeamIntroCamera
Derived from: [C_CSGO_TeamPreviewCamera](#c_csgo_teampreviewcamera), [C_CSGO_MapPreviewCameraPath](#c_csgo_mappreviewcamerapath), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPulseCell_Step_DebugLog
Derived from: [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

---

## CCSPlayerController_ActionTrackingServices


Name | Type
------------ | -------------
m_perRoundStats | `C_UtlVectorEmbeddedNetworkVar< CSPerRoundStats_t >`
m_matchStats | `CSMatchStats_t`
m_iNumRoundKills | `int32`
m_iNumRoundKillsHeadshots | `int32`
m_unTotalRoundDamageDealt | `uint32`

---

## CBodyComponentBaseAnimGraph
Derived from: [CBodyComponentSkeletonInstance](#cbodycomponentskeletoninstance), [CBodyComponent](#cbodycomponent), [CEntityComponent](#centitycomponent)

Name | Type
------------ | -------------
m_animationController | `CBaseAnimGraphController`

---

## C_CSGO_PreviewModelAlias_csgo_item_previewmodel
Derived from: [C_CSGO_PreviewModel](#c_csgo_previewmodel), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_InfoInstructorHintHostageRescueZone
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPulseCell_BaseYieldingInflow
Derived from: [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

---

## PulseNodeDynamicOutflows_t

Name | Type
------------ | -------------
m_Outflows | `CUtlVector< PulseNodeDynamicOutflows_t::DynamicOutflow_t >`

---

## C_TriggerBuoyancy
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_BuoyancyHelper | `CBuoyancyHelper`
m_flFluidDensity | `float32`

---

## CPlayer_MovementServices_Humanoid
Derived from: [CPlayer_MovementServices](#cplayer_movementservices)

Name | Type
------------ | -------------
m_flStepSoundTime | `float32`
m_flFallVelocity | `float32`
m_bInCrouch | `bool`
m_nCrouchState | `uint32`
m_flCrouchTransitionStartTime | `GameTime_t`
m_bDucked | `bool`
m_bDucking | `bool`
m_bInDuckJump | `bool`
m_groundNormal | `Vector`
m_flSurfaceFriction | `float32`
m_surfaceProps | `CUtlStringToken`
m_nStepside | `int32`

---

## CPulseCell_IsRequirementValid::Criteria_t

Name | Type
------------ | -------------
m_bIsValid | `bool`

---

## C_WeaponTec9
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_PhysPropClientside
Derived from: [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flTouchDelta | `GameTime_t`
m_fDeathTime | `GameTime_t`
m_vecDamagePosition | `Vector`
m_vecDamageDirection | `Vector`
m_nDamageType | `DamageTypes_t`

---

## C_BaseDoor
Derived from: [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bIsUsable | `bool`

---

## CSMatchStats_t
Derived from: [CSPerRoundStats_t](#csperroundstats_t)

Name | Type
------------ | -------------
m_iEnemy5Ks | `int32`
m_iEnemy4Ks | `int32`
m_iEnemy3Ks | `int32`
m_iEnemyKnifeKills | `int32`
m_iEnemyTaserKills | `int32`

---

## EntityRenderAttribute_t

Name | Type
------------ | -------------
m_ID | `CUtlStringToken`
m_Values | `Vector4D`

---

## CPulseCell_Inflow_ObservableVariableListener
Derived from: [CPulseCell_Inflow_BaseEntrypoint](#cpulsecell_inflow_baseentrypoint), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_nBlackboardReference | `PulseRuntimeBlackboardReferenceIndex_t`
m_bSelfReference | `bool`

---

## CFilterMultipleAPI

---

## CHostageRescueZone
Derived from: [CHostageRescueZoneShim](#chostagerescuezoneshim), [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CModelState

Name | Type
------------ | -------------
m_hModel | `CStrongHandle< InfoForResourceTypeCModel >`
m_ModelName | `CUtlSymbolLarge`
m_bClientClothCreationSuppressed | `bool`
m_MeshGroupMask | `uint64`
m_nBodyGroupChoices | `C_NetworkUtlVectorBase< int32 >`
m_nIdealMotionType | `int8`
m_nForceLOD | `int8`
m_nClothUpdateFlags | `int8`

---

## CPulseCell_LerpCameraSettings::CursorState_t
Derived from: [CPulseCell_BaseLerp::CursorState_t](#cpulsecell_baselerp::cursorstate_t)

Name | Type
------------ | -------------
m_hCamera | `CHandle< C_PointCamera >`
m_OverlaidStart | `PointCameraSettings_t`
m_OverlaidEnd | `PointCameraSettings_t`

---

## CPulseCell_Outflow_CycleOrdered
Derived from: [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_Outputs | `CUtlVector< CPulse_OutflowConnection >`

---

## C_CSWeaponBaseGun
Derived from: [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_zoomLevel | `int32`
m_iBurstShotsRemaining | `int32`
m_iSilencerBodygroup | `int32`
m_silencedModelIndex | `int32`
m_inPrecache | `bool`
m_bNeedsBoltAction | `bool`
m_nRevolverCylinderIdx | `int32`

---

## C_CSGameRulesProxy
Derived from: [C_GameRulesProxy](#c_gamerulesproxy), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_pGameRules | `C_CSGameRules*`

---

## CCollisionProperty

Name | Type
------------ | -------------
m_collisionAttribute | `VPhysicsCollisionAttribute_t`
m_vecMins | `Vector`
m_vecMaxs | `Vector`
m_usSolidFlags | `uint8`
m_nSolidType | `SolidType_t`
m_triggerBloat | `uint8`
m_nSurroundType | `SurroundingBoundsType_t`
m_CollisionGroup | `uint8`
m_nEnablePhysics | `uint8`
m_flBoundingRadius | `float32`
m_vecSpecifiedSurroundingMins | `Vector`
m_vecSpecifiedSurroundingMaxs | `Vector`
m_vecSurroundingMaxs | `Vector`
m_vecSurroundingMins | `Vector`
m_vCapsuleCenter1 | `Vector`
m_vCapsuleCenter2 | `Vector`
m_flCapsuleRadius | `float32`

---

## C_WeaponP250
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_ShatterGlassShardPhysics
Derived from: [C_PhysicsProp](#c_physicsprop), [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_ShardDesc | `shard_model_desc_t`

---

## CFilterMassGreater
Derived from: [CBaseFilter](#cbasefilter), [CLogicalEntity](#clogicalentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_fFilterMass | `float32`

---

## C_EntityDissolve
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flStartTime | `GameTime_t`
m_flFadeInStart | `float32`
m_flFadeInLength | `float32`
m_flFadeOutModelStart | `float32`
m_flFadeOutModelLength | `float32`
m_flFadeOutStart | `float32`
m_flFadeOutLength | `float32`
m_flNextSparkTime | `GameTime_t`
m_nDissolveType | `EntityDisolveType_t`
m_vDissolverOrigin | `Vector`
m_nMagnitude | `uint32`
m_bCoreExplode | `bool`
m_bLinkedToServerEnt | `bool`

---

## C_SoundOpvarSetOBBEntity
Derived from: [C_SoundOpvarSetAABBEntity](#c_soundopvarsetaabbentity), [C_SoundOpvarSetPointEntity](#c_soundopvarsetpointentity), [C_SoundOpvarSetPointBase](#c_soundopvarsetpointbase), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSGameModeRules_ArmsRace
Derived from: [CCSGameModeRules](#ccsgamemoderules)

Name | Type
------------ | -------------
m_WeaponSequence | `C_NetworkUtlVectorBase< CUtlString >`

---

## C_FuncMonitor
Derived from: [C_FuncBrush](#c_funcbrush), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_targetCamera | `CUtlString`
m_nResolutionEnum | `int32`
m_bRenderShadows | `bool`
m_bUseUniqueColorTarget | `bool`
m_brushModelName | `CUtlString`
m_hTargetCamera | `CHandle< C_BaseEntity >`
m_bEnabled | `bool`
m_bDraw3DSkybox | `bool`

---

## C_ClientRagdoll
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bFadeOut | `bool`
m_bImportant | `bool`
m_flEffectTime | `GameTime_t`
m_gibDespawnTime | `GameTime_t`
m_iCurrentFriction | `int32`
m_iMinFriction | `int32`
m_iMaxFriction | `int32`
m_iFrictionAnimState | `int32`
m_bReleaseRagdoll | `bool`
m_iEyeAttachment | `AttachmentHandle_t`
m_bFadingOut | `bool`
m_flScaleEnd | `float32[10]`
m_flScaleTimeStart | `GameTime_t[10]`
m_flScaleTimeEnd | `GameTime_t[10]`

---

## PulseSelectorOutflowList_t

Name | Type
------------ | -------------
m_Outflows | `CUtlVector< OutflowWithRequirements_t >`

---

## CPulseCell_PlaySequence::CursorState_t

Name | Type
------------ | -------------
m_hTarget | `CHandle< CBaseAnimGraph >`

---

## CBodyComponentSkeletonInstance
Derived from: [CBodyComponent](#cbodycomponent), [CEntityComponent](#centitycomponent)

Name | Type
------------ | -------------
m_skeletonInstance | `CSkeletonInstance`

---

## C_CS2WeaponModuleBase
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_TeamPreviewCharacterPosition
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_nVariant | `int32`
m_nRandom | `int32`
m_nOrdinal | `int32`
m_sWeaponName | `CUtlString`
m_xuid | `uint64`
m_agentItem | `C_EconItemView`
m_glovesItem | `C_EconItemView`
m_weaponItem | `C_EconItemView`

---

## C_SmokeGrenadeProjectile
Derived from: [C_BaseCSGrenadeProjectile](#c_basecsgrenadeprojectile), [C_BaseGrenade](#c_basegrenade), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_nSmokeEffectTickBegin | `int32`
m_bDidSmokeEffect | `bool`
m_nRandomSeed | `int32`
m_vSmokeColor | `Vector`
m_vSmokeDetonationPos | `Vector`
m_VoxelFrameData | `C_NetworkUtlVectorBase< uint8 >`
m_nVoxelFrameDataSize | `int32`
m_nVoxelUpdate | `int32`
m_bSmokeVolumeDataReceived | `bool`
m_bSmokeEffectSpawned | `bool`

---

## CScriptComponent
Derived from: [CEntityComponent](#centitycomponent)

Name | Type
------------ | -------------
m_scriptClassName | `CUtlSymbolLarge`

---

## CCSPlayer_BuyServices


Name | Type
------------ | -------------
m_vecSellbackPurchaseEntries | `C_UtlVectorEmbeddedNetworkVar< SellbackPurchaseEntry_t >`

---

## C_PortraitWorldCallbackHandler
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_DynamicProp
Derived from: [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bUseHitboxesForRenderBox | `bool`
m_bUseAnimGraph | `bool`
m_pOutputAnimBegun | `CEntityIOOutput`
m_pOutputAnimOver | `CEntityIOOutput`
m_pOutputAnimLoopCycleOver | `CEntityIOOutput`
m_OnAnimReachedStart | `CEntityIOOutput`
m_OnAnimReachedEnd | `CEntityIOOutput`
m_iszIdleAnim | `CUtlSymbolLarge`
m_nIdleAnimLoopMode | `AnimLoopMode_t`
m_bRandomizeCycle | `bool`
m_bStartDisabled | `bool`
m_bFiredStartEndOutput | `bool`
m_bForceNpcExclude | `bool`
m_bCreateNonSolid | `bool`
m_bIsOverrideProp | `bool`
m_iInitialGlowState | `int32`
m_nGlowRange | `int32`
m_nGlowRangeMin | `int32`
m_glowColor | `Color`
m_nGlowTeam | `int32`
m_iCachedFrameCount | `int32`
m_vecCachedRenderMins | `Vector`
m_vecCachedRenderMaxs | `Vector`

---

## C_CSTeam
Derived from: [C_Team](#c_team), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_szTeamMatchStat | `char[512]`
m_numMapVictories | `int32`
m_bSurrendered | `bool`
m_scoreFirstHalf | `int32`
m_scoreSecondHalf | `int32`
m_scoreOvertime | `int32`
m_szClanTeamname | `char[129]`
m_iClanID | `uint32`
m_szTeamFlagImage | `char[8]`
m_szTeamLogoImage | `char[8]`

---

## C_CS2HudModelWeapon
Derived from: [C_CS2HudModelBase](#c_cs2hudmodelbase), [C_LateUpdatedAnimating](#c_lateupdatedanimating), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPulseRuntimeLibModuleLocalTypeQueryRegistration

---

## C_TextureBasedAnimatable
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bLoop | `bool`
m_flFPS | `float32`
m_hPositionKeys | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_hRotationKeys | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_vAnimationBoundsMin | `Vector`
m_vAnimationBoundsMax | `Vector`
m_flStartTime | `float32`
m_flStartFrame | `float32`

---

## C_LightEnvironmentEntity
Derived from: [C_LightDirectionalEntity](#c_lightdirectionalentity), [C_LightEntity](#c_lightentity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CLogicRelayAPI

---

## C_TriggerPhysics
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_gravityScale | `float32`
m_linearLimit | `float32`
m_linearDamping | `float32`
m_angularLimit | `float32`
m_angularDamping | `float32`
m_linearForce | `float32`
m_flFrequency | `float32`
m_flDampingRatio | `float32`
m_vecLinearForcePointAt | `Vector`
m_bCollapseToForcePoint | `bool`
m_vecLinearForcePointAtWorld | `Vector`
m_vecLinearForceDirection | `Vector`
m_bConvertToDebrisWhenPossible | `bool`

---

## C_PropDoorRotating
Derived from: [C_BasePropDoor](#c_basepropdoor), [C_DynamicProp](#c_dynamicprop), [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_HandleTest
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_Handle | `CHandle< C_BaseEntity >`
m_bSendHandle | `bool`

---

## CInfoWorldLayer
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_pOutputOnEntitiesSpawned | `CEntityIOOutput`
m_worldName | `CUtlSymbolLarge`
m_layerName | `CUtlSymbolLarge`
m_bWorldLayerVisible | `bool`
m_bEntitiesSpawned | `bool`
m_bCreateAsChildSpawnGroup | `bool`
m_hLayerSpawnGroup | `uint32`
m_bWorldLayerActuallyVisible | `bool`

---

## CBodyComponentBaseModelEntity
Derived from: [CBodyComponentSkeletonInstance](#cbodycomponentskeletoninstance), [CBodyComponent](#cbodycomponent), [CEntityComponent](#centitycomponent)

---

## C_Multimeter
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_hTargetC4 | `CHandle< C_PlantedC4 >`

---

## C_BaseTrigger
Derived from: [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_OnStartTouch | `CEntityIOOutput`
m_OnStartTouchAll | `CEntityIOOutput`
m_OnEndTouch | `CEntityIOOutput`
m_OnEndTouchAll | `CEntityIOOutput`
m_OnTouching | `CEntityIOOutput`
m_OnTouchingEachEntity | `CEntityIOOutput`
m_OnNotTouching | `CEntityIOOutput`
m_hTouchingEntities | `CUtlVector< CHandle< C_BaseEntity > >`
m_iFilterName | `CUtlSymbolLarge`
m_hFilter | `CHandle< CBaseFilter >`
m_bDisabled | `bool`

---

## FilterDamageType
Derived from: [CBaseFilter](#cbasefilter), [CLogicalEntity](#clogicalentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_iDamageType | `int32`

---

## CAttributeList

Name | Type
------------ | -------------
m_Attributes | `C_UtlVectorEmbeddedNetworkVar< CEconItemAttribute >`
m_pManager | `CAttributeManager*`

---

## CPulseCell_Inflow_Wait
Derived from: [CPulseCell_BaseYieldingInflow](#cpulsecell_baseyieldinginflow), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_WakeResume | `CPulse_ResumePoint`

---

## CFilterProximity
Derived from: [CBaseFilter](#cbasefilter), [CLogicalEntity](#clogicalentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flRadius | `float32`

---

## CEffectData

Name | Type
------------ | -------------
m_vOrigin | `Vector`
m_vStart | `Vector`
m_vNormal | `Vector`
m_vAngles | `QAngle`
m_hEntity | `CEntityHandle`
m_hOtherEntity | `CEntityHandle`
m_flScale | `float32`
m_flMagnitude | `float32`
m_flRadius | `float32`
m_nSurfaceProp | `CUtlStringToken`
m_nEffectIndex | `CWeakHandle< InfoForResourceTypeIParticleSystemDefinition >`
m_nDamageType | `uint32`
m_nPenetrate | `uint8`
m_nMaterial | `uint16`
m_nHitBox | `uint16`
m_nColor | `uint8`
m_fFlags | `uint8`
m_nAttachmentIndex | `AttachmentHandle_t`
m_nAttachmentName | `CUtlStringToken`
m_iEffectName | `uint16`
m_nExplosionType | `uint8`

---

## C_ParticleSystem
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_szSnapshotFileName | `char[512]`
m_bActive | `bool`
m_bFrozen | `bool`
m_flFreezeTransitionDuration | `float32`
m_nStopType | `int32`
m_bAnimateDuringGameplayPause | `bool`
m_iEffectIndex | `CStrongHandle< InfoForResourceTypeIParticleSystemDefinition >`
m_flStartTime | `GameTime_t`
m_flPreSimTime | `float32`
m_vServerControlPoints | `Vector[4]`
m_iServerControlPointAssignments | `uint8[4]`
m_hControlPointEnts | `CHandle< C_BaseEntity >[64]`
m_bNoSave | `bool`
m_bNoFreeze | `bool`
m_bNoRamp | `bool`
m_bStartActive | `bool`
m_iszEffectName | `CUtlSymbolLarge`
m_iszControlPointNames | `CUtlSymbolLarge[64]`
m_nDataCP | `int32`
m_vecDataCPValue | `Vector`
m_nTintCP | `int32`
m_clrTint | `Color`
m_bOldActive | `bool`
m_bOldFrozen | `bool`

---

## CPulseCell_Outflow_CycleShuffled
Derived from: [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_Outputs | `CUtlVector< CPulse_OutflowConnection >`

---

## C_WeaponSCAR20
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BaseFlex
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flexWeight | `C_NetworkUtlVectorBase< float32 >`
m_vLookTargetPosition | `Vector`
m_blinktoggle | `bool`
m_nLastFlexUpdateFrameCount | `int32`
m_CachedViewTarget | `Vector`
m_nNextSceneEventId | `SceneEventId_t`
m_iBlink | `int32`
m_blinktime | `float32`
m_prevblinktoggle | `bool`
m_iJawOpen | `int32`
m_flJawOpenAmount | `float32`
m_flBlinkAmount | `float32`
m_iMouthAttachment | `AttachmentHandle_t`
m_iEyeAttachment | `AttachmentHandle_t`
m_bResetFlexWeightsOnModelChange | `bool`
m_nEyeOcclusionRendererBone | `int32`
m_mEyeOcclusionRendererCameraToBoneTransform | `matrix3x4_t`
m_vEyeOcclusionRendererHalfExtent | `Vector`
m_PhonemeClasses | `C_BaseFlex::Emphasized_Phoneme[3]`

---

## C_FuncMover
Derived from: [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CLightComponent
Derived from: [CEntityComponent](#centitycomponent)

Name | Type
------------ | -------------
__m_pChainEntity | `CNetworkVarChainer`
m_Color | `Color`
m_SecondaryColor | `Color`
m_flBrightness | `float32`
m_flBrightnessScale | `float32`
m_flBrightnessMult | `float32`
m_flRange | `float32`
m_flFalloff | `float32`
m_flAttenuation0 | `float32`
m_flAttenuation1 | `float32`
m_flAttenuation2 | `float32`
m_flTheta | `float32`
m_flPhi | `float32`
m_hLightCookie | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_nCascades | `int32`
m_nCastShadows | `int32`
m_nShadowWidth | `int32`
m_nShadowHeight | `int32`
m_bRenderDiffuse | `bool`
m_nRenderSpecular | `int32`
m_bRenderTransmissive | `bool`
m_flOrthoLightWidth | `float32`
m_flOrthoLightHeight | `float32`
m_nStyle | `int32`
m_Pattern | `CUtlString`
m_nCascadeRenderStaticObjects | `int32`
m_flShadowCascadeCrossFade | `float32`
m_flShadowCascadeDistanceFade | `float32`
m_flShadowCascadeDistance0 | `float32`
m_flShadowCascadeDistance1 | `float32`
m_flShadowCascadeDistance2 | `float32`
m_flShadowCascadeDistance3 | `float32`
m_nShadowCascadeResolution0 | `int32`
m_nShadowCascadeResolution1 | `int32`
m_nShadowCascadeResolution2 | `int32`
m_nShadowCascadeResolution3 | `int32`
m_bUsesBakedShadowing | `bool`
m_nShadowPriority | `int32`
m_nBakedShadowIndex | `int32`
m_nLightPathUniqueId | `int32`
m_nLightMapUniqueId | `int32`
m_bRenderToCubemaps | `bool`
m_bAllowSSTGeneration | `bool`
m_nDirectLight | `int32`
m_nIndirectLight | `int32`
m_flFadeMinDist | `float32`
m_flFadeMaxDist | `float32`
m_flShadowFadeMinDist | `float32`
m_flShadowFadeMaxDist | `float32`
m_bEnabled | `bool`
m_bFlicker | `bool`
m_bPrecomputedFieldsValid | `bool`
m_vPrecomputedBoundsMins | `Vector`
m_vPrecomputedBoundsMaxs | `Vector`
m_vPrecomputedOBBOrigin | `Vector`
m_vPrecomputedOBBAngles | `QAngle`
m_vPrecomputedOBBExtent | `Vector`
m_flPrecomputedMaxRange | `float32`
m_nFogLightingMode | `int32`
m_flFogContributionStength | `float32`
m_flNearClipPlane | `float32`
m_SkyColor | `Color`
m_flSkyIntensity | `float32`
m_SkyAmbientBounce | `Color`
m_bUseSecondaryColor | `bool`
m_bMixedShadows | `bool`
m_flLightStyleStartTime | `GameTime_t`
m_flCapsuleLength | `float32`
m_flMinRoughness | `float32`

---

## C_DecoyGrenade
Derived from: [C_BaseCSGrenade](#c_basecsgrenade), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WaterBullet
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPlayer_ActionTrackingServices


Name | Type
------------ | -------------
m_hLastWeaponBeforeC4AutoSwitch | `CHandle< C_BasePlayerWeapon >`
m_bIsRescuing | `bool`
m_weaponPurchasesThisMatch | `WeaponPurchaseTracker_t`
m_weaponPurchasesThisRound | `WeaponPurchaseTracker_t`

---

## C_EnvCubemap
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_Entity_hCubemapTexture | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_bCustomCubemapTexture | `bool`
m_Entity_flInfluenceRadius | `float32`
m_Entity_vBoxProjectMins | `Vector`
m_Entity_vBoxProjectMaxs | `Vector`
m_Entity_bMoveable | `bool`
m_Entity_nHandshake | `int32`
m_Entity_nEnvCubeMapArrayIndex | `int32`
m_Entity_nPriority | `int32`
m_Entity_flEdgeFadeDist | `float32`
m_Entity_vEdgeFadeDists | `Vector`
m_Entity_flDiffuseScale | `float32`
m_Entity_bStartDisabled | `bool`
m_Entity_bDefaultEnvMap | `bool`
m_Entity_bDefaultSpecEnvMap | `bool`
m_Entity_bIndoorCubeMap | `bool`
m_Entity_bCopyDiffuseFromDefaultCubemap | `bool`
m_Entity_bEnabled | `bool`

---

## CCSObserver_MovementServices
Derived from: [CPlayer_MovementServices](#cplayer_movementservices)

---

## CBodyComponent
Derived from: [CEntityComponent](#centitycomponent)

Name | Type
------------ | -------------
m_pSceneNode | `CGameSceneNode*`
__m_pChainEntity | `CNetworkVarChainer`

---

## CPulseCell_Inflow_Method
Derived from: [CPulseCell_Inflow_BaseEntrypoint](#cpulsecell_inflow_baseentrypoint), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_MethodName | `PulseSymbol_t`
m_Description | `CUtlString`
m_bIsPublic | `bool`
m_ReturnType | `CPulseValueFullType`
m_Args | `CUtlLeanVector< CPulseRuntimeMethodArg >`

---

## C_BaseCombatCharacter
Derived from: [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_hMyWearables | `C_NetworkUtlVectorBase< CHandle< C_EconWearable > >`
m_leftFootAttachment | `AttachmentHandle_t`
m_rightFootAttachment | `AttachmentHandle_t`
m_nWaterWakeMode | `C_BaseCombatCharacter::WaterWakeMode_t`
m_flWaterWorldZ | `float32`
m_flWaterNextTraceTime | `float32`

---

## CGlowProperty

Name | Type
------------ | -------------
m_fGlowColor | `Vector`
m_iGlowType | `int32`
m_iGlowTeam | `int32`
m_nGlowRange | `int32`
m_nGlowRangeMin | `int32`
m_glowColorOverride | `Color`
m_bFlashing | `bool`
m_flGlowTime | `float32`
m_flGlowStartTime | `float32`
m_bEligibleForScreenHighlight | `bool`
m_bGlowing | `bool`

---

## C_PointClientUIDialog
Derived from: [C_BaseClientUIEntity](#c_baseclientuientity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_hActivator | `CHandle< C_BaseEntity >`
m_bStartEnabled | `bool`

---

## CPulseCell_BaseValue
Derived from: [CPulseCell_Base](#cpulsecell_base)

---

## C_WeaponHKP2000
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_FootstepControl
Derived from: [C_BaseTrigger](#c_basetrigger), [C_BaseToggle](#c_basetoggle), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_source | `CUtlSymbolLarge`
m_destination | `CUtlSymbolLarge`

---

## CCitadelSoundOpvarSetOBB
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_iszStackName | `CUtlSymbolLarge`
m_iszOperatorName | `CUtlSymbolLarge`
m_iszOpvarName | `CUtlSymbolLarge`
m_vDistanceInnerMins | `Vector`
m_vDistanceInnerMaxs | `Vector`
m_vDistanceOuterMins | `Vector`
m_vDistanceOuterMaxs | `Vector`
m_nAABBDirection | `int32`

---

## C_CSGO_EndOfMatchLineupStart
Derived from: [C_CSGO_EndOfMatchLineupEndpoint](#c_csgo_endofmatchlineupendpoint), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPlayer_WaterServices


---

## CPulseCell_BooleanSwitchState
Derived from: [CPulseCell_BaseState](#cpulsecell_basestate), [CPulseCell_BaseYieldingInflow](#cpulsecell_baseyieldinginflow), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_Condition | `PulseObservableBoolExpression_t`
m_SubGraph | `CPulse_OutflowConnection`
m_WhenTrue | `CPulse_OutflowConnection`
m_WhenFalse | `CPulse_OutflowConnection`

---

## CDamageRecord

Name | Type
------------ | -------------
m_PlayerDamager | `CHandle< C_CSPlayerPawn >`
m_PlayerRecipient | `CHandle< C_CSPlayerPawn >`
m_hPlayerControllerDamager | `CHandle< CCSPlayerController >`
m_hPlayerControllerRecipient | `CHandle< CCSPlayerController >`
m_szPlayerDamagerName | `CUtlString`
m_szPlayerRecipientName | `CUtlString`
m_DamagerXuid | `uint64`
m_RecipientXuid | `uint64`
m_iBulletsDamage | `int32`
m_iDamage | `int32`
m_iActualHealthRemoved | `int32`
m_iNumHits | `int32`
m_iLastBulletUpdate | `int32`
m_bIsOtherEnemy | `bool`
m_killType | `EKillTypes_t`

---

## VPhysicsCollisionAttribute_t

Name | Type
------------ | -------------
m_nInteractsAs | `uint64`
m_nInteractsWith | `uint64`
m_nInteractsExclude | `uint64`
m_nEntityId | `uint32`
m_nOwnerId | `uint32`
m_nHierarchyId | `uint16`
m_nCollisionGroup | `uint8`
m_nCollisionFunctionMask | `uint8`

---

## C_DynamicPropAlias_dynamic_prop
Derived from: [C_DynamicProp](#c_dynamicprop), [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CEnvSoundscapeProxyAlias_snd_soundscape_proxy
Derived from: [CEnvSoundscapeProxy](#cenvsoundscapeproxy), [CEnvSoundscape](#cenvsoundscape), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_OmniLight
Derived from: [C_BarnLight](#c_barnlight), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flInnerAngle | `float32`
m_flOuterAngle | `float32`
m_bShowLight | `bool`

---

## C_SceneEntity
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bIsPlayingBack | `bool`
m_bPaused | `bool`
m_bMultiplayer | `bool`
m_bAutogenerated | `bool`
m_flForceClientTime | `float32`
m_nSceneStringIndex | `uint16`
m_bClientOnly | `bool`
m_hOwner | `CHandle< C_BaseFlex >`
m_hActorList | `C_NetworkUtlVectorBase< CHandle< C_BaseFlex > >`
m_bWasPlaying | `bool`
m_QueuedEvents | `CUtlVector< C_SceneEntity::QueuedEvents_t >`
m_flCurrentTime | `float32`

---

## CPulseCell_Inflow_Yield
Derived from: [CPulseCell_BaseYieldingInflow](#cpulsecell_baseyieldinginflow), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_UnyieldResume | `CPulse_ResumePoint`

---

## CPulseMathlib

---

## C_NametagModule
Derived from: [C_CS2WeaponModuleBase](#c_cs2weaponmodulebase), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_strNametagString | `CUtlString`

---

## C_EconEntity
Derived from: [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flFlexDelayTime | `float32`
m_flFlexDelayedWeight | `float32*`
m_bAttributesInitialized | `bool`
m_AttributeManager | `C_AttributeContainer`
m_OriginalOwnerXuidLow | `uint32`
m_OriginalOwnerXuidHigh | `uint32`
m_nFallbackPaintKit | `int32`
m_nFallbackSeed | `int32`
m_flFallbackWear | `float32`
m_nFallbackStatTrak | `int32`
m_bClientside | `bool`
m_bParticleSystemsCreated | `bool`
m_vecAttachedParticles | `CUtlVector< int32 >`
m_hViewmodelAttachment | `CHandle< CBaseAnimGraph >`
m_iOldTeam | `int32`
m_bAttachmentDirty | `bool`
m_nUnloadedModelIndex | `int32`
m_iNumOwnerValidationRetries | `int32`
m_hOldProvidee | `CHandle< C_BaseEntity >`
m_vecAttachedModels | `CUtlVector< C_EconEntity::AttachedModelData_t >`

---

## CPlayer_UseServices


---

## C_PointValueRemapper
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bDisabled | `bool`
m_bDisabledOld | `bool`
m_bUpdateOnClient | `bool`
m_nInputType | `ValueRemapperInputType_t`
m_hRemapLineStart | `CHandle< C_BaseEntity >`
m_hRemapLineEnd | `CHandle< C_BaseEntity >`
m_flMaximumChangePerSecond | `float32`
m_flDisengageDistance | `float32`
m_flEngageDistance | `float32`
m_bRequiresUseKey | `bool`
m_nOutputType | `ValueRemapperOutputType_t`
m_hOutputEntities | `C_NetworkUtlVectorBase< CHandle< C_BaseEntity > >`
m_nHapticsType | `ValueRemapperHapticsType_t`
m_nMomentumType | `ValueRemapperMomentumType_t`
m_flMomentumModifier | `float32`
m_flSnapValue | `float32`
m_flCurrentMomentum | `float32`
m_nRatchetType | `ValueRemapperRatchetType_t`
m_flRatchetOffset | `float32`
m_flInputOffset | `float32`
m_bEngaged | `bool`
m_bFirstUpdate | `bool`
m_flPreviousValue | `float32`
m_flPreviousUpdateTickTime | `GameTime_t`
m_vecPreviousTestPoint | `Vector`

---

## CGameSceneNodeHandle

Name | Type
------------ | -------------
m_hOwner | `CEntityHandle`
m_name | `CUtlStringToken`

---

## CPulseCell_Unknown
Derived from: [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_UnknownKeys | `KeyValues3`

---

## C_WeaponMP7
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CSPerRoundStats_t

Name | Type
------------ | -------------
m_iKills | `int32`
m_iDeaths | `int32`
m_iAssists | `int32`
m_iDamage | `int32`
m_iEquipmentValue | `int32`
m_iMoneySaved | `int32`
m_iKillReward | `int32`
m_iLiveTime | `int32`
m_iHeadShotKills | `int32`
m_iObjective | `int32`
m_iCashEarned | `int32`
m_iUtilityDamage | `int32`
m_iEnemiesFlashed | `int32`

---

## CPulseCell_Outflow_CycleRandom
Derived from: [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_Outputs | `CUtlVector< CPulse_OutflowConnection >`

---

## CPulseCell_Step_PublicOutput
Derived from: [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_OutputIndex | `PulseRuntimeOutputIndex_t`

---

## C_CS2HudModelBase
Derived from: [C_LateUpdatedAnimating](#c_lateupdatedanimating), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CDestructiblePartsSystemComponent

Name | Type
------------ | -------------
__m_pChainEntity | `CNetworkVarChainer`
m_DamageLevelTakenByHitGroup | `C_NetworkUtlVectorBase< uint16 >`
m_hOwner | `CHandle< C_BaseModelEntity >`
m_nLastHitDamageLevel | `int32`

---

## C_CSGameRules
Derived from: [C_TeamplayRules](#c_teamplayrules), [C_MultiplayRules](#c_multiplayrules), [C_GameRules](#c_gamerules)

Name | Type
------------ | -------------
m_bFreezePeriod | `bool`
m_bWarmupPeriod | `bool`
m_fWarmupPeriodEnd | `GameTime_t`
m_fWarmupPeriodStart | `GameTime_t`
m_bTerroristTimeOutActive | `bool`
m_bCTTimeOutActive | `bool`
m_flTerroristTimeOutRemaining | `float32`
m_flCTTimeOutRemaining | `float32`
m_nTerroristTimeOuts | `int32`
m_nCTTimeOuts | `int32`
m_bTechnicalTimeOut | `bool`
m_bMatchWaitingForResume | `bool`
m_iRoundTime | `int32`
m_fMatchStartTime | `float32`
m_fRoundStartTime | `GameTime_t`
m_flRestartRoundTime | `GameTime_t`
m_bGameRestart | `bool`
m_flGameStartTime | `float32`
m_timeUntilNextPhaseStarts | `float32`
m_gamePhase | `int32`
m_totalRoundsPlayed | `int32`
m_nRoundsPlayedThisPhase | `int32`
m_nOvertimePlaying | `int32`
m_iHostagesRemaining | `int32`
m_bAnyHostageReached | `bool`
m_bMapHasBombTarget | `bool`
m_bMapHasRescueZone | `bool`
m_bMapHasBuyZone | `bool`
m_bIsQueuedMatchmaking | `bool`
m_nQueuedMatchmakingMode | `int32`
m_bIsValveDS | `bool`
m_bLogoMap | `bool`
m_bPlayAllStepSoundsOnServer | `bool`
m_iSpectatorSlotCount | `int32`
m_MatchDevice | `int32`
m_bHasMatchStarted | `bool`
m_nNextMapInMapgroup | `int32`
m_szTournamentEventName | `char[512]`
m_szTournamentEventStage | `char[512]`
m_szMatchStatTxt | `char[512]`
m_szTournamentPredictionsTxt | `char[512]`
m_nTournamentPredictionsPct | `int32`
m_flCMMItemDropRevealStartTime | `GameTime_t`
m_flCMMItemDropRevealEndTime | `GameTime_t`
m_bIsDroppingItems | `bool`
m_bIsQuestEligible | `bool`
m_bIsHltvActive | `bool`
m_arrProhibitedItemIndices | `uint16[100]`
m_arrTournamentActiveCasterAccounts | `uint32[4]`
m_numBestOfMaps | `int32`
m_nHalloweenMaskListSeed | `int32`
m_bBombDropped | `bool`
m_bBombPlanted | `bool`
m_iRoundWinStatus | `int32`
m_eRoundWinReason | `int32`
m_bTCantBuy | `bool`
m_bCTCantBuy | `bool`
m_iMatchStats_RoundResults | `int32[30]`
m_iMatchStats_PlayersAlive_CT | `int32[30]`
m_iMatchStats_PlayersAlive_T | `int32[30]`
m_TeamRespawnWaveTimes | `float32[32]`
m_flNextRespawnWave | `GameTime_t[32]`
m_vMinimapMins | `Vector`
m_vMinimapMaxs | `Vector`
m_MinimapVerticalSectionHeights | `float32[8]`
m_ullLocalMatchID | `uint64`
m_nEndMatchMapGroupVoteTypes | `int32[10]`
m_nEndMatchMapGroupVoteOptions | `int32[10]`
m_nEndMatchMapVoteWinner | `int32`
m_iNumConsecutiveCTLoses | `int32`
m_iNumConsecutiveTerroristLoses | `int32`
m_bMarkClientStopRecordAtRoundEnd | `bool`
m_nMatchAbortedEarlyReason | `int32`
m_bHasTriggeredRoundStartMusic | `bool`
m_bSwitchingTeamsAtRoundReset | `bool`
m_pGameModeRules | `CCSGameModeRules*`
m_RetakeRules | `C_RetakeGameRules`
m_nMatchEndCount | `uint8`
m_nTTeamIntroVariant | `int32`
m_nCTTeamIntroVariant | `int32`
m_bTeamIntroPeriod | `bool`
m_iRoundEndWinnerTeam | `int32`
m_eRoundEndReason | `int32`
m_bRoundEndShowTimerDefend | `bool`
m_iRoundEndTimerTime | `int32`
m_sRoundEndFunFactToken | `CUtlString`
m_iRoundEndFunFactPlayerSlot | `CPlayerSlot`
m_iRoundEndFunFactData1 | `int32`
m_iRoundEndFunFactData2 | `int32`
m_iRoundEndFunFactData3 | `int32`
m_sRoundEndMessage | `CUtlString`
m_iRoundEndPlayerCount | `int32`
m_bRoundEndNoMusic | `bool`
m_iRoundEndLegacy | `int32`
m_nRoundEndCount | `uint8`
m_iRoundStartRoundNumber | `int32`
m_nRoundStartCount | `uint8`
m_flLastPerfSampleTime | `float64`

---

## CGrenadeTracer
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flTracerDuration | `float32`
m_nType | `GrenadeType_t`

---

## CCSGameModeRules_Noop
Derived from: [CCSGameModeRules](#ccsgamemoderules)

---

## CPulse_BlackboardReference

Name | Type
------------ | -------------
m_hBlackboardResource | `CStrongHandle< InfoForResourceTypeIPulseGraphDef >`
m_BlackboardResource | `PulseSymbol_t`
m_nNodeID | `PulseDocNodeID_t`
m_NodeName | `CGlobalSymbol`

---

## C_BaseCSGrenadeProjectile
Derived from: [C_BaseGrenade](#c_basegrenade), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_vInitialPosition | `Vector`
m_vInitialVelocity | `Vector`
m_nBounces | `int32`
m_nExplodeEffectIndex | `CStrongHandle< InfoForResourceTypeIParticleSystemDefinition >`
m_nExplodeEffectTickBegin | `int32`
m_vecExplodeEffectOrigin | `Vector`
m_flSpawnTime | `GameTime_t`
vecLastTrailLinePos | `Vector`
flNextTrailLineTime | `GameTime_t`
m_bExplodeEffectBegan | `bool`
m_bCanCreateGrenadeTrail | `bool`
m_nSnapshotTrajectoryEffectIndex | `ParticleIndex_t`
m_hSnapshotTrajectoryParticleSnapshot | `CStrongHandle< InfoForResourceTypeIParticleSnapshot >`
m_arrTrajectoryTrailPoints | `CUtlVector< Vector >`
m_arrTrajectoryTrailPointCreationTimes | `CUtlVector< float32 >`
m_flTrajectoryTrailEffectCreationTime | `float32`

---

## C_GradientFog
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_hGradientFogTexture | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_flFogStartDistance | `float32`
m_flFogEndDistance | `float32`
m_bHeightFogEnabled | `bool`
m_flFogStartHeight | `float32`
m_flFogEndHeight | `float32`
m_flFarZ | `float32`
m_flFogMaxOpacity | `float32`
m_flFogFalloffExponent | `float32`
m_flFogVerticalExponent | `float32`
m_fogColor | `Color`
m_flFogStrength | `float32`
m_flFadeTime | `float32`
m_bStartDisabled | `bool`
m_bIsEnabled | `bool`
m_bGradientFogNeedsTextures | `bool`

---

## CCSPlayerController_InGameMoneyServices


Name | Type
------------ | -------------
m_iAccount | `int32`
m_iStartAccount | `int32`
m_iTotalCashSpent | `int32`
m_iCashSpentThisRound | `int32`

---

## C_HEGrenadeProjectile
Derived from: [C_BaseCSGrenadeProjectile](#c_basecsgrenadeprojectile), [C_BaseGrenade](#c_basegrenade), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CAnimGraphNetworkedVariables

Name | Type
------------ | -------------
m_PredNetBoolVariables | `C_NetworkUtlVectorBase< uint32 >`
m_PredNetByteVariables | `C_NetworkUtlVectorBase< uint8 >`
m_PredNetUInt16Variables | `C_NetworkUtlVectorBase< uint16 >`
m_PredNetIntVariables | `C_NetworkUtlVectorBase< int32 >`
m_PredNetUInt32Variables | `C_NetworkUtlVectorBase< uint32 >`
m_PredNetUInt64Variables | `C_NetworkUtlVectorBase< uint64 >`
m_PredNetFloatVariables | `C_NetworkUtlVectorBase< float32 >`
m_PredNetVectorVariables | `C_NetworkUtlVectorBase< Vector >`
m_PredNetQuaternionVariables | `C_NetworkUtlVectorBase< Quaternion >`
m_PredNetGlobalSymbolVariables | `C_NetworkUtlVectorBase< CGlobalSymbol >`
m_OwnerOnlyPredNetBoolVariables | `C_NetworkUtlVectorBase< uint32 >`
m_OwnerOnlyPredNetByteVariables | `C_NetworkUtlVectorBase< uint8 >`
m_OwnerOnlyPredNetUInt16Variables | `C_NetworkUtlVectorBase< uint16 >`
m_OwnerOnlyPredNetIntVariables | `C_NetworkUtlVectorBase< int32 >`
m_OwnerOnlyPredNetUInt32Variables | `C_NetworkUtlVectorBase< uint32 >`
m_OwnerOnlyPredNetUInt64Variables | `C_NetworkUtlVectorBase< uint64 >`
m_OwnerOnlyPredNetFloatVariables | `C_NetworkUtlVectorBase< float32 >`
m_OwnerOnlyPredNetVectorVariables | `C_NetworkUtlVectorBase< Vector >`
m_OwnerOnlyPredNetQuaternionVariables | `C_NetworkUtlVectorBase< Quaternion >`
m_OwnerOnlyPredNetGlobalSymbolVariables | `C_NetworkUtlVectorBase< CGlobalSymbol >`
m_nBoolVariablesCount | `int32`
m_nOwnerOnlyBoolVariablesCount | `int32`
m_nRandomSeedOffset | `int32`
m_flLastTeleportTime | `float32`

---

## CFilterModel
Derived from: [CBaseFilter](#cbasefilter), [CLogicalEntity](#clogicalentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_iFilterModel | `CUtlSymbolLarge`

---

## C_SoundAreaEntityOrientedBox
Derived from: [C_SoundAreaEntityBase](#c_soundareaentitybase), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_vMin | `Vector`
m_vMax | `Vector`

---

## C_SoundOpvarSetPointEntity
Derived from: [C_SoundOpvarSetPointBase](#c_soundopvarsetpointbase), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPulseCell_Value_RandomInt
Derived from: [CPulseCell_BaseValue](#cpulsecell_basevalue), [CPulseCell_Base](#cpulsecell_base)

---

## C_RagdollPropAttached
Derived from: [C_RagdollProp](#c_ragdollprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_boneIndexAttached | `uint32`
m_ragdollAttachedObjectIndex | `uint32`
m_attachmentPointBoneSpace | `Vector`
m_attachmentPointRagdollSpace | `Vector`
m_vecOffset | `Vector`
m_parentTime | `float32`
m_bHasParent | `bool`

---

## C_ModelPointEntity
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_PreviewPlayer
Derived from: [C_CSPlayerPawn](#c_csplayerpawn), [C_CSPlayerPawnBase](#c_csplayerpawnbase), [C_BasePlayerPawn](#c_baseplayerpawn), [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_animgraph | `CUtlString`
m_animgraphCharacterModeString | `CGlobalSymbol`
m_flInitialModelScale | `float32`

---

## C_RectLight
Derived from: [C_BarnLight](#c_barnlight), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bShowLight | `bool`

---

## CPathSimple
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_CPathQueryComponent | `CPathQueryComponent`
m_pathString | `CUtlString`
m_bClosedLoop | `bool`

---

## CPulseCell_Outflow_IntSwitch
Derived from: [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_DefaultCaseOutflow | `CPulse_OutflowConnection`
m_CaseOutflows | `CUtlVector< CPulse_OutflowConnection >`

---

## C_FuncTrackTrain
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_nLongAxis | `int32`
m_flRadius | `float32`
m_flLineLength | `float32`

---

## CCSPointScriptExtensions_CCSWeaponBaseVData

---

## C_EconWearable
Derived from: [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_nForceSkin | `int32`
m_bAlwaysAllow | `bool`

---

## C_EnvDecal
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_hDecalMaterial | `CStrongHandle< InfoForResourceTypeIMaterial2 >`
m_flWidth | `float32`
m_flHeight | `float32`
m_flDepth | `float32`
m_nRenderOrder | `uint32`
m_bProjectOnWorld | `bool`
m_bProjectOnCharacters | `bool`
m_bProjectOnWater | `bool`
m_flDepthSortBias | `float32`

---

## EntitySpottedState_t

Name | Type
------------ | -------------
m_bSpotted | `bool`
m_bSpottedByMask | `uint32[2]`

---

## fogparams_t

Name | Type
------------ | -------------
dirPrimary | `Vector`
colorPrimary | `Color`
colorSecondary | `Color`
colorPrimaryLerpTo | `Color`
colorSecondaryLerpTo | `Color`
start | `float32`
end | `float32`
farz | `float32`
maxdensity | `float32`
exponent | `float32`
HDRColorScale | `float32`
skyboxFogFactor | `float32`
skyboxFogFactorLerpTo | `float32`
startLerpTo | `float32`
endLerpTo | `float32`
maxdensityLerpTo | `float32`
lerptime | `GameTime_t`
duration | `float32`
blendtobackground | `float32`
scattering | `float32`
locallightscale | `float32`
enable | `bool`
blend | `bool`
m_bPadding2 | `bool`
m_bPadding | `bool`

---

## C_WeaponM4A1
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_Item
Derived from: [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_pReticleHintTextName | `char[256]`

---

## C_EnvProjectedTexture
Derived from: [C_ModelPointEntity](#c_modelpointentity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSPetPlacement
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_Beam
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flFrameRate | `float32`
m_flHDRColorScale | `float32`
m_flFireTime | `GameTime_t`
m_flDamage | `float32`
m_nNumBeamEnts | `uint8`
m_queryHandleHalo | `int32`
m_hBaseMaterial | `CStrongHandle< InfoForResourceTypeIMaterial2 >`
m_nHaloIndex | `CStrongHandle< InfoForResourceTypeIMaterial2 >`
m_nBeamType | `BeamType_t`
m_nBeamFlags | `uint32`
m_hAttachEntity | `CHandle< C_BaseEntity >[10]`
m_nAttachIndex | `AttachmentHandle_t[10]`
m_fWidth | `float32`
m_fEndWidth | `float32`
m_fFadeLength | `float32`
m_fHaloScale | `float32`
m_fAmplitude | `float32`
m_fStartFrame | `float32`
m_fSpeed | `float32`
m_flFrame | `float32`
m_nClipStyle | `BeamClipStyle_t`
m_bTurnedOff | `bool`
m_vecEndPos | `Vector`
m_hEndEntity | `CHandle< C_BaseEntity >`

---

## C_EnvLightProbeVolume
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_Entity_hLightProbeTexture_AmbientCube | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_hLightProbeTexture_SDF | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_hLightProbeTexture_SH2_DC | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_hLightProbeTexture_SH2_R | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_hLightProbeTexture_SH2_G | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_hLightProbeTexture_SH2_B | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_hLightProbeDirectLightIndicesTexture | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_hLightProbeDirectLightScalarsTexture | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_hLightProbeDirectLightShadowsTexture | `CStrongHandle< InfoForResourceTypeCTextureBase >`
m_Entity_vBoxMins | `Vector`
m_Entity_vBoxMaxs | `Vector`
m_Entity_bMoveable | `bool`
m_Entity_nHandshake | `int32`
m_Entity_nPriority | `int32`
m_Entity_bStartDisabled | `bool`
m_Entity_nLightProbeSizeX | `int32`
m_Entity_nLightProbeSizeY | `int32`
m_Entity_nLightProbeSizeZ | `int32`
m_Entity_nLightProbeAtlasX | `int32`
m_Entity_nLightProbeAtlasY | `int32`
m_Entity_nLightProbeAtlasZ | `int32`
m_Entity_bEnabled | `bool`

---

## C_FuncConveyor
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_vecMoveDirEntitySpace | `Vector`
m_flTargetSpeed | `float32`
m_nTransitionStartTick | `GameTick_t`
m_nTransitionDurationTicks | `int32`
m_flTransitionStartSpeed | `float32`
m_hConveyorModels | `C_NetworkUtlVectorBase< CHandle< C_BaseEntity > >`
m_flCurrentConveyorOffset | `float32`
m_flCurrentConveyorSpeed | `float32`

---

## CCSPlayer_WeaponServices
Derived from: [CPlayer_WeaponServices](#cplayer_weaponservices)

Name | Type
------------ | -------------
m_flNextAttack | `GameTime_t`
m_bIsLookingAtWeapon | `bool`
m_bIsHoldingLookAtWeapon | `bool`
m_nOldTotalShootPositionHistoryCount | `uint32`
m_nOldTotalInputHistoryCount | `uint32`
m_networkAnimTiming | `C_NetworkUtlVectorBase< uint8 >`
m_bBlockInspectUntilNextGraphUpdate | `bool`

---

## C_PhysMagnet
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_aAttachedObjectsFromServer | `CUtlVector< int32 >`
m_aAttachedObjects | `CUtlVector< CHandle< C_BaseEntity > >`

---

## CEnvSoundscapeTriggerableAlias_snd_soundscape_triggerable
Derived from: [CEnvSoundscapeTriggerable](#cenvsoundscapetriggerable), [CEnvSoundscape](#cenvsoundscape), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_Breakable
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_PlantedC4
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bBombTicking | `bool`
m_nBombSite | `int32`
m_nSourceSoundscapeHash | `int32`
m_entitySpottedState | `EntitySpottedState_t`
m_flNextGlow | `GameTime_t`
m_flNextBeep | `GameTime_t`
m_flC4Blow | `GameTime_t`
m_bCannotBeDefused | `bool`
m_bHasExploded | `bool`
m_flTimerLength | `float32`
m_bBeingDefused | `bool`
m_bTriggerWarning | `float32`
m_bExplodeWarning | `float32`
m_bC4Activated | `bool`
m_bTenSecWarning | `bool`
m_flDefuseLength | `float32`
m_flDefuseCountDown | `GameTime_t`
m_bBombDefused | `bool`
m_hBombDefuser | `CHandle< C_CSPlayerPawn >`
m_AttributeManager | `C_AttributeContainer`
m_hDefuserMultimeter | `CHandle< C_Multimeter >`
m_flNextRadarFlashTime | `GameTime_t`
m_bRadarFlash | `bool`
m_pBombDefuser | `CHandle< C_CSPlayerPawn >`
m_fLastDefuseTime | `GameTime_t`
m_pPredictionOwner | `CBasePlayerController*`
m_vecC4ExplodeSpectatePos | `Vector`
m_vecC4ExplodeSpectateAng | `QAngle`
m_flC4ExplodeSpectateDuration | `float32`

---

## CCSGO_WingmanIntroCharacterPosition
Derived from: [C_CSGO_TeamIntroCharacterPosition](#c_csgo_teamintrocharacterposition), [C_CSGO_TeamPreviewCharacterPosition](#c_csgo_teampreviewcharacterposition), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CFilterName
Derived from: [CBaseFilter](#cbasefilter), [CLogicalEntity](#clogicalentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_iFilterName | `CUtlSymbolLarge`

---

## C_RagdollProp
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_ragEnabled | `C_NetworkUtlVectorBase< bool >`
m_ragPos | `C_NetworkUtlVectorBase< Vector >`
m_ragAngles | `C_NetworkUtlVectorBase< QAngle >`
m_flBlendWeight | `float32`
m_hRagdollSource | `CHandle< C_BaseEntity >`
m_iEyeAttachment | `AttachmentHandle_t`
m_flBlendWeightCurrent | `float32`
m_parentPhysicsBoneIndices | `CUtlVector< int32 >`
m_worldSpaceBoneComputationOrder | `CUtlVector< int32 >`

---

## CPulse_CallInfo

Name | Type
------------ | -------------
m_PortName | `PulseSymbol_t`
m_nEditorNodeID | `PulseDocNodeID_t`
m_RegisterMap | `PulseRegisterMap_t`
m_CallMethodID | `PulseDocNodeID_t`
m_nSrcChunk | `PulseRuntimeChunkIndex_t`
m_nSrcInstruction | `int32`

---

## C_MapPreviewParticleSystem
Derived from: [C_ParticleSystem](#c_particlesystem), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CBaseAnimGraph
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bInitiallyPopulateInterpHistory | `bool`
m_bSuppressAnimEventSounds | `bool`
m_bAnimGraphUpdateEnabled | `bool`
m_flMaxSlopeDistance | `float32`
m_vLastSlopeCheckPos | `Vector`
m_bAnimationUpdateScheduled | `bool`
m_vecForce | `Vector`
m_nForceBone | `int32`
m_pClientsideRagdoll | `CBaseAnimGraph*`
m_bBuiltRagdoll | `bool`
m_RagdollPose | `PhysicsRagdollPose_t`
m_bRagdollEnabled | `bool`
m_bRagdollClientSide | `bool`
m_bHasAnimatedMaterialAttributes | `bool`

---

## CPulseCell_InlineNodeSkipSelector
Derived from: [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_nFlowNodeID | `PulseDocNodeID_t`
m_bAnd | `bool`
m_PassOutflow | `PulseSelectorOutflowList_t`
m_FailOutflow | `CPulse_OutflowConnection`

---

## C_LightEntity
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_CLightComponent | `CLightComponent*`

---

## C_WeaponM249
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_LocalTempEntity
Derived from: [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
flags | `int32`
die | `GameTime_t`
m_flFrameMax | `float32`
x | `float32`
y | `float32`
fadeSpeed | `float32`
bounceFactor | `float32`
hitSound | `int32`
priority | `int32`
tentOffset | `Vector`
m_vecTempEntAngVelocity | `QAngle`
tempent_renderamt | `int32`
m_vecNormal | `Vector`
m_flSpriteScale | `float32`
m_nFlickerFrame | `int32`
m_flFrameRate | `float32`
m_flFrame | `float32`
m_pszImpactEffect | `char*`
m_pszParticleEffect | `char*`
m_bParticleCollision | `bool`
m_iLastCollisionFrame | `int32`
m_vLastCollisionOrigin | `Vector`
m_vecTempEntVelocity | `Vector`
m_vecPrevAbsOrigin | `Vector`
m_vecTempEntAcceleration | `Vector`

---

## C_WeaponTaser
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_fFireTime | `GameTime_t`
m_nLastAttackTick | `int32`

---

## C_PointEntity
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_SingleplayRules
Derived from: [C_GameRules](#c_gamerules)

---

## CLogicalEntity
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_PrecipitationBlocker
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_CounterTerroristTeamIntroCamera
Derived from: [C_CSGO_TeamPreviewCamera](#c_csgo_teampreviewcamera), [C_CSGO_MapPreviewCameraPath](#c_csgo_mappreviewcamerapath), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_SoundOpvarSetPathCornerEntity
Derived from: [C_SoundOpvarSetPointEntity](#c_soundopvarsetpointentity), [C_SoundOpvarSetPointBase](#c_soundopvarsetpointbase), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPlayer_WeaponServices


Name | Type
------------ | -------------
m_hMyWeapons | `C_NetworkUtlVectorBase< CHandle< C_BasePlayerWeapon > >`
m_hActiveWeapon | `CHandle< C_BasePlayerWeapon >`
m_hLastWeapon | `CHandle< C_BasePlayerWeapon >`
m_iAmmo | `uint16[32]`

---

## C_WeaponNegev
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WeaponFiveSeven
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_WeaponSawedoff
Derived from: [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_TriggerVolume
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CPulseCell_LimitCount
Derived from: [CPulseCell_BaseRequirement](#cpulsecell_baserequirement), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_nLimitCount | `int32`

---

## CPulseCell_Step_CallExternalMethod
Derived from: [CPulseCell_BaseYieldingInflow](#cpulsecell_baseyieldinginflow), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_MethodName | `PulseSymbol_t`
m_GameBlackboard | `PulseSymbol_t`
m_ExpectedArgs | `CUtlLeanVector< CPulseRuntimeMethodArg >`
m_nAsyncCallMode | `PulseMethodCallMode_t`
m_OnFinished | `CPulse_ResumePoint`

---

## C_WeaponMP9
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_DynamicPropAlias_prop_dynamic_override
Derived from: [C_DynamicProp](#c_dynamicprop), [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CEnvSoundscapeTriggerable
Derived from: [CEnvSoundscape](#cenvsoundscape), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_PlayerPing
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_hPlayer | `CHandle< C_CSPlayerPawn >`
m_hPingedEntity | `CHandle< C_BaseEntity >`
m_iType | `int32`
m_bUrgent | `bool`
m_szPlaceName | `char[18]`

---

## C_AK47
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_MapPreviewCameraPathNode
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_szParentPathUniqueID | `CUtlSymbolLarge`
m_nPathIndex | `int32`
m_vInTangentLocal | `Vector`
m_vOutTangentLocal | `Vector`
m_flFOV | `float32`
m_flCameraSpeed | `float32`
m_flEaseIn | `float32`
m_flEaseOut | `float32`
m_vInTangentWorld | `Vector`
m_vOutTangentWorld | `Vector`

---

## C_CSPlayerResource
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bHostageAlive | `bool[12]`
m_isHostageFollowingSomeone | `bool[12]`
m_iHostageEntityIDs | `CEntityIndex[12]`
m_bombsiteCenterA | `Vector`
m_bombsiteCenterB | `Vector`
m_hostageRescueX | `int32[4]`
m_hostageRescueY | `int32[4]`
m_hostageRescueZ | `int32[4]`
m_bEndMatchNextMapAllVoted | `bool`
m_foundGoalPositions | `bool`

---

## CSkyboxReference
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_worldGroupId | `WorldGroupId_t`
m_hSkyCamera | `CHandle< C_SkyCamera >`

---

## C_IncendiaryGrenade
Derived from: [C_MolotovGrenade](#c_molotovgrenade), [C_BaseCSGrenade](#c_basecsgrenade), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CFilterClass
Derived from: [CBaseFilter](#cbasefilter), [CLogicalEntity](#clogicalentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_iFilterClass | `CUtlSymbolLarge`

---

## C_PointCameraVFOV
Derived from: [C_PointCamera](#c_pointcamera), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_flVerticalFOV | `float32`

---

## C_PointCamera
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_FOV | `float32`
m_Resolution | `float32`
m_bFogEnable | `bool`
m_FogColor | `Color`
m_flFogStart | `float32`
m_flFogEnd | `float32`
m_flFogMaxDensity | `float32`
m_bActive | `bool`
m_bUseScreenAspectRatio | `bool`
m_flAspectRatio | `float32`
m_bNoSky | `bool`
m_fBrightness | `float32`
m_flZFar | `float32`
m_flZNear | `float32`
m_bCanHLTVUse | `bool`
m_bAlignWithParent | `bool`
m_bDofEnabled | `bool`
m_flDofNearBlurry | `float32`
m_flDofNearCrisp | `float32`
m_flDofFarCrisp | `float32`
m_flDofFarBlurry | `float32`
m_flDofTiltToGround | `float32`
m_TargetFOV | `float32`
m_DegreesPerSecond | `float32`
m_bIsOn | `bool`
m_pNext | `C_PointCamera*`

---

## CBaseFilter
Derived from: [CLogicalEntity](#clogicalentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bNegated | `bool`
m_OnPass | `CEntityIOOutput`
m_OnFail | `CEntityIOOutput`

---

## WeaponPurchaseTracker_t

Name | Type
------------ | -------------
m_weaponPurchases | `C_UtlVectorEmbeddedNetworkVar< WeaponPurchaseCount_t >`

---

## PulseObservableBoolExpression_t

Name | Type
------------ | -------------
m_EvaluateConnection | `CPulse_OutflowConnection`
m_DependentObservableVars | `CUtlVector< PulseRuntimeVarIndex_t >`
m_DependentObservableBlackboardReferences | `CUtlVector< PulseRuntimeBlackboardReferenceIndex_t >`

---

## CMapInfo
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_iBuyingStatus | `int32`
m_flBombRadius | `float32`
m_iPetPopulation | `int32`
m_bUseNormalSpawnsForDM | `bool`
m_bDisableAutoGeneratedDMSpawns | `bool`
m_flBotMaxVisionDistance | `float32`
m_iHostageCount | `int32`
m_bFadePlayerVisibilityFarZ | `bool`
m_bRainTraceToSkyEnabled | `bool`

---

## C_CSGO_EndOfMatchCamera
Derived from: [C_CSGO_TeamPreviewCamera](#c_csgo_teampreviewcamera), [C_CSGO_MapPreviewCameraPath](#c_csgo_mappreviewcamerapath), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_BaseGrenade
Derived from: [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bHasWarnedAI | `bool`
m_bIsSmokeGrenade | `bool`
m_bIsLive | `bool`
m_DmgRadius | `float32`
m_flDetonateTime | `GameTime_t`
m_flWarnAITime | `float32`
m_flDamage | `float32`
m_iszBounceSound | `CUtlSymbolLarge`
m_ExplosionSound | `CUtlString`
m_hThrower | `CHandle< C_CSPlayerPawn >`
m_flNextAttack | `GameTime_t`
m_hOriginalThrower | `CHandle< C_CSPlayerPawn >`

---

## C_PlayerSprayDecal
Derived from: [C_ModelPointEntity](#c_modelpointentity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_nUniqueID | `int32`
m_unAccountID | `uint32`
m_unTraceID | `uint32`
m_rtGcTime | `uint32`
m_vecEndPos | `Vector`
m_vecStart | `Vector`
m_vecLeft | `Vector`
m_vecNormal | `Vector`
m_nPlayer | `int32`
m_nEntity | `int32`
m_nHitbox | `int32`
m_flCreationTime | `float32`
m_nTintID | `int32`
m_nVersion | `uint8`
m_ubSignature | `uint8[128]`
m_SprayRenderHelper | `CPlayerSprayDecalRenderHelper`

---

## CEntityIdentity

Name | Type
------------ | -------------
m_nameStringableIndex | `int32`
m_name | `CUtlSymbolLarge`
m_designerName | `CUtlSymbolLarge`
m_flags | `uint32`
m_worldGroupId | `WorldGroupId_t`
m_fDataObjectTypes | `uint32`
m_PathIndex | `ChangeAccessorFieldPathIndex_t`
m_pPrev | `CEntityIdentity*`
m_pNext | `CEntityIdentity*`
m_pPrevByClass | `CEntityIdentity*`
m_pNextByClass | `CEntityIdentity*`

---

## CPulseCell_LimitCount::Criteria_t

Name | Type
------------ | -------------
m_bLimitCountPasses | `bool`

---

## C_CS2HudModelArms
Derived from: [C_CS2HudModelBase](#c_cs2hudmodelbase), [C_LateUpdatedAnimating](#c_lateupdatedanimating), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CBasePlayerVData


Name | Type
------------ | -------------
m_sModelName | `CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >`
m_flHeadDamageMultiplier | `CSkillFloat`
m_flChestDamageMultiplier | `CSkillFloat`
m_flStomachDamageMultiplier | `CSkillFloat`
m_flArmDamageMultiplier | `CSkillFloat`
m_flLegDamageMultiplier | `CSkillFloat`
m_flHoldBreathTime | `float32`
m_flDrowningDamageInterval | `float32`
m_nDrowningDamageInitial | `int32`
m_nDrowningDamageMax | `int32`
m_nWaterSpeed | `int32`
m_flUseRange | `float32`
m_flUseAngleTolerance | `float32`
m_flCrouchTime | `float32`

---

## C_LightSpotEntity
Derived from: [C_LightEntity](#c_lightentity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSGameModeRules_Deathmatch
Derived from: [CCSGameModeRules](#ccsgamemoderules)

Name | Type
------------ | -------------
m_flDMBonusStartTime | `GameTime_t`
m_flDMBonusTimeLength | `float32`
m_sDMBonusWeapon | `CUtlString`

---

## CPulseCell_CursorQueue
Derived from: [CPulseCell_WaitForCursorsWithTagBase](#cpulsecell_waitforcursorswithtagbase), [CPulseCell_BaseYieldingInflow](#cpulsecell_baseyieldinginflow), [CPulseCell_BaseFlow](#cpulsecell_baseflow), [CPulseCell_Base](#cpulsecell_base)

Name | Type
------------ | -------------
m_nCursorsAllowedToRunParallel | `int32`

---

## CPulseCell_Value_RandomFloat
Derived from: [CPulseCell_BaseValue](#cpulsecell_basevalue), [CPulseCell_Base](#cpulsecell_base)

---

## CPulseExecCursor

---

## C_Sprite
Derived from: [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_hSpriteMaterial | `CStrongHandle< InfoForResourceTypeIMaterial2 >`
m_hAttachedToEntity | `CHandle< C_BaseEntity >`
m_nAttachment | `AttachmentHandle_t`
m_flSpriteFramerate | `float32`
m_flFrame | `float32`
m_flDieTime | `GameTime_t`
m_nBrightness | `uint32`
m_flBrightnessDuration | `float32`
m_flSpriteScale | `float32`
m_flScaleDuration | `float32`
m_bWorldSpaceScale | `bool`
m_flGlowProxySize | `float32`
m_flHDRColorScale | `float32`
m_flLastTime | `GameTime_t`
m_flMaxFrame | `float32`
m_flStartScale | `float32`
m_flDestScale | `float32`
m_flScaleTimeStart | `GameTime_t`
m_nStartBrightness | `int32`
m_nDestBrightness | `int32`
m_flBrightnessTimeStart | `GameTime_t`
m_nSpriteWidth | `int32`
m_nSpriteHeight | `int32`

---

## C_CsmFovOverride
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_cameraName | `CUtlString`
m_flCsmFovOverrideValue | `float32`

---

## C_WeaponGlock
Derived from: [C_CSWeaponBaseGun](#c_csweaponbasegun), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_PhysicsProp
Derived from: [C_BreakableProp](#c_breakableprop), [CBaseProp](#cbaseprop), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bAwake | `bool`

---

## CFilterTeam
Derived from: [CBaseFilter](#cbasefilter), [CLogicalEntity](#clogicalentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_iFilterTeam | `int32`

---

## CBasePlayerWeaponVData


Name | Type
------------ | -------------
m_szWorldModel | `CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >`
m_sToolsOnlyOwnerModelName | `CResourceNameTyped< CWeakHandle< InfoForResourceTypeCModel > >`
m_bBuiltRightHanded | `bool`
m_bAllowFlipping | `bool`
m_sMuzzleAttachment | `CAttachmentNameSymbolWithStorage`
m_szMuzzleFlashParticle | `CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >`
m_szBarrelSmokeParticle | `CResourceNameTyped< CWeakHandle< InfoForResourceTypeIParticleSystemDefinition > >`
m_nMuzzleSmokeShotThreshold | `uint8`
m_flMuzzleSmokeTimeout | `float32`
m_flMuzzleSmokeDecrementRate | `float32`
m_bLinkedCooldowns | `bool`
m_iFlags | `ItemFlagTypes_t`
m_nPrimaryAmmoType | `AmmoIndex_t`
m_nSecondaryAmmoType | `AmmoIndex_t`
m_iMaxClip1 | `int32`
m_iMaxClip2 | `int32`
m_iDefaultClip1 | `int32`
m_iDefaultClip2 | `int32`
m_bReserveAmmoAsClips | `bool`
m_bTreatAsSingleClip | `bool`
m_iWeight | `int32`
m_bAutoSwitchTo | `bool`
m_bAutoSwitchFrom | `bool`
m_iRumbleEffect | `RumbleEffect_t`
m_flDropSpeed | `float32`
m_iSlot | `int32`
m_iPosition | `int32`
m_aShootSounds | `CUtlOrderedMap< WeaponSound_t, CSoundEventName >`

---

## C_CSGO_EndOfMatchLineupEnd
Derived from: [C_CSGO_EndOfMatchLineupEndpoint](#c_csgo_endofmatchlineupendpoint), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_CSGO_PreviewPlayerAlias_csgo_player_previewmodel
Derived from: [C_CSGO_PreviewPlayer](#c_csgo_previewplayer), [C_CSPlayerPawn](#c_csplayerpawn), [C_CSPlayerPawnBase](#c_csplayerpawnbase), [C_BasePlayerPawn](#c_baseplayerpawn), [C_BaseCombatCharacter](#c_basecombatcharacter), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## C_SmokeGrenade
Derived from: [C_BaseCSGrenade](#c_basecsgrenade), [C_CSWeaponBase](#c_csweaponbase), [C_BasePlayerWeapon](#c_baseplayerweapon), [C_EconEntity](#c_econentity), [C_BaseFlex](#c_baseflex), [CBaseAnimGraph](#cbaseanimgraph), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CInfoParticleTarget
Derived from: [C_PointEntity](#c_pointentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

---

## CCSPlayer_DamageReactServices


---

## C_PointClientUIWorldPanel
Derived from: [C_BaseClientUIEntity](#c_baseclientuientity), [C_BaseModelEntity](#c_basemodelentity), [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_bForceRecreateNextUpdate | `bool`
m_bMoveViewToPlayerNextThink | `bool`
m_bCheckCSSClasses | `bool`
m_anchorDeltaTransform | `CTransform`
m_pOffScreenIndicator | `CPointOffScreenIndicatorUi*`
m_bIgnoreInput | `bool`
m_bLit | `bool`
m_bFollowPlayerAcrossTeleport | `bool`
m_flWidth | `float32`
m_flHeight | `float32`
m_flDPI | `float32`
m_flInteractDistance | `float32`
m_flDepthOffset | `float32`
m_unOwnerContext | `uint32`
m_unHorizontalAlign | `uint32`
m_unVerticalAlign | `uint32`
m_unOrientation | `uint32`
m_bAllowInteractionFromAllSceneWorlds | `bool`
m_vecCSSClasses | `C_NetworkUtlVectorBase< CUtlSymbolLarge >`
m_bOpaque | `bool`
m_bNoDepth | `bool`
m_bRenderBackface | `bool`
m_bUseOffScreenIndicator | `bool`
m_bExcludeFromSaveGames | `bool`
m_bGrabbable | `bool`
m_bOnlyRenderToTexture | `bool`
m_bDisableMipGen | `bool`
m_nExplicitImageLayout | `int32`

---

## C_EntityFlame
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_hEntAttached | `CHandle< C_BaseEntity >`
m_hOldAttached | `CHandle< C_BaseEntity >`
m_bCheapEffect | `bool`

---

## CBasePlayerController
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)

Name | Type
------------ | -------------
m_CommandContext | `C_CommandContext`
m_nInButtonsWhichAreToggles | `uint64`
m_nTickBase | `uint32`
m_hPawn | `CHandle< C_BasePlayerPawn >`
m_bKnownTeamMismatch | `bool`
m_hPredictedPawn | `CHandle< C_BasePlayerPawn >`
m_nSplitScreenSlot | `CSplitScreenSlot`
m_hSplitOwner | `CHandle< CBasePlayerController >`
m_hSplitScreenPlayers | `CUtlVector< CHandle< CBasePlayerController > >`
m_bIsHLTV | `bool`
m_iConnected | `PlayerConnectedState`
m_iszPlayerName | `char[128]`
m_steamID | `uint64`
m_bIsLocalPlayerController | `bool`
m_bNoClipEnabled | `bool`
m_iDesiredFOV | `uint32`

---

## C_CSGO_EndOfMatchLineupEndpoint
Derived from: [C_BaseEntity](#c_baseentity), [CEntityInstance](#centityinstance)