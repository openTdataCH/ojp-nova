## Install

```
# Edit service file
nano /var/projects/ojp-nova/service/ojp-nova.service

# Create (symlink) Systemd Service File
cd /etc/systemd/system
sudo ln -s /var/projects/ojp-nova/service/ojp-nova.service .

# Reload the systemd daemon to recognize your new service:
sudo systemctl daemon-reload

# Start Python application as a service:
sudo systemctl start ojp-nova.service

# Enable the service to start on boot:
sudo systemctl enable ojp-nova.service
```

## Operations
```
# Verify that your service is running:
sudo systemctl status ojp-nova.service

# View the application logs:
journalctl -u ojp-nova.service
```