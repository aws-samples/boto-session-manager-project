# -*- coding: utf-8 -*-

import typing as T

from .services import AwsServiceEnum

if T.TYPE_CHECKING:
    from .manager import BotoSesManager
    import mypy_boto3_accessanalyzer
    import mypy_boto3_account
    import mypy_boto3_acm
    import mypy_boto3_acm_pca
    import mypy_boto3_alexaforbusiness
    import mypy_boto3_amp
    import mypy_boto3_amplify
    import mypy_boto3_amplifybackend
    import mypy_boto3_amplifyuibuilder
    import mypy_boto3_apigateway
    import mypy_boto3_apigatewaymanagementapi
    import mypy_boto3_apigatewayv2
    import mypy_boto3_appconfig
    import mypy_boto3_appconfigdata
    import mypy_boto3_appflow
    import mypy_boto3_appintegrations
    import mypy_boto3_application_autoscaling
    import mypy_boto3_application_insights
    import mypy_boto3_applicationcostprofiler
    import mypy_boto3_appmesh
    import mypy_boto3_apprunner
    import mypy_boto3_appstream
    import mypy_boto3_appsync
    import mypy_boto3_arc_zonal_shift
    import mypy_boto3_athena
    import mypy_boto3_auditmanager
    import mypy_boto3_autoscaling
    import mypy_boto3_autoscaling_plans
    import mypy_boto3_backup
    import mypy_boto3_backup_gateway
    import mypy_boto3_backupstorage
    import mypy_boto3_batch
    import mypy_boto3_billingconductor
    import mypy_boto3_braket
    import mypy_boto3_budgets
    import mypy_boto3_ce
    import mypy_boto3_chime
    import mypy_boto3_chime_sdk_identity
    import mypy_boto3_chime_sdk_media_pipelines
    import mypy_boto3_chime_sdk_meetings
    import mypy_boto3_chime_sdk_messaging
    import mypy_boto3_chime_sdk_voice
    import mypy_boto3_cleanrooms
    import mypy_boto3_cloud9
    import mypy_boto3_cloudcontrol
    import mypy_boto3_clouddirectory
    import mypy_boto3_cloudformation
    import mypy_boto3_cloudfront
    import mypy_boto3_cloudhsm
    import mypy_boto3_cloudhsmv2
    import mypy_boto3_cloudsearch
    import mypy_boto3_cloudsearchdomain
    import mypy_boto3_cloudtrail
    import mypy_boto3_cloudtrail_data
    import mypy_boto3_cloudwatch
    import mypy_boto3_codeartifact
    import mypy_boto3_codebuild
    import mypy_boto3_codecatalyst
    import mypy_boto3_codecommit
    import mypy_boto3_codedeploy
    import mypy_boto3_codeguru_reviewer
    import mypy_boto3_codeguruprofiler
    import mypy_boto3_codepipeline
    import mypy_boto3_codestar
    import mypy_boto3_codestar_connections
    import mypy_boto3_codestar_notifications
    import mypy_boto3_cognito_identity
    import mypy_boto3_cognito_idp
    import mypy_boto3_cognito_sync
    import mypy_boto3_comprehend
    import mypy_boto3_comprehendmedical
    import mypy_boto3_compute_optimizer
    import mypy_boto3_config
    import mypy_boto3_connect
    import mypy_boto3_connect_contact_lens
    import mypy_boto3_connectcampaigns
    import mypy_boto3_connectcases
    import mypy_boto3_connectparticipant
    import mypy_boto3_controltower
    import mypy_boto3_cur
    import mypy_boto3_customer_profiles
    import mypy_boto3_databrew
    import mypy_boto3_dataexchange
    import mypy_boto3_datapipeline
    import mypy_boto3_datasync
    import mypy_boto3_dax
    import mypy_boto3_detective
    import mypy_boto3_devicefarm
    import mypy_boto3_devops_guru
    import mypy_boto3_directconnect
    import mypy_boto3_discovery
    import mypy_boto3_dlm
    import mypy_boto3_dms
    import mypy_boto3_docdb
    import mypy_boto3_docdb_elastic
    import mypy_boto3_drs
    import mypy_boto3_ds
    import mypy_boto3_dynamodb
    import mypy_boto3_dynamodbstreams
    import mypy_boto3_ebs
    import mypy_boto3_ec2
    import mypy_boto3_ec2_instance_connect
    import mypy_boto3_ecr
    import mypy_boto3_ecr_public
    import mypy_boto3_ecs
    import mypy_boto3_efs
    import mypy_boto3_eks
    import mypy_boto3_elastic_inference
    import mypy_boto3_elasticache
    import mypy_boto3_elasticbeanstalk
    import mypy_boto3_elastictranscoder
    import mypy_boto3_elb
    import mypy_boto3_elbv2
    import mypy_boto3_emr
    import mypy_boto3_emr_containers
    import mypy_boto3_emr_serverless
    import mypy_boto3_es
    import mypy_boto3_events
    import mypy_boto3_evidently
    import mypy_boto3_finspace
    import mypy_boto3_finspace_data
    import mypy_boto3_firehose
    import mypy_boto3_fis
    import mypy_boto3_fms
    import mypy_boto3_forecast
    import mypy_boto3_forecastquery
    import mypy_boto3_frauddetector
    import mypy_boto3_fsx
    import mypy_boto3_gamelift
    import mypy_boto3_gamesparks
    import mypy_boto3_glacier
    import mypy_boto3_globalaccelerator
    import mypy_boto3_glue
    import mypy_boto3_grafana
    import mypy_boto3_greengrass
    import mypy_boto3_greengrassv2
    import mypy_boto3_groundstation
    import mypy_boto3_guardduty
    import mypy_boto3_health
    import mypy_boto3_healthlake
    import mypy_boto3_honeycode
    import mypy_boto3_iam
    import mypy_boto3_identitystore
    import mypy_boto3_imagebuilder
    import mypy_boto3_importexport
    import mypy_boto3_inspector
    import mypy_boto3_inspector2
    import mypy_boto3_internetmonitor
    import mypy_boto3_iot
    import mypy_boto3_iot_data
    import mypy_boto3_iot_jobs_data
    import mypy_boto3_iot_roborunner
    import mypy_boto3_iot1click_devices
    import mypy_boto3_iot1click_projects
    import mypy_boto3_iotanalytics
    import mypy_boto3_iotdeviceadvisor
    import mypy_boto3_iotevents
    import mypy_boto3_iotevents_data
    import mypy_boto3_iotfleethub
    import mypy_boto3_iotfleetwise
    import mypy_boto3_iotsecuretunneling
    import mypy_boto3_iotsitewise
    import mypy_boto3_iotthingsgraph
    import mypy_boto3_iottwinmaker
    import mypy_boto3_iotwireless
    import mypy_boto3_ivs
    import mypy_boto3_ivschat
    import mypy_boto3_kafka
    import mypy_boto3_kafkaconnect
    import mypy_boto3_kendra
    import mypy_boto3_kendra_ranking
    import mypy_boto3_keyspaces
    import mypy_boto3_kinesis
    import mypy_boto3_kinesis_video_archived_media
    import mypy_boto3_kinesis_video_media
    import mypy_boto3_kinesis_video_signaling
    import mypy_boto3_kinesis_video_webrtc_storage
    import mypy_boto3_kinesisanalytics
    import mypy_boto3_kinesisanalyticsv2
    import mypy_boto3_kinesisvideo
    import mypy_boto3_kms
    import mypy_boto3_lakeformation
    import mypy_boto3_lambda
    import mypy_boto3_lex_models
    import mypy_boto3_lex_runtime
    import mypy_boto3_lexv2_models
    import mypy_boto3_lexv2_runtime
    import mypy_boto3_license_manager
    import mypy_boto3_license_manager_linux_subscriptions
    import mypy_boto3_license_manager_user_subscriptions
    import mypy_boto3_lightsail
    import mypy_boto3_location
    import mypy_boto3_logs
    import mypy_boto3_lookoutequipment
    import mypy_boto3_lookoutmetrics
    import mypy_boto3_lookoutvision
    import mypy_boto3_m2
    import mypy_boto3_machinelearning
    import mypy_boto3_macie
    import mypy_boto3_macie2
    import mypy_boto3_managedblockchain
    import mypy_boto3_marketplace_catalog
    import mypy_boto3_marketplace_entitlement
    import mypy_boto3_marketplacecommerceanalytics
    import mypy_boto3_mediaconnect
    import mypy_boto3_mediaconvert
    import mypy_boto3_medialive
    import mypy_boto3_mediapackage
    import mypy_boto3_mediapackage_vod
    import mypy_boto3_mediastore
    import mypy_boto3_mediastore_data
    import mypy_boto3_mediatailor
    import mypy_boto3_memorydb
    import mypy_boto3_meteringmarketplace
    import mypy_boto3_mgh
    import mypy_boto3_mgn
    import mypy_boto3_migration_hub_refactor_spaces
    import mypy_boto3_migrationhub_config
    import mypy_boto3_migrationhuborchestrator
    import mypy_boto3_migrationhubstrategy
    import mypy_boto3_mobile
    import mypy_boto3_mq
    import mypy_boto3_mturk
    import mypy_boto3_mwaa
    import mypy_boto3_neptune
    import mypy_boto3_network_firewall
    import mypy_boto3_networkmanager
    import mypy_boto3_nimble
    import mypy_boto3_oam
    import mypy_boto3_omics
    import mypy_boto3_opensearch
    import mypy_boto3_opensearchserverless
    import mypy_boto3_opsworks
    import mypy_boto3_opsworkscm
    import mypy_boto3_organizations
    import mypy_boto3_outposts
    import mypy_boto3_panorama
    import mypy_boto3_personalize
    import mypy_boto3_personalize_events
    import mypy_boto3_personalize_runtime
    import mypy_boto3_pi
    import mypy_boto3_pinpoint
    import mypy_boto3_pinpoint_email
    import mypy_boto3_pinpoint_sms_voice
    import mypy_boto3_pinpoint_sms_voice_v2
    import mypy_boto3_pipes
    import mypy_boto3_polly
    import mypy_boto3_pricing
    import mypy_boto3_privatenetworks
    import mypy_boto3_proton
    import mypy_boto3_qldb
    import mypy_boto3_qldb_session
    import mypy_boto3_quicksight
    import mypy_boto3_ram
    import mypy_boto3_rbin
    import mypy_boto3_rds
    import mypy_boto3_rds_data
    import mypy_boto3_redshift
    import mypy_boto3_redshift_data
    import mypy_boto3_redshift_serverless
    import mypy_boto3_rekognition
    import mypy_boto3_resiliencehub
    import mypy_boto3_resource_explorer_2
    import mypy_boto3_resource_groups
    import mypy_boto3_resourcegroupstaggingapi
    import mypy_boto3_robomaker
    import mypy_boto3_rolesanywhere
    import mypy_boto3_route53
    import mypy_boto3_route53_recovery_cluster
    import mypy_boto3_route53_recovery_control_config
    import mypy_boto3_route53_recovery_readiness
    import mypy_boto3_route53domains
    import mypy_boto3_route53resolver
    import mypy_boto3_rum
    import mypy_boto3_s3
    import mypy_boto3_s3control
    import mypy_boto3_s3outposts
    import mypy_boto3_sagemaker
    import mypy_boto3_sagemaker_a2i_runtime
    import mypy_boto3_sagemaker_edge
    import mypy_boto3_sagemaker_featurestore_runtime
    import mypy_boto3_sagemaker_geospatial
    import mypy_boto3_sagemaker_metrics
    import mypy_boto3_sagemaker_runtime
    import mypy_boto3_savingsplans
    import mypy_boto3_scheduler
    import mypy_boto3_schemas
    import mypy_boto3_sdb
    import mypy_boto3_secretsmanager
    import mypy_boto3_securityhub
    import mypy_boto3_securitylake
    import mypy_boto3_serverlessrepo
    import mypy_boto3_service_quotas
    import mypy_boto3_servicecatalog
    import mypy_boto3_servicecatalog_appregistry
    import mypy_boto3_servicediscovery
    import mypy_boto3_ses
    import mypy_boto3_sesv2
    import mypy_boto3_shield
    import mypy_boto3_signer
    import mypy_boto3_simspaceweaver
    import mypy_boto3_sms
    import mypy_boto3_sms_voice
    import mypy_boto3_snow_device_management
    import mypy_boto3_snowball
    import mypy_boto3_sns
    import mypy_boto3_sqs
    import mypy_boto3_ssm
    import mypy_boto3_ssm_contacts
    import mypy_boto3_ssm_incidents
    import mypy_boto3_ssm_sap
    import mypy_boto3_sso
    import mypy_boto3_sso_admin
    import mypy_boto3_sso_oidc
    import mypy_boto3_stepfunctions
    import mypy_boto3_storagegateway
    import mypy_boto3_sts
    import mypy_boto3_support
    import mypy_boto3_support_app
    import mypy_boto3_swf
    import mypy_boto3_synthetics
    import mypy_boto3_textract
    import mypy_boto3_timestream_query
    import mypy_boto3_timestream_write
    import mypy_boto3_tnb
    import mypy_boto3_transcribe
    import mypy_boto3_transfer
    import mypy_boto3_translate
    import mypy_boto3_voice_id
    import mypy_boto3_waf
    import mypy_boto3_waf_regional
    import mypy_boto3_wafv2
    import mypy_boto3_wellarchitected
    import mypy_boto3_wisdom
    import mypy_boto3_workdocs
    import mypy_boto3_worklink
    import mypy_boto3_workmail
    import mypy_boto3_workmailmessageflow
    import mypy_boto3_workspaces
    import mypy_boto3_workspaces_web
    import mypy_boto3_xray

