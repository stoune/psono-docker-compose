#!/bin/sh

docker run --rm -v $(pwd):/certs -w /certs alpine sh generate_certificates.sh