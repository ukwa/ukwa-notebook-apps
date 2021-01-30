#!/bin/sh
docker build -t urn --build-arg https_proxy=http://explorer.bl.uk:3127/ .