class ClientMixin:
    
    @property
    def accessanalyzer_client(self: "BotoSesManager") -> "mypy_boto3_accessanalyzer.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html
        """
        return self.get_client(AwsServiceEnum.AccessAnalyzer)
    
    @property
    def account_client(self: "BotoSesManager") -> "mypy_boto3_account.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html
        """
        return self.get_client(AwsServiceEnum.Account)
    
    @property
    def acm_client(self: "BotoSesManager") -> "mypy_boto3_acm.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html
        """
        return self.get_client(AwsServiceEnum.ACM)
    
    @property
    def acmpca_client(self: "BotoSesManager") -> "mypy_boto3_acm_pca.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html
        """
        return self.get_client(AwsServiceEnum.ACMPCA)
    
    @property
    def alexaforbusiness_client(self: "BotoSesManager") -> "mypy_boto3_alexaforbusiness.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html
        """
        return self.get_client(AwsServiceEnum.AlexaForBusiness)
    
    @property
    def prometheusservice_client(self: "BotoSesManager") -> "mypy_boto3_amp.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html
        """
        return self.get_client(AwsServiceEnum.PrometheusService)
    
    @property
    def amplify_client(self: "BotoSesManager") -> "mypy_boto3_amplify.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html
        """
        return self.get_client(AwsServiceEnum.Amplify)
    
    @property
    def amplifybackend_client(self: "BotoSesManager") -> "mypy_boto3_amplifybackend.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html
        """
        return self.get_client(AwsServiceEnum.AmplifyBackend)
    
    @property
    def amplifyuibuilder_client(self: "BotoSesManager") -> "mypy_boto3_amplifyuibuilder.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html
        """
        return self.get_client(AwsServiceEnum.AmplifyUIBuilder)
    
    @property
    def apigateway_client(self: "BotoSesManager") -> "mypy_boto3_apigateway.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html
        """
        return self.get_client(AwsServiceEnum.APIGateway)
    
    @property
    def apigatewaymanagementapi_client(self: "BotoSesManager") -> "mypy_boto3_apigatewaymanagementapi.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi.html
        """
        return self.get_client(AwsServiceEnum.ApiGatewayManagementApi)
    
    @property
    def apigatewayv2_client(self: "BotoSesManager") -> "mypy_boto3_apigatewayv2.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html
        """
        return self.get_client(AwsServiceEnum.ApiGatewayV2)
    
    @property
    def appconfig_client(self: "BotoSesManager") -> "mypy_boto3_appconfig.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html
        """
        return self.get_client(AwsServiceEnum.AppConfig)
    
    @property
    def appconfigdata_client(self: "BotoSesManager") -> "mypy_boto3_appconfigdata.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfigdata.html
        """
        return self.get_client(AwsServiceEnum.AppConfigData)
    
    @property
    def appflow_client(self: "BotoSesManager") -> "mypy_boto3_appflow.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html
        """
        return self.get_client(AwsServiceEnum.Appflow)
    
    @property
    def appintegrationsservice_client(self: "BotoSesManager") -> "mypy_boto3_appintegrations.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html
        """
        return self.get_client(AwsServiceEnum.AppIntegrationsService)
    
    @property
    def applicationautoscaling_client(self: "BotoSesManager") -> "mypy_boto3_application_autoscaling.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html
        """
        return self.get_client(AwsServiceEnum.ApplicationAutoScaling)
    
    @property
    def applicationinsights_client(self: "BotoSesManager") -> "mypy_boto3_application_insights.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html
        """
        return self.get_client(AwsServiceEnum.ApplicationInsights)
    
    @property
    def applicationcostprofiler_client(self: "BotoSesManager") -> "mypy_boto3_applicationcostprofiler.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/applicationcostprofiler.html
        """
        return self.get_client(AwsServiceEnum.ApplicationCostProfiler)
    
    @property
    def appmesh_client(self: "BotoSesManager") -> "mypy_boto3_appmesh.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html
        """
        return self.get_client(AwsServiceEnum.AppMesh)
    
    @property
    def apprunner_client(self: "BotoSesManager") -> "mypy_boto3_apprunner.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html
        """
        return self.get_client(AwsServiceEnum.AppRunner)
    
    @property
    def appstream_client(self: "BotoSesManager") -> "mypy_boto3_appstream.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html
        """
        return self.get_client(AwsServiceEnum.AppStream)
    
    @property
    def appsync_client(self: "BotoSesManager") -> "mypy_boto3_appsync.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html
        """
        return self.get_client(AwsServiceEnum.AppSync)
    
    @property
    def arczonalshift_client(self: "BotoSesManager") -> "mypy_boto3_arc_zonal_shift.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift.html
        """
        return self.get_client(AwsServiceEnum.ARCZonalShift)
    
    @property
    def athena_client(self: "BotoSesManager") -> "mypy_boto3_athena.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html
        """
        return self.get_client(AwsServiceEnum.Athena)
    
    @property
    def auditmanager_client(self: "BotoSesManager") -> "mypy_boto3_auditmanager.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html
        """
        return self.get_client(AwsServiceEnum.AuditManager)
    
    @property
    def autoscaling_client(self: "BotoSesManager") -> "mypy_boto3_autoscaling.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html
        """
        return self.get_client(AwsServiceEnum.AutoScaling)
    
    @property
    def autoscalingplans_client(self: "BotoSesManager") -> "mypy_boto3_autoscaling_plans.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html
        """
        return self.get_client(AwsServiceEnum.AutoScalingPlans)
    
    @property
    def backup_client(self: "BotoSesManager") -> "mypy_boto3_backup.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html
        """
        return self.get_client(AwsServiceEnum.Backup)
    
    @property
    def backupgateway_client(self: "BotoSesManager") -> "mypy_boto3_backup_gateway.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway.html
        """
        return self.get_client(AwsServiceEnum.BackupGateway)
    
    @property
    def backupstorage_client(self: "BotoSesManager") -> "mypy_boto3_backupstorage.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backupstorage.html
        """
        return self.get_client(AwsServiceEnum.BackupStorage)
    
    @property
    def batch_client(self: "BotoSesManager") -> "mypy_boto3_batch.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html
        """
        return self.get_client(AwsServiceEnum.Batch)
    
    @property
    def billingconductor_client(self: "BotoSesManager") -> "mypy_boto3_billingconductor.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor.html
        """
        return self.get_client(AwsServiceEnum.BillingConductor)
    
    @property
    def braket_client(self: "BotoSesManager") -> "mypy_boto3_braket.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html
        """
        return self.get_client(AwsServiceEnum.Braket)
    
    @property
    def budgets_client(self: "BotoSesManager") -> "mypy_boto3_budgets.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html
        """
        return self.get_client(AwsServiceEnum.Budgets)
    
    @property
    def costexplorer_client(self: "BotoSesManager") -> "mypy_boto3_ce.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html
        """
        return self.get_client(AwsServiceEnum.CostExplorer)
    
    @property
    def chime_client(self: "BotoSesManager") -> "mypy_boto3_chime.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html
        """
        return self.get_client(AwsServiceEnum.Chime)
    
    @property
    def chimesdkidentity_client(self: "BotoSesManager") -> "mypy_boto3_chime_sdk_identity.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity.html
        """
        return self.get_client(AwsServiceEnum.ChimeSDKIdentity)
    
    @property
    def chimesdkmediapipelines_client(self: "BotoSesManager") -> "mypy_boto3_chime_sdk_media_pipelines.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html
        """
        return self.get_client(AwsServiceEnum.ChimeSDKMediaPipelines)
    
    @property
    def chimesdkmeetings_client(self: "BotoSesManager") -> "mypy_boto3_chime_sdk_meetings.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings.html
        """
        return self.get_client(AwsServiceEnum.ChimeSDKMeetings)
    
    @property
    def chimesdkmessaging_client(self: "BotoSesManager") -> "mypy_boto3_chime_sdk_messaging.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-messaging.html
        """
        return self.get_client(AwsServiceEnum.ChimeSDKMessaging)
    
    @property
    def chimesdkvoice_client(self: "BotoSesManager") -> "mypy_boto3_chime_sdk_voice.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice.html
        """
        return self.get_client(AwsServiceEnum.ChimeSDKVoice)
    
    @property
    def cleanroomsservice_client(self: "BotoSesManager") -> "mypy_boto3_cleanrooms.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms.html
        """
        return self.get_client(AwsServiceEnum.CleanRoomsService)
    
    @property
    def cloud9_client(self: "BotoSesManager") -> "mypy_boto3_cloud9.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html
        """
        return self.get_client(AwsServiceEnum.Cloud9)
    
    @property
    def cloudcontrolapi_client(self: "BotoSesManager") -> "mypy_boto3_cloudcontrol.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol.html
        """
        return self.get_client(AwsServiceEnum.CloudControlApi)
    
    @property
    def clouddirectory_client(self: "BotoSesManager") -> "mypy_boto3_clouddirectory.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html
        """
        return self.get_client(AwsServiceEnum.CloudDirectory)
    
    @property
    def cloudformation_client(self: "BotoSesManager") -> "mypy_boto3_cloudformation.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html
        """
        return self.get_client(AwsServiceEnum.CloudFormation)
    
    @property
    def cloudfront_client(self: "BotoSesManager") -> "mypy_boto3_cloudfront.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html
        """
        return self.get_client(AwsServiceEnum.CloudFront)
    
    @property
    def cloudhsm_client(self: "BotoSesManager") -> "mypy_boto3_cloudhsm.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html
        """
        return self.get_client(AwsServiceEnum.CloudHSM)
    
    @property
    def cloudhsmv2_client(self: "BotoSesManager") -> "mypy_boto3_cloudhsmv2.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html
        """
        return self.get_client(AwsServiceEnum.CloudHSMV2)
    
    @property
    def cloudsearch_client(self: "BotoSesManager") -> "mypy_boto3_cloudsearch.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html
        """
        return self.get_client(AwsServiceEnum.CloudSearch)
    
    @property
    def cloudsearchdomain_client(self: "BotoSesManager") -> "mypy_boto3_cloudsearchdomain.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html
        """
        return self.get_client(AwsServiceEnum.CloudSearchDomain)
    
    @property
    def cloudtrail_client(self: "BotoSesManager") -> "mypy_boto3_cloudtrail.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html
        """
        return self.get_client(AwsServiceEnum.CloudTrail)
    
    @property
    def cloudtraildataservice_client(self: "BotoSesManager") -> "mypy_boto3_cloudtrail_data.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail-data.html
        """
        return self.get_client(AwsServiceEnum.CloudTrailDataService)
    
    @property
    def cloudwatch_client(self: "BotoSesManager") -> "mypy_boto3_cloudwatch.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html
        """
        return self.get_client(AwsServiceEnum.CloudWatch)
    
    @property
    def codeartifact_client(self: "BotoSesManager") -> "mypy_boto3_codeartifact.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html
        """
        return self.get_client(AwsServiceEnum.CodeArtifact)
    
    @property
    def codebuild_client(self: "BotoSesManager") -> "mypy_boto3_codebuild.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html
        """
        return self.get_client(AwsServiceEnum.CodeBuild)
    
    @property
    def codecatalyst_client(self: "BotoSesManager") -> "mypy_boto3_codecatalyst.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html
        """
        return self.get_client(AwsServiceEnum.CodeCatalyst)
    
    @property
    def codecommit_client(self: "BotoSesManager") -> "mypy_boto3_codecommit.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html
        """
        return self.get_client(AwsServiceEnum.CodeCommit)
    
    @property
    def codedeploy_client(self: "BotoSesManager") -> "mypy_boto3_codedeploy.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html
        """
        return self.get_client(AwsServiceEnum.CodeDeploy)
    
    @property
    def codegurureviewer_client(self: "BotoSesManager") -> "mypy_boto3_codeguru_reviewer.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html
        """
        return self.get_client(AwsServiceEnum.CodeGuruReviewer)
    
    @property
    def codeguruprofiler_client(self: "BotoSesManager") -> "mypy_boto3_codeguruprofiler.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html
        """
        return self.get_client(AwsServiceEnum.CodeGuruProfiler)
    
    @property
    def codepipeline_client(self: "BotoSesManager") -> "mypy_boto3_codepipeline.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html
        """
        return self.get_client(AwsServiceEnum.CodePipeline)
    
    @property
    def codestar_client(self: "BotoSesManager") -> "mypy_boto3_codestar.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html
        """
        return self.get_client(AwsServiceEnum.CodeStar)
    
    @property
    def codestarconnections_client(self: "BotoSesManager") -> "mypy_boto3_codestar_connections.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html
        """
        return self.get_client(AwsServiceEnum.CodeStarconnections)
    
    @property
    def codestarnotifications_client(self: "BotoSesManager") -> "mypy_boto3_codestar_notifications.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html
        """
        return self.get_client(AwsServiceEnum.CodeStarNotifications)
    
    @property
    def cognitoidentity_client(self: "BotoSesManager") -> "mypy_boto3_cognito_identity.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html
        """
        return self.get_client(AwsServiceEnum.CognitoIdentity)
    
    @property
    def cognitoidentityprovider_client(self: "BotoSesManager") -> "mypy_boto3_cognito_idp.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html
        """
        return self.get_client(AwsServiceEnum.CognitoIdentityProvider)
    
    @property
    def cognitosync_client(self: "BotoSesManager") -> "mypy_boto3_cognito_sync.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html
        """
        return self.get_client(AwsServiceEnum.CognitoSync)
    
    @property
    def comprehend_client(self: "BotoSesManager") -> "mypy_boto3_comprehend.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html
        """
        return self.get_client(AwsServiceEnum.Comprehend)
    
    @property
    def comprehendmedical_client(self: "BotoSesManager") -> "mypy_boto3_comprehendmedical.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html
        """
        return self.get_client(AwsServiceEnum.ComprehendMedical)
    
    @property
    def computeoptimizer_client(self: "BotoSesManager") -> "mypy_boto3_compute_optimizer.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html
        """
        return self.get_client(AwsServiceEnum.ComputeOptimizer)
    
    @property
    def configservice_client(self: "BotoSesManager") -> "mypy_boto3_config.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html
        """
        return self.get_client(AwsServiceEnum.ConfigService)
    
    @property
    def connect_client(self: "BotoSesManager") -> "mypy_boto3_connect.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html
        """
        return self.get_client(AwsServiceEnum.Connect)
    
    @property
    def connectcontactlens_client(self: "BotoSesManager") -> "mypy_boto3_connect_contact_lens.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect-contact-lens.html
        """
        return self.get_client(AwsServiceEnum.ConnectContactLens)
    
    @property
    def connectcampaignservice_client(self: "BotoSesManager") -> "mypy_boto3_connectcampaigns.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaigns.html
        """
        return self.get_client(AwsServiceEnum.ConnectCampaignService)
    
    @property
    def connectcases_client(self: "BotoSesManager") -> "mypy_boto3_connectcases.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html
        """
        return self.get_client(AwsServiceEnum.ConnectCases)
    
    @property
    def connectparticipant_client(self: "BotoSesManager") -> "mypy_boto3_connectparticipant.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html
        """
        return self.get_client(AwsServiceEnum.ConnectParticipant)
    
    @property
    def controltower_client(self: "BotoSesManager") -> "mypy_boto3_controltower.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html
        """
        return self.get_client(AwsServiceEnum.ControlTower)
    
    @property
    def costandusagereportservice_client(self: "BotoSesManager") -> "mypy_boto3_cur.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cur.html
        """
        return self.get_client(AwsServiceEnum.CostandUsageReportService)
    
    @property
    def customerprofiles_client(self: "BotoSesManager") -> "mypy_boto3_customer_profiles.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html
        """
        return self.get_client(AwsServiceEnum.CustomerProfiles)
    
    @property
    def gluedatabrew_client(self: "BotoSesManager") -> "mypy_boto3_databrew.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html
        """
        return self.get_client(AwsServiceEnum.GlueDataBrew)
    
    @property
    def dataexchange_client(self: "BotoSesManager") -> "mypy_boto3_dataexchange.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html
        """
        return self.get_client(AwsServiceEnum.DataExchange)
    
    @property
    def datapipeline_client(self: "BotoSesManager") -> "mypy_boto3_datapipeline.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html
        """
        return self.get_client(AwsServiceEnum.DataPipeline)
    
    @property
    def datasync_client(self: "BotoSesManager") -> "mypy_boto3_datasync.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html
        """
        return self.get_client(AwsServiceEnum.DataSync)
    
    @property
    def dax_client(self: "BotoSesManager") -> "mypy_boto3_dax.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html
        """
        return self.get_client(AwsServiceEnum.DAX)
    
    @property
    def detective_client(self: "BotoSesManager") -> "mypy_boto3_detective.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html
        """
        return self.get_client(AwsServiceEnum.Detective)
    
    @property
    def devicefarm_client(self: "BotoSesManager") -> "mypy_boto3_devicefarm.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html
        """
        return self.get_client(AwsServiceEnum.DeviceFarm)
    
    @property
    def devopsguru_client(self: "BotoSesManager") -> "mypy_boto3_devops_guru.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html
        """
        return self.get_client(AwsServiceEnum.DevOpsGuru)
    
    @property
    def directconnect_client(self: "BotoSesManager") -> "mypy_boto3_directconnect.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html
        """
        return self.get_client(AwsServiceEnum.DirectConnect)
    
    @property
    def applicationdiscoveryservice_client(self: "BotoSesManager") -> "mypy_boto3_discovery.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html
        """
        return self.get_client(AwsServiceEnum.ApplicationDiscoveryService)
    
    @property
    def dlm_client(self: "BotoSesManager") -> "mypy_boto3_dlm.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html
        """
        return self.get_client(AwsServiceEnum.DLM)
    
    @property
    def databasemigrationservice_client(self: "BotoSesManager") -> "mypy_boto3_dms.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html
        """
        return self.get_client(AwsServiceEnum.DatabaseMigrationService)
    
    @property
    def docdb_client(self: "BotoSesManager") -> "mypy_boto3_docdb.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html
        """
        return self.get_client(AwsServiceEnum.DocDB)
    
    @property
    def docdbelastic_client(self: "BotoSesManager") -> "mypy_boto3_docdb_elastic.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html
        """
        return self.get_client(AwsServiceEnum.DocDBElastic)
    
    @property
    def drs_client(self: "BotoSesManager") -> "mypy_boto3_drs.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs.html
        """
        return self.get_client(AwsServiceEnum.drs)
    
    @property
    def directoryservice_client(self: "BotoSesManager") -> "mypy_boto3_ds.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html
        """
        return self.get_client(AwsServiceEnum.DirectoryService)
    
    @property
    def dynamodb_client(self: "BotoSesManager") -> "mypy_boto3_dynamodb.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html
        """
        return self.get_client(AwsServiceEnum.DynamoDB)
    
    @property
    def dynamodbstreams_client(self: "BotoSesManager") -> "mypy_boto3_dynamodbstreams.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams.html
        """
        return self.get_client(AwsServiceEnum.DynamoDBStreams)
    
    @property
    def ebs_client(self: "BotoSesManager") -> "mypy_boto3_ebs.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html
        """
        return self.get_client(AwsServiceEnum.EBS)
    
    @property
    def ec2_client(self: "BotoSesManager") -> "mypy_boto3_ec2.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html
        """
        return self.get_client(AwsServiceEnum.EC2)
    
    @property
    def ec2instanceconnect_client(self: "BotoSesManager") -> "mypy_boto3_ec2_instance_connect.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect.html
        """
        return self.get_client(AwsServiceEnum.EC2InstanceConnect)
    
    @property
    def ecr_client(self: "BotoSesManager") -> "mypy_boto3_ecr.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html
        """
        return self.get_client(AwsServiceEnum.ECR)
    
    @property
    def ecrpublic_client(self: "BotoSesManager") -> "mypy_boto3_ecr_public.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html
        """
        return self.get_client(AwsServiceEnum.ECRPublic)
    
    @property
    def ecs_client(self: "BotoSesManager") -> "mypy_boto3_ecs.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html
        """
        return self.get_client(AwsServiceEnum.ECS)
    
    @property
    def efs_client(self: "BotoSesManager") -> "mypy_boto3_efs.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html
        """
        return self.get_client(AwsServiceEnum.EFS)
    
    @property
    def eks_client(self: "BotoSesManager") -> "mypy_boto3_eks.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html
        """
        return self.get_client(AwsServiceEnum.EKS)
    
    @property
    def elasticinference_client(self: "BotoSesManager") -> "mypy_boto3_elastic_inference.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html
        """
        return self.get_client(AwsServiceEnum.ElasticInference)
    
    @property
    def elasticache_client(self: "BotoSesManager") -> "mypy_boto3_elasticache.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html
        """
        return self.get_client(AwsServiceEnum.ElastiCache)
    
    @property
    def elasticbeanstalk_client(self: "BotoSesManager") -> "mypy_boto3_elasticbeanstalk.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html
        """
        return self.get_client(AwsServiceEnum.ElasticBeanstalk)
    
    @property
    def elastictranscoder_client(self: "BotoSesManager") -> "mypy_boto3_elastictranscoder.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html
        """
        return self.get_client(AwsServiceEnum.ElasticTranscoder)
    
    @property
    def elasticloadbalancing_client(self: "BotoSesManager") -> "mypy_boto3_elb.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html
        """
        return self.get_client(AwsServiceEnum.ElasticLoadBalancing)
    
    @property
    def elasticloadbalancingv2_client(self: "BotoSesManager") -> "mypy_boto3_elbv2.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html
        """
        return self.get_client(AwsServiceEnum.ElasticLoadBalancingv2)
    
    @property
    def emr_client(self: "BotoSesManager") -> "mypy_boto3_emr.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html
        """
        return self.get_client(AwsServiceEnum.EMR)
    
    @property
    def emrcontainers_client(self: "BotoSesManager") -> "mypy_boto3_emr_containers.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html
        """
        return self.get_client(AwsServiceEnum.EMRContainers)
    
    @property
    def emrserverless_client(self: "BotoSesManager") -> "mypy_boto3_emr_serverless.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless.html
        """
        return self.get_client(AwsServiceEnum.EMRServerless)
    
    @property
    def elasticsearchservice_client(self: "BotoSesManager") -> "mypy_boto3_es.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html
        """
        return self.get_client(AwsServiceEnum.ElasticsearchService)
    
    @property
    def eventbridge_client(self: "BotoSesManager") -> "mypy_boto3_events.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html
        """
        return self.get_client(AwsServiceEnum.EventBridge)
    
    @property
    def cloudwatchevidently_client(self: "BotoSesManager") -> "mypy_boto3_evidently.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently.html
        """
        return self.get_client(AwsServiceEnum.CloudWatchEvidently)
    
    @property
    def finspace_client(self: "BotoSesManager") -> "mypy_boto3_finspace.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html
        """
        return self.get_client(AwsServiceEnum.finspace)
    
    @property
    def finspacedata_client(self: "BotoSesManager") -> "mypy_boto3_finspace_data.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace-data.html
        """
        return self.get_client(AwsServiceEnum.FinSpaceData)
    
    @property
    def firehose_client(self: "BotoSesManager") -> "mypy_boto3_firehose.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html
        """
        return self.get_client(AwsServiceEnum.Firehose)
    
    @property
    def fis_client(self: "BotoSesManager") -> "mypy_boto3_fis.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html
        """
        return self.get_client(AwsServiceEnum.FIS)
    
    @property
    def fms_client(self: "BotoSesManager") -> "mypy_boto3_fms.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html
        """
        return self.get_client(AwsServiceEnum.FMS)
    
    @property
    def forecastservice_client(self: "BotoSesManager") -> "mypy_boto3_forecast.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html
        """
        return self.get_client(AwsServiceEnum.ForecastService)
    
    @property
    def forecastqueryservice_client(self: "BotoSesManager") -> "mypy_boto3_forecastquery.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecastquery.html
        """
        return self.get_client(AwsServiceEnum.ForecastQueryService)
    
    @property
    def frauddetector_client(self: "BotoSesManager") -> "mypy_boto3_frauddetector.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html
        """
        return self.get_client(AwsServiceEnum.FraudDetector)
    
    @property
    def fsx_client(self: "BotoSesManager") -> "mypy_boto3_fsx.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html
        """
        return self.get_client(AwsServiceEnum.FSx)
    
    @property
    def gamelift_client(self: "BotoSesManager") -> "mypy_boto3_gamelift.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html
        """
        return self.get_client(AwsServiceEnum.GameLift)
    
    @property
    def gamesparks_client(self: "BotoSesManager") -> "mypy_boto3_gamesparks.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamesparks.html
        """
        return self.get_client(AwsServiceEnum.GameSparks)
    
    @property
    def glacier_client(self: "BotoSesManager") -> "mypy_boto3_glacier.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html
        """
        return self.get_client(AwsServiceEnum.Glacier)
    
    @property
    def globalaccelerator_client(self: "BotoSesManager") -> "mypy_boto3_globalaccelerator.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html
        """
        return self.get_client(AwsServiceEnum.GlobalAccelerator)
    
    @property
    def glue_client(self: "BotoSesManager") -> "mypy_boto3_glue.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html
        """
        return self.get_client(AwsServiceEnum.Glue)
    
    @property
    def managedgrafana_client(self: "BotoSesManager") -> "mypy_boto3_grafana.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html
        """
        return self.get_client(AwsServiceEnum.ManagedGrafana)
    
    @property
    def greengrass_client(self: "BotoSesManager") -> "mypy_boto3_greengrass.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html
        """
        return self.get_client(AwsServiceEnum.Greengrass)
    
    @property
    def greengrassv2_client(self: "BotoSesManager") -> "mypy_boto3_greengrassv2.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html
        """
        return self.get_client(AwsServiceEnum.GreengrassV2)
    
    @property
    def groundstation_client(self: "BotoSesManager") -> "mypy_boto3_groundstation.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html
        """
        return self.get_client(AwsServiceEnum.GroundStation)
    
    @property
    def guardduty_client(self: "BotoSesManager") -> "mypy_boto3_guardduty.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html
        """
        return self.get_client(AwsServiceEnum.GuardDuty)
    
    @property
    def health_client(self: "BotoSesManager") -> "mypy_boto3_health.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html
        """
        return self.get_client(AwsServiceEnum.Health)
    
    @property
    def healthlake_client(self: "BotoSesManager") -> "mypy_boto3_healthlake.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake.html
        """
        return self.get_client(AwsServiceEnum.HealthLake)
    
    @property
    def honeycode_client(self: "BotoSesManager") -> "mypy_boto3_honeycode.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html
        """
        return self.get_client(AwsServiceEnum.Honeycode)
    
    @property
    def iam_client(self: "BotoSesManager") -> "mypy_boto3_iam.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html
        """
        return self.get_client(AwsServiceEnum.IAM)
    
    @property
    def identitystore_client(self: "BotoSesManager") -> "mypy_boto3_identitystore.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html
        """
        return self.get_client(AwsServiceEnum.IdentityStore)
    
    @property
    def imagebuilder_client(self: "BotoSesManager") -> "mypy_boto3_imagebuilder.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html
        """
        return self.get_client(AwsServiceEnum.imagebuilder)
    
    @property
    def importexport_client(self: "BotoSesManager") -> "mypy_boto3_importexport.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport.html
        """
        return self.get_client(AwsServiceEnum.ImportExport)
    
    @property
    def inspector_client(self: "BotoSesManager") -> "mypy_boto3_inspector.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html
        """
        return self.get_client(AwsServiceEnum.Inspector)
    
    @property
    def inspector2_client(self: "BotoSesManager") -> "mypy_boto3_inspector2.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html
        """
        return self.get_client(AwsServiceEnum.Inspector2)
    
    @property
    def cloudwatchinternetmonitor_client(self: "BotoSesManager") -> "mypy_boto3_internetmonitor.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor.html
        """
        return self.get_client(AwsServiceEnum.CloudWatchInternetMonitor)
    
    @property
    def iot_client(self: "BotoSesManager") -> "mypy_boto3_iot.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html
        """
        return self.get_client(AwsServiceEnum.IoT)
    
    @property
    def iotdataplane_client(self: "BotoSesManager") -> "mypy_boto3_iot_data.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-data.html
        """
        return self.get_client(AwsServiceEnum.IoTDataPlane)
    
    @property
    def iotjobsdataplane_client(self: "BotoSesManager") -> "mypy_boto3_iot_jobs_data.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data.html
        """
        return self.get_client(AwsServiceEnum.IoTJobsDataPlane)
    
    @property
    def iotroborunner_client(self: "BotoSesManager") -> "mypy_boto3_iot_roborunner.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-roborunner.html
        """
        return self.get_client(AwsServiceEnum.IoTRoboRunner)
    
    @property
    def iot1clickdevicesservice_client(self: "BotoSesManager") -> "mypy_boto3_iot1click_devices.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html
        """
        return self.get_client(AwsServiceEnum.IoT1ClickDevicesService)
    
    @property
    def iot1clickprojects_client(self: "BotoSesManager") -> "mypy_boto3_iot1click_projects.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html
        """
        return self.get_client(AwsServiceEnum.IoT1ClickProjects)
    
    @property
    def iotanalytics_client(self: "BotoSesManager") -> "mypy_boto3_iotanalytics.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html
        """
        return self.get_client(AwsServiceEnum.IoTAnalytics)
    
    @property
    def iotdeviceadvisor_client(self: "BotoSesManager") -> "mypy_boto3_iotdeviceadvisor.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html
        """
        return self.get_client(AwsServiceEnum.IoTDeviceAdvisor)
    
    @property
    def iotevents_client(self: "BotoSesManager") -> "mypy_boto3_iotevents.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html
        """
        return self.get_client(AwsServiceEnum.IoTEvents)
    
    @property
    def ioteventsdata_client(self: "BotoSesManager") -> "mypy_boto3_iotevents_data.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data.html
        """
        return self.get_client(AwsServiceEnum.IoTEventsData)
    
    @property
    def iotfleethub_client(self: "BotoSesManager") -> "mypy_boto3_iotfleethub.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleethub.html
        """
        return self.get_client(AwsServiceEnum.IoTFleetHub)
    
    @property
    def iotfleetwise_client(self: "BotoSesManager") -> "mypy_boto3_iotfleetwise.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html
        """
        return self.get_client(AwsServiceEnum.IoTFleetWise)
    
    @property
    def iotsecuretunneling_client(self: "BotoSesManager") -> "mypy_boto3_iotsecuretunneling.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling.html
        """
        return self.get_client(AwsServiceEnum.IoTSecureTunneling)
    
    @property
    def iotsitewise_client(self: "BotoSesManager") -> "mypy_boto3_iotsitewise.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html
        """
        return self.get_client(AwsServiceEnum.IoTSiteWise)
    
    @property
    def iotthingsgraph_client(self: "BotoSesManager") -> "mypy_boto3_iotthingsgraph.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html
        """
        return self.get_client(AwsServiceEnum.IoTThingsGraph)
    
    @property
    def iottwinmaker_client(self: "BotoSesManager") -> "mypy_boto3_iottwinmaker.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker.html
        """
        return self.get_client(AwsServiceEnum.IoTTwinMaker)
    
    @property
    def iotwireless_client(self: "BotoSesManager") -> "mypy_boto3_iotwireless.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html
        """
        return self.get_client(AwsServiceEnum.IoTWireless)
    
    @property
    def ivs_client(self: "BotoSesManager") -> "mypy_boto3_ivs.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html
        """
        return self.get_client(AwsServiceEnum.IVS)
    
    @property
    def ivschat_client(self: "BotoSesManager") -> "mypy_boto3_ivschat.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html
        """
        return self.get_client(AwsServiceEnum.ivschat)
    
    @property
    def kafka_client(self: "BotoSesManager") -> "mypy_boto3_kafka.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html
        """
        return self.get_client(AwsServiceEnum.Kafka)
    
    @property
    def kafkaconnect_client(self: "BotoSesManager") -> "mypy_boto3_kafkaconnect.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect.html
        """
        return self.get_client(AwsServiceEnum.KafkaConnect)
    
    @property
    def kendra_client(self: "BotoSesManager") -> "mypy_boto3_kendra.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html
        """
        return self.get_client(AwsServiceEnum.kendra)
    
    @property
    def kendraranking_client(self: "BotoSesManager") -> "mypy_boto3_kendra_ranking.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html
        """
        return self.get_client(AwsServiceEnum.KendraRanking)
    
    @property
    def keyspaces_client(self: "BotoSesManager") -> "mypy_boto3_keyspaces.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspaces.html
        """
        return self.get_client(AwsServiceEnum.Keyspaces)
    
    @property
    def kinesis_client(self: "BotoSesManager") -> "mypy_boto3_kinesis.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html
        """
        return self.get_client(AwsServiceEnum.Kinesis)
    
    @property
    def kinesisvideoarchivedmedia_client(self: "BotoSesManager") -> "mypy_boto3_kinesis_video_archived_media.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html
        """
        return self.get_client(AwsServiceEnum.KinesisVideoArchivedMedia)
    
    @property
    def kinesisvideomedia_client(self: "BotoSesManager") -> "mypy_boto3_kinesis_video_media.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-media.html
        """
        return self.get_client(AwsServiceEnum.KinesisVideoMedia)
    
    @property
    def kinesisvideosignalingchannels_client(self: "BotoSesManager") -> "mypy_boto3_kinesis_video_signaling.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-signaling.html
        """
        return self.get_client(AwsServiceEnum.KinesisVideoSignalingChannels)
    
    @property
    def kinesisvideowebrtcstorage_client(self: "BotoSesManager") -> "mypy_boto3_kinesis_video_webrtc_storage.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-webrtc-storage.html
        """
        return self.get_client(AwsServiceEnum.KinesisVideoWebRTCStorage)
    
    @property
    def kinesisanalytics_client(self: "BotoSesManager") -> "mypy_boto3_kinesisanalytics.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html
        """
        return self.get_client(AwsServiceEnum.KinesisAnalytics)
    
    @property
    def kinesisanalyticsv2_client(self: "BotoSesManager") -> "mypy_boto3_kinesisanalyticsv2.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2.html
        """
        return self.get_client(AwsServiceEnum.KinesisAnalyticsV2)
    
    @property
    def kinesisvideo_client(self: "BotoSesManager") -> "mypy_boto3_kinesisvideo.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html
        """
        return self.get_client(AwsServiceEnum.KinesisVideo)
    
    @property
    def kms_client(self: "BotoSesManager") -> "mypy_boto3_kms.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html
        """
        return self.get_client(AwsServiceEnum.KMS)
    
    @property
    def lakeformation_client(self: "BotoSesManager") -> "mypy_boto3_lakeformation.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html
        """
        return self.get_client(AwsServiceEnum.LakeFormation)
    
    @property
    def lambda_client(self: "BotoSesManager") -> "mypy_boto3_lambda.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html
        """
        return self.get_client(AwsServiceEnum.Lambda)
    
    @property
    def lexmodelbuildingservice_client(self: "BotoSesManager") -> "mypy_boto3_lex_models.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html
        """
        return self.get_client(AwsServiceEnum.LexModelBuildingService)
    
    @property
    def lexruntimeservice_client(self: "BotoSesManager") -> "mypy_boto3_lex_runtime.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-runtime.html
        """
        return self.get_client(AwsServiceEnum.LexRuntimeService)
    
    @property
    def lexmodelsv2_client(self: "BotoSesManager") -> "mypy_boto3_lexv2_models.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html
        """
        return self.get_client(AwsServiceEnum.LexModelsV2)
    
    @property
    def lexruntimev2_client(self: "BotoSesManager") -> "mypy_boto3_lexv2_runtime.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime.html
        """
        return self.get_client(AwsServiceEnum.LexRuntimeV2)
    
    @property
    def licensemanager_client(self: "BotoSesManager") -> "mypy_boto3_license_manager.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html
        """
        return self.get_client(AwsServiceEnum.LicenseManager)
    
    @property
    def licensemanagerlinuxsubscriptions_client(self: "BotoSesManager") -> "mypy_boto3_license_manager_linux_subscriptions.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-linux-subscriptions.html
        """
        return self.get_client(AwsServiceEnum.LicenseManagerLinuxSubscriptions)
    
    @property
    def licensemanagerusersubscriptions_client(self: "BotoSesManager") -> "mypy_boto3_license_manager_user_subscriptions.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html
        """
        return self.get_client(AwsServiceEnum.LicenseManagerUserSubscriptions)
    
    @property
    def lightsail_client(self: "BotoSesManager") -> "mypy_boto3_lightsail.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html
        """
        return self.get_client(AwsServiceEnum.Lightsail)
    
    @property
    def locationservice_client(self: "BotoSesManager") -> "mypy_boto3_location.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html
        """
        return self.get_client(AwsServiceEnum.LocationService)
    
    @property
    def cloudwatchlogs_client(self: "BotoSesManager") -> "mypy_boto3_logs.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html
        """
        return self.get_client(AwsServiceEnum.CloudWatchLogs)
    
    @property
    def lookoutequipment_client(self: "BotoSesManager") -> "mypy_boto3_lookoutequipment.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html
        """
        return self.get_client(AwsServiceEnum.LookoutEquipment)
    
    @property
    def lookoutmetrics_client(self: "BotoSesManager") -> "mypy_boto3_lookoutmetrics.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html
        """
        return self.get_client(AwsServiceEnum.LookoutMetrics)
    
    @property
    def lookoutforvision_client(self: "BotoSesManager") -> "mypy_boto3_lookoutvision.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html
        """
        return self.get_client(AwsServiceEnum.LookoutforVision)
    
    @property
    def mainframemodernization_client(self: "BotoSesManager") -> "mypy_boto3_m2.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html
        """
        return self.get_client(AwsServiceEnum.MainframeModernization)
    
    @property
    def machinelearning_client(self: "BotoSesManager") -> "mypy_boto3_machinelearning.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html
        """
        return self.get_client(AwsServiceEnum.MachineLearning)
    
    @property
    def macie_client(self: "BotoSesManager") -> "mypy_boto3_macie.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html
        """
        return self.get_client(AwsServiceEnum.Macie)
    
    @property
    def macie2_client(self: "BotoSesManager") -> "mypy_boto3_macie2.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html
        """
        return self.get_client(AwsServiceEnum.Macie2)
    
    @property
    def managedblockchain_client(self: "BotoSesManager") -> "mypy_boto3_managedblockchain.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html
        """
        return self.get_client(AwsServiceEnum.ManagedBlockchain)
    
    @property
    def marketplacecatalog_client(self: "BotoSesManager") -> "mypy_boto3_marketplace_catalog.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html
        """
        return self.get_client(AwsServiceEnum.MarketplaceCatalog)
    
    @property
    def marketplaceentitlementservice_client(self: "BotoSesManager") -> "mypy_boto3_marketplace_entitlement.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement.html
        """
        return self.get_client(AwsServiceEnum.MarketplaceEntitlementService)
    
    @property
    def marketplacecommerceanalytics_client(self: "BotoSesManager") -> "mypy_boto3_marketplacecommerceanalytics.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplacecommerceanalytics.html
        """
        return self.get_client(AwsServiceEnum.MarketplaceCommerceAnalytics)
    
    @property
    def mediaconnect_client(self: "BotoSesManager") -> "mypy_boto3_mediaconnect.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html
        """
        return self.get_client(AwsServiceEnum.MediaConnect)
    
    @property
    def mediaconvert_client(self: "BotoSesManager") -> "mypy_boto3_mediaconvert.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html
        """
        return self.get_client(AwsServiceEnum.MediaConvert)
    
    @property
    def medialive_client(self: "BotoSesManager") -> "mypy_boto3_medialive.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html
        """
        return self.get_client(AwsServiceEnum.MediaLive)
    
    @property
    def mediapackage_client(self: "BotoSesManager") -> "mypy_boto3_mediapackage.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html
        """
        return self.get_client(AwsServiceEnum.MediaPackage)
    
    @property
    def mediapackagevod_client(self: "BotoSesManager") -> "mypy_boto3_mediapackage_vod.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html
        """
        return self.get_client(AwsServiceEnum.MediaPackageVod)
    
    @property
    def mediastore_client(self: "BotoSesManager") -> "mypy_boto3_mediastore.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html
        """
        return self.get_client(AwsServiceEnum.MediaStore)
    
    @property
    def mediastoredata_client(self: "BotoSesManager") -> "mypy_boto3_mediastore_data.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data.html
        """
        return self.get_client(AwsServiceEnum.MediaStoreData)
    
    @property
    def mediatailor_client(self: "BotoSesManager") -> "mypy_boto3_mediatailor.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html
        """
        return self.get_client(AwsServiceEnum.MediaTailor)
    
    @property
    def memorydb_client(self: "BotoSesManager") -> "mypy_boto3_memorydb.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html
        """
        return self.get_client(AwsServiceEnum.MemoryDB)
    
    @property
    def marketplacemetering_client(self: "BotoSesManager") -> "mypy_boto3_meteringmarketplace.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html
        """
        return self.get_client(AwsServiceEnum.MarketplaceMetering)
    
    @property
    def migrationhub_client(self: "BotoSesManager") -> "mypy_boto3_mgh.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html
        """
        return self.get_client(AwsServiceEnum.MigrationHub)
    
    @property
    def mgn_client(self: "BotoSesManager") -> "mypy_boto3_mgn.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html
        """
        return self.get_client(AwsServiceEnum.mgn)
    
    @property
    def migrationhubrefactorspaces_client(self: "BotoSesManager") -> "mypy_boto3_migration_hub_refactor_spaces.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces.html
        """
        return self.get_client(AwsServiceEnum.MigrationHubRefactorSpaces)
    
    @property
    def migrationhubconfig_client(self: "BotoSesManager") -> "mypy_boto3_migrationhub_config.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config.html
        """
        return self.get_client(AwsServiceEnum.MigrationHubConfig)
    
    @property
    def migrationhuborchestrator_client(self: "BotoSesManager") -> "mypy_boto3_migrationhuborchestrator.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html
        """
        return self.get_client(AwsServiceEnum.MigrationHubOrchestrator)
    
    @property
    def migrationhubstrategyrecommendations_client(self: "BotoSesManager") -> "mypy_boto3_migrationhubstrategy.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhubstrategy.html
        """
        return self.get_client(AwsServiceEnum.MigrationHubStrategyRecommendations)
    
    @property
    def mobile_client(self: "BotoSesManager") -> "mypy_boto3_mobile.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html
        """
        return self.get_client(AwsServiceEnum.Mobile)
    
    @property
    def mq_client(self: "BotoSesManager") -> "mypy_boto3_mq.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html
        """
        return self.get_client(AwsServiceEnum.MQ)
    
    @property
    def mturk_client(self: "BotoSesManager") -> "mypy_boto3_mturk.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html
        """
        return self.get_client(AwsServiceEnum.MTurk)
    
    @property
    def mwaa_client(self: "BotoSesManager") -> "mypy_boto3_mwaa.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html
        """
        return self.get_client(AwsServiceEnum.MWAA)
    
    @property
    def neptune_client(self: "BotoSesManager") -> "mypy_boto3_neptune.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html
        """
        return self.get_client(AwsServiceEnum.Neptune)
    
    @property
    def networkfirewall_client(self: "BotoSesManager") -> "mypy_boto3_network_firewall.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html
        """
        return self.get_client(AwsServiceEnum.NetworkFirewall)
    
    @property
    def networkmanager_client(self: "BotoSesManager") -> "mypy_boto3_networkmanager.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html
        """
        return self.get_client(AwsServiceEnum.NetworkManager)
    
    @property
    def nimblestudio_client(self: "BotoSesManager") -> "mypy_boto3_nimble.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html
        """
        return self.get_client(AwsServiceEnum.NimbleStudio)
    
    @property
    def cloudwatchobservabilityaccessmanager_client(self: "BotoSesManager") -> "mypy_boto3_oam.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html
        """
        return self.get_client(AwsServiceEnum.CloudWatchObservabilityAccessManager)
    
    @property
    def omics_client(self: "BotoSesManager") -> "mypy_boto3_omics.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html
        """
        return self.get_client(AwsServiceEnum.Omics)
    
    @property
    def opensearchservice_client(self: "BotoSesManager") -> "mypy_boto3_opensearch.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html
        """
        return self.get_client(AwsServiceEnum.OpenSearchService)
    
    @property
    def opensearchserviceserverless_client(self: "BotoSesManager") -> "mypy_boto3_opensearchserverless.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html
        """
        return self.get_client(AwsServiceEnum.OpenSearchServiceServerless)
    
    @property
    def opsworks_client(self: "BotoSesManager") -> "mypy_boto3_opsworks.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html
        """
        return self.get_client(AwsServiceEnum.OpsWorks)
    
    @property
    def opsworkscm_client(self: "BotoSesManager") -> "mypy_boto3_opsworkscm.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html
        """
        return self.get_client(AwsServiceEnum.OpsWorksCM)
    
    @property
    def organizations_client(self: "BotoSesManager") -> "mypy_boto3_organizations.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html
        """
        return self.get_client(AwsServiceEnum.Organizations)
    
    @property
    def outposts_client(self: "BotoSesManager") -> "mypy_boto3_outposts.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html
        """
        return self.get_client(AwsServiceEnum.Outposts)
    
    @property
    def panorama_client(self: "BotoSesManager") -> "mypy_boto3_panorama.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/panorama.html
        """
        return self.get_client(AwsServiceEnum.Panorama)
    
    @property
    def personalize_client(self: "BotoSesManager") -> "mypy_boto3_personalize.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html
        """
        return self.get_client(AwsServiceEnum.Personalize)
    
    @property
    def personalizeevents_client(self: "BotoSesManager") -> "mypy_boto3_personalize_events.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html
        """
        return self.get_client(AwsServiceEnum.PersonalizeEvents)
    
    @property
    def personalizeruntime_client(self: "BotoSesManager") -> "mypy_boto3_personalize_runtime.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-runtime.html
        """
        return self.get_client(AwsServiceEnum.PersonalizeRuntime)
    
    @property
    def pi_client(self: "BotoSesManager") -> "mypy_boto3_pi.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi.html
        """
        return self.get_client(AwsServiceEnum.PI)
    
    @property
    def pinpoint_client(self: "BotoSesManager") -> "mypy_boto3_pinpoint.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html
        """
        return self.get_client(AwsServiceEnum.Pinpoint)
    
    @property
    def pinpointemail_client(self: "BotoSesManager") -> "mypy_boto3_pinpoint_email.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email.html
        """
        return self.get_client(AwsServiceEnum.PinpointEmail)
    
    @property
    def pinpointsmsvoice_client(self: "BotoSesManager") -> "mypy_boto3_pinpoint_sms_voice.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice.html
        """
        return self.get_client(AwsServiceEnum.PinpointSMSVoice)
    
    @property
    def pinpointsmsvoicev2_client(self: "BotoSesManager") -> "mypy_boto3_pinpoint_sms_voice_v2.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html
        """
        return self.get_client(AwsServiceEnum.PinpointSMSVoiceV2)
    
    @property
    def eventbridgepipes_client(self: "BotoSesManager") -> "mypy_boto3_pipes.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html
        """
        return self.get_client(AwsServiceEnum.EventBridgePipes)
    
    @property
    def polly_client(self: "BotoSesManager") -> "mypy_boto3_polly.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html
        """
        return self.get_client(AwsServiceEnum.Polly)
    
    @property
    def pricing_client(self: "BotoSesManager") -> "mypy_boto3_pricing.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html
        """
        return self.get_client(AwsServiceEnum.Pricing)
    
    @property
    def private5g_client(self: "BotoSesManager") -> "mypy_boto3_privatenetworks.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks.html
        """
        return self.get_client(AwsServiceEnum.Private5G)
    
    @property
    def proton_client(self: "BotoSesManager") -> "mypy_boto3_proton.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html
        """
        return self.get_client(AwsServiceEnum.Proton)
    
    @property
    def qldb_client(self: "BotoSesManager") -> "mypy_boto3_qldb.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html
        """
        return self.get_client(AwsServiceEnum.QLDB)
    
    @property
    def qldbsession_client(self: "BotoSesManager") -> "mypy_boto3_qldb_session.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb-session.html
        """
        return self.get_client(AwsServiceEnum.QLDBSession)
    
    @property
    def quicksight_client(self: "BotoSesManager") -> "mypy_boto3_quicksight.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html
        """
        return self.get_client(AwsServiceEnum.QuickSight)
    
    @property
    def ram_client(self: "BotoSesManager") -> "mypy_boto3_ram.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html
        """
        return self.get_client(AwsServiceEnum.RAM)
    
    @property
    def recyclebin_client(self: "BotoSesManager") -> "mypy_boto3_rbin.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin.html
        """
        return self.get_client(AwsServiceEnum.RecycleBin)
    
    @property
    def rds_client(self: "BotoSesManager") -> "mypy_boto3_rds.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html
        """
        return self.get_client(AwsServiceEnum.RDS)
    
    @property
    def rdsdataservice_client(self: "BotoSesManager") -> "mypy_boto3_rds_data.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html
        """
        return self.get_client(AwsServiceEnum.RDSDataService)
    
    @property
    def redshift_client(self: "BotoSesManager") -> "mypy_boto3_redshift.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html
        """
        return self.get_client(AwsServiceEnum.Redshift)
    
    @property
    def redshiftdataapiservice_client(self: "BotoSesManager") -> "mypy_boto3_redshift_data.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html
        """
        return self.get_client(AwsServiceEnum.RedshiftDataAPIService)
    
    @property
    def redshiftserverless_client(self: "BotoSesManager") -> "mypy_boto3_redshift_serverless.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html
        """
        return self.get_client(AwsServiceEnum.RedshiftServerless)
    
    @property
    def rekognition_client(self: "BotoSesManager") -> "mypy_boto3_rekognition.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html
        """
        return self.get_client(AwsServiceEnum.Rekognition)
    
    @property
    def resiliencehub_client(self: "BotoSesManager") -> "mypy_boto3_resiliencehub.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub.html
        """
        return self.get_client(AwsServiceEnum.ResilienceHub)
    
    @property
    def resourceexplorer_client(self: "BotoSesManager") -> "mypy_boto3_resource_explorer_2.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html
        """
        return self.get_client(AwsServiceEnum.ResourceExplorer)
    
    @property
    def resourcegroups_client(self: "BotoSesManager") -> "mypy_boto3_resource_groups.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html
        """
        return self.get_client(AwsServiceEnum.ResourceGroups)
    
    @property
    def resourcegroupstaggingapi_client(self: "BotoSesManager") -> "mypy_boto3_resourcegroupstaggingapi.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html
        """
        return self.get_client(AwsServiceEnum.ResourceGroupsTaggingAPI)
    
    @property
    def robomaker_client(self: "BotoSesManager") -> "mypy_boto3_robomaker.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html
        """
        return self.get_client(AwsServiceEnum.RoboMaker)
    
    @property
    def iamrolesanywhere_client(self: "BotoSesManager") -> "mypy_boto3_rolesanywhere.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html
        """
        return self.get_client(AwsServiceEnum.IAMRolesAnywhere)
    
    @property
    def route53_client(self: "BotoSesManager") -> "mypy_boto3_route53.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html
        """
        return self.get_client(AwsServiceEnum.Route53)
    
    @property
    def route53recoverycluster_client(self: "BotoSesManager") -> "mypy_boto3_route53_recovery_cluster.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-cluster.html
        """
        return self.get_client(AwsServiceEnum.Route53RecoveryCluster)
    
    @property
    def route53recoverycontrolconfig_client(self: "BotoSesManager") -> "mypy_boto3_route53_recovery_control_config.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html
        """
        return self.get_client(AwsServiceEnum.Route53RecoveryControlConfig)
    
    @property
    def route53recoveryreadiness_client(self: "BotoSesManager") -> "mypy_boto3_route53_recovery_readiness.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html
        """
        return self.get_client(AwsServiceEnum.Route53RecoveryReadiness)
    
    @property
    def route53domains_client(self: "BotoSesManager") -> "mypy_boto3_route53domains.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html
        """
        return self.get_client(AwsServiceEnum.Route53Domains)
    
    @property
    def route53resolver_client(self: "BotoSesManager") -> "mypy_boto3_route53resolver.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html
        """
        return self.get_client(AwsServiceEnum.Route53Resolver)
    
    @property
    def cloudwatchrum_client(self: "BotoSesManager") -> "mypy_boto3_rum.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html
        """
        return self.get_client(AwsServiceEnum.CloudWatchRUM)
    
    @property
    def s3_client(self: "BotoSesManager") -> "mypy_boto3_s3.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
        """
        return self.get_client(AwsServiceEnum.S3)
    
    @property
    def s3control_client(self: "BotoSesManager") -> "mypy_boto3_s3control.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html
        """
        return self.get_client(AwsServiceEnum.S3Control)
    
    @property
    def s3outposts_client(self: "BotoSesManager") -> "mypy_boto3_s3outposts.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts.html
        """
        return self.get_client(AwsServiceEnum.S3Outposts)
    
    @property
    def sagemaker_client(self: "BotoSesManager") -> "mypy_boto3_sagemaker.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html
        """
        return self.get_client(AwsServiceEnum.SageMaker)
    
    @property
    def augmentedairuntime_client(self: "BotoSesManager") -> "mypy_boto3_sagemaker_a2i_runtime.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime.html
        """
        return self.get_client(AwsServiceEnum.AugmentedAIRuntime)
    
    @property
    def sagemakeredgemanager_client(self: "BotoSesManager") -> "mypy_boto3_sagemaker_edge.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html
        """
        return self.get_client(AwsServiceEnum.SagemakerEdgeManager)
    
    @property
    def sagemakerfeaturestoreruntime_client(self: "BotoSesManager") -> "mypy_boto3_sagemaker_featurestore_runtime.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime.html
        """
        return self.get_client(AwsServiceEnum.SageMakerFeatureStoreRuntime)
    
    @property
    def sagemakergeospatialcapabilities_client(self: "BotoSesManager") -> "mypy_boto3_sagemaker_geospatial.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-geospatial.html
        """
        return self.get_client(AwsServiceEnum.SageMakergeospatialcapabilities)
    
    @property
    def sagemakermetrics_client(self: "BotoSesManager") -> "mypy_boto3_sagemaker_metrics.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-metrics.html
        """
        return self.get_client(AwsServiceEnum.SageMakerMetrics)
    
    @property
    def sagemakerruntime_client(self: "BotoSesManager") -> "mypy_boto3_sagemaker_runtime.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime.html
        """
        return self.get_client(AwsServiceEnum.SageMakerRuntime)
    
    @property
    def savingsplans_client(self: "BotoSesManager") -> "mypy_boto3_savingsplans.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html
        """
        return self.get_client(AwsServiceEnum.SavingsPlans)
    
    @property
    def eventbridgescheduler_client(self: "BotoSesManager") -> "mypy_boto3_scheduler.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/scheduler.html
        """
        return self.get_client(AwsServiceEnum.EventBridgeScheduler)
    
    @property
    def schemas_client(self: "BotoSesManager") -> "mypy_boto3_schemas.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html
        """
        return self.get_client(AwsServiceEnum.Schemas)
    
    @property
    def simpledb_client(self: "BotoSesManager") -> "mypy_boto3_sdb.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb.html
        """
        return self.get_client(AwsServiceEnum.SimpleDB)
    
    @property
    def secretsmanager_client(self: "BotoSesManager") -> "mypy_boto3_secretsmanager.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html
        """
        return self.get_client(AwsServiceEnum.SecretsManager)
    
    @property
    def securityhub_client(self: "BotoSesManager") -> "mypy_boto3_securityhub.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html
        """
        return self.get_client(AwsServiceEnum.SecurityHub)
    
    @property
    def securitylake_client(self: "BotoSesManager") -> "mypy_boto3_securitylake.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake.html
        """
        return self.get_client(AwsServiceEnum.SecurityLake)
    
    @property
    def serverlessapplicationrepository_client(self: "BotoSesManager") -> "mypy_boto3_serverlessrepo.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html
        """
        return self.get_client(AwsServiceEnum.ServerlessApplicationRepository)
    
    @property
    def servicequotas_client(self: "BotoSesManager") -> "mypy_boto3_service_quotas.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html
        """
        return self.get_client(AwsServiceEnum.ServiceQuotas)
    
    @property
    def servicecatalog_client(self: "BotoSesManager") -> "mypy_boto3_servicecatalog.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog.html
        """
        return self.get_client(AwsServiceEnum.ServiceCatalog)
    
    @property
    def appregistry_client(self: "BotoSesManager") -> "mypy_boto3_servicecatalog_appregistry.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html
        """
        return self.get_client(AwsServiceEnum.AppRegistry)
    
    @property
    def servicediscovery_client(self: "BotoSesManager") -> "mypy_boto3_servicediscovery.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html
        """
        return self.get_client(AwsServiceEnum.ServiceDiscovery)
    
    @property
    def ses_client(self: "BotoSesManager") -> "mypy_boto3_ses.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html
        """
        return self.get_client(AwsServiceEnum.SES)
    
    @property
    def sesv2_client(self: "BotoSesManager") -> "mypy_boto3_sesv2.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html
        """
        return self.get_client(AwsServiceEnum.SESV2)
    
    @property
    def shield_client(self: "BotoSesManager") -> "mypy_boto3_shield.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html
        """
        return self.get_client(AwsServiceEnum.Shield)
    
    @property
    def signer_client(self: "BotoSesManager") -> "mypy_boto3_signer.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html
        """
        return self.get_client(AwsServiceEnum.signer)
    
    @property
    def simspaceweaver_client(self: "BotoSesManager") -> "mypy_boto3_simspaceweaver.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html
        """
        return self.get_client(AwsServiceEnum.SimSpaceWeaver)
    
    @property
    def sms_client(self: "BotoSesManager") -> "mypy_boto3_sms.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html
        """
        return self.get_client(AwsServiceEnum.SMS)
    
    @property
    def pinpointsmsvoice_client(self: "BotoSesManager") -> "mypy_boto3_sms_voice.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms-voice.html
        """
        return self.get_client(AwsServiceEnum.PinpointSMSVoice)
    
    @property
    def snowdevicemanagement_client(self: "BotoSesManager") -> "mypy_boto3_snow_device_management.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management.html
        """
        return self.get_client(AwsServiceEnum.SnowDeviceManagement)
    
    @property
    def snowball_client(self: "BotoSesManager") -> "mypy_boto3_snowball.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html
        """
        return self.get_client(AwsServiceEnum.Snowball)
    
    @property
    def sns_client(self: "BotoSesManager") -> "mypy_boto3_sns.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html
        """
        return self.get_client(AwsServiceEnum.SNS)
    
    @property
    def sqs_client(self: "BotoSesManager") -> "mypy_boto3_sqs.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html
        """
        return self.get_client(AwsServiceEnum.SQS)
    
    @property
    def ssm_client(self: "BotoSesManager") -> "mypy_boto3_ssm.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html
        """
        return self.get_client(AwsServiceEnum.SSM)
    
    @property
    def ssmcontacts_client(self: "BotoSesManager") -> "mypy_boto3_ssm_contacts.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html
        """
        return self.get_client(AwsServiceEnum.SSMContacts)
    
    @property
    def ssmincidents_client(self: "BotoSesManager") -> "mypy_boto3_ssm_incidents.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents.html
        """
        return self.get_client(AwsServiceEnum.SSMIncidents)
    
    @property
    def ssmsap_client(self: "BotoSesManager") -> "mypy_boto3_ssm_sap.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html
        """
        return self.get_client(AwsServiceEnum.SsmSap)
    
    @property
    def sso_client(self: "BotoSesManager") -> "mypy_boto3_sso.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html
        """
        return self.get_client(AwsServiceEnum.SSO)
    
    @property
    def ssoadmin_client(self: "BotoSesManager") -> "mypy_boto3_sso_admin.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html
        """
        return self.get_client(AwsServiceEnum.SSOAdmin)
    
    @property
    def ssooidc_client(self: "BotoSesManager") -> "mypy_boto3_sso_oidc.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc.html
        """
        return self.get_client(AwsServiceEnum.SSOOIDC)
    
    @property
    def sfn_client(self: "BotoSesManager") -> "mypy_boto3_stepfunctions.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html
        """
        return self.get_client(AwsServiceEnum.SFN)
    
    @property
    def storagegateway_client(self: "BotoSesManager") -> "mypy_boto3_storagegateway.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html
        """
        return self.get_client(AwsServiceEnum.StorageGateway)
    
    @property
    def sts_client(self: "BotoSesManager") -> "mypy_boto3_sts.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html
        """
        return self.get_client(AwsServiceEnum.STS)
    
    @property
    def support_client(self: "BotoSesManager") -> "mypy_boto3_support.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html
        """
        return self.get_client(AwsServiceEnum.Support)
    
    @property
    def supportapp_client(self: "BotoSesManager") -> "mypy_boto3_support_app.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html
        """
        return self.get_client(AwsServiceEnum.SupportApp)
    
    @property
    def swf_client(self: "BotoSesManager") -> "mypy_boto3_swf.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html
        """
        return self.get_client(AwsServiceEnum.SWF)
    
    @property
    def synthetics_client(self: "BotoSesManager") -> "mypy_boto3_synthetics.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html
        """
        return self.get_client(AwsServiceEnum.Synthetics)
    
    @property
    def textract_client(self: "BotoSesManager") -> "mypy_boto3_textract.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html
        """
        return self.get_client(AwsServiceEnum.Textract)
    
    @property
    def timestreamquery_client(self: "BotoSesManager") -> "mypy_boto3_timestream_query.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query.html
        """
        return self.get_client(AwsServiceEnum.TimestreamQuery)
    
    @property
    def timestreamwrite_client(self: "BotoSesManager") -> "mypy_boto3_timestream_write.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html
        """
        return self.get_client(AwsServiceEnum.TimestreamWrite)
    
    @property
    def telconetworkbuilder_client(self: "BotoSesManager") -> "mypy_boto3_tnb.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html
        """
        return self.get_client(AwsServiceEnum.TelcoNetworkBuilder)
    
    @property
    def transcribeservice_client(self: "BotoSesManager") -> "mypy_boto3_transcribe.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html
        """
        return self.get_client(AwsServiceEnum.TranscribeService)
    
    @property
    def transfer_client(self: "BotoSesManager") -> "mypy_boto3_transfer.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html
        """
        return self.get_client(AwsServiceEnum.Transfer)
    
    @property
    def translate_client(self: "BotoSesManager") -> "mypy_boto3_translate.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html
        """
        return self.get_client(AwsServiceEnum.Translate)
    
    @property
    def voiceid_client(self: "BotoSesManager") -> "mypy_boto3_voice_id.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html
        """
        return self.get_client(AwsServiceEnum.VoiceID)
    
    @property
    def waf_client(self: "BotoSesManager") -> "mypy_boto3_waf.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf.html
        """
        return self.get_client(AwsServiceEnum.WAF)
    
    @property
    def wafregional_client(self: "BotoSesManager") -> "mypy_boto3_waf_regional.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html
        """
        return self.get_client(AwsServiceEnum.WAFRegional)
    
    @property
    def wafv2_client(self: "BotoSesManager") -> "mypy_boto3_wafv2.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html
        """
        return self.get_client(AwsServiceEnum.WAFV2)
    
    @property
    def wellarchitected_client(self: "BotoSesManager") -> "mypy_boto3_wellarchitected.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html
        """
        return self.get_client(AwsServiceEnum.WellArchitected)
    
    @property
    def connectwisdomservice_client(self: "BotoSesManager") -> "mypy_boto3_wisdom.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom.html
        """
        return self.get_client(AwsServiceEnum.ConnectWisdomService)
    
    @property
    def workdocs_client(self: "BotoSesManager") -> "mypy_boto3_workdocs.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html
        """
        return self.get_client(AwsServiceEnum.WorkDocs)
    
    @property
    def worklink_client(self: "BotoSesManager") -> "mypy_boto3_worklink.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html
        """
        return self.get_client(AwsServiceEnum.WorkLink)
    
    @property
    def workmail_client(self: "BotoSesManager") -> "mypy_boto3_workmail.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html
        """
        return self.get_client(AwsServiceEnum.WorkMail)
    
    @property
    def workmailmessageflow_client(self: "BotoSesManager") -> "mypy_boto3_workmailmessageflow.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmailmessageflow.html
        """
        return self.get_client(AwsServiceEnum.WorkMailMessageFlow)
    
    @property
    def workspaces_client(self: "BotoSesManager") -> "mypy_boto3_workspaces.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html
        """
        return self.get_client(AwsServiceEnum.WorkSpaces)
    
    @property
    def workspacesweb_client(self: "BotoSesManager") -> "mypy_boto3_workspaces_web.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html
        """
        return self.get_client(AwsServiceEnum.WorkSpacesWeb)
    
    @property
    def xray_client(self: "BotoSesManager") -> "mypy_boto3_xray.Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html
        """
        return self.get_client(AwsServiceEnum.XRay)
    