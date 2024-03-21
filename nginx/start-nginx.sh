#!/bin/sh
envsubst '__APP_SERVER_PORT__' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf
exec nginx -g 'daemon off;'