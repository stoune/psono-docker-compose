#!/bin/sh
set -e  # Exit on error

# Default name (can be overridden by an environment variable or argument)
CERT_NAME="${CERT_NAME:-mailserver}"

apk add --no-cache openssl coreutils > /dev/null 2>&1  # Silent install

# Generate private key & self-signed certificate in one step
openssl req -new -newkey rsa:2048 -nodes -keyout "${CERT_NAME}.key" -x509 -days 1095 -out "${CERT_NAME}.crt" -subj "/C=UA/ST=Kyiv/L=Kyiv/O=UN/OU=Peaceda/CN=mailserver"

# Combine key and certificate into a PEM file
cat "${CERT_NAME}.crt" "${CERT_NAME}.key" > "${CERT_NAME}.pem"

# Display fingerprint
openssl x509 -noout -fingerprint -sha256 -inform pem -in "${CERT_NAME}.pem"
