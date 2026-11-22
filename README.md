My servers

I made a second server (Server B) using a snapshot of my first server (Server A) in cPouta. Server B has its own IP address.

Server A still runs my Week 2 application and Week 3 report.

Website backups

I made a script called backup.sh to copy the website files from Server A to Server B.

I used rsync and SSH to transfer the files. The backups are saved in /var/backups/website on Server B.

I added the script to cron so it runs automatically every hour. Each backup gets its own date and time in the folder name.

The script also writes messages to backup.log so I can see if a backup worked or failed.

Database replication

I set up MariaDB replication from Server A to Server B.

When the visitor counter changes on Server A, the update is copied to Server B.

I made a separate database user called viikko4read for the Week 4 page. It only has permission to read the counter.

Week 4 page

The Week 4 page runs on Server B and shows the visitor counter from its local database.

It only reads the value. It does not increase the counter.

Testing

I tested the backup script and checked that it created backup folders.

I also restored a test file to a separate folder and compared its SHA256 hash with the original file. The hashes matched.

I tested the database replication by opening the Week 2 page on Server A and checking that the counter updated on Server B.

What I learned

I learned how to create another server from a snapshot, copy website files between servers and make automatic backups.

I also learned more about MariaDB replication and how to give database users different permissions.
