#!/usr/bin/bash
chmod +x ../black_candle.py
sudo ln -sf ../black_candle.py /usr/bin/black_candle
sudo cp tools/black_candle.desktop ~/.local/share/applications
sudo update-desktop-database
