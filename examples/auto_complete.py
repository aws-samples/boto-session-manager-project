from boto_session_manager import BotoSesManager

bsm = BotoSesManager()

bsm.s3_client.put_object()