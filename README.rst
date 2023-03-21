.. image:: https://github.com/MacHu-GWU/boto_session_manager-project/workflows/CI/badge.svg
    :target: https://github.com/MacHu-GWU/boto_session_manager-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/boto_session_manager-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/boto_session_manager-project

.. image:: https://img.shields.io/pypi/v/boto_session_manager.svg
    :target: https://pypi.python.org/pypi/boto_session_manager

.. image:: https://img.shields.io/pypi/pyversions/boto_session_manager.svg
    :target: https://pypi.python.org/pypi/boto_session_manager

.. image:: https://img.shields.io/pypi/dm/boto_session_manager.svg

------

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_


Welcome to ``boto_session_manager`` Documentation
==============================================================================


About ``boto_session_manager``
------------------------------------------------------------------------------
``boto_session_manager`` is a light weight, zero dependency python library that simplify managing your AWS boto3 session in your application code. It bring auto complete and type hint to the default ``boto3`` SDK, and provide smooth development experience with the following goodies:

- boto3 Client auto complete
- Cached boto3 Client
- Assume IAM role in application code
- Set temporary credential for AWS Cli


Feature
------------------------------------------------------------------------------
**Boto Client Enum**

Provide an Enum class to access the aws service name to create boto client.

.. code-block:: python

    from boto_session_manager import BotoSesManager, AwsServiceEnum

    bsm = BotoSesManager()
    s3_client = bsm.s3_client

.. image:: https://user-images.githubusercontent.com/6800411/215315252-52d89d6a-d234-4635-b412-044894a46442.gif

One click to jump to the documentation:

.. image:: https://user-images.githubusercontent.com/6800411/215315251-162886ee-067e-4441-882e-f2641b0997ca.gif

**Cached Client**

Once an boto session is defined, each AWS Service client should be created only once in most of the case. ``boto_session_manager.BotoSesManager.get_client(service_name)`` allow you to fetch the client object from cache if possible.

.. code-block:: python

    from boto_session_manager import BotoSesManager, AwsServiceEnum

    bsm = BotoSesManager()
    s3_client1 = bsm.get_client(AwsServiceEnum.S3)
    s3_client2 = bsm.get_client(AwsServiceEnum.S3)
    assert id(s3_client1) = id(s3_client2)
    
Or you can just do:

.. code-block:: python

    bsm.s3_client.list_buckets() # it cache the client when needed

**Assume Role**

Create another boto session manager based on an assumed IAM role. Allow you to check if it is expired and maybe renew later.

.. code-block:: python

    bsm_assumed = bsm.assume_role("arn:aws:iam::669508176277:role/sanhe-assume-role-for-iam-test")
    sts_client = bsm_assumed.get_client(AwsServiceEnum.sts)
    print(sts_client.get_caller_identity())

    print(bsm_assumed.is_expired())

**AWS CLI context manager**

You explicitly defined a boto session manager that is not the same as the default one used by your AWS CLI. The ``boto_session_manager.BotoSesManager.awscli()`` context manager can temporarily set your default AWS CLI credential as the same as the one you defined, and automatically revert it back.

.. code-block:: python

    # explicitly define a boto session manager
    bsm = BotoSesManager(
        profile_name="my_aws_profile",
    )

    with bsm.awscli():
        # now the default AWS CLI credential is the same as the ``bsm`` you defined

Here's a more detailed example:

.. code-block:: python

    import os
    from boto_session_manager import BotoSesManager

    def print_default_aws_cli_credential():
        print("AWS_ACCESS_KEY_ID =", os.environ.get("AWS_ACCESS_KEY_ID"))
        print("AWS_SECRET_ACCESS_KEY =", os.environ.get("AWS_SECRET_ACCESS_KEY"))
        print("AWS_SESSION_TOKEN =", os.environ.get("AWS_SESSION_TOKEN"))
        print("AWS_REGION =", os.environ.get("AWS_REGION"))
        print("AWS_PROFILE =", os.environ.get("AWS_PROFILE"))

    print("--- before ---")
    print_default_aws_cli_credential()

    bsm = BotoSesManager(profile_name="aws_data_lab_open_source_us_east_1")
    with bsm.awscli():
        print("--- within awscli() context manager ---")
        print_default_aws_cli_credential()

    print("--- after ---")
    print_default_aws_cli_credential()

    # --- before ---
    # AWS_ACCESS_KEY_ID = None
    # AWS_SECRET_ACCESS_KEY = None
    # AWS_SESSION_TOKEN = None
    # AWS_REGION = None
    # AWS_PROFILE = None
    # --- within awscli() context manager ---
    # AWS_ACCESS_KEY_ID = ABCDEFG...
    # AWS_SECRET_ACCESS_KEY = ABCDEFG...
    # AWS_SESSION_TOKEN = ABCDEFG...
    # AWS_REGION = us-east-1
    # AWS_PROFILE = None
    # --- after ---
    # AWS_ACCESS_KEY_ID = None
    # AWS_SECRET_ACCESS_KEY = None
    # AWS_SESSION_TOKEN = None
    # AWS_REGION = None
    # AWS_PROFILE = None


.. _install:

Install
------------------------------------------------------------------------------

``boto_session_manager`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install boto_session_manager

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade boto_session_manager
