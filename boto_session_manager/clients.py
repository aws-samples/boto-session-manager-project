# -*- coding: utf-8 -*-

import typing as T

from .services import AwsServiceEnum

if T.TYPE_CHECKING:
    from .manager import BotoSesManager
    from mypy_boto3_accessanalyzer import AccessanalyzerClient
    from mypy_boto3_account import AccountClient
    from mypy_boto3_acm import AcmClient
    from mypy_boto3_acm_pca import AcmpcaClient
    from mypy_boto3_alexaforbusiness import AlexaforbusinessClient
    from mypy_boto3_amp import PrometheusserviceClient
    from mypy_boto3_amplify import AmplifyClient
    from mypy_boto3_amplifybackend import AmplifybackendClient
    from mypy_boto3_amplifyuibuilder import AmplifyuibuilderClient
    from mypy_boto3_apigateway import ApigatewayClient
    from mypy_boto3_apigatewaymanagementapi import ApigatewaymanagementapiClient
    from mypy_boto3_apigatewayv2 import Apigatewayv2Client
    from mypy_boto3_appconfig import AppconfigClient
    from mypy_boto3_appconfigdata import AppconfigdataClient
    from mypy_boto3_appflow import AppflowClient
    from mypy_boto3_appintegrations import AppintegrationsserviceClient
    from mypy_boto3_application_autoscaling import ApplicationautoscalingClient
    from mypy_boto3_application_insights import ApplicationinsightsClient
    from mypy_boto3_applicationcostprofiler import ApplicationcostprofilerClient
    from mypy_boto3_appmesh import AppmeshClient
    from mypy_boto3_apprunner import ApprunnerClient
    from mypy_boto3_appstream import AppstreamClient
    from mypy_boto3_appsync import AppsyncClient
    from mypy_boto3_arc_zonal_shift import ArczonalshiftClient
    from mypy_boto3_athena import AthenaClient
    from mypy_boto3_auditmanager import AuditmanagerClient
    from mypy_boto3_autoscaling import AutoscalingClient
    from mypy_boto3_autoscaling_plans import AutoscalingplansClient
    from mypy_boto3_backup import BackupClient
    from mypy_boto3_backup_gateway import BackupgatewayClient
    from mypy_boto3_backupstorage import BackupstorageClient
    from mypy_boto3_batch import BatchClient
    from mypy_boto3_billingconductor import BillingconductorClient
    from mypy_boto3_braket import BraketClient
    from mypy_boto3_budgets import BudgetsClient
    from mypy_boto3_ce import CostexplorerClient
    from mypy_boto3_chime import ChimeClient
    from mypy_boto3_chime_sdk_identity import ChimesdkidentityClient
    from mypy_boto3_chime_sdk_media_pipelines import ChimesdkmediapipelinesClient
    from mypy_boto3_chime_sdk_meetings import ChimesdkmeetingsClient
    from mypy_boto3_chime_sdk_messaging import ChimesdkmessagingClient
    from mypy_boto3_chime_sdk_voice import ChimesdkvoiceClient
    from mypy_boto3_cleanrooms import CleanroomsserviceClient
    from mypy_boto3_cloud9 import Cloud9Client
    from mypy_boto3_cloudcontrol import CloudcontrolapiClient
    from mypy_boto3_clouddirectory import ClouddirectoryClient
    from mypy_boto3_cloudformation import CloudformationClient
    from mypy_boto3_cloudfront import CloudfrontClient
    from mypy_boto3_cloudhsm import CloudhsmClient
    from mypy_boto3_cloudhsmv2 import Cloudhsmv2Client
    from mypy_boto3_cloudsearch import CloudsearchClient
    from mypy_boto3_cloudsearchdomain import CloudsearchdomainClient
    from mypy_boto3_cloudtrail import CloudtrailClient
    from mypy_boto3_cloudtrail_data import CloudtraildataserviceClient
    from mypy_boto3_cloudwatch import CloudwatchClient
    from mypy_boto3_codeartifact import CodeartifactClient
    from mypy_boto3_codebuild import CodebuildClient
    from mypy_boto3_codecatalyst import CodecatalystClient
    from mypy_boto3_codecommit import CodecommitClient
    from mypy_boto3_codedeploy import CodedeployClient
    from mypy_boto3_codeguru_reviewer import CodegurureviewerClient
    from mypy_boto3_codeguruprofiler import CodeguruprofilerClient
    from mypy_boto3_codepipeline import CodepipelineClient
    from mypy_boto3_codestar import CodestarClient
    from mypy_boto3_codestar_connections import CodestarconnectionsClient
    from mypy_boto3_codestar_notifications import CodestarnotificationsClient
    from mypy_boto3_cognito_identity import CognitoidentityClient
    from mypy_boto3_cognito_idp import CognitoidentityproviderClient
    from mypy_boto3_cognito_sync import CognitosyncClient
    from mypy_boto3_comprehend import ComprehendClient
    from mypy_boto3_comprehendmedical import ComprehendmedicalClient
    from mypy_boto3_compute_optimizer import ComputeoptimizerClient
    from mypy_boto3_config import ConfigserviceClient
    from mypy_boto3_connect import ConnectClient
    from mypy_boto3_connect_contact_lens import ConnectcontactlensClient
    from mypy_boto3_connectcampaigns import ConnectcampaignserviceClient
    from mypy_boto3_connectcases import ConnectcasesClient
    from mypy_boto3_connectparticipant import ConnectparticipantClient
    from mypy_boto3_controltower import ControltowerClient
    from mypy_boto3_cur import CostandusagereportserviceClient
    from mypy_boto3_customer_profiles import CustomerprofilesClient
    from mypy_boto3_databrew import GluedatabrewClient
    from mypy_boto3_dataexchange import DataexchangeClient
    from mypy_boto3_datapipeline import DatapipelineClient
    from mypy_boto3_datasync import DatasyncClient
    from mypy_boto3_dax import DaxClient
    from mypy_boto3_detective import DetectiveClient
    from mypy_boto3_devicefarm import DevicefarmClient
    from mypy_boto3_devops_guru import DevopsguruClient
    from mypy_boto3_directconnect import DirectconnectClient
    from mypy_boto3_discovery import ApplicationdiscoveryserviceClient
    from mypy_boto3_dlm import DlmClient
    from mypy_boto3_dms import DatabasemigrationserviceClient
    from mypy_boto3_docdb import DocdbClient
    from mypy_boto3_docdb_elastic import DocdbelasticClient
    from mypy_boto3_drs import DrsClient
    from mypy_boto3_ds import DirectoryserviceClient
    from mypy_boto3_dynamodb import DynamodbClient
    from mypy_boto3_dynamodbstreams import DynamodbstreamsClient
    from mypy_boto3_ebs import EbsClient
    from mypy_boto3_ec2 import Ec2Client
    from mypy_boto3_ec2_instance_connect import Ec2instanceconnectClient
    from mypy_boto3_ecr import EcrClient
    from mypy_boto3_ecr_public import EcrpublicClient
    from mypy_boto3_ecs import EcsClient
    from mypy_boto3_efs import EfsClient
    from mypy_boto3_eks import EksClient
    from mypy_boto3_elastic_inference import ElasticinferenceClient
    from mypy_boto3_elasticache import ElasticacheClient
    from mypy_boto3_elasticbeanstalk import ElasticbeanstalkClient
    from mypy_boto3_elastictranscoder import ElastictranscoderClient
    from mypy_boto3_elb import ElasticloadbalancingClient
    from mypy_boto3_elbv2 import Elasticloadbalancingv2Client
    from mypy_boto3_emr import EmrClient
    from mypy_boto3_emr_containers import EmrcontainersClient
    from mypy_boto3_emr_serverless import EmrserverlessClient
    from mypy_boto3_es import ElasticsearchserviceClient
    from mypy_boto3_events import EventbridgeClient
    from mypy_boto3_evidently import CloudwatchevidentlyClient
    from mypy_boto3_finspace import FinspaceClient
    from mypy_boto3_finspace_data import FinspacedataClient
    from mypy_boto3_firehose import FirehoseClient
    from mypy_boto3_fis import FisClient
    from mypy_boto3_fms import FmsClient
    from mypy_boto3_forecast import ForecastserviceClient
    from mypy_boto3_forecastquery import ForecastqueryserviceClient
    from mypy_boto3_frauddetector import FrauddetectorClient
    from mypy_boto3_fsx import FsxClient
    from mypy_boto3_gamelift import GameliftClient
    from mypy_boto3_gamesparks import GamesparksClient
    from mypy_boto3_glacier import GlacierClient
    from mypy_boto3_globalaccelerator import GlobalacceleratorClient
    from mypy_boto3_glue import GlueClient
    from mypy_boto3_grafana import ManagedgrafanaClient
    from mypy_boto3_greengrass import GreengrassClient
    from mypy_boto3_greengrassv2 import Greengrassv2Client
    from mypy_boto3_groundstation import GroundstationClient
    from mypy_boto3_guardduty import GuarddutyClient
    from mypy_boto3_health import HealthClient
    from mypy_boto3_healthlake import HealthlakeClient
    from mypy_boto3_honeycode import HoneycodeClient
    from mypy_boto3_iam import IamClient
    from mypy_boto3_identitystore import IdentitystoreClient
    from mypy_boto3_imagebuilder import ImagebuilderClient
    from mypy_boto3_importexport import ImportexportClient
    from mypy_boto3_inspector import InspectorClient
    from mypy_boto3_inspector2 import Inspector2Client
    from mypy_boto3_internetmonitor import CloudwatchinternetmonitorClient
    from mypy_boto3_iot import IotClient
    from mypy_boto3_iot_data import IotdataplaneClient
    from mypy_boto3_iot_jobs_data import IotjobsdataplaneClient
    from mypy_boto3_iot_roborunner import IotroborunnerClient
    from mypy_boto3_iot1click_devices import Iot1clickdevicesserviceClient
    from mypy_boto3_iot1click_projects import Iot1clickprojectsClient
    from mypy_boto3_iotanalytics import IotanalyticsClient
    from mypy_boto3_iotdeviceadvisor import IotdeviceadvisorClient
    from mypy_boto3_iotevents import IoteventsClient
    from mypy_boto3_iotevents_data import IoteventsdataClient
    from mypy_boto3_iotfleethub import IotfleethubClient
    from mypy_boto3_iotfleetwise import IotfleetwiseClient
    from mypy_boto3_iotsecuretunneling import IotsecuretunnelingClient
    from mypy_boto3_iotsitewise import IotsitewiseClient
    from mypy_boto3_iotthingsgraph import IotthingsgraphClient
    from mypy_boto3_iottwinmaker import IottwinmakerClient
    from mypy_boto3_iotwireless import IotwirelessClient
    from mypy_boto3_ivs import IvsClient
    from mypy_boto3_ivschat import IvschatClient
    from mypy_boto3_kafka import KafkaClient
    from mypy_boto3_kafkaconnect import KafkaconnectClient
    from mypy_boto3_kendra import KendraClient
    from mypy_boto3_kendra_ranking import KendrarankingClient
    from mypy_boto3_keyspaces import KeyspacesClient
    from mypy_boto3_kinesis import KinesisClient
    from mypy_boto3_kinesis_video_archived_media import KinesisvideoarchivedmediaClient
    from mypy_boto3_kinesis_video_media import KinesisvideomediaClient
    from mypy_boto3_kinesis_video_signaling import KinesisvideosignalingchannelsClient
    from mypy_boto3_kinesis_video_webrtc_storage import KinesisvideowebrtcstorageClient
    from mypy_boto3_kinesisanalytics import KinesisanalyticsClient
    from mypy_boto3_kinesisanalyticsv2 import Kinesisanalyticsv2Client
    from mypy_boto3_kinesisvideo import KinesisvideoClient
    from mypy_boto3_kms import KmsClient
    from mypy_boto3_lakeformation import LakeformationClient
    from mypy_boto3_lambda import LambdaClient
    from mypy_boto3_lex_models import LexmodelbuildingserviceClient
    from mypy_boto3_lex_runtime import LexruntimeserviceClient
    from mypy_boto3_lexv2_models import Lexmodelsv2Client
    from mypy_boto3_lexv2_runtime import Lexruntimev2Client
    from mypy_boto3_license_manager import LicensemanagerClient
    from mypy_boto3_license_manager_linux_subscriptions import LicensemanagerlinuxsubscriptionsClient
    from mypy_boto3_license_manager_user_subscriptions import LicensemanagerusersubscriptionsClient
    from mypy_boto3_lightsail import LightsailClient
    from mypy_boto3_location import LocationserviceClient
    from mypy_boto3_logs import CloudwatchlogsClient
    from mypy_boto3_lookoutequipment import LookoutequipmentClient
    from mypy_boto3_lookoutmetrics import LookoutmetricsClient
    from mypy_boto3_lookoutvision import LookoutforvisionClient
    from mypy_boto3_m2 import MainframemodernizationClient
    from mypy_boto3_machinelearning import MachinelearningClient
    from mypy_boto3_macie import MacieClient
    from mypy_boto3_macie2 import Macie2Client
    from mypy_boto3_managedblockchain import ManagedblockchainClient
    from mypy_boto3_marketplace_catalog import MarketplacecatalogClient
    from mypy_boto3_marketplace_entitlement import MarketplaceentitlementserviceClient
    from mypy_boto3_marketplacecommerceanalytics import MarketplacecommerceanalyticsClient
    from mypy_boto3_mediaconnect import MediaconnectClient
    from mypy_boto3_mediaconvert import MediaconvertClient
    from mypy_boto3_medialive import MedialiveClient
    from mypy_boto3_mediapackage import MediapackageClient
    from mypy_boto3_mediapackage_vod import MediapackagevodClient
    from mypy_boto3_mediastore import MediastoreClient
    from mypy_boto3_mediastore_data import MediastoredataClient
    from mypy_boto3_mediatailor import MediatailorClient
    from mypy_boto3_memorydb import MemorydbClient
    from mypy_boto3_meteringmarketplace import MarketplacemeteringClient
    from mypy_boto3_mgh import MigrationhubClient
    from mypy_boto3_mgn import MgnClient
    from mypy_boto3_migration_hub_refactor_spaces import MigrationhubrefactorspacesClient
    from mypy_boto3_migrationhub_config import MigrationhubconfigClient
    from mypy_boto3_migrationhuborchestrator import MigrationhuborchestratorClient
    from mypy_boto3_migrationhubstrategy import MigrationhubstrategyrecommendationsClient
    from mypy_boto3_mobile import MobileClient
    from mypy_boto3_mq import MqClient
    from mypy_boto3_mturk import MturkClient
    from mypy_boto3_mwaa import MwaaClient
    from mypy_boto3_neptune import NeptuneClient
    from mypy_boto3_network_firewall import NetworkfirewallClient
    from mypy_boto3_networkmanager import NetworkmanagerClient
    from mypy_boto3_nimble import NimblestudioClient
    from mypy_boto3_oam import CloudwatchobservabilityaccessmanagerClient
    from mypy_boto3_omics import OmicsClient
    from mypy_boto3_opensearch import OpensearchserviceClient
    from mypy_boto3_opensearchserverless import OpensearchserviceserverlessClient
    from mypy_boto3_opsworks import OpsworksClient
    from mypy_boto3_opsworkscm import OpsworkscmClient
    from mypy_boto3_organizations import OrganizationsClient
    from mypy_boto3_outposts import OutpostsClient
    from mypy_boto3_panorama import PanoramaClient
    from mypy_boto3_personalize import PersonalizeClient
    from mypy_boto3_personalize_events import PersonalizeeventsClient
    from mypy_boto3_personalize_runtime import PersonalizeruntimeClient
    from mypy_boto3_pi import PiClient
    from mypy_boto3_pinpoint import PinpointClient
    from mypy_boto3_pinpoint_email import PinpointemailClient
    from mypy_boto3_pinpoint_sms_voice import PinpointsmsvoiceClient
    from mypy_boto3_pinpoint_sms_voice_v2 import Pinpointsmsvoicev2Client
    from mypy_boto3_pipes import EventbridgepipesClient
    from mypy_boto3_polly import PollyClient
    from mypy_boto3_pricing import PricingClient
    from mypy_boto3_privatenetworks import Private5gClient
    from mypy_boto3_proton import ProtonClient
    from mypy_boto3_qldb import QldbClient
    from mypy_boto3_qldb_session import QldbsessionClient
    from mypy_boto3_quicksight import QuicksightClient
    from mypy_boto3_ram import RamClient
    from mypy_boto3_rbin import RecyclebinClient
    from mypy_boto3_rds import RdsClient
    from mypy_boto3_rds_data import RdsdataserviceClient
    from mypy_boto3_redshift import RedshiftClient
    from mypy_boto3_redshift_data import RedshiftdataapiserviceClient
    from mypy_boto3_redshift_serverless import RedshiftserverlessClient
    from mypy_boto3_rekognition import RekognitionClient
    from mypy_boto3_resiliencehub import ResiliencehubClient
    from mypy_boto3_resource_explorer_2 import ResourceexplorerClient
    from mypy_boto3_resource_groups import ResourcegroupsClient
    from mypy_boto3_resourcegroupstaggingapi import ResourcegroupstaggingapiClient
    from mypy_boto3_robomaker import RobomakerClient
    from mypy_boto3_rolesanywhere import IamrolesanywhereClient
    from mypy_boto3_route53 import Route53Client
    from mypy_boto3_route53_recovery_cluster import Route53recoveryclusterClient
    from mypy_boto3_route53_recovery_control_config import Route53recoverycontrolconfigClient
    from mypy_boto3_route53_recovery_readiness import Route53recoveryreadinessClient
    from mypy_boto3_route53domains import Route53domainsClient
    from mypy_boto3_route53resolver import Route53resolverClient
    from mypy_boto3_rum import CloudwatchrumClient
    from mypy_boto3_s3 import S3Client
    from mypy_boto3_s3control import S3controlClient
    from mypy_boto3_s3outposts import S3outpostsClient
    from mypy_boto3_sagemaker import SagemakerClient
    from mypy_boto3_sagemaker_a2i_runtime import AugmentedairuntimeClient
    from mypy_boto3_sagemaker_edge import SagemakeredgemanagerClient
    from mypy_boto3_sagemaker_featurestore_runtime import SagemakerfeaturestoreruntimeClient
    from mypy_boto3_sagemaker_geospatial import SagemakergeospatialcapabilitiesClient
    from mypy_boto3_sagemaker_metrics import SagemakermetricsClient
    from mypy_boto3_sagemaker_runtime import SagemakerruntimeClient
    from mypy_boto3_savingsplans import SavingsplansClient
    from mypy_boto3_scheduler import EventbridgeschedulerClient
    from mypy_boto3_schemas import SchemasClient
    from mypy_boto3_sdb import SimpledbClient
    from mypy_boto3_secretsmanager import SecretsmanagerClient
    from mypy_boto3_securityhub import SecurityhubClient
    from mypy_boto3_securitylake import SecuritylakeClient
    from mypy_boto3_serverlessrepo import ServerlessapplicationrepositoryClient
    from mypy_boto3_service_quotas import ServicequotasClient
    from mypy_boto3_servicecatalog import ServicecatalogClient
    from mypy_boto3_servicecatalog_appregistry import AppregistryClient
    from mypy_boto3_servicediscovery import ServicediscoveryClient
    from mypy_boto3_ses import SesClient
    from mypy_boto3_sesv2 import Sesv2Client
    from mypy_boto3_shield import ShieldClient
    from mypy_boto3_signer import SignerClient
    from mypy_boto3_simspaceweaver import SimspaceweaverClient
    from mypy_boto3_sms import SmsClient
    from mypy_boto3_sms_voice import PinpointsmsvoiceClient
    from mypy_boto3_snow_device_management import SnowdevicemanagementClient
    from mypy_boto3_snowball import SnowballClient
    from mypy_boto3_sns import SnsClient
    from mypy_boto3_sqs import SqsClient
    from mypy_boto3_ssm import SsmClient
    from mypy_boto3_ssm_contacts import SsmcontactsClient
    from mypy_boto3_ssm_incidents import SsmincidentsClient
    from mypy_boto3_ssm_sap import SsmsapClient
    from mypy_boto3_sso import SsoClient
    from mypy_boto3_sso_admin import SsoadminClient
    from mypy_boto3_sso_oidc import SsooidcClient
    from mypy_boto3_stepfunctions import SfnClient
    from mypy_boto3_storagegateway import StoragegatewayClient
    from mypy_boto3_sts import StsClient
    from mypy_boto3_support import SupportClient
    from mypy_boto3_support_app import SupportappClient
    from mypy_boto3_swf import SwfClient
    from mypy_boto3_synthetics import SyntheticsClient
    from mypy_boto3_textract import TextractClient
    from mypy_boto3_timestream_query import TimestreamqueryClient
    from mypy_boto3_timestream_write import TimestreamwriteClient
    from mypy_boto3_tnb import TelconetworkbuilderClient
    from mypy_boto3_transcribe import TranscribeserviceClient
    from mypy_boto3_transfer import TransferClient
    from mypy_boto3_translate import TranslateClient
    from mypy_boto3_voice_id import VoiceidClient
    from mypy_boto3_waf import WafClient
    from mypy_boto3_waf_regional import WafregionalClient
    from mypy_boto3_wafv2 import Wafv2Client
    from mypy_boto3_wellarchitected import WellarchitectedClient
    from mypy_boto3_wisdom import ConnectwisdomserviceClient
    from mypy_boto3_workdocs import WorkdocsClient
    from mypy_boto3_worklink import WorklinkClient
    from mypy_boto3_workmail import WorkmailClient
    from mypy_boto3_workmailmessageflow import WorkmailmessageflowClient
    from mypy_boto3_workspaces import WorkspacesClient
    from mypy_boto3_workspaces_web import WorkspaceswebClient
    from mypy_boto3_xray import XrayClient

