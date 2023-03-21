# -*- coding: utf-8 -*-

import pytest


def test():
    import boto_session_manager

    _ = boto_session_manager.BotoSesManager
    _ = boto_session_manager.AwsServiceEnum


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
