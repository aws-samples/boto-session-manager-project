.. image:: https://github.com/aws-samples/boto-session-manager-project/workflows/CI/badge.svg
    :target: https://github.com/aws-samples/boto-session-manager-project/actions?query=workflow:CI

.. image:: https://img.shields.io/pypi/v/boto_session_manager.svg
    :target: https://pypi.python.org/pypi/boto_session_manager

.. image:: https://img.shields.io/pypi/l/boto_session_manager.svg
    :target: https://pypi.python.org/pypi/boto_session_manager

.. image:: https://img.shields.io/pypi/pyversions/boto_session_manager.svg
    :target: https://pypi.python.org/pypi/boto_session_manager

.. image:: https://img.shields.io/pypi/dm/boto_session_manager.svg
    :target: https://pypi.python.org/pypi/boto_session_manager

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/aws-samples/boto-session-manager-project

------

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/aws-samples/boto-session-manager-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/aws-samples/boto-session-manager-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/aws-samples/boto-session-manager-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/boto_session_manager#files


Welcome to ``boto_session_manager`` Documentation
==============================================================================


About ``boto_session_manager``
------------------------------------------------------------------------------
``boto_session_manager`` is a light weight, zero dependency python library that simplify managing your AWS boto3 session in your application code. It bring auto complete and type hint to the default ``boto3`` SDK, and provide smooth development experience with the following goodies:

- boto3 Client auto complete
- Cached boto3 Client
- Assume IAM role in application code
- Set temporary credential for AWS Cli

Additionally, if you use `boto3-stubs <https://pypi.org/project/boto3-stubs/>`_ and you did ``pip install "boto3-stubs[all]"``, then ``boto_session_manager`` comes with the auto complete and type hint for all boto3 methods out-of-the-box, without any extra configuration (such as `explicit type annotations <https://pypi.org/project/boto3-stubs/#explicit-type-annotations>`_)


Feature
------------------------------------------------------------------------------
**Boto Client Auto Complete**

Provide an Enum class to access the aws service name to create boto client.

.. code-block:: python

    from boto_session_manager import BotoSesManager, AwsServiceEnum

    bsm = BotoSesManager()
    s3_client = bsm.s3_client

.. image:: https://user-images.githubusercontent.com/6800411/227536578-839191b7-e1b3-4f92-92b3-9dd5309ea307.gif

One click to jump to the documentation:

.. image:: https://user-images.githubusercontent.com/6800411/227536582-8e743936-95a8-4697-b382-72007ff72198.gif

Client method auto complete:

.. image:: https://user-images.githubusercontent.com/6800411/227536584-bdbc10d0-bb1a-458d-9248-5d5646a910de.gif

Arguments type hint:

.. image:: https://user-images.githubusercontent.com/6800411/227537394-9a494249-1899-4a76-98a7-41ff7a3ac4a6.gif

Note: you have to do ``pip install "boto3-stubs[all]"`` to enable "Client method auto complete" and "Arguments type hint" features.

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
    # --- within awscli() context manager ---
    # AWS_ACCESS_KEY_ID = ABCDEFG...
    # AWS_SECRET_ACCESS_KEY = ABCDEFG...
    # AWS_SESSION_TOKEN = ABCDEFG...
    # AWS_REGION = us-east-1
    # --- after ---
    # AWS_ACCESS_KEY_ID = None
    # AWS_SECRET_ACCESS_KEY = None
    # AWS_SESSION_TOKEN = None
    # AWS_REGION = None


.. _install:

Install
------------------------------------------------------------------------------

``boto_session_manager`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install boto_session_manager

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade boto_session_manager
