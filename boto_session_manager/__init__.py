# -*- coding: utf-8 -*-

"""
Usage::

    >>> from boto_session_manager import BotoSesManager, AwsServiceEnum
    >>> bsm = BotoSesManager()
    >>> s3_client1 = bsm.s3_client
    >>> s3_client2 = bsm.s3_client
    >>> id(s3_client1) == id(s3_client2)
    True
"""

from ._version import __version__

try:
    from .manager import BotoSesManager
    from .services import AwsServiceEnum
except ImportError:  # pragma: no cover
    pass
except:  # pragma: no cover
    raise

__short_description__ = "Python AWS SDK boto3 library enhancement"
__license__ = "MIT"
__author__ = "Sanhe Hu"
__author_email__ = "husanhe@gmail.com"
__maintainer__ = "Sanhe Hu"
__maintainer_email__ = "sanhehu@amazon.com"
__github_username__ = "aws-samples"
