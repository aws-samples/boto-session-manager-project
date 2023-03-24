# -*- coding: utf-8 -*-

"""
Manage the underlying boto3 session and client.
"""

import typing as T
import os
import uuid
import contextlib
from datetime import datetime, timezone, timedelta

try:
    import boto3
    import boto3.session
    import botocore.session
except ImportError as e:  # pragma: no cover
    print("You probably need to install 'boto3' first.")

if T.TYPE_CHECKING:  # pragma: no cover
    from botocore.client import BaseClient
    from boto3.resources.base import ServiceResource

from .services import AwsServiceEnum
from .clients import ClientMixin


class BotoSesManager(ClientMixin):
    """
    Boto3 session and client manager that use cache to create low level client.

    .. note::

        boto3.session.Session is a static object that won't talk to AWS endpoint.
        also session.client("s3") won't talk to AWS endpoint right away. The
        authentication only happen when a concrete API request called.

    .. versionadded:: 0.0.1

    .. versionchanged:: 0.0.4

        add ``default_client_kwargs`` arguments that set default keyword
        arguments for ``boto3.session.Session.client`` method.
    """

    def __init__(
        self,
        aws_access_key_id: str = None,
        aws_secret_access_key: str = None,
        aws_session_token: str = None,
        region_name: str = None,
        botocore_session: T.Optional["botocore.session.Session"] = None,
        profile_name: str = None,
        default_client_kwargs: dict = None,
        expiration_time: datetime = None,
    ):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_session_token = aws_session_token
        self.region_name = region_name
        if botocore_session is not None:  # pragma: no cover
            if not isinstance(botocore_session, botocore.session.Session):
                raise TypeError
        self.botocore_session: "botocore.session.Session" = botocore_session
        self.profile_name = profile_name
        self.expiration_time: datetime
        if expiration_time is None:
            self.expiration_time = datetime.utcnow().replace(
                tzinfo=timezone.utc
            ) + timedelta(days=365)
        else:
            self.expiration_time = expiration_time
        if default_client_kwargs is None:
            default_client_kwargs = dict()
        self.default_client_kwargs = default_client_kwargs

        self._boto_ses_cache: T.Optional["boto3.session.Session"] = None
        self._client_cache: T.Dict[str, "BaseClient"] = dict()
        self._resource_cache: T.Dict[str, "ServiceResource"] = dict()
        self._aws_account_id_cache: T.Optional[str] = None
        self._aws_region_cache: T.Optional[str] = None

    @property
    def boto_ses(self) -> "boto3.session.Session":
        """
        Get boto3 session from metadata.

        .. versionadded:: 1.0.2
        """
        if self._boto_ses_cache is None:
            self._boto_ses_cache = boto3.session.Session(
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key,
                aws_session_token=self.aws_session_token,
                region_name=self.region_name,
                botocore_session=self.botocore_session,
                profile_name=self.profile_name,
            )
        return self._boto_ses_cache

    @property
    def aws_account_id(self) -> str:
        """
        Get current aws account id of the boto session

        .. versionadded:: 1.0.1
        """
        if self._aws_account_id_cache is None:
            sts_client = self.get_client(AwsServiceEnum.STS)
            self._aws_account_id_cache = sts_client.get_caller_identity()["Account"]
        return self._aws_account_id_cache

    @property
    def aws_region(self) -> str:
        """
        Get current aws region of the boto session

        .. versionadded:: 0.0.1
        """
        if self._aws_region_cache is None:
            self._aws_region_cache = self.boto_ses.region_name
        return self._aws_region_cache

    def get_client(
        self,
        service_name: str,
        region_name: str = None,
        api_version: str = None,
        use_ssl: bool = True,
        verify: T.Union[bool, str] = None,
        endpoint_url: str = None,
        aws_access_key_id: str = None,
        aws_secret_access_key: str = None,
        aws_session_token: str = None,
        config=None,
    ) -> "BaseClient":
        """
        Get aws boto client using cache.

        .. versionadded:: 0.0.1

        .. versionchanged:: 0.0.3

            add additional keyword arguments pass to
            ``boto3.session.Session.client()`` method.
        """
        try:
            return self._client_cache[service_name]
        except KeyError:
            client_kwargs = dict(
                region_name=region_name,
                api_version=api_version,
                use_ssl=use_ssl,
                verify=verify,
                endpoint_url=endpoint_url,
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                aws_session_token=aws_session_token,
                config=config,
            )
            client_kwargs = {k: v for k, v in client_kwargs.items() if v is not None}
            kwargs = dict(self.default_client_kwargs)
            if self.default_client_kwargs:  # pragma: no cover
                kwargs.update(client_kwargs)
            client = self.boto_ses.client(service_name, **kwargs)
            self._client_cache[service_name] = client
            return client

    def get_resource(
        self,
        service_name: str,
        region_name: str = None,
        api_version: str = None,
        use_ssl: bool = True,
        verify: T.Union[bool, str] = None,
        endpoint_url: str = None,
        aws_access_key_id: str = None,
        aws_secret_access_key: str = None,
        aws_session_token: str = None,
        config=None,
    ) -> "ServiceResource":
        """
        Get aws boto service resource using cache

        .. versionadded:: 0.0.2

        .. versionchanged:: 0.0.3

            add additional keyword arguments pass to
            ``boto3.session.Session.resource()`` method.
        """
        try:
            return self._resource_cache[service_name]
        except KeyError:
            resource_kwargs = dict(
                region_name=region_name,
                api_version=api_version,
                use_ssl=use_ssl,
                verify=verify,
                endpoint_url=endpoint_url,
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                aws_session_token=aws_session_token,
                config=config,
            )
            resource_kwargs = {
                k: v for k, v in resource_kwargs.items() if v is not None
            }
            kwargs = dict(self.default_client_kwargs)
            if self.default_client_kwargs:
                kwargs.update(resource_kwargs)
            resource = self.boto_ses.resource(service_name, **kwargs)
            self._resource_cache[service_name] = resource
            return resource

    def assume_role(
        self,
        role_arn: str,
        role_session_name: str = None,
        duration_seconds: int = 3600,
        tags: list = None,
        transitive_tag_keys: list = None,
        external_id: str = None,
        mfa_serial_number: str = None,
        mfa_token: str = None,
        source_identity: str = None,
    ) -> "BotoSesManager":
        """
        Assume an IAM role, create another :class`BotoSessionManager` and return.

        .. versionadded:: 0.0.1
        """
        if role_session_name is None:
            role_session_name = uuid.uuid4().hex
        kwargs = {
            k: v
            for k, v in dict(
                RoleArn=role_arn,
                RoleSessionName=role_session_name,
                DurationSeconds=duration_seconds,
                Tags=tags,
                TransitiveTagKeys=transitive_tag_keys,
                external_id=external_id,
                SerialNumber=mfa_serial_number,
                TokenCode=mfa_token,
                SourceIdentity=source_identity,
            ).items()
            if v is not None
        }
        sts_client = self.get_client(AwsServiceEnum.STS)
        res = sts_client.assume_role(**kwargs)
        expiration_time = res["Credentials"]["Expiration"]
        bsm = self.__class__(
            aws_access_key_id=res["Credentials"]["AccessKeyId"],
            aws_secret_access_key=res["Credentials"]["SecretAccessKey"],
            aws_session_token=res["Credentials"]["SessionToken"],
            expiration_time=expiration_time,
            default_client_kwargs=self.default_client_kwargs,
        )
        return bsm

    def is_expired(self, delta: int = 0) -> bool:
        """
        Check if this boto session is expired.

        .. versionadded:: 0.0.1
        """
        return (
            datetime.utcnow().replace(tzinfo=timezone.utc) + timedelta(seconds=delta)
        ) >= self.expiration_time

    @contextlib.contextmanager
    def awscli(
        self,
        duration_seconds: int = 900,
        serial_number: T.Optional[str] = None,
        token_code: T.Optional[str] = None,
    ) -> "BotoSesManager":
        """
        Temporarily set up environment variable to pass the boto session
        credential to AWS CLI.

        Example::

            import subprocess

            bsm = BotoSesManager(...)

            with bsm.awscli():
                subprocess.run(["aws", "sts", "get-caller-identity"])

        Reference:

        - https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html

        .. versionadded:: 1.2.1
        """
        # record the existing env var state
        env_names = [
            "AWS_ACCESS_KEY_ID",
            "AWS_SECRET_ACCESS_KEY",
            "AWS_SESSION_TOKEN",
            "AWS_REGION",
            "AWS_PROFILE",
        ]
        env_var = dict()
        for env_name in env_names:
            if env_name in os.environ:  # pragma: no cover
                env_var[env_name] = os.environ[env_name]
            else:
                env_var[env_name] = None

        # set environment variable for aws cli
        if (
            (self.aws_access_key_id is not None)
            and (self.aws_secret_access_key is not None)
            and (self.aws_access_key_id is not None)
        ):
            os.environ["AWS_ACCESS_KEY_ID"] = self.aws_access_key_id
            os.environ["AWS_SECRET_ACCESS_KEY"] = self.aws_secret_access_key
            os.environ["AWS_SESSION_TOKEN"] = self.aws_session_token
            os.environ["AWS_REGION"] = self.aws_region
        else:
            kwargs = dict(
                DurationSeconds=duration_seconds,
            )
            if serial_number is not None:  # pragma: no cover
                kwargs["SerialNumber"] = serial_number
            if token_code is not None:  # pragma: no cover
                kwargs["TokenCode"] = token_code
            response = self.sts_client.get_session_token(**kwargs)
            os.environ["AWS_ACCESS_KEY_ID"] = response["Credentials"]["AccessKeyId"]
            os.environ["AWS_SECRET_ACCESS_KEY"] = response["Credentials"][
                "SecretAccessKey"
            ]
            os.environ["AWS_SESSION_TOKEN"] = response["Credentials"]["SessionToken"]
            os.environ["AWS_REGION"] = self.aws_region
        try:
            yield self
        finally:
            # recover previous existing env var
            for env_name, env_value in env_var.items():
                if env_value is None:
                    if env_name in os.environ:
                        os.environ.pop(env_name)
                else:
                    os.environ[env_name] = env_value

    def clear_cache(self):
        """
        Clear all the boto session and boto client cache.
        """
        self._boto_ses_cache = None
        self._client_cache.clear()
        self._resource_cache.clear()
        self._aws_account_id_cache = None
        self._aws_region_cache = None
