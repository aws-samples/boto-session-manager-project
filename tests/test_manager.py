# -*- coding: utf-8 -*-

import pytest

import os
import sys
import json
import subprocess
from boto_session_manager.manager import BotoSesManager, AwsServiceEnum

if "CI" in os.environ:  # pragma: no cover
    aws_access_key_id = os.environ["AWS_ACCESS_KEY_ID_FOR_GITHUB_CI"]
    aws_secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY_FOR_GITHUB_CI"]
    bsm = BotoSesManager(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )
else:  # pragma: no cover
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

    @pytest.mark.skipif(
        sys.platform.startswith("win"),
        reason="windows CLI system is different",
    )
    def test_cli_context_manager_with_arguments(self):
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

        assert "AWS_ACCESS_KEY_ID" not in os.environ
        assert "AWS_SECRET_ACCESS_KEY" not in os.environ
        assert "AWS_PROFILE" not in os.environ

        assert arn.endswith(f"user/{iam_user_name}")

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

        assert "AWS_ACCESS_KEY_ID" not in os.environ
        assert "AWS_SECRET_ACCESS_KEY" not in os.environ
        assert "AWS_SESSION_TOKEN" not in os.environ
        assert "AWS_PROFILE" not in os.environ

        assert f"assumed-role/{iam_role_name}" in arn

    @pytest.mark.skipif(
        sys.platform.startswith("win"),
        reason="windows CLI system is different",
    )
    def test_cli_context_manager_with_botocore_session(self):
        # iam user
        bsm_new = BotoSesManager(botocore_session=bsm.boto_ses._session)

        with bsm_new.awscli():
            args = ["aws", "sts", "get-caller-identity"]
            response = json.loads(
                subprocess.run(args, capture_output=True).stdout.decode("utf-8")
            )
            user_id, aws_account_id, arn = (
                response["UserId"],
                response["Account"],
                response["Arn"],
            )

        assert "AWS_ACCESS_KEY_ID" not in os.environ
        assert "AWS_SECRET_ACCESS_KEY" not in os.environ
        assert "AWS_PROFILE" not in os.environ

        assert arn.endswith(f"user/{iam_user_name}")

        # assume role
        bsm_assumed = bsm_new.assume_role(
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

        assert "AWS_ACCESS_KEY_ID" not in os.environ
        assert "AWS_SECRET_ACCESS_KEY" not in os.environ
        assert "AWS_SESSION_TOKEN" not in os.environ
        assert "AWS_PROFILE" not in os.environ

        assert f"assumed-role/{iam_role_name}" in arn


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
