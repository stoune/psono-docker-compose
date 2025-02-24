import logging
import os
import ssl

from django.core.mail.backends.smtp import EmailBackend

logger = logging.getLogger(__name__)

class CustomSSLEmailBackend(EmailBackend):
    def __init__(self, *args, **kwargs):
        ca_filepath = os.environ.get('CERT_PATH')
        logger.debug("Initializing CustomSSLEmailBackend")
        logger.debug(f"Using CA file path: {ca_filepath}")

        super().__init__(*args, **kwargs)
        self.ssl_context = ssl.create_default_context()
        self.ssl_context.load_verify_locations(cafile=ca_filepath)