#!/bin/bash
# comment :)
curl -s -o /dev/null -w "%{response_code}" "$1"
