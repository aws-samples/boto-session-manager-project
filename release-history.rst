.. _release_history:

Release and Version History
==============================================================================


Backlog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


1.5.1 (2023-04-14)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add auto refreshable session support (beta). Note that it is using ``AssumeRoleCredentialFetcher`` and ``DeferredRefreshableCredentials`` from botocore, which is not public API officially supported by botocore.

**Minor Improvements**

- Use Sentinel ``NOTHING`` instead of ``None`` to remove the ambiguity of ``None`` value.


1.4.3 (2023-04-14)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Miscellaneous**

- Add ``boto3`` as explicit dependency.
- Change license from MIT to Apache 2.0


1.4.2 (2023-03-24)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Fix a bug that the client object cannot locate the right boto3 stubs.


1.4.1 (2023-03-24)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Now all the client and it's methods support auto complete and type hint. You have to do ``pip install "boto3-stubs[all]"`` to enable "Client method auto complete" and "Arguments type hint" features.

**Bugfixes**

- Fix a bug that :meth:`~boto_session_manager.manager.BotoSesManager.awscli()`` context manager doesn't work properly.


1.3.2 (2023-01-31)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add boto3 documentation link in doc string


1.3.1 (2022-12-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Allow to call :meth:`~boto_session_manager.manager.BotoSesManager.clear_cache()` to clear all cached boto session and client.
- Add ton's of property method to access the cached boto client.
- Update the list of AWS service to the latest (as of 2022-12-10), which are 333 services.


1.2.2 (2022-12-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Miscellaneous**

- Now ``boto_session_manager`` doesn't force to install ``boto3`` when installing itself. You have to manage your ``boto3`` installation separately.


1.2.1 (2022-11-20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add :meth:`~boto_session_manager.manager.BotoSesManager.awscli` context manager to pass boto session credential to AWS CLI.


1.1.1 (2022-11-20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- The first API stable version

**Minor Improvements**

- Add ``delta`` arguments for :meth:`~boto_session_manager.manager.BotoSesManager.is_expired` method. allow to check if the session will expire in X seconds.


0.0.4 (2022-05-20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add ``default_client_kwargs`` argument for :class:`boto_session_manager.manager.BotoSesManager`.

**Miscellaneous**

- Use `localstack <https://localstack.cloud/>`_ for unit test.


0.0.3 (2022-05-16)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add additional keyword arguments for :meth:`boto_session_manager.manager.BotoSesManager.get_client` method


0.0.2 (2022-04-30)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Now the public API becomes :class:`boto_session_manager.manager.BotoSesManager`
- Add :meth:`boto_session_manager.manager.BotoSesManager.get_resource` method


0.0.1 (2022-04-26)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First release
- Add :class:`boto_session_manager.manager.BotoSessionManager` class
- Add :class:`boto_session_manager.services.BotoSessionManager` class
