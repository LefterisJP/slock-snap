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

# if the config.yaml is not copied to the APP_DATA path copy it there
if [ ! -e "$SNAP_APP_DATA_PATH/conf/config.yaml" ]; then
    mkdir -p "$SNAP_APP_DATA_PATH/conf/"
    cp "$SNAP_APP_PATH/conf/config.yaml" "$SNAP_APP_DATA_PATH/conf/config.yaml"
fi

export NODE_PATH=./lib/node_modules:$NODE_PATH
$NODE_EXEC ./lib/node_modules/slock/bin/slock.js "$SNAP_APP_DATA_PATH/conf/config.yaml"
