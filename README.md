#Installation
1. Clone the repository and copy it to /var/www/.
2. Create `local_settings.py` in `ayudh` folder and set values as required.
3. Install `apache2`, `mysql-server` and `libapache2-mod-wsgi`.
    ```bash
    sudo apt-get install apache2 mysql-server-5.5 libapache2-mod-wsgi
    ```
4. Install app requirements: `Django`, `Bootstrap` etc
    ```bash
    sudo apt-get install python-pip
    ```
    ```bash
    sudo pip install -r requirements
    ```
#Development
if you are planning to develop this application, I would highly suggest you
to run it on a python virtual environment. Before the step [4], you could 
install `virtualenvwrapper`

1.  `virtualenvwrapper`
    ```bash
    sudo pip install virtualenvwrapper
    ```
2. Make a virtual environment
    ```bash
    mkvirutalenv ayudh
    ```
3. If you want to workon the same virtualenv
    ```bash
    workon ayudh
    ```

#Possible Issues
1. Invalid command `WSGIScriptAlias`, perhaps misspelled or defined by a 
module not included in the server configuration. This is because WSGI 
module is not loaded into apache2. Add the following line to 
`/etc/apache2/mods-available/wsgi.load`
`LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so`
and create a symlink to the file in `/etc/apache2/mods-enabled`. Don't 
forget to restart apache :).
2. Server error when registering a user This is probably because Apache 
is unable to create `email_list`. To resolve this, determine the path 
where Apache tries to create the file by turning Debug mode on and 
create it with 666 permissions.

#Configuring automatic emailing of database dump
Using mutt and cron, it's possible to get the database dump emailed 
periodically. Use the following script to send the database dump via 
email:

```bash
#!/bin/bash

ctime=`/bin/date`
dumpfile="/tmp/dump-"$ctime
/usr/bin/mysqldump -u <username> -p<password> <database> > "$dumpfile"
echo "Database backup" | mutt -e "my_hdr From:DB Dumper<dbdump@ayudh.in>" -s "Database backup at $ctime" -a "$dumpfile" -- recipient1@gmail.com,recipient2@gmail.com
rm "$dumpfile"
```

Note: Since the database password is hardcoded in the script, make 
the script file accessible to root and no other user.

Add this entry to `/etc/crontab` to run the script at `10:00` everyday.
```bash
00 10   * * *   root    /path/to/db/backup/script.sh
```


