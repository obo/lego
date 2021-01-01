## Taken from:
## https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/rpyc.html
## run this on robot to get RPyC service

echo "[Unit]
Description=RPyC Classic Service
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/rpyc_classic.py

[Install]
WantedBy=multi-user.target" > rpyc-classic.service

sudo cp rpyc-classic.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable rpyc-classic.service
sudo systemctl start rpyc-classic.service
