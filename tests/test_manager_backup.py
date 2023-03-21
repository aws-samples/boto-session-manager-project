# this is old code that I use localstack to test, but it didn't work well
# but I would like to leave it here for reference
#
# # -*- coding: utf-8 -*-
#
# import pytest
#
# import os
# import json
# from boto_session_manager.manager import BotoSesManager, AwsServiceEnum
#
# if "CI" in os.environ:  # pragma: no cover
#     endpoint_url = "http://localstack.cloud"
# else:  # pragma: no cover
#     endpoint_url = "http://localhost.localstack.cloud:4566"
#
# bsm = BotoSesManager(
#     default_client_kwargs=dict(
#         endpoint_url=endpoint_url,
#     )
# )
#
#
# class TestBotoSesManager:
#     def test_aws_account_id_and_region(self):
#         _ = bsm.aws_account_id
#         _ = bsm.aws_region
#
#     def test_get_client(self):
#         s3_client1 = bsm.get_client(AwsServiceEnum.S3)
#         s3_client2 = bsm.get_client(AwsServiceEnum.S3)
#         assert id(s3_client1) == id(s3_client2)
#
#     def test_get_resource(self):
#         s3_resource1 = bsm.get_resource(AwsServiceEnum.S3)
#         s3_resource2 = bsm.get_resource(AwsServiceEnum.S3)
#         assert id(s3_resource1) == id(s3_resource2)
#
#     def test_is_expired(self):
#         assert bsm.is_expired() is False
#
#     def test_assume_role(self):
#         s3_client = bsm.get_client(AwsServiceEnum.S3)
#         res = s3_client.list_buckets()
#         assert len(res["Buckets"]) == 0
#
#         localstack_account_id = "000000000000"
#
#         sts_client = bsm.get_client((AwsServiceEnum.STS))
#         res = sts_client.get_caller_identity()
#         assert res["Account"] == localstack_account_id
#
#         # Test IAM role and Assumed IAM Role
#         role_name = "external_account_assume_role"
#         iam_client = bsm.get_client(AwsServiceEnum.IAM)
#         res = iam_client.list_roles()
#
#         if len(res["Roles"]) == 0:
#             iam_client.create_role(
#                 RoleName=role_name,
#                 AssumeRolePolicyDocument=json.dumps(
#                     {
#                         "Version": "2012-10-17",
#                         "Statement": [
#                             {
#                                 "Effect": "Allow",
#                                 "Principal": {
#                                     "AWS": f"arn:aws:iam::{localstack_account_id}:root"
#                                 },
#                                 "Action": "sts:AssumeRole",
#                                 "Condition": {},
#                             }
#                         ],
#                     }
#                 ),
#             )
#
#         iam_client.put_role_policy(
#             RoleName=role_name,
#             PolicyName="policy",
#             PolicyDocument=json.dumps(
#                 {
#                     "Version": "2012-10-17",
#                     "Statement": [{"Effect": "Allow", "Action": "*", "Resource": "*"}],
#                 }
#             ),
#         )
#
#         bsm_assumed = bsm.assume_role(
#             role_arn=f"arn:aws:iam::{localstack_account_id}:role/{role_name}"
#         )
#         sts_client_assumed = bsm_assumed.get_client(AwsServiceEnum.STS)
#         res = sts_client_assumed.get_caller_identity()
#         assert res["Arn"].startswith(
#             f"arn:aws:sts::{localstack_account_id}:assumed-role/{role_name}"
#         )
#         assert bsm_assumed.expiration_time <= bsm.expiration_time
#
#
# if __name__ == "__main__":
#     import os
#
#     basename = os.path.basename(__file__)
#     pytest.main([basename, "-s", "--tb=native"])
