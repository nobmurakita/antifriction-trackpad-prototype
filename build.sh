#!/bin/sh

APP_NAME=AntifrictionTrackpad
APP_VERSION=1.0

CF_BUNDLE_NAME=${APP_NAME}
CF_BUNDLE_IDENTIFIER=com.example.${APP_NAME}
CF_BUNDLE_VERSION=${APP_VERSION}.$(date +%s)


APP_DIR=dist/${APP_NAME}.app

rm -rf dist/*
mkdir -p ${APP_DIR}/Contents/MacOS
cp src/*.py ${APP_DIR}/Contents/MacOS
chmod +x ${APP_DIR}/Contents/MacOS/app.py

cat <<EOF > ${APP_DIR}/Contents/Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleExecutable</key>
	<string>app.py</string>
	<key>CFBundleName</key>
	<string>${CF_BUNDLE_NAME}</string>
	<key>CFBundleIdentifier</key>
	<string>${CF_BUNDLE_IDENTIFIER}</string>
  <key>CFBundleVersion</key>
  <string>${CF_BUNDLE_VERSION}</string>
	<key>LSUIElement</key>
	<true/>
</dict>
</plist>
EOF
