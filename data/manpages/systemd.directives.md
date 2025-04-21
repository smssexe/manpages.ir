SYSTEMD.DIRECTIVES(7)						      systemd.directives						 SYSTEMD.DIRECTIVES(7)

NAME
       systemd.directives - Index of configuration directives

UNIT DIRECTIVES
       Directives for configuring units, used in unit files.

       Accept=
	   systemd.socket(5)

       AccuracySec=
	   systemd.timer(5)

       After=
	   systemd.unit(5)

       Alias=
	   systemd.unit(5)

       AllowIsolate=
	   systemd.unit(5)

       AllowedCPUs=
	   systemd.resource-control(5)

       AllowedMemoryNodes=
	   systemd.resource-control(5)

       Also=
	   systemd.unit(5)

       AmbientCapabilities=
	   systemd.exec(5)

       AppArmorProfile=
	   systemd.exec(5)

       AssertACPower=
	   systemd.unit(5)

       AssertArchitecture=
	   systemd.unit(5)

       AssertCPUFeature=
	   systemd.unit(5)

       AssertCPUPressure=
	   systemd.unit(5)

       AssertCPUs=
	   systemd.unit(5)

       AssertCapability=
	   systemd.unit(5)

       AssertControlGroupController=
	   systemd.unit(5)

       AssertCredential=
	   systemd.unit(5)

       AssertDirectoryNotEmpty=
	   systemd.unit(5)

       AssertEnvironment=
	   systemd.unit(5)

       AssertFileIsExecutable=
	   systemd.unit(5)

       AssertFileNotEmpty=
	   systemd.unit(5)

       AssertFirstBoot=
	   systemd.unit(5)

       AssertGroup=
	   systemd.unit(5)

       AssertHost=
	   systemd.unit(5)

       AssertIOPressure=
	   systemd.unit(5)

       AssertKernelCommandLine=
	   systemd.unit(5)

       AssertKernelVersion=
	   systemd.unit(5)

       AssertMemory=
	   systemd.unit(5)

       AssertMemoryPressure=
	   systemd.unit(5)

       AssertNeedsUpdate=
	   systemd.unit(5)

       AssertOSRelease=
	   systemd.unit(5)

       AssertPathExists=
	   systemd.unit(5)

       AssertPathExistsGlob=
	   systemd.unit(5)

       AssertPathIsDirectory=
	   systemd.unit(5)

       AssertPathIsEncrypted=
	   systemd.unit(5)

       AssertPathIsMountPoint=
	   systemd.unit(5)

       AssertPathIsReadWrite=
	   systemd.unit(5)

       AssertPathIsSymbolicLink=
	   systemd.unit(5)

       AssertSecurity=
	   systemd.unit(5)

       AssertUser=
	   systemd.unit(5)

       AssertVirtualization=
	   systemd.unit(5)

       BPFProgram=
	   systemd.resource-control(5)

       Backlog=
	   systemd.socket(5)

       Before=
	   systemd.unit(5)

       BindIPv6Only=
	   systemd.socket(5)

       BindPaths=
	   systemd.exec(5)

       BindReadOnlyPaths=
	   systemd.exec(5)

       BindToDevice=
	   systemd.socket(5)

       BindsTo=
	   systemd.unit(5)

       Broadcast=
	   systemd.socket(5)

       BusName=
	   systemd.service(5)

       CPUAccounting=
	   systemd.resource-control(5)

       CPUAffinity=
	   systemd.exec(5)

       CPUQuota=
	   systemd.resource-control(5)

       CPUQuotaPeriodSec=
	   systemd.resource-control(5)

       CPUSchedulingPolicy=
	   systemd.exec(5)

       CPUSchedulingPriority=
	   systemd.exec(5)

       CPUSchedulingResetOnFork=
	   systemd.exec(5)

       CPUWeight=
	   systemd.resource-control(5)

       CacheDirectory=
	   systemd.exec(5)

       CacheDirectoryMode=
	   systemd.exec(5)

       CapabilityBoundingSet=
	   systemd.exec(5)

       CollectMode=
	   systemd.unit(5)

       ConditionACPower=
	   systemd.unit(5)

       ConditionArchitecture=
	   systemd.unit(5)

       ConditionCPUFeature=
	   systemd.unit(5)

       ConditionCPUPressure=
	   systemd.unit(5)

       ConditionCPUs=
	   systemd.unit(5)

       ConditionCapability=
	   systemd.unit(5)

       ConditionControlGroupController=
	   systemd.unit(5)

       ConditionCredential=
	   systemd.unit(5)

       ConditionDirectoryNotEmpty=
	   systemd.unit(5)

       ConditionEnvironment=
	   systemd.unit(5)

       ConditionFileIsExecutable=
	   systemd.unit(5)

       ConditionFileNotEmpty=
	   systemd.unit(5)

       ConditionFirmware=
	   systemd.unit(5)

       ConditionFirstBoot=
	   systemd.unit(5)

       ConditionGroup=
	   systemd.unit(5)

       ConditionHost=
	   systemd.unit(5)

       ConditionIOPressure=
	   systemd.unit(5)

       ConditionKernelCommandLine=
	   systemd.unit(5)

       ConditionKernelVersion=
	   systemd.unit(5)

       ConditionMemory=
	   systemd.unit(5)

       ConditionMemoryPressure=
	   systemd.unit(5)

       ConditionNeedsUpdate=
	   systemd.unit(5)

       ConditionOSRelease=
	   systemd.unit(5)

       ConditionPathExists=
	   systemd.unit(5)

       ConditionPathExistsGlob=
	   systemd.unit(5)

       ConditionPathIsDirectory=
	   systemd.unit(5)

       ConditionPathIsEncrypted=
	   systemd.unit(5)

       ConditionPathIsMountPoint=
	   systemd.unit(5)

       ConditionPathIsReadWrite=
	   systemd.unit(5)

       ConditionPathIsSymbolicLink=
	   systemd.unit(5)

       ConditionSecurity=
	   systemd.unit(5)

       ConditionUser=
	   systemd.unit(5)

       ConditionVirtualization=
	   systemd.unit(5)

       ConfigurationDirectory=
	   systemd.exec(5)

       ConfigurationDirectoryMode=
	   systemd.exec(5)

       Conflicts=
	   systemd.unit(5)

       CoredumpFilter=
	   systemd.exec(5)

       CoredumpReceive=
	   systemd.resource-control(5)

       DefaultDependencies=
	   systemd.unit(5)

       DefaultInstance=
	   systemd.unit(5)

       DefaultStartupMemoryLow=
	   systemd.resource-control(5)

       DeferAcceptSec=
	   systemd.socket(5)

       Delegate=
	   systemd.resource-control(5)

       DelegateSubgroup=
	   systemd.resource-control(5)

       Description=
	   systemd.unit(5)

       DeviceAllow=
	   systemd.resource-control(5)

       DevicePolicy=
	   systemd.resource-control(5)

       DirectoryMode=
	   systemd.automount(5), systemd.mount(5), systemd.path(5), systemd.socket(5)

       DirectoryNotEmpty=
	   systemd.path(5)

       DisableControllers=
	   systemd.resource-control(5)

       Documentation=
	   systemd.unit(5)

       DynamicUser=
	   systemd.exec(5)

       Environment=
	   systemd.exec(5)

       EnvironmentFile=
	   systemd.exec(5)

       ExecCondition=
	   systemd.service(5)

       ExecPaths=
	   systemd.exec(5)

       ExecReload=
	   systemd.service(5)

       ExecSearchPath=
	   systemd.exec(5)

       ExecStart=
	   systemd.service(5)

       ExecStartPost=
	   systemd.service(5), systemd.socket(5)

       ExecStartPre=
	   systemd.service(5), systemd.socket(5)

       ExecStop=
	   systemd.service(5)

       ExecStopPost=
	   systemd.service(5), systemd.socket(5)

       ExecStopPre=
	   systemd.socket(5)

       ExitType=
	   systemd.service(5)

       ExtensionDirectories=
	   systemd.exec(5)

       ExtensionImagePolicy=
	   systemd.exec(5)

       ExtensionImages=
	   systemd.exec(5)

       ExtraOptions=
	   systemd.automount(5)

       FailureAction=
	   systemd.unit(5)

       FailureActionExitStatus=
	   systemd.unit(5)

       FileDescriptorName=
	   systemd.socket(5)

       FileDescriptorStoreMax=
	   systemd.service(5)

       FileDescriptorStorePreserve=
	   systemd.service(5)

       FinalKillSignal=
	   systemd.kill(5)

       FixedRandomDelay=
	   systemd.timer(5)

       FlushPending=
	   systemd.socket(5)

       ForceUnmount=
	   systemd.mount(5)

       FreeBind=
	   systemd.socket(5)

       Group=
	   systemd.exec(5)

       GuessMainPID=
	   systemd.service(5)

       IOAccounting=
	   systemd.resource-control(5)

       IODeviceLatencyTargetSec=
	   systemd.resource-control(5)

       IODeviceWeight=
	   systemd.resource-control(5)

       IOReadBandwidthMax=
	   systemd.resource-control(5)

       IOReadIOPSMax=
	   systemd.resource-control(5)

       IOSchedulingClass=
	   systemd.exec(5)

       IOSchedulingPriority=
	   systemd.exec(5)

       IOWeight=
	   systemd.resource-control(5)

       IOWriteBandwidthMax=
	   systemd.resource-control(5)

       IOWriteIOPSMax=
	   systemd.resource-control(5)

       IPAccounting=
	   systemd.resource-control(5)

       IPAddressAllow=
	   systemd.resource-control(5)

       IPAddressDeny=
	   systemd.resource-control(5)

       IPCNamespacePath=
	   systemd.exec(5)

       IPEgressFilterPath=
	   systemd.resource-control(5)

       IPIngressFilterPath=
	   systemd.resource-control(5)

       IPTOS=
	   systemd.socket(5)

       IPTTL=
	   systemd.socket(5)

       IgnoreOnIsolate=
	   systemd.unit(5)

       IgnoreSIGPIPE=
	   systemd.exec(5)

       ImportCredential=
	   systemd.exec(5)

       InaccessiblePaths=
	   systemd.exec(5)

       JobRunningTimeoutSec=
	   systemd.unit(5)

       JobTimeoutAction=
	   systemd.unit(5)

       JobTimeoutRebootArgument=
	   systemd.unit(5)

       JobTimeoutSec=
	   systemd.unit(5)

       JoinsNamespaceOf=
	   systemd.unit(5)

       KeepAlive=
	   systemd.socket(5)

       KeepAliveIntervalSec=
	   systemd.socket(5)

       KeepAliveProbes=
	   systemd.socket(5)

       KeepAliveTimeSec=
	   systemd.socket(5)

       KeyringMode=
	   systemd.exec(5)

       KillMode=
	   systemd.kill(5)

       KillSignal=
	   systemd.kill(5)

       LazyUnmount=
	   systemd.mount(5)

       LimitAS=
	   systemd.exec(5)

       LimitCORE=
	   systemd.exec(5)

       LimitCPU=
	   systemd.exec(5)

       LimitDATA=
	   systemd.exec(5)

       LimitFSIZE=
	   systemd.exec(5)

       LimitLOCKS=
	   systemd.exec(5)

       LimitMEMLOCK=
	   systemd.exec(5)

       LimitMSGQUEUE=
	   systemd.exec(5)

       LimitNICE=
	   systemd.exec(5)

       LimitNOFILE=
	   systemd.exec(5)

       LimitNPROC=
	   systemd.exec(5)

       LimitRSS=
	   systemd.exec(5)

       LimitRTPRIO=
	   systemd.exec(5)

       LimitRTTIME=
	   systemd.exec(5)

       LimitSIGPENDING=
	   systemd.exec(5)

       LimitSTACK=
	   systemd.exec(5)

       ListenDatagram=
	   systemd.socket(5)

       ListenFIFO=
	   systemd.socket(5)

       ListenMessageQueue=
	   systemd.socket(5)

       ListenNetlink=
	   systemd.socket(5)

       ListenSequentialPacket=
	   systemd.socket(5)

       ListenSpecial=
	   systemd.socket(5)

       ListenStream=
	   systemd.socket(5)

       ListenUSBFunction=
	   systemd.socket(5)

       LoadCredential=
	   systemd.exec(5)

       LoadCredentialEncrypted=
	   systemd.exec(5)

       LockPersonality=
	   systemd.exec(5)

       LogExtraFields=
	   systemd.exec(5)

       LogFilterPatterns=
	   systemd.exec(5)

       LogLevelMax=
	   systemd.exec(5)

       LogNamespace=
	   systemd.exec(5)

       LogRateLimitBurst=
	   systemd.exec(5)

       LogRateLimitIntervalSec=
	   systemd.exec(5)

       LogsDirectory=
	   systemd.exec(5)

       LogsDirectoryMode=
	   systemd.exec(5)

       MakeDirectory=
	   systemd.path(5)

       ManagedOOMMemoryPressure=
	   systemd.resource-control(5)

       ManagedOOMMemoryPressureLimit=
	   systemd.resource-control(5)

       ManagedOOMPreference=
	   systemd.resource-control(5)

       ManagedOOMSwap=
	   systemd.resource-control(5)

       Mark=
	   systemd.socket(5)

       MaxConnections=
	   systemd.socket(5)

       MaxConnectionsPerSource=
	   systemd.socket(5)

       MemoryAccounting=
	   systemd.resource-control(5)

       MemoryDenyWriteExecute=
	   systemd.exec(5)

       MemoryHigh=
	   systemd.resource-control(5)

       MemoryKSM=
	   systemd.exec(5)

       MemoryLow=
	   systemd.resource-control(5)

       MemoryMax=
	   systemd.resource-control(5)

       MemoryMin=
	   systemd.resource-control(5)

       MemoryPressureThresholdSec=
	   systemd.resource-control(5)

       MemoryPressureWatch=
	   systemd.resource-control(5)

       MemorySwapMax=
	   systemd.resource-control(5)

       MemoryZSwapMax=
	   systemd.resource-control(5)

       MessageQueueMaxMessages=
	   systemd.socket(5)

       MessageQueueMessageSize=
	   systemd.socket(5)

       MountAPIVFS=
	   systemd.exec(5)

       MountFlags=
	   systemd.exec(5)

       MountImagePolicy=
	   systemd.exec(5)

       MountImages=
	   systemd.exec(5)

       NFTSet=
	   systemd.resource-control(5)

       NUMAMask=
	   systemd.exec(5)

       NUMAPolicy=
	   systemd.exec(5)

       NetworkNamespacePath=
	   systemd.exec(5)

       Nice=
	   systemd.exec(5)

       NoDelay=
	   systemd.socket(5)

       NoExecPaths=
	   systemd.exec(5)

       NoNewPrivileges=
	   systemd.exec(5)

       NonBlocking=
	   systemd.service(5)

       NotifyAccess=
	   systemd.service(5)

       OOMPolicy=
	   systemd.scope(5), systemd.service(5)

       OOMScoreAdjust=
	   systemd.exec(5)

       OnActiveSec=
	   systemd.timer(5)

       OnBootSec=
	   systemd.timer(5)

       OnCalendar=
	   systemd.timer(5)

       OnClockChange=
	   systemd.timer(5)

       OnFailure=
	   systemd.unit(5)

       OnFailureJobMode=
	   systemd.unit(5)

       OnStartupSec=
	   systemd.timer(5)

       OnSuccess=
	   systemd.unit(5)

       OnSuccessJobMode=
	   systemd.unit(5)

       OnTimezoneChange=
	   systemd.timer(5)

       OnUnitActiveSec=
	   systemd.timer(5)

       OnUnitInactiveSec=
	   systemd.timer(5)

       OpenFile=
	   systemd.service(5)

       Options=
	   systemd.mount(5), systemd.swap(5)

       PAMName=
	   systemd.exec(5)

       PIDFile=
	   systemd.service(5)

       PartOf=
	   systemd.unit(5)

       PassCredentials=
	   systemd.socket(5)

       PassEnvironment=
	   systemd.exec(5)

       PassPacketInfo=
	   systemd.socket(5)

       PassSecurity=
	   systemd.socket(5)

       PathChanged=
	   systemd.path(5)

       PathExists=
	   systemd.path(5)

       PathExistsGlob=
	   systemd.path(5)

       PathModified=
	   systemd.path(5)

       Persistent=
	   systemd.timer(5)

       Personality=
	   systemd.exec(5)

       PipeSize=
	   systemd.socket(5)

       PollLimitBurst=
	   systemd.socket(5)

       PollLimitIntervalSec=
	   systemd.socket(5)

       Priority=
	   systemd.socket(5), systemd.swap(5)

       PrivateDevices=
	   systemd.exec(5)

       PrivateIPC=
	   systemd.exec(5)

       PrivateMounts=
	   systemd.exec(5)

       PrivateNetwork=
	   systemd.exec(5)

       PrivateTmp=
	   systemd.exec(5)

       PrivateUsers=
	   systemd.exec(5)

       ProcSubset=
	   systemd.exec(5)

       PropagatesReloadTo=
	   systemd.unit(5)

       PropagatesStopTo=
	   systemd.unit(5)

       ProtectClock=
	   systemd.exec(5)

       ProtectControlGroups=
	   systemd.exec(5)

       ProtectHome=
	   systemd.exec(5)

       ProtectHostname=
	   systemd.exec(5)

       ProtectKernelLogs=
	   systemd.exec(5)

       ProtectKernelModules=
	   systemd.exec(5)

       ProtectKernelTunables=
	   systemd.exec(5)

       ProtectProc=
	   systemd.exec(5)

       ProtectSystem=
	   systemd.exec(5)

       RandomizedDelaySec=
	   systemd.timer(5)

       ReadOnlyPaths=
	   systemd.exec(5)

       ReadWriteOnly=
	   systemd.mount(5)

       ReadWritePaths=
	   systemd.exec(5)

       RebootArgument=
	   systemd.unit(5)

       ReceiveBuffer=
	   systemd.socket(5)

       RefuseManualStart=
	   systemd.unit(5)

       RefuseManualStop=
	   systemd.unit(5)

       ReloadPropagatedFrom=
	   systemd.unit(5)

       ReloadSignal=
	   systemd.service(5)

       RemainAfterElapse=
	   systemd.timer(5)

       RemainAfterExit=
	   systemd.service(5)

       RemoveIPC=
	   systemd.exec(5)

       RemoveOnStop=
	   systemd.socket(5)

       RequiredBy=
	   systemd.unit(5)

       Requires=
	   systemd.unit(5)

       RequiresMountsFor=
	   systemd.unit(5)

       Requisite=
	   systemd.unit(5)

       Restart=
	   systemd.service(5)

       RestartForceExitStatus=
	   systemd.service(5)

       RestartKillSignal=
	   systemd.kill(5)

       RestartMaxDelaySec=
	   systemd.service(5)

       RestartMode=
	   systemd.service(5)

       RestartPreventExitStatus=
	   systemd.service(5)

       RestartSec=
	   systemd.service(5)

       RestartSteps=
	   systemd.service(5)

       RestrictAddressFamilies=
	   systemd.exec(5)

       RestrictFileSystems=
	   systemd.exec(5)

       RestrictNamespaces=
	   systemd.exec(5)

       RestrictNetworkInterfaces=
	   systemd.resource-control(5)

       RestrictRealtime=
	   systemd.exec(5)

       RestrictSUIDSGID=
	   systemd.exec(5)

       ReusePort=
	   systemd.socket(5)

       RootDirectory=
	   systemd.exec(5)

       RootDirectoryStartOnly=
	   systemd.service(5)

       RootEphemeral=
	   systemd.exec(5)

       RootHash=
	   systemd.exec(5)

       RootHashSignature=
	   systemd.exec(5)

       RootImage=
	   systemd.exec(5)

       RootImageOptions=
	   systemd.exec(5)

       RootImagePolicy=
	   systemd.exec(5)

       RootVerity=
	   systemd.exec(5)

       RuntimeDirectory=
	   systemd.exec(5)

       RuntimeDirectoryMode=
	   systemd.exec(5)

       RuntimeDirectoryPreserve=
	   systemd.exec(5)

       RuntimeMaxSec=
	   systemd.scope(5), systemd.service(5)

       RuntimeRandomizedExtraSec=
	   systemd.scope(5), systemd.service(5)

       SELinuxContext=
	   systemd.exec(5)

       SELinuxContextFromNet=
	   systemd.socket(5)

       SecureBits=
	   systemd.exec(5)

       SendBuffer=
	   systemd.socket(5)

       SendSIGHUP=
	   systemd.kill(5)

       SendSIGKILL=
	   systemd.kill(5)

       Service=
	   systemd.socket(5)

       SetCredential=
	   systemd.exec(5)

       SetCredentialEncrypted=
	   systemd.exec(5)

       SetLoginEnvironment=
	   systemd.exec(5)

       Slice=
	   systemd.resource-control(5)

       SloppyOptions=
	   systemd.mount(5)

       SmackLabel=
	   systemd.socket(5)

       SmackLabelIPIn=
	   systemd.socket(5)

       SmackLabelIPOut=
	   systemd.socket(5)

       SmackProcessLabel=
	   systemd.exec(5)

       SocketBindAllow=
	   systemd.resource-control(5)

       SocketBindDeny=
	   systemd.resource-control(5)

       SocketGroup=
	   systemd.socket(5)

       SocketMode=
	   systemd.socket(5)

       SocketProtocol=
	   systemd.socket(5)

       SocketUser=
	   systemd.socket(5)

       Sockets=
	   systemd.service(5)

       SourcePath=
	   systemd.unit(5)

       StandardError=
	   systemd.exec(5)

       StandardInput=
	   systemd.exec(5)

       StandardInputData=
	   systemd.exec(5)

       StandardInputText=
	   systemd.exec(5)

       StandardOutput=
	   systemd.exec(5)

       StartLimitAction=
	   systemd.unit(5)

       StartLimitBurst=
	   systemd.unit(5)

       StartLimitIntervalSec=
	   systemd.unit(5)

       StartupAllowedCPUs=
	   systemd.resource-control(5)

       StartupAllowedMemoryNodes=
	   systemd.resource-control(5)

       StartupCPUWeight=
	   systemd.resource-control(5)

       StartupIOWeight=
	   systemd.resource-control(5)

       StartupMemoryHigh=
	   systemd.resource-control(5)

       StartupMemoryLow=
	   systemd.resource-control(5)

       StartupMemoryMax=
	   systemd.resource-control(5)

       StartupMemorySwapMax=
	   systemd.resource-control(5)

       StartupMemoryZSwapMax=
	   systemd.resource-control(5)

       StateDirectory=
	   systemd.exec(5)

       StateDirectoryMode=
	   systemd.exec(5)

       StopPropagatedFrom=
	   systemd.unit(5)

       StopWhenUnneeded=
	   systemd.unit(5)

       SuccessAction=
	   systemd.unit(5)

       SuccessActionExitStatus=
	   systemd.unit(5)

       SuccessExitStatus=
	   systemd.service(5)

       SupplementaryGroups=
	   systemd.exec(5)

       SurviveFinalKillSignal=
	   systemd.unit(5)

       Symlinks=
	   systemd.socket(5)

       SyslogFacility=
	   systemd.exec(5)

       SyslogIdentifier=
	   systemd.exec(5)

       SyslogLevel=
	   systemd.exec(5)

       SyslogLevelPrefix=
	   systemd.exec(5)

       SystemCallArchitectures=
	   systemd.exec(5)

       SystemCallErrorNumber=
	   systemd.exec(5)

       SystemCallFilter=
	   systemd.exec(5)

       SystemCallLog=
	   systemd.exec(5)

       TCPCongestion=
	   systemd.socket(5)

       TTYColumns=
	   systemd.exec(5)

       TTYPath=
	   systemd.exec(5)

       TTYReset=
	   systemd.exec(5)

       TTYRows=
	   systemd.exec(5)

       TTYVHangup=
	   systemd.exec(5)

       TTYVTDisallocate=
	   systemd.exec(5)

       TasksAccounting=
	   systemd.resource-control(5)

       TasksMax=
	   systemd.resource-control(5)

       TemporaryFileSystem=
	   systemd.exec(5)

       TimeoutAbortSec=
	   systemd.service(5)

       TimeoutCleanSec=
	   systemd.exec(5)

       TimeoutIdleSec=
	   systemd.automount(5)

       TimeoutSec=
	   systemd.mount(5), systemd.service(5), systemd.socket(5), systemd.swap(5)

       TimeoutStartFailureMode=
	   systemd.service(5)

       TimeoutStartSec=
	   systemd.service(5)

       TimeoutStopFailureMode=
	   systemd.service(5)

       TimeoutStopSec=
	   systemd.service(5)

       TimerSlackNSec=
	   systemd.exec(5)

       Timestamping=
	   systemd.socket(5)

       Transparent=
	   systemd.socket(5)

       TriggerLimitBurst=
	   systemd.path(5), systemd.socket(5)

       TriggerLimitIntervalSec=
	   systemd.path(5), systemd.socket(5)

       Type=
	   systemd.mount(5), systemd.service(5)

       UMask=
	   systemd.exec(5)

       USBFunctionDescriptors=
	   systemd.service(5)

       USBFunctionStrings=
	   systemd.service(5)

       Unit=
	   systemd.path(5), systemd.timer(5)

       UnsetEnvironment=
	   systemd.exec(5)

       UpheldBy=
	   systemd.unit(5)

       Upholds=
	   systemd.unit(5)

       User=
	   systemd.exec(5)

       UtmpIdentifier=
	   systemd.exec(5)

       UtmpMode=
	   systemd.exec(5)

       WakeSystem=
	   systemd.timer(5)

       WantedBy=
	   systemd.unit(5)

       Wants=
	   systemd.unit(5)

       WatchdogSec=
	   systemd.service(5)

       WatchdogSignal=
	   systemd.kill(5)

       What=
	   systemd.mount(5), systemd.swap(5)

       Where=
	   systemd.automount(5), systemd.mount(5)

       WorkingDirectory=
	   systemd.exec(5)

       Writable=
	   systemd.socket(5)

OPTIONS ON THE KERNEL COMMAND LINE
       Kernel boot options for configuring the behaviour of the systemd process.

       -b
	   kernel-command-line(7), systemd(1)

       1
	   kernel-command-line(7), systemd(1)

       2
	   kernel-command-line(7), systemd(1)

       3
	   kernel-command-line(7), systemd(1)

       4
	   kernel-command-line(7), systemd(1)

       5
	   kernel-command-line(7), systemd(1)

       S
	   kernel-command-line(7), systemd(1)

       bond=
	   systemd-network-generator.service(8)

       bootdev=
	   systemd-network-generator.service(8)

       bridge=
	   systemd-network-generator.service(8)

       debug
	   kernel-command-line(7), systemd(1)

       domain=
	   kernel-command-line(7), systemd-resolved.service(8)

       emergency
	   kernel-command-line(7), systemd(1)

       fsck.mode=
	   kernel-command-line(7), systemd-fsck@.service(8)

       fsck.repair=
	   kernel-command-line(7), systemd-fsck@.service(8)

       fstab=
	   kernel-command-line(7), systemd-fstab-generator(8)

       ifname=
	   systemd-network-generator.service(8)

       ip=
	   systemd-network-generator.service(8)

       locale.LANG=
	   kernel-command-line(7), systemd(1)

       locale.LANGUAGE=
	   kernel-command-line(7), systemd(1)

       locale.LC_ADDRESS=
	   kernel-command-line(7), systemd(1)

       locale.LC_COLLATE=
	   kernel-command-line(7), systemd(1)

       locale.LC_CTYPE=
	   kernel-command-line(7), systemd(1)

       locale.LC_IDENTIFICATION=
	   kernel-command-line(7), systemd(1)

       locale.LC_MEASUREMENT=
	   kernel-command-line(7), systemd(1)

       locale.LC_MESSAGES=
	   kernel-command-line(7), systemd(1)

       locale.LC_MONETARY=
	   kernel-command-line(7), systemd(1)

       locale.LC_NAME=
	   kernel-command-line(7), systemd(1)

       locale.LC_NUMERIC=
	   kernel-command-line(7), systemd(1)

       locale.LC_PAPER=
	   kernel-command-line(7), systemd(1)

       locale.LC_TELEPHONE=
	   kernel-command-line(7), systemd(1)

       locale.LC_TIME=
	   kernel-command-line(7), systemd(1)

       luks.crypttab=
	   kernel-command-line(7), systemd-cryptsetup-generator(8)

       luks.data=
	   systemd-cryptsetup-generator(8)

       luks.key=
	   kernel-command-line(7), systemd-cryptsetup-generator(8)

       luks.name=
	   kernel-command-line(7), systemd-cryptsetup-generator(8)

       luks.options=
	   kernel-command-line(7), systemd-cryptsetup-generator(8)

       luks.uuid=
	   kernel-command-line(7), systemd-cryptsetup-generator(8)

       luks=
	   kernel-command-line(7), systemd-cryptsetup-generator(8)

       modules_load=
	   kernel-command-line(7), systemd-modules-load.service(8)

       mount.usr=
	   kernel-command-line(7), systemd-fstab-generator(8)

       mount.usrflags=
	   kernel-command-line(7), systemd-fstab-generator(8)

       mount.usrfstype=
	   kernel-command-line(7), systemd-fstab-generator(8)

       nameserver=
	   kernel-command-line(7), systemd-network-generator.service(8), systemd-resolved.service(8)

       net.ifname-policy=
	   systemd-network-generator.service(8), systemd-udevd.service(8)

       net.ifnames=
	   kernel-command-line(7), systemd-udevd.service(8)

       net.naming-scheme=
	   kernel-command-line(7), systemd-udevd.service(8)

       noresume
	   systemd-hibernate-resume-generator(8)

       plymouth.enable=
	   kernel-command-line(7)

       quiet
	   kernel-command-line(7), systemd(1)

       quotacheck.mode=
	   kernel-command-line(7), systemd-quotacheck.service(8)

       rd.emergency
	   kernel-command-line(7), systemd(1)

       rd.fstab=
	   kernel-command-line(7), systemd-fstab-generator(8)

       rd.luks.crypttab=
	   kernel-command-line(7), systemd-cryptsetup-generator(8)

       rd.luks.data=
	   systemd-cryptsetup-generator(8)

       rd.luks.key=
	   kernel-command-line(7), systemd-cryptsetup-generator(8)

       rd.luks.name=
	   kernel-command-line(7), systemd-cryptsetup-generator(8)

       rd.luks.options=
	   kernel-command-line(7), systemd-cryptsetup-generator(8)

       rd.luks.uuid=
	   kernel-command-line(7), systemd-cryptsetup-generator(8)

       rd.luks=
	   kernel-command-line(7), systemd-cryptsetup-generator(8)

       rd.modules_load=
	   kernel-command-line(7), systemd-modules-load.service(8)

       rd.peerdns=
	   systemd-network-generator.service(8)

       rd.rescue
	   kernel-command-line(7), systemd(1)

       rd.route=
	   systemd-network-generator.service(8)

       rd.systemd.gpt_auto
	   systemd-gpt-auto-generator(8)

       rd.systemd.gpt_auto=
	   kernel-command-line(7)

       rd.systemd.image_policy=
	   kernel-command-line(7), systemd-gpt-auto-generator(8)

       rd.systemd.mount-extra=
	   systemd-fstab-generator(8)

       rd.systemd.swap-extra=
	   systemd-fstab-generator(8)

       rd.systemd.unit=
	   kernel-command-line(7), systemd(1)

       rd.systemd.verity=
	   kernel-command-line(7), systemd-veritysetup-generator(8)

       rd.udev.blockdev_read_only
	   kernel-command-line(7), systemd-udevd.service(8)

       rd.udev.children_max=
	   kernel-command-line(7), systemd-udevd.service(8)

       rd.udev.event_timeout=
	   kernel-command-line(7), systemd-udevd.service(8)

       rd.udev.exec_delay=
	   kernel-command-line(7), systemd-udevd.service(8)

       rd.udev.log_level=
	   kernel-command-line(7), systemd-udevd.service(8)

       rd.udev.timeout_signal=
	   kernel-command-line(7), systemd-udevd.service(8)

       rd.veritytab=
	   kernel-command-line(7)

       rescue
	   kernel-command-line(7), systemd(1)

       resume=
	   kernel-command-line(7), systemd-hibernate-resume-generator(8)

       resume_offset=
	   systemd-hibernate-resume-generator(8)

       resumeflags=
	   kernel-command-line(7), systemd-hibernate-resume-generator(8)

       ro
	   kernel-command-line(7), systemd-gpt-auto-generator(8)

       root=
	   kernel-command-line(7), systemd-fstab-generator(8), systemd-gpt-auto-generator(8)

       rootflags=
	   kernel-command-line(7), systemd-fstab-generator(8), systemd-gpt-auto-generator(8)

       rootfstype=
	   kernel-command-line(7), systemd-fstab-generator(8), systemd-gpt-auto-generator(8)

       roothash=
	   kernel-command-line(7), systemd-fstab-generator(8), systemd-veritysetup-generator(8)

       rw
	   kernel-command-line(7), systemd-gpt-auto-generator(8)

       s
	   kernel-command-line(7), systemd(1)

       single
	   kernel-command-line(7), systemd(1)

       systemd.battery-check=
	   systemd-battery-check.service(8)

       systemd.clock-usec=
	   kernel-command-line(7)

       systemd.condition-first-boot=
	   kernel-command-line(7)

       systemd.condition-needs-update=
	   kernel-command-line(7)

       systemd.confirm_spawn
	   kernel-command-line(7), systemd(1)

       systemd.cpu_affinity=
	   kernel-command-line(7)

       systemd.crash_chvt
	   kernel-command-line(7), systemd(1)

       systemd.crash_reboot
	   kernel-command-line(7), systemd(1)

       systemd.crash_shell
	   kernel-command-line(7), systemd(1)

       systemd.debug_shell
	   kernel-command-line(7)

       systemd.default_device_timeout_sec=
	   kernel-command-line(7)

       systemd.default_standard_error=
	   kernel-command-line(7), systemd(1)

       systemd.default_standard_output=
	   kernel-command-line(7), systemd(1)

       systemd.default_timeout_start_sec=
	   kernel-command-line(7)

       systemd.dump_core
	   kernel-command-line(7), systemd(1)

       systemd.early_core_pattern=
	   kernel-command-line(7)

       systemd.firstboot=
	   kernel-command-line(7), systemd-firstboot(1)

       systemd.getty_auto=
	   kernel-command-line(7), systemd-getty-generator(8)

       systemd.gpt_auto
	   systemd-gpt-auto-generator(8)

       systemd.gpt_auto=
	   kernel-command-line(7)

       systemd.hostname=
	   kernel-command-line(7)

       systemd.image_policy=
	   kernel-command-line(7), systemd-gpt-auto-generator(8)

       systemd.import_credentials=
	   kernel-command-line(7), systemd(1)

       systemd.journald.forward_to_console=
	   kernel-command-line(7), systemd-journald.service(8)

       systemd.journald.forward_to_kmsg=
	   kernel-command-line(7), systemd-journald.service(8)

       systemd.journald.forward_to_syslog=
	   kernel-command-line(7), systemd-journald.service(8)

       systemd.journald.forward_to_wall=
	   kernel-command-line(7), systemd-journald.service(8)

       systemd.log_color
	   kernel-command-line(7), systemd(1)

       systemd.log_level=
	   kernel-command-line(7), systemd(1)

       systemd.log_location
	   systemd(1)

       systemd.log_location=
	   kernel-command-line(7)

       systemd.log_ratelimit_kmsg
	   kernel-command-line(7), systemd(1)

       systemd.log_target=
	   kernel-command-line(7), systemd(1)

       systemd.log_tid
	   systemd(1)

       systemd.log_time
	   systemd(1)

       systemd.machine_id=
	   kernel-command-line(7), systemd(1)

       systemd.mask=
	   kernel-command-line(7)

       systemd.mount-extra=
	   systemd-fstab-generator(8)

       systemd.random-seed=
	   kernel-command-line(7)

       systemd.reload_limit_burst=
	   kernel-command-line(7)

       systemd.reload_limit_interval_sec=
	   kernel-command-line(7)

       systemd.restore_state=
	   kernel-command-line(7), systemd-backlight@.service(8), systemd-rfkill.service(8)

       systemd.run=
	   kernel-command-line(7)

       systemd.run_failure_action=
	   kernel-command-line(7)

       systemd.run_success_action=
	   kernel-command-line(7)

       systemd.service_watchdogs
	   kernel-command-line(7)

       systemd.service_watchdogs=
	   systemd(1)

       systemd.set_credential=
	   kernel-command-line(7), systemd(1)

       systemd.set_credential_binary=
	   kernel-command-line(7), systemd(1)

       systemd.setenv=
	   kernel-command-line(7), systemd(1)

       systemd.show_status
	   kernel-command-line(7), systemd(1)

       systemd.status_unit_format=
	   kernel-command-line(7), systemd(1)

       systemd.swap-extra=
	   systemd-fstab-generator(8)

       systemd.swap=
	   systemd-fstab-generator(8), systemd-gpt-auto-generator(8)

       systemd.tty.columns.tty=
	   kernel-command-line(7)

       systemd.tty.rows.tty=
	   kernel-command-line(7)

       systemd.tty.term.tty=
	   kernel-command-line(7)

       systemd.unit=
	   kernel-command-line(7), systemd(1)

       systemd.verity.root_options=
	   kernel-command-line(7)

       systemd.verity=
	   kernel-command-line(7), systemd-veritysetup-generator(8)

       systemd.verity_root_data=
	   kernel-command-line(7), systemd-veritysetup-generator(8)

       systemd.verity_root_hash=
	   kernel-command-line(7), systemd-veritysetup-generator(8)

       systemd.verity_root_options=
	   systemd-veritysetup-generator(8)

       systemd.verity_usr_data=
	   kernel-command-line(7), systemd-veritysetup-generator(8)

       systemd.verity_usr_hash=
	   kernel-command-line(7), systemd-veritysetup-generator(8)

       systemd.verity_usr_options=
	   kernel-command-line(7), systemd-veritysetup-generator(8)

       systemd.volatile=
	   kernel-command-line(7), systemd-fstab-generator(8)

       systemd.wants=
	   kernel-command-line(7)

       systemd.watchdog_device=
	   kernel-command-line(7)

       systemd.watchdog_pre_sec=
	   kernel-command-line(7)

       systemd.watchdog_pretimeout_governor=
	   kernel-command-line(7)

       systemd.watchdog_sec=
	   kernel-command-line(7)

       udev.blockdev_read_only
	   kernel-command-line(7), systemd-udevd.service(8)

       udev.children_max=
	   kernel-command-line(7), systemd-udevd.service(8)

       udev.event_timeout=
	   kernel-command-line(7), systemd-udevd.service(8)

       udev.exec_delay=
	   kernel-command-line(7), systemd-udevd.service(8)

       udev.log_level=
	   kernel-command-line(7), systemd-udevd.service(8)

       udev.timeout_signal=
	   kernel-command-line(7), systemd-udevd.service(8)

       usrhash=
	   kernel-command-line(7), systemd-fstab-generator(8), systemd-veritysetup-generator(8)

       vconsole.font=
	   kernel-command-line(7)

       vconsole.font_map=
	   kernel-command-line(7)

       vconsole.font_unimap=
	   kernel-command-line(7)

       vconsole.keymap=
	   kernel-command-line(7)

       vconsole.keymap_toggle=
	   kernel-command-line(7)

       veritytab=
	   kernel-command-line(7)

       vlan=
	   systemd-network-generator.service(8)

SMBIOS TYPE 11 VARIABLES
       Data passed from VMM to system via SMBIOS Type 11.

       io.systemd.credential.binary:
	   smbios-type-11(7)

       io.systemd.credential:
	   smbios-type-11(7)

       io.systemd.stub.kernel-cmdline-extra=
	   smbios-type-11(7)

ENVIRONMENT VARIABLES
       Environment variables understood by the systemd manager and other programs and environment variable-compatible settings.

       $CACHE_DIRECTORY
	   systemd.exec(5)

       $CONFIGURATION_DIRECTORY
	   systemd.exec(5)

       $CREDENTIALS_DIRECTORY
	   systemd.exec(5), systemd.generator(7)

       $EMAIL
	   pam_systemd(8)

       $ENCRYPTED_CREDENTIALS_DIRECTORY
	   systemd.generator(7)

       $EXIT_CODE
	   systemd.exec(5)

       $EXIT_STATUS
	   systemd.exec(5)

       $FDSTORE
	   systemd.exec(5)

       $HOME
	   systemd.exec(5)

       $INVOCATION_ID
	   systemd.exec(5)

       $JOURNAL_STREAM
	   systemd.exec(5)

       $LANG
	   pam_systemd(8), systemd.exec(5)

       $LISTEN_FDNAMES
	   sd_listen_fds(3), systemd(1), systemd-socket-activate(1), systemd.exec(5)

       $LISTEN_FDS
	   sd_listen_fds(3), systemd(1), systemd-socket-activate(1), systemd.exec(5)

       $LISTEN_PID
	   sd_listen_fds(3), systemd(1), systemd-socket-activate(1), systemd.exec(5)

       $LOGNAME
	   systemd.exec(5)

       $LOGS_DIRECTORY
	   systemd.exec(5)

       $LOG_NAMESPACE
	   systemd.exec(5)

       $MAINPID
	   systemd.exec(5)

       $MANAGERPID
	   systemd.exec(5)

       $MEMORY_PRESSURE_WATCH
	   systemd.exec(5)

       $MEMORY_PRESSURE_WRITE
	   systemd.exec(5)

       $MONITOR_EXIT_CODE
	   systemd.exec(5)

       $MONITOR_EXIT_STATUS
	   systemd.exec(5)

       $MONITOR_INVOCATION_ID
	   systemd.exec(5)

       $MONITOR_SERVICE_RESULT
	   systemd.exec(5)

       $MONITOR_UNIT
	   systemd.exec(5)

       $NOTIFY_SOCKET
	   sd_notify(3), systemd(1), systemd.exec(5)

       $PATH
	   systemd.exec(5)

       $PIDFILE
	   systemd.exec(5)

       $PREVLEVEL
	   runlevel(8)

       $REMOTE_ADDR
	   systemd.exec(5)

       $REMOTE_PORT
	   systemd.exec(5)

       $RUNLEVEL
	   runlevel(8)

       $RUNTIME_DIRECTORY
	   systemd.exec(5)

       $SERVICE_RESULT
	   systemd.exec(5)

       $SHELL
	   systemd.exec(5)

       $STATE_DIRECTORY
	   systemd.exec(5)

       $SYSTEMD_ARCHITECTURE
	   systemd.generator(7)

       $SYSTEMD_COLORS
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       $SYSTEMD_CONFIDENTIAL_VIRTUALIZATION
	   systemd.generator(7)

       $SYSTEMD_DEBUGGER
	   coredumpctl(1)

       $SYSTEMD_EDITOR
	   systemctl(1)

       $SYSTEMD_ENVIRONMENT_GENERATOR_PATH
	   systemd(1)

       $SYSTEMD_EXEC_PID
	   systemd.exec(5)

       $SYSTEMD_FIRST_BOOT
	   systemd.generator(7)

       $SYSTEMD_GENERATOR_PATH
	   systemd(1)

       $SYSTEMD_GETTY_AUTO
	   systemd-getty-generator(8)

       $SYSTEMD_HOME=
	   pam_systemd_home(8)

       $SYSTEMD_HOME_SUSPEND=
	   pam_systemd_home(8)

       $SYSTEMD_IN_INITRD
	   systemd.generator(7)

       $SYSTEMD_LESS
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       $SYSTEMD_LESSCHARSET
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       $SYSTEMD_LOG_COLOR
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-socket-activate(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       $SYSTEMD_LOG_LEVEL
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-socket-activate(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       $SYSTEMD_LOG_LOCATION
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-socket-activate(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       $SYSTEMD_LOG_RATELIMIT_KMSG
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemd(1), systemd-analyze(1), systemd-inhibit(1), systemd-
	   nspawn(1), timedatectl(1), userdbctl(1)

       $SYSTEMD_LOG_TARGET
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-socket-activate(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       $SYSTEMD_LOG_TID
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemd(1), systemd-analyze(1), systemd-inhibit(1), systemd-
	   nspawn(1), timedatectl(1), userdbctl(1)

       $SYSTEMD_LOG_TIME
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-socket-activate(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       $SYSTEMD_NSS_RESOLVE_CACHE
	   nss-resolve(8)

       $SYSTEMD_NSS_RESOLVE_NETWORK
	   nss-resolve(8)

       $SYSTEMD_NSS_RESOLVE_SYNTHESIZE
	   nss-resolve(8)

       $SYSTEMD_NSS_RESOLVE_TRUST_ANCHOR
	   nss-resolve(8)

       $SYSTEMD_NSS_RESOLVE_VALIDATE
	   nss-resolve(8)

       $SYSTEMD_NSS_RESOLVE_ZONE
	   nss-resolve(8)

       $SYSTEMD_PAGER
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       $SYSTEMD_PAGERSECURE
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       $SYSTEMD_RANDOM_SEED_CREDIT
	   systemd-random-seed.service(8)

       $SYSTEMD_SCOPE
	   systemd.generator(7)

       $SYSTEMD_UNIT_PATH
	   systemd(1)

       $SYSTEMD_URLIFY
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       $SYSTEMD_VIRTUALIZATION
	   systemd.generator(7)

       $TERM
	   systemd.exec(5)

       $TRIGGER_PATH
	   systemd.exec(5)

       $TRIGGER_TIMER_MONOTONIC_USEC
	   systemd.exec(5)

       $TRIGGER_TIMER_REALTIME_USEC
	   systemd.exec(5)

       $TRIGGER_UNIT
	   systemd.exec(5)

       $TZ
	   pam_systemd(8)

       $USER
	   systemd.exec(5)

       $WATCHDOG_PID
	   sd_watchdog_enabled(3), systemd.exec(5)

       $WATCHDOG_USEC
	   sd_watchdog_enabled(3), systemd.exec(5)

       $XDG_CONFIG_DIRS
	   systemd(1)

       $XDG_CONFIG_HOME
	   systemd(1)

       $XDG_DATA_DIRS
	   systemd(1)

       $XDG_DATA_HOME
	   systemd(1)

       $XDG_RUNTIME_DIR
	   pam_systemd(8), systemd.exec(5)

       $XDG_SEAT
	   pam_systemd(8)

       $XDG_SESSION_CLASS
	   pam_systemd(8)

       $XDG_SESSION_DESKTOP
	   pam_systemd(8)

       $XDG_SESSION_ID
	   pam_systemd(8)

       $XDG_SESSION_TYPE
	   pam_systemd(8)

       $XDG_VTNR
	   pam_systemd(8)

       ANSI_COLOR=
	   os-release(5)

       ARCHITECTURE=
	   os-release(5)

       BUG_REPORT_URL=
	   os-release(5)

       BUILD_ID=
	   os-release(5)

       CHASSIS=
	   machine-info(5)

       CONFEXT_LEVEL=
	   os-release(5)

       CONFEXT_SCOPE=
	   os-release(5)

       CPE_NAME=
	   os-release(5)

       DEFAULT_HOSTNAME=
	   os-release(5)

       DEPLOYMENT=
	   machine-info(5)

       DOCUMENTATION_URL=
	   os-release(5)

       HARDWARE_MODEL=
	   machine-info(5)

       HARDWARE_VENDOR=
	   machine-info(5)

       HOME_URL=
	   os-release(5)

       ICON_NAME=
	   machine-info(5)

       ID=
	   os-release(5)

       ID_LIKE=
	   os-release(5)

       IMAGE_ID=
	   os-release(5)

       IMAGE_VERSION=
	   os-release(5)

       LOCATION=
	   machine-info(5)

       LOGO=
	   os-release(5)

       NAME=
	   os-release(5)

       PORTABLE_PREFIXES=
	   os-release(5)

       PRETTY_HOSTNAME=
	   machine-info(5)

       PRETTY_NAME=
	   os-release(5)

       PRIVACY_POLICY_URL=
	   os-release(5)

       SUPPORT_END=
	   os-release(5)

       SUPPORT_URL=
	   os-release(5)

       SYSEXT_LEVEL=
	   os-release(5)

       SYSEXT_SCOPE=
	   os-release(5)

       VARIANT=
	   os-release(5)

       VARIANT_ID=
	   os-release(5)

       VENDOR_NAME=
	   os-release(5)

       VENDOR_URL=
	   os-release(5)

       VERSION=
	   os-release(5)

       VERSION_CODENAME=
	   os-release(5)

       VERSION_ID=
	   os-release(5)

SYSTEM CREDENTIALS
       System credentials understood by the system and service manager and various other components:

       firstboot.keymap
	   systemd-firstboot(1), systemd.system-credentials(7)

       firstboot.locale
	   systemd-firstboot(1), systemd.system-credentials(7)

       firstboot.locale-messages
	   systemd-firstboot(1), systemd.system-credentials(7)

       firstboot.timezone
	   systemd-firstboot(1), systemd.system-credentials(7)

       fstab.extra
	   systemd-fstab-generator(8), systemd.system-credentials(7)

       getty.ttys.container
	   systemd-getty-generator(8), systemd.system-credentials(7)

       getty.ttys.serial
	   systemd-getty-generator(8), systemd.system-credentials(7)

       login.issue
	   systemd.system-credentials(7)

       login.motd
	   systemd.system-credentials(7)

       network.dns
	   systemd-resolved.service(8), systemd.system-credentials(7)

       network.hosts
	   systemd.system-credentials(7)

       network.search_domains
	   systemd-resolved.service(8), systemd.system-credentials(7)

       passwd.hashed-password.user
	   systemd-sysusers(8)

       passwd.hashed-password.root
	   systemd-firstboot(1), systemd.system-credentials(7)

       passwd.plaintext-password.user
	   systemd-sysusers(8)

       passwd.plaintext-password.root
	   systemd-firstboot(1), systemd.system-credentials(7)

       passwd.shell.user
	   systemd-sysusers(8)

       passwd.shell.root
	   systemd-firstboot(1), systemd.system-credentials(7)

       ssh.authorized_keys.root
	   systemd.system-credentials(7)

       sysctl.extra
	   systemd-sysctl.service(8), systemd.system-credentials(7)

       system.machine_id
	   systemd(1), systemd.system-credentials(7)

       sysusers.extra
	   systemd-sysusers(8), systemd.system-credentials(7)

       tmpfiles.extra
	   systemd-tmpfiles(8), systemd.system-credentials(7)

       vconsole.font
	   systemd.system-credentials(7)

       vconsole.font_map
	   systemd.system-credentials(7)

       vconsole.font_unimap
	   systemd.system-credentials(7)

       vconsole.keymap
	   systemd.system-credentials(7)

       vconsole.keymap_toggle
	   systemd.system-credentials(7)

       vmm.notify_socket
	   systemd(1), systemd.system-credentials(7)

EFI VARIABLES
       EFI variables understood by systemd-boot(7) and other programs.

       LoaderBootCountPath
	   systemd-boot(7)

       LoaderConfigConsoleMode
	   systemd-boot(7)

       LoaderConfigTimeout
	   systemd-boot(7)

       LoaderConfigTimeoutOneShot
	   systemd-boot(7)

       LoaderDevicePartUUID
	   systemd-boot(7), systemd-stub(7)

       LoaderEntries
	   systemd-boot(7)

       LoaderEntryDefault
	   systemd-boot(7)

       LoaderEntryLastBooted
	   systemd-boot(7)

       LoaderEntryOneShot
	   systemd-boot(7)

       LoaderEntrySelected
	   systemd-boot(7)

       LoaderFeatures
	   systemd-boot(7)

       LoaderFirmwareInfo
	   systemd-boot(7), systemd-stub(7)

       LoaderFirmwareType
	   systemd-boot(7), systemd-stub(7)

       LoaderImageIdentifier
	   systemd-boot(7), systemd-stub(7)

       LoaderInfo
	   systemd-boot(7)

       LoaderSystemToken
	   systemd-boot(7)

       LoaderTimeExecUSec
	   systemd-boot(7)

       LoaderTimeInitUSec
	   systemd-boot(7)

       LoaderTimeMenuUsec
	   systemd-boot(7)

       StubInfo
	   systemd-stub(7)

       StubPcrInitRDSysExts
	   systemd-stub(7)

       StubPcrKernelImage
	   systemd-stub(7)

       StubPcrKernelParameters
	   systemd-stub(7)

HOME AREA/USER ACCOUNT DIRECTIVES
       Directives for configuring home areas and user accounts via systemd-homed.service(8).

       DefaultFileSystemType=
	   homed.conf(5)

       DefaultStorage=
	   homed.conf(5)

UDEV DIRECTIVES
       Directives for configuring systemd units through the udev database.

       $$
	   udev(7)

       $attr{file}
	   udev(7)

       $devnode
	   udev(7)

       $devpath
	   udev(7)

       $driver
	   udev(7)

       $env{key}
	   udev(7)

       $id
	   udev(7)

       $kernel
	   udev(7)

       $links
	   udev(7)

       $major
	   udev(7)

       $minor
	   udev(7)

       $name
	   udev(7)

       $number
	   udev(7)

       $parent
	   udev(7)

       $result
	   udev(7)

       $root
	   udev(7)

       $sys
	   udev(7)

       "%%"
	   udev(7)

       %E{key}
	   udev(7)

       "%M"
	   udev(7)

       "%N"
	   udev(7)

       "%P"
	   udev(7)

       "%S"
	   udev(7)

       "%b"
	   udev(7)

       %c
	   udev(7)

       %k
	   udev(7)

       "%m"
	   udev(7)

       "%n"
	   udev(7)

       "%p"
	   udev(7)

       %r
	   udev(7)

       %s{file}
	   udev(7)

       ACTION
	   udev(7)

       ATTRS{filename}
	   udev(7)

       ATTR{filename}
	   udev(7)

       CONST{key}
	   udev(7)

       DEVPATH
	   udev(7)

       DRIVER
	   udev(7)

       DRIVERS
	   udev(7)

       ENV{key}
	   udev(7)

       GOTO
	   udev(7)

       GROUP
	   udev(7)

       ID_AUTOSEAT
	   sd-login(3)

       ID_FOR_SEAT
	   sd-login(3)

       ID_MODEL=
	   systemd.device(5)

       ID_MODEL_FROM_DATABASE=
	   systemd.device(5)

       ID_SEAT
	   sd-login(3)

       IMPORT{type}
	   udev(7)

       KERNEL
	   udev(7)

       KERNELS
	   udev(7)

       LABEL
	   udev(7)

       MODE
	   udev(7)

       NAME
	   udev(7)

       OPTIONS
	   udev(7)

       OWNER
	   udev(7)

       PROGRAM
	   udev(7)

       RESULT
	   udev(7)

       RUN{type}
	   udev(7)

       SECLABEL{module}
	   udev(7)

       SUBSYSTEM
	   udev(7)

       SUBSYSTEMS
	   udev(7)

       SYMLINK
	   udev(7)

       SYSCTL{kernel parameter}
	   udev(7)

       SYSTEMD_ALIAS=
	   systemd.device(5)

       SYSTEMD_MOUNT_OPTIONS=
	   systemd-mount(1)

       SYSTEMD_MOUNT_WHERE=
	   systemd-mount(1)

       SYSTEMD_READY=
	   systemd.device(5)

       SYSTEMD_USER_WANTS=
	   systemd.device(5)

       SYSTEMD_WANTS=
	   systemd.device(5)

       TAG
	   udev(7)

       TAGS
	   udev(7)

       TEST{octal mode mask}
	   udev(7)

       db_persist
	   udev(7)

       link_priority=
	   udev(7)

       log_level=
	   udev(7)

       nowatch
	   udev(7)

       static_node=
	   udev(7)

       string_escape=
	   udev(7)

       watch
	   udev(7)

NETWORK DIRECTIVES
       Directives for configuring network links through the net-setup-link udev builtin and networks through systemd-networkd.

       ARP=
	   systemd.network(5)

       ARPAllTargets=
	   systemd.netdev(5)

       ARPIPTargets=
	   systemd.netdev(5)

       ARPIntervalSec=
	   systemd.netdev(5)

       ARPValidate=
	   systemd.netdev(5)

       AckFilter=
	   systemd.network(5)

       Activate=
	   systemd.netdev(5)

       ActivationPolicy=
	   systemd.network(5)

       ActiveSlave=
	   systemd.network(5)

       AdActorSystem=
	   systemd.netdev(5)

       AdActorSystemPriority=
	   systemd.netdev(5)

       AdSelect=
	   systemd.netdev(5)

       AdUserPortKey=
	   systemd.netdev(5)

       AddPrefixRoute=
	   systemd.network(5)

       Address=
	   systemd.network(5)

       AddressAutoconfiguration=
	   systemd.network(5)

       Advertise=
	   systemd.link(5)

       AgeingTimeSec=
	   systemd.netdev(5)

       Aggregation=
	   systemd.netdev(5)

       Alias=
	   systemd.link(5)

       AllMulticast=
	   systemd.network(5)

       AllSlavesActive=
	   systemd.netdev(5)

       AllowList=
	   systemd.network(5)

       AllowLocalRemote=
	   systemd.netdev(5)

       AllowPortToBeRoot=
	   systemd.network(5)

       AllowedIPs=
	   systemd.netdev(5)

       AlternativeName=
	   systemd.link(5)

       AlternativeNamesPolicy=
	   systemd.link(5)

       Announce=
	   systemd.network(5)

       Anonymize=
	   systemd.network(5)

       Architecture=
	   systemd.link(5), systemd.netdev(5), systemd.network(5)

       Assign=
	   systemd.network(5)

       AssignToLoopback=
	   systemd.netdev(5)

       AssociatedWith=
	   systemd.network(5)

       AutoJoin=
	   systemd.network(5)

       AutoNegotiation=
	   systemd.link(5)

       AutoNegotiationFlowControl=
	   systemd.link(5)

       AutoRateIngress=
	   systemd.network(5)

       BSSID=
	   systemd.network(5)

       Bands=
	   systemd.network(5)

       Bandwidth=
	   systemd.network(5)

       BatmanAdvanced=
	   systemd.network(5)

       BindCarrier=
	   systemd.network(5)

       BindToInterface=
	   systemd.network(5)

       BitRate=
	   systemd.network(5)

       BitsPerSecond=
	   systemd.link(5)

       Blackhole=
	   systemd.network(5)

       Bond=
	   systemd.network(5)

       BootFilename=
	   systemd.network(5)

       BootServerAddress=
	   systemd.network(5)

       BootServerName=
	   systemd.network(5)

       Bridge=
	   systemd.network(5)

       BridgeLoopAvoidance=
	   systemd.netdev(5)

       Broadcast=
	   systemd.network(5)

       BroadcastMulticastQueueLength=
	   systemd.netdev(5)

       Buckets=
	   systemd.network(5)

       BufferBytes=
	   systemd.network(5)

       BurstBytes=
	   systemd.network(5)

       BusErrorReporting=
	   systemd.network(5)

       CEThresholdSec=
	   systemd.network(5)

       Cache=
	   resolved.conf(5)

       CacheFromLocalhost=
	   resolved.conf(5)

       CeilBufferBytes=
	   systemd.network(5)

       CeilRate=
	   systemd.network(5)

       ClassId=
	   systemd.network(5)

       ClassicDataLengthCode=
	   systemd.network(5)

       ClientIdentifier=
	   systemd.network(5)

       CoalescePacketRateHigh=
	   systemd.link(5)

       CoalescePacketRateLow=
	   systemd.link(5)

       CoalescePacketRateSampleIntervalSec=
	   systemd.link(5)

       CombinedChannels=
	   systemd.link(5)

       CompensationMode=
	   systemd.network(5)

       ConfigureWithoutCarrier=
	   systemd.network(5)

       ConnectionRetrySec=
	   timesyncd.conf(5)

       CopyDSCP=
	   systemd.netdev(5)

       Cost=
	   systemd.network(5)

       Credential=
	   systemd.link(5), systemd.netdev(5), systemd.network(5)

       DHCP=
	   systemd.network(5)

       DHCPPrefixDelegation=
	   systemd.network(5)

       DHCPServer=
	   systemd.network(5)

       DHCPv6Client=
	   systemd.network(5)

       DNS=
	   resolved.conf(5), systemd.network(5)

       DNSDefaultRoute=
	   systemd.network(5)

       DNSLifetimeSec=
	   systemd.network(5)

       DNSOverTLS=
	   resolved.conf(5), systemd.network(5)

       DNSSEC=
	   resolved.conf(5), systemd.network(5)

       DNSSECNegativeTrustAnchors=
	   systemd.network(5)

       DNSStubListener=
	   resolved.conf(5)

       DNSStubListenerExtra=
	   resolved.conf(5)

       DUIDRawData=
	   networkd.conf(5), systemd.network(5)

       DUIDType=
	   networkd.conf(5), systemd.network(5)

       DataBitRate=
	   systemd.network(5)

       DataPhaseBufferSegment1=
	   systemd.network(5)

       DataPhaseBufferSegment2=
	   systemd.network(5)

       DataPropagationSegment=
	   systemd.network(5)

       DataSamplePoint=
	   systemd.network(5)

       DataSyncJumpWidth=
	   systemd.network(5)

       DataTimeQuantaNSec=
	   systemd.network(5)

       DefaultClass=
	   systemd.network(5)

       DefaultLeaseTimeSec=
	   systemd.network(5)

       DefaultPVID=
	   systemd.netdev(5)

       DefaultRouteOnDevice=
	   systemd.network(5)

       DefaultVirtualQueue=
	   systemd.network(5)

       DelayJitterSec=
	   systemd.network(5)

       DelaySec=
	   systemd.network(5)

       DenyList=
	   systemd.network(5)

       Description=
	   systemd.link(5), systemd.netdev(5), systemd.network(5)

       Destination=
	   systemd.network(5)

       DestinationPort=
	   systemd.netdev(5), systemd.network(5)

       DiscoverPathMTU=
	   systemd.netdev(5)

       DistributedArpTable=
	   systemd.netdev(5)

       Domains=
	   resolved.conf(5), systemd.network(5)

       DownDelaySec=
	   systemd.netdev(5)

       Driver=
	   systemd.link(5), systemd.network(5)

       Duplex=
	   systemd.link(5)

       DuplicateAddressDetection=
	   systemd.network(5)

       DuplicateRate=
	   systemd.network(5)

       DynamicTransmitLoadBalancing=
	   systemd.netdev(5)

       ECN=
	   systemd.network(5)

       ERSPANDirection=
	   systemd.netdev(5)

       ERSPANHardwareId=
	   systemd.netdev(5)

       ERSPANIndex=
	   systemd.netdev(5)

       ERSPANVersion=
	   systemd.netdev(5)

       EgressQOSMaps=
	   systemd.netdev(5)

       EgressUntagged=
	   systemd.network(5)

       EmitDNS=
	   systemd.network(5)

       EmitDomains=
	   systemd.network(5)

       EmitLLDP=
	   systemd.network(5)

       EmitLPR=
	   systemd.network(5)

       EmitNTP=
	   systemd.network(5)

       EmitPOP3=
	   systemd.network(5)

       EmitRouter=
	   systemd.network(5)

       EmitSIP=
	   systemd.network(5)

       EmitSMTP=
	   systemd.network(5)

       EmitTimezone=
	   systemd.network(5)

       Encapsulation=
	   systemd.netdev(5)

       EncapsulationLimit=
	   systemd.netdev(5)

       EncapsulationType=
	   systemd.netdev(5)

       Encrypt=
	   systemd.netdev(5)

       Endpoint=
	   systemd.netdev(5)

       EtherType=
	   systemd.netdev(5)

       External=
	   systemd.netdev(5)

       FDBAgeingSec=
	   systemd.netdev(5)

       FDMode=
	   systemd.network(5)

       FDNonISO=
	   systemd.network(5)

       FOUDestinationPort=
	   systemd.netdev(5)

       FOUSourcePort=
	   systemd.netdev(5)

       FailOverMACPolicy=
	   systemd.netdev(5)

       FallbackDNS=
	   resolved.conf(5)

       FallbackLeaseLifetimeSec=
	   systemd.network(5)

       FallbackNTP=
	   timesyncd.conf(5)

       Family=
	   systemd.network(5)

       FastLeave=
	   systemd.network(5)

       FastOpenNoCookie=
	   systemd.network(5)

       FirewallMark=
	   systemd.netdev(5), systemd.network(5)

       Firmware=
	   systemd.link(5), systemd.netdev(5), systemd.network(5)

       Flags=
	   systemd.netdev(5)

       FlowIsolationMode=
	   systemd.network(5)

       FlowLabel=
	   systemd.netdev(5)

       FlowLimit=
	   systemd.network(5)

       Flows=
	   systemd.network(5)

       FooOverUDP=
	   systemd.netdev(5)

       ForwardDelaySec=
	   systemd.netdev(5)

       Fragmentation=
	   systemd.netdev(5)

       From=
	   systemd.network(5)

       GVRP=
	   systemd.netdev(5)

       Gateway=
	   systemd.network(5)

       GatewayBandwidthDown=
	   systemd.netdev(5)

       GatewayBandwidthUp=
	   systemd.netdev(5)

       GatewayMode=
	   systemd.netdev(5)

       GatewayOnLink=
	   systemd.network(5)

       GenericProtocolExtension=
	   systemd.netdev(5)

       GenericRIO=
	   systemd.network(5)

       GenericReceiveOffload=
	   systemd.link(5)

       GenericReceiveOffloadHardware=
	   systemd.link(5)

       GenericSegmentOffloadMaxBytes=
	   systemd.link(5)

       GenericSegmentOffloadMaxSegments=
	   systemd.link(5)

       GenericSegmentationOffload=
	   systemd.link(5)

       GratuitousARP=
	   systemd.netdev(5)

       Group=
	   systemd.netdev(5), systemd.network(5)

       GroupForwardMask=
	   systemd.netdev(5)

       GroupPolicyExtension=
	   systemd.netdev(5)

       HairPin=
	   systemd.network(5)

       Handle=
	   systemd.network(5)

       HelloTimeSec=
	   systemd.netdev(5)

       HomeAddress=
	   systemd.network(5)

       HomeAgent=
	   systemd.network(5)

       HomeAgentLifetimeSec=
	   systemd.network(5)

       HomeAgentPreference=
	   systemd.network(5)

       HopLimit=
	   systemd.network(5)

       HopPenalty=
	   systemd.netdev(5)

       Host=
	   systemd.link(5), systemd.netdev(5), systemd.network(5)

       Hostname=
	   systemd.network(5)

       IAID=
	   systemd.network(5)

       IPDoNotFragment=
	   systemd.netdev(5)

       IPForward=
	   systemd.network(5)

       IPMasquerade=
	   systemd.network(5)

       IPProtocol=
	   systemd.network(5)

       IPServiceType=
	   systemd.network(5)

       IPVLAN=
	   systemd.network(5)

       IPVTAP=
	   systemd.network(5)

       IPoIB=
	   systemd.network(5)

       IPv4AcceptLocal=
	   systemd.network(5)

       IPv4LLRoute=
	   systemd.network(5)

       IPv4LLStartAddress=
	   systemd.network(5)

       IPv4ProxyARP=
	   systemd.network(5)

       IPv4ReversePathFilter=
	   systemd.network(5)

       IPv4RouteLocalnet=
	   systemd.network(5)

       IPv6AcceptRA=
	   systemd.network(5)

       IPv6DuplicateAddressDetection=
	   systemd.network(5)

       IPv6FlowLabel=
	   systemd.netdev(5)

       IPv6HopLimit=
	   systemd.network(5)

       IPv6LinkLocalAddressGenerationMode=
	   systemd.network(5)

       IPv6MTUBytes=
	   systemd.network(5)

       IPv6OnlyMode=
	   systemd.network(5)

       IPv6OnlyPreferredSec=
	   systemd.network(5)

       IPv6Preference=
	   systemd.network(5)

       IPv6PrivacyExtensions=
	   networkd.conf(5), systemd.network(5)

       IPv6ProxyNDP=
	   systemd.network(5)

       IPv6ProxyNDPAddress=
	   systemd.network(5)

       IPv6RapidDeploymentPrefix=
	   systemd.netdev(5)

       IPv6SendRA=
	   systemd.network(5)

       IPv6StableSecretAddress=
	   systemd.network(5)

       ISATAP=
	   systemd.netdev(5)

       Id=
	   systemd.netdev(5), systemd.network(5)

       IgnoreCarrierLoss=
	   systemd.network(5)

       IgnoreDontFragment=
	   systemd.netdev(5)

       IgnoreUserspaceMulticastGroup=
	   systemd.netdev(5), systemd.network(5)

       IncomingInterface=
	   systemd.network(5)

       Independent=
	   systemd.netdev(5)

       IngressQOSMaps=
	   systemd.netdev(5)

       InheritInnerProtocol=
	   systemd.netdev(5)

       InitialAdvertisedReceiveWindow=
	   systemd.network(5)

       InitialCongestionWindow=
	   systemd.network(5)

       InitialQuantumBytes=
	   systemd.network(5)

       InputKey=
	   systemd.netdev(5)

       InterfaceId=
	   systemd.netdev(5)

       IntervalSec=
	   systemd.network(5)

       InvertRule=
	   systemd.network(5)

       Isolated=
	   systemd.network(5)

       KeepCarrier=
	   systemd.netdev(5)

       KeepConfiguration=
	   systemd.network(5)

       KeepMaster=
	   systemd.network(5)

       KernelCommandLine=
	   systemd.link(5), systemd.netdev(5), systemd.network(5)

       KernelVersion=
	   systemd.link(5), systemd.netdev(5), systemd.network(5)

       Key=
	   systemd.netdev(5)

       KeyFile=
	   systemd.netdev(5)

       KeyId=
	   systemd.netdev(5)

       Kind=
	   systemd.link(5), systemd.netdev(5), systemd.network(5)

       L2MissNotification=
	   systemd.netdev(5)

       L3MissNotification=
	   systemd.netdev(5)

       LACPTransmitRate=
	   systemd.netdev(5)

       LLDP=
	   systemd.network(5)

       LLMNR=
	   resolved.conf(5), systemd.network(5)

       LPR=
	   systemd.network(5)

       Label=
	   systemd.network(5)

       LargeReceiveOffload=
	   systemd.link(5)

       LatencySec=
	   systemd.network(5)

       Layer2SpecificHeader=
	   systemd.netdev(5)

       LearnPacketIntervalSec=
	   systemd.netdev(5)

       Learning=
	   systemd.network(5)

       LifetimeSec=
	   systemd.network(5)

       LimitBytes=
	   systemd.network(5)

       LinkLayerAddress=
	   systemd.network(5)

       LinkLocalAddressing=
	   systemd.network(5)

       LinkState=
	   systemd.link(5), systemd.network(5)

       ListenOnly=
	   systemd.network(5)

       ListenPort=
	   systemd.netdev(5), systemd.network(5)

       Local=
	   systemd.netdev(5)

       Loopback=
	   systemd.network(5)

       LooseBinding=
	   systemd.netdev(5)

       LossRate=
	   systemd.network(5)

       MACAddress=
	   systemd.link(5), systemd.netdev(5), systemd.network(5)

       MACAddressPolicy=
	   systemd.link(5)

       MACSpoofCheck=
	   systemd.link(5), systemd.network(5)

       MACVLAN=
	   systemd.network(5)

       MACVTAP=
	   systemd.network(5)

       MACsec=
	   systemd.network(5)

       MDI=
	   systemd.link(5)

       MIIMonitorSec=
	   systemd.netdev(5)

       MPUBytes=
	   systemd.network(5)

       MTUBytes=
	   systemd.link(5), systemd.netdev(5), systemd.network(5)

       MUDURL=
	   systemd.network(5)

       MVRP=
	   systemd.netdev(5)

       MacLearning=
	   systemd.netdev(5)

       ManageForeignRoutes=
	   networkd.conf(5)

       ManageForeignRoutingPolicyRules=
	   networkd.conf(5)

       ManageTemporaryAddress=
	   systemd.network(5)

       Managed=
	   systemd.network(5)

       MaxAgeSec=
	   systemd.netdev(5)

       MaxAttempts=
	   systemd.network(5)

       MaxLeaseTimeSec=
	   systemd.network(5)

       MaxPacketBytes=
	   systemd.network(5)

       MaximumFDBEntries=
	   systemd.netdev(5)

       MaximumRate=
	   systemd.network(5)

       MemoryLimitBytes=
	   systemd.network(5)

       Metric=
	   systemd.network(5)

       MinLinks=
	   systemd.netdev(5)

       Mode=
	   systemd.netdev(5), systemd.network(5)

       MultiPathRoute=
	   systemd.network(5)

       MultiQueue=
	   systemd.netdev(5)

       Multicast=
	   systemd.network(5)

       MulticastDNS=
	   resolved.conf(5), systemd.network(5)

       MulticastFlood=
	   systemd.network(5)

       MulticastGroupAddress=
	   systemd.network(5)

       MulticastIGMPVersion=
	   systemd.netdev(5)

       MulticastQuerier=
	   systemd.netdev(5)

       MulticastRouter=
	   systemd.network(5)

       MulticastSnooping=
	   systemd.netdev(5)

       MulticastToUnicast=
	   systemd.network(5)

       NAT=
	   systemd.network(5)

       NFTSet=
	   systemd.network(5)

       NTP=
	   systemd.network(5), timesyncd.conf(5)

       NTupleFilter=
	   systemd.link(5)

       Name=
	   systemd.dnssd(5), systemd.link(5), systemd.netdev(5), systemd.network(5)

       NamePolicy=
	   systemd.link(5)

       NeighborSuppression=
	   systemd.network(5)

       NetLabel=
	   systemd.network(5)

       NextHop=
	   systemd.network(5)

       OnLink=
	   systemd.network(5)

       OneShot=
	   systemd.network(5)

       OriginalName=
	   systemd.link(5)

       OriginatorIntervalSec=
	   systemd.netdev(5)

       OrphanMask=
	   systemd.network(5)

       OtherChannels=
	   systemd.link(5)

       OtherInformation=
	   systemd.network(5)

       OutgoingInterface=
	   systemd.network(5)

       OutputKey=
	   systemd.netdev(5)

       OverheadBytes=
	   systemd.network(5)

       POP3=
	   systemd.network(5)

       PVID=
	   systemd.network(5)

       Pacing=
	   systemd.network(5)

       PacketInfo=
	   systemd.netdev(5)

       PacketLimit=
	   systemd.network(5)

       PacketNumber=
	   systemd.netdev(5)

       PacketsPerSlave=
	   systemd.netdev(5)

       Parent=
	   systemd.network(5)

       PartitionKey=
	   systemd.netdev(5)

       Path=
	   systemd.link(5), systemd.network(5)

       PeakRate=
	   systemd.network(5)

       Peer=
	   systemd.netdev(5), systemd.network(5)

       PeerPort=
	   systemd.netdev(5)

       PeerSessionId=
	   systemd.netdev(5)

       PeerTunnelId=
	   systemd.netdev(5)

       PermanentMACAddress=
	   systemd.link(5), systemd.network(5)

       PersistentKeepalive=
	   systemd.netdev(5)

       PerturbPeriodSec=
	   systemd.network(5)

       PhaseBufferSegment1=
	   systemd.network(5)

       PhaseBufferSegment2=
	   systemd.network(5)

       PhysicalDevice=
	   systemd.netdev(5)

       PollIntervalMaxSec=
	   timesyncd.conf(5)

       PollIntervalMinSec=
	   timesyncd.conf(5)

       PoolOffset=
	   systemd.network(5)

       PoolSize=
	   systemd.network(5)

       Port=
	   systemd.dnssd(5), systemd.link(5), systemd.netdev(5)

       PortRange=
	   systemd.netdev(5)

       PreferredLifetime=
	   systemd.network(5)

       PreferredLifetimeSec=
	   systemd.network(5)

       PreferredSource=
	   systemd.network(5)

       Prefix=
	   systemd.network(5)

       PrefixAllowList=
	   systemd.network(5)

       PrefixDelegationHint=
	   systemd.network(5)

       PrefixDenyList=
	   systemd.network(5)

       PresharedKey=
	   systemd.netdev(5)

       PresharedKeyFile=
	   systemd.netdev(5)

       PresumeAck=
	   systemd.network(5)

       PrimaryReselectPolicy=
	   systemd.netdev(5)

       PrimarySlave=
	   systemd.network(5)

       Priority=
	   systemd.dnssd(5), systemd.netdev(5), systemd.network(5)

       PriorityMap=
	   systemd.network(5)

       PriorityQueueingPreset=
	   systemd.network(5)

       PrivateKey=
	   systemd.netdev(5)

       PrivateKeyFile=
	   systemd.netdev(5)

       Promiscuous=
	   systemd.network(5)

       PropagationSegment=
	   systemd.network(5)

       Property=
	   systemd.link(5), systemd.network(5)

       Protocol=
	   systemd.netdev(5), systemd.network(5)

       ProxyARP=
	   systemd.network(5)

       ProxyARPWiFi=
	   systemd.network(5)

       PublicKey=
	   systemd.netdev(5)

       QualityOfService=
	   systemd.link(5), systemd.network(5)

       QuantumBytes=
	   systemd.network(5)

       QueryReceiveSideScaling=
	   systemd.link(5), systemd.network(5)

       QuickAck=
	   systemd.network(5)

       RTTSec=
	   systemd.network(5)

       RapidCommit=
	   systemd.network(5)

       Rate=
	   systemd.network(5)

       RateToQuantum=
	   systemd.network(5)

       ReadEtcHosts=
	   resolved.conf(5)

       ReceiveChecksumOffload=
	   systemd.link(5)

       ReceiveQueues=
	   systemd.link(5)

       ReceiveVLANCTAGFilter=
	   systemd.link(5)

       ReceiveVLANCTAGHardwareAcceleration=
	   systemd.link(5)

       ReduceARPProxy=
	   systemd.netdev(5)

       RelayAgentCircuitId=
	   systemd.network(5)

       RelayAgentRemoteId=
	   systemd.network(5)

       RelayTarget=
	   systemd.network(5)

       Remote=
	   systemd.netdev(5)

       RemoteChecksumRx=
	   systemd.netdev(5)

       RemoteChecksumTx=
	   systemd.netdev(5)

       ReorderHeader=
	   systemd.netdev(5)

       RequestAddress=
	   systemd.network(5)

       RequestBroadcast=
	   systemd.network(5)

       RequestOptions=
	   systemd.network(5)

       RequiredFamilyForOnline=
	   systemd.network(5)

       RequiredForOnline=
	   systemd.network(5)

       ResendIGMP=
	   systemd.netdev(5)

       ResolveUnicastSingleLabel=
	   resolved.conf(5)

       RestartSec=
	   systemd.network(5)

       RetransmitSec=
	   systemd.network(5)

       RootDistanceMaxSec=
	   timesyncd.conf(5)

       Route=
	   systemd.network(5)

       RouteAllowList=
	   systemd.network(5)

       RouteDenyList=
	   systemd.network(5)

       RouteMTUBytes=
	   systemd.network(5)

       RouteMetric=
	   systemd.netdev(5), systemd.network(5)

       RouteShortCircuit=
	   systemd.netdev(5)

       RouteTable=
	   networkd.conf(5), systemd.netdev(5), systemd.network(5)

       Router=
	   systemd.network(5)

       RouterAllowList=
	   systemd.network(5)

       RouterDenyList=
	   systemd.network(5)

       RouterLifetimeSec=
	   systemd.network(5)

       RouterPreference=
	   systemd.network(5)

       RoutesToDNS=
	   systemd.network(5)

       RoutesToNTP=
	   systemd.network(5)

       RoutingAlgorithm=
	   systemd.netdev(5)

       RxBufferSize=
	   systemd.link(5)

       RxChannels=
	   systemd.link(5)

       RxCoalesceHighSec=
	   systemd.link(5)

       RxCoalesceIrqSec=
	   systemd.link(5)

       RxCoalesceLowSec=
	   systemd.link(5)

       RxCoalesceSec=
	   systemd.link(5)

       RxFlowControl=
	   systemd.link(5)

       RxJumboBufferSize=
	   systemd.link(5)

       RxMaxCoalescedFrames=
	   systemd.link(5)

       RxMaxCoalescedHighFrames=
	   systemd.link(5)

       RxMaxCoalescedIrqFrames=
	   systemd.link(5)

       RxMaxCoalescedLowFrames=
	   systemd.link(5)

       RxMiniBufferSize=
	   systemd.link(5)

       SIP=
	   systemd.network(5)

       SMTP=
	   systemd.network(5)

       SR-IOVVirtualFunctions=
	   systemd.link(5)

       SSID=
	   systemd.network(5)

       STP=
	   systemd.netdev(5)

       SamplePoint=
	   systemd.network(5)

       SaveIntervalSec=
	   timesyncd.conf(5)

       Scope=
	   systemd.network(5)

       SendDecline=
	   systemd.network(5)

       SendHostname=
	   systemd.network(5)

       SendOption=
	   systemd.network(5)

       SendRelease=
	   systemd.network(5)

       SendVendorOption=
	   systemd.network(5)

       SerializeTunneledPackets=
	   systemd.netdev(5)

       ServerAddress=
	   systemd.network(5)

       SessionId=
	   systemd.netdev(5)

       SocketPriority=
	   systemd.network(5)

       Source=
	   systemd.network(5)

       SourceMACAddress=
	   systemd.netdev(5)

       SourcePort=
	   systemd.network(5)

       SpeedMeter=
	   networkd.conf(5)

       SpeedMeterIntervalSec=
	   networkd.conf(5)

       SplitGSO=
	   systemd.network(5)

       StatisticsBlockCoalesceSec=
	   systemd.link(5)

       StrictBands=
	   systemd.network(5)

       SubnetId=
	   systemd.network(5)

       SuppressInterfaceGroup=
	   systemd.network(5)

       SuppressPrefixLength=
	   systemd.network(5)

       SyncJumpWidth=
	   systemd.network(5)

       TCP6SegmentationOffload=
	   systemd.link(5)

       TCPAdvertisedMaximumSegmentSize=
	   systemd.network(5)

       TCPCongestionControlAlgorithm=
	   systemd.network(5)

       TCPRetransmissionTimeoutSec=
	   systemd.network(5)

       TCPSegmentationOffload=
	   systemd.link(5)

       TOS=
	   systemd.netdev(5)

       TTL=
	   systemd.netdev(5)

       TTLPropagate=
	   systemd.network(5)

       Table=
	   systemd.netdev(5), systemd.network(5)

       TargetSec=
	   systemd.network(5)

       Termination=
	   systemd.network(5)

       TimeQuantaNSec=
	   systemd.network(5)

       Timezone=
	   systemd.network(5)

       To=
	   systemd.network(5)

       Token=
	   systemd.network(5)

       TransmitChecksumOffload=
	   systemd.link(5)

       TransmitHashPolicy=
	   systemd.netdev(5)

       TransmitQueueLength=
	   systemd.link(5)

       TransmitQueues=
	   systemd.link(5)

       TransmitVLANCTAGHardwareAcceleration=
	   systemd.link(5)

       TransmitVLANSTAGHardwareAcceleration=
	   systemd.link(5)

       TripleSampling=
	   systemd.network(5)

       Trust=
	   systemd.link(5), systemd.network(5)

       Tunnel=
	   systemd.network(5)

       TunnelId=
	   systemd.netdev(5)

       TxBufferSize=
	   systemd.link(5)

       TxChannels=
	   systemd.link(5)

       TxCoalesceHighSec=
	   systemd.link(5)

       TxCoalesceIrqSec=
	   systemd.link(5)

       TxCoalesceLowSec=
	   systemd.link(5)

       TxCoalesceSec=
	   systemd.link(5)

       TxFlowControl=
	   systemd.link(5)

       TxMaxCoalescedFrames=
	   systemd.link(5)

       TxMaxCoalescedHighFrames=
	   systemd.link(5)

       TxMaxCoalescedIrqFrames=
	   systemd.link(5)

       TxMaxCoalescedLowFrames=
	   systemd.link(5)

       TxtData=
	   systemd.dnssd(5)

       TxtText=
	   systemd.dnssd(5)

       Type=
	   systemd.dnssd(5), systemd.link(5), systemd.netdev(5), systemd.network(5)

       TypeOfService=
	   systemd.network(5)

       UDP6ZeroChecksumRx=
	   systemd.netdev(5)

       UDP6ZeroChecksumTx=
	   systemd.netdev(5)

       UDPChecksum=
	   systemd.netdev(5)

       UDPDestinationPort=
	   systemd.netdev(5)

       UDPSourcePort=
	   systemd.netdev(5)

       UnicastFlood=
	   systemd.network(5)

       Unmanaged=
	   systemd.network(5)

       UpDelaySec=
	   systemd.netdev(5)

       UplinkInterface=
	   systemd.network(5)

       Use6RD=
	   systemd.network(5)

       UseAdaptiveRxCoalesce=
	   systemd.link(5)

       UseAdaptiveTxCoalesce=
	   systemd.link(5)

       UseAddress=
	   systemd.network(5)

       UseAutonomousPrefix=
	   systemd.network(5)

       UseBPDU=
	   systemd.network(5)

       UseCaptivePortal=
	   systemd.network(5)

       UseDNS=
	   systemd.network(5)

       UseDelegatedPrefix=
	   systemd.network(5)

       UseDomains=
	   systemd.network(5)

       UseForEncoding=
	   systemd.netdev(5)

       UseGateway=
	   systemd.network(5)

       UseHopLimit=
	   systemd.network(5)

       UseHostname=
	   systemd.network(5)

       UseICMP6RateLimit=
	   systemd.network(5)

       UseMTU=
	   systemd.network(5)

       UseNTP=
	   systemd.network(5)

       UseOnLinkPrefix=
	   systemd.network(5)

       UsePREF64=
	   systemd.network(5)

       UseRawPacketSize=
	   systemd.network(5)

       UseRoutePrefix=
	   systemd.network(5)

       UseRoutes=
	   systemd.network(5)

       UseSIP=
	   systemd.network(5)

       UseTimezone=
	   systemd.network(5)

       User=
	   systemd.netdev(5), systemd.network(5)

       UserClass=
	   systemd.network(5)

       VLAN=
	   systemd.network(5)

       VLANFiltering=
	   systemd.netdev(5)

       VLANId=
	   systemd.link(5), systemd.network(5)

       VLANProtocol=
	   systemd.link(5), systemd.netdev(5), systemd.network(5)

       VNI=
	   systemd.netdev(5), systemd.network(5)

       VNetHeader=
	   systemd.netdev(5)

       VRF=
	   systemd.network(5)

       VXLAN=
	   systemd.network(5)

       ValidLifetimeSec=
	   systemd.network(5)

       VendorClass=
	   systemd.network(5)

       VendorClassIdentifier=
	   systemd.network(5)

       VirtualFunction=
	   systemd.link(5), systemd.network(5)

       VirtualQueues=
	   systemd.network(5)

       Virtualization=
	   systemd.link(5), systemd.netdev(5), systemd.network(5)

       WDS=
	   systemd.netdev(5)

       WLANInterfaceType=
	   systemd.network(5)

       WakeOnLan=
	   systemd.link(5)

       WakeOnLanPassword=
	   systemd.link(5)

       Wash=
	   systemd.network(5)

       Weight=
	   systemd.dnssd(5), systemd.network(5)

       WithoutRA=
	   systemd.network(5)

       Xfrm=
	   systemd.network(5)

JOURNAL FIELDS
       Fields in the journal events with a well known meaning.

       CODE_FILE=
	   systemd.journal-fields(7)

       CODE_FUNC=
	   systemd.journal-fields(7)

       CODE_LINE=
	   systemd.journal-fields(7)

       COREDUMP=
	   systemd-coredump(8)

       COREDUMP_CGROUP=
	   systemd-coredump(8)

       COREDUMP_CMDLINE=
	   systemd-coredump(8)

       COREDUMP_COMM=
	   systemd-coredump(8)

       COREDUMP_CONTAINER_CMDLINE=
	   systemd-coredump(8)

       COREDUMP_CWD=
	   systemd-coredump(8)

       COREDUMP_ENVIRON=
	   systemd-coredump(8)

       COREDUMP_EXE=
	   systemd-coredump(8)

       COREDUMP_FILENAME=
	   systemd-coredump(8)

       COREDUMP_GID=
	   systemd-coredump(8)

       COREDUMP_HOSTNAME=
	   systemd-coredump(8)

       COREDUMP_OPEN_FDS=
	   systemd-coredump(8)

       COREDUMP_OWNER_UID=
	   systemd-coredump(8)

       COREDUMP_PACKAGE_JSON=
	   systemd-coredump(8)

       COREDUMP_PACKAGE_NAME=
	   systemd-coredump(8)

       COREDUMP_PACKAGE_VERSION=
	   systemd-coredump(8)

       COREDUMP_PID=
	   systemd-coredump(8)

       COREDUMP_PROC_AUXV=
	   systemd-coredump(8)

       COREDUMP_PROC_CGROUP=
	   systemd-coredump(8)

       COREDUMP_PROC_LIMITS=
	   systemd-coredump(8)

       COREDUMP_PROC_MAPS=
	   systemd-coredump(8)

       COREDUMP_PROC_MOUNTINFO=
	   systemd-coredump(8)

       COREDUMP_PROC_STATUS=
	   systemd-coredump(8)

       COREDUMP_RLIMIT=
	   systemd-coredump(8)

       COREDUMP_ROOT=
	   systemd-coredump(8)

       COREDUMP_SESSION=
	   systemd-coredump(8)

       COREDUMP_SIGNAL=
	   systemd-coredump(8)

       COREDUMP_SIGNAL_NAME=
	   systemd-coredump(8)

       COREDUMP_SLICE=
	   systemd-coredump(8)

       COREDUMP_TIMESTAMP=
	   systemd-coredump(8)

       COREDUMP_TRUNCATED=
	   systemd-coredump(8)

       COREDUMP_UID=
	   systemd-coredump(8)

       COREDUMP_UNIT=
	   systemd-coredump(8), systemd.journal-fields(7)

       COREDUMP_USER_UNIT=
	   systemd-coredump(8), systemd.journal-fields(7)

       DOCUMENTATION=
	   systemd.journal-fields(7)

       ERRNO=
	   systemd.journal-fields(7)

       INVOCATION_ID=
	   systemd.journal-fields(7)

       MESSAGE=
	   systemd-coredump(8), systemd.journal-fields(7)

       MESSAGE_ID=
	   systemd.journal-fields(7)

       OBJECT_AUDIT_LOGINUID=
	   systemd.journal-fields(7)

       OBJECT_AUDIT_SESSION=
	   systemd.journal-fields(7)

       OBJECT_CMDLINE=
	   systemd.journal-fields(7)

       OBJECT_COMM=
	   systemd.journal-fields(7)

       OBJECT_EXE=
	   systemd.journal-fields(7)

       OBJECT_GID=
	   systemd.journal-fields(7)

       OBJECT_PID=
	   systemd.journal-fields(7)

       OBJECT_SYSTEMD_CGROUP=
	   systemd.journal-fields(7)

       OBJECT_SYSTEMD_OWNER_UID=
	   systemd.journal-fields(7)

       OBJECT_SYSTEMD_SESSION=
	   systemd.journal-fields(7)

       OBJECT_SYSTEMD_UNIT=
	   systemd.journal-fields(7)

       OBJECT_SYSTEMD_USER_UNIT=
	   systemd.journal-fields(7)

       OBJECT_UID=
	   systemd.journal-fields(7)

       PRIORITY=
	   systemd.journal-fields(7)

       SYSLOG_FACILITY=
	   systemd.journal-fields(7)

       SYSLOG_IDENTIFIER=
	   systemd.journal-fields(7)

       SYSLOG_PID=
	   systemd.journal-fields(7)

       SYSLOG_RAW=
	   systemd.journal-fields(7)

       SYSLOG_TIMESTAMP=
	   systemd.journal-fields(7)

       TID=
	   systemd.journal-fields(7)

       UNIT=
	   systemd.journal-fields(7)

       USER_INVOCATION_ID=
	   systemd.journal-fields(7)

       USER_UNIT=
	   systemd.journal-fields(7)

       _AUDIT_LOGINUID=
	   systemd.journal-fields(7)

       _AUDIT_SESSION=
	   systemd.journal-fields(7)

       _BOOT_ID=
	   systemd.journal-fields(7)

       _CAP_EFFECTIVE=
	   systemd.journal-fields(7)

       _CMDLINE=
	   systemd.journal-fields(7)

       _COMM=
	   systemd.journal-fields(7)

       _EXE=
	   systemd.journal-fields(7)

       _GID=
	   systemd.journal-fields(7)

       _HOSTNAME=
	   systemd.journal-fields(7)

       _KERNEL_DEVICE=
	   systemd.journal-fields(7)

       _KERNEL_SUBSYSTEM=
	   systemd.journal-fields(7)

       _LINE_BREAK=
	   systemd.journal-fields(7)

       _MACHINE_ID=
	   systemd.journal-fields(7)

       _NAMESPACE=
	   systemd.journal-fields(7)

       _PID=
	   systemd.journal-fields(7)

       _RUNTIME_SCOPE=
	   systemd.journal-fields(7)

       _SELINUX_CONTEXT=
	   systemd.journal-fields(7)

       _SOURCE_REALTIME_TIMESTAMP=
	   systemd.journal-fields(7)

       _STREAM_ID=
	   systemd.journal-fields(7)

       _SYSTEMD_CGROUP=
	   systemd.journal-fields(7)

       _SYSTEMD_INVOCATION_ID=
	   systemd.journal-fields(7)

       _SYSTEMD_OWNER_UID=
	   systemd.journal-fields(7)

       _SYSTEMD_SESSION=
	   systemd.journal-fields(7)

       _SYSTEMD_SLICE=
	   systemd.journal-fields(7)

       _SYSTEMD_UNIT=
	   systemd.journal-fields(7)

       _SYSTEMD_USER_SLICE=
	   systemd.journal-fields(7)

       _SYSTEMD_USER_UNIT=
	   systemd.journal-fields(7)

       _TRANSPORT=
	   systemd.journal-fields(7)

       _UDEV_DEVLINK=
	   systemd.journal-fields(7)

       _UDEV_DEVNODE=
	   systemd.journal-fields(7)

       _UDEV_SYSNAME=
	   systemd.journal-fields(7)

       _UID=
	   systemd.journal-fields(7)

       __CURSOR=
	   systemd.journal-fields(7)

       __MONOTONIC_TIMESTAMP=
	   systemd.journal-fields(7)

       __REALTIME_TIMESTAMP=
	   systemd.journal-fields(7)

       __SEQNUM=
	   systemd.journal-fields(7)

       __SEQNUM_ID=
	   systemd.journal-fields(7)

PAM CONFIGURATION DIRECTIVES
       Directives for configuring PAM behaviour.

       class=
	   pam_systemd(8)

       debug
	   pam_systemd(8), pam_systemd_home(8), pam_systemd_loadkey(8)

       default-capability-ambient-set=
	   pam_systemd(8)

       default-capability-bounding-set=
	   pam_systemd(8)

       desktop=
	   pam_systemd(8)

       keyname=
	   pam_systemd_loadkey(8)

       suspend=
	   pam_systemd_home(8)

       systemd.cpu_weight=
	   pam_systemd(8)

       systemd.io_weight=
	   pam_systemd(8)

       systemd.memory_max=
	   pam_systemd(8)

       systemd.runtime_max_sec=
	   pam_systemd(8)

       systemd.tasks_max=
	   pam_systemd(8)

       type=
	   pam_systemd(8)

/ETC/CRYPTTAB, /ETC/VERITYTAB AND /ETC/FSTAB OPTIONS
       Options which influence mounted filesystems and encrypted volumes.

       _netdev
	   crypttab(5), systemd.mount(5), veritytab(5)

       auto
	   systemd.mount(5), systemd.swap(5)

       bitlk
	   crypttab(5)

       check-at-most-once
	   veritytab(5)

       cipher=
	   crypttab(5)

       data-block-size=
	   veritytab(5)

       data-blocks=
	   veritytab(5)

       discard
	   crypttab(5)

       fec-device=
	   veritytab(5)

       fec-offset=
	   veritytab(5)

       fec-roots=
	   veritytab(5)

       fido2-cid=
	   crypttab(5)

       fido2-device=
	   crypttab(5)

       fido2-rp=
	   crypttab(5)

       format=
	   veritytab(5)

       hash-block-size=
	   veritytab(5)

       hash-offset=
	   veritytab(5)

       hash=
	   crypttab(5), veritytab(5)

       header=
	   crypttab(5)

       headless=
	   crypttab(5)

       ignore-corruption
	   veritytab(5)

       ignore-zero-blocks
	   veritytab(5)

       key-slot=
	   crypttab(5)

       keyfile-erase
	   crypttab(5)

       keyfile-offset=
	   crypttab(5)

       keyfile-size=
	   crypttab(5)

       keyfile-timeout=
	   crypttab(5)

       luks
	   crypttab(5)

       no-read-workqueue
	   crypttab(5)

       no-write-workqueue
	   crypttab(5)

       noauto
	   crypttab(5), systemd.mount(5), systemd.swap(5), veritytab(5)

       nofail
	   crypttab(5), systemd.mount(5), systemd.swap(5), veritytab(5)

       offset=
	   crypttab(5)

       panic-on-corruption
	   veritytab(5)

       password-echo=
	   crypttab(5)

       pkcs11-uri=
	   crypttab(5)

       plain
	   crypttab(5)

       read-only
	   crypttab(5)

       readonly
	   crypttab(5)

       restart-on-corruption
	   veritytab(5)

       root-hash-signature=
	   veritytab(5)

       salt=
	   veritytab(5)

       same-cpu-crypt
	   crypttab(5)

       sector-size=
	   crypttab(5)

       size=
	   crypttab(5)

       skip=
	   crypttab(5)

       submit-from-crypt-cpus
	   crypttab(5)

       superblock=
	   veritytab(5)

       swap
	   crypttab(5)

       tcrypt
	   crypttab(5)

       tcrypt-hidden
	   crypttab(5)

       tcrypt-keyfile=
	   crypttab(5)

       tcrypt-system
	   crypttab(5)

       tcrypt-veracrypt
	   crypttab(5)

       timeout=
	   crypttab(5)

       tmp=
	   crypttab(5)

       token-timeout=
	   crypttab(5)

       tpm2-device=
	   crypttab(5)

       tpm2-measure-bank=
	   crypttab(5)

       tpm2-measure-pcr=
	   crypttab(5)

       tpm2-pcrlock=
	   crypttab(5)

       tpm2-pcrs=
	   crypttab(5)

       tpm2-pin=
	   crypttab(5)

       tpm2-signature=
	   crypttab(5)

       tries=
	   crypttab(5)

       try-empty-password=
	   crypttab(5)

       uuid=
	   veritytab(5)

       veracrypt-pim=
	   crypttab(5)

       verify
	   crypttab(5)

       x-initrd.attach
	   crypttab(5), veritytab(5)

       x-initrd.mount
	   systemd.mount(5)

       x-systemd.after=
	   systemd.mount(5)

       x-systemd.automount
	   systemd.mount(5)

       x-systemd.before=
	   systemd.mount(5)

       x-systemd.device-bound=
	   systemd.mount(5)

       x-systemd.device-timeout=
	   crypttab(5), systemd.mount(5), systemd.swap(5)

       x-systemd.growfs
	   systemd.mount(5)

       x-systemd.idle-timeout=
	   systemd.mount(5)

       x-systemd.makefs
	   systemd.mount(5), systemd.swap(5)

       x-systemd.mount-timeout=
	   systemd.mount(5)

       x-systemd.pcrfs
	   systemd.mount(5)

       x-systemd.required-by=
	   systemd.mount(5)

       x-systemd.requires-mounts-for=
	   systemd.mount(5)

       x-systemd.requires=
	   systemd.mount(5)

       x-systemd.rw-only
	   systemd.mount(5)

       x-systemd.wanted-by=
	   systemd.mount(5)

SYSTEMD.NSPAWN(5) DIRECTIVES
       Directives for configuring systemd-nspawn containers.

       AmbientCapability=
	   systemd.nspawn(5)

       Bind=
	   systemd.nspawn(5)

       BindReadOnly=
	   systemd.nspawn(5)

       BindUser=
	   systemd.nspawn(5)

       Boot=
	   systemd.nspawn(5)

       Bridge=
	   systemd.nspawn(5)

       CPUAffinity=
	   systemd.nspawn(5)

       Capability=
	   systemd.nspawn(5)

       DropCapability=
	   systemd.nspawn(5)

       Environment=
	   systemd.nspawn(5)

       Ephemeral=
	   systemd.nspawn(5)

       Hostname=
	   systemd.nspawn(5)

       IPVLAN=
	   systemd.nspawn(5)

       Inaccessible=
	   systemd.nspawn(5)

       Interface=
	   systemd.nspawn(5)

       KillSignal=
	   systemd.nspawn(5)

       LimitAS=
	   systemd.nspawn(5)

       LimitCORE=
	   systemd.nspawn(5)

       LimitCPU=
	   systemd.nspawn(5)

       LimitDATA=
	   systemd.nspawn(5)

       LimitFSIZE=
	   systemd.nspawn(5)

       LimitLOCKS=
	   systemd.nspawn(5)

       LimitMEMLOCK=
	   systemd.nspawn(5)

       LimitMSGQUEUE=
	   systemd.nspawn(5)

       LimitNICE=
	   systemd.nspawn(5)

       LimitNOFILE=
	   systemd.nspawn(5)

       LimitNPROC=
	   systemd.nspawn(5)

       LimitRSS=
	   systemd.nspawn(5)

       LimitRTPRIO=
	   systemd.nspawn(5)

       LimitRTTIME=
	   systemd.nspawn(5)

       LimitSIGPENDING=
	   systemd.nspawn(5)

       LimitSTACK=
	   systemd.nspawn(5)

       LinkJournal=
	   systemd.nspawn(5)

       MACVLAN=
	   systemd.nspawn(5)

       MachineID=
	   systemd.nspawn(5)

       NoNewPrivileges=
	   systemd.nspawn(5)

       NotifyReady=
	   systemd.nspawn(5)

       OOMScoreAdjust=
	   systemd.nspawn(5)

       Overlay=
	   systemd.nspawn(5)

       OverlayReadOnly=
	   systemd.nspawn(5)

       Parameters=
	   systemd.nspawn(5)

       Personality=
	   systemd.nspawn(5)

       PivotRoot=
	   systemd.nspawn(5)

       Port=
	   systemd.nspawn(5)

       Private=
	   systemd.nspawn(5)

       PrivateUsers=
	   systemd.nspawn(5)

       PrivateUsersOwnership=
	   systemd.nspawn(5)

       ProcessTwo=
	   systemd.nspawn(5)

       ReadOnly=
	   systemd.nspawn(5)

       ResolvConf=
	   systemd.nspawn(5)

       SuppressSync=
	   systemd.nspawn(5)

       SystemCallFilter=
	   systemd.nspawn(5)

       TemporaryFileSystem=
	   systemd.nspawn(5)

       Timezone=
	   systemd.nspawn(5)

       User=
	   systemd.nspawn(5)

       VirtualEthernet=
	   systemd.nspawn(5)

       VirtualEthernetExtra=
	   systemd.nspawn(5)

       Volatile=
	   systemd.nspawn(5)

       WorkingDirectory=
	   systemd.nspawn(5)

       Zone=
	   systemd.nspawn(5)

PROGRAM CONFIGURATION OPTIONS
       Directives for configuring the behaviour of the systemd process and other tools through configuration files.

       AllowHibernation=
	   systemd-sleep.conf(5)

       AllowHybridSleep=
	   systemd-sleep.conf(5)

       AllowSuspend=
	   systemd-sleep.conf(5)

       AllowSuspendThenHibernate=
	   systemd-sleep.conf(5)

       Audit=
	   journald.conf(5)

       CPUAffinity=
	   systemd-system.conf(5)

       CapabilityBoundingSet=
	   systemd-system.conf(5)

       Compress=
	   coredump.conf(5), journald.conf(5)

       CrashChangeVT=
	   systemd-system.conf(5)

       CrashReboot=
	   systemd-system.conf(5)

       CrashShell=
	   systemd-system.conf(5)

       CtrlAltDelBurstAction=
	   systemd-system.conf(5)

       DefaultCPUAccounting=
	   systemd-system.conf(5)

       DefaultDeviceTimeoutSec=
	   systemd-system.conf(5)

       DefaultEnvironment=
	   systemd-system.conf(5)

       DefaultIOAccounting=
	   systemd-system.conf(5)

       DefaultIPAccounting=
	   systemd-system.conf(5)

       DefaultLimitAS=
	   systemd-system.conf(5)

       DefaultLimitCORE=
	   systemd-system.conf(5)

       DefaultLimitCPU=
	   systemd-system.conf(5)

       DefaultLimitDATA=
	   systemd-system.conf(5)

       DefaultLimitFSIZE=
	   systemd-system.conf(5)

       DefaultLimitLOCKS=
	   systemd-system.conf(5)

       DefaultLimitMEMLOCK=
	   systemd-system.conf(5)

       DefaultLimitMSGQUEUE=
	   systemd-system.conf(5)

       DefaultLimitNICE=
	   systemd-system.conf(5)

       DefaultLimitNOFILE=
	   systemd-system.conf(5)

       DefaultLimitNPROC=
	   systemd-system.conf(5)

       DefaultLimitRSS=
	   systemd-system.conf(5)

       DefaultLimitRTPRIO=
	   systemd-system.conf(5)

       DefaultLimitRTTIME=
	   systemd-system.conf(5)

       DefaultLimitSIGPENDING=
	   systemd-system.conf(5)

       DefaultLimitSTACK=
	   systemd-system.conf(5)

       DefaultMemoryAccounting=
	   systemd-system.conf(5)

       DefaultMemoryPressureDurationSec=
	   oomd.conf(5)

       DefaultMemoryPressureLimit=
	   oomd.conf(5)

       DefaultMemoryPressureThresholdSec=
	   systemd-system.conf(5)

       DefaultMemoryPressureWatch=
	   systemd-system.conf(5)

       DefaultOOMPolicy=
	   systemd-system.conf(5)

       DefaultOOMScoreAdjust=
	   systemd-system.conf(5)

       DefaultRestartSec=
	   systemd-system.conf(5)

       DefaultSmackProcessLabel=
	   systemd-system.conf(5)

       DefaultStandardError=
	   systemd-system.conf(5)

       DefaultStandardOutput=
	   systemd-system.conf(5)

       DefaultStartLimitBurst=
	   systemd-system.conf(5)

       DefaultStartLimitIntervalSec=
	   systemd-system.conf(5)

       DefaultTasksAccounting=
	   systemd-system.conf(5)

       DefaultTasksMax=
	   systemd-system.conf(5)

       DefaultTimeoutAbortSec=
	   systemd-system.conf(5)

       DefaultTimeoutStartSec=
	   systemd-system.conf(5)

       DefaultTimeoutStopSec=
	   systemd-system.conf(5)

       DefaultTimerAccuracySec=
	   systemd-system.conf(5)

       DumpCore=
	   systemd-system.conf(5)

       ExternalSizeMax=
	   coredump.conf(5)

       ForwardToConsole=
	   journald.conf(5)

       ForwardToKMsg=
	   journald.conf(5)

       ForwardToSyslog=
	   journald.conf(5)

       ForwardToWall=
	   journald.conf(5)

       HandleHibernateKey=
	   logind.conf(5)

       HandleHibernateKeyLongPress=
	   logind.conf(5)

       HandleLidSwitch=
	   logind.conf(5)

       HandleLidSwitchDocked=
	   logind.conf(5)

       HandleLidSwitchExternalPower=
	   logind.conf(5)

       HandlePowerKey=
	   logind.conf(5)

       HandlePowerKeyLongPress=
	   logind.conf(5)

       HandleRebootKey=
	   logind.conf(5)

       HandleRebootKeyLongPress=
	   logind.conf(5)

       HandleSuspendKey=
	   logind.conf(5)

       HandleSuspendKeyLongPress=
	   logind.conf(5)

       HibernateDelaySec=
	   systemd-sleep.conf(5)

       HibernateKeyIgnoreInhibited=
	   logind.conf(5)

       HibernateMode=
	   systemd-sleep.conf(5)

       HoldoffTimeoutSec=
	   logind.conf(5)

       IdleAction=
	   logind.conf(5)

       IdleActionSec=
	   logind.conf(5)

       InhibitDelayMaxSec=
	   logind.conf(5)

       InhibitorsMax=
	   logind.conf(5)

       JournalSizeMax=
	   coredump.conf(5)

       KExecWatchdogSec=
	   systemd-system.conf(5)

       KeepFree=
	   coredump.conf(5), journal-remote.conf(5)

       KillExcludeUsers=
	   logind.conf(5)

       KillOnlyUsers=
	   logind.conf(5)

       KillUserProcesses=
	   logind.conf(5)

       LidSwitchIgnoreInhibited=
	   logind.conf(5)

       LineMax=
	   journald.conf(5)

       LogColor=
	   systemd-system.conf(5)

       LogLevel=
	   systemd-system.conf(5)

       LogLocation=
	   systemd-system.conf(5)

       LogTarget=
	   systemd-system.conf(5)

       LogTime=
	   systemd-system.conf(5)

       ManagerEnvironment=
	   systemd-system.conf(5)

       MaxFileSec=
	   journald.conf(5)

       MaxFileSize=
	   journal-remote.conf(5)

       MaxFiles=
	   journal-remote.conf(5)

       MaxLevelConsole=
	   journald.conf(5)

       MaxLevelKMsg=
	   journald.conf(5)

       MaxLevelStore=
	   journald.conf(5)

       MaxLevelSyslog=
	   journald.conf(5)

       MaxLevelWall=
	   journald.conf(5)

       MaxRetentionSec=
	   journald.conf(5)

       MaxUse=
	   coredump.conf(5), journal-remote.conf(5)

       NAutoVTs=
	   logind.conf(5)

       NUMAMask=
	   systemd-system.conf(5)

       NUMAPolicy=
	   systemd-system.conf(5)

       NetworkTimeoutSec=
	   journal-upload.conf(5)

       NoNewPrivileges=
	   systemd-system.conf(5)

       PowerKeyIgnoreInhibited=
	   logind.conf(5)

       ProcessSizeMax=
	   coredump.conf(5)

       RateLimitBurst=
	   journald.conf(5)

       RateLimitIntervalSec=
	   journald.conf(5)

       ReadKMsg=
	   journald.conf(5)

       RebootKeyIgnoreInhibited=
	   logind.conf(5)

       RebootWatchdogSec=
	   systemd-system.conf(5)

       ReloadLimitBurst=
	   systemd-system.conf(5)

       ReloadLimitIntervalSec=
	   systemd-system.conf(5)

       RemoveIPC=
	   logind.conf(5)

       ReserveVT=
	   logind.conf(5)

       RuntimeDirectoryInodesMax=
	   logind.conf(5)

       RuntimeDirectorySize=
	   logind.conf(5)

       RuntimeKeepFree=
	   journald.conf(5)

       RuntimeMaxFileSize=
	   journald.conf(5)

       RuntimeMaxFiles=
	   journald.conf(5)

       RuntimeMaxUse=
	   journald.conf(5)

       RuntimeWatchdogPreGovernor=
	   systemd-system.conf(5)

       RuntimeWatchdogPreSec=
	   systemd-system.conf(5)

       RuntimeWatchdogSec=
	   systemd-system.conf(5)

       Seal=
	   journal-remote.conf(5), journald.conf(5)

       ServerCertificateFile=
	   journal-remote.conf(5), journal-upload.conf(5)

       ServerKeyFile=
	   journal-remote.conf(5), journal-upload.conf(5)

       SessionsMax=
	   logind.conf(5)

       ShowStatus=
	   systemd-system.conf(5)

       SplitMode=
	   journal-remote.conf(5), journald.conf(5)

       StatusUnitFormat=
	   systemd-system.conf(5)

       StopIdleSessionSec=
	   logind.conf(5)

       Storage=
	   coredump.conf(5), journald.conf(5), pstore.conf(5)

       SuspendEstimationSec=
	   systemd-sleep.conf(5)

       SuspendKeyIgnoreInhibited=
	   logind.conf(5)

       SuspendState=
	   systemd-sleep.conf(5)

       SwapUsedLimit=
	   oomd.conf(5)

       SyncIntervalSec=
	   journald.conf(5)

       SystemCallArchitectures=
	   systemd-system.conf(5)

       SystemKeepFree=
	   journald.conf(5)

       SystemMaxFileSize=
	   journald.conf(5)

       SystemMaxFiles=
	   journald.conf(5)

       SystemMaxUse=
	   journald.conf(5)

       TTYPath=
	   journald.conf(5)

       TargetSolution=
	   iocost.conf(5)

       TimerSlackNSec=
	   systemd-system.conf(5)

       TrustedCertificateFile=
	   journal-remote.conf(5), journal-upload.conf(5)

       URL=
	   journal-upload.conf(5)

       Unlink=
	   pstore.conf(5)

       UserStopDelaySec=
	   logind.conf(5)

       WatchdogDevice=
	   systemd-system.conf(5)

       children_max=
	   udev.conf(5)

       event_timeout=
	   udev.conf(5)

       exec_delay=
	   udev.conf(5)

       resolve_names=
	   udev.conf(5)

       timeout_signal=
	   udev.conf(5)

       udev_log=
	   udev.conf(5)

COMMAND LINE OPTIONS
       Command-line options accepted by programs in the systemd suite.

       --accept
	   systemd-socket-activate(1)

       --accept-cached
	   systemd-ask-password(1)

       --access-mode
	   homectl(1)

       --acquired
	   busctl(1)

       --action
	   udevadm(8)

       --activatable
	   busctl(1)

       --address
	   busctl(1)

       --adjust-system-clock
	   timedatectl(1)

       --after
	   systemctl(1)

       --after-cursor
	   journalctl(1), systemd-journal-upload.service(8)

       --all
	   coredumpctl(1), journalctl(1), loginctl(1), machinectl(1), networkctl(1), systemctl(1), systemd-cgls(1), systemd-storagetm.service(8),
	   timedatectl(1), ukify(1)

       --all-architectures
	   bootctl(1)

       --allow-interactive-authorization
	   busctl(1)

       --ambient-capability
	   systemd-nspawn(1)

       --any
	   systemd-networkd-wait-online.service(8)

       --app-specific
	   systemd-id128(1)

       --append
	   systemd-measure(1)

       --architecture
	   systemd-repart(8)

       --are-updates-enabled
	   resolvectl(1)

       --as-pid2
	   systemd-nspawn(1)

       --attach
	   systemd-dissect(1)

       --attr-match[=FILE[=VALUE]]
	   udevadm(8)

       --attr-nomatch[=FILE[=VALUE]]
	   udevadm(8)

       --attribute-walk
	   udevadm(8)

       --augment-creds
	   busctl(1)

       --auto-login
	   homectl(1)

       --auto-resize-mode
	   homectl(1)

       --auto-start
	   busctl(1)

       --automount
	   systemd-mount(1)

       --automount-property
	   systemd-mount(1)

       --backing
	   udevadm(8)

       --bank
	   systemd-measure(1), systemd-pcrphase.service(8)

       --base-time
	   systemd-analyze(1)

       --batch
	   systemd-cgtop(1)

       --before
	   systemctl(1)

       --bind
	   systemd-nspawn(1)

       --bind-device
	   systemd-mount(1)

       --bind-ro
	   systemd-nspawn(1)

       --bind-user
	   systemd-nspawn(1)

       --boot[=[ID][±offset]|all]
	   journalctl(1), systemd-nspawn(1), systemd-tmpfiles(8)

       --boot-loader-entry
	   systemctl(1)

       --boot-loader-menu
	   systemctl(1)

       --boot-path
	   bootctl(1), kernel-install(8)

       --booted
	   systemd-notify(1)

       --bus-path
	   systemd-stdio-bridge(1)

       --cache
	   resolvectl(1)

       --can-factory-reset
	   systemd-repart(8)

       --capability
	   systemd-nspawn(1)

       --capability-ambient-set
	   homectl(1)

       --capability-bounding-set
	   homectl(1)

       --case-sensitive[=BOOLEAN]
	   journalctl(1)

       --cat
	   portablectl(1)

       --cat-config
	   systemd-binfmt.service(8), systemd-sysctl.service(8), systemd-sysusers(8), systemd-tmpfiles(8)

       --catalog
	   journalctl(1)

       --cert
	   systemd-journal-gatewayd.service(8), systemd-journal-remote.service(8), systemd-journal-upload.service(8)

       --certificate
	   systemd-repart(8)

       --cgroup-id
	   systemd-cgls(1)

       --chain
	   userdbctl(1)

       --chdir
	   systemd-nspawn(1)

       --check-inhibitors
	   systemctl(1)

       --children-max
	   systemd-udevd.service(8), udevadm(8)

       --chroot
	   systemd-detect-virt(1)

       --cifs-domain
	   homectl(1)

       --cifs-extra-mount-options
	   homectl(1)

       --cifs-service
	   homectl(1)

       --cifs-user-name
	   homectl(1)

       --class
	   resolvectl(1)

       --clean
	   systemd-tmpfiles(8)

       --cleanup-db
	   udevadm(8)

       --cmdline
	   systemd-measure(1), ukify(1)

       --cname
	   resolvectl(1)

       --collect
	   systemd-mount(1), systemd-run(1)

       --commit
	   systemd-machine-id-setup(1)

       --component
	   systemd-sysupdate(8)

       --components
	   systemd-pcrlock(8)

       --compress
	   systemd-journal-remote.service(8)

       --config
	   ukify(1)

       --confirm-spawn
	   systemd(1)

       --connections-max
	   systemd-socket-proxyd(8)

       --console
	   systemd-nspawn(1), systemd-tty-ask-password-agent(1)

       --container
	   systemd-detect-virt(1)

       --continuous
	   systemd-bsod.service(8)

       --copy
	   portablectl(1), systemd-firstboot(1)

       --copy-from
	   systemd-dissect(1), systemd-repart(8)

       --copy-keymap
	   systemd-firstboot(1)

       --copy-locale
	   systemd-firstboot(1)

       --copy-root-password
	   systemd-firstboot(1)

       --copy-root-shell
	   systemd-firstboot(1)

       --copy-source
	   systemd-repart(8)

       --copy-timezone
	   systemd-firstboot(1)

       --copy-to
	   systemd-dissect(1)

       --cpu
	   systemd-cgtop(1)

       --cpu-affinity
	   systemd-nspawn(1)

       --cpu-weight
	   homectl(1)

       --crash-reboot
	   systemd(1)

       --crash-shell
	   systemd(1)

       --crash-vt
	   systemd(1)

       --create
	   systemd-tmpfiles(8)

       --credential
	   systemd-ask-password(1)

       --current
	   systemd-measure(1)

       --cursor
	   journalctl(1), systemd-journal-upload.service(8)

       --cursor-file
	   journalctl(1)

       --cvm
	   systemd-detect-virt(1)

       --daemon
	   systemd-udevd.service(8)

       --datagram
	   systemd-socket-activate(1)

       --debug
	   systemd-udevd.service(8), udevadm(8)

       --debugger
	   coredumpctl(1)

       --debugger-arguments
	   coredumpctl(1)

       --default-standard-error
	   systemd(1)

       --default-standard-output
	   systemd(1)

       --defer-partitions
	   systemd-repart(8)

       --definitions
	   systemd-repart(8), systemd-sysupdate(8)

       --delay
	   systemd-cgtop(1)

       --delete-root-password
	   systemd-firstboot(1)

       --depth
	   systemd-cgtop(1)

       --description
	   systemd-mount(1), systemd-run(1)

       --destination
	   busctl(1)

       --detach
	   systemd-dissect(1)

       --device
	   udevadm(8)

       --device-id-of-file
	   udevadm(8)

       --devicetree
	   ukify(1)

       --diff
	   systemd-delta(1)

       --directory
	   coredumpctl(1), journalctl(1), systemd-journal-gatewayd.service(8), systemd-journal-upload.service(8), systemd-nspawn(1)

       --disable-updates
	   resolvectl(1)

       --discard
	   systemd-dissect(1), systemd-repart(8)

       --discover
	   systemd-dissect(1), systemd-mount(1)

       --disk-size
	   homectl(1)

       --disk-usage
	   journalctl(1)

       --dmesg
	   journalctl(1)

       --drop-caches
	   homectl(1)

       --drop-capability
	   systemd-nspawn(1)

       --drop-in
	   networkctl(1), systemctl(1)

       --dry-run
	   bootctl(1), systemctl(1), systemd-oomd.service(8), systemd-repart(8), systemd-sysusers(8), udevadm(8)

       --dtb
	   systemd-measure(1)

       --dump-bus-properties
	   systemd(1)

       --dump-catalog
	   journalctl(1)

       --dump-configuration-items
	   systemd(1)

       --dump-core
	   systemd(1)

       --echo
	   systemd-ask-password(1)

       --efi-boot-option-description
	   bootctl(1)

       --email-address
	   homectl(1)

       --emoji
	   systemd-ask-password(1)

       --empty
	   systemd-repart(8)

       --enable
	   portablectl(1)

       --enable-updates
	   resolvectl(1)

       --enforce-password-policy
	   homectl(1)

       --entry-token
	   bootctl(1), kernel-install(8)

       --ephemeral
	   systemd-nspawn(1)

       --esp-path
	   bootctl(1), kernel-install(8)

       --event-timeout
	   systemd-udevd.service(8)

       --exclude-partitions
	   systemd-repart(8)

       --exclude-prefix
	   systemd-tmpfiles(8)

       --exec
	   systemd-notify(1)

       --exec-delay
	   systemd-udevd.service(8)

       --exit
	   udevadm(8)

       --exit-idle-time
	   systemd-socket-proxyd(8)

       --exit-if-exists
	   udevadm(8)

       --expand-environment
	   systemd-run(1)

       --expect-reply
	   busctl(1)

       --export
	   udevadm(8)

       --export-db
	   udevadm(8)

       --export-format
	   homectl(1)

       --export-prefix
	   udevadm(8)

       --extension
	   portablectl(1)

       --facility
	   journalctl(1)

       --factory-reset
	   systemd-repart(8)

       --fail
	   systemctl(1)

       --failed
	   systemctl(1)

       --fd
	   systemd-notify(1)

       --fdname
	   systemd-notify(1), systemd-socket-activate(1)

       --fido2-credential-algorithm
	   homectl(1), systemd-cryptenroll(1)

       --fido2-device
	   homectl(1), systemd-cryptenroll(1)

       --fido2-with-client-pin
	   homectl(1), systemd-cryptenroll(1)

       --fido2-with-user-presence
	   homectl(1), systemd-cryptenroll(1)

       --fido2-with-user-verification
	   homectl(1), systemd-cryptenroll(1)

       --field
	   coredumpctl(1), journalctl(1)

       --fields
	   journalctl(1)

       --file
	   coredumpctl(1), journalctl(1), systemd-journal-gatewayd.service(8), systemd-journal-upload.service(8)

       --file-system
	   systemd-pcrphase.service(8)

       --firmware-setup
	   systemctl(1)

       --flush
	   journalctl(1)

       --follow
	   journalctl(1), systemd-journal-upload.service(8)

       --force
	   journalctl(1), machinectl(1), portablectl(1), poweroff(8), systemctl(1), systemd-firstboot(1), systemd-pcrlock(8), systemd-sysext(8)

       --format
	   machinectl(1)

       --from-pattern
	   systemd-analyze(1)

       --fs-type
	   homectl(1)

       --fsck
	   systemd-dissect(1), systemd-mount(1)

       --full
	   busctl(1), journalctl(1), loginctl(1), machinectl(1), networkctl(1), systemctl(1), systemd-cgls(1), systemd-mount(1)

       --fuzz
	   systemd-analyze(1)

       --generators
	   systemd-analyze(1)

       --getter
	   systemd-journal-remote.service(8)

       --gid
	   systemd-run(1)

       --global
	   systemctl(1), systemd-analyze(1)

       --gnutls-log
	   systemd-journal-remote.service(8)

       --graceful
	   bootctl(1), systemd-pcrphase.service(8), systemd-tmpfiles(8)

       --grep
	   journalctl(1)

       --growfs
	   systemd-dissect(1)

       --halt
	   poweroff(8), shutdown(8)

       --header
	   journalctl(1)

       --help
	   bootctl(1), busctl(1), coredumpctl(1), homectl(1), hostnamectl(1), journalctl(1), kernel-install(8), localectl(1), loginctl(1), machinectl(1),
	   networkctl(1), oomctl(1), portablectl(1), poweroff(8), resolvectl(1), runlevel(8), shutdown(8), systemctl(1), systemd(1), systemd-ac-power(1),
	   systemd-analyze(1), systemd-ask-password(1), systemd-battery-check.service(8), systemd-binfmt.service(8), systemd-bless-boot.service(8), systemd-
	   bsod.service(8), systemd-cat(1), systemd-cgls(1), systemd-cgtop(1), systemd-creds(1), systemd-cryptenroll(1), systemd-delta(1), systemd-detect-
	   virt(1), systemd-dissect(1), systemd-escape(1), systemd-firstboot(1), systemd-fsckd.service(8), systemd-hwdb(8), systemd-id128(1), systemd-
	   inhibit(1), systemd-journal-gatewayd.service(8), systemd-journal-remote.service(8), systemd-journal-upload.service(8), systemd-machine-id-setup(1),
	   systemd-measure(1), systemd-mount(1), systemd-networkd-wait-online.service(8), systemd-notify(1), systemd-nspawn(1), systemd-path(1), systemd-
	   pcrlock(8), systemd-pcrphase.service(8), systemd-repart(8), systemd-run(1), systemd-socket-activate(1), systemd-socket-proxyd(8), systemd-stdio-
	   bridge(1), systemd-storagetm.service(8), systemd-suspend.service(8), systemd-sysctl.service(8), systemd-sysext(8), systemd-sysupdate(8), systemd-
	   sysusers(8), systemd-tmpfiles(8), systemd-tty-ask-password-agent(1), systemd-udevd.service(8), telinit(8), timedatectl(1), udevadm(8), ukify(1),
	   userdbctl(1), varlinkctl(1)

       --home-dir
	   homectl(1)

       --host
	   busctl(1), homectl(1), hostnamectl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd-analyze(1), systemd-
	   mount(1), systemd-run(1), timedatectl(1)

       --hostname
	   systemd-firstboot(1), systemd-nspawn(1)

       --icon
	   systemd-ask-password(1)

       --icon-name
	   homectl(1)

       --id
	   systemd-ask-password(1)

       --identifier
	   journalctl(1), systemd-cat(1)

       --identity
	   homectl(1)

       --ignore
	   systemd-networkd-wait-online.service(8)

       --image
	   bootctl(1), coredumpctl(1), journalctl(1), kernel-install(8), systemctl(1), systemd-analyze(1), systemd-firstboot(1), systemd-machine-id-setup(1),
	   systemd-nspawn(1), systemd-repart(8), systemd-sysupdate(8), systemd-sysusers(8), systemd-tmpfiles(8)

       --image-path
	   homectl(1)

       --image-policy
	   bootctl(1), coredumpctl(1), journalctl(1), kernel-install(8), systemctl(1), systemd-analyze(1), systemd-dissect(1), systemd-machine-id-setup(1),
	   systemd-nspawn(1), systemd-repart(8), systemd-sysext(8), systemd-sysupdate(8), systemd-sysusers(8), systemd-tmpfiles(8)

       --in-memory
	   systemd-dissect(1)

       --inaccessible
	   systemd-nspawn(1)

       --include-partitions
	   systemd-repart(8)

       --inetd
	   systemd-socket-activate(1)

       --initialized
	   udevadm(8)

       --initialized-match
	   udevadm(8)

       --initialized-nomatch
	   udevadm(8)

       --initrd
	   systemd-measure(1), ukify(1)

       --inline
	   systemd-sysusers(8)

       --install-source
	   bootctl(1)

       --instance
	   systemd-escape(1)

       --instances-max
	   systemd-sysupdate(8)

       --interface
	   resolvectl(1), systemd-networkd-wait-online.service(8)

       --interval
	   journalctl(1)

       --io-weight
	   homectl(1)

       --ipv4
	   systemd-networkd-wait-online.service(8)

       --ipv6
	   systemd-networkd-wait-online.service(8)

       --iterations
	   systemd-analyze(1), systemd-cgtop(1)

       --job-mode
	   systemctl(1)

       --json
	   bootctl(1), busctl(1), coredumpctl(1), homectl(1), hostnamectl(1), kernel-install(8), networkctl(1), resolvectl(1), systemd-analyze(1), systemd-
	   creds(1), systemd-dissect(1), systemd-measure(1), systemd-pcrlock(8), systemd-repart(8), systemd-sysext(8), systemd-sysupdate(8), udevadm(8),
	   ukify(1), userdbctl(1), varlinkctl(1)

       --keep-unit
	   systemd-nspawn(1)

       --kernel
	   udevadm(8)

       --kernel-command-line
	   systemd-firstboot(1)

       --key
	   systemd-journal-gatewayd.service(8), systemd-journal-remote.service(8), systemd-journal-upload.service(8)

       --key-file
	   systemd-repart(8)

       --keymap
	   systemd-firstboot(1)

       --keyname
	   systemd-ask-password(1)

       --kill-processes
	   homectl(1)

       --kill-signal
	   systemd-nspawn(1)

       --kill-value
	   systemctl(1)

       --kill-whom
	   loginctl(1), machinectl(1), systemctl(1)

       --language
	   homectl(1)

       --legend
	   resolvectl(1), systemctl(1)

       --level-prefix
	   systemd-cat(1)

       --lines
	   journalctl(1), loginctl(1), machinectl(1), networkctl(1), systemctl(1)

       --link-journal
	   systemd-nspawn(1)

       --linux
	   systemd-measure(1), ukify(1)

       --list
	   busctl(1), systemd-detect-virt(1), systemd-dissect(1), systemd-inhibit(1), systemd-mount(1), systemd-tty-ask-password-agent(1)

       --list-boots
	   journalctl(1)

       --list-catalog
	   journalctl(1)

       --list-cvm
	   systemd-detect-virt(1)

       --listen
	   systemd-socket-activate(1)

       --listen-http
	   systemd-journal-remote.service(8)

       --listen-https
	   systemd-journal-remote.service(8)

       --listen-raw
	   systemd-journal-remote.service(8)

       --load-credential
	   systemd-nspawn(1)

       --locale
	   systemd-firstboot(1)

       --locale-messages
	   systemd-firstboot(1)

       --location
	   homectl(1), systemd-pcrlock(8)

       --locked
	   homectl(1)

       --log-color
	   systemd(1)

       --log-level
	   systemd(1), udevadm(8)

       --log-location
	   systemd(1)

       --log-target
	   systemd(1)

       --log-time
	   systemd(1)

       --loop-ref
	   systemd-dissect(1)

       --low
	   systemd-ac-power(1)

       --luks-cipher
	   homectl(1)

       --luks-cipher-mode
	   homectl(1)

       --luks-discard
	   homectl(1)

       --luks-extra-mount-options
	   homectl(1)

       --luks-offline-discard
	   homectl(1)

       --luks-pbkdf-force-iterations
	   homectl(1)

       --luks-pbkdf-hash-algorithm
	   homectl(1)

       --luks-pbkdf-memory-cost
	   homectl(1)

       --luks-pbkdf-parallel-threads
	   homectl(1)

       --luks-pbkdf-time-cost
	   homectl(1)

       --luks-pbkdf-type
	   homectl(1)

       --luks-sector-size
	   homectl(1)

       --luks-volume-key-size
	   homectl(1)

       --machine
	   busctl(1), homectl(1), hostnamectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd-analyze(1),
	   systemd-cgls(1), systemd-cgtop(1), systemd-mount(1), systemd-nspawn(1), systemd-run(1), systemd-stdio-bridge(1), timedatectl(1)

       --machine-id
	   systemd(1), systemd-firstboot(1), systemd-pcrphase.service(8)

       --make-ddi
	   systemd-repart(8)

       --make-entry-directory
	   bootctl(1), kernel-install(8)

       --man
	   systemd-analyze(1)

       --mangle
	   systemd-escape(1)

       --marked
	   systemctl(1)

       --match
	   busctl(1)

       --max-addresses
	   machinectl(1)

       --measure
	   ukify(1)

       --member-of
	   homectl(1)

       --memory-high
	   homectl(1)

       --memory-max
	   homectl(1)

       --merge
	   journalctl(1), systemd-journal-gatewayd.service(8), systemd-journal-upload.service(8)

       --message
	   systemctl(1)

       --mkdir
	   machinectl(1), systemctl(1), systemd-dissect(1)

       --mode
	   systemd-inhibit(1)

       --monitor
	   timedatectl(1)

       --more
	   varlinkctl(1)

       --mount
	   systemd-dissect(1)

       --mtree
	   systemd-dissect(1)

       --mtree-hash
	   systemd-dissect(1)

       --multiple
	   systemd-ask-password(1)

       --multiplexer
	   userdbctl(1)

       --name
	   systemd-creds(1), udevadm(8)

       --name-match[=NAME]
	   udevadm(8)

       --namespace
	   journalctl(1), systemd-journal-upload.service(8)

       --network
	   resolvectl(1)

       --network-bridge
	   systemd-nspawn(1)

       --network-interface
	   systemd-nspawn(1)

       --network-ipvlan
	   systemd-nspawn(1)

       --network-macvlan
	   systemd-nspawn(1)

       --network-namespace-path
	   systemd-nspawn(1)

       --network-veth
	   systemd-nspawn(1)

       --network-veth-extra
	   systemd-nspawn(1)

       --network-zone
	   systemd-nspawn(1)

       --newline
	   systemd-creds(1)

       --nice
	   homectl(1), systemd-run(1)

       --no-ask-password
	   homectl(1), hostnamectl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd-mount(1), systemd-run(1),
	   timedatectl(1)

       --no-block
	   portablectl(1), systemctl(1), systemd-mount(1), systemd-notify(1), systemd-run(1)

       --no-convert
	   localectl(1)

       --no-full
	   journalctl(1)

       --no-hostname
	   journalctl(1)

       --no-legend
	   busctl(1), coredumpctl(1), homectl(1), kernel-install(8), loginctl(1), machinectl(1), networkctl(1), portablectl(1), systemd-analyze(1), systemd-
	   creds(1), systemd-dissect(1), systemd-inhibit(1), systemd-mount(1), systemd-repart(8), systemd-sysext(8), systemd-sysupdate(8), userdbctl(1)

       --no-measure
	   ukify(1)

       --no-new-privileges
	   systemd-nspawn(1)

       --no-output
	   systemd-ask-password(1)

       --no-pager
	   bootctl(1), busctl(1), coredumpctl(1), homectl(1), journalctl(1), kernel-install(8), localectl(1), loginctl(1), machinectl(1), networkctl(1),
	   oomctl(1), portablectl(1), resolvectl(1), systemctl(1), systemd-analyze(1), systemd-binfmt.service(8), systemd-cgls(1), systemd-creds(1), systemd-
	   delta(1), systemd-dissect(1), systemd-inhibit(1), systemd-measure(1), systemd-mount(1), systemd-nspawn(1), systemd-path(1), systemd-pcrlock(8),
	   systemd-repart(8), systemd-sysctl.service(8), systemd-sysext(8), systemd-sysupdate(8), systemd-sysusers(8), systemd-tmpfiles(8), timedatectl(1),
	   udevadm(8), userdbctl(1), varlinkctl(1)

       --no-reload
	   networkctl(1), portablectl(1), systemctl(1), systemd-sysext(8)

       --no-sign-kernel
	   ukify(1)

       --no-style
	   udevadm(8)

       --no-summary
	   udevadm(8)

       --no-sync
	   poweroff(8)

       --no-tail
	   journalctl(1)

       --no-tty
	   systemd-ask-password(1)

       --no-variables
	   bootctl(1)

       --no-wall
	   poweroff(8), shutdown(8), systemctl(1), telinit(8)

       --no-warn
	   systemctl(1)

       --no-wtmp
	   poweroff(8)

       --nodev
	   homectl(1)

       --noexec
	   homectl(1), systemd-sysext(8)

       --nosuid
	   homectl(1)

       --not-after
	   homectl(1), systemd-creds(1)

       --not-before
	   homectl(1)

       --notify-ready
	   systemd-nspawn(1)

       --now
	   machinectl(1), portablectl(1), systemctl(1)

       --nqn
	   systemd-storagetm.service(8)

       --nv-index
	   systemd-pcrlock(8)

       --oci-bundle
	   systemd-nspawn(1)

       --offline
	   systemd-analyze(1), systemd-repart(8)

       --on-active
	   systemd-run(1)

       --on-boot
	   systemd-run(1)

       --on-calendar
	   systemd-run(1)

       --on-clock-change
	   systemd-run(1)

       --on-startup
	   systemd-run(1)

       --on-timezone-change
	   systemd-run(1)

       --on-unit-active
	   systemd-run(1)

       --on-unit-inactive
	   systemd-run(1)

       --oneway
	   varlinkctl(1)

       --oom-score-adjust
	   systemd-nspawn(1)

       --operational-state
	   systemd-networkd-wait-online.service(8)

       --options
	   systemd-mount(1)

       --order
	   systemd-analyze(1), systemd-cgtop(1)

       --os-release
	   ukify(1)

       --osrel
	   systemd-measure(1)

       --output
	   coredumpctl(1), journalctl(1), loginctl(1), machinectl(1), systemctl(1), systemd-journal-remote.service(8), ukify(1), userdbctl(1)

       --output-fields
	   journalctl(1)

       --overlay
	   systemd-nspawn(1)

       --overlay-ro
	   systemd-nspawn(1)

       --owner
	   systemd-mount(1)

       --pager-end
	   journalctl(1)

       --parent-match[=NAME]
	   udevadm(8)

       --password
	   systemd-cryptenroll(1)

       --password-change-inactive
	   homectl(1)

       --password-change-max
	   homectl(1)

       --password-change-min
	   homectl(1)

       --password-change-now
	   homectl(1)

       --password-change-warn
	   homectl(1)

       --password-hint
	   homectl(1)

       --path
	   systemd-escape(1), udevadm(8)

       --path-property
	   systemd-run(1)

       --pcr
	   systemd-pcrlock(8), systemd-pcrphase.service(8)

       --pcr-banks
	   ukify(1)

       --pcr-private-key
	   ukify(1)

       --pcr-public-key
	   ukify(1)

       --pcrlock
	   systemd-pcrlock(8)

       --pcrpkey
	   systemd-measure(1), ukify(1)

       --personality
	   systemd-nspawn(1)

       --phase
	   systemd-measure(1)

       --phases
	   ukify(1)

       --pid
	   systemd-notify(1)

       --ping
	   udevadm(8)

       --pipe
	   systemd-nspawn(1), systemd-run(1)

       --pivot-root
	   systemd-nspawn(1)

       --pkcs11-token-uri
	   homectl(1), systemd-cryptenroll(1)

       --plain
	   systemctl(1)

       --plymouth
	   systemd-tty-ask-password-agent(1)

       --policy
	   systemd-pcrlock(8)

       --port
	   systemd-nspawn(1)

       --poweroff
	   poweroff(8), shutdown(8)

       --prefix
	   systemd-sysctl.service(8), systemd-tmpfiles(8)

       --preset-mode
	   systemctl(1)

       --pretty
	   hostnamectl(1), systemd-creds(1), systemd-id128(1), systemd-repart(8)

       --print
	   systemd-machine-id-setup(1), udevadm(8)

       --print-boot-path
	   bootctl(1)

       --print-esp-path
	   bootctl(1)

       --print-root-device
	   bootctl(1)

       --prioritized-subsystem
	   udevadm(8)

       --priority
	   journalctl(1), systemd-cat(1)

       --private-key
	   systemd-measure(1), systemd-repart(8)

       --private-network
	   systemd-nspawn(1)

       --private-users
	   systemd-detect-virt(1), systemd-nspawn(1)

       --private-users-ownership
	   systemd-nspawn(1)

       --profile
	   portablectl(1), systemd-analyze(1)

       --prompt
	   systemd-firstboot(1)

       --prompt-hostname
	   systemd-firstboot(1)

       --prompt-keymap
	   systemd-firstboot(1)

       --prompt-locale
	   systemd-firstboot(1)

       --prompt-root-password
	   systemd-firstboot(1)

       --prompt-root-shell
	   systemd-firstboot(1)

       --prompt-timezone
	   systemd-firstboot(1)

       --property
	   loginctl(1), machinectl(1), systemctl(1), systemd-mount(1), systemd-nspawn(1), systemd-run(1), timedatectl(1), udevadm(8)

       --property-match[=KEY=VALUE]
	   udevadm(8)

       --protocol
	   resolvectl(1)

       --pty
	   systemd-run(1)

       --public-key
	   systemd-measure(1)

       --query
	   systemd-tty-ask-password-agent(1), udevadm(8)

       --quiet
	   bootctl(1), busctl(1), coredumpctl(1), journalctl(1), machinectl(1), portablectl(1), systemctl(1), systemd-analyze(1), systemd-creds(1), systemd-
	   detect-virt(1), systemd-mount(1), systemd-networkd-wait-online.service(8), systemd-nspawn(1), systemd-run(1), udevadm(8)

       --rate-limit-burst
	   homectl(1)

       --rate-limit-interval
	   homectl(1)

       --raw
	   resolvectl(1), systemd-cgtop(1)

       --raw-description
	   systemd-pcrlock(8)

       --read-only
	   machinectl(1), systemctl(1), systemd-dissect(1), systemd-nspawn(1)

       --ready
	   systemd-notify(1)

       --real-name
	   homectl(1)

       --realm
	   homectl(1)

       --rebalance-weight
	   homectl(1)

       --reboot
	   poweroff(8), shutdown(8), systemd-sysupdate(8)

       --reboot-argument
	   systemctl(1)

       --recovery-key
	   homectl(1), systemd-cryptenroll(1)

       --recovery-pin
	   systemd-pcrlock(8)

       --recursive
	   systemctl(1), systemd-cgtop(1)

       --recursive-errors
	   systemd-analyze(1)

       --register
	   systemd-nspawn(1)

       --relinquish-var
	   journalctl(1)

       --reload
	   udevadm(8)

       --reloading
	   systemd-notify(1)

       --remain-after-exit
	   systemd-run(1)

       --remove
	   systemd-tmpfiles(8)

       --removed
	   udevadm(8)

       --replace
	   systemd-sysusers(8), systemd-tmpfiles(8)

       --require
	   systemd-analyze(1)

       --reset
	   systemd-firstboot(1)

       --resolv-conf
	   systemd-nspawn(1)

       --resolve-names
	   systemd-udevd.service(8), udevadm(8)

       --reverse
	   coredumpctl(1), journalctl(1), systemctl(1)

       --rlimit
	   homectl(1), systemd-nspawn(1)

       --rmdir
	   systemd-dissect(1)

       --root
	   bootctl(1), coredumpctl(1), journalctl(1), kernel-install(8), systemctl(1), systemd-analyze(1), systemd-firstboot(1), systemd-hwdb(8), systemd-
	   machine-id-setup(1), systemd-repart(8), systemd-sysext(8), systemd-sysupdate(8), systemd-sysusers(8), systemd-tmpfiles(8), udevadm(8)

       --root-hash
	   systemd-dissect(1), systemd-nspawn(1)

       --root-hash-sig
	   systemd-dissect(1), systemd-nspawn(1)

       --root-password
	   systemd-firstboot(1)

       --root-password-file
	   systemd-firstboot(1)

       --root-password-hashed
	   systemd-firstboot(1)

       --root-shell
	   systemd-firstboot(1)

       --rotate
	   journalctl(1)

       --runtime
	   portablectl(1), systemctl(1)

       --same-dir
	   systemd-run(1)

       --save-state
	   systemd-journal-upload.service(8)

       --sbat
	   systemd-measure(1), ukify(1)

       --scope
	   systemd-run(1)

       --seal
	   systemd-journal-remote.service(8)

       --search
	   resolvectl(1)

       --section
	   ukify(1)

       --sector-size
	   systemd-repart(8)

       --secureboot-certificate
	   ukify(1)

       --secureboot-certificate-dir
	   ukify(1)

       --secureboot-certificate-name
	   ukify(1)

       --secureboot-certificate-validity
	   ukify(1)

       --secureboot-private-key
	   ukify(1)

       --security-policy
	   systemd-analyze(1)

       --seed
	   systemd-repart(8)

       --selinux-apifs-context
	   systemd-nspawn(1)

       --selinux-context
	   systemd-nspawn(1)

       --send-sighup
	   systemd-run(1)

       --seqpacket
	   systemd-socket-activate(1)

       --service
	   userdbctl(1)

       --service-address
	   resolvectl(1)

       --service-txt
	   resolvectl(1)

       --service-type
	   systemd-run(1)

       --service-watchdogs
	   systemd(1)

       --set-credential
	   systemd-nspawn(1)

       --setenv
	   homectl(1), machinectl(1), systemd-nspawn(1), systemd-run(1), systemd-socket-activate(1)

       --settings
	   systemd-nspawn(1)

       --settle
	   udevadm(8)

       --setup-keys
	   journalctl(1)

       --setup-machine-id
	   systemd-firstboot(1)

       --shell
	   homectl(1), systemd-run(1)

       --show
	   shutdown(8)

       --show-cursor
	   journalctl(1)

       --show-machine
	   busctl(1)

       --show-status
	   systemd(1)

       --show-transaction
	   systemctl(1)

       --show-types
	   systemctl(1)

       --sign-kernel
	   ukify(1)

       --signal
	   loginctl(1), machinectl(1), systemctl(1)

       --signing-engine
	   ukify(1)

       --signtool
	   ukify(1)

       --since
	   coredumpctl(1), journalctl(1)

       --size
	   busctl(1), systemd-repart(8)

       --skel
	   homectl(1)

       --slice
	   systemd-nspawn(1), systemd-run(1)

       --slice-inherit
	   systemd-run(1)

       --smart-relinquish-var
	   journalctl(1)

       --socket-property
	   systemd-run(1)

       --splash
	   systemd-measure(1), ukify(1)

       --split
	   systemd-repart(8)

       --split-mode
	   systemd-journal-remote.service(8)

       --ssh-authorized-keys
	   homectl(1)

       --stale-data
	   resolvectl(1)

       --start-exec-queue
	   udevadm(8)

       --state
	   systemctl(1)

       --static
	   hostnamectl(1)

       --stats
	   networkctl(1)

       --status
	   systemd-notify(1)

       --stderr-priority
	   systemd-cat(1)

       --stop-delay
	   homectl(1)

       --stop-exec-queue
	   udevadm(8)

       --stopping
	   systemd-notify(1)

       --storage
	   homectl(1)

       --strict
	   systemd-hwdb(8), systemd-sysctl.service(8)

       --subsystem-match[=SUBSYSTEM]
	   udevadm(8)

       --subsystem-nomatch[=SUBSYSTEM]
	   udevadm(8)

       --suffix
	   systemd-escape(1), systemd-path(1)

       --summary
	   ukify(1)

       --suppress-sync
	   systemd-nspawn(1)

       --sync
	   journalctl(1), systemd-sysupdate(8)

       --synthesize
	   resolvectl(1), userdbctl(1)

       --sysname-match[=NAME]
	   udevadm(8)

       --system
	   busctl(1), journalctl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-creds(1), systemd-journal-gatewayd.service(8), systemd-journal-
	   upload.service(8), systemd-mount(1), systemd-run(1), systemd-stdio-bridge(1)

       --system-call-filter
	   systemd-nspawn(1)

       --table
	   systemd-analyze(1)

       --tag-match[=TAG]
	   udevadm(8)

       --tasks-max
	   homectl(1)

       --template
	   systemd-escape(1), systemd-nspawn(1)

       --test
	   systemd(1)

       --threshold
	   systemd-analyze(1)

       --timeout
	   busctl(1), systemd-ask-password(1), systemd-networkd-wait-online.service(8), udevadm(8)

       --timeout-idle-sec
	   systemd-mount(1)

       --timeout-signal
	   systemd-udevd.service(8)

       --timer-property
	   systemd-run(1)

       --timestamp
	   systemctl(1), systemd-creds(1)

       --timezone
	   homectl(1), systemd-firstboot(1), systemd-nspawn(1)

       --tldr
	   systemd-analyze(1), systemd-binfmt.service(8), systemd-sysctl.service(8), systemd-sysusers(8), systemd-tmpfiles(8)

       --tmpfs
	   systemd-mount(1), systemd-nspawn(1)

       --to-pattern
	   systemd-analyze(1)

       --tools
	   ukify(1)

       --tpm2-device
	   systemd-creds(1), systemd-cryptenroll(1), systemd-measure(1), systemd-pcrphase.service(8), systemd-repart(8)

       --tpm2-device-key
	   systemd-cryptenroll(1), systemd-repart(8)

       --tpm2-pcrlock
	   systemd-cryptenroll(1), systemd-repart(8)

       --tpm2-pcrs
	   systemd-creds(1), systemd-cryptenroll(1), systemd-repart(8)

       --tpm2-public-key
	   systemd-creds(1), systemd-cryptenroll(1), systemd-repart(8)

       --tpm2-public-key-pcrs
	   systemd-creds(1), systemd-cryptenroll(1), systemd-repart(8)

       --tpm2-seal-key-handle
	   systemd-cryptenroll(1), systemd-repart(8)

       --tpm2-signature
	   systemd-creds(1), systemd-cryptenroll(1)

       --tpm2-with-pin
	   systemd-cryptenroll(1)

       --transcode
	   systemd-creds(1)

       --transient
	   hostnamectl(1)

       --tree
	   udevadm(8)

       --truncate-newline
	   journalctl(1)

       --trust
	   systemd-journal-gatewayd.service(8), systemd-journal-remote.service(8), systemd-journal-upload.service(8)

       --trust-anchor
	   resolvectl(1)

       --type
	   resolvectl(1), systemctl(1), systemd-delta(1), systemd-mount(1), udevadm(8)

       --udev
	   udevadm(8)

       --uid
	   homectl(1), machinectl(1), systemd-notify(1), systemd-run(1)

       --umask
	   homectl(1)

       --umount
	   systemd-dissect(1), systemd-mount(1)

       --uname
	   systemd-measure(1), ukify(1)

       --unescape
	   systemd-escape(1)

       --unique
	   busctl(1)

       --unit
	   journalctl(1), systemd(1), systemd-analyze(1), systemd-cgls(1), systemd-run(1)

       --unlock-fido2-device
	   systemd-cryptenroll(1)

       --unlock-key-file
	   systemd-cryptenroll(1)

       --unregister
	   systemd-binfmt.service(8)

       --until
	   coredumpctl(1), journalctl(1)

       --update-catalog
	   journalctl(1)

       --url
	   systemd-journal-remote.service(8), systemd-journal-upload.service(8)

       --user
	   busctl(1), journalctl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-journal-gatewayd.service(8), systemd-journal-upload.service(8),
	   systemd-mount(1), systemd-nspawn(1), systemd-run(1), systemd-stdio-bridge(1), systemd-tmpfiles(8)

       --user-unit
	   journalctl(1), systemd-cgls(1)

       --usr
	   systemd-hwdb(8)

       --utc
	   journalctl(1)

       --uuid
	   systemd-id128(1), systemd-nspawn(1), udevadm(8)

       --vacuum-files
	   journalctl(1)

       --vacuum-size
	   journalctl(1)

       --vacuum-time
	   journalctl(1)

       --validate
	   resolvectl(1), systemd-dissect(1)

       --value
	   loginctl(1), machinectl(1), systemctl(1), systemd-id128(1), timedatectl(1), udevadm(8)

       --verbose
	   busctl(1), kernel-install(8), systemd-ac-power(1), udevadm(8)

       --verify
	   journalctl(1), machinectl(1), systemd-sysupdate(8)

       --verify-key
	   journalctl(1)

       --verity-data
	   systemd-dissect(1), systemd-nspawn(1)

       --version
	   bootctl(1), busctl(1), coredumpctl(1), homectl(1), hostnamectl(1), journalctl(1), kernel-install(8), localectl(1), loginctl(1), machinectl(1),
	   networkctl(1), oomctl(1), portablectl(1), resolvectl(1), systemctl(1), systemd(1), systemd-ac-power(1), systemd-analyze(1), systemd-battery-
	   check.service(8), systemd-binfmt.service(8), systemd-bless-boot.service(8), systemd-bsod.service(8), systemd-cat(1), systemd-cgls(1), systemd-
	   cgtop(1), systemd-creds(1), systemd-cryptenroll(1), systemd-delta(1), systemd-detect-virt(1), systemd-dissect(1), systemd-escape(1), systemd-
	   firstboot(1), systemd-fsckd.service(8), systemd-id128(1), systemd-inhibit(1), systemd-journal-gatewayd.service(8), systemd-journal-
	   remote.service(8), systemd-journal-upload.service(8), systemd-machine-id-setup(1), systemd-measure(1), systemd-mount(1), systemd-networkd-wait-
	   online.service(8), systemd-notify(1), systemd-nspawn(1), systemd-path(1), systemd-pcrlock(8), systemd-pcrphase.service(8), systemd-repart(8),
	   systemd-run(1), systemd-socket-activate(1), systemd-socket-proxyd(8), systemd-stdio-bridge(1), systemd-storagetm.service(8), systemd-
	   suspend.service(8), systemd-sysctl.service(8), systemd-sysext(8), systemd-sysupdate(8), systemd-sysusers(8), systemd-tmpfiles(8), systemd-tty-ask-
	   password-agent(1), systemd-udevd.service(8), timedatectl(1), udevadm(8), ukify(1), userdbctl(1), varlinkctl(1)

       --vm
	   systemd-detect-virt(1)

       --volatile
	   systemd-nspawn(1)

       --wait
	   systemctl(1), systemd-run(1)

       --wait-daemon[
	   udevadm(8)

       --wait-for-initialization[=SECONDS]
	   udevadm(8)

       --wall
	   systemd-tty-ask-password-agent(1)

       --watch
	   systemd-tty-ask-password-agent(1)

       --watch-bind
	   busctl(1)

       --welcome
	   systemd-firstboot(1)

       --what
	   systemctl(1), systemd-inhibit(1)

       --when
	   systemctl(1)

       --who
	   systemd-inhibit(1)

       --why
	   systemd-inhibit(1)

       --wipe-slot
	   systemd-cryptenroll(1)

       --with
	   systemd-dissect(1)

       --with-dependencies
	   systemctl(1)

       --with-dropin
	   userdbctl(1)

       --with-key
	   systemd-creds(1)

       --with-nss
	   userdbctl(1)

       --with-varlink
	   userdbctl(1)

       --working-directory
	   systemd-run(1)

       --wtmp-only
	   poweroff(8)

       --xattr
	   systemd-cgls(1)

       --xml-interface
	   busctl(1)

       --zone
	   resolvectl(1)

       -1
	   coredumpctl(1), systemd-cgtop(1)

       -4
	   resolvectl(1), systemd-networkd-wait-online.service(8)

       -6
	   resolvectl(1), systemd-networkd-wait-online.service(8)

       -A
	   coredumpctl(1), systemd-mount(1), udevadm(8)

       -C
	   systemd-repart(8), systemd-sysupdate(8)

       -D
	   coredumpctl(1), journalctl(1), systemd-journal-gatewayd.service(8), systemd-journal-upload.service(8), systemd-nspawn(1), systemd-udevd.service(8)

       -E
	   homectl(1), machinectl(1), systemd-nspawn(1), systemd-run(1), systemd-socket-activate(1), systemd-tmpfiles(8), udevadm(8)

       -EE
	   homectl(1)

       -F
	   coredumpctl(1), journalctl(1)

       -G
	   homectl(1), systemd-mount(1), systemd-run(1)

       -H
	   busctl(1), homectl(1), hostnamectl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), shutdown(8), systemctl(1), systemd-analyze(1),
	   systemd-creds(1), systemd-mount(1), systemd-run(1), timedatectl(1)

       -I
	   resolvectl(1)

       -L
	   systemd-nspawn(1)

       -M
	   busctl(1), homectl(1), hostnamectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd-analyze(1),
	   systemd-cgls(1), systemd-cgtop(1), systemd-dissect(1), systemd-mount(1), systemd-nspawn(1), systemd-run(1), systemd-stdio-bridge(1), timedatectl(1)

       -N
	   journalctl(1), systemd-udevd.service(8), udevadm(8), userdbctl(1)

       -P
	   homectl(1), shutdown(8), systemctl(1), systemd-cgtop(1), systemd-id128(1), systemd-nspawn(1), systemd-repart(8), systemd-run(1), udevadm(8)

       -R
	   bootctl(1), resolvectl(1), udevadm(8)

       -S
	   coredumpctl(1), journalctl(1), systemd-nspawn(1), systemd-repart(8), systemd-run(1), udevadm(8)

       -T
	   systemctl(1), systemd-creds(1), systemd-mount(1)

       -U
	   coredumpctl(1), journalctl(1), systemd-dissect(1), systemd-nspawn(1)

       -V
	   resolvectl(1)

       -Z
	   systemd-nspawn(1)

       -a
	   journalctl(1), loginctl(1), machinectl(1), networkctl(1), resolvectl(1), systemctl(1), systemd-dissect(1), systemd-id128(1), systemd-nspawn(1),
	   systemd-socket-activate(1), systemd-storagetm.service(8), timedatectl(1), udevadm(8)

       -b
	   journalctl(1), systemd-cgtop(1), systemd-nspawn(1), udevadm(8)

       -c
	   homectl(1), journalctl(1), resolvectl(1), shutdown(8), systemd-bsod.service(8), systemd-cgls(1), systemd-cgtop(1), systemd-detect-virt(1), systemd-
	   socket-proxyd(8), systemd-udevd.service(8), udevadm(8)

       -d
	   homectl(1), poweroff(8), resolvectl(1), systemd-cgtop(1), systemd-run(1), systemd-socket-activate(1), systemd-udevd.service(8), udevadm(8)

       -e
	   journalctl(1), systemd-ask-password(1), systemd-udevd.service(8), udevadm(8)

       -f
	   journalctl(1), poweroff(8), resolvectl(1), systemctl(1)

       -g
	   journalctl(1), udevadm(8)

       -h
	   bootctl(1), busctl(1), coredumpctl(1), homectl(1), hostnamectl(1), journalctl(1), kernel-install(8), localectl(1), loginctl(1), machinectl(1),
	   networkctl(1), oomctl(1), portablectl(1), resolvectl(1), shutdown(8), systemctl(1), systemd(1), systemd-ac-power(1), systemd-analyze(1), systemd-
	   ask-password(1), systemd-battery-check.service(8), systemd-binfmt.service(8), systemd-bless-boot.service(8), systemd-bsod.service(8), systemd-
	   cat(1), systemd-cgls(1), systemd-cgtop(1), systemd-creds(1), systemd-cryptenroll(1), systemd-delta(1), systemd-detect-virt(1), systemd-dissect(1),
	   systemd-escape(1), systemd-firstboot(1), systemd-fsckd.service(8), systemd-hwdb(8), systemd-id128(1), systemd-inhibit(1), systemd-journal-
	   gatewayd.service(8), systemd-journal-remote.service(8), systemd-journal-upload.service(8), systemd-machine-id-setup(1), systemd-measure(1),
	   systemd-mount(1), systemd-networkd-wait-online.service(8), systemd-notify(1), systemd-nspawn(1), systemd-path(1), systemd-pcrlock(8), systemd-
	   pcrphase.service(8), systemd-repart(8), systemd-run(1), systemd-socket-activate(1), systemd-socket-proxyd(8), systemd-stdio-bridge(1), systemd-
	   storagetm.service(8), systemd-suspend.service(8), systemd-sysctl.service(8), systemd-sysext(8), systemd-sysupdate(8), systemd-sysusers(8), systemd-
	   tmpfiles(8), systemd-tty-ask-password-agent(1), systemd-udevd.service(8), timedatectl(1), udevadm(8), ukify(1), userdbctl(1), varlinkctl(1)

       -i
	   resolvectl(1), systemctl(1), systemd-cgtop(1), systemd-networkd-wait-online.service(8), systemd-nspawn(1)

       -j
	   busctl(1), homectl(1), resolvectl(1), systemd-nspawn(1), varlinkctl(1)

       -k
	   journalctl(1), shutdown(8), systemd-cgls(1), systemd-cgtop(1), udevadm(8)

       -l
	   busctl(1), journalctl(1), loginctl(1), machinectl(1), networkctl(1), resolvectl(1), systemctl(1), systemd-cgls(1), systemd-dissect(1), systemd-
	   mount(1), systemd-socket-activate(1), udevadm(8)

       -m
	   journalctl(1), resolvectl(1), systemd-cgtop(1), systemd-dissect(1), systemd-escape(1), systemd-journal-gatewayd.service(8), systemd-journal-
	   upload.service(8), systemd-sysupdate(8), udevadm(8)

       -n
	   coredumpctl(1), journalctl(1), loginctl(1), machinectl(1), networkctl(1), poweroff(8), systemctl(1), systemd-ask-password(1), systemd-cgtop(1),
	   systemd-nspawn(1), udevadm(8)

       -o
	   coredumpctl(1), journalctl(1), loginctl(1), machinectl(1), systemctl(1), systemd-journal-remote.service(8), systemd-mount(1), systemd-networkd-
	   wait-online.service(8)

       -p
	   bootctl(1), journalctl(1), loginctl(1), machinectl(1), portablectl(1), poweroff(8), resolvectl(1), systemctl(1), systemd-cat(1), systemd-cgtop(1),
	   systemd-creds(1), systemd-escape(1), systemd-id128(1), systemd-mount(1), systemd-nspawn(1), systemd-run(1), systemd-stdio-bridge(1),
	   timedatectl(1), udevadm(8)

       -q
	   bootctl(1), busctl(1), coredumpctl(1), journalctl(1), machinectl(1), portablectl(1), systemctl(1), systemd-analyze(1), systemd-creds(1), systemd-
	   detect-virt(1), systemd-mount(1), systemd-networkd-wait-online.service(8), systemd-nspawn(1), systemd-run(1), udevadm(8)

       -r
	   coredumpctl(1), journalctl(1), resolvectl(1), shutdown(8), systemctl(1), systemd-cgtop(1), systemd-detect-virt(1), systemd-dissect(1), systemd-
	   hwdb(8), systemd-run(1), udevadm(8)

       -s
	   loginctl(1), machinectl(1), networkctl(1), systemctl(1), systemd-hwdb(8), systemd-repart(8), systemd-udevd.service(8), udevadm(8), userdbctl(1)

       -t
	   journalctl(1), resolvectl(1), systemctl(1), systemd-cat(1), systemd-cgtop(1), systemd-delta(1), systemd-mount(1), systemd-run(1), systemd-
	   udevd.service(8), udevadm(8)

       -u
	   journalctl(1), resolvectl(1), systemd-cgls(1), systemd-dissect(1), systemd-escape(1), systemd-id128(1), systemd-journal-upload.service(8), systemd-
	   mount(1), systemd-nspawn(1), systemd-run(1), udevadm(8)

       -v
	   kernel-install(8), resolvectl(1), systemd-ac-power(1), systemd-detect-virt(1), udevadm(8)

       -w
	   poweroff(8), udevadm(8)

       -x
	   bootctl(1), journalctl(1), resolvectl(1), systemd-cgls(1), systemd-dissect(1), systemd-nspawn(1), udevadm(8)

       -y
	   udevadm(8)

       IPv4
	   systemd.link(5), systemd.network(5)

       IPv6
	   systemd.link(5), systemd.network(5)

       K
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       X
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       allow-discards
	   integritytab(5)

       arp
	   systemd.link(5)

       attach
	   systemd-integritysetup@.service(8), systemd-veritysetup@.service(8)

       audit
	   systemd.journal-fields(7)

       aui
	   systemd.link(5)

       auto
	   systemd.resource-control(5)

       bad
	   systemd-bless-boot.service(8)

       besteffort
	   systemd.network(5)

       bnc
	   systemd.link(5)

       broadcast
	   systemd.link(5)

       cat
	   journalctl(1)

       check-new
	   systemd-sysupdate(8)

       cleanup
	   bootctl(1)

       closed
	   systemd.resource-control(5)

       colon-delimited
	   systemd.link(5), systemd.network(5)

       components
	   systemd-sysupdate(8)

       data-device=
	   integritytab(5)

       database
	   systemd.link(5)

       detach
	   systemd-integritysetup@.service(8), systemd-veritysetup@.service(8)

       diffserv3
	   systemd.network(5)

       diffserv4
	   systemd.network(5)

       diffserv8
	   systemd.network(5)

       dot-delimited
	   systemd.link(5), systemd.network(5)

       driver
	   systemd.journal-fields(7)

       dst-host
	   systemd.network(5)

       dual-dst-host
	   systemd.network(5)

       dual-src-host
	   systemd.network(5)

       eui64
	   systemd.network(5)

       export
	   journalctl(1)

       fibre
	   systemd.link(5)

       flows
	   systemd.network(5)

       force
	   loader.conf(5)

       good
	   systemd-bless-boot.service(8)

       help
	   systemd-integritysetup@.service(8), systemd-veritysetup@.service(8)

       hibernate
	   systemd-suspend.service(8)

       hosts
	   systemd.network(5)

       hybrid-sleep
	   systemd-suspend.service(8)

       hyphen-delimited
	   systemd.link(5), systemd.network(5)

       if-safe
	   loader.conf(5)

       indeterminate
	   systemd-bless-boot.service(8)

       install
	   bootctl(1)

       integrity-algorithm=
	   integritytab(5)

       is-installed
	   bootctl(1)

       journal
	   systemd.journal-fields(7)

       journal-commit-time=
	   integritytab(5)

       journal-watermark=
	   integritytab(5)

       json
	   journalctl(1)

       json-pretty
	   journalctl(1)

       json-seq
	   journalctl(1)

       json-sse
	   journalctl(1)

       keep
	   systemd.link(5)

       kernel
	   systemd.journal-fields(7), systemd.link(5)

       kernel-identify
	   bootctl(1)

       kernel-inspect
	   bootctl(1)

       link-layer
	   networkd.conf(5)

       link-layer-time[:TIME]
	   networkd.conf(5)

       list
	   bootctl(1), systemd-sysext(8), systemd-sysupdate(8)

       mac
	   systemd.link(5)

       magic
	   systemd.link(5)

       manual
	   loader.conf(5)

       merge
	   systemd-sysext(8)

       mii
	   systemd.link(5)

       mode=
	   integritytab(5)

       multicast
	   systemd.link(5)

       none
	   systemd.link(5), systemd.network(5)

       off
	   loader.conf(5)

       onboard
	   systemd.link(5)

       path
	   systemd.link(5)

       pending
	   systemd-sysupdate(8)

       persistent
	   systemd.link(5)

       phy
	   systemd.link(5)

       precedence
	   systemd.network(5)

       prefixstable[:ADDRESS][,UUID]
	   systemd.network(5)

       pretty
	   systemctl(1)

       random
	   systemd.link(5)

       random-seed
	   bootctl(1)

       reboot
	   systemd-sysupdate(8)

       reboot-to-firmware
	   bootctl(1)

       refresh
	   systemd-sysext(8)

       remove
	   bootctl(1)

       secureon
	   systemd.link(5)

       set-default
	   bootctl(1)

       set-oneshot
	   bootctl(1)

       set-timeout
	   bootctl(1)

       set-timeout-oneshot
	   bootctl(1)

       short
	   journalctl(1)

       short-delta
	   journalctl(1)

       short-full
	   journalctl(1)

       short-iso
	   journalctl(1)

       short-iso-precise
	   journalctl(1)

       short-monotonic
	   journalctl(1)

       short-precise
	   journalctl(1)

       short-unix
	   journalctl(1)

       slot
	   systemd.link(5)

       src-host
	   systemd.network(5)

       static:ADDRESS
	   systemd.network(5)

       status
	   bootctl(1), systemd-bless-boot.service(8), systemd-sysext(8)

       stdout
	   systemd.journal-fields(7)

       strict
	   systemd.resource-control(5)

       suspend
	   systemd-suspend.service(8)

       suspend-then-hibernate
	   systemd-suspend.service(8)

       syslog
	   systemd.journal-fields(7)

       tp
	   systemd.link(5)

       triple
	   systemd.network(5)

       unicast
	   systemd.link(5)

       unix
	   systemctl(1)

       unlink
	   bootctl(1)

       unmerge
	   systemd-sysext(8)

       update
	   bootctl(1), systemd-sysupdate(8)

       us
	   systemctl(1)

       us+utc
	   systemctl(1)

       utc
	   systemctl(1)

       uuid
	   networkd.conf(5)

       vacuum
	   systemd-sysupdate(8)

       vendor
	   networkd.conf(5)

       verbose
	   journalctl(1)

       with-unit
	   journalctl(1)

       μs
	   systemctl(1)

       μs+utc
	   systemctl(1)

CONSTANTS
       Various constants used and/or defined by systemd.

	-1
	   sd_journal_get_fd(3), sd_login_monitor_new(3)

       'h'
	   sd_bus_message_read_basic(3)

       's'
	   sd_bus_message_read_basic(3)

       'y'
	   sd_bus_message_read_basic(3)

       -
	   systemd.resource-control(5)

       -0
	   journalctl(1)

       -1
	   journalctl(1), sd_event_run(3), sd_event_wait(3), sd_journal_get_fd(3)

       -E2BIG
	   sd_journal_get_data(3), sd_journal_query_unique(3)

       -EADDRINUSE
	   sd_bus_request_name(3)

       -EADDRNOTAVAIL
	   sd_journal_get_data(3), sd_journal_query_unique(3)

       -EAGAIN
	   sd_hwdb_get(3)

       -EALREADY
	   sd_bus_request_name(3)

       -EBADF
	   sd_bus_set_fd(3), sd_event_add_inotify(3), sd_pid_get_owner_uid(3)

       -EBADMSG
	   sd_bus_message_open_container(3), sd_bus_message_read(3), sd_bus_message_read_array(3), sd_bus_message_read_basic(3), sd_bus_message_read_strv(3),
	   sd_bus_message_seal(3), sd_bus_message_skip(3), sd_event_add_memory_pressure(3), sd_journal_get_data(3), sd_journal_query_unique(3)

       -EBUSY
	   sd_bus_message_open_container(3), sd_bus_message_read(3), sd_bus_process(3), sd_bus_track_new(3), sd_event_add_child(3),
	   sd_event_add_memory_pressure(3), sd_event_add_signal(3), sd_event_run(3), sd_event_wait(3)

       -ECHILD
	   sd_bus_add_node_enumerator(3), sd_bus_add_object(3), sd_bus_add_object_manager(3), sd_bus_attach_event(3), sd_bus_call(3), sd_bus_can_send(3),
	   sd_bus_close(3), sd_bus_emit_signal(3), sd_bus_enqueue_for_read(3), sd_bus_get_fd(3), sd_bus_get_n_queued_read(3), sd_bus_get_name_creds(3),
	   sd_bus_get_name_machine_id(3), sd_bus_is_open(3), sd_bus_list_names(3), sd_bus_negotiate_fds(3), sd_bus_process(3), sd_bus_query_sender_creds(3),
	   sd_bus_request_name(3), sd_bus_send(3), sd_bus_set_address(3), sd_bus_set_close_on_exit(3), sd_bus_set_connected_signal(3),
	   sd_bus_set_description(3), sd_bus_set_exit_on_disconnect(3), sd_bus_set_fd(3), sd_bus_set_sender(3), sd_bus_set_server(3),
	   sd_bus_set_watch_bind(3), sd_bus_slot_set_floating(3), sd_bus_start(3), sd_bus_wait(3), sd_event_add_child(3), sd_event_add_defer(3),
	   sd_event_add_inotify(3), sd_event_add_io(3), sd_event_add_memory_pressure(3), sd_event_add_signal(3), sd_event_add_time(3), sd_event_exit(3),
	   sd_event_get_fd(3), sd_event_now(3), sd_event_run(3), sd_event_set_signal_exit(3), sd_event_set_watchdog(3), sd_event_source_get_pending(3),
	   sd_event_source_set_description(3), sd_event_source_set_enabled(3), sd_event_source_set_floating(3), sd_event_source_set_prepare(3),
	   sd_event_source_set_priority(3), sd_event_source_set_ratelimit(3), sd_event_wait(3), sd_journal_get_data(3), sd_journal_open(3),
	   sd_journal_query_unique(3)

       -ECONNRESET
	   sd_bus_call(3), sd_bus_process(3), sd_bus_send(3)

       -EDOM
	   sd_event_add_child(3), sd_event_add_inotify(3), sd_event_add_io(3), sd_event_add_memory_pressure(3), sd_event_add_signal(3), sd_event_add_time(3),
	   sd_event_source_get_pending(3), sd_event_source_set_exit_on_failure(3), sd_event_source_set_prepare(3), sd_event_source_set_ratelimit(3)

       -EEXIST
	   sd_bus_add_object(3), sd_bus_message_set_destination(3), sd_bus_request_name(3)

       -EHOSTDOWN
	   sd_event_add_memory_pressure(3)

       -EINVAL
	   sd_bus_add_node_enumerator(3), sd_bus_add_object(3), sd_bus_add_object_manager(3), sd_bus_call(3), sd_bus_creds_get_pid(3),
	   sd_bus_creds_new_from_pid(3), sd_bus_default(3), sd_bus_emit_signal(3), sd_bus_error(3), sd_bus_error_add_map(3), sd_bus_get_fd(3),
	   sd_bus_get_name_creds(3), sd_bus_get_name_machine_id(3), sd_bus_interface_name_is_valid(3), sd_bus_list_names(3), sd_bus_message_append(3),
	   sd_bus_message_append_array(3), sd_bus_message_append_basic(3), sd_bus_message_append_string_memfd(3), sd_bus_message_append_strv(3),
	   sd_bus_message_at_end(3), sd_bus_message_copy(3), sd_bus_message_get_cookie(3), sd_bus_message_get_monotonic_usec(3),
	   sd_bus_message_get_signature(3), sd_bus_message_get_type(3), sd_bus_message_new(3), sd_bus_message_new_method_call(3),
	   sd_bus_message_new_method_error(3), sd_bus_message_new_signal(3), sd_bus_message_open_container(3), sd_bus_message_read(3),
	   sd_bus_message_read_array(3), sd_bus_message_read_basic(3), sd_bus_message_read_strv(3), sd_bus_message_rewind(3), sd_bus_message_seal(3),
	   sd_bus_message_sensitive(3), sd_bus_message_set_destination(3), sd_bus_message_set_expect_reply(3), sd_bus_message_skip(3),
	   sd_bus_message_verify_type(3), sd_bus_negotiate_fds(3), sd_bus_process(3), sd_bus_query_sender_creds(3), sd_bus_reply_method_error(3),
	   sd_bus_reply_method_return(3), sd_bus_request_name(3), sd_bus_send(3), sd_bus_set_address(3), sd_bus_set_description(3),
	   sd_bus_set_exit_on_disconnect(3), sd_bus_set_fd(3), sd_bus_set_method_call_timeout(3), sd_bus_set_server(3), sd_bus_slot_set_description(3),
	   sd_bus_slot_set_destroy_callback(3), sd_bus_slot_set_floating(3), sd_bus_start(3), sd_bus_track_add_name(3), sd_bus_track_new(3), sd_bus_wait(3),
	   sd_device_get_syspath(3), sd_event_add_child(3), sd_event_add_defer(3), sd_event_add_inotify(3), sd_event_add_io(3),
	   sd_event_add_memory_pressure(3), sd_event_add_signal(3), sd_event_add_time(3), sd_event_exit(3), sd_event_get_fd(3), sd_event_now(3),
	   sd_event_run(3), sd_event_set_signal_exit(3), sd_event_set_watchdog(3), sd_event_source_get_pending(3), sd_event_source_set_description(3),
	   sd_event_source_set_destroy_callback(3), sd_event_source_set_enabled(3), sd_event_source_set_exit_on_failure(3), sd_event_source_set_floating(3),
	   sd_event_source_set_prepare(3), sd_event_source_set_priority(3), sd_event_source_set_ratelimit(3), sd_event_wait(3), sd_hwdb_get(3),
	   sd_hwdb_new(3), sd_journal_get_data(3), sd_journal_query_unique(3), sd_login_monitor_new(3), sd_machine_get_class(3), sd_path_lookup(3),
	   sd_pid_get_owner_uid(3), sd_seat_get_active(3), sd_session_is_active(3), sd_uid_get_state(3)

       -EIO
	   sd_bus_error(3), sd_journal_get_data(3), sd_journal_query_unique(3)

       -ELOOP
	   sd_bus_call(3)

       -EMFILE
	   sd_event_new(3)

       -ENOBUFS
	   sd_bus_send(3), sd_journal_get_data(3), sd_journal_query_unique(3)

       -ENODATA
	   sd_bus_creds_get_pid(3), sd_bus_message_get_cookie(3), sd_bus_message_get_monotonic_usec(3), sd_bus_negotiate_fds(3), sd_bus_set_address(3),
	   sd_bus_set_description(3), sd_event_exit(3), sd_pid_get_owner_uid(3), sd_seat_get_active(3), sd_session_is_active(3), sd_uid_get_state(3)

       -ENOENT
	   sd_device_get_syspath(3), sd_hwdb_get(3), sd_hwdb_new(3), sd_id128_get_machine(3), sd_journal_get_data(3), sd_journal_query_unique(3)

       -ENOEXEC
	   sd_event_source_set_ratelimit(3)

       -ENOMEDIUM
	   sd_bus_default(3), sd_id128_get_machine(3)

       -ENOMEM
	   sd_bus_add_node_enumerator(3), sd_bus_add_object(3), sd_bus_add_object_manager(3), sd_bus_call(3), sd_bus_creds_get_pid(3),
	   sd_bus_creds_new_from_pid(3), sd_bus_default(3), sd_bus_emit_signal(3), sd_bus_error(3), sd_bus_error_add_map(3), sd_bus_get_name_creds(3),
	   sd_bus_get_name_machine_id(3), sd_bus_list_names(3), sd_bus_message_append(3), sd_bus_message_append_array(3), sd_bus_message_append_basic(3),
	   sd_bus_message_append_string_memfd(3), sd_bus_message_append_strv(3), sd_bus_message_copy(3), sd_bus_message_new(3),
	   sd_bus_message_new_method_call(3), sd_bus_message_new_method_error(3), sd_bus_message_new_signal(3), sd_bus_message_open_container(3),
	   sd_bus_message_skip(3), sd_bus_new(3), sd_bus_reply_method_error(3), sd_bus_reply_method_return(3), sd_bus_send(3), sd_bus_set_description(3),
	   sd_bus_slot_set_description(3), sd_bus_track_add_name(3), sd_bus_track_new(3), sd_event_add_child(3), sd_event_add_defer(3),
	   sd_event_add_inotify(3), sd_event_add_io(3), sd_event_add_memory_pressure(3), sd_event_add_signal(3), sd_event_add_time(3), sd_event_new(3),
	   sd_event_source_get_pending(3), sd_event_source_set_description(3), sd_event_source_set_enabled(3), sd_event_source_set_prepare(3),
	   sd_event_source_set_priority(3), sd_get_seats(3), sd_hwdb_new(3), sd_journal_get_data(3), sd_login_monitor_new(3), sd_machine_get_class(3),
	   sd_path_lookup(3), sd_pid_get_owner_uid(3), sd_seat_get_active(3), sd_session_is_active(3), sd_uid_get_state(3)

       -ENOMSG
	   sd_bus_message_seal(3)

       -ENOPKG
	   sd_bus_add_node_enumerator(3), sd_bus_add_object(3), sd_bus_add_object_manager(3), sd_bus_can_send(3), sd_bus_emit_signal(3), sd_bus_get_fd(3),
	   sd_bus_get_name_creds(3), sd_bus_get_name_machine_id(3), sd_bus_list_names(3), sd_bus_negotiate_fds(3), sd_bus_set_address(3),
	   sd_bus_set_description(3), sd_bus_set_exit_on_disconnect(3), sd_bus_set_fd(3), sd_bus_set_method_call_timeout(3), sd_bus_set_server(3),
	   sd_bus_start(3), sd_id128_get_machine(3)

       -ENOSYS
	   sd_event_add_inotify(3), sd_id128_get_machine(3)

       -ENOTCONN
	   sd_bus_call(3), sd_bus_can_send(3), sd_bus_get_fd(3), sd_bus_list_names(3), sd_bus_message_new(3), sd_bus_message_new_method_call(3),
	   sd_bus_message_new_method_error(3), sd_bus_message_new_signal(3), sd_bus_process(3), sd_bus_query_sender_creds(3), sd_bus_reply_method_error(3),
	   sd_bus_reply_method_return(3), sd_bus_request_name(3), sd_bus_send(3), sd_bus_set_server(3), sd_bus_wait(3)

       -ENOTTY
	   sd_event_add_memory_pressure(3)

       -ENXIO
	   sd_bus_creds_get_pid(3), sd_bus_message_append(3), sd_bus_message_append_array(3), sd_bus_message_append_basic(3),
	   sd_bus_message_append_string_memfd(3), sd_bus_message_append_strv(3), sd_bus_message_copy(3), sd_bus_message_open_container(3),
	   sd_bus_message_read(3), sd_bus_message_read_basic(3), sd_bus_message_read_strv(3), sd_bus_message_skip(3), sd_bus_set_description(3),
	   sd_bus_slot_set_description(3), sd_event_new(3), sd_event_source_set_description(3), sd_id128_get_machine(3), sd_machine_get_class(3),
	   sd_path_lookup(3), sd_seat_get_active(3), sd_session_is_active(3), sd_uid_get_state(3)

       -EOPNOTSUPP
	   sd_bus_creds_new_from_pid(3), sd_bus_message_new_method_call(3), sd_bus_message_read_array(3), sd_bus_send(3), sd_event_add_child(3),
	   sd_event_add_memory_pressure(3), sd_event_add_time(3), sd_event_now(3), sd_path_lookup(3)

       -EOVERFLOW
	   sd_event_add_time(3)

       -EPERM
	   sd_bus_get_fd(3), sd_bus_get_name_creds(3), sd_bus_message_append(3), sd_bus_message_append_array(3), sd_bus_message_append_basic(3),
	   sd_bus_message_append_string_memfd(3), sd_bus_message_append_strv(3), sd_bus_message_at_end(3), sd_bus_message_copy(3),
	   sd_bus_message_new_method_call(3), sd_bus_message_new_method_error(3), sd_bus_message_open_container(3), sd_bus_message_read_array(3),
	   sd_bus_message_read_strv(3), sd_bus_message_rewind(3), sd_bus_message_set_destination(3), sd_bus_message_set_expect_reply(3),
	   sd_bus_message_skip(3), sd_bus_message_verify_type(3), sd_bus_negotiate_fds(3), sd_bus_query_sender_creds(3), sd_bus_reply_method_error(3),
	   sd_bus_reply_method_return(3), sd_bus_set_address(3), sd_bus_set_description(3), sd_bus_set_fd(3), sd_bus_set_sender(3), sd_bus_set_server(3),
	   sd_bus_start(3), sd_event_add_io(3), sd_id128_get_machine(3)

       -EPROTONOSUPPORT
	   sd_journal_get_data(3), sd_journal_query_unique(3)

       -EPROTOTYPE
	   sd_bus_add_object(3)

       -ESOCKTNOSUPPORT
	   sd_bus_default(3)

       -ESRCH
	   sd_bus_creds_new_from_pid(3), sd_bus_emit_signal(3), sd_bus_request_name(3), sd_pid_get_owner_uid(3)

       -ESTALE
	   sd_bus_message_append(3), sd_bus_message_append_array(3), sd_bus_message_append_basic(3), sd_bus_message_append_string_memfd(3),
	   sd_bus_message_append_strv(3), sd_bus_message_copy(3), sd_bus_message_open_container(3), sd_bus_slot_set_floating(3), sd_event_add_child(3),
	   sd_event_add_defer(3), sd_event_add_inotify(3), sd_event_add_io(3), sd_event_add_memory_pressure(3), sd_event_add_signal(3), sd_event_add_time(3),
	   sd_event_exit(3), sd_event_run(3), sd_event_source_get_pending(3), sd_event_source_set_prepare(3), sd_event_source_set_priority(3),
	   sd_event_wait(3), sd_journal_get_realtime_usec(3)

       -ETIMEDOUT
	   sd_bus_call(3)

       -EUCLEAN
	   sd_id128_get_machine(3)

       -EUNATCH
	   sd_bus_track_add_name(3)

       /org/freedesktop/systemd1
	   org.freedesktop.systemd1(5)

       0
	   kernel-install(8), org.freedesktop.resolve1(5), sd_bus_add_object(3), sd_bus_error(3), sd_event_add_time(3), sd_journal_add_match(3), systemctl(1),
	   systemd-analyze(1), systemd.netdev(5), systemd.resource-control(5), tmpfiles.d(5), udev_device_get_syspath(3), udev_device_has_tag(3),
	   udev_enumerate_add_match_subsystem(3), udev_enumerate_scan_devices(3), udev_monitor_filter_update(3), udev_monitor_receive_device(3), udevadm(8)

       0657fd6d-a4ab-43c4-84e5-0933c84b4f4f
	   systemd-gpt-auto-generator(8)

       0755
	   systemd.exec(5)

       0x0000000000000002
	   systemd-gpt-auto-generator(8)

       0x1000000000000000
	   systemd-gpt-auto-generator(8)

       0x8000000000000000
	   systemd-gpt-auto-generator(8)

       0xFF
	   sd-id128(3)

       0xFFFF
	   sd_uid_get_state(3)

       0xFFFFFFFF
	   sd_uid_get_state(3)

       1
	   journalctl(1), sd_bus_add_object(3), systemctl(1), systemd-analyze(1), systemd-oomd.service(8), systemd-tmpfiles(8), systemd.network(5),
	   systemd.scope(5), systemd.service(5), udev_device_get_syspath(3)

       10
	   systemd-journald.service(8)

       11
	   systemd-analyze(1)

       12
	   systemd-analyze(1)

       128
	   systemd.resource-control(5)

       19532
	   systemd-journal-upload.service(8)

       2
	   journalctl(1), systemctl(1), systemd.network(5)

       3
	   systemctl(1)

       3b8f8425-20e0-4f3b-907f-1a25a76f98e8
	   systemd-gpt-auto-generator(8)

       4
	   systemctl(1)

       443
	   resolvectl(1)

       4a67b082-0a4c-41cf-b6c7-440b29bb8c4
	   systemd-bless-boot.service(8)

       4a67b082-0a4c-41cf-b6c7-440b29bb8c4f
	   systemd-gpt-auto-generator(8)

       4d21b016-b534-45c2-a9fb-5c16e091fd2d
	   systemd-gpt-auto-generator(8)

       4f68bce3-e8cd-4db1-96e7-fbcaf984b709
	   repart.d(5), systemd-gpt-auto-generator(8)

       65
	   systemd-tmpfiles(8)

       73
	   systemd-tmpfiles(8)

       77
	   kernel-install(8)

       7ec6f557-3bc5-4aca-b293-16ef5df639d1
	   systemd-gpt-auto-generator(8)

       8cf2644b-4b0b-428f-9387-6d876050dc67
	   systemd-repart(8)

       933ac7e1-2eb4-4f13-b844-0e14e2aef915
	   systemd-gpt-auto-generator(8)

       :
	   systemd.resource-control(5)

       A
	   tmpfiles.d(5)

       ACTION
	   udev_device_new_from_syspath(3)

       AF_INET
	   journald.conf(5), org.freedesktop.machine1(5), org.freedesktop.resolve1(5), sd_is_fifo(3), systemd.exec(5), systemd.resource-control(5),
	   systemd.socket(5)

       AF_INET6
	   org.freedesktop.machine1(5), org.freedesktop.resolve1(5), sd_is_fifo(3), systemd.exec(5), systemd.resource-control(5), systemd.socket(5)

       AF_NETLINK
	   systemd.exec(5), systemd.socket(5)

       AF_PACKET
	   systemd.exec(5), systemd.socket(5)

       AF_UNIX
	   busctl(1), crypttab(5), daemon(7), journald.conf(5), machinectl(1), nss-resolve(8), pam_systemd(8), sd_is_fifo(3), sd_notify(3),
	   sd_pid_get_owner_uid(3), systemctl(1), systemd(1), systemd-journal-gatewayd.service(8), systemd-journal-remote.service(8), systemd-repart(8),
	   systemd.exec(5), systemd.link(5), systemd.netdev(5), systemd.service(5), systemd.socket(5), varlinkctl(1)

       AF_UNSPEC
	   org.freedesktop.resolve1(5), sd_is_fifo(3)

       AF_VSOCK
	   sd_notify(3), systemd(1), systemd.socket(5), systemd.system-credentials(7)

       ALLOW_INTERACTIVE_AUTHORIZATION
	   sd_bus_message_set_expect_reply(3), sd_bus_set_description(3)

       AND
	   systemd.exec(5)

       ANY
	   resolvectl(1)

       B
	   tmpfiles.d(5)

       BLKDISCARD
	   systemd-repart(8)

       BUS_MESSAGE_NO_REPLY_EXPECTED
	   sd_bus_call(3)

       C
	   tmpfiles.d(5)

       CAP_AUDIT_CONTROL
	   systemd-nspawn(1)

       CAP_AUDIT_WRITE
	   systemd-nspawn(1)

       CAP_BLOCK_SUSPEND
	   homectl(1), pam_systemd(8)

       CAP_CHOWN
	   systemd-nspawn(1)

       CAP_DAC_OVERRIDE
	   systemd-nspawn(1), systemd.exec(5)

       CAP_DAC_READ_SEARCH
	   systemd-nspawn(1)

       CAP_FOWNER
	   systemd-nspawn(1), systemd-tmpfiles(8)

       CAP_FSETID
	   systemd-nspawn(1)

       CAP_IPC_OWNER
	   systemd-nspawn(1)

       CAP_KILL
	   systemd-nspawn(1)

       CAP_LEASE
	   systemd-nspawn(1)

       CAP_LINUX_IMMUTABLE
	   systemd-nspawn(1)

       CAP_MKNOD
	   systemd-nspawn(1), systemd.exec(5)

       CAP_NET_ADMIN
	   systemd-nspawn(1)

       CAP_NET_BIND_SERVICE
	   systemd-nspawn(1)

       CAP_NET_BROADCAST
	   systemd-nspawn(1)

       CAP_NET_RAW
	   systemd-nspawn(1)

       CAP_SETFCAP
	   systemd-nspawn(1)

       CAP_SETGID
	   systemd-nspawn(1)

       CAP_SETPCAP
	   systemd-nspawn(1)

       CAP_SETUID
	   systemd-nspawn(1)

       CAP_SYSLOG
	   systemd.exec(5)

       CAP_SYS_ADMIN
	   org.freedesktop.systemd1(5), sd_bus_add_object(3), systemd-nspawn(1), systemd.exec(5)

       CAP_SYS_BOOT
	   systemd-nspawn(1)

       CAP_SYS_CHROOT
	   systemd-nspawn(1)

       CAP_SYS_MODULE
	   systemd.exec(5)

       CAP_SYS_NICE
	   systemd-nspawn(1)

       CAP_SYS_PTRACE
	   systemd-nspawn(1), systemd.exec(5)

       CAP_SYS_RAWIO
	   systemd.exec(5)

       CAP_SYS_RESOURCE
	   systemd-nspawn(1)

       CAP_SYS_TIME
	   systemd.exec(5)

       CAP_SYS_TTY_CONFIG
	   systemd-nspawn(1)

       CAP_WAKE_ALARM
	   homectl(1), pam_systemd(8), systemd.exec(5)

       CLOCK_BOOTTIME
	   sd-event(3), sd_event_add_time(3), sd_event_now(3), systemd.timer(5)

       CLOCK_BOOTTIME_ALARM
	   sd-event(3), sd_event_add_time(3), sd_event_now(3)

       CLOCK_MONOTONIC
	   org.freedesktop.login1(5), org.freedesktop.systemd1(5), sd-event(3), sd_bus_get_fd(3), sd_bus_message_get_monotonic_usec(3), sd_event_add_time(3),
	   sd_event_now(3), sd_journal_get_cutoff_realtime_usec(3), sd_journal_get_fd(3), sd_journal_get_realtime_usec(3), sd_journal_seek_head(3),
	   sd_login_monitor_new(3), sd_notify(3), systemd.journal-fields(7), systemd.service(5), systemd.timer(5)

       CLOCK_REALTIME
	   org.freedesktop.login1(5), org.freedesktop.systemd1(5), org.freedesktop.timedate1(5), sd-event(3), sd_bus_message_get_monotonic_usec(3),
	   sd_event_add_time(3), sd_event_now(3), sd_journal_get_cutoff_realtime_usec(3), sd_journal_get_realtime_usec(3), sd_journal_seek_head(3),
	   sd_session_is_active(3), sd_uid_get_state(3), systemd.journal-fields(7), systemd.special(7), systemd.timer(5)

       CLOCK_REALTIME_ALARM
	   sd-event(3), sd_event_add_time(3), sd_event_now(3)

       CLONE_NEWNS
	   systemd.exec(5)

       DEVPATH
	   udev_device_new_from_syspath(3)

       DHCPDECLINE
	   systemd.network(5)

       EACCES
	   systemd.exec(5)

       EOPNOTSUPP
	   sd_event_add_child(3)

       EPERM
	   systemd.exec(5)

       EPIPE
	   systemd-journald.service(8)

       EPOLLERR
	   sd_event_add_io(3), sd_notify(3)

       EPOLLET
	   sd-event(3), sd_event_add_io(3)

       EPOLLHUP
	   sd_event_add_io(3), sd_notify(3)

       EPOLLIN
	   sd_event_add_io(3), sd_event_get_fd(3)

       EPOLLOUT
	   sd_event_add_io(3)

       EPOLLPRI
	   sd_event_add_io(3)

       EPOLLRDHUP
	   sd_event_add_io(3)

       ESC
	   systemctl(1)

       EUCLEAN
	   sd-bus-errors(3), systemd.exec(5)

       EXIT_ADDRESS_FAMILIES
	   systemd.exec(5)

       EXIT_APPARMOR_PROFILE
	   systemd.exec(5)

       EXIT_BPF
	   systemd.exec(5)

       EXIT_CACHE_DIRECTORY
	   systemd.exec(5)

       EXIT_CAPABILITIES
	   systemd.exec(5)

       EXIT_CGROUP
	   systemd.exec(5)

       EXIT_CHDIR
	   systemd.exec(5)

       EXIT_CHOWN
	   systemd.exec(5)

       EXIT_CHROOT
	   systemd.exec(5)

       EXIT_CONFIGURATION_DIRECTORY
	   systemd.exec(5)

       EXIT_CONFIRM
	   systemd.exec(5)

       EXIT_CPUAFFINITY
	   systemd.exec(5)

       EXIT_CREDENTIALS
	   systemd.exec(5)

       EXIT_EXEC
	   systemd.exec(5)

       EXIT_FAILURE
	   sd_bus_set_exit_on_disconnect(3), systemd-tmpfiles(8), systemd.exec(5)

       EXIT_FDS
	   systemd.exec(5)

       EXIT_GROUP
	   systemd.exec(5)

       EXIT_INVALIDARGUMENT
	   systemd.exec(5)

       EXIT_IOPRIO
	   systemd.exec(5)

       EXIT_KEYRING
	   systemd.exec(5)

       EXIT_LIMITS
	   systemd.exec(5)

       EXIT_LOGS_DIRECTORY
	   systemd.exec(5)

       EXIT_MEMORY
	   systemd.exec(5)

       EXIT_NAMESPACE
	   systemd.exec(5)

       EXIT_NETWORK
	   systemd.exec(5)

       EXIT_NICE
	   systemd.exec(5)

       EXIT_NOPERMISSION
	   systemd.exec(5)

       EXIT_NOTCONFIGURED
	   systemd.exec(5)

       EXIT_NOTIMPLEMENTED
	   systemd.exec(5)

       EXIT_NOTINSTALLED
	   systemd.exec(5)

       EXIT_NOTRUNNING
	   systemd.exec(5)

       EXIT_NO_NEW_PRIVILEGES
	   systemd.exec(5)

       EXIT_NUMA_POLICY
	   systemd.exec(5)

       EXIT_OOM_ADJUST
	   systemd.exec(5)

       EXIT_PAM
	   systemd.exec(5)

       EXIT_PERSONALITY
	   systemd.exec(5)

       EXIT_RUNTIME_DIRECTORY
	   systemd.exec(5)

       EXIT_SECCOMP
	   systemd.exec(5)

       EXIT_SECUREBITS
	   systemd.exec(5)

       EXIT_SELINUX_CONTEXT
	   systemd.exec(5)

       EXIT_SETSCHEDULER
	   systemd.exec(5)

       EXIT_SETSID
	   systemd.exec(5)

       EXIT_SIGNAL_MASK
	   systemd.exec(5)

       EXIT_SMACK_PROCESS_LABEL
	   systemd.exec(5)

       EXIT_STATE_DIRECTORY
	   systemd.exec(5)

       EXIT_STDERR
	   systemd.exec(5)

       EXIT_STDIN
	   systemd.exec(5)

       EXIT_STDOUT
	   systemd.exec(5)

       EXIT_SUCCESS
	   systemd.exec(5)

       EXIT_TIMERSLACK
	   systemd.exec(5)

       EXIT_USER
	   systemd.exec(5)

       EX_CANTCREAT
	   systemd-tmpfiles(8), systemd.exec(5)

       EX_CONFIG
	   systemd.exec(5)

       EX_DATAERR
	   systemd-tmpfiles(8), systemd.exec(5)

       EX_IOERR
	   systemd.exec(5)

       EX_NOHOST
	   systemd.exec(5)

       EX_NOINPUT
	   systemd.exec(5)

       EX_NOPERM
	   systemd.exec(5)

       EX_NOUSER
	   systemd.exec(5)

       EX_OSERR
	   systemd.exec(5)

       EX_OSFILE
	   systemd.exec(5)

       EX_PROTOCOL
	   systemd.exec(5)

       EX_SOFTWARE
	   systemd.exec(5)

       EX_TEMPFAIL
	   systemd.exec(5)

       EX_UNAVAILABLE
	   systemd.exec(5)

       EX_USAGE
	   systemd.exec(5)

       FD_CLOEXEC
	   sd_listen_fds(3)

       IFF_UP
	   org.freedesktop.resolve1(5)

       IN
	   resolvectl(1)

       INIT_PROCESS
	   systemd.exec(5)

       IN_ACCESS
	   sd_event_add_inotify(3)

       IN_ATTRIB
	   sd_event_add_inotify(3)

       IN_CLOSE_WRITE
	   sd_event_add_inotify(3)

       IN_MASK_ADD
	   sd_event_add_inotify(3)

       IN_ONESHOT
	   sd_event_add_inotify(3)

       IPPROTO_SCTP
	   systemd.socket(5)

       IPPROTO_UDPLITE
	   systemd.socket(5)

       IPV6_FREEBIND
	   daemon(7), systemd.socket(5)

       IPV6_RECVPKTINFO
	   systemd.socket(5)

       IPV6_TRANSPARENT
	   systemd.socket(5)

       IPV6_UNICAST_HOPS
	   systemd.socket(5)

       IP_FREEBIND
	   daemon(7), systemd.socket(5)

       IP_PKTINFO
	   systemd.socket(5)

       IP_TOS
	   systemd.socket(5)

       IP_TRANSPARENT
	   systemd.socket(5)

       IP_TTL
	   systemd.socket(5)

       LINE_MAX - 8
	   sd_journal_print(3)

       LOCK_EX
	   systemd-pcrphase.service(8)

       LOCK_SH
	   systemd-pcrphase.service(8)

       LOGIN_PROCESS
	   systemd.exec(5)

       LOG_ALERT
	   sd_journal_print(3), sd_journal_stream_fd(3)

       LOG_CRIT
	   sd_journal_print(3), sd_journal_stream_fd(3)

       LOG_DEBUG
	   sd_event_add_memory_pressure(3), sd_journal_print(3), sd_journal_stream_fd(3)

       LOG_EMERG
	   sd_journal_print(3), sd_journal_stream_fd(3)

       LOG_ERR
	   sd_journal_print(3), sd_journal_stream_fd(3)

       LOG_INFO
	   sd_journal_print(3), sd_journal_stream_fd(3)

       LOG_NOTICE
	   sd_journal_print(3), sd_journal_stream_fd(3)

       LOG_WARNING
	   sd_journal_print(3), sd_journal_stream_fd(3)

       M
	   tmpfiles.d(5)

       MAP_ANON
	   systemd.exec(5)

       MESSAGE_ID=fc2e22bc6ee647b6b90729ab34a250b1
	   systemd-coredump(8)

       MSDOS_SUPER_MAGIC
	   file-hierarchy(7)

       MS_NOSUID
	   systemd.exec(5)

       MS_SLAVE
	   systemd.exec(5)

       NETLINK_PKTINFO
	   systemd.socket(5)

       NL
	   systemctl(1)

       NO_ADDRESS
	   org.freedesktop.resolve1(5)

       NO_AUTO_START
	   sd_bus_message_set_expect_reply(3)

       NO_REPLY_EXPECTED
	   sd_bus_message_set_expect_reply(3)

       NUL
	   crypttab(5), journald.conf(5), pam_systemd(8), sd-id128(3), sd_bus_creds_get_pid(3), sd_bus_message_append(3), sd_bus_message_append_basic(3),
	   sd_bus_message_append_string_memfd(3), sd_bus_message_append_strv(3), sd_bus_message_read(3), sd_bus_message_read_array(3), sd_bus_path_encode(3),
	   sd_event_source_set_description(3), sd_hwdb_get(3), sd_id128_to_string(3), sd_journal_add_match(3), sd_path_lookup(3), systemd-ask-password(1),
	   systemd-journald.service(8), systemd-nspawn(1), systemd.exec(5), systemd.journal-fields(7), systemd.network(5), systemd.socket(5), systemd.unit(5),
	   udev(7), udev_device_has_tag(3)

       NULL
	   sd-login(3), sd_bus_add_match(3), sd_bus_add_node_enumerator(3), sd_bus_add_object(3), sd_bus_add_object_manager(3), sd_bus_attach_event(3),
	   sd_bus_call(3), sd_bus_can_send(3), sd_bus_close(3), sd_bus_creds_get_pid(3), sd_bus_creds_new_from_pid(3), sd_bus_default(3),
	   sd_bus_emit_signal(3), sd_bus_error(3), sd_bus_get_current_handler(3), sd_bus_interface_name_is_valid(3), sd_bus_is_open(3), sd_bus_list_names(3),
	   sd_bus_message_append(3), sd_bus_message_append_array(3), sd_bus_message_append_basic(3), sd_bus_message_append_strv(3), sd_bus_message_at_end(3),
	   sd_bus_message_copy(3), sd_bus_message_dump(3), sd_bus_message_get_signature(3), sd_bus_message_get_type(3), sd_bus_message_new(3),
	   sd_bus_message_new_method_call(3), sd_bus_message_new_method_error(3), sd_bus_message_new_signal(3), sd_bus_message_open_container(3),
	   sd_bus_message_read(3), sd_bus_message_read_array(3), sd_bus_message_read_basic(3), sd_bus_message_read_strv(3), sd_bus_message_rewind(3),
	   sd_bus_message_seal(3), sd_bus_message_sensitive(3), sd_bus_message_set_destination(3), sd_bus_message_set_expect_reply(3), sd_bus_message_skip(3),
	   sd_bus_message_verify_type(3), sd_bus_new(3), sd_bus_path_encode(3), sd_bus_process(3), sd_bus_query_sender_creds(3), sd_bus_reply_method_error(3),
	   sd_bus_reply_method_return(3), sd_bus_request_name(3), sd_bus_send(3), sd_bus_set_address(3), sd_bus_set_description(3),
	   sd_bus_set_exit_on_disconnect(3), sd_bus_set_method_call_timeout(3), sd_bus_set_property(3), sd_bus_set_sender(3), sd_bus_set_server(3),
	   sd_bus_slot_get_bus(3), sd_bus_slot_ref(3), sd_bus_slot_set_description(3), sd_bus_slot_set_destroy_callback(3), sd_bus_slot_set_floating(3),
	   sd_bus_slot_set_userdata(3), sd_bus_start(3), sd_bus_track_add_name(3), sd_bus_track_new(3), sd_device_ref(3), sd_event_add_child(3),
	   sd_event_add_defer(3), sd_event_add_inotify(3), sd_event_add_io(3), sd_event_add_memory_pressure(3), sd_event_add_signal(3), sd_event_add_time(3),
	   sd_event_exit(3), sd_event_new(3), sd_event_run(3), sd_event_source_get_event(3), sd_event_source_set_description(3),
	   sd_event_source_set_destroy_callback(3), sd_event_source_set_enabled(3), sd_event_source_set_floating(3), sd_event_source_set_prepare(3),
	   sd_event_source_set_userdata(3), sd_event_source_unref(3), sd_event_wait(3), sd_get_seats(3), sd_hwdb_get(3), sd_hwdb_new(3),
	   sd_id128_to_string(3), sd_is_fifo(3), sd_journal_get_cutoff_realtime_usec(3), sd_journal_get_data(3), sd_journal_get_realtime_usec(3),
	   sd_journal_get_seqnum(3), sd_journal_has_runtime_files(3), sd_journal_open(3), sd_journal_print(3), sd_journal_query_unique(3), sd_listen_fds(3),
	   sd_login_monitor_new(3), sd_machine_get_class(3), sd_path_lookup(3), sd_pid_get_owner_uid(3), sd_seat_get_active(3), sd_session_is_active(3),
	   sd_uid_get_state(3), sd_watchdog_enabled(3), udev_device_get_syspath(3), udev_device_has_tag(3), udev_device_new_from_syspath(3),
	   udev_enumerate_new(3), udev_enumerate_scan_devices(3), udev_list_entry(3), udev_monitor_new_from_netlink(3), udev_monitor_receive_device(3),
	   udev_new(3)

       OP
	   systemd-analyze(1)

       OR
	   systemd.exec(5)

       O_DSYNC
	   systemd-nspawn(1)

       O_NOCTTY
	   daemon(7)

       O_NONBLOCK
	   sd_event_add_io(3), sd_journal_stream_fd(3), systemd.service(5)

       O_PATH
	   sd_event_add_inotify(3)

       O_RDONLY
	   org.freedesktop.systemd1(5)

       O_RDWR
	   org.freedesktop.systemd1(5)

       O_SYNC
	   systemd-nspawn(1)

       P
	   systemd.net-naming-scheme(7)

       PACKET_AUXDATA
	   systemd.socket(5)

       PAM_SUCCESS
	   pam_systemd(8)

       PID
	   sd_pid_get_owner_uid(3)

       PIDFD
	   sd_pid_get_owner_uid(3)

       POLLERR
	   systemd.service(5)

       POLLHUP
	   systemd.service(5)

       POLLIN
	   sd_bus_get_fd(3), sd_event_add_memory_pressure(3), sd_event_get_fd(3), sd_journal_get_fd(3), sd_login_monitor_new(3)

       POLLOUT
	   sd_bus_get_fd(3), sd_journal_get_fd(3), sd_login_monitor_new(3)

       POLLPRI
	   sd_event_add_memory_pressure(3)

       PROT_EXEC
	   file-hierarchy(7), systemd.exec(5)

       PROT_WRITE
	   systemd.exec(5)

       PR_SET_NO_NEW_PRIVS
	   systemd-nspawn(1), systemd.nspawn(5)

       READY=1
	   systemd(1)

       RLIMIT_NICE
	   systemd-nspawn(1)

       RLIMIT_NOFILE
	   daemon(7), systemd-nspawn(1)

       RLIMIT_NPROC
	   systemd-nspawn(1)

       SCHED_DEADLINE
	   systemd.exec(5)

       SCHED_FIFO
	   systemd.exec(5)

       SCHED_RR
	   systemd.exec(5)

       SD_BUS_ARGS(...)
	   sd_bus_add_object(3)

       SD_BUS_ARGS()
	   sd_bus_add_object(3)

       SD_BUS_CREDS_AUDIT_LOGIN_UID
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_AUDIT_SESSION_ID
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_AUGMENT
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_BOUNDING_CAPS
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_CGROUP
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_CMDLINE
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_COMM
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_DESCRIPTION
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_EFFECTIVE_CAPS
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_EGID
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_EUID
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_EXE
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_FSGID
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_FSUID
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_GID
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_INHERITABLE_CAPS
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_OWNER_UID
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_PERMITTED_CAPS
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_PID
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_PPID
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_SELINUX_CONTEXT
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_SESSION
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_SGID
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_SLICE
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_SUID
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_SUPPLEMENTARY_GIDS
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_TID
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_TID_COMM
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_TTY
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_UID
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_UNIQUE_NAME
	   sd_bus_creds_new_from_pid(3), sd_bus_negotiate_fds(3)

       SD_BUS_CREDS_UNIT
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_USER_SLICE
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_USER_UNIT
	   sd_bus_creds_new_from_pid(3)

       SD_BUS_CREDS_WELL_KNOWN_NAMES
	   sd_bus_creds_new_from_pid(3), sd_bus_negotiate_fds(3)

       SD_BUS_ERROR_ACCESS_DENIED
	   sd-bus-errors(3)

       SD_BUS_ERROR_ADDRESS_IN_USE
	   sd-bus-errors(3)

       SD_BUS_ERROR_AUTH_FAILED
	   sd-bus-errors(3)

       SD_BUS_ERROR_BAD_ADDRESS
	   sd-bus-errors(3)

       SD_BUS_ERROR_DISCONNECTED
	   sd-bus-errors(3)

       SD_BUS_ERROR_FAILED
	   sd-bus-errors(3)

       SD_BUS_ERROR_FILE_EXISTS
	   sd-bus-errors(3)

       SD_BUS_ERROR_FILE_NOT_FOUND
	   sd-bus-errors(3)

       SD_BUS_ERROR_INCONSISTENT_MESSAGE
	   sd-bus-errors(3)

       SD_BUS_ERROR_INTERACTIVE_AUTHORIZATION_REQUIRED
	   sd-bus-errors(3)

       SD_BUS_ERROR_INVALID_ARGS
	   sd-bus-errors(3)

       SD_BUS_ERROR_INVALID_SIGNATURE
	   sd-bus-errors(3)

       SD_BUS_ERROR_IO_ERROR
	   sd-bus-errors(3)

       SD_BUS_ERROR_LIMITS_EXCEEDED
	   sd-bus-errors(3)

       SD_BUS_ERROR_MAKE_CONST(name, message)
	   sd_bus_error(3)

       SD_BUS_ERROR_MAKE_CONST()
	   sd_bus_error(3)

       SD_BUS_ERROR_MAP(name, code)
	   sd_bus_error_add_map(3)

       SD_BUS_ERROR_MAP()
	   sd_bus_error_add_map(3)

       SD_BUS_ERROR_MAP_END
	   sd_bus_error_add_map(3)

       SD_BUS_ERROR_MATCH_RULE_INVALID
	   sd-bus-errors(3)

       SD_BUS_ERROR_MATCH_RULE_NOT_FOUND
	   sd-bus-errors(3)

       SD_BUS_ERROR_NAME_HAS_NO_OWNER
	   sd-bus-errors(3)

       SD_BUS_ERROR_NOT_SUPPORTED
	   sd-bus-errors(3), sd_bus_message_new_method_error(3)

       SD_BUS_ERROR_NO_MEMORY
	   sd-bus-errors(3), sd_bus_error(3)

       SD_BUS_ERROR_NO_NETWORK
	   sd-bus-errors(3)

       SD_BUS_ERROR_NO_REPLY
	   sd-bus-errors(3)

       SD_BUS_ERROR_NO_SERVER
	   sd-bus-errors(3)

       SD_BUS_ERROR_NULL
	   sd_bus_call(3), sd_bus_error(3)

       SD_BUS_ERROR_PROPERTY_READ_ONLY
	   sd-bus-errors(3)

       SD_BUS_ERROR_SERVICE_UNKNOWN
	   sd-bus-errors(3)

       SD_BUS_ERROR_TIMEOUT
	   sd-bus-errors(3)

       SD_BUS_ERROR_UNIX_PROCESS_ID_UNKNOWN
	   sd-bus-errors(3)

       SD_BUS_ERROR_UNKNOWN_INTERFACE
	   sd-bus-errors(3)

       SD_BUS_ERROR_UNKNOWN_METHOD
	   sd-bus-errors(3)

       SD_BUS_ERROR_UNKNOWN_OBJECT
	   sd-bus-errors(3)

       SD_BUS_ERROR_UNKNOWN_PROPERTY
	   sd-bus-errors(3)

       SD_BUS_MESSAGE_DUMP_SUBTREE_ONLY
	   sd_bus_message_dump(3)

       SD_BUS_MESSAGE_DUMP_WITH_HEADER
	   sd_bus_message_dump(3)

       SD_BUS_MESSAGE_METHOD_CALL
	   sd_bus_message_get_type(3), sd_bus_message_new(3)

       SD_BUS_MESSAGE_METHOD_ERROR
	   sd_bus_message_get_type(3), sd_bus_message_new(3)

       SD_BUS_MESSAGE_METHOD_RETURN
	   sd_bus_message_get_type(3), sd_bus_message_new(3)

       SD_BUS_MESSAGE_SIGNAL
	   sd_bus_message_get_type(3), sd_bus_message_new(3)

       SD_BUS_METHOD(member, signature, result, handler, flags)
	   sd_bus_add_object(3)

       SD_BUS_METHOD()
	   sd_bus_add_object(3)

       SD_BUS_METHOD_WITH_ARGS(member, args, result, handler, flags)
	   sd_bus_add_object(3)

       SD_BUS_METHOD_WITH_ARGS()
	   sd_bus_add_object(3)

       SD_BUS_METHOD_WITH_ARGS_OFFSET(member, args, result, handler, offset, flags)
	   sd_bus_add_object(3)

       SD_BUS_METHOD_WITH_ARGS_OFFSET()
	   sd_bus_add_object(3)

       SD_BUS_METHOD_WITH_NAMES(member, signature, in_names, result, out_names, handler, flags)
	   sd_bus_add_object(3)

       SD_BUS_METHOD_WITH_NAMES()
	   sd_bus_add_object(3)

       SD_BUS_METHOD_WITH_NAMES_OFFSET(member, signature, in_names, result, out_names, handler, offset, flags)
	   sd_bus_add_object(3)

       SD_BUS_METHOD_WITH_NAMES_OFFSET()
	   sd_bus_add_object(3)

       SD_BUS_METHOD_WITH_OFFSET(member, signature, result, handler, offset, flags)
	   sd_bus_add_object(3)

       SD_BUS_METHOD_WITH_OFFSET()
	   sd_bus_add_object(3)

       SD_BUS_NAME_ALLOW_REPLACEMENT
	   sd_bus_request_name(3)

       SD_BUS_NAME_QUEUE
	   sd_bus_request_name(3)

       SD_BUS_NAME_REPLACE_EXISTING
	   sd_bus_request_name(3)

       SD_BUS_NO_ARGS
	   sd_bus_add_object(3)

       SD_BUS_NO_RESULT
	   sd_bus_add_object(3)

       SD_BUS_PARAM(name)
	   sd_bus_add_object(3)

       SD_BUS_PARAM()
	   sd_bus_add_object(3)

       SD_BUS_PROPERTY(member, signature, get, offset, flags)
	   sd_bus_add_object(3)

       SD_BUS_PROPERTY()
	   sd_bus_add_object(3)

       SD_BUS_RESULT(...)
	   sd_bus_add_object(3)

       SD_BUS_RESULT()
	   sd_bus_add_object(3)

       SD_BUS_SIGNAL(member, signature, flags)
	   sd_bus_add_object(3)

       SD_BUS_SIGNAL()
	   sd_bus_add_object(3)

       SD_BUS_SIGNAL_WITH_ARGS(member, args, flags)
	   sd_bus_add_object(3)

       SD_BUS_SIGNAL_WITH_ARGS()
	   sd_bus_add_object(3)

       SD_BUS_SIGNAL_WITH_NAMES(member, signature, names, flags)
	   sd_bus_add_object(3)

       SD_BUS_SIGNAL_WITH_NAMES()
	   sd_bus_add_object(3)

       SD_BUS_TYPE
	   sd_bus_can_send(3)

       SD_BUS_TYPE_ARRAY
	   sd_bus_message_append(3), sd_bus_message_open_container(3), sd_bus_message_read(3)

       SD_BUS_TYPE_BOOLEAN
	   sd_bus_message_append(3), sd_bus_message_append_basic(3), sd_bus_message_read(3), sd_bus_message_read_basic(3)

       SD_BUS_TYPE_BYTE
	   sd_bus_message_append(3), sd_bus_message_append_basic(3), sd_bus_message_read(3), sd_bus_message_read_basic(3)

       SD_BUS_TYPE_DICT_ENTRY
	   sd_bus_message_open_container(3)

       SD_BUS_TYPE_DICT_ENTRY_BEGIN
	   sd_bus_message_append(3), sd_bus_message_read(3)

       SD_BUS_TYPE_DICT_ENTRY_END
	   sd_bus_message_append(3), sd_bus_message_read(3)

       SD_BUS_TYPE_DOUBLE
	   sd_bus_message_append(3), sd_bus_message_append_basic(3), sd_bus_message_read(3), sd_bus_message_read_basic(3)

       SD_BUS_TYPE_INT16
	   sd_bus_message_append(3), sd_bus_message_append_basic(3), sd_bus_message_read(3), sd_bus_message_read_basic(3)

       SD_BUS_TYPE_INT32
	   sd_bus_message_append(3), sd_bus_message_append_basic(3), sd_bus_message_read(3), sd_bus_message_read_basic(3)

       SD_BUS_TYPE_INT64
	   sd_bus_message_append(3), sd_bus_message_append_basic(3), sd_bus_message_read(3), sd_bus_message_read_basic(3)

       SD_BUS_TYPE_OBJECT_PATH
	   sd_bus_message_append(3), sd_bus_message_append_basic(3), sd_bus_message_read(3), sd_bus_message_read_basic(3)

       SD_BUS_TYPE_SIGNATURE
	   sd_bus_message_append(3), sd_bus_message_append_basic(3), sd_bus_message_read(3), sd_bus_message_read_basic(3)

       SD_BUS_TYPE_STRING
	   sd_bus_message_append(3), sd_bus_message_append_basic(3), sd_bus_message_read(3), sd_bus_message_read_basic(3)

       SD_BUS_TYPE_STRUCT
	   sd_bus_message_open_container(3)

       SD_BUS_TYPE_STRUCT_BEGIN
	   sd_bus_message_append(3), sd_bus_message_read(3)

       SD_BUS_TYPE_STRUCT_END
	   sd_bus_message_append(3), sd_bus_message_read(3)

       SD_BUS_TYPE_UINT16
	   sd_bus_message_append(3), sd_bus_message_append_basic(3), sd_bus_message_read(3), sd_bus_message_read_basic(3)

       SD_BUS_TYPE_UINT32
	   sd_bus_message_append(3), sd_bus_message_append_basic(3), sd_bus_message_read(3), sd_bus_message_read_basic(3)

       SD_BUS_TYPE_UINT64
	   sd_bus_message_append(3), sd_bus_message_append_basic(3), sd_bus_message_read(3), sd_bus_message_read_basic(3)

       SD_BUS_TYPE_UNIX_FD
	   sd_bus_message_append(3), sd_bus_message_append_basic(3), sd_bus_message_read(3), sd_bus_message_read_basic(3), sd_bus_negotiate_fds(3)

       SD_BUS_TYPE_VARIANT
	   sd_bus_message_append(3), sd_bus_message_open_container(3), sd_bus_message_read(3)

       SD_BUS_VTABLE_ABSOLUTE_OFFSET
	   sd_bus_add_object(3)

       SD_BUS_VTABLE_CAPABILITY(capability)
	   sd_bus_add_object(3)

       SD_BUS_VTABLE_DEPRECATED
	   sd_bus_add_object(3)

       SD_BUS_VTABLE_END
	   sd_bus_add_object(3)

       SD_BUS_VTABLE_HIDDEN
	   sd_bus_add_object(3)

       SD_BUS_VTABLE_METHOD_NO_REPLY
	   sd_bus_add_object(3)

       SD_BUS_VTABLE_PROPERTY_CONST
	   sd_bus_add_object(3)

       SD_BUS_VTABLE_PROPERTY_EMITS_CHANGE
	   sd_bus_add_object(3)

       SD_BUS_VTABLE_PROPERTY_EMITS_INVALIDATION
	   sd_bus_add_object(3)

       SD_BUS_VTABLE_PROPERTY_EXPLICIT
	   sd_bus_add_object(3)

       SD_BUS_VTABLE_SENSITIVE
	   sd_bus_add_object(3)

       SD_BUS_VTABLE_START(flags)
	   sd_bus_add_object(3)

       SD_BUS_VTABLE_START()
	   sd_bus_add_object(3)

       SD_BUS_VTABLE_UNPRIVILEGED
	   sd_bus_add_object(3)

       SD_BUS_WRITABLE_PROPERTY(member, signature, get, set, offset, flags)
	   sd_bus_add_object(3)

       SD_BUS_WRITABLE_PROPERTY()
	   sd_bus_add_object(3)

       SD_EVENT_ARMED
	   sd_event_wait(3)

       SD_EVENT_EXITING
	   sd_event_wait(3)

       SD_EVENT_FINISHED
	   sd_event_wait(3)

       SD_EVENT_INITIAL
	   sd_event_wait(3)

       SD_EVENT_OFF
	   sd_event_add_child(3), sd_event_add_defer(3), sd_event_add_io(3), sd_event_add_memory_pressure(3), sd_event_add_signal(3), sd_event_add_time(3),
	   sd_event_source_set_enabled(3), sd_event_source_set_ratelimit(3), sd_event_source_unref(3)

       SD_EVENT_ON
	   sd_event_add_child(3), sd_event_add_defer(3), sd_event_add_inotify(3), sd_event_add_io(3), sd_event_add_signal(3), sd_event_add_time(3),
	   sd_event_source_set_enabled(3)

       SD_EVENT_ONESHOT
	   sd_event_add_child(3), sd_event_add_defer(3), sd_event_add_inotify(3), sd_event_add_time(3), sd_event_source_set_enabled(3)

       SD_EVENT_PENDING
	   sd_event_wait(3)

       SD_EVENT_PREPARING
	   sd_event_wait(3)

       SD_EVENT_PRIORITY_IDLE
	   sd_event_source_set_priority(3)

       SD_EVENT_PRIORITY_IMPORTANT
	   sd_event_source_set_priority(3)

       SD_EVENT_PRIORITY_NORMAL
	   sd_event_source_set_priority(3)

       SD_EVENT_RUNNING
	   sd_event_wait(3)

       SD_EVENT_SIGNAL_PROCMASK
	   sd_event_add_signal(3)

       SD_GPT_ESP
	   systemd-gpt-auto-generator(8)

       SD_GPT_FLAG_NO_AUTO
	   systemd-gpt-auto-generator(8)

       SD_GPT_FLAG_NO_BLOCK_IO_PROTOCOL
	   systemd-gpt-auto-generator(8)

       SD_GPT_FLAG_READ_ONLY
	   systemd-gpt-auto-generator(8)

       SD_GPT_HOME
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_ALPHA
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_ARC
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_ARM
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_ARM64
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_IA64
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_LOONGARCH64
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_MIPS
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_MIPS64
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_MIPS64_LE
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_MIPS_LE
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_PARISC
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_PPC
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_PPC64
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_PPC64_LE
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_RISCV32
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_RISCV64
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_S390
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_S390X
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_TILEGX
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_X86
	   systemd-gpt-auto-generator(8)

       SD_GPT_ROOT_X86_64
	   systemd-gpt-auto-generator(8)

       SD_GPT_SRV
	   systemd-gpt-auto-generator(8)

       SD_GPT_SWAP
	   systemd-gpt-auto-generator(8)

       SD_GPT_TMP
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_ALPHA
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_ARC
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_ARM
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_IA64
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_LOONGARCH64
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_MIPS64_LE
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_MIPS_LE
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_PARISC
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_PPC
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_PPC64
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_PPC64_LE
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_RISCV32
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_RISCV64
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_S390
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_S390X
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_TILEGX
	   systemd-gpt-auto-generator(8)

       SD_GPT_USR_X86
	   systemd-gpt-auto-generator(8)

       SD_GPT_VAR
	   systemd-gpt-auto-generator(8)

       SD_GPT_XBOOTLDR
	   systemd-gpt-auto-generator(8)

       SD_ID128_ALLF
	   sd-id128(3), sd_id128_get_machine(3), sd_id128_randomize(3)

       SD_ID128_CONST_STR(id)
	   sd-id128(3)

       SD_ID128_FORMAT_STR
	   sd-id128(3), sd_id128_to_string(3)

       SD_ID128_FORMAT_VAL(id)
	   sd-id128(3)

       SD_ID128_MAKE(v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, vA, vB, vC, vD, vE, vF)
	   sd-id128(3)

       SD_ID128_MAKE_STR(v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, vA, vB, vC, vD, vE, vF)
	   sd-id128(3)

       SD_ID128_MAKE_UUID_STR(v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, vA, vB, vC, vD, vE, vF)
	   sd-id128(3)

       SD_ID128_NULL
	   sd-id128(3), sd_bus_set_server(3), sd_id128_get_machine(3), sd_id128_randomize(3)

       SD_ID128_STRING_MAX
	   sd_id128_to_string(3)

       SD_ID128_UUID_FORMAT_STR
	   sd-id128(3)

       SD_JOURNAL_ALL_NAMESPACES
	   sd_journal_open(3)

       SD_JOURNAL_APPEND
	   sd_journal_get_fd(3)

       SD_JOURNAL_CURRENT_USER
	   sd_journal_open(3)

       SD_JOURNAL_INCLUDE_DEFAULT_NAMESPACE
	   sd_journal_open(3)

       SD_JOURNAL_INVALIDATE
	   sd_journal_get_fd(3)

       SD_JOURNAL_LOCAL_ONLY
	   sd_journal_get_usage(3), sd_journal_open(3)

       SD_JOURNAL_NOP
	   sd_journal_get_fd(3)

       SD_JOURNAL_OS_ROOT
	   sd_journal_open(3)

       SD_JOURNAL_RUNTIME_ONLY
	   sd_journal_open(3)

       SD_JOURNAL_SUPPRESS_LOCATION
	   sd_journal_print(3)

       SD_JOURNAL_SYSTEM
	   sd_journal_open(3)

       SD_JOURNAL_TAKE_DIRECTORY_FD
	   sd_journal_open(3)

       SD_LISTEN_FDS_START
	   sd_listen_fds(3)

       SD_LOGIND_KEXEC_REBOOT
	   org.freedesktop.login1(5)

       SD_LOGIND_ROOT_CHECK_INHIBITORS
	   org.freedesktop.login1(5)

       SD_LOGIND_SOFT_REBOOT
	   org.freedesktop.login1(5)

       SD_LOGIND_SOFT_REBOOT_IF_NEXTROOT_SET_UP
	   org.freedesktop.login1(5)

       SD_PATH_BINFMT
	   sd_path_lookup(3)

       SD_PATH_CATALOG
	   sd_path_lookup(3)

       SD_PATH_MODULES_LOAD
	   sd_path_lookup(3)

       SD_PATH_SEARCH_BINARIES
	   sd_path_lookup(3)

       SD_PATH_SEARCH_BINARIES_DEFAULT
	   sd_path_lookup(3)

       SD_PATH_SEARCH_CONFIGURATION
	   sd_path_lookup(3)

       SD_PATH_SEARCH_CONFIGURATION_FACTORY
	   sd_path_lookup(3)

       SD_PATH_SEARCH_LIBRARY_ARCH
	   sd_path_lookup(3)

       SD_PATH_SEARCH_LIBRARY_PRIVATE
	   sd_path_lookup(3)

       SD_PATH_SEARCH_SHARED
	   sd_path_lookup(3)

       SD_PATH_SEARCH_STATE_FACTORY
	   sd_path_lookup(3)

       SD_PATH_SYSCTL
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_SEARCH_NETWORK
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_SEARCH_SYSTEM_ENVIRONMENT_GENERATOR
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_SEARCH_SYSTEM_GENERATOR
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_SEARCH_SYSTEM_UNIT
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_SEARCH_USER_ENVIRONMENT_GENERATOR
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_SEARCH_USER_GENERATOR
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_SEARCH_USER_UNIT
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_SHUTDOWN
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_SLEEP
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_SYSTEM_CONF
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_SYSTEM_ENVIRONMENT_GENERATOR
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_SYSTEM_GENERATOR
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_SYSTEM_PRESET
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_SYSTEM_UNIT
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_USER_CONF
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_USER_ENVIRONMENT_GENERATOR
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_USER_GENERATOR
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_USER_PRESET
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_USER_UNIT
	   sd_path_lookup(3)

       SD_PATH_SYSTEMD_UTIL
	   sd_path_lookup(3)

       SD_PATH_SYSTEM_BINARIES
	   sd_path_lookup(3)

       SD_PATH_SYSTEM_CONFIGURATION
	   sd_path_lookup(3)

       SD_PATH_SYSTEM_CONFIGURATION_FACTORY
	   sd_path_lookup(3)

       SD_PATH_SYSTEM_INCLUDE
	   sd_path_lookup(3)

       SD_PATH_SYSTEM_LIBRARY_ARCH
	   sd_path_lookup(3)

       SD_PATH_SYSTEM_LIBRARY_PRIVATE
	   sd_path_lookup(3)

       SD_PATH_SYSTEM_RUNTIME
	   sd_path_lookup(3)

       SD_PATH_SYSTEM_RUNTIME_LOGS
	   sd_path_lookup(3)

       SD_PATH_SYSTEM_SHARED
	   sd_path_lookup(3)

       SD_PATH_SYSTEM_STATE_CACHE
	   sd_path_lookup(3)

       SD_PATH_SYSTEM_STATE_FACTORY
	   sd_path_lookup(3)

       SD_PATH_SYSTEM_STATE_LOGS
	   sd_path_lookup(3)

       SD_PATH_SYSTEM_STATE_PRIVATE
	   sd_path_lookup(3)

       SD_PATH_SYSTEM_STATE_SPOOL
	   sd_path_lookup(3)

       SD_PATH_SYSUSERS
	   sd_path_lookup(3)

       SD_PATH_TEMPORARY
	   sd_path_lookup(3)

       SD_PATH_TEMPORARY_LARGE
	   sd_path_lookup(3)

       SD_PATH_TMPFILES
	   sd_path_lookup(3)

       SD_PATH_USER
	   sd_path_lookup(3)

       SD_PATH_USER_BINARIES
	   sd_path_lookup(3)

       SD_PATH_USER_CONFIGURATION
	   sd_path_lookup(3)

       SD_PATH_USER_DESKTOP
	   sd_path_lookup(3)

       SD_PATH_USER_DOCUMENTS
	   sd_path_lookup(3)

       SD_PATH_USER_DOWNLOAD
	   sd_path_lookup(3)

       SD_PATH_USER_LIBRARY_ARCH
	   sd_path_lookup(3)

       SD_PATH_USER_LIBRARY_PRIVATE
	   sd_path_lookup(3)

       SD_PATH_USER_MUSIC
	   sd_path_lookup(3)

       SD_PATH_USER_PICTURES
	   sd_path_lookup(3)

       SD_PATH_USER_PUBLIC
	   sd_path_lookup(3)

       SD_PATH_USER_RUNTIME
	   sd_path_lookup(3)

       SD_PATH_USER_SHARED
	   sd_path_lookup(3)

       SD_PATH_USER_STATE_CACHE
	   sd_path_lookup(3)

       SD_PATH_USER_STATE_PRIVATE
	   sd_path_lookup(3)

       SD_PATH_USER_TEMPLATES
	   sd_path_lookup(3)

       SD_PATH_USER_VIDEOS
	   sd_path_lookup(3)

       SD_WARNING
	   sd_journal_stream_fd(3)

       SEQNUM
	   udev_device_new_from_syspath(3)

       SHM_EXEC
	   systemd.exec(5)

       SIGABRT
	   systemd-udevd.service(8), systemd.kill(5), systemd.service(5)

       SIGCHLD
	   sd_event_add_child(3)

       SIGCONT
	   systemd.kill(5)

       SIGHUP
	   daemon(7), org.freedesktop.hostname1(5), systemd(1), systemd.kill(5), systemd.service(5)

       SIGINT
	   loginctl(1), machinectl(1), sd_event_set_signal_exit(3), systemctl(1), systemd(1), systemd.service(5), systemd.special(7)

       SIGKILL
	   sd_event_add_child(3), systemd-nspawn(1), systemd-oomd.service(8), systemd-soft-reboot.service(8), systemd-udevd.service(8), systemd.kill(5),
	   systemd.mount(5), systemd.resource-control(5), systemd.service(5), systemd.socket(5), systemd.swap(5)

       SIGPIPE
	   systemd-journald.service(8), systemd.exec(5), systemd.service(5)

       SIGPWR
	   systemd(1)

       SIGQUIT
	   systemd.kill(5)

       SIGRTMAX-...
	   org.freedesktop.systemd1(5)

       SIGRTMIN+0
	   systemd(1)

       SIGRTMIN+1
	   resolvectl(1), systemd(1), systemd-resolved.service(8)

       SIGRTMIN+13
	   systemd(1)

       SIGRTMIN+14
	   systemd(1)

       SIGRTMIN+15
	   systemd(1)

       SIGRTMIN+16
	   systemd(1)

       SIGRTMIN+17
	   systemd(1)

       SIGRTMIN+2
	   systemd(1)

       SIGRTMIN+20
	   systemd(1)

       SIGRTMIN+21
	   systemd(1)

       SIGRTMIN+22
	   systemd(1)

       SIGRTMIN+23
	   systemd(1)

       SIGRTMIN+24
	   systemd(1)

       SIGRTMIN+25
	   systemd(1)

       SIGRTMIN+26
	   systemd(1)

       SIGRTMIN+27
	   systemd(1)

       SIGRTMIN+28
	   systemd(1)

       SIGRTMIN+3
	   systemd(1), systemd-nspawn(1)

       SIGRTMIN+4
	   systemd(1)

       SIGRTMIN+5
	   systemd(1)

       SIGRTMIN+6
	   systemd(1)

       SIGRTMIN+7
	   systemd(1)

       SIGRTMIN+...
	   org.freedesktop.systemd1(5)

       SIGSTOP
	   loginctl(1), machinectl(1), systemctl(1)

       SIGSYS
	   systemd.exec(5)

       SIGTERM
	   daemon(7), loginctl(1), machinectl(1), org.freedesktop.systemd1(5), sd_event_exit(3), sd_event_set_signal_exit(3), systemctl(1), systemd(1),
	   systemd-nspawn(1), systemd-soft-reboot.service(8), systemd.kill(5), systemd.mount(5), systemd.service(5), systemd.socket(5), systemd.special(7),
	   systemd.swap(5)

       SIGUSR1
	   journald.conf(5), systemd(1), systemd-journald.service(8), systemd-resolved.service(8)

       SIGUSR2
	   resolvectl(1), systemd(1), systemd-resolved.service(8)

       SIGWINCH
	   systemd(1)

       SIG_DFL
	   daemon(7)

       SOCK_DGRAM
	   sd_is_fifo(3), sd_notify(3), systemd(1), systemd-socket-activate(1), systemd.socket(5)

       SOCK_RAW
	   systemd.socket(5)

       SOCK_SEQPACKET
	   sd_notify(3), systemd(1), systemd-socket-activate(1), systemd.exec(5), systemd.socket(5)

       SOCK_STREAM
	   sd_is_fifo(3), systemd-socket-activate(1), systemd.socket(5)

       SO_BINDTODEVICE
	   systemd.socket(5)

       SO_BROADCAST
	   systemd.socket(5)

       SO_KEEPALIVE
	   systemd.socket(5)

       SO_MARK
	   systemd.socket(5)

       SO_PASSCRED
	   systemd.socket(5)

       SO_PASSSEC
	   systemd.socket(5)

       SO_PRIORITY
	   systemd.netdev(5), systemd.network(5), systemd.socket(5)

       SO_RCVBUF
	   systemd.socket(5)

       SO_REUSEPORT
	   systemd.socket(5)

       SO_SNDBUF
	   systemd.socket(5)

       SO_TIMESTAMP
	   systemd.socket(5)

       SO_TIMESTAMPNS
	   systemd.socket(5)

       SUBSYSTEM
	   udev_device_new_from_syspath(3)

       S_IFREG
	   org.freedesktop.systemd1(5)

       S_IRUSR
	   org.freedesktop.systemd1(5)

       TAB
	   systemctl(1)

       TCP_DEFER_ACCEPT
	   systemd.socket(5)

       TCP_KEEPINTVL
	   systemd.socket(5)

       TEMPFAIL
	   systemd.service(5)

       TFD_TIMER_CANCEL_ON_SET
	   org.freedesktop.timedate1(5)

       TIOCSTI
	   systemd-nspawn(1)

       U+0000
	   systemd.exec(5)

       U+FEFF
	   systemd.exec(5)

       UINT64_MAX
	   org.freedesktop.home1(5), sd_bus_get_fd(3), sd_bus_wait(3), sd_event_add_time(3)

       USER_PROCESS
	   systemd.exec(5)

       WCONTINUED
	   sd_event_add_child(3)

       WEXITED
	   sd_event_add_child(3)

       WSTOPPED
	   sd_event_add_child(3)

       X
	   systemd.net-naming-scheme(7)

       _NSIG
	   daemon(7)

       _SC_ARG_MAX
	   systemctl(1)

       _SD_BUS_CREDS_ALL
	   sd_bus_creds_new_from_pid(3)

       a
	   systemd.net-naming-scheme(7), tmpfiles.d(5)

       abcmABM
	   tmpfiles.d(5)

       activating
	   systemctl(1)

       active
	   systemctl(1)

       alert
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       all
	   journalctl(1), systemctl(1), systemd.exec(5), udevadm(8)

       alpha
	   repart.d(5), systemd.exec(5)

       any
	   systemd.resource-control(5)

       application/json
	   systemd-journal-gatewayd.service(8)

       application/vnd.fdo.journal
	   systemd-journal-gatewayd.service(8)

       arc
	   repart.d(5)

       argv[0]
	   systemd.service(5)

       arm
	   repart.d(5), systemd.exec(5)

       arm-be
	   systemd.exec(5)

       arm64
	   repart.d(5), systemd-system.conf(5), systemd.dnssd(5), systemd.exec(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       arm64-be
	   systemd.exec(5)

       auto
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       b
	   systemd.net-naming-scheme(7), tmpfiles.d(5), udev_device_new_from_syspath(3)

       b921b045-1df0-41c3-af44-4c6f280d3fae
	   systemd-gpt-auto-generator(8)

       bad-setting
	   systemctl(1)

       basic.target
	   systemd-soft-reboot.service(8)

       bc13c2ff-59e6-4262-a352-b275fd6f7172
	   systemd-gpt-auto-generator(8)

       bind4
	   systemd.resource-control(5)

       bind6
	   systemd.resource-control(5)

       boot
	   sysupdate.d(5)

       c
	   systemd.net-naming-scheme(7), tmpfiles.d(5), udev_device_new_from_syspath(3)

       c12a7328-f81f-11d2-ba4b-00a0c93ec93b
	   systemd-gpt-auto-generator(8)

       cache
	   systemctl(1)

       cgroup
	   systemd.exec(5)

       cgroup/bind4
	   systemd.resource-control(5)

       cgroup/bind6
	   systemd.resource-control(5)

       configuration
	   systemctl(1)

       connect4
	   systemd.resource-control(5)

       connect6
	   systemd.resource-control(5)

       console
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       console-prefixed
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       const
	   sd_bus_add_object(3)

       continue
	   systemd.scope(5), systemd.service(5)

       control-group
	   systemd.kill(5)

       crit
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       d
	   systemd.net-naming-scheme(7), tmpfiles.d(5)

       deactivating
	   systemctl(1)

       debug
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       default
	   systemd.exec(5)

       device
	   systemd.resource-control(5)

       directory
	   sysupdate.d(5)

       early
	   udevadm(8)

       egress
	   systemd.resource-control(5)

       elf-headers
	   systemd.exec(5)

       emerg
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       en
	   systemd.net-naming-scheme(7)

       enter-initrd
	   ukify(1)

       err
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       error
	   sd_bus_message_new_method_error(3), systemctl(1), systemd(1)

       esp
	   repart.d(5), systemd.exec(5), sysupdate.d(5)

       ext2
	   systemd.exec(5)

       ext4
	   systemd.exec(5)

       f
	   systemd.net-naming-scheme(7)

       failed
	   systemctl(1), systemd.unit(5)

       false
	   sd_bus_error(3)

       fdstore
	   systemctl(1)

       getsockopt
	   systemd.resource-control(5)

       h
	   tmpfiles.d(5)

       home
	   repart.d(5), systemd.exec(5)

       host
	   systemd-journal-remote.service(8)

       https
	   systemd-journal-upload.service(8)

       i
	   systemd.net-naming-scheme(7)

       ia64
	   repart.d(5)

       ib
	   systemd.net-naming-scheme(7)

       inactive
	   systemctl(1), systemd.unit(5)

       infinity
	   systemd-socket-proxyd(8), systemd.exec(5)

       info
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       ingress
	   systemd.resource-control(5)

       invalidates
	   sd_bus_add_object(3)

       io.systemd.DropIn
	   systemd-userdbd.service(8), userdbctl(1)

       io.systemd.DynamicUser
	   userdbctl(1)

       io.systemd.Home
	   userdbctl(1)

       io.systemd.Machine
	   userdbctl(1)

       io.systemd.Multiplexer
	   systemd-userdbd.service(8), userdbctl(1)

       io.systemd.NameServiceSwitch
	   systemd-userdbd.service(8), userdbctl(1)

       ipc
	   systemd.exec(5)

       ipv4
	   systemd.resource-control(5)

       ipv6
	   systemd.resource-control(5)

       journal
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       journal-or-kmsg
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       keep
	   systemd.net-naming-scheme(7)

       keep-caps
	   systemd.exec(5)

       kernel.modules_disabled
	   systemd.exec(5)

       kill
	   systemd.scope(5), systemd.service(5)

       kmsg
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       late
	   udevadm(8)

       latest
	   systemd.net-naming-scheme(7)

       leave-initrd
	   ukify(1)

       libsystemd
	   libsystemd(3), sd-bus(3), sd-bus-errors(3), sd-daemon(3), sd-device(3), sd-event(3), sd-hwdb(3), sd-id128(3), sd-journal(3), sd-login(3),
	   sd_booted(3), sd_bus_add_match(3), sd_bus_add_node_enumerator(3), sd_bus_add_object(3), sd_bus_add_object_manager(3), sd_bus_attach_event(3),
	   sd_bus_call(3), sd_bus_call_method(3), sd_bus_can_send(3), sd_bus_close(3), sd_bus_creds_get_pid(3), sd_bus_creds_new_from_pid(3),
	   sd_bus_default(3), sd_bus_emit_signal(3), sd_bus_enqueue_for_read(3), sd_bus_error(3), sd_bus_error_add_map(3), sd_bus_get_current_handler(3),
	   sd_bus_get_fd(3), sd_bus_get_name_creds(3), sd_bus_get_name_machine_id(3), sd_bus_interface_name_is_valid(3), sd_bus_is_open(3),
	   sd_bus_list_names(3), sd_bus_message_append(3), sd_bus_message_append_array(3), sd_bus_message_append_basic(3),
	   sd_bus_message_append_string_memfd(3), sd_bus_message_append_strv(3), sd_bus_message_at_end(3), sd_bus_message_copy(3), sd_bus_message_dump(3),
	   sd_bus_message_get_cookie(3), sd_bus_message_get_monotonic_usec(3), sd_bus_message_get_signature(3), sd_bus_message_get_type(3),
	   sd_bus_message_new(3), sd_bus_message_new_method_call(3), sd_bus_message_new_method_error(3), sd_bus_message_new_signal(3),
	   sd_bus_message_open_container(3), sd_bus_message_read(3), sd_bus_message_rewind(3), sd_bus_message_seal(3), sd_bus_message_sensitive(3),
	   sd_bus_message_set_destination(3), sd_bus_message_set_expect_reply(3), sd_bus_message_skip(3), sd_bus_message_verify_type(3),
	   sd_bus_negotiate_fds(3), sd_bus_new(3), sd_bus_path_encode(3), sd_bus_process(3), sd_bus_query_sender_creds(3), sd_bus_reply_method_error(3),
	   sd_bus_reply_method_return(3), sd_bus_request_name(3), sd_bus_send(3), sd_bus_set_address(3), sd_bus_set_close_on_exit(3),
	   sd_bus_set_connected_signal(3), sd_bus_set_description(3), sd_bus_set_exit_on_disconnect(3), sd_bus_set_fd(3), sd_bus_set_method_call_timeout(3),
	   sd_bus_set_property(3), sd_bus_set_sender(3), sd_bus_set_server(3), sd_bus_set_watch_bind(3), sd_bus_slot_get_bus(3), sd_bus_slot_ref(3),
	   sd_bus_slot_set_description(3), sd_bus_slot_set_destroy_callback(3), sd_bus_slot_set_floating(3), sd_bus_slot_set_userdata(3), sd_bus_start(3),
	   sd_bus_track_add_name(3), sd_bus_track_new(3), sd_bus_wait(3), sd_device_get_syspath(3), sd_event_add_child(3), sd_event_add_defer(3),
	   sd_event_add_inotify(3), sd_event_add_io(3), sd_event_add_memory_pressure(3), sd_event_add_signal(3), sd_event_add_time(3), sd_event_exit(3),
	   sd_event_get_fd(3), sd_event_new(3), sd_event_now(3), sd_event_run(3), sd_event_set_signal_exit(3), sd_event_set_watchdog(3),
	   sd_event_source_get_event(3), sd_event_source_get_pending(3), sd_event_source_set_description(3), sd_event_source_set_destroy_callback(3),
	   sd_event_source_set_enabled(3), sd_event_source_set_exit_on_failure(3), sd_event_source_set_floating(3), sd_event_source_set_prepare(3),
	   sd_event_source_set_priority(3), sd_event_source_set_ratelimit(3), sd_event_source_set_userdata(3), sd_event_source_unref(3), sd_event_wait(3),
	   sd_get_seats(3), sd_hwdb_get(3), sd_hwdb_new(3), sd_id128_get_machine(3), sd_id128_randomize(3), sd_id128_to_string(3), sd_is_fifo(3),
	   sd_journal_add_match(3), sd_journal_enumerate_fields(3), sd_journal_get_catalog(3), sd_journal_get_cursor(3),
	   sd_journal_get_cutoff_realtime_usec(3), sd_journal_get_data(3), sd_journal_get_fd(3), sd_journal_get_realtime_usec(3), sd_journal_get_seqnum(3),
	   sd_journal_get_usage(3), sd_journal_has_runtime_files(3), sd_journal_next(3), sd_journal_open(3), sd_journal_print(3), sd_journal_query_unique(3),
	   sd_journal_seek_head(3), sd_journal_stream_fd(3), sd_listen_fds(3), sd_login_monitor_new(3), sd_machine_get_class(3), sd_notify(3),
	   sd_path_lookup(3), sd_pid_get_owner_uid(3), sd_seat_get_active(3), sd_session_is_active(3), sd_uid_get_state(3), sd_watchdog_enabled(3)

       link-local
	   systemd.resource-control(5)

       linux-generic
	   repart.d(5), sysupdate.d(5)

       loaded
	   systemctl(1)

       localhost
	   systemd.resource-control(5)

       logs
	   systemctl(1)

       loongarch64
	   repart.d(5)

       m
	   systemd.resource-control(5), tmpfiles.d(5)

       m68k
	   systemd.exec(5)

       masked
	   systemctl(1)

       max_equalizers=N+1
	   systemd.network(5)

       min
	   tmpfiles.d(5)

       mips-le
	   repart.d(5)

       mips64-le
	   repart.d(5)

       mips64-le-n32
	   systemd.exec(5)

       mips64-n32
	   systemd.exec(5)

       mixed
	   systemd.kill(5)

       mnt
	   systemd.exec(5)

       more
	   varlinkctl(1)

       ms
	   tmpfiles.d(5)

       multi
	   systemd.resource-control(5)

       multicast
	   systemd.resource-control(5)

       n
	   systemd.net-naming-scheme(7)

       name
	   udevadm(8)

       native
	   systemd.exec(5)

       net
	   systemd.exec(5)

       never
	   udevadm(8)

       no
	   systemd.service(5)

       nobody
	   systemd-nspawn(1)

       noexec
	   systemd.exec(5)

       none
	   systemd-journal-remote.service(8), systemd.kill(5)

       not-found
	   systemctl(1)

       notice
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       null
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       o
	   systemd.net-naming-scheme(7)

       oneway
	   varlinkctl(1)

       org.freedesktop.DBus.Deprecated
	   sd_bus_add_object(3)

       org.freedesktop.DBus.Introspectable.Introspect
	   busctl(1), sd_bus_add_node_enumerator(3), sd_bus_add_object(3)

       org.freedesktop.DBus.Method.NoReply
	   sd_bus_add_object(3)

       org.freedesktop.DBus.ObjectManager
	   sd_bus_add_object_manager(3), sd_bus_emit_signal(3)

       org.freedesktop.DBus.ObjectManager.GetManagedObjects
	   sd_bus_add_node_enumerator(3)

       org.freedesktop.DBus.Peer
	   sd_bus_get_name_machine_id(3)

       org.freedesktop.DBus.Properties
	   sd_bus_emit_signal(3), sd_bus_set_property(3)

       org.freedesktop.DBus.Properties.PropertiesChanged
	   sd_bus_add_object(3)

       org.freedesktop.DBus.Property.EmitsChangedSignal
	   sd_bus_add_object(3)

       org.freedesktop.locale1.set-keyboard
	   org.freedesktop.locale1(5)

       org.freedesktop.locale1.set-locale
	   org.freedesktop.locale1(5)

       org.freedesktop.resolve1.Aborted
	   org.freedesktop.resolve1(5)

       org.freedesktop.resolve1.CNameLoop
	   org.freedesktop.resolve1(5)

       org.freedesktop.resolve1.DnsError.NXDOMAIN
	   org.freedesktop.resolve1(5)

       org.freedesktop.resolve1.DnsError.REFUSED
	   org.freedesktop.resolve1(5)

       org.freedesktop.resolve1.DnssecFailed
	   org.freedesktop.resolve1(5)

       org.freedesktop.resolve1.InvalidReply
	   org.freedesktop.resolve1(5)

       org.freedesktop.resolve1.LinkBusy
	   org.freedesktop.resolve1(5)

       org.freedesktop.resolve1.NetworkDown
	   org.freedesktop.resolve1(5)

       org.freedesktop.resolve1.NoNameServers
	   org.freedesktop.resolve1(5)

       org.freedesktop.resolve1.NoSuchLink
	   org.freedesktop.resolve1(5)

       org.freedesktop.resolve1.NoSuchRR
	   org.freedesktop.resolve1(5)

       org.freedesktop.resolve1.NoSuchService
	   org.freedesktop.resolve1(5)

       org.freedesktop.resolve1.NoTrustAnchor
	   org.freedesktop.resolve1(5)

       org.freedesktop.resolve1.ResourceRecordTypeUnsupported
	   org.freedesktop.resolve1(5)

       org.freedesktop.systemd1.Explicit
	   sd_bus_add_object(3)

       org.freedesktop.systemd1.Privileged
	   sd_bus_add_object(3)

       p
	   systemd.net-naming-scheme(7)

       parisc
	   repart.d(5)

       partition
	   sysupdate.d(5)

       path
	   udevadm(8)

       pid
	   systemd.exec(5)

       post_bind4
	   systemd.resource-control(5)

       post_bind6
	   systemd.resource-control(5)

       ppc
	   repart.d(5), systemd.exec(5)

       ppc-le
	   systemd.exec(5)

       ppc64
	   repart.d(5), systemd.exec(5)

       ppc64-le
	   repart.d(5), systemd.exec(5)

       private-anonymous
	   systemd.exec(5)

       private-dax
	   systemd.exec(5)

       private-file-backed
	   systemd.exec(5)

       private-huge
	   systemd.exec(5)

       process
	   systemd.kill(5)

       property
	   udevadm(8)

       r
	   systemd.net-naming-scheme(7), systemd.resource-control(5)

       random
	   systemd-repart(8)

       ready
	   ukify(1)

       recvmsg4
	   systemd.resource-control(5)

       recvmsg6
	   systemd.resource-control(5)

       regular-file
	   sysupdate.d(5)

       reloading
	   systemctl(1)

       restart
	   systemd.service(5)

       return
	   sd_bus_error(3)

       riscv32
	   repart.d(5)

       riscv64
	   repart.d(5)

       root
	   repart.d(5), systemd.exec(5), sysupdate.d(5)

       root-riscv64
	   repart.d(5)

       root-secondary
	   repart.d(5)

       root-secondary-verity
	   repart.d(5)

       root-secondary-verity-sig
	   repart.d(5)

       root-verity
	   repart.d(5)

       root-verity-sig
	   repart.d(5)

       root-x86-64
	   repart.d(5)

       root-{arch}
	   repart.d(5)

       root-{arch}-verity
	   repart.d(5)

       root-{arch}-verity-sig
	   repart.d(5)

       runtime
	   systemctl(1)

       rw
	   systemd.exec(5), systemd.service(5)

       rwm
	   systemd.exec(5)

       rwxrwxrwx
	   systemd-mount(1)

       s
	   systemd.net-naming-scheme(7), tmpfiles.d(5)

       s390
	   repart.d(5), systemd.exec(5)

       s390x
	   repart.d(5), systemd.exec(5)

       sch_teql
	   systemd.network(5)

       sendmsg4
	   systemd.resource-control(5)

       sendmsg6
	   systemd.resource-control(5)

       setsockopt
	   systemd.resource-control(5)

       shared-anonymous
	   systemd.exec(5)

       shared-dax
	   systemd.exec(5)

       shared-file-backed
	   systemd.exec(5)

       shared-huge
	   systemd.exec(5)

       simple
	   systemd-run(1)

       sl
	   systemd.net-naming-scheme(7)

       sock_create
	   systemd.resource-control(5)

       sock_ops
	   systemd.resource-control(5)

       srv
	   repart.d(5), systemd.exec(5)

       state
	   systemctl(1)

       stdio
	   sd_bus_message_dump(3)

       stop
	   systemd.scope(5), systemd.service(5)

       subvolume
	   sysupdate.d(5)

       swap
	   repart.d(5)

       symlink
	   udevadm(8)

       sysctl
	   systemd.resource-control(5)

       sysinit
	   ukify(1)

       syslog
	   systemctl(1)

       tar
	   sysupdate.d(5)

       tcp
	   resolvectl(1), systemd.resource-control(5)

       text/event-stream
	   systemd-journal-gatewayd.service(8)

       text/plain
	   systemd-journal-gatewayd.service(8)

       tilegx
	   repart.d(5)

       tmp
	   repart.d(5), systemd.exec(5)

       tmpfs
	   systemd-mount(1), systemd.exec(5)

       true
	   sd_bus_add_object(3), systemd-oomd.service(8)

       u
	   systemd.net-naming-scheme(7)

       udev_hwdb
	   libudev(3)

       udev_queue
	   libudev(3)

       udp
	   systemd.resource-control(5)

       url-file
	   sysupdate.d(5)

       url-tar
	   sysupdate.d(5)

       us
	   tmpfiles.d(5)

       user
	   systemd.exec(5)

       usr
	   repart.d(5), systemd.exec(5)

       usr-secondary
	   repart.d(5)

       usr-secondary-verity
	   repart.d(5)

       usr-secondary-verity-sig
	   repart.d(5)

       usr-verity
	   repart.d(5)

       usr-verity-sig
	   repart.d(5)

       usr-x86-64
	   repart.d(5)

       usr-{arch}
	   repart.d(5)

       usr-{arch}-verity
	   repart.d(5)

       usr-{arch}-verity-sig
	   repart.d(5)

       uts
	   systemd.exec(5)

       v
	   systemd.net-naming-scheme(7)

       v238
	   systemd.net-naming-scheme(7)

       v239
	   systemd.net-naming-scheme(7)

       v240
	   systemd.net-naming-scheme(7)

       v241
	   systemd.net-naming-scheme(7)

       v243
	   systemd.net-naming-scheme(7)

       v245
	   systemd.net-naming-scheme(7)

       v247
	   systemd.net-naming-scheme(7)

       v249
	   systemd.net-naming-scheme(7)

       v250
	   systemd.net-naming-scheme(7)

       v251
	   systemd.net-naming-scheme(7)

       v252
	   systemd.net-naming-scheme(7)

       v253
	   systemd.net-naming-scheme(7)

       v254
	   systemd.net-naming-scheme(7)

       v255
	   systemd.net-naming-scheme(7)

       var
	   repart.d(5), systemd.exec(5)

       w
	   systemd.resource-control(5), tmpfiles.d(5)

       warning
	   homectl(1), journalctl(1), localectl(1), loginctl(1), machinectl(1), portablectl(1), systemctl(1), systemd(1), systemd-analyze(1), systemd-
	   inhibit(1), systemd-nspawn(1), systemd-tmpfiles(8), timedatectl(1), userdbctl(1)

       wl
	   systemd.net-naming-scheme(7)

       ww
	   systemd.net-naming-scheme(7)

       x
	   systemd.net-naming-scheme(7)

       x32
	   systemd.exec(5)

       x86
	   repart.d(5), systemd-system.conf(5), systemd.dnssd(5), systemd.exec(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       x86-64
	   repart.d(5), systemd-system.conf(5), systemd.dnssd(5), systemd.exec(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       xbootldr
	   repart.d(5), systemd.exec(5), sysupdate.d(5)

       yes
	   systemd.resource-control(5), systemd.service(5)

DNS RESOURCE RECORD TYPES
       A
	   resolvectl(1)

       AAAA
	   resolvectl(1)

       CNAME
	   resolvectl(1)

       DNAME
	   resolvectl(1)

       DNSKEY
	   dnssec-trust-anchors.d(5)

       DS
	   dnssec-trust-anchors.d(5)

       MX
	   resolvectl(1)

       OPENPGP
	   resolvectl(1)

       OPENPGPKEY
	   resolvectl(1)

       PTR
	   resolvectl(1)

       SRV
	   org.freedesktop.resolve1(5), resolvectl(1), systemd.dnssd(5)

       TLSA
	   resolvectl(1)

       TXT
	   org.freedesktop.resolve1(5), resolvectl(1)

MISCELLANEOUS OPTIONS AND DIRECTIVES
       Other configuration elements which don't fit in any of the above groups.

       $LISTEN_FDS
	   systemd-journal-remote.service(8)

       A
	   tmpfiles.d(5)

       A+
	   tmpfiles.d(5)

       C
	   tmpfiles.d(5)

       C+
	   tmpfiles.d(5)

       Cmdline=
	   ukify(1)

       CopyBlocks=
	   repart.d(5)

       CopyFiles=
	   repart.d(5)

       CurrentSymlink=
	   sysupdate.d(5)

       D
	   tmpfiles.d(5)

       DeviceTree=
	   ukify(1)

       Encrypt=
	   repart.d(5)

       ExcludeFiles=
	   repart.d(5)

       ExcludeFilesTarget=
	   repart.d(5)

       FactoryReset=
	   repart.d(5)

       Flags=
	   repart.d(5)

       Format=
	   repart.d(5)

       GrowFileSystem=
	   repart.d(5)

       H
	   tmpfiles.d(5)

       ID_NET_LABEL_ONBOARD=
	   systemd.net-naming-scheme(7)

       ID_NET_NAME_MAC=
	   systemd.net-naming-scheme(7)

       ID_NET_NAME_ONBOARD=
	   systemd.net-naming-scheme(7)

       ID_NET_NAME_PATH=
	   systemd.net-naming-scheme(7)

       ID_NET_NAME_SLOT=
	   systemd.net-naming-scheme(7)

       Initrd=
	   ukify(1)

       InstancesMax=
	   sysupdate.d(5)

       L
	   tmpfiles.d(5)

       L+
	   tmpfiles.d(5)

       Label=
	   repart.d(5)

       Linux=
	   ukify(1)

       MakeDirectories=
	   repart.d(5)

       MatchPartitionType=
	   sysupdate.d(5)

       MatchPattern=
	   sysupdate.d(5)

       MinVersion=
	   sysupdate.d(5)

       Minimize=
	   repart.d(5)

       Mode=
	   sysupdate.d(5)

       NoAuto=
	   repart.d(5)

       OSRelease=
	   ukify(1)

       PCRBanks=
	   ukify(1)

       PCRPKey=
	   ukify(1)

       PCRPrivateKey=
	   ukify(1)

       PCRPublicKey=
	   ukify(1)

       PaddingMaxBytes=
	   repart.d(5)

       PaddingMinBytes=
	   repart.d(5)

       PaddingWeight=
	   repart.d(5)

       PartitionFlags=
	   sysupdate.d(5)

       PartitionGrowFileSystem=
	   sysupdate.d(5)

       PartitionNoAuto=
	   sysupdate.d(5)

       PartitionUUID=
	   sysupdate.d(5)

       Path=
	   sysupdate.d(5)

       PathRelativeTo=
	   sysupdate.d(5)

       Phases=
	   ukify(1)

       Priority=
	   repart.d(5)

       ProtectVersion=
	   sysupdate.d(5)

       Q
	   tmpfiles.d(5)

       R
	   tmpfiles.d(5)

       ReadOnly=
	   repart.d(5), sysupdate.d(5)

       RemoveTemporary=
	   sysupdate.d(5)

       SBAT=
	   ukify(1)

       SecureBootCertificate=
	   ukify(1)

       SecureBootCertificateDir=
	   ukify(1)

       SecureBootCertificateName=
	   ukify(1)

       SecureBootCertificateValidity=
	   ukify(1)

       SecureBootPrivateKey=
	   ukify(1)

       SecureBootSigningTool=
	   ukify(1)

       SignKernel=
	   ukify(1)

       SigningEngine=
	   ukify(1)

       SizeMaxBytes=
	   repart.d(5)

       SizeMinBytes=
	   repart.d(5)

       Splash=
	   ukify(1)

       SplitName=
	   repart.d(5)

       Subvolumes=
	   repart.d(5)

       T
	   tmpfiles.d(5)

       TriesDone=
	   sysupdate.d(5)

       TriesLeft=
	   sysupdate.d(5)

       Type=
	   repart.d(5), sysupdate.d(5)

       UUID=
	   repart.d(5)

       Uname=
	   ukify(1)

       Verify=
	   sysupdate.d(5)

       Verity=
	   repart.d(5)

       VerityDataBlockSizeBytes=
	   repart.d(5)

       VerityHashBlockSizeBytes=
	   repart.d(5)

       VerityMatchKey=
	   repart.d(5)

       Weight=
	   repart.d(5)

       X
	   tmpfiles.d(5)

       Z
	   tmpfiles.d(5)

       a
	   tmpfiles.d(5)

       a+
	   tmpfiles.d(5)

       b
	   tmpfiles.d(5)

       b+
	   tmpfiles.d(5)

       c
	   tmpfiles.d(5)

       c+
	   tmpfiles.d(5)

       d
	   tmpfiles.d(5)

       e
	   tmpfiles.d(5)

       equivalent
	   systemd-delta(1)

       extended
	   systemd-delta(1)

       f
	   tmpfiles.d(5)

       f+
	   tmpfiles.d(5)

       g
	   sysusers.d(5)

       h
	   tmpfiles.d(5)

       io.systemd.stub.kernel-cmdline-extra
	   systemd-stub(7)

       m
	   sysusers.d(5)

       masked
	   systemd-delta(1)

       overridden
	   systemd-delta(1)

       p
	   tmpfiles.d(5)

       p+
	   tmpfiles.d(5)

       q
	   tmpfiles.d(5)

       r
	   sysusers.d(5), tmpfiles.d(5)

       redirected
	   systemd-delta(1)

       t
	   tmpfiles.d(5)

       u
	   sysusers.d(5)

       unchanged
	   systemd-delta(1)

       user.coredump.comm
	   systemd-coredump(8)

       user.coredump.exe
	   systemd-coredump(8)

       user.coredump.gid
	   systemd-coredump(8)

       user.coredump.hostname
	   systemd-coredump(8)

       user.coredump.pid
	   systemd-coredump(8)

       user.coredump.rlimit
	   systemd-coredump(8)

       user.coredump.signal
	   systemd-coredump(8)

       user.coredump.timestamp
	   systemd-coredump(8)

       user.coredump.uid
	   systemd-coredump(8)

       v
	   tmpfiles.d(5)

       w
	   tmpfiles.d(5)

       w+
	   tmpfiles.d(5)

       x
	   tmpfiles.d(5)

       z
	   tmpfiles.d(5)

SPECIFIERS
       Short strings which are substituted in configuration directives.

       "%%"
	   repart.d(5), systemd-system.conf(5), systemd.automount(5), systemd.dnssd(5), systemd.mount(5), systemd.swap(5), systemd.unit(5), sysupdate.d(5),
	   sysusers.d(5), tmpfiles.d(5)

       "%A"
	   repart.d(5), systemd-system.conf(5), systemd.dnssd(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       "%B"
	   repart.d(5), systemd-system.conf(5), systemd.dnssd(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       "%C"
	   systemd.unit(5), tmpfiles.d(5)

       "%E"
	   systemd.unit(5)

       "%G"
	   systemd-system.conf(5), systemd.unit(5), tmpfiles.d(5)

       "%H"
	   repart.d(5), systemd-system.conf(5), systemd.dnssd(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       "%I"
	   systemd.unit(5)

       "%J"
	   systemd.unit(5)

       "%L"
	   systemd.unit(5), tmpfiles.d(5)

       "%M"
	   repart.d(5), systemd-system.conf(5), systemd.dnssd(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       "%N"
	   systemd.unit(5)

       "%P"
	   systemd.unit(5)

       "%S"
	   systemd.unit(5), tmpfiles.d(5)

       "%T"
	   repart.d(5), systemd-system.conf(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       "%U"
	   repart.d(5), systemd-system.conf(5), systemd.unit(5), tmpfiles.d(5)

       "%V"
	   repart.d(5), systemd-system.conf(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       "%W"
	   repart.d(5), systemd-system.conf(5), systemd.dnssd(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       "%Y"
	   systemd.unit(5)

       "%a"
	   repart.d(5), systemd-system.conf(5), systemd.dnssd(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       "%b"
	   repart.d(5), systemd-system.conf(5), systemd.dnssd(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       "%d"
	   systemd.unit(5)

       "%f"
	   systemd.unit(5)

       "%g"
	   systemd-system.conf(5), systemd.unit(5), tmpfiles.d(5)

       "%h"
	   systemd-system.conf(5), systemd.unit(5), tmpfiles.d(5)

       "%i"
	   systemd.unit(5)

       "%j"
	   systemd.unit(5)

       "%l"
	   repart.d(5), systemd-system.conf(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       "%m"
	   repart.d(5), systemd-system.conf(5), systemd.dnssd(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       "%n"
	   repart.d(5), systemd.unit(5)

       "%o"
	   repart.d(5), systemd-system.conf(5), systemd.dnssd(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       "%p"
	   systemd.unit(5)

       "%q"
	   systemd.unit(5)

       "%s"
	   systemd-system.conf(5), systemd.unit(5)

       "%t"
	   repart.d(5), systemd.unit(5), tmpfiles.d(5)

       "%u"
	   systemd-system.conf(5), systemd.unit(5), tmpfiles.d(5)

       "%v"
	   repart.d(5), systemd-system.conf(5), systemd.dnssd(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       "%w"
	   repart.d(5), systemd-system.conf(5), systemd.dnssd(5), systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       "%y"
	   systemd.unit(5)

FILES AND DIRECTORIES
       Paths and file names referred to in the documentation.

       /
	   file-hierarchy(7), repart.d(5), systemd-gpt-auto-generator(8), systemd-nspawn(1), systemd-remount-fs.service(8), systemd-repart(8), systemd-
	   stub(7), systemd.nspawn(5), systemd.special(7), systemd.unit(5), tmpfiles.d(5)

       $XDG_CONFIG_DIRS/systemd/user/
	   systemd.unit(5)

       $XDG_DATA_DIRS/systemd/user/
	   systemd.unit(5)

       $XDG_DATA_HOME/systemd/user/
	   systemd.unit(5)

       $XDG_RUNTIME_DIR/systemd/generator/
	   systemd.unit(5)

       $XDG_RUNTIME_DIR/systemd/generator.early/
	   systemd.unit(5)

       $XDG_RUNTIME_DIR/systemd/generator.late/
	   systemd.unit(5)

       $XDG_RUNTIME_DIR/systemd/transient/
	   systemd.unit(5)

       $XDG_RUNTIME_DIR/systemd/user/
	   systemd.unit(5)

       $XDG_RUNTIME_DIR/systemd/user.control/
	   systemd.unit(5)

       $XDG_RUNTIME_DIR/user-tmpfiles.d/*.conf
	   tmpfiles.d(5)

       -.mount
	   systemd.special(7)

       -.slice
	   systemd.special(7)

       /.extra/credentials/
	   systemd-stub(7)

       /.extra/credentials/*.cred
	   systemd-stub(7)

       /.extra/global_credentials/
	   systemd-stub(7)

       /.extra/global_credentials/*.cred
	   systemd-stub(7)

       /.extra/sysext/
	   systemd-stub(7), systemd-sysext(8)

       /.extra/sysext/*.raw
	   systemd-stub(7)

       /.extra/tpm2-pcr-pkey.pem
	   systemd-stub(7)

       /.extra/tpm2-pcr-public-key.pem
	   systemd-stub(7)

       /.extra/tpm2-pcr-signature.json
	   systemd-stub(7)

       /EFI/Linux/
	   systemd-boot(7)

       /EFI/systemd/drivers/
	   systemd-boot(7)

       /SHA256SUMS
	   sysupdate.d(5)

       /SHA256SUMS.gpg
	   sysupdate.d(5)

       /bin/
	   file-hierarchy(7), org.freedesktop.systemd1(5), systemd-nspawn(1), systemd.service(5)

       /bin/bash
	   homectl(1)

       /bin/echo
	   systemd.service(5)

       /bin/ls
	   systemd-cat(1)

       /bin/sh
	   machinectl(1), sysusers.d(5)

       /boot/
	   bootctl(1), file-hierarchy(7), kernel-install(8), systemd-boot(7), systemd-gpt-auto-generator(8), systemd-nspawn(1), systemd.exec(5)

       /boot/efi/
	   bootctl(1), kernel-install(8), systemd-boot(7)

       /dev/
	   file-hierarchy(7), kernel-command-line(7), systemd-debug-generator(8), systemd-nspawn(1), systemd-remount-fs.service(8), systemd.device(5),
	   systemd.exec(5), systemd.generator(7), systemd.journal-fields(7), systemd.resource-control(5), udev(7), udevadm(8)

       /dev/block/
	   systemd.resource-control(5)

       /dev/block/$major:$minor
	   systemd-gpt-auto-generator(8)

       /dev/char/
	   systemd.resource-control(5)

       /dev/console
	   journald.conf(5), systemd-getty-generator(8), systemd-nspawn(1), systemd-tty-ask-password-agent(1), systemd.exec(5)

       /dev/disk/by-label/...
	   systemd-fstab-generator(8)

       /dev/disk/by-loop-ref/...
	   systemd-dissect(1)

       /dev/disk/by-uuid/...
	   systemd-fstab-generator(8)

       /dev/full
	   systemd.resource-control(5)

       /dev/hidraw1
	   crypttab(5), homectl(1), systemd-cryptenroll(1)

       /dev/initctl
	   systemd(1), systemd-initctl.service(8)

       /dev/kmsg
	   journald.conf(5), systemd-journald.service(8), systemd.exec(5), systemd.generator(7)

       /dev/log
	   systemctl(1), systemd-journald.service(8)

       /dev/loop-control
	   systemd.exec(5)

       /dev/mapper/
	   crypttab(5), integritytab(5), veritytab(5)

       /dev/mapper/home
	   systemd-gpt-auto-generator(8)

       /dev/mapper/root
	   systemd-fstab-generator(8), systemd-gpt-auto-generator(8)

       /dev/mapper/srv
	   systemd-gpt-auto-generator(8)

       /dev/mapper/swap
	   systemd-gpt-auto-generator(8)

       /dev/mapper/tmp
	   systemd-gpt-auto-generator(8)

       /dev/mapper/usr
	   systemd-fstab-generator(8)

       /dev/mapper/var
	   systemd-gpt-auto-generator(8)

       /dev/mem
	   systemd.exec(5)

       /dev/net/tun
	   systemd.netdev(5)

       /dev/null
	   binfmt.d(5), coredump.conf(5), daemon(7), dnssec-trust-anchors.d(5), environment.d(5), homed.conf(5), hwdb(7), iocost.conf(5), journal-
	   remote.conf(5), journal-upload.conf(5), journald.conf(5), kernel-install(8), logind.conf(5), modules-load.d(5), networkd.conf(5), oomd.conf(5),
	   org.freedesktop.systemd1(5), pstore.conf(5), resolved.conf(5), sd_event_add_memory_pressure(3), sysctl.d(5), systemctl(1), systemd-sleep.conf(5),
	   systemd-system.conf(5), systemd.environment-generator(7), systemd.exec(5), systemd.generator(7), systemd.link(5), systemd.netdev(5),
	   systemd.network(5), systemd.preset(5), systemd.resource-control(5), systemd.unit(5), sysusers.d(5), timesyncd.conf(5), tmpfiles.d(5), udev(7)

       /dev/nvme0n1
	   bootctl(1)

       /dev/nvme0n1p5
	   bootctl(1)

       /dev/port
	   systemd.exec(5)

       /dev/random
	   systemd.exec(5), systemd.resource-control(5)

       /dev/rtc0
	   systemd.exec(5)

       /dev/rtc1
	   systemd.exec(5)

       /dev/sda
	   systemd.exec(5)

       /dev/sda5
	   systemd.resource-control(5)

       /dev/shm/
	   file-hierarchy(7), systemd.exec(5)

       /dev/tpmrm0
	   crypttab(5), systemd-creds(1), systemd-cryptenroll(1), systemd-measure(1), systemd-pcrphase.service(8), systemd.exec(5)

       /dev/tty7
	   sd_device_get_syspath(3)

       /dev/tty9
	   systemd-debug-generator(8)

       /dev/urandom
	   crypttab(5), systemd-random-seed.service(8), systemd.resource-control(5)

       /dev/watchdog0
	   systemd-system.conf(5)

       /dev/zero
	   systemd.exec(5), systemd.resource-control(5)

       /devices/virtual/tty/tty7
	   sd_device_get_syspath(3)

       /efi/
	   bootctl(1), file-hierarchy(7), kernel-install(8), systemd-boot(7), systemd-gpt-auto-generator(8), systemd-nspawn(1), systemd.exec(5)

       /etc/
	   binfmt.d(5), coredump.conf(5), environment.d(5), file-hierarchy(7), homed.conf(5), hwdb(7), iocost.conf(5), journal-remote.conf(5), journal-
	   upload.conf(5), journald.conf(5), kernel-command-line(7), logind.conf(5), machine-id(5), machinectl(1), modules-load.d(5), networkctl(1),
	   networkd.conf(5), nss-myhostname(8), oomd.conf(5), org.freedesktop.systemd1(5), os-release(5), portablectl(1), pstore.conf(5), resolved.conf(5),
	   sysctl.d(5), systemctl(1), systemd-delta(1), systemd-firstboot(1), systemd-fstab-generator(8), systemd-machine-id-commit.service(8), systemd-
	   machine-id-setup(1), systemd-modules-load.service(8), systemd-nspawn(1), systemd-sleep.conf(5), systemd-sysext(8), systemd-system.conf(5), systemd-
	   sysusers(8), systemd-timedated.service(8), systemd-update-done.service(8), systemd-volatile-root.service(8), systemd.dnssd(5), systemd.environment-
	   generator(7), systemd.exec(5), systemd.generator(7), systemd.link(5), systemd.mount(5), systemd.netdev(5), systemd.network(5), systemd.preset(5),
	   systemd.unit(5), timesyncd.conf(5), tmpfiles.d(5), udev(7)

       /etc/.updated
	   systemd-update-done.service(8)

       /etc/adjtime
	   timedatectl(1)

       /etc/binfmt.d/*.conf
	   binfmt.d(5)

       /etc/credstore/
	   systemd.exec(5)

       /etc/credstore.encrypted/
	   systemd.exec(5)

       /etc/cryptsetup-keys.d/
	   crypttab(5), systemd-cryptsetup(8)

       /etc/crypttab
	   crypttab(5), systemd-cryptenroll(1), systemd-cryptsetup(8), systemd-cryptsetup-generator(8), systemd-gpt-auto-generator(8), systemd-system.conf(5)

       /etc/dnssec-trust-anchors.d/
	   dnssec-trust-anchors.d(5)

       /etc/dnssec-trust-anchors.d/*.negative
	   dnssec-trust-anchors.d(5)

       /etc/dnssec-trust-anchors.d/*.positive
	   dnssec-trust-anchors.d(5)

       /etc/environment
	   environment.d(5)

       /etc/environment.d/*.conf
	   environment.d(5)

       /etc/extension-release.d/extension-release.IMAGE
	   os-release(5), systemd-sysext(8)

       /etc/extension-release.d/extension-release.IMAGE
	   systemd.exec(5)

       /etc/extensions/
	   systemd-sysext(8)

       /etc/fstab
	   crypttab(5), kernel-command-line(7), org.freedesktop.systemd1(5), systemd(1), systemd-dissect(1), systemd-fsck@.service(8), systemd-fstab-
	   generator(8), systemd-gpt-auto-generator(8), systemd-mount(1), systemd-pcrphase.service(8), systemd-remount-fs.service(8), systemd-system.conf(5),
	   systemd.automount(5), systemd.generator(7), systemd.mount(5), systemd.special(7), systemd.swap(5)

       /etc/group
	   nss-systemd(8), systemd-nspawn(1), systemd-tmpfiles(8), systemd.exec(5), sysusers.d(5), userdbctl(1)

       /etc/gshadow
	   nss-systemd(8)

       /etc/hostname
	   hostname(5), kernel-command-line(7), machine-info(5), org.freedesktop.hostname1(5), systemd-hostnamed.service(8)

       /etc/hosts
	   nss-myhostname(8), nss-resolve(8), org.freedesktop.hostname1(5), org.freedesktop.resolve1(5), resolvectl(1), resolved.conf(5), systemd-
	   resolved.service(8), systemd.system-credentials(7)

       /etc/init.d/
	   systemd-sysv-generator(8)

       /etc/initrd-release
	   bootup(7), os-release(5)

       /etc/integritytab
	   integritytab(5), systemd-integritysetup-generator(8)

       /etc/issue.d/50-provision.conf
	   systemd.system-credentials(7)

       /etc/kernel/
	   ukify(1)

       /etc/kernel/cmdline
	   kernel-install(8), systemd-firstboot(1)

       /etc/kernel/devicetree
	   kernel-install(8)

       /etc/kernel/entry-token
	   bootctl(1), kernel-install(8)

       /etc/kernel/install.conf
	   kernel-install(8)

       /etc/kernel/install.d/
	   kernel-install(8)

       /etc/kernel/install.d/*.install
	   kernel-install(8)

       /etc/kernel/tries
	   kernel-install(8), systemd-boot(7)

       /etc/kernel/uki.conf
	   kernel-install(8), ukify(1)

       /etc/locale.conf
	   locale.conf(5), localectl(1), systemd(1)

       /etc/localtime
	   localtime(5), systemd-nspawn(1), systemd.network(5), systemd.nspawn(5), timedatectl(1)

       /etc/machine-id
	   kernel-install(8), machine-id(5), org.freedesktop.machine1(5), sd_bus_get_name_machine_id(3), sd_id128_get_machine(3), systemd(1), systemd-machine-
	   id-commit.service(8), systemd-machine-id-setup(1), systemd-nspawn(1), systemd-pcrlock(8), systemd.pcrlock(5), systemd.unit(5)

       /etc/machine-info
	   machine-info(5), org.freedesktop.hostname1(5), systemd-hostnamed.service(8), systemd.unit(5)

       /etc/modules-load.d/program.conf
	   modules-load.d(5)

       /etc/modules-load.d/*.conf
	   modules-load.d(5)

       /etc/modules-load.d/bridge.conf
	   sysctl.d(5)

       /etc/motd
	   systemd-repart(8)

       /etc/motd.d/50-provision.conf
	   systemd.system-credentials(7)

       /etc/nsswitch.conf
	   nss-myhostname(8), nss-mymachines(8), nss-resolve(8), nss-systemd(8)

       /etc/os-release
	   kernel-install(8), os-release(5), repart.d(5), systemd-nspawn(1), systemd-system.conf(5), systemd-sysupdate(8), systemd.dnssd(5), systemd.unit(5),
	   sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       /etc/pam.d/
	   pam_systemd_loadkey(8)

       /etc/passwd
	   homectl(1), nss-systemd(8), systemd-firstboot(1), systemd-nspawn(1), systemd-tmpfiles(8), systemd.exec(5), sysusers.d(5), userdbctl(1)

       /etc/pcrlock.d/
	   systemd-pcrlock(8)

       /etc/pcrlock.d/*.pcrlock
	   systemd.pcrlock(5)

       /etc/pcrlock.d/*.pcrlock.d/*.pcrlock
	   systemd.pcrlock(5)

       /etc/pki/pesign
	   ukify(1)

       /etc/portables/
	   portablectl(1)

       /etc/rc.local
	   systemd-rc-local-generator(8)

       /etc/repart.d/*.conf
	   repart.d(5), systemd-repart(8)

       /etc/resolv.conf
	   org.freedesktop.resolve1(5), resolvectl(1), resolved.conf(5), systemd-nspawn(1), systemd-resolved.service(8), systemd.network(5), systemd.nspawn(5)

       /etc/shadow
	   nss-systemd(8), systemd-firstboot(1)

       /etc/skel/
	   homectl(1)

       /etc/ssl/ca/trusted.pem
	   systemd-journal-remote.service(8), systemd-journal-upload.service(8)

       /etc/ssl/certs/journal-remote.pem
	   systemd-journal-remote.service(8)

       /etc/ssl/certs/journal-upload.pem
	   systemd-journal-upload.service(8)

       /etc/ssl/private/journal-remote.pem
	   systemd-journal-remote.service(8)

       /etc/ssl/private/journal-upload.pem
	   systemd-journal-upload.service(8)

       /etc/sysctl.d/
	   systemd-soft-reboot.service(8)

       /etc/sysctl.d/*.conf
	   sysctl.d(5)

       /etc/sysctl.d/20-rp_filter.conf
	   sysctl.d(5)

       /etc/sysctl.d/50-coredump.conf
	   systemd-sysctl.service(8)

       /etc/sysctl.d/bridge.conf
	   sysctl.d(5)

       /etc/sysctl.d/domain-name.conf
	   sysctl.d(5)

       /etc/system-update
	   systemd-system-update-generator(8), systemd.offline-updates(7), systemd.special(7)

       /etc/systemd/
	   coredump.conf(5), crypttab(5), homed.conf(5), iocost.conf(5), journal-remote.conf(5), journal-upload.conf(5), journald.conf(5), logind.conf(5),
	   networkd.conf(5), oomd.conf(5), pstore.conf(5), resolved.conf(5), systemd-creds(1), systemd-cryptenroll(1), systemd-sleep.conf(5), systemd-
	   system.conf(5), timesyncd.conf(5)

       /etc/systemd/*.conf.d/
	   coredump.conf(5), homed.conf(5), iocost.conf(5), journal-remote.conf(5), journal-upload.conf(5), journald.conf(5), logind.conf(5),
	   networkd.conf(5), oomd.conf(5), pstore.conf(5), resolved.conf(5), systemd-sleep.conf(5), systemd-system.conf(5), timesyncd.conf(5)

       /etc/systemd/coredump.conf
	   coredump.conf(5), systemd-coredump(8)

       /etc/systemd/coredump.conf.d/*.conf
	   coredump.conf(5), systemd-coredump(8)

       /etc/systemd/dnssd
	   systemd.dnssd(5)

       /etc/systemd/homed.conf
	   homed.conf(5)

       /etc/systemd/homed.conf.d/*.conf
	   homed.conf(5)

       /etc/systemd/import-pubring.gpg
	   machinectl(1), sysupdate.d(5)

       /etc/systemd/iocost.conf
	   iocost.conf(5)

       /etc/systemd/iocost.conf.d/*.conf
	   iocost.conf(5)

       /etc/systemd/journal-remote.conf
	   journal-remote.conf(5), systemd-journal-upload.service(8)

       /etc/systemd/journal-remote.conf.d/*.conf
	   journal-remote.conf(5)

       /etc/systemd/journal-upload.conf
	   journal-upload.conf(5), systemd-journal-upload.service(8)

       /etc/systemd/journal-upload.conf.d/*.conf
	   journal-upload.conf(5)

       /etc/systemd/journald.conf
	   journald.conf(5), systemd-journald.service(8)

       /etc/systemd/journald.conf.d/*.conf
	   journald.conf(5)

       /etc/systemd/journald@NAMESPACE.conf
	   journald.conf(5), systemd-journald.service(8)

       /etc/systemd/logind.conf
	   logind.conf(5), systemd-analyze(1)

       /etc/systemd/logind.conf.d/*.conf
	   logind.conf(5)

       /etc/systemd/network
	   systemd-networkd.service(8), systemd.link(5), systemd.netdev(5), systemd.network(5)

       /etc/systemd/network/*.network
	   systemd-resolved.service(8)

       /etc/systemd/networkd.conf
	   networkd.conf(5)

       /etc/systemd/networkd.conf.d/*.conf
	   networkd.conf(5)

       /etc/systemd/nspawn/
	   machinectl(1), systemd-nspawn(1), systemd.nspawn(5)

       /etc/systemd/oomd.conf
	   oomd.conf(5)

       /etc/systemd/oomd.conf.d/*.conf
	   oomd.conf(5)

       /etc/systemd/portable/profile/
	   portablectl(1)

       /etc/systemd/pstore.conf
	   pstore.conf(5), systemd-pstore.service(8)

       /etc/systemd/pstore.conf.d/
	   pstore.conf(5)

       /etc/systemd/pstore.conf.d/*.conf
	   systemd-pstore.service(8)

       /etc/systemd/resolved.conf
	   org.freedesktop.resolve1(5), resolvectl(1), resolved.conf(5), systemd-resolved.service(8)

       /etc/systemd/resolved.conf.d/*.conf
	   resolved.conf(5)

       /etc/systemd/sleep.conf
	   systemd-sleep.conf(5), systemd-suspend.service(8)

       /etc/systemd/sleep.conf.d/*.conf
	   systemd-sleep.conf(5)

       /etc/systemd/system/
	   systemctl(1), systemd.unit(5)

       /etc/systemd/system-environment-generators/
	   systemd.environment-generator(7)

       /etc/systemd/system-generators/
	   systemd.generator(7)

       /etc/systemd/system-preset/
	   systemd.preset(5)

       /etc/systemd/system-preset/*.preset
	   systemd.preset(5)

       /etc/systemd/system.attached
	   org.freedesktop.systemd1(5), portablectl(1), systemd.unit(5)

       /etc/systemd/system.conf
	   org.freedesktop.systemd1(5), systemd-system.conf(5)

       /etc/systemd/system.conf.d/*.conf
	   systemd-system.conf(5)

       /etc/systemd/system.control/
	   systemd.unit(5)

       /etc/systemd/system/ctrl-alt-del.service
	   systemd.unit(5)

       /etc/systemd/system/httpd.service
	   systemd.unit(5)

       /etc/systemd/system/httpd.service.d/local.conf
	   systemd.unit(5)

       /etc/systemd/system/systemd-nspawn@foobar.service.d/50-network.conf
	   systemd-nspawn(1)

       /etc/systemd/timesyncd.conf
	   timesyncd.conf(5)

       /etc/systemd/timesyncd.conf.d/*.conf
	   timesyncd.conf(5)

       /etc/systemd/ukify.conf
	   ukify(1)

       /etc/systemd/user/
	   systemd.unit(5)

       /etc/systemd/user-environment-generators/
	   systemd.environment-generator(7)

       /etc/systemd/user-generators/
	   systemd.generator(7)

       /etc/systemd/user-preset/*.preset
	   systemd.preset(5)

       /etc/systemd/user.conf
	   systemd-system.conf(5)

       /etc/systemd/user.conf.d/*.conf
	   systemd-system.conf(5)

       /etc/sysupdate.component.d/*.conf
	   systemd-sysupdate(8)

       /etc/sysupdate.*.d/
	   systemd-sysupdate(8)

       /etc/sysupdate.d/*.conf
	   systemd-sysupdate(8), sysupdate.d(5)

       /etc/sysusers.d
	   sysusers.d(5)

       /etc/sysusers.d/*.conf
	   sysusers.d(5)

       /etc/sysusers.d/00-overrides.conf
	   systemd-sysusers(8)

       /etc/sysusers.d/radvd.conf
	   systemd-sysusers(8)

       /etc/tmpfiles.d
	   tmpfiles.d(5)

       /etc/tmpfiles.d/*.conf
	   tmpfiles.d(5)

       /etc/udev/hwdb.bin
	   hwdb(7)

       /etc/udev/hwdb.d
	   hwdb(7)

       /etc/udev/rules.d
	   udev(7)

       /etc/udev/rules.d/99-bridge.rules
	   sysctl.d(5)

       /etc/udev/udev.conf
	   udev.conf(5)

       /etc/userdb/
	   nss-systemd(8), systemd-userdbd.service(8), userdbctl(1)

       /etc/vconsole.conf
	   localectl(1), systemd-firstboot(1)

       /etc/veritytab
	   veritytab(5)

       /etc/xdg
	   systemd.unit(5)

       /etc/xdg/systemd/user
	   systemd.unit(5)

       /etc/xdg/user-dirs.conf
	   sd_path_lookup(3)

       /home/
	   file-hierarchy(7), homectl(1), homed.conf(5), repart.d(5), systemctl(1), systemd-gpt-auto-generator(8), systemd-repart(8), systemd.exec(5),
	   systemd.generator(7), systemd.image-policy(7), systemd.unit(5), tmpfiles.d(5)

       /home/$USER
	   homectl(1)

       /home/$USER.home
	   homectl(1)

       /home/$USER.homedir
	   homectl(1)

       /home/*.home
	   homectl(1)

       /home/*.homedir
	   homectl(1)

       /home/lennart
	   systemd.automount(5)

       /lib/
	   file-hierarchy(7), org.freedesktop.systemd1(5), systemd-nspawn(1)

       /lib64/
	   file-hierarchy(7)

       /loader/addons/*.addon.efi
	   systemd-stub(7)

       /loader/credentials/
	   systemd-stub(7)

       /loader/credentials/*.cred
	   systemd-stub(7)

       /loader/entries/
	   systemd-boot(7)

       /loader/keys/NAME
	   loader.conf(5), systemd-boot(7)

       /loader/loader.conf
	   systemd-boot(7)

       /loader/random-seed
	   systemd-boot(7)

       /log/
	   systemd.exec(5)

       /mysql-password
	   systemd-creds(1)

       /opt/
	   systemd-sysext(8), systemd.exec(5), systemd.image-policy(7)

       /org/freedesktop/LogControl1
	   org.freedesktop.LogControl1(5)

       /proc/
	   busctl(1), file-hierarchy(7), sd-login(3), sd_bus_creds_get_pid(3), sd_bus_creds_new_from_pid(3), sd_event_add_inotify(3), sd_id128_get_machine(3),
	   sd_is_fifo(3), sd_pid_get_owner_uid(3), systemctl(1), systemd(1), systemd-coredump(8), systemd-remount-fs.service(8), systemd.exec(5),
	   systemd.generator(7), systemd.socket(5), tmpfiles.d(5)

       /proc/$PID/ns/ipc
	   systemd.exec(5)

       /proc/$PID/ns/net
	   systemd-nspawn(1), systemd.exec(5)

       /proc/1/cmdline
	   systemd.unit(5)

       /proc/acpi
	   systemd.exec(5)

       /proc/cmdline
	   kernel-command-line(7), kernel-install(8), systemd(1), systemd-pcrlock(8), systemd.unit(5)

       /proc/crypto
	   homectl(1)

       /proc/devices
	   systemd.resource-control(5)

       /proc/fs
	   systemd.exec(5)

       /proc/irq
	   systemd.exec(5)

       /proc/kmsg
	   systemd.exec(5)

       /proc/latency_stats
	   systemd.exec(5)

       /proc/pressure/memory
	   sd_event_add_memory_pressure(3)

       /proc/self/cgroup
	   systemd-coredump(8)

       /proc/self/fd
	   daemon(7)

       /proc/self/mountinfo
	   systemd.mount(5)

       /proc/self/oom_score_adj
	   systemd-nspawn(1)

       /proc/self/sessionid
	   pam_systemd(8)

       /proc/sys/
	   file-hierarchy(7), systemd-nspawn(1), systemd-soft-reboot.service(8), systemd-sysctl.service(8), systemd.exec(5)

       /proc/sys/kernel/core_pattern
	   systemd-sysctl.service(8)

       /proc/sys/kernel/domainname
	   sysctl.d(5)

       /proc/sys/kernel/hostname
	   org.freedesktop.hostname1(5)

       /proc/sys/kernel/modules_disabled
	   systemd.exec(5)

       /proc/sys/kernel/random/boot_id
	   sd_id128_get_machine(3)

       /proc/sys/net/ipv4/conf/enp3s0.200/forwarding
	   sysctl.d(5)

       /proc/sys/net/ipv4/ip_default_ttl
	   systemd.netdev(5)

       /proc/sys/net/ipv4/tcp_keepalive_time
	   systemd.socket(5)

       /proc/sys/net/ipv6/bindv6only
	   systemd.socket(5)

       /proc/sysrq-trigger
	   systemd.exec(5)

       /proc/timer_stats
	   systemd.exec(5)

       /root/
	   file-hierarchy(7), systemd.exec(5)

       /root/.ssh/authorized_keys
	   systemd.system-credentials(7), tmpfiles.d(5)

       /run/
	   binfmt.d(5), crypttab(5), environment.d(5), file-hierarchy(7), modules-load.d(5), org.freedesktop.systemd1(5), sd-login(3), sd_notify(3),
	   sysctl.d(5), systemctl(1), systemd-delta(1), systemd-journald.service(8), systemd-modules-load.service(8), systemd-nspawn(1), systemd-
	   poweroff.service(8), systemd-soft-reboot.service(8), systemd-timedated.service(8), systemd.dnssd(5), systemd.environment-generator(7),
	   systemd.exec(5), systemd.generator(7), systemd.link(5), systemd.netdev(5), systemd.network(5), systemd.preset(5), systemd.service(5),
	   systemd.unit(5), tmpfiles.d(5), udev(7)

       /run/binfmt.d/*.conf
	   binfmt.d(5)

       /run/confexts/
	   systemd-sysext(8)

       /run/credentials/@initrd/
	   systemd(1)

       /run/credstore/
	   systemd.exec(5)

       /run/credstore.encrypted/
	   systemd.exec(5)

       /run/cryptsetup-keys.d/
	   crypttab(5), systemd-cryptsetup(8)

       /run/dnssec-trust-anchors.d/
	   dnssec-trust-anchors.d(5)

       /run/dnssec-trust-anchors.d/*.negative
	   dnssec-trust-anchors.d(5)

       /run/dnssec-trust-anchors.d/*.positive
	   dnssec-trust-anchors.d(5)

       /run/environment.d/*.conf
	   environment.d(5)

       /run/extensions/
	   systemd-sysext(8)

       /run/host/home/
	   systemd-nspawn(1)

       /run/host/incoming/
	   systemd.exec(5)

       /run/host/os-release
	   os-release(5), systemd.exec(5)

       /run/host/userdb/
	   nss-systemd(8), systemd-userdbd.service(8), userdbctl(1)

       /run/log/
	   file-hierarchy(7), sd_journal_get_seqnum(3)

       /run/log/journal/
	   journalctl(1), journald.conf(5), sd_journal_open(3), systemd-journald.service(8)

       /run/log/systemd/tpm2-measure.log
	   systemd-pcrlock(8), systemd-pcrphase.service(8)

       /run/media/system/
	   systemd-mount(1)

       /run/modules-load.d/*.conf
	   modules-load.d(5)

       /run/netns
	   systemd-nspawn(1)

       /run/nextroot/
	   org.freedesktop.systemd1(5), systemd-soft-reboot.service(8)

       /run/nologin
	   shutdown(8), systemd-user-sessions.service(8)

       /run/pcrlock.d/
	   systemd-pcrlock(8)

       /run/pcrlock.d/*.pcrlock
	   systemd.pcrlock(5)

       /run/pcrlock.d/*.pcrlock.d/*.pcrlock
	   systemd.pcrlock(5)

       /run/portables/
	   portablectl(1)

       /run/repart.d/*.conf
	   repart.d(5), systemd-repart(8)

       /run/screens
	   tmpfiles.d(5)

       /run/sysctl.d/*.conf
	   sysctl.d(5)

       /run/sysctl.d/50-coredump.conf
	   systemd-sysctl.service(8)

       /run/system/nspawn/
	   systemd.nspawn(5)

       /run/systemd/
	   crypttab(5), systemd-creds(1), systemd-cryptenroll(1)

       /run/systemd/coredump.conf.d/*.conf
	   coredump.conf(5)

       /run/systemd/dnssd
	   systemd.dnssd(5)

       /run/systemd/generator
	   systemd.generator(7), systemd.unit(5)

       /run/systemd/generator.early
	   systemd.generator(7), systemd.unit(5)

       /run/systemd/generator.late
	   systemd.generator(7), systemd.unit(5)

       /run/systemd/homed.conf.d/*.conf
	   homed.conf(5)

       /run/systemd/journal-remote.conf.d/*.conf
	   journal-remote.conf(5)

       /run/systemd/journal-upload.conf.d/*.conf
	   journal-upload.conf(5)

       /run/systemd/journal/dev-log
	   systemd-journald.service(8)

       /run/systemd/journal/socket
	   systemd-journald.service(8)

       /run/systemd/journal/stdout
	   systemd-journald.service(8)

       /run/systemd/journal/syslog
	   journald.conf(5)

       /run/systemd/journald.conf.d/*.conf
	   journald.conf(5)

       /run/systemd/journald@NAMESPACE.conf.d/*.conf
	   journald.conf(5)

       /run/systemd/logind.conf.d/*.conf
	   logind.conf(5)

       /run/systemd/network/
	   systemd-network-generator.service(8), systemd-networkd.service(8), systemd.link(5), systemd.netdev(5), systemd.network(5)

       /run/systemd/notify
	   systemd(1)

       /run/systemd/nspawn/
	   systemd-nspawn(1), systemd.nspawn(5)

       /run/systemd/portables/
	   portablectl(1)

       /run/systemd/private
	   systemd(1)

       /run/systemd/propagate/
	   systemd.exec(5)

       /run/systemd/resolve/io.systemd.Resolve
	   nss-resolve(8)

       /run/systemd/resolve/resolv.conf
	   org.freedesktop.resolve1(5), resolvectl(1), systemd-nspawn(1), systemd-resolved.service(8)

       /run/systemd/resolve/stub-resolv.conf
	   systemd-nspawn(1), systemd-resolved.service(8)

       /run/systemd/resolved.conf.d/*.conf
	   resolved.conf(5)

       /run/systemd/sleep.conf.d/*.conf
	   systemd-sleep.conf(5)

       /run/systemd/system/
	   sd_booted(3), systemctl(1), systemd.unit(5)

       /run/systemd/system-environment-generators/
	   systemd.environment-generator(7)

       /run/systemd/system-generators/
	   systemd.generator(7)

       /run/systemd/system-preset/*.preset
	   systemd.preset(5)

       /run/systemd/system.attached
	   org.freedesktop.systemd1(5), portablectl(1), systemd.unit(5)

       /run/systemd/system.conf.d/*.conf
	   systemd-system.conf(5)

       /run/systemd/system.control/
	   systemd.unit(5)

       /run/systemd/systemd/
	   systemctl(1)

       /run/systemd/timesync/synchronized
	   systemd-time-wait-sync.service(8), systemd-timesyncd.service(8)

       /run/systemd/timesyncd.conf.d/*.conf
	   timesyncd.conf(5)

       /run/systemd/tpm2-pcr-public-key.pem
	   systemd-stub(7)

       /run/systemd/tpm2-pcr-signature.json
	   systemd-stub(7)

       /run/systemd/tpm2-srk-public-key.
	   systemd-tpm2-setup.service(8)

       /run/systemd/tpm2-srk-public-key.pem
	   systemd-tpm2-setup.service(8)

       /run/systemd/tpm2-srk-public-key.tpm2_public
	   systemd-tpm2-setup.service(8)

       /run/systemd/tpm2-srk-public-key.tpm2b_public
	   systemd-cryptenroll(1), systemd-tpm2-setup.service(8)

       /run/systemd/transient/
	   systemd.unit(5)

       /run/systemd/ukify.conf
	   ukify(1)

       /run/systemd/user/
	   systemd.unit(5)

       /run/systemd/user-environment-generators/
	   systemd.environment-generator(7)

       /run/systemd/user-generators/
	   systemd.generator(7)

       /run/systemd/user-preset/*.preset
	   systemd.preset(5)

       /run/systemd/user.conf.d/*.conf
	   systemd-system.conf(5)

       /run/systemd/volatile-root
	   systemd-gpt-auto-generator(8)

       /run/sysupdate.component.d/*.conf
	   systemd-sysupdate(8)

       /run/sysupdate.*.d/
	   systemd-sysupdate(8)

       /run/sysupdate.d/*.conf
	   systemd-sysupdate(8), sysupdate.d(5)

       /run/sysusers.d
	   sysusers.d(5)

       /run/sysusers.d/*.conf
	   sysusers.d(5)

       /run/tmpfiles.d
	   tmpfiles.d(5)

       /run/tmpfiles.d/*.conf
	   tmpfiles.d(5)

       /run/udev/rules.d
	   udev(7)

       /run/udev/static_node-tags/tag
	   udev(7)

       /run/user/
	   file-hierarchy(7), systemd.exec(5), user@.service(5)

       /run/user/$UID
	   pam_systemd(8)

       /run/userdb/
	   nss-systemd(8), systemd-nspawn(1), systemd-userdbd.service(8), userdbctl(1)

       /run/utmp
	   runlevel(8)

       /sbin/
	   file-hierarchy(7), org.freedesktop.systemd1(5)

       /sbin/init
	   systemd(1)

       /sbin/mkfs.type
	   systemd-makefs@.service(8)

       /sbin/mkswap
	   systemd-makefs@.service(8)

       /sbin/mount.ddi
	   systemd-dissect(1)

       /srv/
	   file-hierarchy(7), repart.d(5), systemd-gpt-auto-generator(8), systemd-repart(8), systemd.image-policy(7)

       /srv/webserver
	   systemd.unit(5)

       /srv/www
	   systemd.unit(5)

       /sys/
	   file-hierarchy(7), loginctl(1), org.freedesktop.login1(5), sd_device_get_syspath(3), sd_is_fifo(3), systemd(1), systemd-nspawn(1), systemd-remount-
	   fs.service(8), systemd-soft-reboot.service(8), systemd-tmpfiles(8), systemd.device(5), systemd.exec(5), systemd.generator(7), systemd.journal-
	   fields(7), systemd.socket(5), tmpfiles.d(5), udev_device_new_from_syspath(3), udevadm(8)

       /sys/bus/pci/devices/0000:00:1f.6
	   sd_device_get_syspath(3)

       /sys/class/subsystem/name/max_brightness
	   org.freedesktop.login1(5)

       /sys/class/block/loopX/loop/backing_file
	   systemd-dissect(1)

       /sys/class/dmi/id/
	   systemd.unit(5)

       /sys/class/dmi/id/product_uuid
	   org.freedesktop.hostname1(5)

       /sys/class/watchdog/watchdogX/pretimeout_available_governors
	   systemd-system.conf(5)

       /sys/devices
	   udev_device_new_from_syspath(3)

       /sys/devices/virtual/tty/tty7
	   sd_device_get_syspath(3)

       /sys/firmware/dmi/entries/11-*/raw
	   smbios-type-11(7)

       /sys/fs/bpf/
	   systemd.resource-control(5)

       /sys/fs/cgroup/
	   file-hierarchy(7), sd-login(3), sd_pid_get_owner_uid(3), systemd(1), systemd-cgls(1), systemd.exec(5)

       /sys/fs/cgroup/io.cost.
	   iocost.conf(5)

       /sys/fs/cgroup/systemd
	   org.freedesktop.systemd1(5)

       /sys/fs/cgroup/unified/
	   file-hierarchy(7)

       /sys/fs/pstore/
	   systemd-pstore.service(8)

       /sys/fs/selinux/
	   systemd-nspawn(1)

       /sys/kernel/security/tpm0/binary_bios_measurements
	   systemd-pcrlock(8)

       /sys/module/kernel/parameters/crash_kexec_post_notifiers
	   systemd-pstore.service(8)

       /sys/module/printk/parameters/always_kmsg_dump
	   systemd-pstore.service(8)

       /sys/power/disk
	   systemd-sleep.conf(5)

       /sys/power/resume
	   systemd-hibernate-resume.service(8)

       /sys/power/resume_offset
	   systemd-hibernate-resume.service(8)

       /sys/power/state
	   systemd-sleep.conf(5), systemd-suspend.service(8)

       /sysroot
	   bootup(7), systemctl(1), systemd-fstab-generator(8), systemd-gpt-auto-generator(8), systemd-repart(8), systemd.special(7)

       /sysroot/etc/fstab
	   bootup(7)

       /system-update
	   systemd-system-update-generator(8), systemd.offline-updates(7), systemd.special(7)

       /sysusr/
	   systemd.special(7)

       /tmp/
	   crypttab(5), file-hierarchy(7), repart.d(5), systemd-system.conf(5), systemd-tmpfiles(8), systemd.exec(5), systemd.special(7), systemd.unit(5),
	   sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       /upload
	   systemd-journal-remote.service(8)

       /user.slice/user-1000.slice/user@1000.service/
	   systemd.resource-control(5)

       /usr/
	   binfmt.d(5), bootctl(1), bootup(7), coredump.conf(5), environment.d(5), file-hierarchy(7), homed.conf(5), iocost.conf(5), journal-remote.conf(5),
	   journal-upload.conf(5), journald.conf(5), kernel-command-line(7), logind.conf(5), machinectl(1), modules-load.d(5), networkd.conf(5), oomd.conf(5),
	   org.freedesktop.systemd1(5), portablectl(1), pstore.conf(5), repart.d(5), resolved.conf(5), sysctl.d(5), systemctl(1), systemd-dissect(1), systemd-
	   fstab-generator(8), systemd-modules-load.service(8), systemd-nspawn(1), systemd-remount-fs.service(8), systemd-sleep.conf(5), systemd-sysext(8),
	   systemd-system.conf(5), systemd-timedated.service(8), systemd-update-done.service(8), systemd-veritysetup-generator(8), systemd-volatile-
	   root.service(8), systemd.exec(5), systemd.generator(7), systemd.image-policy(7), systemd.mount(5), systemd.network(5), systemd.special(7),
	   systemd.unit(5), timesyncd.conf(5), udev(7)

       /usr/bin/
	   file-hierarchy(7), systemd.exec(5), systemd.service(5)

       /usr/bin/mount
	   org.freedesktop.systemd1(5), systemctl(1)

       /usr/bin/umount
	   org.freedesktop.systemd1(5), systemctl(1)

       /usr/include/
	   file-hierarchy(7)

       /usr/include/stdlib.h
	   systemd-tmpfiles(8)

       /usr/include/sysexits.h
	   systemd-tmpfiles(8)

       /usr/lib/
	   binfmt.d(5), environment.d(5), file-hierarchy(7), hwdb(7), modules-load.d(5), sysctl.d(5), systemd-delta(1), systemd-timedated.service(8),
	   systemd.dnssd(5), systemd.link(5), systemd.netdev(5), systemd.network(5), systemd.preset(5), systemd.unit(5), udev(7)

       /usr/lib/binfmt.d/*.conf
	   binfmt.d(5)

       /usr/lib/clock-epoch
	   systemd-timesyncd.service(8)

       /usr/lib/confexts/
	   systemd-dissect(1), systemd-sysext(8)

       /usr/lib/credstore/
	   systemd.exec(5)

       /usr/lib/credstore.encrypted/
	   systemd.exec(5)

       /usr/lib/dnssec-trust-anchors.d/
	   dnssec-trust-anchors.d(5)

       /usr/lib/dnssec-trust-anchors.d/*.negative
	   dnssec-trust-anchors.d(5)

       /usr/lib/dnssec-trust-anchors.d/*.positive
	   dnssec-trust-anchors.d(5)

       /usr/lib/environment.d/*.conf
	   environment.d(5)

       /usr/lib/extension-release.d/extension-release.IMAGE
	   os-release(5), systemd-sysext(8)

       /usr/lib/extension-release.d/extension-release.IMAGE
	   systemd.exec(5)

       /usr/lib/kernel/cmdline
	   kernel-install(8)

       /usr/lib/kernel/devicetree
	   kernel-install(8)

       /usr/lib/kernel/install.conf
	   kernel-install(8)

       /usr/lib/kernel/install.d/
	   kernel-install(8)

       /usr/lib/kernel/install.d/*.install
	   kernel-install(8)

       /usr/lib/machines/
	   machinectl(1), systemd-dissect(1)

       /usr/lib/modules/KERNEL_VERSION/vmlinuz
	   kernel-install(8), systemd.exec(5)

       /usr/lib/modules-load.d/*.conf
	   modules-load.d(5)

       /usr/lib/os-release
	   kernel-install(8), os-release(5), systemd-nspawn(1), systemd-sysext(8)

       /usr/lib/pcrlock.d/
	   systemd-pcrlock(8)

       /usr/lib/pcrlock.d/*.pcrlock
	   systemd.pcrlock(5)

       /usr/lib/pcrlock.d/*.pcrlock.d/*.pcrlock
	   systemd.pcrlock(5)

       /usr/lib/portables/
	   portablectl(1), systemd-dissect(1)

       /usr/lib/repart.d/*.conf
	   repart.d(5), systemd-repart(8)

       /usr/lib/sysctl.d/*.conf
	   sysctl.d(5)

       /usr/lib/sysctl.d/50-coredump.conf
	   systemd-coredump(8), systemd-sysctl.service(8)

       /usr/lib/systemd/
	   coredump.conf(5), crypttab(5), homed.conf(5), iocost.conf(5), journal-remote.conf(5), journal-upload.conf(5), journald.conf(5), logind.conf(5),
	   networkd.conf(5), oomd.conf(5), pstore.conf(5), resolved.conf(5), systemd-creds(1), systemd-cryptenroll(1), systemd-sleep.conf(5), systemd-
	   system.conf(5), timesyncd.conf(5)

       /usr/lib/systemd/*.conf.d/
	   coredump.conf(5), homed.conf(5), iocost.conf(5), journal-remote.conf(5), journal-upload.conf(5), journald.conf(5), logind.conf(5),
	   networkd.conf(5), oomd.conf(5), pstore.conf(5), resolved.conf(5), systemd-sleep.conf(5), systemd-system.conf(5), timesyncd.conf(5)

       /usr/lib/systemd/boot/efi/linuxaa64.efi.stub
	   systemd-stub(7)

       /usr/lib/systemd/boot/efi/linuxia32.efi.stub
	   systemd-stub(7)

       /usr/lib/systemd/boot/efi/linuxx64.efi.stub
	   systemd-stub(7)

       /usr/lib/systemd/coredump.conf.d/*.conf
	   coredump.conf(5)

       /usr/lib/systemd/dnssd
	   systemd.dnssd(5)

       /usr/lib/systemd/homed.conf.d/*.conf
	   homed.conf(5)

       /usr/lib/systemd/import-pubring.gpg
	   machinectl(1), sysupdate.d(5)

       /usr/lib/systemd/journal-remote.conf.d/*.conf
	   journal-remote.conf(5)

       /usr/lib/systemd/journal-upload.conf.d/*.conf
	   journal-upload.conf(5)

       /usr/lib/systemd/journald.conf.d/*.conf
	   journald.conf(5)

       /usr/lib/systemd/journald@NAMESPACE.conf.d/*.conf
	   journald.conf(5)

       /usr/lib/systemd/logind.conf
	   systemd-analyze(1)

       /usr/lib/systemd/logind.conf.d/*.conf
	   logind.conf(5)

       /usr/lib/systemd/network
	   systemd-networkd.service(8), systemd.link(5), systemd.netdev(5), systemd.network(5)

       /usr/lib/systemd/network/80-container-host0.network
	   systemd-nspawn(1)

       /usr/lib/systemd/network/80-container-ve.network
	   systemd-nspawn(1)

       /usr/lib/systemd/network/80-container-vz.network
	   systemd-nspawn(1)

       /usr/lib/systemd/networkd.conf.d/*.conf
	   networkd.conf(5)

       /usr/lib/systemd/ntp-units.d/
	   systemd-timedated.service(8)

       /usr/lib/systemd/oomd.conf.d/*.conf
	   oomd.conf(5)

       /usr/lib/systemd/portable/profile/
	   portablectl(1)

       /usr/lib/systemd/portable/profile/default/service.conf
	   portablectl(1)

       /usr/lib/systemd/resolv.conf
	   systemd-nspawn(1), systemd-resolved.service(8)

       /usr/lib/systemd/resolved.conf.d/*.conf
	   resolved.conf(5)

       /usr/lib/systemd/sleep.conf.d/*.conf
	   systemd-sleep.conf(5)

       /usr/lib/systemd/system/
	   systemctl(1), systemd(1), systemd.unit(5)

       /usr/lib/systemd/system-boot-check-no-failures
	   systemd-boot-check-no-failures.service(8)

       /usr/lib/systemd/system-environment-generators/
	   systemd.environment-generator(7)

       /usr/lib/systemd/system-environment-generators/some-generator
	   systemd.environment-generator(7)

       /usr/lib/systemd/system-generators/
	   systemd.generator(7)

       /usr/lib/systemd/system-generators/systemd-bless-boot-generator
	   systemd-bless-boot-generator(8)

       /usr/lib/systemd/system-generators/systemd-cryptsetup-generator
	   systemd-cryptsetup-generator(8)

       /usr/lib/systemd/system-generators/systemd-debug-generator
	   systemd-debug-generator(8)

       /usr/lib/systemd/system-generators/systemd-fstab-generator
	   systemd-fstab-generator(8)

       /usr/lib/systemd/system-generators/systemd-getty-generator
	   systemd-getty-generator(8)

       /usr/lib/systemd/system-generators/systemd-gpt-auto-generator
	   systemd-gpt-auto-generator(8)

       /usr/lib/systemd/system-generators/systemd-hibernate-resume-generator
	   systemd-hibernate-resume-generator(8)

       /usr/lib/systemd/system-generators/systemd-integritysetup-generator
	   systemd-integritysetup-generator(8)

       /usr/lib/systemd/system-generators/systemd-rc-local-generator
	   systemd-rc-local-generator(8)

       /usr/lib/systemd/system-generators/systemd-run-generator
	   systemd-run-generator(8)

       /usr/lib/systemd/system-generators/systemd-system-update-generator
	   systemd-system-update-generator(8)

       /usr/lib/systemd/system-generators/systemd-sysv-generator
	   systemd-sysv-generator(8)

       /usr/lib/systemd/system-generators/systemd-veritysetup-generator
	   systemd-veritysetup-generator(8)

       /usr/lib/systemd/system-pcrextend
	   systemd-pcrphase.service(8)

       /usr/lib/systemd/system-preset/*.preset
	   systemd.preset(5)

       /usr/lib/systemd/system-shutdown/
	   systemd-poweroff.service(8), systemd-soft-reboot.service(8)

       /usr/lib/systemd/system-sleep
	   systemd-suspend.service(8)

       /usr/lib/systemd/system.conf.d/*.conf
	   systemd-system.conf(5)

       /usr/lib/systemd/system/httpd.service
	   systemd.unit(5)

       /usr/lib/systemd/systemd
	   systemd(1)

       /usr/lib/systemd/systemd-backlight
	   systemd-backlight@.service(8)

       /usr/lib/systemd/systemd-battery-check
	   systemd-battery-check.service(8)

       /usr/lib/systemd/systemd-binfmt
	   systemd-binfmt.service(8)

       /usr/lib/systemd/systemd-bless-boot
	   systemd-bless-boot.service(8)

       /usr/lib/systemd/systemd-coredump
	   systemd-coredump(8)

       /usr/lib/systemd/systemd-fsck
	   systemd-fsck@.service(8)

       /usr/lib/systemd/systemd-fsckd
	   systemd-fsckd.service(8)

       /usr/lib/systemd/systemd-growfs
	   systemd-makefs@.service(8)

       /usr/lib/systemd/systemd-hibernate-resume
	   systemd-hibernate-resume.service(8)

       /usr/lib/systemd/systemd-homed
	   systemd-homed.service(8)

       /usr/lib/systemd/systemd-hostnamed
	   systemd-hostnamed.service(8)

       /usr/lib/systemd/systemd-importd
	   systemd-importd.service(8)

       /usr/lib/systemd/systemd-initctl
	   systemd-initctl.service(8)

       /usr/lib/systemd/systemd-integritysetup
	   systemd-integritysetup@.service(8)

       /usr/lib/systemd/systemd-journal-gatewayd
	   systemd-journal-gatewayd.service(8)

       /usr/lib/systemd/systemd-journal-remote
	   systemd-journal-remote.service(8)

       /usr/lib/systemd/systemd-journal-upload
	   systemd-journal-upload.service(8)

       /usr/lib/systemd/systemd-journald
	   systemd-journald.service(8)

       /usr/lib/systemd/systemd-localed
	   systemd-localed.service(8)

       /usr/lib/systemd/systemd-logind
	   systemd-logind.service(8)

       /usr/lib/systemd/systemd-machined
	   systemd-machined.service(8)

       /usr/lib/systemd/systemd-makefs
	   systemd-makefs@.service(8)

       /usr/lib/systemd/systemd-measure
	   systemd-measure(1)

       /usr/lib/systemd/systemd-modules-load
	   systemd-modules-load.service(8)

       /usr/lib/systemd/systemd-network-generator
	   systemd-network-generator.service(8)

       /usr/lib/systemd/systemd-networkd
	   systemd-networkd.service(8)

       /usr/lib/systemd/systemd-networkd-wait-online
	   systemd-networkd-wait-online.service(8)

       /usr/lib/systemd/systemd-oomd
	   systemd-oomd.service(8)

       /usr/lib/systemd/systemd-pcrextend
	   systemd-pcrphase.service(8), varlinkctl(1)

       /usr/lib/systemd/systemd-pcrlock
	   systemd-pcrlock(8)

       /usr/lib/systemd/systemd-portabled
	   systemd-portabled.service(8)

       /usr/lib/systemd/systemd-pstore
	   systemd-pstore.service(8)

       /usr/lib/systemd/systemd-quotacheck
	   systemd-quotacheck.service(8)

       /usr/lib/systemd/systemd-random-seed
	   systemd-random-seed.service(8)

       /usr/lib/systemd/systemd-remount-fs
	   systemd-remount-fs.service(8)

       /usr/lib/systemd/systemd-resolved
	   systemd-resolved.service(8)

       /usr/lib/systemd/systemd-rfkill
	   systemd-rfkill.service(8)

       /usr/lib/systemd/systemd-shutdown
	   systemd-poweroff.service(8)

       /usr/lib/systemd/systemd-storagetm
	   systemd-storagetm.service(8)

       /usr/lib/systemd/systemd-sysctl
	   systemd-sysctl.service(8)

       /usr/lib/systemd/systemd-time-wait-sync
	   systemd-time-wait-sync.service(8)

       /usr/lib/systemd/systemd-timedated
	   systemd-timedated.service(8)

       /usr/lib/systemd/systemd-timesyncd
	   systemd-timesyncd.service(8)

       /usr/lib/systemd/systemd-tpm2-setup
	   systemd-tpm2-setup.service(8)

       /usr/lib/systemd/systemd-udevd
	   systemd-udevd.service(8)

       /usr/lib/systemd/systemd-update-done
	   systemd-update-done.service(8)

       /usr/lib/systemd/systemd-update-utmp
	   systemd-update-utmp.service(8)

       /usr/lib/systemd/systemd-user-runtime-dir
	   user@.service(5)

       /usr/lib/systemd/systemd-user-sessions
	   systemd-user-sessions.service(8)

       /usr/lib/systemd/systemd-userdbd
	   systemd-userdbd.service(8)

       /usr/lib/systemd/systemd-veritysetup
	   systemd-veritysetup@.service(8)

       /usr/lib/systemd/systemd-volatile-root
	   systemd-volatile-root.service(8)

       /usr/lib/systemd/timesyncd.conf.d/*.conf
	   timesyncd.conf(5)

       /usr/lib/systemd/ukify.conf
	   ukify(1)

       /usr/lib/systemd/user/
	   systemd.unit(5)

       /usr/lib/systemd/user-environment-generators/
	   systemd.environment-generator(7)

       /usr/lib/systemd/user-environment-generators/30-systemd-environment-d-generator
	   systemd-environment-d-generator(8)

       /usr/lib/systemd/user-environment-generators/some-generator
	   systemd.environment-generator(7)

       /usr/lib/systemd/user-generators/
	   systemd.generator(7)

       /usr/lib/systemd/user-generators/systemd-xdg-autostart-generator
	   systemd-xdg-autostart-generator(8)

       /usr/lib/systemd/user-preset/*.preset
	   systemd.preset(5)

       /usr/lib/systemd/user.conf.d/*.conf
	   systemd-system.conf(5)

       /usr/lib/sysupdate.component.d/*.conf
	   systemd-sysupdate(8)

       /usr/lib/sysupdate.*.d/
	   systemd-sysupdate(8)

       /usr/lib/sysupdate.d/*.conf
	   systemd-sysupdate(8), sysupdate.d(5)

       /usr/lib/sysusers.d
	   sysusers.d(5)

       /usr/lib/sysusers.d/*.conf
	   sysusers.d(5)

       /usr/lib/sysusers.d/radvd.conf
	   systemd-sysusers(8)

       /usr/lib/tmpfiles.d
	   tmpfiles.d(5)

       /usr/lib/tmpfiles.d/*.conf
	   tmpfiles.d(5)

       /usr/lib/tmpfiles.d/provision.conf
	   systemd.system-credentials(7)

       /usr/lib/tmpfiles.d/systemd.conf
	   systemd-coredump(8)

       /usr/lib/tmpfiles/systemd-pstore.conf
	   systemd-pstore.service(8)

       /usr/lib/udev
	   udev(7)

       /usr/lib/udev/hwdb.bin
	   hwdb(7)

       /usr/lib/udev/hwdb.d
	   hwdb(7)

       /usr/lib/udev/rules.d
	   udev(7)

       /usr/lib/userdb/
	   nss-systemd(8), systemd-userdbd.service(8), userdbctl(1)

       /usr/lib64/
	   file-hierarchy(7)

       /usr/lib64/firefox/firefox
	   coredumpctl(1)

       /usr/local/bin
	   systemd.exec(5), systemd.service(5)

       /usr/local/lib/
	   binfmt.d(5), environment.d(5), modules-load.d(5), sysctl.d(5), systemd-timedated.service(8), systemd.dnssd(5)

       /usr/local/lib/confexts/
	   systemd-sysext(8)

       /usr/local/lib/machines/
	   machinectl(1)

       /usr/local/lib/portables/
	   portablectl(1)

       /usr/local/lib/systemd/*.conf.d/
	   coredump.conf(5), homed.conf(5), iocost.conf(5), journal-remote.conf(5), journal-upload.conf(5), journald.conf(5), logind.conf(5),
	   networkd.conf(5), oomd.conf(5), pstore.conf(5), resolved.conf(5), systemd-sleep.conf(5), systemd-system.conf(5), timesyncd.conf(5)

       /usr/local/lib/systemd/dnssd
	   systemd.dnssd(5)

       /usr/local/lib/systemd/network
	   systemd.link(5), systemd.netdev(5), systemd.network(5)

       /usr/local/lib/systemd/system
	   systemd(1), systemd.unit(5)

       /usr/local/lib/systemd/system-environment-generators/
	   systemd.environment-generator(7)

       /usr/local/lib/systemd/system-generators/
	   systemd.generator(7)

       /usr/local/lib/systemd/ukify.conf
	   ukify(1)

       /usr/local/lib/systemd/user
	   systemd.unit(5)

       /usr/local/lib/systemd/user-environment-generators/
	   systemd.environment-generator(7)

       /usr/local/lib/systemd/user-generators/
	   systemd.generator(7)

       /usr/local/lib/udev/rules.d
	   udev(7)

       /usr/local/pcrlock.d/
	   systemd-pcrlock(8)

       /usr/local/pcrlock.d/*.pcrlock
	   systemd.pcrlock(5)

       /usr/local/pcrlock.d/*.pcrlock.d/*.pcrlock
	   systemd.pcrlock(5)

       /usr/local/sbin
	   systemd.exec(5)

       /usr/local/share
	   systemd.unit(5)

       /usr/local/share/systemd/user
	   systemd.unit(5)

       /usr/sbin/
	   file-hierarchy(7), systemd.exec(5)

       /usr/sbin/nologin
	   sysusers.d(5)

       /usr/share/
	   file-hierarchy(7), systemd.unit(5)

       /usr/share/dbus-1/system-services/org.example.simple-dbus-service.service
	   systemd.service(5)

       /usr/share/doc/
	   file-hierarchy(7)

       /usr/share/factory/
	   file-hierarchy(7), tmpfiles.d(5)

       /usr/share/factory/etc/
	   file-hierarchy(7)

       /usr/share/factory/var/
	   file-hierarchy(7)

       /usr/share/systemd/user
	   systemd.unit(5)

       /usr/share/user-tmpfiles.d/
	   systemd-tmpfiles(8)

       /usr/share/user-tmpfiles.d/*.conf
	   tmpfiles.d(5)

       /usr/share/zoneinfo/
	   localtime(5)

       /usr/share/zoneinfo/zone.tab
	   org.freedesktop.timedate1(5)

       /var/
	   file-hierarchy(7), journald.conf(5), kernel-command-line(7), repart.d(5), systemctl(1), systemd-cryptenroll(1), systemd-fstab-generator(8),
	   systemd-gpt-auto-generator(8), systemd-journald.service(8), systemd-nspawn(1), systemd-pcrlock(8), systemd-pcrphase.service(8), systemd-
	   poweroff.service(8), systemd-random-seed.service(8), systemd-sysext(8), systemd-tpm2-setup.service(8), systemd-update-done.service(8), systemd-
	   volatile-root.service(8), systemd.exec(5), systemd.generator(7), systemd.offline-updates(7), systemd.special(7), systemd.unit(5), tmpfiles.d(5)

       /var/.updated
	   systemd-update-done.service(8)

       /var/cache/
	   file-hierarchy(7), systemd.exec(5), systemd.unit(5), tmpfiles.d(5)

       /var/cache/dnf/
	   tmpfiles.d(5)

       /var/cache/krb5rcache/
	   tmpfiles.d(5)

       /var/cache/private
	   systemd.exec(5)

       /var/lib/
	   file-hierarchy(7), systemd.exec(5), systemd.unit(5), tmpfiles.d(5)

       /var/lib/confexts/
	   systemd-sysext(8)

       /var/lib/container/
	   machinectl(1)

       /var/lib/dbus/machine-id
	   machine-id(5)

       /var/lib/extensions/
	   systemd-dissect(1), systemd-sysext(8)

       /var/lib/machines/
	   machinectl(1), org.freedesktop.import1(5), systemd-dissect(1), systemd-nspawn(1), systemd.nspawn(5), tmpfiles.d(5)

       /var/lib/machines/myContainer
	   sysupdate.d(5)

       /var/lib/machines/myContainer_@v
	   sysupdate.d(5)

       /var/lib/pcrlock.d/
	   systemd-pcrlock(8)

       /var/lib/pcrlock.d/*.pcrlock
	   systemd.pcrlock(5)

       /var/lib/pcrlock.d/*.pcrlock.d/*.pcrlock
	   systemd.pcrlock(5)

       /var/lib/pcrlock.d/230-secureboot-policy.pcrlock.d/generated.pcrlock
	   systemd-pcrlock(8)

       /var/lib/pcrlock.d/250-firmware-code-early.pcrlock.d/generated.pcrlock
	   systemd-pcrlock(8)

       /var/lib/pcrlock.d/250-firmware-config-early.pcrlock.d/generated.pcrlock
	   systemd-pcrlock(8)

       /var/lib/pcrlock.d/550-firmware-code-late.pcrlock.d/generated.pcrlock
	   systemd-pcrlock(8)

       /var/lib/pcrlock.d/550-firmware-config-late.pcrlock.d/generated.pcrlock
	   systemd-pcrlock(8)

       /var/lib/pcrlock.d/600-gpt.pcrlock.d/generated.pcrlock
	   systemd-pcrlock(8)

       /var/lib/pcrlock.d/620-secureboot-authority.pcrlock.d/generated.pcrlock
	   systemd-pcrlock(8)

       /var/lib/pcrlock.d/710-kernel-cmdline.pcrlock/generated.pcrlock
	   systemd-pcrlock(8)

       /var/lib/pcrlock.d/720-kernel-initrd.pcrlock/generated.pcrlock
	   systemd-pcrlock(8)

       /var/lib/pcrlock.d/820-machine-id.pcrlock
	   systemd-pcrlock(8)

       /var/lib/pcrlock.d/830-root-file-system.pcrlock
	   systemd-pcrlock(8)

       /var/lib/pcrlock.d/840-file-system-path.pcrlock
	   systemd-pcrlock(8)

       /var/lib/portables/
	   portablectl(1), systemd-dissect(1)

       /var/lib/private
	   systemd.exec(5)

       /var/lib/systemd/
	   crypttab(5), systemd-creds(1), systemd-cryptenroll(1), systemd.exec(5)

       /var/lib/systemd/backlight/
	   systemd-backlight@.service(8)

       /var/lib/systemd/coredump/
	   coredump.conf(5), coredumpctl(1), systemd-coredump(8)

       /var/lib/systemd/credential.secret
	   systemd-creds(1)

       /var/lib/systemd/credentials.secret
	   systemd.exec(5)

       /var/lib/systemd/ephemeral-trees/
	   systemd.exec(5)

       /var/lib/systemd/home/
	   systemd-homed.service(8)

       /var/lib/systemd/home/*.public
	   systemd-homed.service(8)

       /var/lib/systemd/home/local.private
	   systemd-homed.service(8)

       /var/lib/systemd/home/local.public
	   systemd-homed.service(8)

       /var/lib/systemd/journal-upload/state
	   systemd-journal-upload.service(8)

       /var/lib/systemd/pcrlock.json
	   systemd-pcrlock(8)

       /var/lib/systemd/pstore/
	   pstore.conf(5), systemd-pstore.service(8)

       /var/lib/systemd/random-seed
	   systemd-random-seed.service(8)

       /var/lib/systemd/rfkill/
	   systemd-rfkill.service(8)

       /var/lib/systemd/timesync/clock
	   systemd-timesyncd.service(8)

       /var/lib/systemd/tpm2-srk-public-key.
	   systemd-tpm2-setup.service(8)

       /var/lib/systemd/tpm2-srk-public-key.pem
	   systemd-tpm2-setup.service(8)

       /var/lib/systemd/tpm2-srk-public-key.tpm2_public
	   systemd-tpm2-setup.service(8)

       /var/lib/systemd/tpm2-srk-public-key.tpm2b_public
	   systemd-tpm2-setup.service(8)

       /var/lock
	   systemctl(1)

       /var/log/
	   file-hierarchy(7), sd_journal_get_seqnum(3), systemd.exec(5), systemd.unit(5), tmpfiles.d(5)

       /var/log/journal/
	   coredumpctl(1), journalctl(1), journald.conf(5), sd_journal_open(3), systemd-journald.service(8), systemd-nspawn(1)

       /var/log/journal/remote/
	   systemd-journal-remote.service(8)

       /var/log/journal/remote/remote-some.host.journal
	   systemd-journal-remote.service(8)

       /var/log/private
	   systemd.exec(5)

       /var/run/
	   file-hierarchy(7), org.freedesktop.systemd1(5), systemctl(1), tmpfiles.d(5)

       /var/spool/
	   file-hierarchy(7)

       /var/tmp/
	   file-hierarchy(7), repart.d(5), systemd-gpt-auto-generator(8), systemd-nspawn(1), systemd-system.conf(5), systemd.exec(5), systemd.special(7),
	   systemd.unit(5), sysupdate.d(5), sysusers.d(5), tmpfiles.d(5)

       ESP/.../foo.efi.extra.d/*.addon.efi
	   systemd-stub(7)

       ESP/.../foo.efi.extra.d/*.cred
	   systemd-stub(7)

       ESP/.../foo.efi.extra.d/*.raw
	   systemd-stub(7)

       ESP/loader/addons/*.addon.efi
	   systemd-stub(7)

       ESP/loader/credentials/*.cred
	   systemd-stub(7)

       ESP/loader/entries/*.conf
	   loader.conf(5)

       ESP/loader/loader.conf
	   loader.conf(5)

       XBOOTLDR/loader/entries/*.conf
	   loader.conf(5)

       automount.automount
	   systemd.automount(5), systemd.unit(5)

       basic.target
	   systemd.special(7)

       blockdev@.target
	   systemd.special(7)

       bluetooth.target
	   systemd.special(7)

       boot-complete.target
	   systemd.special(7)

       bootctl
	   bootctl(1)

       busctl
	   busctl(1)

       coredumpctl
	   coredumpctl(1)

       cryptsetup-pre.target
	   systemd.special(7)

       cryptsetup.target
	   systemd.special(7)

       ctrl-alt-del.target
	   systemd.special(7)

       dbus.service
	   systemd.special(7)

       dbus.socket
	   systemd.special(7)

       default.target
	   systemd.special(7)

       device.device
	   systemd.device(5), systemd.unit(5)

       display-manager.service
	   systemd.special(7)

       emergency.target
	   systemd.special(7)

       exit.target
	   systemd.special(7)

       factory-reset.target
	   systemd.special(7)

       final.target
	   systemd.special(7)

       first-boot-complete.target
	   systemd.special(7)

       getty-pre.target
	   systemd.special(7)

       getty.target
	   systemd.special(7)

       graphical.target
	   systemd.special(7)

       halt
	   poweroff(8)

       halt.target
	   systemd.special(7)

       hibernate.target
	   systemd.special(7)

       homectl
	   homectl(1)

       hostnamectl
	   hostnamectl(1)

       hybrid-sleep.target
	   systemd.special(7)

       init
	   systemd(1)

       init.scope
	   systemd.special(7)

       initrd-fs.target
	   systemd.special(7)

       initrd-root-device.target
	   systemd.special(7)

       initrd-root-fs.target
	   systemd.special(7)

       initrd-usr-fs.target
	   systemd.special(7)

       initrd.target
	   systemd.special(7)

       integritysetup-pre.target
	   systemd.special(7)

       integritysetup.target
	   systemd.special(7)

       journalctl
	   journalctl(1)

       kbrequest.target
	   systemd.special(7)

       kernel-install
	   kernel-install(8)

       kexec.target
	   systemd.special(7)

       libnss_myhostname.so.2
	   nss-myhostname(8)

       libnss_mymachines.so.2
	   nss-mymachines(8)

       libnss_resolve.so.2
	   nss-resolve(8)

       libnss_systemd.so.2
	   nss-systemd(8)

       link.link
	   systemd.link(5)

       local-fs-pre.target
	   systemd.special(7)

       local-fs.target
	   systemd.special(7)

       localectl
	   localectl(1)

       loginctl
	   loginctl(1)

       machine.slice
	   systemd.special(7)

       machinectl
	   machinectl(1)

       machines.target
	   systemd.special(7)

       mount.mount
	   systemd.exec(5), systemd.kill(5), systemd.mount(5), systemd.resource-control(5), systemd.unit(5)

       multi-user.target
	   systemd.special(7)

       netdev.netdev
	   systemd.netdev(5)

       network.network
	   systemd.network(5)

       network-online.target
	   systemd.special(7)

       network-pre.target
	   systemd.special(7)

       network.target
	   systemd.special(7)

       network_service.dnssd
	   systemd.dnssd(5)

       networkctl
	   networkctl(1)

       nss-lookup.target
	   systemd.special(7)

       nss-user-lookup.target
	   systemd.special(7)

       oomctl
	   oomctl(1)

       pam_systemd.so
	   pam_systemd(8)

       pam_systemd_home.so
	   pam_systemd_home(8)

       pam_systemd_loadkey.so
	   pam_systemd_loadkey(8)

       path.path
	   systemd.path(5), systemd.unit(5)

       paths.target
	   systemd.special(7)

       pkg-config
	   libsystemd(3), libudev(3), sd-bus(3), sd-daemon(3), sd-device(3), sd-event(3), sd-hwdb(3), sd-id128(3), sd-journal(3), sd-login(3)

       portablectl
	   portablectl(1)

       poweroff
	   poweroff(8)

       poweroff.target
	   systemd.special(7)

       printer.target
	   systemd.special(7)

       rc-local.service
	   systemd-rc-local-generator(8)

       reboot
	   poweroff(8)

       reboot.target
	   systemd.special(7)

       remote-cryptsetup.target
	   systemd.special(7)

       remote-fs-pre.target
	   systemd.special(7)

       remote-fs.target
	   systemd.special(7)

       remote-veritysetup.target
	   systemd.special(7)

       rescue.target
	   systemd.special(7)

       resolvectl
	   resolvectl(1)

       rpcbind.target
	   systemd.special(7)

       runlevel
	   runlevel(8)

       runlevel2.target
	   systemd.special(7)

       runlevel3.target
	   systemd.special(7)

       runlevel4.target
	   systemd.special(7)

       runlevel5.target
	   systemd.special(7)

       scope.scope
	   systemd.kill(5), systemd.resource-control(5), systemd.scope(5), systemd.unit(5)

       service.service
	   systemd.exec(5), systemd.kill(5), systemd.resource-control(5), systemd.service(5), systemd.unit(5)

       shutdown
	   shutdown(8)

       shutdown.target
	   systemd.special(7)

       sigpwr.target
	   systemd.special(7)

       sleep.target
	   systemd.special(7)

       slice.slice
	   systemd.resource-control(5), systemd.slice(5), systemd.unit(5)

       slices.target
	   systemd.special(7)

       smartcard.target
	   systemd.special(7)

       socket.socket
	   systemd.exec(5), systemd.kill(5), systemd.resource-control(5), systemd.socket(5), systemd.unit(5)

       sockets.target
	   systemd.special(7)

       soft-reboot.target
	   systemd.special(7)

       sound.target
	   systemd.special(7)

       storage-target-mode.target
	   systemd.special(7)

       suspend-then-hibernate.target
	   systemd.special(7)

       suspend.target
	   systemd.special(7)

       swap.swap
	   systemd.exec(5), systemd.kill(5), systemd.resource-control(5), systemd.swap(5), systemd.unit(5)

       swap.target
	   systemd.special(7)

       sysinit.target
	   systemd.special(7)

       syslog.socket
	   systemd.special(7)

       system-systemd\x2dcryptsetup.slice
	   systemd-cryptsetup(8)

       system-update-cleanup.service
	   systemd.special(7)

       system-update-pre.target
	   systemd.special(7)

       system-update.target
	   systemd.special(7)

       system.slice
	   systemd.special(7)

       systemctl
	   systemctl(1)

       systemd-ac-power
	   systemd-ac-power(1)

       systemd-analyze
	   systemd-analyze(1)

       systemd-ask-password
	   systemd-ask-password(1)

       systemd-ask-password-console.path
	   systemd-ask-password-console.service(8)

       systemd-ask-password-console.service
	   systemd-ask-password-console.service(8)

       systemd-ask-password-wall.path
	   systemd-ask-password-console.service(8)

       systemd-ask-password-wall.service
	   systemd-ask-password-console.service(8)

       systemd-backlight@.service
	   systemd-backlight@.service(8)

       systemd-battery-check.service
	   systemd-battery-check.service(8)

       systemd-binfmt.service
	   systemd-binfmt.service(8)

       systemd-bless-boot.service
	   systemd-bless-boot.service(8)

       systemd-boot-check-no-failures.service
	   systemd-boot-check-no-failures.service(8)

       systemd-boot-random-seed.service
	   systemd-boot-random-seed.service(8)

       systemd-bsod
	   systemd-bsod.service(8)

       systemd-bsod.service
	   systemd-bsod.service(8)

       systemd-cat
	   systemd-cat(1)

       systemd-cgls
	   systemd-cgls(1)

       systemd-cgtop
	   systemd-cgtop(1)

       systemd-confext
	   systemd-sysext(8)

       systemd-confext.service
	   systemd-sysext(8)

       systemd-coredump.socket
	   systemd-coredump(8)

       systemd-coredump@.service
	   systemd-coredump(8)

       systemd-creds
	   systemd-creds(1)

       systemd-cryptenroll
	   systemd-cryptenroll(1)

       systemd-cryptsetup
	   systemd-cryptsetup(8)

       systemd-cryptsetup@.service
	   systemd-cryptsetup(8)

       systemd-delta
	   systemd-delta(1)

       systemd-detect-virt
	   systemd-detect-virt(1)

       systemd-dissect
	   systemd-dissect(1)

       systemd-escape
	   systemd-escape(1)

       systemd-firstboot
	   systemd-firstboot(1)

       systemd-firstboot.service
	   systemd-firstboot(1)

       systemd-fsck-root.service
	   systemd-fsck@.service(8)

       systemd-fsck-usr.service
	   systemd-fsck@.service(8)

       systemd-fsck@.service
	   systemd-fsck@.service(8)

       systemd-fsckd.service
	   systemd-fsckd.service(8)

       systemd-fsckd.socket
	   systemd-fsckd.service(8)

       systemd-growfs-root.service
	   systemd-makefs@.service(8)

       systemd-growfs@mountpoint.service
	   systemd-makefs@.service(8)

       systemd-halt.service
	   systemd-poweroff.service(8)

       systemd-hibernate-resume.service
	   systemd-hibernate-resume.service(8)

       systemd-hibernate.service
	   systemd-suspend.service(8)

       systemd-homed.service
	   systemd-homed.service(8)

       systemd-hostnamed.service
	   systemd-hostnamed.service(8)

       systemd-hwdb
	   systemd-hwdb(8)

       systemd-hybrid-sleep.service
	   systemd-suspend.service(8)

       systemd-id128
	   systemd-id128(1)

       systemd-importd.service
	   systemd-importd.service(8)

       systemd-inhibit
	   systemd-inhibit(1)

       systemd-initctl.service
	   systemd-initctl.service(8)

       systemd-initctl.socket
	   systemd-initctl.service(8)

       systemd-integritysetup@.service
	   systemd-integritysetup@.service(8)

       systemd-journal-gatewayd.service
	   systemd-journal-gatewayd.service(8)

       systemd-journal-gatewayd.socket
	   systemd-journal-gatewayd.service(8)

       systemd-journal-remote.service
	   systemd-journal-remote.service(8)

       systemd-journal-remote.socket
	   systemd-journal-remote.service(8)

       systemd-journal-upload.service
	   systemd-journal-upload.service(8)

       systemd-journald-audit.socket
	   systemd-journald.service(8)

       systemd-journald-dev-log.socket
	   systemd-journald.service(8)

       systemd-journald-varlink@.socket
	   systemd-journald.service(8)

       systemd-journald.service
	   systemd-journald.service(8)

       systemd-journald.socket
	   systemd-journald.service(8)

       systemd-journald@.service
	   systemd-journald.service(8)

       systemd-journald@.socket
	   systemd-journald.service(8)

       systemd-kexec.service
	   systemd-poweroff.service(8)

       systemd-localed.service
	   systemd-localed.service(8)

       systemd-logind.service
	   systemd-logind.service(8)

       systemd-machine-id-commit.service
	   systemd-machine-id-commit.service(8)

       systemd-machine-id-setup
	   systemd-machine-id-setup(1)

       systemd-machined.service
	   systemd-machined.service(8)

       systemd-makefs@device.service
	   systemd-makefs@.service(8)

       systemd-mkswap@device.service
	   systemd-makefs@.service(8)

       systemd-modules-load.service
	   systemd-modules-load.service(8)

       systemd-mount
	   systemd-mount(1)

       systemd-network-generator.service
	   systemd-network-generator.service(8)

       systemd-networkd-wait-online.service
	   systemd-networkd-wait-online.service(8)

       systemd-networkd-wait-online@.service
	   systemd-networkd-wait-online.service(8)

       systemd-networkd.service
	   systemd-networkd.service(8)

       systemd-notify
	   systemd-notify(1)

       systemd-nspawn
	   systemd-nspawn(1)

       systemd-oomd.service
	   systemd-oomd.service(8)

       systemd-path
	   systemd-path(1)

       systemd-pcrfs-root.service
	   systemd-pcrphase.service(8)

       systemd-pcrfs@.service
	   systemd-pcrphase.service(8)

       systemd-pcrmachine.service
	   systemd-pcrphase.service(8)

       systemd-pcrphase-initrd.service
	   systemd-pcrphase.service(8)

       systemd-pcrphase-sysinit.service
	   systemd-pcrphase.service(8)

       systemd-pcrphase.service
	   systemd-pcrphase.service(8)

       systemd-portabled.service
	   systemd-portabled.service(8)

       systemd-poweroff.service
	   systemd-poweroff.service(8)

       systemd-pstore.service
	   systemd-pstore.service(8)

       systemd-quotacheck.service
	   systemd-quotacheck.service(8)

       systemd-random-seed.service
	   systemd-random-seed.service(8)

       systemd-reboot.service
	   systemd-poweroff.service(8)

       systemd-remount-fs.service
	   systemd-remount-fs.service(8)

       systemd-repart
	   systemd-repart(8)

       systemd-repart.service
	   systemd-repart(8)

       systemd-resolved.service
	   systemd-resolved.service(8)

       systemd-rfkill.service
	   systemd-rfkill.service(8)

       systemd-rfkill.socket
	   systemd-rfkill.service(8)

       systemd-run
	   systemd-run(1)

       systemd-socket-activate
	   systemd-socket-activate(1)

       systemd-socket-proxyd
	   systemd-socket-proxyd(8)

       systemd-soft-reboot.service
	   systemd-soft-reboot.service(8)

       systemd-stdio-bridge
	   systemd-stdio-bridge(1)

       systemd-storagetm.service
	   systemd-storagetm.service(8)

       systemd-suspend-then-hibernate.service
	   systemd-suspend.service(8)

       systemd-suspend.service
	   systemd-suspend.service(8)

       systemd-sysctl.service
	   systemd-sysctl.service(8)

       systemd-sysext
	   systemd-sysext(8)

       systemd-sysext.service
	   systemd-sysext(8)

       systemd-sysupdate
	   systemd-sysupdate(8)

       systemd-sysupdate.service
	   systemd-sysupdate(8)

       systemd-sysusers
	   systemd-sysusers(8)

       systemd-sysusers.service
	   systemd-sysusers(8)

       systemd-time-wait-sync.service
	   systemd-time-wait-sync.service(8)

       systemd-timedated.service
	   systemd-timedated.service(8)

       systemd-timesyncd.service
	   systemd-timesyncd.service(8)

       systemd-tmpfiles
	   systemd-tmpfiles(8)

       systemd-tmpfiles-clean.service
	   systemd-tmpfiles(8)

       systemd-tmpfiles-clean.timer
	   systemd-tmpfiles(8)

       systemd-tmpfiles-setup-dev-early.service
	   systemd-tmpfiles(8)

       systemd-tmpfiles-setup-dev.service
	   systemd-tmpfiles(8)

       systemd-tmpfiles-setup.service
	   systemd-tmpfiles(8)

       systemd-tpm2-setup.service
	   systemd-tpm2-setup.service(8)

       systemd-tty-ask-password-agent
	   systemd-tty-ask-password-agent(1)

       systemd-udev-settle.service
	   systemd-udev-settle.service(8)

       systemd-udevd-control.socket
	   systemd-udevd.service(8)

       systemd-udevd-kernel.socket
	   systemd-udevd.service(8)

       systemd-udevd.service
	   systemd-udevd.service(8)

       systemd-update-done.service
	   systemd-update-done.service(8)

       systemd-update-utmp-runlevel.service
	   systemd-update-utmp.service(8)

       systemd-update-utmp.service
	   systemd-update-utmp.service(8)

       systemd-user-sessions.service
	   systemd-user-sessions.service(8)

       systemd-userdbd.service
	   systemd-userdbd.service(8)

       systemd-veritysetup@.service
	   systemd-veritysetup@.service(8)

       systemd-volatile-root.service
	   systemd-volatile-root.service(8)

       target.target
	   systemd.target(5), systemd.unit(5)

       telinit
	   telinit(8)

       time-set.target
	   systemd.special(7)

       time-sync.target
	   systemd.special(7)

       timedatectl
	   timedatectl(1)

       timer.timer
	   systemd.timer(5), systemd.unit(5)

       timers.target
	   systemd.special(7)

       udevadm
	   udevadm(8)

       ukify
	   ukify(1)

       umount.target
	   systemd.special(7)

       usb-gadget.target
	   systemd.special(7)

       user-UID.slice
	   user@.service(5)

       user-runtime-dir@UID.service
	   user@.service(5)

       user.slice
	   systemd.special(7)

       user@UID.service
	   user@.service(5)

       userdbctl
	   userdbctl(1)

       varlinkctl
	   varlinkctl(1)

       veritysetup-pre.target
	   systemd.special(7)

       veritysetup.target
	   systemd.special(7)

       ~/.config/environment.d/*.conf
	   environment.d(5)

       ~/.config/systemd/user/
	   systemd.unit(5)

       ~/.config/systemd/user.conf
	   systemd-system.conf(5)

       ~/.config/systemd/user.control/
	   systemd.unit(5)

       ~/.config/user-tmpfiles.d/*.conf
	   tmpfiles.d(5)

       ~/.local/share/user-tmpfiles.d/*.conf
	   tmpfiles.d(5)

D-BUS INTERFACES
       Interfaces exposed over D-Bus.

       org.freedesktop.DBus.ObjectManager
	   org.freedesktop.home1(5)

       org.freedesktop.LogControl1
	   org.freedesktop.LogControl1(5)

       org.freedesktop.home1.Home
	   org.freedesktop.home1(5)

       org.freedesktop.home1.Manager
	   org.freedesktop.home1(5)

       org.freedesktop.hostname1
	   org.freedesktop.hostname1(5)

       org.freedesktop.import1.Manager
	   org.freedesktop.import1(5)

       org.freedesktop.import1.Transfer
	   org.freedesktop.import1(5)

       org.freedesktop.locale1
	   org.freedesktop.locale1(5)

       org.freedesktop.login1.Manager
	   org.freedesktop.login1(5)

       org.freedesktop.login1.Seat
	   org.freedesktop.login1(5)

       org.freedesktop.login1.Session
	   org.freedesktop.login1(5)

       org.freedesktop.login1.User
	   org.freedesktop.login1(5)

       org.freedesktop.machine1.Machine
	   org.freedesktop.machine1(5)

       org.freedesktop.machine1.Manager
	   org.freedesktop.machine1(5)

       org.freedesktop.network1.DHCPServer
	   org.freedesktop.network1(5)

       org.freedesktop.network1.DHCPv4Client
	   org.freedesktop.network1(5)

       org.freedesktop.network1.DHCPv6Client
	   org.freedesktop.network1(5)

       org.freedesktop.network1.Link
	   org.freedesktop.network1(5)

       org.freedesktop.network1.Manager
	   org.freedesktop.network1(5)

       org.freedesktop.network1.Network
	   org.freedesktop.network1(5)

       org.freedesktop.oom1.Manager
	   org.freedesktop.oom1(5)

       org.freedesktop.portable1.Image
	   org.freedesktop.portable1(5)

       org.freedesktop.portable1.Manager
	   org.freedesktop.portable1(5)

       org.freedesktop.resolve1.Link
	   org.freedesktop.resolve1(5)

       org.freedesktop.resolve1.Manager
	   org.freedesktop.resolve1(5)

       org.freedesktop.systemd1.Automount
	   org.freedesktop.systemd1(5)

       org.freedesktop.systemd1.Device
	   org.freedesktop.systemd1(5)

       org.freedesktop.systemd1.Job
	   org.freedesktop.systemd1(5)

       org.freedesktop.systemd1.Manager
	   org.freedesktop.systemd1(5)

       org.freedesktop.systemd1.Mount
	   org.freedesktop.systemd1(5)

       org.freedesktop.systemd1.Path
	   org.freedesktop.systemd1(5)

       org.freedesktop.systemd1.Scope
	   org.freedesktop.systemd1(5)

       org.freedesktop.systemd1.Service
	   org.freedesktop.systemd1(5)

       org.freedesktop.systemd1.Slice
	   org.freedesktop.systemd1(5)

       org.freedesktop.systemd1.Socket
	   org.freedesktop.systemd1(5)

       org.freedesktop.systemd1.Swap
	   org.freedesktop.systemd1(5)

       org.freedesktop.systemd1.Timer
	   org.freedesktop.systemd1(5)

       org.freedesktop.systemd1.Unit
	   org.freedesktop.systemd1(5)

       org.freedesktop.timedate1
	   org.freedesktop.timedate1(5)

D-BUS METHODS
       Methods exposed in the D-Bus interface.

       Abandon()
	   org.freedesktop.systemd1(5)

       AbandonScope()
	   org.freedesktop.systemd1(5)

       Acquire()
	   org.freedesktop.home1(5)

       AcquireHome()
	   org.freedesktop.home1(5)

       Activate()
	   org.freedesktop.home1(5), org.freedesktop.login1(5)

       ActivateHome()
	   org.freedesktop.home1(5)

       ActivateSession()
	   org.freedesktop.login1(5)

       ActivateSessionOnSeat()
	   org.freedesktop.login1(5)

       AddDependencyUnitFiles()
	   org.freedesktop.systemd1(5)

       Attach()
	   org.freedesktop.portable1(5)

       AttachDevice()
	   org.freedesktop.login1(5)

       AttachImage()
	   org.freedesktop.portable1(5)

       AttachImageWithExtensions()
	   org.freedesktop.portable1(5)

       AttachProcesses()
	   org.freedesktop.systemd1(5)

       AttachProcessesToUnit()
	   org.freedesktop.systemd1(5)

       AttachWithExtensions()
	   org.freedesktop.portable1(5)

       Authenticate()
	   org.freedesktop.home1(5)

       AuthenticateHome()
	   org.freedesktop.home1(5)

       BindMount()
	   org.freedesktop.machine1(5), org.freedesktop.systemd1(5)

       BindMountMachine()
	   org.freedesktop.machine1(5)

       BindMountUnit()
	   org.freedesktop.systemd1(5)

       CanHalt()
	   org.freedesktop.login1(5)

       CanHibernate()
	   org.freedesktop.login1(5)

       CanHybridSleep()
	   org.freedesktop.login1(5)

       CanPowerOff()
	   org.freedesktop.login1(5)

       CanReboot()
	   org.freedesktop.login1(5)

       CanRebootParameter()
	   org.freedesktop.login1(5)

       CanRebootToBootLoaderEntry()
	   org.freedesktop.login1(5)

       CanRebootToBootLoaderMenu()
	   org.freedesktop.login1(5)

       CanRebootToFirmwareSetup()
	   org.freedesktop.login1(5)

       CanSuspend()
	   org.freedesktop.login1(5)

       CanSuspendThenHibernate()
	   org.freedesktop.login1(5)

       Cancel()
	   org.freedesktop.import1(5), org.freedesktop.systemd1(5)

       CancelJob()
	   org.freedesktop.systemd1(5)

       CancelScheduledShutdown()
	   org.freedesktop.login1(5)

       CancelTransfer()
	   org.freedesktop.import1(5)

       ChangePassword()
	   org.freedesktop.home1(5)

       ChangePasswordHome()
	   org.freedesktop.home1(5)

       Clean()
	   org.freedesktop.systemd1(5)

       CleanPool()
	   org.freedesktop.machine1(5)

       CleanUnit()
	   org.freedesktop.systemd1(5)

       ClearJobs()
	   org.freedesktop.systemd1(5)

       CloneImage()
	   org.freedesktop.machine1(5)

       CopyFrom()
	   org.freedesktop.machine1(5)

       CopyFromMachine()
	   org.freedesktop.machine1(5)

       CopyFromMachineWithFlags()
	   org.freedesktop.machine1(5)

       CopyFromWithFlags()
	   org.freedesktop.machine1(5)

       CopyTo()
	   org.freedesktop.machine1(5)

       CopyToMachine()
	   org.freedesktop.machine1(5)

       CopyToMachineWithFlags()
	   org.freedesktop.machine1(5)

       CopyToWithFlags()
	   org.freedesktop.machine1(5)

       CreateHome()
	   org.freedesktop.home1(5)

       CreateMachine()
	   org.freedesktop.machine1(5)

       CreateMachineWithNetwork()
	   org.freedesktop.machine1(5)

       CreateSession()
	   org.freedesktop.login1(5)

       CreateSessionWithPIDFD()
	   org.freedesktop.login1(5)

       Deactivate()
	   org.freedesktop.home1(5)

       DeactivateAllHomes()
	   org.freedesktop.home1(5)

       DeactivateHome()
	   org.freedesktop.home1(5)

       Describe()
	   org.freedesktop.hostname1(5), org.freedesktop.network1(5)

       DescribeLink()
	   org.freedesktop.network1(5)

       Detach()
	   org.freedesktop.portable1(5)

       DetachImage()
	   org.freedesktop.portable1(5)

       DetachImageWithExtensions()
	   org.freedesktop.portable1(5)

       DetachWithExtensions()
	   org.freedesktop.portable1(5)

       DisableUnitFiles()
	   org.freedesktop.systemd1(5)

       DisableUnitFilesWithFlags()
	   org.freedesktop.systemd1(5)

       DisableUnitFilesWithFlagsAndInstallInfo()
	   org.freedesktop.systemd1(5)

       Dump()
	   org.freedesktop.systemd1(5)

       DumpByFileDescriptor()
	   org.freedesktop.oom1(5), org.freedesktop.systemd1(5)

       DumpFileDescriptorStore()
	   org.freedesktop.systemd1(5)

       DumpUnitFileDescriptorStore()
	   org.freedesktop.systemd1(5)

       DumpUnitsMatchingPatterns()
	   org.freedesktop.systemd1(5)

       DumpUnitsMatchingPatternsByFileDescriptor()
	   org.freedesktop.systemd1(5)

       EnableUnitFiles()
	   org.freedesktop.systemd1(5)

       EnableUnitFilesWithFlags()
	   org.freedesktop.systemd1(5)

       EnqueueJob()
	   org.freedesktop.systemd1(5)

       EnqueueMarkedJobs()
	   org.freedesktop.systemd1(5)

       EnqueueUnitJob()
	   org.freedesktop.systemd1(5)

       Exit()
	   org.freedesktop.systemd1(5)

       ExportRaw()
	   org.freedesktop.import1(5)

       ExportTar()
	   org.freedesktop.import1(5)

       Fixate()
	   org.freedesktop.home1(5)

       FixateHome()
	   org.freedesktop.home1(5)

       FlushCaches()
	   org.freedesktop.resolve1(5)

       FlushDevices()
	   org.freedesktop.login1(5)

       ForceRenew()
	   org.freedesktop.network1(5)

       ForceRenewLink()
	   org.freedesktop.network1(5)

       Freeze()
	   org.freedesktop.systemd1(5)

       FreezeUnit()
	   org.freedesktop.systemd1(5)

       GetAddresses()
	   org.freedesktop.machine1(5)

       GetAfter()
	   org.freedesktop.systemd1(5)

       GetBefore()
	   org.freedesktop.systemd1(5)

       GetDefaultTarget()
	   org.freedesktop.systemd1(5)

       GetDynamicUsers()
	   org.freedesktop.systemd1(5)

       GetHardwareSerial()
	   org.freedesktop.hostname1(5)

       GetHomeByName()
	   org.freedesktop.home1(5)

       GetHomeByUID()
	   org.freedesktop.home1(5)

       GetImage()
	   org.freedesktop.machine1(5), org.freedesktop.portable1(5)

       GetImageHostname()
	   org.freedesktop.machine1(5)

       GetImageMachineID()
	   org.freedesktop.machine1(5)

       GetImageMachineInfo()
	   org.freedesktop.machine1(5)

       GetImageMetadata()
	   org.freedesktop.portable1(5)

       GetImageMetadataWithExtensions()
	   org.freedesktop.portable1(5)

       GetImageOSRelease()
	   org.freedesktop.machine1(5), org.freedesktop.portable1(5)

       GetImageState()
	   org.freedesktop.portable1(5)

       GetImageStateWithExtensions()
	   org.freedesktop.portable1(5)

       GetJob()
	   org.freedesktop.systemd1(5)

       GetJobAfter()
	   org.freedesktop.systemd1(5)

       GetJobBefore()
	   org.freedesktop.systemd1(5)

       GetLink()
	   org.freedesktop.resolve1(5)

       GetLinkByIndex()
	   org.freedesktop.network1(5)

       GetLinkByName()
	   org.freedesktop.network1(5)

       GetMachine()
	   org.freedesktop.machine1(5)

       GetMachineAddresses()
	   org.freedesktop.machine1(5)

       GetMachineByPID()
	   org.freedesktop.machine1(5)

       GetMachineOSRelease()
	   org.freedesktop.machine1(5)

       GetMachineUIDShift()
	   org.freedesktop.machine1(5)

       GetMetadata()
	   org.freedesktop.portable1(5)

       GetMetadataWithExtensions()
	   org.freedesktop.portable1(5)

       GetOSRelease()
	   org.freedesktop.machine1(5), org.freedesktop.portable1(5)

       GetProcesses()
	   org.freedesktop.systemd1(5)

       GetProductUUID()
	   org.freedesktop.hostname1(5)

       GetSeat()
	   org.freedesktop.login1(5)

       GetSession()
	   org.freedesktop.login1(5)

       GetSessionByPID()
	   org.freedesktop.login1(5)

       GetState()
	   org.freedesktop.portable1(5)

       GetStateWithExtensions()
	   org.freedesktop.portable1(5)

       GetUIDShift()
	   org.freedesktop.machine1(5)

       GetUnit()
	   org.freedesktop.systemd1(5)

       GetUnitByControlGroup()
	   org.freedesktop.systemd1(5)

       GetUnitByInvocationID()
	   org.freedesktop.systemd1(5)

       GetUnitByPID()
	   org.freedesktop.systemd1(5)

       GetUnitByPIDFD()
	   org.freedesktop.systemd1(5)

       GetUnitFileLinks()
	   org.freedesktop.systemd1(5)

       GetUnitFileState()
	   org.freedesktop.systemd1(5)

       GetUnitProcesses()
	   org.freedesktop.systemd1(5)

       GetUser()
	   org.freedesktop.login1(5)

       GetUserByPID()
	   org.freedesktop.login1(5)

       GetUserRecordByName()
	   org.freedesktop.home1(5)

       GetUserRecordByUID()
	   org.freedesktop.home1(5)

       Halt()
	   org.freedesktop.login1(5), org.freedesktop.systemd1(5)

       HaltWithFlags()
	   org.freedesktop.login1(5)

       Hibernate()
	   org.freedesktop.login1(5)

       HibernateWithFlags()
	   org.freedesktop.login1(5)

       HybridSleep()
	   org.freedesktop.login1(5)

       HybridSleepWithFlags()
	   org.freedesktop.login1(5)

       ImportFileSystem()
	   org.freedesktop.import1(5)

       ImportRaw()
	   org.freedesktop.import1(5)

       ImportTar()
	   org.freedesktop.import1(5)

       Inhibit()
	   org.freedesktop.login1(5)

       KExec()
	   org.freedesktop.systemd1(5)

       Kill()
	   org.freedesktop.login1(5), org.freedesktop.machine1(5), org.freedesktop.systemd1(5)

       KillMachine()
	   org.freedesktop.machine1(5)

       KillSession()
	   org.freedesktop.login1(5)

       KillUnit()
	   org.freedesktop.systemd1(5)

       KillUser()
	   org.freedesktop.login1(5)

       LinkUnitFiles()
	   org.freedesktop.systemd1(5)

       ListHomes()
	   org.freedesktop.home1(5)

       ListImages()
	   org.freedesktop.machine1(5), org.freedesktop.portable1(5)

       ListInhibitors()
	   org.freedesktop.login1(5)

       ListJobs()
	   org.freedesktop.systemd1(5)

       ListLinks()
	   org.freedesktop.network1(5)

       ListMachines()
	   org.freedesktop.machine1(5)

       ListSeats()
	   org.freedesktop.login1(5)

       ListSessions()
	   org.freedesktop.login1(5)

       ListTimezones()
	   org.freedesktop.timedate1(5)

       ListTransfers()
	   org.freedesktop.import1(5)

       ListUnitFiles()
	   org.freedesktop.systemd1(5)

       ListUnitFilesByPatterns()
	   org.freedesktop.systemd1(5)

       ListUnits()
	   org.freedesktop.systemd1(5)

       ListUnitsByNames()
	   org.freedesktop.systemd1(5)

       ListUnitsByPatterns()
	   org.freedesktop.systemd1(5)

       ListUnitsFiltered()
	   org.freedesktop.systemd1(5)

       ListUsers()
	   org.freedesktop.login1(5)

       LoadUnit()
	   org.freedesktop.systemd1(5)

       Lock()
	   org.freedesktop.home1(5), org.freedesktop.login1(5)

       LockAllHomes()
	   org.freedesktop.home1(5)

       LockHome()
	   org.freedesktop.home1(5)

       LockSession()
	   org.freedesktop.login1(5)

       LockSessions()
	   org.freedesktop.login1(5)

       LookupDynamicUserByName()
	   org.freedesktop.systemd1(5)

       LookupDynamicUserByUID()
	   org.freedesktop.systemd1(5)

       MapFromMachineGroup()
	   org.freedesktop.machine1(5)

       MapFromMachineUser()
	   org.freedesktop.machine1(5)

       MapToMachineGroup()
	   org.freedesktop.machine1(5)

       MapToMachineUser()
	   org.freedesktop.machine1(5)

       MarkImageReadOnly()
	   org.freedesktop.machine1(5), org.freedesktop.portable1(5)

       MarkReadOnly()
	   org.freedesktop.portable1(5)

       MaskUnitFiles()
	   org.freedesktop.systemd1(5)

       MountImage()
	   org.freedesktop.systemd1(5)

       MountImageUnit()
	   org.freedesktop.systemd1(5)

       OpenLogin()
	   org.freedesktop.machine1(5)

       OpenMachineLogin()
	   org.freedesktop.machine1(5)

       OpenMachinePTY()
	   org.freedesktop.machine1(5)

       OpenMachineRootDirectory()
	   org.freedesktop.machine1(5)

       OpenMachineShell()
	   org.freedesktop.machine1(5)

       OpenPTY()
	   org.freedesktop.machine1(5)

       OpenRootDirectory()
	   org.freedesktop.machine1(5)

       OpenShell()
	   org.freedesktop.machine1(5)

       PauseDeviceComplete()
	   org.freedesktop.login1(5)

       PowerOff()
	   org.freedesktop.login1(5), org.freedesktop.systemd1(5)

       PowerOffWithFlags()
	   org.freedesktop.login1(5)

       PresetAllUnitFiles()
	   org.freedesktop.systemd1(5)

       PresetUnitFiles()
	   org.freedesktop.systemd1(5)

       PresetUnitFilesWithMode()
	   org.freedesktop.systemd1(5)

       PullRaw()
	   org.freedesktop.import1(5)

       PullTar()
	   org.freedesktop.import1(5)

       QueueSignal()
	   org.freedesktop.systemd1(5)

       QueueSignalUnit()
	   org.freedesktop.systemd1(5)

       Realize()
	   org.freedesktop.home1(5)

       RealizeHome()
	   org.freedesktop.home1(5)

       Reattach()
	   org.freedesktop.portable1(5)

       ReattachImage()
	   org.freedesktop.portable1(5)

       ReattachImageWithExtensions()
	   org.freedesktop.portable1(5)

       ReattachWithExtensions()
	   org.freedesktop.portable1(5)

       Rebalance()
	   org.freedesktop.home1(5)

       Reboot()
	   org.freedesktop.login1(5), org.freedesktop.systemd1(5)

       RebootWithFlags()
	   org.freedesktop.login1(5)

       Reconfigure()
	   org.freedesktop.network1(5)

       ReconfigureLink()
	   org.freedesktop.network1(5)

       ReenableUnitFiles()
	   org.freedesktop.systemd1(5)

       Reexecute()
	   org.freedesktop.systemd1(5)

       Ref()
	   org.freedesktop.home1(5), org.freedesktop.systemd1(5)

       RefHome()
	   org.freedesktop.home1(5)

       RefUnit()
	   org.freedesktop.systemd1(5)

       RegisterHome()
	   org.freedesktop.home1(5)

       RegisterMachine()
	   org.freedesktop.machine1(5)

       RegisterMachineWithNetwork()
	   org.freedesktop.machine1(5)

       RegisterService()
	   org.freedesktop.resolve1(5)

       Release()
	   org.freedesktop.home1(5)

       ReleaseControl()
	   org.freedesktop.login1(5)

       ReleaseDevice()
	   org.freedesktop.login1(5)

       ReleaseHome()
	   org.freedesktop.home1(5)

       ReleaseSession()
	   org.freedesktop.login1(5)

       Reload()
	   org.freedesktop.network1(5), org.freedesktop.systemd1(5)

       ReloadOrRestart()
	   org.freedesktop.systemd1(5)

       ReloadOrRestartUnit()
	   org.freedesktop.systemd1(5)

       ReloadOrTryRestart()
	   org.freedesktop.systemd1(5)

       ReloadOrTryRestartUnit()
	   org.freedesktop.systemd1(5)

       ReloadUnit()
	   org.freedesktop.systemd1(5)

       Remove()
	   org.freedesktop.home1(5), org.freedesktop.portable1(5)

       RemoveHome()
	   org.freedesktop.home1(5)

       RemoveImage()
	   org.freedesktop.machine1(5), org.freedesktop.portable1(5)

       RenameImage()
	   org.freedesktop.machine1(5)

       Renew()
	   org.freedesktop.network1(5)

       RenewLink()
	   org.freedesktop.network1(5)

       ResetFailed()
	   org.freedesktop.systemd1(5)

       ResetFailedUnit()
	   org.freedesktop.systemd1(5)

       ResetServerFeatures()
	   org.freedesktop.resolve1(5)

       ResetStatistics()
	   org.freedesktop.resolve1(5)

       Resize()
	   org.freedesktop.home1(5)

       ResizeHome()
	   org.freedesktop.home1(5)

       ResolveAddress()
	   org.freedesktop.resolve1(5)

       ResolveHostname()
	   org.freedesktop.resolve1(5)

       ResolveRecord()
	   org.freedesktop.resolve1(5)

       ResolveService()
	   org.freedesktop.resolve1(5)

       Restart()
	   org.freedesktop.systemd1(5)

       RestartUnit()
	   org.freedesktop.systemd1(5)

       Revert()
	   org.freedesktop.resolve1(5)

       RevertDNS()
	   org.freedesktop.network1(5)

       RevertLink()
	   org.freedesktop.resolve1(5)

       RevertLinkDNS()
	   org.freedesktop.network1(5)

       RevertLinkNTP()
	   org.freedesktop.network1(5)

       RevertNTP()
	   org.freedesktop.network1(5)

       RevertUnitFiles()
	   org.freedesktop.systemd1(5)

       ScheduleShutdown()
	   org.freedesktop.login1(5)

       SetBrightness()
	   org.freedesktop.login1(5)

       SetChassis()
	   org.freedesktop.hostname1(5)

       SetDNS()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetDNSEx()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetDNSOverTLS()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetDNSSEC()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetDNSSECNegativeTrustAnchors()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetDefaultRoute()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetDefaultTarget()
	   org.freedesktop.systemd1(5)

       SetDeployment()
	   org.freedesktop.hostname1(5)

       SetDisplay()
	   org.freedesktop.login1(5)

       SetDomains()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetEnvironment()
	   org.freedesktop.systemd1(5)

       SetExitCode()
	   org.freedesktop.systemd1(5)

       SetHostname()
	   org.freedesktop.hostname1(5)

       SetIconName()
	   org.freedesktop.hostname1(5)

       SetIdleHint()
	   org.freedesktop.login1(5)

       SetImageLimit()
	   org.freedesktop.machine1(5), org.freedesktop.portable1(5)

       SetLLMNR()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetLimit()
	   org.freedesktop.portable1(5)

       SetLinkDNS()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetLinkDNSEx()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetLinkDNSOverTLS()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetLinkDNSSEC()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetLinkDNSSECNegativeTrustAnchors()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetLinkDefaultRoute()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetLinkDomains()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetLinkLLMNR()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetLinkMulticastDNS()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetLinkNTP()
	   org.freedesktop.network1(5)

       SetLocalRTC()
	   org.freedesktop.timedate1(5)

       SetLocale()
	   org.freedesktop.locale1(5)

       SetLocation()
	   org.freedesktop.hostname1(5)

       SetLockedHint()
	   org.freedesktop.login1(5)

       SetMulticastDNS()
	   org.freedesktop.network1(5), org.freedesktop.resolve1(5)

       SetNTP()
	   org.freedesktop.network1(5), org.freedesktop.timedate1(5)

       SetPoolLimit()
	   org.freedesktop.machine1(5), org.freedesktop.portable1(5)

       SetPrettyHostname()
	   org.freedesktop.hostname1(5)

       SetProperties()
	   org.freedesktop.systemd1(5)

       SetRebootParameter()
	   org.freedesktop.login1(5)

       SetRebootToBootLoaderEntry()
	   org.freedesktop.login1(5)

       SetRebootToBootLoaderMenu()
	   org.freedesktop.login1(5)

       SetRebootToFirmwareSetup()
	   org.freedesktop.login1(5)

       SetShowStatus()
	   org.freedesktop.systemd1(5)

       SetStaticHostname()
	   org.freedesktop.hostname1(5)

       SetTTY()
	   org.freedesktop.login1(5)

       SetTime()
	   org.freedesktop.timedate1(5)

       SetTimezone()
	   org.freedesktop.timedate1(5)

       SetType()
	   org.freedesktop.login1(5)

       SetUnitProperties()
	   org.freedesktop.systemd1(5)

       SetUserLinger()
	   org.freedesktop.login1(5)

       SetVConsoleKeyboard()
	   org.freedesktop.locale1(5)

       SetWallMessage()
	   org.freedesktop.login1(5)

       SetX11Keyboard()
	   org.freedesktop.locale1(5)

       SoftReboot()
	   org.freedesktop.systemd1(5)

       Start()
	   org.freedesktop.systemd1(5)

       StartTransientUnit()
	   org.freedesktop.systemd1(5)

       StartUnit()
	   org.freedesktop.systemd1(5)

       StartUnitReplace()
	   org.freedesktop.systemd1(5)

       StartUnitWithFlags()
	   org.freedesktop.systemd1(5)

       Stop()
	   org.freedesktop.systemd1(5)

       StopUnit()
	   org.freedesktop.systemd1(5)

       Subscribe()
	   org.freedesktop.systemd1(5)

       Suspend()
	   org.freedesktop.login1(5)

       SuspendThenHibernate()
	   org.freedesktop.login1(5)

       SuspendThenHibernateWithFlags()
	   org.freedesktop.login1(5)

       SuspendWithFlags()
	   org.freedesktop.login1(5)

       SwitchRoot()
	   org.freedesktop.systemd1(5)

       SwitchTo()
	   org.freedesktop.login1(5)

       SwitchToNext()
	   org.freedesktop.login1(5)

       SwitchToPrevious()
	   org.freedesktop.login1(5)

       TakeControl()
	   org.freedesktop.login1(5)

       TakeDevice()
	   org.freedesktop.login1(5)

       Terminate()
	   org.freedesktop.login1(5), org.freedesktop.machine1(5)

       TerminateMachine()
	   org.freedesktop.machine1(5)

       TerminateSeat()
	   org.freedesktop.login1(5)

       TerminateSession()
	   org.freedesktop.login1(5)

       TerminateUser()
	   org.freedesktop.login1(5)

       Thaw()
	   org.freedesktop.systemd1(5)

       ThawUnit()
	   org.freedesktop.systemd1(5)

       TryRestart()
	   org.freedesktop.systemd1(5)

       TryRestartUnit()
	   org.freedesktop.systemd1(5)

       Unlock()
	   org.freedesktop.home1(5), org.freedesktop.login1(5)

       UnlockHome()
	   org.freedesktop.home1(5)

       UnlockSession()
	   org.freedesktop.login1(5)

       UnlockSessions()
	   org.freedesktop.login1(5)

       UnmaskUnitFiles()
	   org.freedesktop.systemd1(5)

       Unref()
	   org.freedesktop.systemd1(5)

       UnrefUnit()
	   org.freedesktop.systemd1(5)

       Unregister()
	   org.freedesktop.home1(5)

       UnregisterHome()
	   org.freedesktop.home1(5)

       UnregisterMachine()
	   org.freedesktop.machine1(5)

       UnregisterService()
	   org.freedesktop.resolve1(5)

       UnsetAndSetEnvironment()
	   org.freedesktop.systemd1(5)

       UnsetEnvironment()
	   org.freedesktop.systemd1(5)

       Unsubscribe()
	   org.freedesktop.systemd1(5)

       Update()
	   org.freedesktop.home1(5)

       UpdateHome()
	   org.freedesktop.home1(5)

D-BUS PROPERTIES
       Properties exposed in the D-Bus interface.

       Accept
	   org.freedesktop.systemd1(5)

       AccessSELinuxContext
	   org.freedesktop.systemd1(5)

       AccuracyUSec
	   org.freedesktop.systemd1(5)

       ActivationDetails
	   org.freedesktop.systemd1(5)

       Active
	   org.freedesktop.login1(5)

       ActiveEnterTimestamp
	   org.freedesktop.systemd1(5)

       ActiveEnterTimestampMonotonic
	   org.freedesktop.systemd1(5)

       ActiveExitTimestamp
	   org.freedesktop.systemd1(5)

       ActiveExitTimestampMonotonic
	   org.freedesktop.systemd1(5)

       ActiveSession
	   org.freedesktop.login1(5)

       ActiveState
	   org.freedesktop.systemd1(5)

       AddressState
	   org.freedesktop.network1(5)

       AdministrativeState
	   org.freedesktop.network1(5)

       After
	   org.freedesktop.systemd1(5)

       AllowIsolate
	   org.freedesktop.systemd1(5)

       AllowedCPUs
	   org.freedesktop.systemd1(5)

       AllowedMemoryNodes
	   org.freedesktop.systemd1(5)

       AmbientCapabilities
	   org.freedesktop.systemd1(5)

       AppArmorProfile
	   org.freedesktop.systemd1(5)

       Architecture
	   org.freedesktop.systemd1(5)

       AssertResult
	   org.freedesktop.systemd1(5)

       AssertTimestamp
	   org.freedesktop.systemd1(5)

       AssertTimestampMonotonic
	   org.freedesktop.systemd1(5)

       Asserts
	   org.freedesktop.systemd1(5)

       Audit
	   org.freedesktop.login1(5)

       AutoLogin
	   org.freedesktop.home1(5)

       BPFProgram
	   org.freedesktop.systemd1(5)

       Backlog
	   org.freedesktop.systemd1(5)

       Before
	   org.freedesktop.systemd1(5)

       BindIPv6Only
	   org.freedesktop.systemd1(5)

       BindPaths
	   org.freedesktop.systemd1(5)

       BindReadOnlyPaths
	   org.freedesktop.systemd1(5)

       BindToDevice
	   org.freedesktop.systemd1(5)

       BindsTo
	   org.freedesktop.systemd1(5)

       BitRates
	   org.freedesktop.network1(5)

       BlockIOAccounting
	   org.freedesktop.systemd1(5)

       BlockIODeviceWeight
	   org.freedesktop.systemd1(5)

       BlockIOReadBandwidth
	   org.freedesktop.systemd1(5)

       BlockIOWeight
	   org.freedesktop.systemd1(5)

       BlockIOWriteBandwidth
	   org.freedesktop.systemd1(5)

       BlockInhibited
	   org.freedesktop.login1(5)

       BootID
	   org.freedesktop.hostname1(5)

       BootLoaderEntries
	   org.freedesktop.login1(5)

       BoundBy
	   org.freedesktop.systemd1(5)

       Broadcast
	   org.freedesktop.systemd1(5)

       BusName
	   org.freedesktop.systemd1(5)

       CPUAccounting
	   org.freedesktop.systemd1(5)

       CPUAffinity
	   org.freedesktop.systemd1(5)

       CPUAffinityFromNUMA
	   org.freedesktop.systemd1(5)

       CPUQuotaPerSecUSec
	   org.freedesktop.systemd1(5)

       CPUQuotaPeriodUSec
	   org.freedesktop.systemd1(5)

       CPUSchedulingPolicy
	   org.freedesktop.systemd1(5)

       CPUSchedulingPriority
	   org.freedesktop.systemd1(5)

       CPUSchedulingResetOnFork
	   org.freedesktop.systemd1(5)

       CPUShares
	   org.freedesktop.systemd1(5)

       CPUUsageNSec
	   org.freedesktop.systemd1(5)

       CPUWeight
	   org.freedesktop.systemd1(5)

       CacheDirectory
	   org.freedesktop.systemd1(5)

       CacheDirectoryMode
	   org.freedesktop.systemd1(5)

       CacheDirectorySymlink
	   org.freedesktop.systemd1(5)

       CacheStatistics
	   org.freedesktop.resolve1(5)

       CanClean
	   org.freedesktop.systemd1(5)

       CanFreeze
	   org.freedesktop.systemd1(5)

       CanGraphical
	   org.freedesktop.login1(5)

       CanIsolate
	   org.freedesktop.systemd1(5)

       CanNTP
	   org.freedesktop.timedate1(5)

       CanReload
	   org.freedesktop.systemd1(5)

       CanStart
	   org.freedesktop.systemd1(5)

       CanStop
	   org.freedesktop.systemd1(5)

       CanTTY
	   org.freedesktop.login1(5)

       CapabilityBoundingSet
	   org.freedesktop.systemd1(5)

       CarrierState
	   org.freedesktop.network1(5)

       Chassis
	   org.freedesktop.hostname1(5)

       Class
	   org.freedesktop.login1(5), org.freedesktop.machine1(5)

       CleanResult
	   org.freedesktop.systemd1(5)

       CollectMode
	   org.freedesktop.systemd1(5)

       ConditionResult
	   org.freedesktop.systemd1(5)

       ConditionTimestamp
	   org.freedesktop.systemd1(5)

       ConditionTimestampMonotonic
	   org.freedesktop.systemd1(5)

       Conditions
	   org.freedesktop.systemd1(5)

       ConfidentialVirtualization
	   org.freedesktop.systemd1(5)

       ConfigurationDirectory
	   org.freedesktop.systemd1(5)

       ConfigurationDirectoryMode
	   org.freedesktop.systemd1(5)

       ConfirmSpawn
	   org.freedesktop.systemd1(5)

       ConflictedBy
	   org.freedesktop.systemd1(5)

       Conflicts
	   org.freedesktop.systemd1(5)

       ConsistsOf
	   org.freedesktop.systemd1(5)

       ControlGroup
	   org.freedesktop.systemd1(5)

       ControlGroupId
	   org.freedesktop.systemd1(5)

       ControlPID
	   org.freedesktop.systemd1(5)

       Controller
	   org.freedesktop.systemd1(5)

       CoredumpFilter
	   org.freedesktop.systemd1(5)

       CoredumpReceive
	   org.freedesktop.systemd1(5)

       CreationTimestamp
	   org.freedesktop.portable1(5)

       CtrlAltDelBurstAction
	   org.freedesktop.systemd1(5)

       CurrentDNSServer
	   org.freedesktop.resolve1(5)

       CurrentDNSServerEx
	   org.freedesktop.resolve1(5)

       DNS
	   org.freedesktop.resolve1(5)

       DNSEx
	   org.freedesktop.resolve1(5)

       DNSOverTLS
	   org.freedesktop.resolve1(5)

       DNSSEC
	   org.freedesktop.resolve1(5)

       DNSSECNegativeTrustAnchors
	   org.freedesktop.resolve1(5)

       DNSSECStatistics
	   org.freedesktop.resolve1(5)

       DNSSECSupported
	   org.freedesktop.resolve1(5)

       DNSStubListener
	   org.freedesktop.resolve1(5)

       DefaultBlockIOAccounting
	   org.freedesktop.systemd1(5)

       DefaultCPUAccounting
	   org.freedesktop.systemd1(5)

       DefaultDependencies
	   org.freedesktop.systemd1(5)

       DefaultDeviceTimeoutUSec
	   org.freedesktop.systemd1(5)

       DefaultHostname
	   org.freedesktop.hostname1(5)

       DefaultIOAccounting
	   org.freedesktop.systemd1(5)

       DefaultIPAccounting
	   org.freedesktop.systemd1(5)

       DefaultLimitAS
	   org.freedesktop.systemd1(5)

       DefaultLimitASSoft
	   org.freedesktop.systemd1(5)

       DefaultLimitCORE
	   org.freedesktop.systemd1(5)

       DefaultLimitCORESoft
	   org.freedesktop.systemd1(5)

       DefaultLimitCPU
	   org.freedesktop.systemd1(5)

       DefaultLimitCPUSoft
	   org.freedesktop.systemd1(5)

       DefaultLimitDATA
	   org.freedesktop.systemd1(5)

       DefaultLimitDATASoft
	   org.freedesktop.systemd1(5)

       DefaultLimitFSIZE
	   org.freedesktop.systemd1(5)

       DefaultLimitFSIZESoft
	   org.freedesktop.systemd1(5)

       DefaultLimitLOCKS
	   org.freedesktop.systemd1(5)

       DefaultLimitLOCKSSoft
	   org.freedesktop.systemd1(5)

       DefaultLimitMEMLOCK
	   org.freedesktop.systemd1(5)

       DefaultLimitMEMLOCKSoft
	   org.freedesktop.systemd1(5)

       DefaultLimitMSGQUEUE
	   org.freedesktop.systemd1(5)

       DefaultLimitMSGQUEUESoft
	   org.freedesktop.systemd1(5)

       DefaultLimitNICE
	   org.freedesktop.systemd1(5)

       DefaultLimitNICESoft
	   org.freedesktop.systemd1(5)

       DefaultLimitNOFILE
	   org.freedesktop.systemd1(5)

       DefaultLimitNOFILESoft
	   org.freedesktop.systemd1(5)

       DefaultLimitNPROC
	   org.freedesktop.systemd1(5)

       DefaultLimitNPROCSoft
	   org.freedesktop.systemd1(5)

       DefaultLimitRSS
	   org.freedesktop.systemd1(5)

       DefaultLimitRSSSoft
	   org.freedesktop.systemd1(5)

       DefaultLimitRTPRIO
	   org.freedesktop.systemd1(5)

       DefaultLimitRTPRIOSoft
	   org.freedesktop.systemd1(5)

       DefaultLimitRTTIME
	   org.freedesktop.systemd1(5)

       DefaultLimitRTTIMESoft
	   org.freedesktop.systemd1(5)

       DefaultLimitSIGPENDING
	   org.freedesktop.systemd1(5)

       DefaultLimitSIGPENDINGSoft
	   org.freedesktop.systemd1(5)

       DefaultLimitSTACK
	   org.freedesktop.systemd1(5)

       DefaultLimitSTACKSoft
	   org.freedesktop.systemd1(5)

       DefaultMemoryAccounting
	   org.freedesktop.systemd1(5)

       DefaultMemoryLow
	   org.freedesktop.systemd1(5)

       DefaultMemoryMin
	   org.freedesktop.systemd1(5)

       DefaultMemoryPressureThresholdUSec
	   org.freedesktop.systemd1(5)

       DefaultMemoryPressureWatch
	   org.freedesktop.systemd1(5)

       DefaultOOMPolicy
	   org.freedesktop.systemd1(5)

       DefaultOOMScoreAdjust
	   org.freedesktop.systemd1(5)

       DefaultRestartUSec
	   org.freedesktop.systemd1(5)

       DefaultRoute
	   org.freedesktop.resolve1(5)

       DefaultStandardError
	   org.freedesktop.systemd1(5)

       DefaultStandardOutput
	   org.freedesktop.systemd1(5)

       DefaultStartLimitBurst
	   org.freedesktop.systemd1(5)

       DefaultStartLimitIntervalUSec
	   org.freedesktop.systemd1(5)

       DefaultStartupMemoryLow
	   org.freedesktop.systemd1(5)

       DefaultTasksAccounting
	   org.freedesktop.systemd1(5)

       DefaultTasksMax
	   org.freedesktop.systemd1(5)

       DefaultTimeoutAbortUSec
	   org.freedesktop.systemd1(5)

       DefaultTimeoutStartUSec
	   org.freedesktop.systemd1(5)

       DefaultTimeoutStopUSec
	   org.freedesktop.systemd1(5)

       DefaultTimerAccuracyUSec
	   org.freedesktop.systemd1(5)

       DeferAcceptUSec
	   org.freedesktop.systemd1(5)

       DelayInhibited
	   org.freedesktop.login1(5)

       Delegate
	   org.freedesktop.systemd1(5)

       DelegateControllers
	   org.freedesktop.systemd1(5)

       DelegateSubgroup
	   org.freedesktop.systemd1(5)

       Deployment
	   org.freedesktop.hostname1(5)

       Description
	   org.freedesktop.network1(5), org.freedesktop.systemd1(5)

       Desktop
	   org.freedesktop.login1(5)

       DeviceAllow
	   org.freedesktop.systemd1(5)

       DevicePolicy
	   org.freedesktop.systemd1(5)

       DirectoryMode
	   org.freedesktop.systemd1(5)

       DisableControllers
	   org.freedesktop.systemd1(5)

       Display
	   org.freedesktop.login1(5)

       Docked
	   org.freedesktop.login1(5)

       Documentation
	   org.freedesktop.systemd1(5)

       Domains
	   org.freedesktop.resolve1(5)

       DropInPaths
	   org.freedesktop.systemd1(5)

       DynamicUser
	   org.freedesktop.systemd1(5)

       EffectiveCPUs
	   org.freedesktop.systemd1(5)

       EffectiveMemoryNodes
	   org.freedesktop.systemd1(5)

       EnableWallMessages
	   org.freedesktop.login1(5)

       Environment
	   org.freedesktop.systemd1(5)

       EnvironmentFiles
	   org.freedesktop.systemd1(5)

       ExecActivate
	   org.freedesktop.systemd1(5)

       ExecCondition
	   org.freedesktop.systemd1(5)

       ExecConditionEx
	   org.freedesktop.systemd1(5)

       ExecDeactivate
	   org.freedesktop.systemd1(5)

       ExecMainCode
	   org.freedesktop.systemd1(5)

       ExecMainExitTimestamp
	   org.freedesktop.systemd1(5)

       ExecMainExitTimestampMonotonic
	   org.freedesktop.systemd1(5)

       ExecMainPID
	   org.freedesktop.systemd1(5)

       ExecMainStartTimestamp
	   org.freedesktop.systemd1(5)

       ExecMainStartTimestampMonotonic
	   org.freedesktop.systemd1(5)

       ExecMainStatus
	   org.freedesktop.systemd1(5)

       ExecMount
	   org.freedesktop.systemd1(5)

       ExecPaths
	   org.freedesktop.systemd1(5)

       ExecReload
	   org.freedesktop.systemd1(5)

       ExecReloadEx
	   org.freedesktop.systemd1(5)

       ExecRemount
	   org.freedesktop.systemd1(5)

       ExecSearchPath
	   org.freedesktop.systemd1(5)

       ExecStart
	   org.freedesktop.systemd1(5)

       ExecStartEx
	   org.freedesktop.systemd1(5)

       ExecStartPost
	   org.freedesktop.systemd1(5)

       ExecStartPostEx
	   org.freedesktop.systemd1(5)

       ExecStartPre
	   org.freedesktop.systemd1(5)

       ExecStartPreEx
	   org.freedesktop.systemd1(5)

       ExecStop
	   org.freedesktop.systemd1(5)

       ExecStopEx
	   org.freedesktop.systemd1(5)

       ExecStopPost
	   org.freedesktop.systemd1(5)

       ExecStopPostEx
	   org.freedesktop.systemd1(5)

       ExecStopPre
	   org.freedesktop.systemd1(5)

       ExecUnmount
	   org.freedesktop.systemd1(5)

       ExitCode
	   org.freedesktop.systemd1(5)

       ExitType
	   org.freedesktop.systemd1(5)

       ExtensionDirectories
	   org.freedesktop.systemd1(5)

       ExtensionImagePolicy
	   org.freedesktop.systemd1(5)

       ExtensionImages
	   org.freedesktop.systemd1(5)

       ExtraOptions
	   org.freedesktop.systemd1(5)

       FailureAction
	   org.freedesktop.systemd1(5)

       FailureActionExitStatus
	   org.freedesktop.systemd1(5)

       FallbackDNS
	   org.freedesktop.resolve1(5)

       FallbackDNSEx
	   org.freedesktop.resolve1(5)

       Features
	   org.freedesktop.systemd1(5)

       FileDescriptorName
	   org.freedesktop.systemd1(5)

       FileDescriptorStoreMax
	   org.freedesktop.systemd1(5)

       FileDescriptorStorePreserve
	   org.freedesktop.systemd1(5)

       FinalKillSignal
	   org.freedesktop.systemd1(5)

       FinishTimestamp
	   org.freedesktop.systemd1(5)

       FinishTimestampMonotonic
	   org.freedesktop.systemd1(5)

       FirmwareDate
	   org.freedesktop.hostname1(5)

       FirmwareTimestamp
	   org.freedesktop.systemd1(5)

       FirmwareTimestampMonotonic
	   org.freedesktop.systemd1(5)

       FirmwareVendor
	   org.freedesktop.hostname1(5)

       FirmwareVersion
	   org.freedesktop.hostname1(5)

       FixedRandomDelay
	   org.freedesktop.systemd1(5)

       FlushPending
	   org.freedesktop.systemd1(5)

       Following
	   org.freedesktop.systemd1(5)

       ForceUnmount
	   org.freedesktop.systemd1(5)

       FragmentPath
	   org.freedesktop.systemd1(5)

       FreeBind
	   org.freedesktop.systemd1(5)

       FreezerState
	   org.freedesktop.systemd1(5)

       GID
	   org.freedesktop.login1(5), org.freedesktop.systemd1(5)

       GeneratorsFinishTimestamp
	   org.freedesktop.systemd1(5)

       GeneratorsFinishTimestampMonotonic
	   org.freedesktop.systemd1(5)

       GeneratorsStartTimestamp
	   org.freedesktop.systemd1(5)

       GeneratorsStartTimestampMonotonic
	   org.freedesktop.systemd1(5)

       Group
	   org.freedesktop.systemd1(5)

       GuessMainPID
	   org.freedesktop.systemd1(5)

       HandleHibernateKey
	   org.freedesktop.login1(5)

       HandleHibernateKeyLongPress
	   org.freedesktop.login1(5)

       HandleLidSwitch
	   org.freedesktop.login1(5)

       HandleLidSwitchDocked
	   org.freedesktop.login1(5)

       HandleLidSwitchExternalPower
	   org.freedesktop.login1(5)

       HandlePowerKey
	   org.freedesktop.login1(5)

       HandlePowerKeyLongPress
	   org.freedesktop.login1(5)

       HandleRebootKey
	   org.freedesktop.login1(5)

       HandleRebootKeyLongPress
	   org.freedesktop.login1(5)

       HandleSuspendKey
	   org.freedesktop.login1(5)

       HandleSuspendKeyLongPress
	   org.freedesktop.login1(5)

       HardwareModel
	   org.freedesktop.hostname1(5)

       HardwareVendor
	   org.freedesktop.hostname1(5)

       HoldoffTimeoutUSec
	   org.freedesktop.login1(5)

       HomeURL
	   org.freedesktop.hostname1(5)

       Hostname
	   org.freedesktop.hostname1(5)

       HostnameSource
	   org.freedesktop.hostname1(5)

       IOAccounting
	   org.freedesktop.systemd1(5)

       IODeviceLatencyTargetUSec
	   org.freedesktop.systemd1(5)

       IODeviceWeight
	   org.freedesktop.systemd1(5)

       IOReadBandwidthMax
	   org.freedesktop.systemd1(5)

       IOReadBytes
	   org.freedesktop.systemd1(5)

       IOReadIOPSMax
	   org.freedesktop.systemd1(5)

       IOReadOperations
	   org.freedesktop.systemd1(5)

       IOSchedulingClass
	   org.freedesktop.systemd1(5)

       IOSchedulingPriority
	   org.freedesktop.systemd1(5)

       IOWeight
	   org.freedesktop.systemd1(5)

       IOWriteBandwidthMax
	   org.freedesktop.systemd1(5)

       IOWriteBytes
	   org.freedesktop.systemd1(5)

       IOWriteIOPSMax
	   org.freedesktop.systemd1(5)

       IOWriteOperations
	   org.freedesktop.systemd1(5)

       IPAccounting
	   org.freedesktop.systemd1(5)

       IPAddressAllow
	   org.freedesktop.systemd1(5)

       IPAddressDeny
	   org.freedesktop.systemd1(5)

       IPCNamespacePath
	   org.freedesktop.systemd1(5)

       IPEgressBytes
	   org.freedesktop.systemd1(5)

       IPEgressFilterPath
	   org.freedesktop.systemd1(5)

       IPEgressPackets
	   org.freedesktop.systemd1(5)

       IPIngressBytes
	   org.freedesktop.systemd1(5)

       IPIngressFilterPath
	   org.freedesktop.systemd1(5)

       IPIngressPackets
	   org.freedesktop.systemd1(5)

       IPTOS
	   org.freedesktop.systemd1(5)

       IPTTL
	   org.freedesktop.systemd1(5)

       IPv4AddressState
	   org.freedesktop.network1(5)

       IPv6AddressState
	   org.freedesktop.network1(5)

       IconName
	   org.freedesktop.hostname1(5)

       Id
	   org.freedesktop.import1(5), org.freedesktop.login1(5), org.freedesktop.machine1(5), org.freedesktop.systemd1(5)

       IdleAction
	   org.freedesktop.login1(5)

       IdleActionUSec
	   org.freedesktop.login1(5)

       IdleHint
	   org.freedesktop.login1(5)

       IdleSinceHint
	   org.freedesktop.login1(5)

       IdleSinceHintMonotonic
	   org.freedesktop.login1(5)

       IgnoreOnIsolate
	   org.freedesktop.systemd1(5)

       IgnoreSIGPIPE
	   org.freedesktop.systemd1(5)

       ImportCredential
	   org.freedesktop.systemd1(5)

       InaccessiblePaths
	   org.freedesktop.systemd1(5)

       InactiveEnterTimestamp
	   org.freedesktop.systemd1(5)

       InactiveEnterTimestampMonotonic
	   org.freedesktop.systemd1(5)

       InactiveExitTimestamp
	   org.freedesktop.systemd1(5)

       InactiveExitTimestampMonotonic
	   org.freedesktop.systemd1(5)

       InhibitDelayMaxUSec
	   org.freedesktop.login1(5)

       InhibitorsMax
	   org.freedesktop.login1(5)

       InitRDGeneratorsFinishTimestamp
	   org.freedesktop.systemd1(5)

       InitRDGeneratorsFinishTimestampMonotonic
	   org.freedesktop.systemd1(5)

       InitRDGeneratorsStartTimestamp
	   org.freedesktop.systemd1(5)

       InitRDGeneratorsStartTimestampMonotonic
	   org.freedesktop.systemd1(5)

       InitRDSecurityFinishTimestamp
	   org.freedesktop.systemd1(5)

       InitRDSecurityFinishTimestampMonotonic
	   org.freedesktop.systemd1(5)

       InitRDSecurityStartTimestamp
	   org.freedesktop.systemd1(5)

       InitRDSecurityStartTimestampMonotonic
	   org.freedesktop.systemd1(5)

       InitRDTimestamp
	   org.freedesktop.systemd1(5)

       InitRDTimestampMonotonic
	   org.freedesktop.systemd1(5)

       InitRDUnitsLoadFinishTimestamp
	   org.freedesktop.systemd1(5)

       InitRDUnitsLoadFinishTimestampMonotonic
	   org.freedesktop.systemd1(5)

       InitRDUnitsLoadStartTimestamp
	   org.freedesktop.systemd1(5)

       InitRDUnitsLoadStartTimestampMonotonic
	   org.freedesktop.systemd1(5)

       InvocationID
	   org.freedesktop.systemd1(5)

       Job
	   org.freedesktop.systemd1(5)

       JobRunningTimeoutUSec
	   org.freedesktop.systemd1(5)

       JobTimeoutAction
	   org.freedesktop.systemd1(5)

       JobTimeoutRebootArgument
	   org.freedesktop.systemd1(5)

       JobTimeoutUSec
	   org.freedesktop.systemd1(5)

       JobType
	   org.freedesktop.systemd1(5)

       JoinsNamespaceOf
	   org.freedesktop.systemd1(5)

       KExecWatchdogUSec
	   org.freedesktop.systemd1(5)

       KeepAlive
	   org.freedesktop.systemd1(5)

       KeepAliveIntervalUSec
	   org.freedesktop.systemd1(5)

       KeepAliveProbes
	   org.freedesktop.systemd1(5)

       KeepAliveTimeUSec
	   org.freedesktop.systemd1(5)

       KernelName
	   org.freedesktop.hostname1(5)

       KernelRelease
	   org.freedesktop.hostname1(5)

       KernelTimestamp
	   org.freedesktop.systemd1(5)

       KernelTimestampMonotonic
	   org.freedesktop.systemd1(5)

       KernelVersion
	   org.freedesktop.hostname1(5)

       KeyringMode
	   org.freedesktop.systemd1(5)

       KillExcludeUsers
	   org.freedesktop.login1(5)

       KillMode
	   org.freedesktop.systemd1(5)

       KillOnlyUsers
	   org.freedesktop.login1(5)

       KillSignal
	   org.freedesktop.systemd1(5)

       KillUserProcesses
	   org.freedesktop.login1(5)

       LLMNR
	   org.freedesktop.resolve1(5)

       LLMNRHostname
	   org.freedesktop.resolve1(5)

       LastTriggerUSec
	   org.freedesktop.systemd1(5)

       LastTriggerUSecMonotonic
	   org.freedesktop.systemd1(5)

       LazyUnmount
	   org.freedesktop.systemd1(5)

       Leader
	   org.freedesktop.login1(5), org.freedesktop.machine1(5)

       Leases
	   org.freedesktop.network1(5)

       LidClosed
	   org.freedesktop.login1(5)

       Limit
	   org.freedesktop.portable1(5)

       LimitAS
	   org.freedesktop.systemd1(5)

       LimitASSoft
	   org.freedesktop.systemd1(5)

       LimitCORE
	   org.freedesktop.systemd1(5)

       LimitCORESoft
	   org.freedesktop.systemd1(5)

       LimitCPU
	   org.freedesktop.systemd1(5)

       LimitCPUSoft
	   org.freedesktop.systemd1(5)

       LimitDATA
	   org.freedesktop.systemd1(5)

       LimitDATASoft
	   org.freedesktop.systemd1(5)

       LimitExclusive
	   org.freedesktop.portable1(5)

       LimitFSIZE
	   org.freedesktop.systemd1(5)

       LimitFSIZESoft
	   org.freedesktop.systemd1(5)

       LimitLOCKS
	   org.freedesktop.systemd1(5)

       LimitLOCKSSoft
	   org.freedesktop.systemd1(5)

       LimitMEMLOCK
	   org.freedesktop.systemd1(5)

       LimitMEMLOCKSoft
	   org.freedesktop.systemd1(5)

       LimitMSGQUEUE
	   org.freedesktop.systemd1(5)

       LimitMSGQUEUESoft
	   org.freedesktop.systemd1(5)

       LimitNICE
	   org.freedesktop.systemd1(5)

       LimitNICESoft
	   org.freedesktop.systemd1(5)

       LimitNOFILE
	   org.freedesktop.systemd1(5)

       LimitNOFILESoft
	   org.freedesktop.systemd1(5)

       LimitNPROC
	   org.freedesktop.systemd1(5)

       LimitNPROCSoft
	   org.freedesktop.systemd1(5)

       LimitRSS
	   org.freedesktop.systemd1(5)

       LimitRSSSoft
	   org.freedesktop.systemd1(5)

       LimitRTPRIO
	   org.freedesktop.systemd1(5)

       LimitRTPRIOSoft
	   org.freedesktop.systemd1(5)

       LimitRTTIME
	   org.freedesktop.systemd1(5)

       LimitRTTIMESoft
	   org.freedesktop.systemd1(5)

       LimitSIGPENDING
	   org.freedesktop.systemd1(5)

       LimitSIGPENDINGSoft
	   org.freedesktop.systemd1(5)

       LimitSTACK
	   org.freedesktop.systemd1(5)

       LimitSTACKSoft
	   org.freedesktop.systemd1(5)

       Linger
	   org.freedesktop.login1(5)

       Listen
	   org.freedesktop.systemd1(5)

       LoadCredential
	   org.freedesktop.systemd1(5)

       LoadCredentialEncrypted
	   org.freedesktop.systemd1(5)

       LoadError
	   org.freedesktop.systemd1(5)

       LoadState
	   org.freedesktop.systemd1(5)

       LoaderTimestamp
	   org.freedesktop.systemd1(5)

       LoaderTimestampMonotonic
	   org.freedesktop.systemd1(5)

       Local
	   org.freedesktop.import1(5)

       LocalRTC
	   org.freedesktop.timedate1(5)

       Locale
	   org.freedesktop.locale1(5)

       Location
	   org.freedesktop.hostname1(5)

       LockPersonality
	   org.freedesktop.systemd1(5)

       LockedHint
	   org.freedesktop.login1(5)

       LogExtraFields
	   org.freedesktop.systemd1(5)

       LogFilterPatterns
	   org.freedesktop.systemd1(5)

       LogLevel
	   org.freedesktop.LogControl1(5), org.freedesktop.systemd1(5)

       LogLevelMax
	   org.freedesktop.systemd1(5)

       LogNamespace
	   org.freedesktop.systemd1(5)

       LogRateLimitBurst
	   org.freedesktop.systemd1(5)

       LogRateLimitIntervalUSec
	   org.freedesktop.systemd1(5)

       LogTarget
	   org.freedesktop.LogControl1(5), org.freedesktop.systemd1(5)

       LogsDirectory
	   org.freedesktop.systemd1(5)

       LogsDirectoryMode
	   org.freedesktop.systemd1(5)

       LogsDirectorySymlink
	   org.freedesktop.systemd1(5)

       MachineID
	   org.freedesktop.hostname1(5)

       MainPID
	   org.freedesktop.systemd1(5)

       MakeDirectory
	   org.freedesktop.systemd1(5)

       ManagedOOMMemoryPressure
	   org.freedesktop.systemd1(5)

       ManagedOOMMemoryPressureLimit
	   org.freedesktop.systemd1(5)

       ManagedOOMPreference
	   org.freedesktop.systemd1(5)

       ManagedOOMSwap
	   org.freedesktop.systemd1(5)

       Mark
	   org.freedesktop.systemd1(5)

       Markers
	   org.freedesktop.systemd1(5)

       MatchDriver
	   org.freedesktop.network1(5)

       MatchMAC
	   org.freedesktop.network1(5)

       MatchName
	   org.freedesktop.network1(5)

       MatchPath
	   org.freedesktop.network1(5)

       MatchType
	   org.freedesktop.network1(5)

       MaxConnections
	   org.freedesktop.systemd1(5)

       MaxConnectionsPerSource
	   org.freedesktop.systemd1(5)

       MemoryAccounting
	   org.freedesktop.systemd1(5)

       MemoryAvailable
	   org.freedesktop.systemd1(5)

       MemoryCurrent
	   org.freedesktop.systemd1(5)

       MemoryDenyWriteExecute
	   org.freedesktop.systemd1(5)

       MemoryHigh
	   org.freedesktop.systemd1(5)

       MemoryKSM
	   org.freedesktop.systemd1(5)

       MemoryLimit
	   org.freedesktop.systemd1(5)

       MemoryLow
	   org.freedesktop.systemd1(5)

       MemoryMax
	   org.freedesktop.systemd1(5)

       MemoryMin
	   org.freedesktop.systemd1(5)

       MemoryPeak
	   org.freedesktop.systemd1(5)

       MemoryPressureThresholdUSec
	   org.freedesktop.systemd1(5)

       MemoryPressureWatch
	   org.freedesktop.systemd1(5)

       MemorySwapCurrent
	   org.freedesktop.systemd1(5)

       MemorySwapMax
	   org.freedesktop.systemd1(5)

       MemorySwapPeak
	   org.freedesktop.systemd1(5)

       MemoryZSwapCurrent
	   org.freedesktop.systemd1(5)

       MemoryZSwapMax
	   org.freedesktop.systemd1(5)

       MessageQueueMaxMessages
	   org.freedesktop.systemd1(5)

       MessageQueueMessageSize
	   org.freedesktop.systemd1(5)

       ModificationTimestamp
	   org.freedesktop.portable1(5)

       MountAPIVFS
	   org.freedesktop.systemd1(5)

       MountFlags
	   org.freedesktop.systemd1(5)

       MountImagePolicy
	   org.freedesktop.systemd1(5)

       MountImages
	   org.freedesktop.systemd1(5)

       MulticastDNS
	   org.freedesktop.resolve1(5)

       NAccepted
	   org.freedesktop.systemd1(5)

       NAutoVTs
	   org.freedesktop.login1(5)

       NConnections
	   org.freedesktop.systemd1(5)

       NCurrentInhibitors
	   org.freedesktop.login1(5)

       NCurrentSessions
	   org.freedesktop.login1(5)

       NFTSet
	   org.freedesktop.systemd1(5)

       NFailedJobs
	   org.freedesktop.systemd1(5)

       NFailedUnits
	   org.freedesktop.systemd1(5)

       NFileDescriptorStore
	   org.freedesktop.systemd1(5)

       NInstalledJobs
	   org.freedesktop.systemd1(5)

       NJobs
	   org.freedesktop.systemd1(5)

       NNames
	   org.freedesktop.systemd1(5)

       NRefused
	   org.freedesktop.systemd1(5)

       NRestarts
	   org.freedesktop.systemd1(5)

       NTP
	   org.freedesktop.timedate1(5)

       NTPSynchronized
	   org.freedesktop.timedate1(5)

       NUMAMask
	   org.freedesktop.systemd1(5)

       NUMAPolicy
	   org.freedesktop.systemd1(5)

       Name
	   org.freedesktop.login1(5), org.freedesktop.machine1(5), org.freedesktop.portable1(5)

       Names
	   org.freedesktop.systemd1(5)

       NamespaceId
	   org.freedesktop.network1(5)

       NeedDaemonReload
	   org.freedesktop.systemd1(5)

       NetworkInterfaces
	   org.freedesktop.machine1(5)

       NetworkNamespacePath
	   org.freedesktop.systemd1(5)

       NextElapseUSecMonotonic
	   org.freedesktop.systemd1(5)

       NextElapseUSecRealtime
	   org.freedesktop.systemd1(5)

       Nice
	   org.freedesktop.systemd1(5)

       NoDelay
	   org.freedesktop.systemd1(5)

       NoExecPaths
	   org.freedesktop.systemd1(5)

       NoNewPrivileges
	   org.freedesktop.systemd1(5)

       NonBlocking
	   org.freedesktop.systemd1(5)

       NotifyAccess
	   org.freedesktop.systemd1(5)

       OOMPolicy
	   org.freedesktop.systemd1(5)

       OOMScoreAdjust
	   org.freedesktop.systemd1(5)

       OnClockChange
	   org.freedesktop.systemd1(5)

       OnExternalPower
	   org.freedesktop.login1(5)

       OnFailure
	   org.freedesktop.systemd1(5)

       OnFailureJobMode
	   org.freedesktop.systemd1(5)

       OnFailureOf
	   org.freedesktop.systemd1(5)

       OnSuccess
	   org.freedesktop.systemd1(5)

       OnSuccessJobMode
	   org.freedesktop.systemd1(5)

       OnSuccessOf
	   org.freedesktop.systemd1(5)

       OnTimezoneChange
	   org.freedesktop.systemd1(5)

       OnlineState
	   org.freedesktop.network1(5)

       OpenFile
	   org.freedesktop.systemd1(5)

       OperatingSystemCPEName
	   org.freedesktop.hostname1(5)

       OperatingSystemPrettyName
	   org.freedesktop.hostname1(5)

       OperatingSystemSupportEnd
	   org.freedesktop.hostname1(5)

       OperationalState
	   org.freedesktop.network1(5)

       Options
	   org.freedesktop.systemd1(5)

       PAMName
	   org.freedesktop.systemd1(5)

       PIDFile
	   org.freedesktop.systemd1(5)

       PartOf
	   org.freedesktop.systemd1(5)

       PassCredentials
	   org.freedesktop.systemd1(5)

       PassEnvironment
	   org.freedesktop.systemd1(5)

       PassPacketInfo
	   org.freedesktop.systemd1(5)

       PassSecurity
	   org.freedesktop.systemd1(5)

       Path
	   org.freedesktop.portable1(5)

       Paths
	   org.freedesktop.systemd1(5)

       Perpetual
	   org.freedesktop.systemd1(5)

       Persistent
	   org.freedesktop.systemd1(5)

       Personality
	   org.freedesktop.systemd1(5)

       PipeSize
	   org.freedesktop.systemd1(5)

       PollLimitBurst
	   org.freedesktop.systemd1(5)

       PollLimitIntervalUSec
	   org.freedesktop.systemd1(5)

       PoolLimit
	   org.freedesktop.machine1(5), org.freedesktop.portable1(5)

       PoolPath
	   org.freedesktop.machine1(5), org.freedesktop.portable1(5)

       PoolUsage
	   org.freedesktop.machine1(5), org.freedesktop.portable1(5)

       PreparingForShutdown
	   org.freedesktop.login1(5)

       PreparingForSleep
	   org.freedesktop.login1(5)

       PrettyHostname
	   org.freedesktop.hostname1(5)

       Priority
	   org.freedesktop.systemd1(5)

       PrivateDevices
	   org.freedesktop.systemd1(5)

       PrivateIPC
	   org.freedesktop.systemd1(5)

       PrivateMounts
	   org.freedesktop.systemd1(5)

       PrivateNetwork
	   org.freedesktop.systemd1(5)

       PrivateTmp
	   org.freedesktop.systemd1(5)

       PrivateUsers
	   org.freedesktop.systemd1(5)

       ProcSubset
	   org.freedesktop.systemd1(5)

       Profiles
	   org.freedesktop.portable1(5)

       Progress
	   org.freedesktop.import1(5), org.freedesktop.systemd1(5)

       PropagatesReloadTo
	   org.freedesktop.systemd1(5)

       PropagatesStopTo
	   org.freedesktop.systemd1(5)

       ProtectClock
	   org.freedesktop.systemd1(5)

       ProtectControlGroups
	   org.freedesktop.systemd1(5)

       ProtectHome
	   org.freedesktop.systemd1(5)

       ProtectHostname
	   org.freedesktop.systemd1(5)

       ProtectKernelLogs
	   org.freedesktop.systemd1(5)

       ProtectKernelModules
	   org.freedesktop.systemd1(5)

       ProtectKernelTunables
	   org.freedesktop.systemd1(5)

       ProtectProc
	   org.freedesktop.systemd1(5)

       ProtectSystem
	   org.freedesktop.systemd1(5)

       RTCTimeUSec
	   org.freedesktop.timedate1(5)

       RandomizedDelayUSec
	   org.freedesktop.systemd1(5)

       ReadOnly
	   org.freedesktop.portable1(5)

       ReadOnlyPaths
	   org.freedesktop.systemd1(5)

       ReadWriteOnly
	   org.freedesktop.systemd1(5)

       ReadWritePaths
	   org.freedesktop.systemd1(5)

       RebootArgument
	   org.freedesktop.systemd1(5)

       RebootParameter
	   org.freedesktop.login1(5)

       RebootToBootLoaderEntry
	   org.freedesktop.login1(5)

       RebootToBootLoaderMenu
	   org.freedesktop.login1(5)

       RebootToFirmwareSetup
	   org.freedesktop.login1(5)

       RebootWatchdogUSec
	   org.freedesktop.systemd1(5)

       ReceiveBuffer
	   org.freedesktop.systemd1(5)

       Refs
	   org.freedesktop.systemd1(5)

       RefuseManualStart
	   org.freedesktop.systemd1(5)

       RefuseManualStop
	   org.freedesktop.systemd1(5)

       ReloadPropagatedFrom
	   org.freedesktop.systemd1(5)

       ReloadResult
	   org.freedesktop.systemd1(5)

       ReloadSignal
	   org.freedesktop.systemd1(5)

       RemainAfterElapse
	   org.freedesktop.systemd1(5)

       RemainAfterExit
	   org.freedesktop.systemd1(5)

       Remote
	   org.freedesktop.import1(5), org.freedesktop.login1(5)

       RemoteHost
	   org.freedesktop.login1(5)

       RemoteUser
	   org.freedesktop.login1(5)

       RemoveIPC
	   org.freedesktop.login1(5), org.freedesktop.systemd1(5)

       RemoveOnStop
	   org.freedesktop.systemd1(5)

       RequiredBy
	   org.freedesktop.systemd1(5)

       Requires
	   org.freedesktop.systemd1(5)

       RequiresMountsFor
	   org.freedesktop.systemd1(5)

       Requisite
	   org.freedesktop.systemd1(5)

       RequisiteOf
	   org.freedesktop.systemd1(5)

       ResolvConfMode
	   org.freedesktop.resolve1(5)

       Restart
	   org.freedesktop.systemd1(5)

       RestartForceExitStatus
	   org.freedesktop.systemd1(5)

       RestartKillSignal
	   org.freedesktop.systemd1(5)

       RestartMaxDelayUSec
	   org.freedesktop.systemd1(5)

       RestartMode
	   org.freedesktop.systemd1(5)

       RestartPreventExitStatus
	   org.freedesktop.systemd1(5)

       RestartSteps
	   org.freedesktop.systemd1(5)

       RestartUSec
	   org.freedesktop.systemd1(5)

       RestartUSecNext
	   org.freedesktop.systemd1(5)

       RestrictAddressFamilies
	   org.freedesktop.systemd1(5)

       RestrictFileSystems
	   org.freedesktop.systemd1(5)

       RestrictNamespaces
	   org.freedesktop.systemd1(5)

       RestrictNetworkInterfaces
	   org.freedesktop.systemd1(5)

       RestrictRealtime
	   org.freedesktop.systemd1(5)

       RestrictSUIDSGID
	   org.freedesktop.systemd1(5)

       Result
	   org.freedesktop.systemd1(5)

       ReusePort
	   org.freedesktop.systemd1(5)

       RootDirectory
	   org.freedesktop.machine1(5), org.freedesktop.systemd1(5)

       RootDirectoryStartOnly
	   org.freedesktop.systemd1(5)

       RootEphemeral
	   org.freedesktop.systemd1(5)

       RootHash
	   org.freedesktop.systemd1(5)

       RootHashPath
	   org.freedesktop.systemd1(5)

       RootHashSignature
	   org.freedesktop.systemd1(5)

       RootHashSignaturePath
	   org.freedesktop.systemd1(5)

       RootImage
	   org.freedesktop.systemd1(5)

       RootImageOptions
	   org.freedesktop.systemd1(5)

       RootImagePolicy
	   org.freedesktop.systemd1(5)

       RootVerity
	   org.freedesktop.systemd1(5)

       RuntimeDirectory
	   org.freedesktop.systemd1(5)

       RuntimeDirectoryInodesMax
	   org.freedesktop.login1(5)

       RuntimeDirectoryMode
	   org.freedesktop.systemd1(5)

       RuntimeDirectoryPreserve
	   org.freedesktop.systemd1(5)

       RuntimeDirectorySize
	   org.freedesktop.login1(5)

       RuntimeDirectorySymlink
	   org.freedesktop.systemd1(5)

       RuntimeMaxUSec
	   org.freedesktop.systemd1(5)

       RuntimePath
	   org.freedesktop.login1(5)

       RuntimeRandomizedExtraUSec
	   org.freedesktop.systemd1(5)

       RuntimeWatchdogPreGovernor
	   org.freedesktop.systemd1(5)

       RuntimeWatchdogPreUSec
	   org.freedesktop.systemd1(5)

       RuntimeWatchdogUSec
	   org.freedesktop.systemd1(5)

       SELinuxContext
	   org.freedesktop.systemd1(5)

       SameProcessGroup
	   org.freedesktop.systemd1(5)

       ScheduledShutdown
	   org.freedesktop.login1(5)

       Scope
	   org.freedesktop.login1(5)

       ScopesMask
	   org.freedesktop.resolve1(5)

       Seat
	   org.freedesktop.login1(5)

       SecureBits
	   org.freedesktop.systemd1(5)

       SecurityFinishTimestamp
	   org.freedesktop.systemd1(5)

       SecurityFinishTimestampMonotonic
	   org.freedesktop.systemd1(5)

       SecurityStartTimestamp
	   org.freedesktop.systemd1(5)

       SecurityStartTimestampMonotonic
	   org.freedesktop.systemd1(5)

       SendBuffer
	   org.freedesktop.systemd1(5)

       SendSIGHUP
	   org.freedesktop.systemd1(5)

       SendSIGKILL
	   org.freedesktop.systemd1(5)

       Service
	   org.freedesktop.login1(5), org.freedesktop.machine1(5)

       ServiceWatchdogs
	   org.freedesktop.systemd1(5)

       Sessions
	   org.freedesktop.login1(5)

       SessionsMax
	   org.freedesktop.login1(5)

       SetCredential
	   org.freedesktop.systemd1(5)

       SetCredentialEncrypted
	   org.freedesktop.systemd1(5)

       SetLoginEnvironment
	   org.freedesktop.systemd1(5)

       ShowStatus
	   org.freedesktop.systemd1(5)

       Slice
	   org.freedesktop.login1(5), org.freedesktop.systemd1(5)

       SliceOf
	   org.freedesktop.systemd1(5)

       SloppyOptions
	   org.freedesktop.systemd1(5)

       SmackLabel
	   org.freedesktop.systemd1(5)

       SmackLabelIPIn
	   org.freedesktop.systemd1(5)

       SmackLabelIPOut
	   org.freedesktop.systemd1(5)

       SmackProcessLabel
	   org.freedesktop.systemd1(5)

       SocketBindAllow
	   org.freedesktop.systemd1(5)

       SocketBindDeny
	   org.freedesktop.systemd1(5)

       SocketGroup
	   org.freedesktop.systemd1(5)

       SocketMode
	   org.freedesktop.systemd1(5)

       SocketProtocol
	   org.freedesktop.systemd1(5)

       SocketUser
	   org.freedesktop.systemd1(5)

       SourcePath
	   org.freedesktop.network1(5), org.freedesktop.systemd1(5)

       StandardError
	   org.freedesktop.systemd1(5)

       StandardErrorFileDescriptorName
	   org.freedesktop.systemd1(5)

       StandardInput
	   org.freedesktop.systemd1(5)

       StandardInputData
	   org.freedesktop.systemd1(5)

       StandardInputFileDescriptorName
	   org.freedesktop.systemd1(5)

       StandardOutput
	   org.freedesktop.systemd1(5)

       StandardOutputFileDescriptorName
	   org.freedesktop.systemd1(5)

       StartLimitAction
	   org.freedesktop.systemd1(5)

       StartLimitBurst
	   org.freedesktop.systemd1(5)

       StartLimitIntervalUSec
	   org.freedesktop.systemd1(5)

       StartupAllowedCPUs
	   org.freedesktop.systemd1(5)

       StartupAllowedMemoryNodes
	   org.freedesktop.systemd1(5)

       StartupBlockIOWeight
	   org.freedesktop.systemd1(5)

       StartupCPUShares
	   org.freedesktop.systemd1(5)

       StartupCPUWeight
	   org.freedesktop.systemd1(5)

       StartupIOWeight
	   org.freedesktop.systemd1(5)

       StartupMemoryHigh
	   org.freedesktop.systemd1(5)

       StartupMemoryLow
	   org.freedesktop.systemd1(5)

       StartupMemoryMax
	   org.freedesktop.systemd1(5)

       StartupMemorySwapMax
	   org.freedesktop.systemd1(5)

       StartupMemoryZSwapMax
	   org.freedesktop.systemd1(5)

       State
	   org.freedesktop.home1(5), org.freedesktop.login1(5), org.freedesktop.machine1(5), org.freedesktop.network1(5), org.freedesktop.systemd1(5)

       StateChangeTimestamp
	   org.freedesktop.systemd1(5)

       StateChangeTimestampMonotonic
	   org.freedesktop.systemd1(5)

       StateDirectory
	   org.freedesktop.systemd1(5)

       StateDirectoryMode
	   org.freedesktop.systemd1(5)

       StateDirectorySymlink
	   org.freedesktop.systemd1(5)

       StaticHostname
	   org.freedesktop.hostname1(5)

       StatusErrno
	   org.freedesktop.systemd1(5)

       StatusText
	   org.freedesktop.systemd1(5)

       StopIdleSessionUSec
	   org.freedesktop.login1(5)

       StopPropagatedFrom
	   org.freedesktop.systemd1(5)

       StopWhenUnneeded
	   org.freedesktop.systemd1(5)

       SubState
	   org.freedesktop.systemd1(5)

       SuccessAction
	   org.freedesktop.systemd1(5)

       SuccessActionExitStatus
	   org.freedesktop.systemd1(5)

       SuccessExitStatus
	   org.freedesktop.systemd1(5)

       SupplementaryGroups
	   org.freedesktop.systemd1(5)

       SurviveFinalKillSignal
	   org.freedesktop.systemd1(5)

       Symlinks
	   org.freedesktop.systemd1(5)

       SysFSPath
	   org.freedesktop.systemd1(5)

       SyslogFacility
	   org.freedesktop.systemd1(5)

       SyslogIdentifier
	   org.freedesktop.LogControl1(5), org.freedesktop.systemd1(5)

       SyslogLevel
	   org.freedesktop.systemd1(5)

       SyslogLevelPrefix
	   org.freedesktop.systemd1(5)

       SyslogPriority
	   org.freedesktop.systemd1(5)

       SystemCallArchitectures
	   org.freedesktop.systemd1(5)

       SystemCallErrorNumber
	   org.freedesktop.systemd1(5)

       SystemCallFilter
	   org.freedesktop.systemd1(5)

       SystemCallLog
	   org.freedesktop.systemd1(5)

       SystemState
	   org.freedesktop.systemd1(5)

       TCPCongestion
	   org.freedesktop.systemd1(5)

       TTY
	   org.freedesktop.login1(5)

       TTYColumns
	   org.freedesktop.systemd1(5)

       TTYPath
	   org.freedesktop.systemd1(5)

       TTYReset
	   org.freedesktop.systemd1(5)

       TTYRows
	   org.freedesktop.systemd1(5)

       TTYVHangup
	   org.freedesktop.systemd1(5)

       TTYVTDisallocate
	   org.freedesktop.systemd1(5)

       Tainted
	   org.freedesktop.systemd1(5)

       TasksAccounting
	   org.freedesktop.systemd1(5)

       TasksCurrent
	   org.freedesktop.systemd1(5)

       TasksMax
	   org.freedesktop.systemd1(5)

       TemporaryFileSystem
	   org.freedesktop.systemd1(5)

       TimeUSec
	   org.freedesktop.timedate1(5)

       TimeoutAbortUSec
	   org.freedesktop.systemd1(5)

       TimeoutCleanUSec
	   org.freedesktop.systemd1(5)

       TimeoutIdleUSec
	   org.freedesktop.systemd1(5)

       TimeoutStartFailureMode
	   org.freedesktop.systemd1(5)

       TimeoutStartUSec
	   org.freedesktop.systemd1(5)

       TimeoutStopFailureMode
	   org.freedesktop.systemd1(5)

       TimeoutStopUSec
	   org.freedesktop.systemd1(5)

       TimeoutUSec
	   org.freedesktop.systemd1(5)

       TimerSlackNSec
	   org.freedesktop.systemd1(5)

       TimersCalendar
	   org.freedesktop.systemd1(5)

       TimersMonotonic
	   org.freedesktop.systemd1(5)

       Timestamp
	   org.freedesktop.login1(5), org.freedesktop.machine1(5)

       TimestampMonotonic
	   org.freedesktop.login1(5), org.freedesktop.machine1(5)

       Timestamping
	   org.freedesktop.systemd1(5)

       Timezone
	   org.freedesktop.timedate1(5)

       TransactionStatistics
	   org.freedesktop.resolve1(5)

       Transient
	   org.freedesktop.systemd1(5)

       Transparent
	   org.freedesktop.systemd1(5)

       TriggerLimitBurst
	   org.freedesktop.systemd1(5)

       TriggerLimitIntervalUSec
	   org.freedesktop.systemd1(5)

       TriggeredBy
	   org.freedesktop.systemd1(5)

       Triggers
	   org.freedesktop.systemd1(5)

       Type
	   org.freedesktop.import1(5), org.freedesktop.login1(5), org.freedesktop.portable1(5), org.freedesktop.systemd1(5)

       UID
	   org.freedesktop.home1(5), org.freedesktop.login1(5), org.freedesktop.systemd1(5)

       UMask
	   org.freedesktop.systemd1(5)

       USBFunctionDescriptors
	   org.freedesktop.systemd1(5)

       USBFunctionStrings
	   org.freedesktop.systemd1(5)

       Unit
	   org.freedesktop.machine1(5), org.freedesktop.systemd1(5)

       UnitFilePreset
	   org.freedesktop.systemd1(5)

       UnitFileState
	   org.freedesktop.systemd1(5)

       UnitPath
	   org.freedesktop.systemd1(5)

       UnitsLoadFinishTimestamp
	   org.freedesktop.systemd1(5)

       UnitsLoadFinishTimestampMonotonic
	   org.freedesktop.systemd1(5)

       UnitsLoadStartTimestamp
	   org.freedesktop.systemd1(5)

       UnitsLoadStartTimestampMonotonic
	   org.freedesktop.systemd1(5)

       UnitsLoadTimestamp
	   org.freedesktop.systemd1(5)

       UnitsLoadTimestampMonotonic
	   org.freedesktop.systemd1(5)

       UnixRecord
	   org.freedesktop.home1(5)

       UnsetEnvironment
	   org.freedesktop.systemd1(5)

       UpheldBy
	   org.freedesktop.systemd1(5)

       Upholds
	   org.freedesktop.systemd1(5)

       Usage
	   org.freedesktop.portable1(5)

       UsageExclusive
	   org.freedesktop.portable1(5)

       User
	   org.freedesktop.login1(5), org.freedesktop.systemd1(5)

       UserName
	   org.freedesktop.home1(5)

       UserRecord
	   org.freedesktop.home1(5)

       UserStopDelayUSec
	   org.freedesktop.login1(5)

       UserspaceTimestamp
	   org.freedesktop.systemd1(5)

       UserspaceTimestampMonotonic
	   org.freedesktop.systemd1(5)

       UtmpIdentifier
	   org.freedesktop.systemd1(5)

       UtmpMode
	   org.freedesktop.systemd1(5)

       VConsoleKeymap
	   org.freedesktop.locale1(5)

       VConsoleKeymapToggle
	   org.freedesktop.locale1(5)

       VTNr
	   org.freedesktop.login1(5)

       Verify
	   org.freedesktop.import1(5)

       Version
	   org.freedesktop.systemd1(5)

       Virtualization
	   org.freedesktop.systemd1(5)

       WakeSystem
	   org.freedesktop.systemd1(5)

       WallMessage
	   org.freedesktop.login1(5)

       WantedBy
	   org.freedesktop.systemd1(5)

       Wants
	   org.freedesktop.systemd1(5)

       WatchdogDevice
	   org.freedesktop.systemd1(5)

       WatchdogLastPingTimestamp
	   org.freedesktop.systemd1(5)

       WatchdogLastPingTimestampMonotonic
	   org.freedesktop.systemd1(5)

       WatchdogSignal
	   org.freedesktop.systemd1(5)

       WatchdogTimestamp
	   org.freedesktop.systemd1(5)

       WatchdogTimestampMonotonic
	   org.freedesktop.systemd1(5)

       WatchdogUSec
	   org.freedesktop.systemd1(5)

       What
	   org.freedesktop.systemd1(5)

       Where
	   org.freedesktop.systemd1(5)

       WorkingDirectory
	   org.freedesktop.systemd1(5)

       Writable
	   org.freedesktop.systemd1(5)

       X11Layout
	   org.freedesktop.locale1(5)

       X11Model
	   org.freedesktop.locale1(5)

       X11Options
	   org.freedesktop.locale1(5)

       X11Variant
	   org.freedesktop.locale1(5)

D-BUS SIGNALS
       Signals emitted in the D-Bus interface.

       JobNew
	   org.freedesktop.systemd1(5)

       JobRemoved
	   org.freedesktop.systemd1(5)

       Killed
	   org.freedesktop.oom1(5)

       Lock
	   org.freedesktop.login1(5)

       LogMessage
	   org.freedesktop.import1(5)

       MachineNew
	   org.freedesktop.machine1(5)

       MachineRemoved
	   org.freedesktop.machine1(5)

       PauseDevice
	   org.freedesktop.login1(5)

       PrepareForShutdown
	   org.freedesktop.login1(5)

       PrepareForShutdownWithMetadata
	   org.freedesktop.login1(5)

       PrepareForSleep
	   org.freedesktop.login1(5)

       Reloading
	   org.freedesktop.systemd1(5)

       RequestStop
	   org.freedesktop.systemd1(5)

       ResumeDevice
	   org.freedesktop.login1(5)

       SeatNew
	   org.freedesktop.login1(5)

       SeatRemoved
	   org.freedesktop.login1(5)

       SessionNew
	   org.freedesktop.login1(5)

       SessionRemoved
	   org.freedesktop.login1(5)

       StartupFinished
	   org.freedesktop.systemd1(5)

       TransferNew
	   org.freedesktop.import1(5)

       TransferRemoved
	   org.freedesktop.import1(5)

       UnitFilesChanged
	   org.freedesktop.systemd1(5)

       UnitNew
	   org.freedesktop.systemd1(5)

       UnitRemoved
	   org.freedesktop.systemd1(5)

       Unlock
	   org.freedesktop.login1(5)

       UserNew
	   org.freedesktop.login1(5)

       UserRemoved
	   org.freedesktop.login1(5)

COLOPHON
       This index contains 5991 entries in 24 sections, referring to 392 individual manual pages.

systemd 255																 SYSTEMD.DIRECTIVES(7)
