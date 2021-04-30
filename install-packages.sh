#!/bin/bash

export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get -y upgrade
apt-get -y install --no-install-recommends wkhtmltopdf
apt-get clean
rm -rf /var/lib/apt/lists/*