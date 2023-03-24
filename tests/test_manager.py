# -*- coding: utf-8 -*-

import pytest

import os
import sys
import json
import subprocess
from boto_session_manager.manager import BotoSesManager, AwsServiceEnum

if "CI" in os.environ:  # pragma: no cover
    is_ci = True
    aws_access_key_id = os.environ["AWS_ACCESS_KEY_ID_FOR_GITHUB_CI"]
    aws_secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY_FOR_GITHUB_CI"]
    bsm = BotoSesManager(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )
else:  # pragma: no cover
    is_ci = False
    profile_name = "aws_data_lab_open_source_boto_session_manager"
    bsm = BotoSesManager(profile_name=profile_name)


iam_user_name = "project-boto_session_manager"
iam_role_name = "project-boto_session_manager"


class TestBotoSesManager:
    def test_aws_account_id_and_region(self):
        _ = bsm.aws_account_id
        _ = bsm.aws_region

    def test_get_client(self):
        s3_client1 = bsm.get_client(AwsServiceEnum.S3)
        s3_client2 = bsm.get_client(AwsServiceEnum.S3)
        assert id(s3_client1) == id(s3_client2)

    def test_get_resource(self):
        s3_resource1 = bsm.get_resource(AwsServiceEnum.S3)
        s3_resource2 = bsm.get_resource(AwsServiceEnum.S3)
        assert id(s3_resource1) == id(s3_resource2)

    def test_clear_cache(self):
        _ = bsm.s3_client
        assert len(bsm._client_cache) >= 1

        bsm.clear_cache()
        assert len(bsm._client_cache) == 0

    def test_is_expired(self):
        assert bsm.is_expired() is False

    def test_assume_role(self):
        # Test STS get caller identity
        aws_account_id = bsm.sts_client.get_caller_identity()["Account"]
        assert aws_account_id == bsm.aws_account_id

        # Test IAM role and Assumed IAM Role
        role_name = "project-boto_session_manager"
        bsm_assumed = bsm.assume_role(
            role_arn=f"arn:aws:iam::{aws_account_id}:role/{role_name}"
        )
        sts_client_assumed = bsm_assumed.get_client(AwsServiceEnum.STS)
        res = sts_client_assumed.get_caller_identity()
        assert res["Arn"].startswith(
            f"arn:aws:sts::{aws_account_id}:assumed-role/{role_name}"
        )
        assert bsm_assumed.expiration_time <= bsm.expiration_time

    def _assert_aws_cli_env_var_exists(self):
        assert "AWS_ACCESS_KEY_ID" in os.environ
        assert "AWS_SECRET_ACCESS_KEY" in os.environ
        assert "AWS_SESSION_TOKEN" in os.environ
        assert "AWS_REGION" in os.environ

    def _assert_aws_cli_env_var_not_exists(self):
        assert "AWS_ACCESS_KEY_ID" not in os.environ
        assert "AWS_SECRET_ACCESS_KEY" not in os.environ
        assert "AWS_SESSION_TOKEN" not in os.environ
        assert "AWS_REGION" not in os.environ

    def _assert_default_aws_cli_credential_is_different(self, bsm: BotoSesManager):
        args = ["aws", "sts", "get-caller-identity"]
        response = json.loads(
            subprocess.run(args, capture_output=True).stdout.decode("utf-8")
        )
        user_id, aws_account_id, arn = (
            response["UserId"],
            response["Account"],
            response["Arn"],
        )
        assert aws_account_id != bsm.aws_account_id
        assert not arn.endswith(iam_user_name)
        self._assert_aws_cli_env_var_not_exists()

    @pytest.mark.skipif(
        is_ci,
        reason="we don't want to expose real AWS credentials in CI",
    )
    def test_cli_context_manager_with_arguments(self):
        # the bsm object is using the profile "aws_data_lab_open_source_boto_session_manager"
        # which is an IAM user.
        # however, the aws cli uses different AWS profile
        self._assert_default_aws_cli_credential_is_different(bsm)

        # iam user
        with bsm.awscli():
            args = ["aws", "sts", "get-caller-identity"]
            response = json.loads(
                subprocess.run(args, capture_output=True).stdout.decode("utf-8")
            )
            user_id, aws_account_id, arn = (
                response["UserId"],
                response["Account"],
                response["Arn"],
            )
            assert aws_account_id == bsm.aws_account_id
            assert arn.endswith(f"user/{iam_user_name}")
            self._assert_aws_cli_env_var_exists()

        self._assert_default_aws_cli_credential_is_different(bsm)

        # assume role
        bsm_assumed = bsm.assume_role(
            role_arn=f"arn:aws:iam::{aws_account_id}:role/{iam_role_name}"
        )
        with bsm_assumed.awscli():
            args = ["aws", "sts", "get-caller-identity"]
            response = json.loads(
                subprocess.run(args, capture_output=True).stdout.decode("utf-8")
            )
            user_id, aws_account_id, arn = (
                response["UserId"],
                response["Account"],
                response["Arn"],
            )
            assert aws_account_id == bsm_assumed.aws_account_id
            assert f"assumed-role/{iam_role_name}" in arn
            self._assert_aws_cli_env_var_exists()

        self._assert_default_aws_cli_credential_is_different(bsm)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
