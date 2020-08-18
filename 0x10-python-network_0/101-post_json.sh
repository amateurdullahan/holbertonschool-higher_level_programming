#!/bin/bash
# Death of Stalin is pretty funny
curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"
