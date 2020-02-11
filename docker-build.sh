#!/bin/sh
docker build -t urn --build-arg https_proxy=http://bspcache.bl.uk:7070/ .
