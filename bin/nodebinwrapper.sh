#!/bin/sh

platform=`uname -i`
NODE_EXEC=

# choose the right node executable depending on platform
case $platform in
  x86_64)
    NODE_EXEC=node
    ;;
  armv7l)
    NODE_EXEC=arm-node
    ;;
  *)
    echo "unknown platform "
    ;;
esac

export NODE_PATH=./lib/node_modules:$NODE_PATH
$NODE_EXEC ./lib/node_modules/slock/bin/slock-snap.js
