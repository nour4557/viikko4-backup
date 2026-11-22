from flask import Flask
import pymysql
import os

app = Flask(__name__)

def get_visitors():
    connection = pymysql.connect(
        host="localhost",
        user="viikko4read",
        password=os.environ["DB_PASSWORD"],
        database="viikko2",
        charset="utf8mb4"
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT kaynnit FROM laskuri WHERE id = 1")
            visitors = cursor.fetchone()[0]

        return visitors

    finally:
        connection.close()


@app.route("/")
def home():
    visitors = get_visitors()

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Week 4 - Server B</title>
    </head>
    <body style="font-family: Arial; background-color: #e8d8c3;
                 color: #795548; text-align: center; padding: 20px;">

        <h1>Week 4 - Server B</h1>
        <h2>Read-only Replica</h2>

        <h2>Replicated Visitor Counter</h2>
        <h1>{visitors}</h1>

        <p>This counter is read from the local MariaDB database
        on Server B.</p>

        <p>The database is replicated from Server A.</p>

        <p>This page only uses SELECT and does not increase
        the visitor count.</p>

        <hr>

        <h2>Project Links</h2>
        <p><a href="http://193.166.24.219/viikko2/">Week 2 - Server A</a></p>
        <p><a href="http://193.166.24.219/viikko3/">Week 3 - Server A</a></p>

        <h2>How I created Server B</h2>
        <p>I created Server B using a snapshot of Server A in cPouta.
        Server B has its own IP address.</p>

        <h2>Storage and Backups</h2>
        <p>The website files are stored in /var/www/html on Server A.</p>
        <p>Website backups are copied to /var/backups/website on Server B.</p>
        <p>The backup script uses rsync over SSH and creates a new
        timestamped backup every hour using cron.</p>

        <h2>Users and Permissions</h2>
        <p>The Linux user ubuntu runs the backup script.</p>
        <p>The SSH backup key is stored in the ubuntu user's
        .ssh directory.</p>
        <p>The backup directory is owned by ubuntu and has
        restricted permissions.</p>
        <p>The database user viikko4read has SELECT permission
        on the visitor counter table.</p>

        <h2>Database Replication</h2>
        <p>MariaDB replicates changes from Server A to Server B.</p>
        <p>Server B is configured as a read-only replica.
        The Week 4 application only reads the replicated counter.</p>

        <h2>Testing</h2>
        <p>I checked that both replication threads were running
        and that there were no replication errors.</p>
        <p>I increased the counter on Server A and checked that
        the new value appeared on Server B.</p>

        <h2>What I learned</h2>
        <p>I learned how to create a second server, configure
        database replication and make automatic website backups.</p>

        <h2>GitHub</h2>
        <a href="https://github.com/nour4557/viikko3-Bash-and-a-Server-Status-Report">
        GitHub</a>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
