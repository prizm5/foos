cd ~
killall python
killall chromium-browser
cd dev/foos
python -m SimpleHTTPServer 8000 &
chromium-browser http://localhost:8000/web &
sudo python3 foos.py &

 
