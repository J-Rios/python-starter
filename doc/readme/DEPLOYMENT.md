# Deployment Guide

This document describes the deployment and installation procedures for the python-starter project on Linux systems.

## Overview

The project includes automated installation and uninstallation scripts for Linux systems. The installation creates a system service that runs the application with proper user isolation, logging, and automatic startup.

## Project Structure

```
deploy/
├── linux/
│   ├── linux_install       # Linux installation script
│   ├── linux_uninstall     # Linux uninstallation script
│   ├── launcher            # Service launcher script
│   └── python-starter.service  # Systemd service definition

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

- **Service User:** `python-starter` (non-privileged user)
- **Installation Directory:** `/opt/python-starter/`
- **Log Directory:** `/var/log/python-starter/`
- **Service File:** `/etc/systemd/system/python-starter.service`
- **Systemd Service:** `python-starter.service`

#### Installation Steps

The installation script performs these steps:

1. **Verify root privileges** - Requires `sudo`
2. **Create application user** - Non-privileged system user for running the service
3. **Install application files** - Copies source code, dependencies config to `/opt/python-starter/`
4. **Setup virtual environment** - Creates `.venv/` and installs `requirements.txt`
5. **Setup logging directory** - Creates `/var/log/python-starter/` with proper permissions
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
- Application directory (`/opt/python-starter/`)
- Log directory (`/var/log/python-starter/`)
- Service user (optional - prompted during uninstall)

#### Uninstallation Steps

1. **Stop the service** - Gracefully stops the running application
2. **Disable the service** - Prevents auto-start on boot
3. **Remove service file** - Deletes `/etc/systemd/system/python-starter.service`
4. **Remove application files** - Deletes `/opt/python-starter/`
5. **Remove log files** - Deletes `/var/log/python-starter/`
6. **Preserve user** - Keeps the `python-starter` user for permission history

### Service Management

#### View Status

```bash
systemctl status python-starter
```

#### Start/Stop/Restart

```bash
sudo systemctl start python-starter
sudo systemctl stop python-starter
sudo systemctl restart python-starter
```

#### View Logs

```bash
# Recent logs
journalctl -u python-starter -n 50

# Follow logs in real-time
journalctl -u python-starter -f

# Logs for last hour
journalctl -u python-starter --since "1 hour ago"

# All logs from service file
tail -f /var/log/python-starter/python-starter.log
```

#### Enable/Disable Auto-start

```bash
sudo systemctl enable python-starter   # Enable auto-start on boot
sudo systemctl disable python-starter  # Disable auto-start on boot
```

## Configuration Files

### Systemd Service File

**Location:** `/etc/systemd/system/python-starter.service`

**Key Settings:**
- `Type=simple` - Service type
- `User=python-starter` - Runs as non-privileged user
- `WorkingDirectory=/opt/python-starter` - Working directory
- `ExecStart=/opt/python-starter/launcher` - Launcher script
- `Restart=always` - Auto-restart on failure
- `RestartSec=10` - Wait 10s before restart

**Modify Service:**

```bash
# Edit the service file
sudo nano /etc/systemd/system/python-starter.service

# Reload systemd
sudo systemctl daemon-reload

# Restart service
sudo systemctl restart python-starter
```

### Launcher Script

**Location:** `/opt/python-starter/launcher`

The launcher script:
1. Sources the virtual environment
2. Sets working directory
3. Runs the application
4. Logs output to file

**Edit Launcher:**

```bash
sudo nano /opt/python-starter/launcher
sudo systemctl restart python-starter
```

## Troubleshooting

### Service Fails to Start

```bash
# Check status
systemctl status python-starter

# View detailed logs
journalctl -u python-starter -n 100

# Check if another instance is running
ps aux | grep python-starter
```

### Permission Denied Errors

```bash
# Fix ownership
sudo chown -R python-starter:python-starter /opt/python-starter
sudo chown -R python-starter:python-starter /var/log/python-starter

# Fix permissions
sudo chmod 755 /opt/python-starter
sudo chmod 644 /var/log/python-starter/python-starter.log
```

### Virtual Environment Issues

```bash
# Check venv
ls -la /opt/python-starter/.venv

# Verify python
/opt/python-starter/.venv/bin/python3 --version

# Reinstall dependencies
sudo -u python-starter /opt/python-starter/.venv/bin/pip install -r /opt/python-starter/requirements.txt
```

### Port Already in Use

If the application uses network ports:

```bash
# Find process using port (e.g., port 8000)
lsof -i :8000

# Kill process
kill -9 <PID>

# Or restart service
sudo systemctl restart python-starter
```

### Check Disk Space

```bash
# Check log size
du -sh /var/log/python-starter/

# Rotate logs if too large
sudo logrotate -f /etc/logrotate.conf
```

## Upgrading the Application

### Backup Current Installation

```bash
sudo cp -r /opt/python-starter /opt/python-starter.backup
```

### Update Application Files

```bash
# Stop the service
sudo systemctl stop python-starter

# Copy new files
sudo cp -r src/ /opt/python-starter/
sudo cp requirements.txt /opt/python-starter/

# Update dependencies
sudo -u python-starter /opt/python-starter/.venv/bin/pip install -r /opt/python-starter/requirements.txt

# Start the service
sudo systemctl start python-starter
```

### Rollback to Previous Version

```bash
# Stop the service
sudo systemctl stop python-starter

# Restore backup
sudo rm -rf /opt/python-starter
sudo mv /opt/python-starter.backup /opt/python-starter

# Start the service
sudo systemctl start python-starter
```

## Security Considerations

### Application User Isolation

- Application runs as non-privileged `python-starter` user
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
