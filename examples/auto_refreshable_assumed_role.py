# -*- coding: utf-8 -*-

import time
from boto_session_manager import BotoSesManager

bsm = BotoSesManager(profile_name="aws_data_lab_open_source_boto_session_manager")
role_name = "project-boto_session_manager"
role_arn = f"arn:aws:iam::{bsm.aws_account_id}:role/{role_name}"

bsm_new = bsm.assume_role(
    role_arn=role_arn,
    # by default, it expires in 15 minutes, but it will automatically refresh
    duration_seconds=900,
    auto_refresh=True,
)

# use the cached client, keep running for 3600 seconds
tick = 60
sleep = 60
for i in range(tick):
    time.sleep(sleep)
    print("elapsed {} seconds".format((i + 1) * sleep))
    print("Account id = {}".format(bsm_new.sts_client.get_caller_identity()["Account"]))