class ClientMixin:
    
    @property
    def accessanalyzer_client(self: "BotoSesManager") -> "AccessanalyzerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer.html
        """
        return self.get_client(AwsServiceEnum.AccessAnalyzer)
    
    @property
    def account_client(self: "BotoSesManager") -> "AccountClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html
        """
        return self.get_client(AwsServiceEnum.Account)
    
    @property
    def acm_client(self: "BotoSesManager") -> "AcmClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm.html
        """
        return self.get_client(AwsServiceEnum.ACM)
    
    @property
    def acmpca_client(self: "BotoSesManager") -> "AcmpcaClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca.html
        """
        return self.get_client(AwsServiceEnum.ACMPCA)
    
    @property
    def alexaforbusiness_client(self: "BotoSesManager") -> "AlexaforbusinessClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/alexaforbusiness.html
        """
        return self.get_client(AwsServiceEnum.AlexaForBusiness)
    
    @property
    def prometheusservice_client(self: "BotoSesManager") -> "PrometheusserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amp.html
        """
        return self.get_client(AwsServiceEnum.PrometheusService)
    
    @property
    def amplify_client(self: "BotoSesManager") -> "AmplifyClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify.html
        """
        return self.get_client(AwsServiceEnum.Amplify)
    
    @property
    def amplifybackend_client(self: "BotoSesManager") -> "AmplifybackendClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifybackend.html
        """
        return self.get_client(AwsServiceEnum.AmplifyBackend)
    
    @property
    def amplifyuibuilder_client(self: "BotoSesManager") -> "AmplifyuibuilderClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html
        """
        return self.get_client(AwsServiceEnum.AmplifyUIBuilder)
    
    @property
    def apigateway_client(self: "BotoSesManager") -> "ApigatewayClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html
        """
        return self.get_client(AwsServiceEnum.APIGateway)
    
    @property
    def apigatewaymanagementapi_client(self: "BotoSesManager") -> "ApigatewaymanagementapiClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi.html
        """
        return self.get_client(AwsServiceEnum.ApiGatewayManagementApi)
    
    @property
    def apigatewayv2_client(self: "BotoSesManager") -> "Apigatewayv2Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewayv2.html
        """
        return self.get_client(AwsServiceEnum.ApiGatewayV2)
    
    @property
    def appconfig_client(self: "BotoSesManager") -> "AppconfigClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfig.html
        """
        return self.get_client(AwsServiceEnum.AppConfig)
    
    @property
    def appconfigdata_client(self: "BotoSesManager") -> "AppconfigdataClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appconfigdata.html
        """
        return self.get_client(AwsServiceEnum.AppConfigData)
    
    @property
    def appflow_client(self: "BotoSesManager") -> "AppflowClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html
        """
        return self.get_client(AwsServiceEnum.Appflow)
    
    @property
    def appintegrationsservice_client(self: "BotoSesManager") -> "AppintegrationsserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appintegrations.html
        """
        return self.get_client(AwsServiceEnum.AppIntegrationsService)
    
    @property
    def applicationautoscaling_client(self: "BotoSesManager") -> "ApplicationautoscalingClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling.html
        """
        return self.get_client(AwsServiceEnum.ApplicationAutoScaling)
    
    @property
    def applicationinsights_client(self: "BotoSesManager") -> "ApplicationinsightsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html
        """
        return self.get_client(AwsServiceEnum.ApplicationInsights)
    
    @property
    def applicationcostprofiler_client(self: "BotoSesManager") -> "ApplicationcostprofilerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/applicationcostprofiler.html
        """
        return self.get_client(AwsServiceEnum.ApplicationCostProfiler)
    
    @property
    def appmesh_client(self: "BotoSesManager") -> "AppmeshClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appmesh.html
        """
        return self.get_client(AwsServiceEnum.AppMesh)
    
    @property
    def apprunner_client(self: "BotoSesManager") -> "ApprunnerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apprunner.html
        """
        return self.get_client(AwsServiceEnum.AppRunner)
    
    @property
    def appstream_client(self: "BotoSesManager") -> "AppstreamClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html
        """
        return self.get_client(AwsServiceEnum.AppStream)
    
    @property
    def appsync_client(self: "BotoSesManager") -> "AppsyncClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html
        """
        return self.get_client(AwsServiceEnum.AppSync)
    
    @property
    def arczonalshift_client(self: "BotoSesManager") -> "ArczonalshiftClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift.html
        """
        return self.get_client(AwsServiceEnum.ARCZonalShift)
    
    @property
    def athena_client(self: "BotoSesManager") -> "AthenaClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html
        """
        return self.get_client(AwsServiceEnum.Athena)
    
    @property
    def auditmanager_client(self: "BotoSesManager") -> "AuditmanagerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html
        """
        return self.get_client(AwsServiceEnum.AuditManager)
    
    @property
    def autoscaling_client(self: "BotoSesManager") -> "AutoscalingClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling.html
        """
        return self.get_client(AwsServiceEnum.AutoScaling)
    
    @property
    def autoscalingplans_client(self: "BotoSesManager") -> "AutoscalingplansClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling-plans.html
        """
        return self.get_client(AwsServiceEnum.AutoScalingPlans)
    
    @property
    def backup_client(self: "BotoSesManager") -> "BackupClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup.html
        """
        return self.get_client(AwsServiceEnum.Backup)
    
    @property
    def backupgateway_client(self: "BotoSesManager") -> "BackupgatewayClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backup-gateway.html
        """
        return self.get_client(AwsServiceEnum.BackupGateway)
    
    @property
    def backupstorage_client(self: "BotoSesManager") -> "BackupstorageClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/backupstorage.html
        """
        return self.get_client(AwsServiceEnum.BackupStorage)
    
    @property
    def batch_client(self: "BotoSesManager") -> "BatchClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html
        """
        return self.get_client(AwsServiceEnum.Batch)
    
    @property
    def billingconductor_client(self: "BotoSesManager") -> "BillingconductorClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor.html
        """
        return self.get_client(AwsServiceEnum.BillingConductor)
    
    @property
    def braket_client(self: "BotoSesManager") -> "BraketClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html
        """
        return self.get_client(AwsServiceEnum.Braket)
    
    @property
    def budgets_client(self: "BotoSesManager") -> "BudgetsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/budgets.html
        """
        return self.get_client(AwsServiceEnum.Budgets)
    
    @property
    def costexplorer_client(self: "BotoSesManager") -> "CostexplorerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html
        """
        return self.get_client(AwsServiceEnum.CostExplorer)
    
    @property
    def chime_client(self: "BotoSesManager") -> "ChimeClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime.html
        """
        return self.get_client(AwsServiceEnum.Chime)
    
    @property
    def chimesdkidentity_client(self: "BotoSesManager") -> "ChimesdkidentityClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity.html
        """
        return self.get_client(AwsServiceEnum.ChimeSDKIdentity)
    
    @property
    def chimesdkmediapipelines_client(self: "BotoSesManager") -> "ChimesdkmediapipelinesClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-media-pipelines.html
        """
        return self.get_client(AwsServiceEnum.ChimeSDKMediaPipelines)
    
    @property
    def chimesdkmeetings_client(self: "BotoSesManager") -> "ChimesdkmeetingsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-meetings.html
        """
        return self.get_client(AwsServiceEnum.ChimeSDKMeetings)
    
    @property
    def chimesdkmessaging_client(self: "BotoSesManager") -> "ChimesdkmessagingClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-messaging.html
        """
        return self.get_client(AwsServiceEnum.ChimeSDKMessaging)
    
    @property
    def chimesdkvoice_client(self: "BotoSesManager") -> "ChimesdkvoiceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-voice.html
        """
        return self.get_client(AwsServiceEnum.ChimeSDKVoice)
    
    @property
    def cleanroomsservice_client(self: "BotoSesManager") -> "CleanroomsserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanrooms.html
        """
        return self.get_client(AwsServiceEnum.CleanRoomsService)
    
    @property
    def cloud9_client(self: "BotoSesManager") -> "Cloud9Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html
        """
        return self.get_client(AwsServiceEnum.Cloud9)
    
    @property
    def cloudcontrolapi_client(self: "BotoSesManager") -> "CloudcontrolapiClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol.html
        """
        return self.get_client(AwsServiceEnum.CloudControlApi)
    
    @property
    def clouddirectory_client(self: "BotoSesManager") -> "ClouddirectoryClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html
        """
        return self.get_client(AwsServiceEnum.CloudDirectory)
    
    @property
    def cloudformation_client(self: "BotoSesManager") -> "CloudformationClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html
        """
        return self.get_client(AwsServiceEnum.CloudFormation)
    
    @property
    def cloudfront_client(self: "BotoSesManager") -> "CloudfrontClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html
        """
        return self.get_client(AwsServiceEnum.CloudFront)
    
    @property
    def cloudhsm_client(self: "BotoSesManager") -> "CloudhsmClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsm.html
        """
        return self.get_client(AwsServiceEnum.CloudHSM)
    
    @property
    def cloudhsmv2_client(self: "BotoSesManager") -> "Cloudhsmv2Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html
        """
        return self.get_client(AwsServiceEnum.CloudHSMV2)
    
    @property
    def cloudsearch_client(self: "BotoSesManager") -> "CloudsearchClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearch.html
        """
        return self.get_client(AwsServiceEnum.CloudSearch)
    
    @property
    def cloudsearchdomain_client(self: "BotoSesManager") -> "CloudsearchdomainClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudsearchdomain.html
        """
        return self.get_client(AwsServiceEnum.CloudSearchDomain)
    
    @property
    def cloudtrail_client(self: "BotoSesManager") -> "CloudtrailClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html
        """
        return self.get_client(AwsServiceEnum.CloudTrail)
    
    @property
    def cloudtraildataservice_client(self: "BotoSesManager") -> "CloudtraildataserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail-data.html
        """
        return self.get_client(AwsServiceEnum.CloudTrailDataService)
    
    @property
    def cloudwatch_client(self: "BotoSesManager") -> "CloudwatchClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html
        """
        return self.get_client(AwsServiceEnum.CloudWatch)
    
    @property
    def codeartifact_client(self: "BotoSesManager") -> "CodeartifactClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html
        """
        return self.get_client(AwsServiceEnum.CodeArtifact)
    
    @property
    def codebuild_client(self: "BotoSesManager") -> "CodebuildClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html
        """
        return self.get_client(AwsServiceEnum.CodeBuild)
    
    @property
    def codecatalyst_client(self: "BotoSesManager") -> "CodecatalystClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecatalyst.html
        """
        return self.get_client(AwsServiceEnum.CodeCatalyst)
    
    @property
    def codecommit_client(self: "BotoSesManager") -> "CodecommitClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html
        """
        return self.get_client(AwsServiceEnum.CodeCommit)
    
    @property
    def codedeploy_client(self: "BotoSesManager") -> "CodedeployClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codedeploy.html
        """
        return self.get_client(AwsServiceEnum.CodeDeploy)
    
    @property
    def codegurureviewer_client(self: "BotoSesManager") -> "CodegurureviewerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguru-reviewer.html
        """
        return self.get_client(AwsServiceEnum.CodeGuruReviewer)
    
    @property
    def codeguruprofiler_client(self: "BotoSesManager") -> "CodeguruprofilerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeguruprofiler.html
        """
        return self.get_client(AwsServiceEnum.CodeGuruProfiler)
    
    @property
    def codepipeline_client(self: "BotoSesManager") -> "CodepipelineClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html
        """
        return self.get_client(AwsServiceEnum.CodePipeline)
    
    @property
    def codestar_client(self: "BotoSesManager") -> "CodestarClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar.html
        """
        return self.get_client(AwsServiceEnum.CodeStar)
    
    @property
    def codestarconnections_client(self: "BotoSesManager") -> "CodestarconnectionsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-connections.html
        """
        return self.get_client(AwsServiceEnum.CodeStarconnections)
    
    @property
    def codestarnotifications_client(self: "BotoSesManager") -> "CodestarnotificationsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html
        """
        return self.get_client(AwsServiceEnum.CodeStarNotifications)
    
    @property
    def cognitoidentity_client(self: "BotoSesManager") -> "CognitoidentityClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html
        """
        return self.get_client(AwsServiceEnum.CognitoIdentity)
    
    @property
    def cognitoidentityprovider_client(self: "BotoSesManager") -> "CognitoidentityproviderClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html
        """
        return self.get_client(AwsServiceEnum.CognitoIdentityProvider)
    
    @property
    def cognitosync_client(self: "BotoSesManager") -> "CognitosyncClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html
        """
        return self.get_client(AwsServiceEnum.CognitoSync)
    
    @property
    def comprehend_client(self: "BotoSesManager") -> "ComprehendClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html
        """
        return self.get_client(AwsServiceEnum.Comprehend)
    
    @property
    def comprehendmedical_client(self: "BotoSesManager") -> "ComprehendmedicalClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehendmedical.html
        """
        return self.get_client(AwsServiceEnum.ComprehendMedical)
    
    @property
    def computeoptimizer_client(self: "BotoSesManager") -> "ComputeoptimizerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer.html
        """
        return self.get_client(AwsServiceEnum.ComputeOptimizer)
    
    @property
    def configservice_client(self: "BotoSesManager") -> "ConfigserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html
        """
        return self.get_client(AwsServiceEnum.ConfigService)
    
    @property
    def connect_client(self: "BotoSesManager") -> "ConnectClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html
        """
        return self.get_client(AwsServiceEnum.Connect)
    
    @property
    def connectcontactlens_client(self: "BotoSesManager") -> "ConnectcontactlensClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect-contact-lens.html
        """
        return self.get_client(AwsServiceEnum.ConnectContactLens)
    
    @property
    def connectcampaignservice_client(self: "BotoSesManager") -> "ConnectcampaignserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcampaigns.html
        """
        return self.get_client(AwsServiceEnum.ConnectCampaignService)
    
    @property
    def connectcases_client(self: "BotoSesManager") -> "ConnectcasesClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectcases.html
        """
        return self.get_client(AwsServiceEnum.ConnectCases)
    
    @property
    def connectparticipant_client(self: "BotoSesManager") -> "ConnectparticipantClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connectparticipant.html
        """
        return self.get_client(AwsServiceEnum.ConnectParticipant)
    
    @property
    def controltower_client(self: "BotoSesManager") -> "ControltowerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html
        """
        return self.get_client(AwsServiceEnum.ControlTower)
    
    @property
    def costandusagereportservice_client(self: "BotoSesManager") -> "CostandusagereportserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cur.html
        """
        return self.get_client(AwsServiceEnum.CostandUsageReportService)
    
    @property
    def customerprofiles_client(self: "BotoSesManager") -> "CustomerprofilesClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html
        """
        return self.get_client(AwsServiceEnum.CustomerProfiles)
    
    @property
    def gluedatabrew_client(self: "BotoSesManager") -> "GluedatabrewClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/databrew.html
        """
        return self.get_client(AwsServiceEnum.GlueDataBrew)
    
    @property
    def dataexchange_client(self: "BotoSesManager") -> "DataexchangeClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html
        """
        return self.get_client(AwsServiceEnum.DataExchange)
    
    @property
    def datapipeline_client(self: "BotoSesManager") -> "DatapipelineClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html
        """
        return self.get_client(AwsServiceEnum.DataPipeline)
    
    @property
    def datasync_client(self: "BotoSesManager") -> "DatasyncClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datasync.html
        """
        return self.get_client(AwsServiceEnum.DataSync)
    
    @property
    def dax_client(self: "BotoSesManager") -> "DaxClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dax.html
        """
        return self.get_client(AwsServiceEnum.DAX)
    
    @property
    def detective_client(self: "BotoSesManager") -> "DetectiveClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/detective.html
        """
        return self.get_client(AwsServiceEnum.Detective)
    
    @property
    def devicefarm_client(self: "BotoSesManager") -> "DevicefarmClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html
        """
        return self.get_client(AwsServiceEnum.DeviceFarm)
    
    @property
    def devopsguru_client(self: "BotoSesManager") -> "DevopsguruClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html
        """
        return self.get_client(AwsServiceEnum.DevOpsGuru)
    
    @property
    def directconnect_client(self: "BotoSesManager") -> "DirectconnectClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect.html
        """
        return self.get_client(AwsServiceEnum.DirectConnect)
    
    @property
    def applicationdiscoveryservice_client(self: "BotoSesManager") -> "ApplicationdiscoveryserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/discovery.html
        """
        return self.get_client(AwsServiceEnum.ApplicationDiscoveryService)
    
    @property
    def dlm_client(self: "BotoSesManager") -> "DlmClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html
        """
        return self.get_client(AwsServiceEnum.DLM)
    
    @property
    def databasemigrationservice_client(self: "BotoSesManager") -> "DatabasemigrationserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html
        """
        return self.get_client(AwsServiceEnum.DatabaseMigrationService)
    
    @property
    def docdb_client(self: "BotoSesManager") -> "DocdbClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb.html
        """
        return self.get_client(AwsServiceEnum.DocDB)
    
    @property
    def docdbelastic_client(self: "BotoSesManager") -> "DocdbelasticClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html
        """
        return self.get_client(AwsServiceEnum.DocDBElastic)
    
    @property
    def drs_client(self: "BotoSesManager") -> "DrsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/drs.html
        """
        return self.get_client(AwsServiceEnum.drs)
    
    @property
    def directoryservice_client(self: "BotoSesManager") -> "DirectoryserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html
        """
        return self.get_client(AwsServiceEnum.DirectoryService)
    
    @property
    def dynamodb_client(self: "BotoSesManager") -> "DynamodbClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html
        """
        return self.get_client(AwsServiceEnum.DynamoDB)
    
    @property
    def dynamodbstreams_client(self: "BotoSesManager") -> "DynamodbstreamsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams.html
        """
        return self.get_client(AwsServiceEnum.DynamoDBStreams)
    
    @property
    def ebs_client(self: "BotoSesManager") -> "EbsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html
        """
        return self.get_client(AwsServiceEnum.EBS)
    
    @property
    def ec2_client(self: "BotoSesManager") -> "Ec2Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html
        """
        return self.get_client(AwsServiceEnum.EC2)
    
    @property
    def ec2instanceconnect_client(self: "BotoSesManager") -> "Ec2instanceconnectClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect.html
        """
        return self.get_client(AwsServiceEnum.EC2InstanceConnect)
    
    @property
    def ecr_client(self: "BotoSesManager") -> "EcrClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html
        """
        return self.get_client(AwsServiceEnum.ECR)
    
    @property
    def ecrpublic_client(self: "BotoSesManager") -> "EcrpublicClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr-public.html
        """
        return self.get_client(AwsServiceEnum.ECRPublic)
    
    @property
    def ecs_client(self: "BotoSesManager") -> "EcsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html
        """
        return self.get_client(AwsServiceEnum.ECS)
    
    @property
    def efs_client(self: "BotoSesManager") -> "EfsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/efs.html
        """
        return self.get_client(AwsServiceEnum.EFS)
    
    @property
    def eks_client(self: "BotoSesManager") -> "EksClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/eks.html
        """
        return self.get_client(AwsServiceEnum.EKS)
    
    @property
    def elasticinference_client(self: "BotoSesManager") -> "ElasticinferenceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastic-inference.html
        """
        return self.get_client(AwsServiceEnum.ElasticInference)
    
    @property
    def elasticache_client(self: "BotoSesManager") -> "ElasticacheClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html
        """
        return self.get_client(AwsServiceEnum.ElastiCache)
    
    @property
    def elasticbeanstalk_client(self: "BotoSesManager") -> "ElasticbeanstalkClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticbeanstalk.html
        """
        return self.get_client(AwsServiceEnum.ElasticBeanstalk)
    
    @property
    def elastictranscoder_client(self: "BotoSesManager") -> "ElastictranscoderClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elastictranscoder.html
        """
        return self.get_client(AwsServiceEnum.ElasticTranscoder)
    
    @property
    def elasticloadbalancing_client(self: "BotoSesManager") -> "ElasticloadbalancingClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb.html
        """
        return self.get_client(AwsServiceEnum.ElasticLoadBalancing)
    
    @property
    def elasticloadbalancingv2_client(self: "BotoSesManager") -> "Elasticloadbalancingv2Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html
        """
        return self.get_client(AwsServiceEnum.ElasticLoadBalancingv2)
    
    @property
    def emr_client(self: "BotoSesManager") -> "EmrClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html
        """
        return self.get_client(AwsServiceEnum.EMR)
    
    @property
    def emrcontainers_client(self: "BotoSesManager") -> "EmrcontainersClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html
        """
        return self.get_client(AwsServiceEnum.EMRContainers)
    
    @property
    def emrserverless_client(self: "BotoSesManager") -> "EmrserverlessClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless.html
        """
        return self.get_client(AwsServiceEnum.EMRServerless)
    
    @property
    def elasticsearchservice_client(self: "BotoSesManager") -> "ElasticsearchserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/es.html
        """
        return self.get_client(AwsServiceEnum.ElasticsearchService)
    
    @property
    def eventbridge_client(self: "BotoSesManager") -> "EventbridgeClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html
        """
        return self.get_client(AwsServiceEnum.EventBridge)
    
    @property
    def cloudwatchevidently_client(self: "BotoSesManager") -> "CloudwatchevidentlyClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently.html
        """
        return self.get_client(AwsServiceEnum.CloudWatchEvidently)
    
    @property
    def finspace_client(self: "BotoSesManager") -> "FinspaceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace.html
        """
        return self.get_client(AwsServiceEnum.finspace)
    
    @property
    def finspacedata_client(self: "BotoSesManager") -> "FinspacedataClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace-data.html
        """
        return self.get_client(AwsServiceEnum.FinSpaceData)
    
    @property
    def firehose_client(self: "BotoSesManager") -> "FirehoseClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/firehose.html
        """
        return self.get_client(AwsServiceEnum.Firehose)
    
    @property
    def fis_client(self: "BotoSesManager") -> "FisClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fis.html
        """
        return self.get_client(AwsServiceEnum.FIS)
    
    @property
    def fms_client(self: "BotoSesManager") -> "FmsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fms.html
        """
        return self.get_client(AwsServiceEnum.FMS)
    
    @property
    def forecastservice_client(self: "BotoSesManager") -> "ForecastserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html
        """
        return self.get_client(AwsServiceEnum.ForecastService)
    
    @property
    def forecastqueryservice_client(self: "BotoSesManager") -> "ForecastqueryserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecastquery.html
        """
        return self.get_client(AwsServiceEnum.ForecastQueryService)
    
    @property
    def frauddetector_client(self: "BotoSesManager") -> "FrauddetectorClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/frauddetector.html
        """
        return self.get_client(AwsServiceEnum.FraudDetector)
    
    @property
    def fsx_client(self: "BotoSesManager") -> "FsxClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/fsx.html
        """
        return self.get_client(AwsServiceEnum.FSx)
    
    @property
    def gamelift_client(self: "BotoSesManager") -> "GameliftClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamelift.html
        """
        return self.get_client(AwsServiceEnum.GameLift)
    
    @property
    def gamesparks_client(self: "BotoSesManager") -> "GamesparksClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gamesparks.html
        """
        return self.get_client(AwsServiceEnum.GameSparks)
    
    @property
    def glacier_client(self: "BotoSesManager") -> "GlacierClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html
        """
        return self.get_client(AwsServiceEnum.Glacier)
    
    @property
    def globalaccelerator_client(self: "BotoSesManager") -> "GlobalacceleratorClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/globalaccelerator.html
        """
        return self.get_client(AwsServiceEnum.GlobalAccelerator)
    
    @property
    def glue_client(self: "BotoSesManager") -> "GlueClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html
        """
        return self.get_client(AwsServiceEnum.Glue)
    
    @property
    def managedgrafana_client(self: "BotoSesManager") -> "ManagedgrafanaClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html
        """
        return self.get_client(AwsServiceEnum.ManagedGrafana)
    
    @property
    def greengrass_client(self: "BotoSesManager") -> "GreengrassClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html
        """
        return self.get_client(AwsServiceEnum.Greengrass)
    
    @property
    def greengrassv2_client(self: "BotoSesManager") -> "Greengrassv2Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrassv2.html
        """
        return self.get_client(AwsServiceEnum.GreengrassV2)
    
    @property
    def groundstation_client(self: "BotoSesManager") -> "GroundstationClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/groundstation.html
        """
        return self.get_client(AwsServiceEnum.GroundStation)
    
    @property
    def guardduty_client(self: "BotoSesManager") -> "GuarddutyClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html
        """
        return self.get_client(AwsServiceEnum.GuardDuty)
    
    @property
    def health_client(self: "BotoSesManager") -> "HealthClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html
        """
        return self.get_client(AwsServiceEnum.Health)
    
    @property
    def healthlake_client(self: "BotoSesManager") -> "HealthlakeClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/healthlake.html
        """
        return self.get_client(AwsServiceEnum.HealthLake)
    
    @property
    def honeycode_client(self: "BotoSesManager") -> "HoneycodeClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/honeycode.html
        """
        return self.get_client(AwsServiceEnum.Honeycode)
    
    @property
    def iam_client(self: "BotoSesManager") -> "IamClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html
        """
        return self.get_client(AwsServiceEnum.IAM)
    
    @property
    def identitystore_client(self: "BotoSesManager") -> "IdentitystoreClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/identitystore.html
        """
        return self.get_client(AwsServiceEnum.IdentityStore)
    
    @property
    def imagebuilder_client(self: "BotoSesManager") -> "ImagebuilderClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/imagebuilder.html
        """
        return self.get_client(AwsServiceEnum.imagebuilder)
    
    @property
    def importexport_client(self: "BotoSesManager") -> "ImportexportClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport.html
        """
        return self.get_client(AwsServiceEnum.ImportExport)
    
    @property
    def inspector_client(self: "BotoSesManager") -> "InspectorClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html
        """
        return self.get_client(AwsServiceEnum.Inspector)
    
    @property
    def inspector2_client(self: "BotoSesManager") -> "Inspector2Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html
        """
        return self.get_client(AwsServiceEnum.Inspector2)
    
    @property
    def cloudwatchinternetmonitor_client(self: "BotoSesManager") -> "CloudwatchinternetmonitorClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor.html
        """
        return self.get_client(AwsServiceEnum.CloudWatchInternetMonitor)
    
    @property
    def iot_client(self: "BotoSesManager") -> "IotClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html
        """
        return self.get_client(AwsServiceEnum.IoT)
    
    @property
    def iotdataplane_client(self: "BotoSesManager") -> "IotdataplaneClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-data.html
        """
        return self.get_client(AwsServiceEnum.IoTDataPlane)
    
    @property
    def iotjobsdataplane_client(self: "BotoSesManager") -> "IotjobsdataplaneClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-jobs-data.html
        """
        return self.get_client(AwsServiceEnum.IoTJobsDataPlane)
    
    @property
    def iotroborunner_client(self: "BotoSesManager") -> "IotroborunnerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-roborunner.html
        """
        return self.get_client(AwsServiceEnum.IoTRoboRunner)
    
    @property
    def iot1clickdevicesservice_client(self: "BotoSesManager") -> "Iot1clickdevicesserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-devices.html
        """
        return self.get_client(AwsServiceEnum.IoT1ClickDevicesService)
    
    @property
    def iot1clickprojects_client(self: "BotoSesManager") -> "Iot1clickprojectsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot1click-projects.html
        """
        return self.get_client(AwsServiceEnum.IoT1ClickProjects)
    
    @property
    def iotanalytics_client(self: "BotoSesManager") -> "IotanalyticsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html
        """
        return self.get_client(AwsServiceEnum.IoTAnalytics)
    
    @property
    def iotdeviceadvisor_client(self: "BotoSesManager") -> "IotdeviceadvisorClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotdeviceadvisor.html
        """
        return self.get_client(AwsServiceEnum.IoTDeviceAdvisor)
    
    @property
    def iotevents_client(self: "BotoSesManager") -> "IoteventsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents.html
        """
        return self.get_client(AwsServiceEnum.IoTEvents)
    
    @property
    def ioteventsdata_client(self: "BotoSesManager") -> "IoteventsdataClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data.html
        """
        return self.get_client(AwsServiceEnum.IoTEventsData)
    
    @property
    def iotfleethub_client(self: "BotoSesManager") -> "IotfleethubClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleethub.html
        """
        return self.get_client(AwsServiceEnum.IoTFleetHub)
    
    @property
    def iotfleetwise_client(self: "BotoSesManager") -> "IotfleetwiseClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotfleetwise.html
        """
        return self.get_client(AwsServiceEnum.IoTFleetWise)
    
    @property
    def iotsecuretunneling_client(self: "BotoSesManager") -> "IotsecuretunnelingClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsecuretunneling.html
        """
        return self.get_client(AwsServiceEnum.IoTSecureTunneling)
    
    @property
    def iotsitewise_client(self: "BotoSesManager") -> "IotsitewiseClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html
        """
        return self.get_client(AwsServiceEnum.IoTSiteWise)
    
    @property
    def iotthingsgraph_client(self: "BotoSesManager") -> "IotthingsgraphClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph.html
        """
        return self.get_client(AwsServiceEnum.IoTThingsGraph)
    
    @property
    def iottwinmaker_client(self: "BotoSesManager") -> "IottwinmakerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iottwinmaker.html
        """
        return self.get_client(AwsServiceEnum.IoTTwinMaker)
    
    @property
    def iotwireless_client(self: "BotoSesManager") -> "IotwirelessClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotwireless.html
        """
        return self.get_client(AwsServiceEnum.IoTWireless)
    
    @property
    def ivs_client(self: "BotoSesManager") -> "IvsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivs.html
        """
        return self.get_client(AwsServiceEnum.IVS)
    
    @property
    def ivschat_client(self: "BotoSesManager") -> "IvschatClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ivschat.html
        """
        return self.get_client(AwsServiceEnum.ivschat)
    
    @property
    def kafka_client(self: "BotoSesManager") -> "KafkaClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafka.html
        """
        return self.get_client(AwsServiceEnum.Kafka)
    
    @property
    def kafkaconnect_client(self: "BotoSesManager") -> "KafkaconnectClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kafkaconnect.html
        """
        return self.get_client(AwsServiceEnum.KafkaConnect)
    
    @property
    def kendra_client(self: "BotoSesManager") -> "KendraClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html
        """
        return self.get_client(AwsServiceEnum.kendra)
    
    @property
    def kendraranking_client(self: "BotoSesManager") -> "KendrarankingClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html
        """
        return self.get_client(AwsServiceEnum.KendraRanking)
    
    @property
    def keyspaces_client(self: "BotoSesManager") -> "KeyspacesClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspaces.html
        """
        return self.get_client(AwsServiceEnum.Keyspaces)
    
    @property
    def kinesis_client(self: "BotoSesManager") -> "KinesisClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html
        """
        return self.get_client(AwsServiceEnum.Kinesis)
    
    @property
    def kinesisvideoarchivedmedia_client(self: "BotoSesManager") -> "KinesisvideoarchivedmediaClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-archived-media.html
        """
        return self.get_client(AwsServiceEnum.KinesisVideoArchivedMedia)
    
    @property
    def kinesisvideomedia_client(self: "BotoSesManager") -> "KinesisvideomediaClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-media.html
        """
        return self.get_client(AwsServiceEnum.KinesisVideoMedia)
    
    @property
    def kinesisvideosignalingchannels_client(self: "BotoSesManager") -> "KinesisvideosignalingchannelsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-signaling.html
        """
        return self.get_client(AwsServiceEnum.KinesisVideoSignalingChannels)
    
    @property
    def kinesisvideowebrtcstorage_client(self: "BotoSesManager") -> "KinesisvideowebrtcstorageClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis-video-webrtc-storage.html
        """
        return self.get_client(AwsServiceEnum.KinesisVideoWebRTCStorage)
    
    @property
    def kinesisanalytics_client(self: "BotoSesManager") -> "KinesisanalyticsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html
        """
        return self.get_client(AwsServiceEnum.KinesisAnalytics)
    
    @property
    def kinesisanalyticsv2_client(self: "BotoSesManager") -> "Kinesisanalyticsv2Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2.html
        """
        return self.get_client(AwsServiceEnum.KinesisAnalyticsV2)
    
    @property
    def kinesisvideo_client(self: "BotoSesManager") -> "KinesisvideoClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisvideo.html
        """
        return self.get_client(AwsServiceEnum.KinesisVideo)
    
    @property
    def kms_client(self: "BotoSesManager") -> "KmsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html
        """
        return self.get_client(AwsServiceEnum.KMS)
    
    @property
    def lakeformation_client(self: "BotoSesManager") -> "LakeformationClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html
        """
        return self.get_client(AwsServiceEnum.LakeFormation)
    
    @property
    def lambda_client(self: "BotoSesManager") -> "LambdaClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html
        """
        return self.get_client(AwsServiceEnum.Lambda)
    
    @property
    def lexmodelbuildingservice_client(self: "BotoSesManager") -> "LexmodelbuildingserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-models.html
        """
        return self.get_client(AwsServiceEnum.LexModelBuildingService)
    
    @property
    def lexruntimeservice_client(self: "BotoSesManager") -> "LexruntimeserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lex-runtime.html
        """
        return self.get_client(AwsServiceEnum.LexRuntimeService)
    
    @property
    def lexmodelsv2_client(self: "BotoSesManager") -> "Lexmodelsv2Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html
        """
        return self.get_client(AwsServiceEnum.LexModelsV2)
    
    @property
    def lexruntimev2_client(self: "BotoSesManager") -> "Lexruntimev2Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime.html
        """
        return self.get_client(AwsServiceEnum.LexRuntimeV2)
    
    @property
    def licensemanager_client(self: "BotoSesManager") -> "LicensemanagerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html
        """
        return self.get_client(AwsServiceEnum.LicenseManager)
    
    @property
    def licensemanagerlinuxsubscriptions_client(self: "BotoSesManager") -> "LicensemanagerlinuxsubscriptionsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-linux-subscriptions.html
        """
        return self.get_client(AwsServiceEnum.LicenseManagerLinuxSubscriptions)
    
    @property
    def licensemanagerusersubscriptions_client(self: "BotoSesManager") -> "LicensemanagerusersubscriptionsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager-user-subscriptions.html
        """
        return self.get_client(AwsServiceEnum.LicenseManagerUserSubscriptions)
    
    @property
    def lightsail_client(self: "BotoSesManager") -> "LightsailClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lightsail.html
        """
        return self.get_client(AwsServiceEnum.Lightsail)
    
    @property
    def locationservice_client(self: "BotoSesManager") -> "LocationserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/location.html
        """
        return self.get_client(AwsServiceEnum.LocationService)
    
    @property
    def cloudwatchlogs_client(self: "BotoSesManager") -> "CloudwatchlogsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html
        """
        return self.get_client(AwsServiceEnum.CloudWatchLogs)
    
    @property
    def lookoutequipment_client(self: "BotoSesManager") -> "LookoutequipmentClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutequipment.html
        """
        return self.get_client(AwsServiceEnum.LookoutEquipment)
    
    @property
    def lookoutmetrics_client(self: "BotoSesManager") -> "LookoutmetricsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutmetrics.html
        """
        return self.get_client(AwsServiceEnum.LookoutMetrics)
    
    @property
    def lookoutforvision_client(self: "BotoSesManager") -> "LookoutforvisionClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lookoutvision.html
        """
        return self.get_client(AwsServiceEnum.LookoutforVision)
    
    @property
    def mainframemodernization_client(self: "BotoSesManager") -> "MainframemodernizationClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2.html
        """
        return self.get_client(AwsServiceEnum.MainframeModernization)
    
    @property
    def machinelearning_client(self: "BotoSesManager") -> "MachinelearningClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html
        """
        return self.get_client(AwsServiceEnum.MachineLearning)
    
    @property
    def macie_client(self: "BotoSesManager") -> "MacieClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie.html
        """
        return self.get_client(AwsServiceEnum.Macie)
    
    @property
    def macie2_client(self: "BotoSesManager") -> "Macie2Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/macie2.html
        """
        return self.get_client(AwsServiceEnum.Macie2)
    
    @property
    def managedblockchain_client(self: "BotoSesManager") -> "ManagedblockchainClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain.html
        """
        return self.get_client(AwsServiceEnum.ManagedBlockchain)
    
    @property
    def marketplacecatalog_client(self: "BotoSesManager") -> "MarketplacecatalogClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html
        """
        return self.get_client(AwsServiceEnum.MarketplaceCatalog)
    
    @property
    def marketplaceentitlementservice_client(self: "BotoSesManager") -> "MarketplaceentitlementserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-entitlement.html
        """
        return self.get_client(AwsServiceEnum.MarketplaceEntitlementService)
    
    @property
    def marketplacecommerceanalytics_client(self: "BotoSesManager") -> "MarketplacecommerceanalyticsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplacecommerceanalytics.html
        """
        return self.get_client(AwsServiceEnum.MarketplaceCommerceAnalytics)
    
    @property
    def mediaconnect_client(self: "BotoSesManager") -> "MediaconnectClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconnect.html
        """
        return self.get_client(AwsServiceEnum.MediaConnect)
    
    @property
    def mediaconvert_client(self: "BotoSesManager") -> "MediaconvertClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediaconvert.html
        """
        return self.get_client(AwsServiceEnum.MediaConvert)
    
    @property
    def medialive_client(self: "BotoSesManager") -> "MedialiveClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medialive.html
        """
        return self.get_client(AwsServiceEnum.MediaLive)
    
    @property
    def mediapackage_client(self: "BotoSesManager") -> "MediapackageClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage.html
        """
        return self.get_client(AwsServiceEnum.MediaPackage)
    
    @property
    def mediapackagevod_client(self: "BotoSesManager") -> "MediapackagevodClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediapackage-vod.html
        """
        return self.get_client(AwsServiceEnum.MediaPackageVod)
    
    @property
    def mediastore_client(self: "BotoSesManager") -> "MediastoreClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore.html
        """
        return self.get_client(AwsServiceEnum.MediaStore)
    
    @property
    def mediastoredata_client(self: "BotoSesManager") -> "MediastoredataClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data.html
        """
        return self.get_client(AwsServiceEnum.MediaStoreData)
    
    @property
    def mediatailor_client(self: "BotoSesManager") -> "MediatailorClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediatailor.html
        """
        return self.get_client(AwsServiceEnum.MediaTailor)
    
    @property
    def memorydb_client(self: "BotoSesManager") -> "MemorydbClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html
        """
        return self.get_client(AwsServiceEnum.MemoryDB)
    
    @property
    def marketplacemetering_client(self: "BotoSesManager") -> "MarketplacemeteringClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html
        """
        return self.get_client(AwsServiceEnum.MarketplaceMetering)
    
    @property
    def migrationhub_client(self: "BotoSesManager") -> "MigrationhubClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgh.html
        """
        return self.get_client(AwsServiceEnum.MigrationHub)
    
    @property
    def mgn_client(self: "BotoSesManager") -> "MgnClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mgn.html
        """
        return self.get_client(AwsServiceEnum.mgn)
    
    @property
    def migrationhubrefactorspaces_client(self: "BotoSesManager") -> "MigrationhubrefactorspacesClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migration-hub-refactor-spaces.html
        """
        return self.get_client(AwsServiceEnum.MigrationHubRefactorSpaces)
    
    @property
    def migrationhubconfig_client(self: "BotoSesManager") -> "MigrationhubconfigClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhub-config.html
        """
        return self.get_client(AwsServiceEnum.MigrationHubConfig)
    
    @property
    def migrationhuborchestrator_client(self: "BotoSesManager") -> "MigrationhuborchestratorClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhuborchestrator.html
        """
        return self.get_client(AwsServiceEnum.MigrationHubOrchestrator)
    
    @property
    def migrationhubstrategyrecommendations_client(self: "BotoSesManager") -> "MigrationhubstrategyrecommendationsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/migrationhubstrategy.html
        """
        return self.get_client(AwsServiceEnum.MigrationHubStrategyRecommendations)
    
    @property
    def mobile_client(self: "BotoSesManager") -> "MobileClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html
        """
        return self.get_client(AwsServiceEnum.Mobile)
    
    @property
    def mq_client(self: "BotoSesManager") -> "MqClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html
        """
        return self.get_client(AwsServiceEnum.MQ)
    
    @property
    def mturk_client(self: "BotoSesManager") -> "MturkClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html
        """
        return self.get_client(AwsServiceEnum.MTurk)
    
    @property
    def mwaa_client(self: "BotoSesManager") -> "MwaaClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html
        """
        return self.get_client(AwsServiceEnum.MWAA)
    
    @property
    def neptune_client(self: "BotoSesManager") -> "NeptuneClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html
        """
        return self.get_client(AwsServiceEnum.Neptune)
    
    @property
    def networkfirewall_client(self: "BotoSesManager") -> "NetworkfirewallClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/network-firewall.html
        """
        return self.get_client(AwsServiceEnum.NetworkFirewall)
    
    @property
    def networkmanager_client(self: "BotoSesManager") -> "NetworkmanagerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmanager.html
        """
        return self.get_client(AwsServiceEnum.NetworkManager)
    
    @property
    def nimblestudio_client(self: "BotoSesManager") -> "NimblestudioClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html
        """
        return self.get_client(AwsServiceEnum.NimbleStudio)
    
    @property
    def cloudwatchobservabilityaccessmanager_client(self: "BotoSesManager") -> "CloudwatchobservabilityaccessmanagerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html
        """
        return self.get_client(AwsServiceEnum.CloudWatchObservabilityAccessManager)
    
    @property
    def omics_client(self: "BotoSesManager") -> "OmicsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html
        """
        return self.get_client(AwsServiceEnum.Omics)
    
    @property
    def opensearchservice_client(self: "BotoSesManager") -> "OpensearchserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearch.html
        """
        return self.get_client(AwsServiceEnum.OpenSearchService)
    
    @property
    def opensearchserviceserverless_client(self: "BotoSesManager") -> "OpensearchserviceserverlessClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opensearchserverless.html
        """
        return self.get_client(AwsServiceEnum.OpenSearchServiceServerless)
    
    @property
    def opsworks_client(self: "BotoSesManager") -> "OpsworksClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworks.html
        """
        return self.get_client(AwsServiceEnum.OpsWorks)
    
    @property
    def opsworkscm_client(self: "BotoSesManager") -> "OpsworkscmClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm.html
        """
        return self.get_client(AwsServiceEnum.OpsWorksCM)
    
    @property
    def organizations_client(self: "BotoSesManager") -> "OrganizationsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html
        """
        return self.get_client(AwsServiceEnum.Organizations)
    
    @property
    def outposts_client(self: "BotoSesManager") -> "OutpostsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html
        """
        return self.get_client(AwsServiceEnum.Outposts)
    
    @property
    def panorama_client(self: "BotoSesManager") -> "PanoramaClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/panorama.html
        """
        return self.get_client(AwsServiceEnum.Panorama)
    
    @property
    def personalize_client(self: "BotoSesManager") -> "PersonalizeClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize.html
        """
        return self.get_client(AwsServiceEnum.Personalize)
    
    @property
    def personalizeevents_client(self: "BotoSesManager") -> "PersonalizeeventsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html
        """
        return self.get_client(AwsServiceEnum.PersonalizeEvents)
    
    @property
    def personalizeruntime_client(self: "BotoSesManager") -> "PersonalizeruntimeClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-runtime.html
        """
        return self.get_client(AwsServiceEnum.PersonalizeRuntime)
    
    @property
    def pi_client(self: "BotoSesManager") -> "PiClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi.html
        """
        return self.get_client(AwsServiceEnum.PI)
    
    @property
    def pinpoint_client(self: "BotoSesManager") -> "PinpointClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint.html
        """
        return self.get_client(AwsServiceEnum.Pinpoint)
    
    @property
    def pinpointemail_client(self: "BotoSesManager") -> "PinpointemailClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-email.html
        """
        return self.get_client(AwsServiceEnum.PinpointEmail)
    
    @property
    def pinpointsmsvoice_client(self: "BotoSesManager") -> "PinpointsmsvoiceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice.html
        """
        return self.get_client(AwsServiceEnum.PinpointSMSVoice)
    
    @property
    def pinpointsmsvoicev2_client(self: "BotoSesManager") -> "Pinpointsmsvoicev2Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pinpoint-sms-voice-v2.html
        """
        return self.get_client(AwsServiceEnum.PinpointSMSVoiceV2)
    
    @property
    def eventbridgepipes_client(self: "BotoSesManager") -> "EventbridgepipesClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pipes.html
        """
        return self.get_client(AwsServiceEnum.EventBridgePipes)
    
    @property
    def polly_client(self: "BotoSesManager") -> "PollyClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html
        """
        return self.get_client(AwsServiceEnum.Polly)
    
    @property
    def pricing_client(self: "BotoSesManager") -> "PricingClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html
        """
        return self.get_client(AwsServiceEnum.Pricing)
    
    @property
    def private5g_client(self: "BotoSesManager") -> "Private5gClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks.html
        """
        return self.get_client(AwsServiceEnum.Private5G)
    
    @property
    def proton_client(self: "BotoSesManager") -> "ProtonClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/proton.html
        """
        return self.get_client(AwsServiceEnum.Proton)
    
    @property
    def qldb_client(self: "BotoSesManager") -> "QldbClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb.html
        """
        return self.get_client(AwsServiceEnum.QLDB)
    
    @property
    def qldbsession_client(self: "BotoSesManager") -> "QldbsessionClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qldb-session.html
        """
        return self.get_client(AwsServiceEnum.QLDBSession)
    
    @property
    def quicksight_client(self: "BotoSesManager") -> "QuicksightClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html
        """
        return self.get_client(AwsServiceEnum.QuickSight)
    
    @property
    def ram_client(self: "BotoSesManager") -> "RamClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ram.html
        """
        return self.get_client(AwsServiceEnum.RAM)
    
    @property
    def recyclebin_client(self: "BotoSesManager") -> "RecyclebinClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin.html
        """
        return self.get_client(AwsServiceEnum.RecycleBin)
    
    @property
    def rds_client(self: "BotoSesManager") -> "RdsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html
        """
        return self.get_client(AwsServiceEnum.RDS)
    
    @property
    def rdsdataservice_client(self: "BotoSesManager") -> "RdsdataserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html
        """
        return self.get_client(AwsServiceEnum.RDSDataService)
    
    @property
    def redshift_client(self: "BotoSesManager") -> "RedshiftClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html
        """
        return self.get_client(AwsServiceEnum.Redshift)
    
    @property
    def redshiftdataapiservice_client(self: "BotoSesManager") -> "RedshiftdataapiserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html
        """
        return self.get_client(AwsServiceEnum.RedshiftDataAPIService)
    
    @property
    def redshiftserverless_client(self: "BotoSesManager") -> "RedshiftserverlessClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html
        """
        return self.get_client(AwsServiceEnum.RedshiftServerless)
    
    @property
    def rekognition_client(self: "BotoSesManager") -> "RekognitionClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html
        """
        return self.get_client(AwsServiceEnum.Rekognition)
    
    @property
    def resiliencehub_client(self: "BotoSesManager") -> "ResiliencehubClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub.html
        """
        return self.get_client(AwsServiceEnum.ResilienceHub)
    
    @property
    def resourceexplorer_client(self: "BotoSesManager") -> "ResourceexplorerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html
        """
        return self.get_client(AwsServiceEnum.ResourceExplorer)
    
    @property
    def resourcegroups_client(self: "BotoSesManager") -> "ResourcegroupsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-groups.html
        """
        return self.get_client(AwsServiceEnum.ResourceGroups)
    
    @property
    def resourcegroupstaggingapi_client(self: "BotoSesManager") -> "ResourcegroupstaggingapiClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html
        """
        return self.get_client(AwsServiceEnum.ResourceGroupsTaggingAPI)
    
    @property
    def robomaker_client(self: "BotoSesManager") -> "RobomakerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker.html
        """
        return self.get_client(AwsServiceEnum.RoboMaker)
    
    @property
    def iamrolesanywhere_client(self: "BotoSesManager") -> "IamrolesanywhereClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html
        """
        return self.get_client(AwsServiceEnum.IAMRolesAnywhere)
    
    @property
    def route53_client(self: "BotoSesManager") -> "Route53Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html
        """
        return self.get_client(AwsServiceEnum.Route53)
    
    @property
    def route53recoverycluster_client(self: "BotoSesManager") -> "Route53recoveryclusterClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-cluster.html
        """
        return self.get_client(AwsServiceEnum.Route53RecoveryCluster)
    
    @property
    def route53recoverycontrolconfig_client(self: "BotoSesManager") -> "Route53recoverycontrolconfigClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html
        """
        return self.get_client(AwsServiceEnum.Route53RecoveryControlConfig)
    
    @property
    def route53recoveryreadiness_client(self: "BotoSesManager") -> "Route53recoveryreadinessClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html
        """
        return self.get_client(AwsServiceEnum.Route53RecoveryReadiness)
    
    @property
    def route53domains_client(self: "BotoSesManager") -> "Route53domainsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53domains.html
        """
        return self.get_client(AwsServiceEnum.Route53Domains)
    
    @property
    def route53resolver_client(self: "BotoSesManager") -> "Route53resolverClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver.html
        """
        return self.get_client(AwsServiceEnum.Route53Resolver)
    
    @property
    def cloudwatchrum_client(self: "BotoSesManager") -> "CloudwatchrumClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html
        """
        return self.get_client(AwsServiceEnum.CloudWatchRUM)
    
    @property
    def s3_client(self: "BotoSesManager") -> "S3Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
        """
        return self.get_client(AwsServiceEnum.S3)
    
    @property
    def s3control_client(self: "BotoSesManager") -> "S3controlClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html
        """
        return self.get_client(AwsServiceEnum.S3Control)
    
    @property
    def s3outposts_client(self: "BotoSesManager") -> "S3outpostsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3outposts.html
        """
        return self.get_client(AwsServiceEnum.S3Outposts)
    
    @property
    def sagemaker_client(self: "BotoSesManager") -> "SagemakerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html
        """
        return self.get_client(AwsServiceEnum.SageMaker)
    
    @property
    def augmentedairuntime_client(self: "BotoSesManager") -> "AugmentedairuntimeClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime.html
        """
        return self.get_client(AwsServiceEnum.AugmentedAIRuntime)
    
    @property
    def sagemakeredgemanager_client(self: "BotoSesManager") -> "SagemakeredgemanagerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html
        """
        return self.get_client(AwsServiceEnum.SagemakerEdgeManager)
    
    @property
    def sagemakerfeaturestoreruntime_client(self: "BotoSesManager") -> "SagemakerfeaturestoreruntimeClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime.html
        """
        return self.get_client(AwsServiceEnum.SageMakerFeatureStoreRuntime)
    
    @property
    def sagemakergeospatialcapabilities_client(self: "BotoSesManager") -> "SagemakergeospatialcapabilitiesClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-geospatial.html
        """
        return self.get_client(AwsServiceEnum.SageMakergeospatialcapabilities)
    
    @property
    def sagemakermetrics_client(self: "BotoSesManager") -> "SagemakermetricsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-metrics.html
        """
        return self.get_client(AwsServiceEnum.SageMakerMetrics)
    
    @property
    def sagemakerruntime_client(self: "BotoSesManager") -> "SagemakerruntimeClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime.html
        """
        return self.get_client(AwsServiceEnum.SageMakerRuntime)
    
    @property
    def savingsplans_client(self: "BotoSesManager") -> "SavingsplansClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html
        """
        return self.get_client(AwsServiceEnum.SavingsPlans)
    
    @property
    def eventbridgescheduler_client(self: "BotoSesManager") -> "EventbridgeschedulerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/scheduler.html
        """
        return self.get_client(AwsServiceEnum.EventBridgeScheduler)
    
    @property
    def schemas_client(self: "BotoSesManager") -> "SchemasClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html
        """
        return self.get_client(AwsServiceEnum.Schemas)
    
    @property
    def simpledb_client(self: "BotoSesManager") -> "SimpledbClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sdb.html
        """
        return self.get_client(AwsServiceEnum.SimpleDB)
    
    @property
    def secretsmanager_client(self: "BotoSesManager") -> "SecretsmanagerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html
        """
        return self.get_client(AwsServiceEnum.SecretsManager)
    
    @property
    def securityhub_client(self: "BotoSesManager") -> "SecurityhubClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securityhub.html
        """
        return self.get_client(AwsServiceEnum.SecurityHub)
    
    @property
    def securitylake_client(self: "BotoSesManager") -> "SecuritylakeClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/securitylake.html
        """
        return self.get_client(AwsServiceEnum.SecurityLake)
    
    @property
    def serverlessapplicationrepository_client(self: "BotoSesManager") -> "ServerlessapplicationrepositoryClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo.html
        """
        return self.get_client(AwsServiceEnum.ServerlessApplicationRepository)
    
    @property
    def servicequotas_client(self: "BotoSesManager") -> "ServicequotasClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas.html
        """
        return self.get_client(AwsServiceEnum.ServiceQuotas)
    
    @property
    def servicecatalog_client(self: "BotoSesManager") -> "ServicecatalogClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog.html
        """
        return self.get_client(AwsServiceEnum.ServiceCatalog)
    
    @property
    def appregistry_client(self: "BotoSesManager") -> "AppregistryClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html
        """
        return self.get_client(AwsServiceEnum.AppRegistry)
    
    @property
    def servicediscovery_client(self: "BotoSesManager") -> "ServicediscoveryClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicediscovery.html
        """
        return self.get_client(AwsServiceEnum.ServiceDiscovery)
    
    @property
    def ses_client(self: "BotoSesManager") -> "SesClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html
        """
        return self.get_client(AwsServiceEnum.SES)
    
    @property
    def sesv2_client(self: "BotoSesManager") -> "Sesv2Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2.html
        """
        return self.get_client(AwsServiceEnum.SESV2)
    
    @property
    def shield_client(self: "BotoSesManager") -> "ShieldClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html
        """
        return self.get_client(AwsServiceEnum.Shield)
    
    @property
    def signer_client(self: "BotoSesManager") -> "SignerClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html
        """
        return self.get_client(AwsServiceEnum.signer)
    
    @property
    def simspaceweaver_client(self: "BotoSesManager") -> "SimspaceweaverClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/simspaceweaver.html
        """
        return self.get_client(AwsServiceEnum.SimSpaceWeaver)
    
    @property
    def sms_client(self: "BotoSesManager") -> "SmsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms.html
        """
        return self.get_client(AwsServiceEnum.SMS)
    
    @property
    def pinpointsmsvoice_client(self: "BotoSesManager") -> "PinpointsmsvoiceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sms-voice.html
        """
        return self.get_client(AwsServiceEnum.PinpointSMSVoice)
    
    @property
    def snowdevicemanagement_client(self: "BotoSesManager") -> "SnowdevicemanagementClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snow-device-management.html
        """
        return self.get_client(AwsServiceEnum.SnowDeviceManagement)
    
    @property
    def snowball_client(self: "BotoSesManager") -> "SnowballClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/snowball.html
        """
        return self.get_client(AwsServiceEnum.Snowball)
    
    @property
    def sns_client(self: "BotoSesManager") -> "SnsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html
        """
        return self.get_client(AwsServiceEnum.SNS)
    
    @property
    def sqs_client(self: "BotoSesManager") -> "SqsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html
        """
        return self.get_client(AwsServiceEnum.SQS)
    
    @property
    def ssm_client(self: "BotoSesManager") -> "SsmClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html
        """
        return self.get_client(AwsServiceEnum.SSM)
    
    @property
    def ssmcontacts_client(self: "BotoSesManager") -> "SsmcontactsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-contacts.html
        """
        return self.get_client(AwsServiceEnum.SSMContacts)
    
    @property
    def ssmincidents_client(self: "BotoSesManager") -> "SsmincidentsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-incidents.html
        """
        return self.get_client(AwsServiceEnum.SSMIncidents)
    
    @property
    def ssmsap_client(self: "BotoSesManager") -> "SsmsapClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-sap.html
        """
        return self.get_client(AwsServiceEnum.SsmSap)
    
    @property
    def sso_client(self: "BotoSesManager") -> "SsoClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html
        """
        return self.get_client(AwsServiceEnum.SSO)
    
    @property
    def ssoadmin_client(self: "BotoSesManager") -> "SsoadminClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html
        """
        return self.get_client(AwsServiceEnum.SSOAdmin)
    
    @property
    def ssooidc_client(self: "BotoSesManager") -> "SsooidcClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc.html
        """
        return self.get_client(AwsServiceEnum.SSOOIDC)
    
    @property
    def sfn_client(self: "BotoSesManager") -> "SfnClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html
        """
        return self.get_client(AwsServiceEnum.SFN)
    
    @property
    def storagegateway_client(self: "BotoSesManager") -> "StoragegatewayClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/storagegateway.html
        """
        return self.get_client(AwsServiceEnum.StorageGateway)
    
    @property
    def sts_client(self: "BotoSesManager") -> "StsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html
        """
        return self.get_client(AwsServiceEnum.STS)
    
    @property
    def support_client(self: "BotoSesManager") -> "SupportClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support.html
        """
        return self.get_client(AwsServiceEnum.Support)
    
    @property
    def supportapp_client(self: "BotoSesManager") -> "SupportappClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/support-app.html
        """
        return self.get_client(AwsServiceEnum.SupportApp)
    
    @property
    def swf_client(self: "BotoSesManager") -> "SwfClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/swf.html
        """
        return self.get_client(AwsServiceEnum.SWF)
    
    @property
    def synthetics_client(self: "BotoSesManager") -> "SyntheticsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/synthetics.html
        """
        return self.get_client(AwsServiceEnum.Synthetics)
    
    @property
    def textract_client(self: "BotoSesManager") -> "TextractClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html
        """
        return self.get_client(AwsServiceEnum.Textract)
    
    @property
    def timestreamquery_client(self: "BotoSesManager") -> "TimestreamqueryClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query.html
        """
        return self.get_client(AwsServiceEnum.TimestreamQuery)
    
    @property
    def timestreamwrite_client(self: "BotoSesManager") -> "TimestreamwriteClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html
        """
        return self.get_client(AwsServiceEnum.TimestreamWrite)
    
    @property
    def telconetworkbuilder_client(self: "BotoSesManager") -> "TelconetworkbuilderClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html
        """
        return self.get_client(AwsServiceEnum.TelcoNetworkBuilder)
    
    @property
    def transcribeservice_client(self: "BotoSesManager") -> "TranscribeserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html
        """
        return self.get_client(AwsServiceEnum.TranscribeService)
    
    @property
    def transfer_client(self: "BotoSesManager") -> "TransferClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html
        """
        return self.get_client(AwsServiceEnum.Transfer)
    
    @property
    def translate_client(self: "BotoSesManager") -> "TranslateClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html
        """
        return self.get_client(AwsServiceEnum.Translate)
    
    @property
    def voiceid_client(self: "BotoSesManager") -> "VoiceidClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/voice-id.html
        """
        return self.get_client(AwsServiceEnum.VoiceID)
    
    @property
    def waf_client(self: "BotoSesManager") -> "WafClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf.html
        """
        return self.get_client(AwsServiceEnum.WAF)
    
    @property
    def wafregional_client(self: "BotoSesManager") -> "WafregionalClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/waf-regional.html
        """
        return self.get_client(AwsServiceEnum.WAFRegional)
    
    @property
    def wafv2_client(self: "BotoSesManager") -> "Wafv2Client":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html
        """
        return self.get_client(AwsServiceEnum.WAFV2)
    
    @property
    def wellarchitected_client(self: "BotoSesManager") -> "WellarchitectedClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html
        """
        return self.get_client(AwsServiceEnum.WellArchitected)
    
    @property
    def connectwisdomservice_client(self: "BotoSesManager") -> "ConnectwisdomserviceClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom.html
        """
        return self.get_client(AwsServiceEnum.ConnectWisdomService)
    
    @property
    def workdocs_client(self: "BotoSesManager") -> "WorkdocsClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html
        """
        return self.get_client(AwsServiceEnum.WorkDocs)
    
    @property
    def worklink_client(self: "BotoSesManager") -> "WorklinkClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/worklink.html
        """
        return self.get_client(AwsServiceEnum.WorkLink)
    
    @property
    def workmail_client(self: "BotoSesManager") -> "WorkmailClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html
        """
        return self.get_client(AwsServiceEnum.WorkMail)
    
    @property
    def workmailmessageflow_client(self: "BotoSesManager") -> "WorkmailmessageflowClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmailmessageflow.html
        """
        return self.get_client(AwsServiceEnum.WorkMailMessageFlow)
    
    @property
    def workspaces_client(self: "BotoSesManager") -> "WorkspacesClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces.html
        """
        return self.get_client(AwsServiceEnum.WorkSpaces)
    
    @property
    def workspacesweb_client(self: "BotoSesManager") -> "WorkspaceswebClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html
        """
        return self.get_client(AwsServiceEnum.WorkSpacesWeb)
    
    @property
    def xray_client(self: "BotoSesManager") -> "XrayClient":
        """
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html
        """
        return self.get_client(AwsServiceEnum.XRay)
    