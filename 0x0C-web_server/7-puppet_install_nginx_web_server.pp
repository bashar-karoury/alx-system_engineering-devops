# This Manifest installs Nginx server into server
exec { 'apt_update':
  command => '/usr/bin/apt update',
}

package { 'nginx':
  ensure => installed,
}

$nginx_config_content = @(EOF)
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /redirect_me {
        return 301;
    }

    location / {
	return 200 "Hello World!
    }
}
EOF

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => $nginx_config_content,
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
