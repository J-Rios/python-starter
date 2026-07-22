# Deployment Guide

This document describes the deployment and installation procedures for the streamlit-starter project on Linux systems.

## Overview

The project includes automated installation and uninstallation scripts for Linux systems. The installation creates a system service that runs the application with proper user isolation, logging, and automatic startup.

## Project Structure

```
deploy/
├── linux/
│   ├── linux_install       # Linux installation script
│   ├── linux_uninstall     # Linux uninstallation script
│   ├── launcher            # Service launcher script
│   └── streamlit-starter.service  # Systemd service definition

tools/
├── install                 # Linux installation wrapper
└── uninstall               # Linux uninstallation wrapper
```

## Linux Deployment

### Installation

#### Using Make (Recommended)

```bash
sudo make install
```

#### Direct Script

```bash
sudo deploy/linux/linux_install
```

#### What Gets Installed

- **Service User:** `streamlit-starter` (non-privileged user)
- **Installation Directory:** `/opt/streamlit-starter/`
- **Log Directory:** `/var/log/streamlit-starter/`
- **Service File:** `/etc/systemd/system/streamlit-starter.service`
- **Systemd Service:** `streamlit-starter.service`

#### Installation Steps

The installation script performs these steps:

1. **Verify root privileges** - Requires `sudo`
2. **Create application user** - Non-privileged system user for running the service
3. **Install application files** - Copies source code, dependencies config to `/opt/streamlit-starter/`
4. **Setup virtual environment** - Creates `.venv/` and installs `requirements.txt`
5. **Setup logging directory** - Creates `/var/log/streamlit-starter/` with proper permissions
6. **Configure systemd service** - Copies and enables the service file
7. **Start the service** - Launches the application and verifies it's running

### Uninstallation

#### Using Make

```bash
sudo make uninstall
```

#### Direct Script

```bash
sudo deploy/linux/linux_uninstall
```

#### What Gets Removed

- Service files and configuration
- Application directory (`/opt/streamlit-starter/`)
- Log directory (`/var/log/streamlit-starter/`)
- Service user (optional - prompted during uninstall)

#### Uninstallation Steps

1. **Stop the service** - Gracefully stops the running application
2. **Disable the service** - Prevents auto-start on boot
3. **Remove service file** - Deletes `/etc/systemd/system/streamlit-starter.service`
4. **Remove application files** - Deletes `/opt/streamlit-starter/`
5. **Remove log files** - Deletes `/var/log/streamlit-starter/`
6. **Preserve user** - Keeps the `streamlit-starter` user for permission history

### Service Management

#### View Status

```bash
systemctl status streamlit-starter
```

#### Start/Stop/Restart

```bash
sudo systemctl start streamlit-starter
sudo systemctl stop streamlit-starter
sudo systemctl restart streamlit-starter
```

#### View Logs

```bash
# Recent logs
journalctl -u streamlit-starter -n 50

# Follow logs in real-time
journalctl -u streamlit-starter -f

# Logs for last hour
journalctl -u streamlit-starter --since "1 hour ago"

# All logs from service file
tail -f /var/log/streamlit-starter/streamlit-starter.log
```

#### Enable/Disable Auto-start

```bash
sudo systemctl enable streamlit-starter   # Enable auto-start on boot
sudo systemctl disable streamlit-starter  # Disable auto-start on boot
```

## Configuration Files

### Systemd Service File

**Location:** `/etc/systemd/system/streamlit-starter.service`

**Key Settings:**
- `Type=simple` - Service type
- `User=streamlit-starter` - Runs as non-privileged user
- `WorkingDirectory=/opt/streamlit-starter` - Working directory
- `ExecStart=/opt/streamlit-starter/launcher` - Launcher script
- `Restart=always` - Auto-restart on failure
- `RestartSec=10` - Wait 10s before restart

**Modify Service:**

```bash
# Edit the service file
sudo nano /etc/systemd/system/streamlit-starter.service

# Reload systemd
sudo systemctl daemon-reload

# Restart service
sudo systemctl restart streamlit-starter
```

### Launcher Script

**Location:** `/opt/streamlit-starter/launcher`

The launcher script:
1. Sources the virtual environment
2. Sets working directory
3. Runs the application
4. Logs output to file

**Edit Launcher:**

```bash
sudo nano /opt/streamlit-starter/launcher
sudo systemctl restart streamlit-starter
```

## Troubleshooting

### Service Fails to Start

```bash
# Check status
systemctl status streamlit-starter

# View detailed logs
journalctl -u streamlit-starter -n 100

# Check if another instance is running
ps aux | grep streamlit-starter
```

### Permission Denied Errors

```bash
# Fix ownership
sudo chown -R streamlit-starter:streamlit-starter /opt/streamlit-starter
sudo chown -R streamlit-starter:streamlit-starter /var/log/streamlit-starter

# Fix permissions
sudo chmod 755 /opt/streamlit-starter
sudo chmod 644 /var/log/streamlit-starter/streamlit-starter.log
```

### Virtual Environment Issues

```bash
# Check venv
ls -la /opt/streamlit-starter/.venv

# Verify python
/opt/streamlit-starter/.venv/bin/python3 --version

# Reinstall dependencies
sudo /opt/streamlit-starter/.venv/bin/pip install -r /opt/streamlit-starter/requirements.txt
```

### Port Already in Use

If the application uses network ports:

```bash
# Find process using port (e.g., port 8000)
lsof -i :8000

# Kill process
kill -9 <PID>

# Or restart service
sudo systemctl restart streamlit-starter
```

### Check Disk Space

```bash
# Check log size
du -sh /var/log/streamlit-starter/

# Rotate logs if too large
sudo logrotate -f /etc/logrotate.conf
```

## Upgrading the Application

### Backup Current Installation

```bash
sudo cp -r /opt/streamlit-starter /opt/streamlit-starter.backup
```

### Update Application Files

```bash
# Stop the service
sudo systemctl stop streamlit-starter

# Copy new files
sudo cp -r src/ /opt/streamlit-starter/
sudo cp requirements.txt /opt/streamlit-starter/

# Update dependencies
sudo -u streamlit-starter /opt/streamlit-starter/.venv/bin/pip install -r /opt/streamlit-starter/requirements.txt

# Start the service
sudo systemctl start streamlit-starter
```

### Rollback to Previous Version

```bash
# Stop the service
sudo systemctl stop streamlit-starter

# Restore backup
sudo rm -rf /opt/streamlit-starter
sudo mv /opt/streamlit-starter.backup /opt/streamlit-starter

# Start the service
sudo systemctl start streamlit-starter
```

## Security Considerations

### Application User Isolation

- Application runs as non-privileged `streamlit-starter` user
- Cannot access system directories without explicit permission
- Limits damage from security vulnerabilities

### Directory Permissions

- Application directory: `755` (rwxr-xr-x)
- Log files: `644` (rw-r--r--)
- Virtual environment: User-owned for safety

### Log Files

- Automatically rotated by systemd
- Accessible to privileged users for auditing
- Stored in separate directory

### Environment Variables

- Set in service file if needed
- `PYTHONUNBUFFERED=1` for immediate logging
- Avoid storing secrets in service file

## Additional Resources

- [systemd Documentation](https://wiki.debian.org/systemd)
- [Linux User Management](https://wiki.archlinux.org/title/Users_and_groups)
- [systemd Service Files](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
