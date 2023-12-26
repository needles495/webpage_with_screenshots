# webpage_with_screenshots
/var/www/termon/
|-- conf
|   `-- htpasswd
|-- favicon.ico
|-- index.html
|-- run.sh
|-- sc2_v1.py
|-- sc2_v2.py
|-- sc2_v3.py
|-- sc3_v1.1.py
|-- sc3_v1.py
|-- sc3_v2.py
|-- sc.py
|-- sc_v2.py
|-- sc_v3.py
|-- test2.html
|-- test.html
`-- test.py

#21:51:01 [root@video termon]# cat /etc/nginx/conf.d/pic.workeat.com.conf
server {
    listen 50080;
    location / {
        auth_basic_user_file /var/www/termon/conf/htpasswd;
        auth_basic "Restricted Content";
        root /var/www/termon;
        expires           -1;
        add_header 'Cache-Control' 'no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0';
    }
    location ~\.(py|sh|conf)$|htpasswd$ {
        deny all;
        return 404;
    }
    access_log /var/log/nginx/pic.workeat.com-access.log;
    error_log /var/log/nginx/pic.workeat.com-error.log;
}
server {
    listen          50081 ssl;
    server_name     pic.workeat.com,82.202.166.34;
    location / {
        auth_basic_user_file /var/www/termon/conf/htpasswd;
        auth_basic "Restricted Content";
        root /var/www/termon;
    }
    location ~\.(py|sh|conf)$ {
        deny all;
        return 404;
    }


    ssl_certificate /etc/nginx/ssl/video.workeat.com.fullchain.pem;
    ssl_certificate_key /etc/nginx/ssl/video.workeat.com.privkey.pem;
    access_log /var/log/nginx/pic.workeat.com-access.log;
    error_log /var/log/nginx/pic.workeat.com-error.log;
}
