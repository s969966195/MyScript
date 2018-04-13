#!/bin/bash

which MEOW || install <(curl 'http://xx/bfs/vc/MEOW') /usr/local/bin/MEOW

mkdir -pm0777 ~/.meow
echo 'listen = http://0.0.0.0:1081
proxy=ss://xxx:000' > ~/.meow/rc

pkill MEOW; nohup MEOW -rc ~/.meowrc >/dev/null 2>&1 &
