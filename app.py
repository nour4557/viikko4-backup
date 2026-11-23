from flask import Flask
import pymysql
import os

app = Flask(__name__)


def get_visitors():
    connection = pymysql.connect(
        host="localhost",
        user="viikko4read",
        password=os.environ["DB_PASSWORD"],
        database="viikko2"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT kaynnit FROM laskuri WHERE id = 1")
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result[0] if result else 0


@app.route("/")
def home():
    visitors = get_visitors()

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Week 4 - Server B</title>

        <style>
            body {{
                background-color: #f5eee5;
                font-family: Arial, sans-serif;
                color: #49382d;
                margin: 0;
                padding: 30px 15px;
                line-height: 1.6;
            }}

            .container {{
                max-width: 850px;
                margin: auto;
            }}

            .card {{
                background: #fffaf4;
                padding: 25px;
                margin-bottom: 20px;
                border-radius: 12px;
            }}

            h1, h2 {{
                color: #805b43;
            }}

            h1 {{
                text-align: center;
            }}

            h2 {{
                border-bottom: 1px solid #e8d8c3;
                padding-bottom: 8px;
            }}

            .counter {{
                text-align: center;
                font-size: 50px;
                font-weight: bold;
                color: #9b704f;
                margin: 15px;
            }}

            a {{
                color: #795548;
            }}

            li {{
                margin-bottom: 8px;
            }}
        </style>
    </head>

    <body>
    <div class="container">

        <div class="card">
            <h1>Week 4 - Server B</h1>

            <p style="text-align:center;">
                 Week 4 Server - Replication
            </p>

            <h2 style="text-align:center;">Visitor Counter</h2>

            <div class="counter">{visitors}</div>

            <p style="text-align:center;">
                This counter shows the value from Server B's database,
                and this page does not increase it.
            </p>
        </div>


        <div class="card">
            <h2>Server setup</h2>

            <p>
                Server A is my first server. It runs my Week 2 application, which I made with Python and Flask, and my Week 3 report, which I made with Bash.
            </p>

            <p>
        I use Nginx to serve the pages and connect the Flask
        application to the website.
            </p>
            <p>
                I made Server B from a snapshot of Server A in cPouta.
                After creating it, I gave B its own IP address.
            </p>

            <p>
               Server A is the main server where the visitor counter
        changes. Server B gets the updates through MariaDB
        replication and shows the counter on this page.
            </p>

            <ul>
                <li>
                    <a href="http://193.166.24.219/viikko2/">
                        Server A - Week 2
                    </a>
                </li>
                <li>
                    <a href="http://193.166.24.219/viikko3/">
                        Server A - Week 3
                    </a>
                </li>
            </ul>
        </div>


        <div class="card">
    <h2>Storage and users</h2>

    <h3>Server A - Primary Server</h3>

    <p>
        Server A contains the original website files and the
        primary MariaDB database.
    </p>

    <ul>
        <li><code>/var/www/html/</code> - Original website files.</li>
        <li><code>/home/ubuntu/viikko2/</code> - Week 2 Python and Flask application.</li>
        <li><code>/home/ubuntu/viikko3/report.sh</code> - Week 3 Bash report script.</li>
        <li><code>/var/lib/mysql/</code> - MariaDB database files.</li>
    </ul>

    <h3>Server B - Replica and Backup Server</h3>

    <p>
        Server B receives website backups from Server A and
        has a local copy of the replicated database.
    </p>

    <ul>
        <li><code>/var/backups/website/</code> - Website backups and backup log.</li>
        <li><code>/home/ubuntu/viikko4/</code> - Week 4 application and backup script.</li>
        <li><code>/var/lib/mysql/</code> - Local MariaDB database files.</li>
        <li><code>/etc/viikko4.env</code> - Database password settings.</li>
    </ul>

    <h3>Users and permissions</h3>

    <p>
        I use the Linux user ubuntu to run the backup script.
        The backup folder belongs to ubuntu and has restricted permissions.
    </p>

    <p>
        I created a database user called viikko4read for the
        Week 4 application. It only has permission to read the
        visitor counter table.
    </p>

    <p>
        The database on Server B is set to read-only so that
        the application does not change the replicated data.
    </p>
</div>


        <div class="card">
            <h2>Website backups</h2>

            <p>
                I made a script called backup.sh to copy the website
                files from A to B. I used rsync and SSH for this.
            </p>

            <p>
                I added the script to cron so it runs every hour.
                Each backup has its own date and time in the folder name.
            </p>

            <p>
                The script also saves a message in backup.log to show
                if the backup worked or failed.
            </p>
        </div>


        <div class="card">
            <h2>Database replication</h2>

            <p>
                I set up MariaDB replication between A and B.
                A is the main database and B gets the changes from it.
            </p>

            <p>
                I opened the Week 2 page on A a few times and saw
                that the counter updated on B too.
            </p>

            <p>
                The Week 4 page only reads the counter. It does not
                increase it or make changes to the database.
            </p>

            <p>
                Replication is not the same as a backup. If I delete
                something by mistake on A, that change can also appear
                on B. Backups are useful because I can go back to an
                older copy of the files.
            </p>
        </div>


        <div class="card">
            <h2>Testing</h2>

            <ul>
                <li>I checked that both Week 2 and Week 4 pages open.</li>
                <li>I opened the Week 2 page on A a few times and saw that the counter updated on B too.</li>
                <li>I opened the Week 4 page on B and checked that it did not increase the counter.</li>
                <li>I checked MariaDB and saw that both replication threads were running.</li>
                <li>I made timestamped backups of the website files.</li>
                <li>I restored a test file to another folder and checked its SHA256 hash against the original file. They matched.</li>
            </ul>

            <p>
                I still need to test that everything works after
                restarting Server B.
            </p>
        </div>


       <div class="card">
            <h2>What I learned</h2>

            <p>
                I learned how to make a second server from a snapshot in CSC cPouta by launching a new instance. I also learned how to copy files between two servers.
            </p>

            <p>
                One problem I had was that I didn't have enough floating IP addresses available because I still had one assigned to a test instance. I deleted the test instance and reused its floating IP addr>
            </p>

            <p>
                I also learned how to make automatic backups with cron and how MariaDB replication works.
            </p>

            <p>
                I had to install and configure MariaDB because the original server had a different database setup. I also learned how to give a database user only the permissions it needs.
            </p>
        </div>


        <div class="card">
            <h2>GitHub</h2>
            <p>
                <a href="https://github.com/nour4557/viikko4-backup">
    My Week 4 GitHub repository
                </a>
            </p>
        </div>

    </div>
    </body>
    </html>
    """
