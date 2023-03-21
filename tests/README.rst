New Test Strategy
------------------------------------------------------------------------------
Use REAL IAM User / Role on a service account with minimal permission

**IAM User**

Name is ``project-boto_session_manager``. Give program access only, Policy is::

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": "sts:AssumeRole",
                "Resource": "arn:aws:iam::${AWS_ACCOUNT_ID}:role/project-boto_session_manager"
            },
            {
                "Sid": "VisualEditor1",
                "Effect": "Allow",
                "Action": [
                    "sts:GetAccessKeyInfo",
                    "sts:GetCallerIdentity"
                ],
                "Resource": "*"
            }
        ]
    }

**IAM Role**

Name is ``project-boto_session_manager``.

Trusted Relationship::

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "AWS": "arn:aws:iam::${AWS_ACCOUNT_ID}:root"
                },
                "Action": "sts:AssumeRole",
                "Condition": {}
            }
        ]
    }

Policy is::

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "sts:GetAccessKeyInfo",
                    "sts:GetCallerIdentity"
                ],
                "Resource": "*"
            }
        ]
    }


Old Test Strategy
------------------------------------------------------------------------------
It use `localstack <https://localstack.cloud/>`_ for testing.

To test, run ``localstack start``.

To stop localstack, run ``localstack stop``.
