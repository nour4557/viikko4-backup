# Week 4 - Server Backup and Database Replication

## Servers
- Server A runs the Week 2 application and Week 3 report.
- Server B was created using a snapshot of Server A.
- Server B has its own IP address.

## Website Backup
- The backup script is backup.sh.
- It copies website files from Server A to Server B using rsync and SSH.
- Backups run automatically every hour using cron.
- Backups are stored in /var/backups/website on Server B.
- The script saves successful and failed backup messages in backup.log.

## Database Replication
- MariaDB replicates data from Server A to Server B.
- Server B is configured as a read-only replica.
- The Week 4 application only reads the visitor counter.

## Application
- app.py displays the replicated visitor counter.
- The application uses the local MariaDB database on Server B.

## Scheduled Tasks
See crontab.txt for the cron configuration.

## Security
Passwords and private SSH keys are stored outside the GitHub repository.
