#!/usr/bin/env bash

SOURCE="ubuntu@192.168.1.143"
SOURCE_DIR="/var/www/html/"
BACKUP_DIR="/var/backups/website"
DATE=$(date '+%Y-%m-%d_%H-%M-%S')
BACKUP_PATH="$BACKUP_DIR/backup_$DATE"
LOG_FILE="$BACKUP_DIR/backup.log"

if rsync -a -e "ssh -i /home/ubuntu/.ssh/backup_key" \
    "$SOURCE:$SOURCE_DIR" "$BACKUP_PATH/" >> "$LOG_FILE" 2>&1
then
    echo "$(date): Backup successful: $BACKUP_PATH" >> "$LOG_FILE"
else
    echo "$(date): Backup FAILED" >> "$LOG_FILE"
    exit 1
fi
