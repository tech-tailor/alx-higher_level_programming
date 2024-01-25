#!/usr/bin/bash
# check bbody size of a response
curl -sI $1 | grep -i content-length | sed 's/[^0-9]*//'
