---
title: Download the certificate if SSL_CERT is not provided
category: misc
source_lines: 24768-24778
line_count: 10
---

# Download the certificate if SSL_CERT is not provided
if not SSL_CERT:
    SSL_CERT = download_cert(
        cert_url="https://portal.singlestore.com/static/ca/singlestore_bundle.pem",
        filename="singlestore_bundle.pem",
    )
    if SSL_CERT:
        os.environ["SINGLESTORE_SSL_CERT"] = SSL_CERT


