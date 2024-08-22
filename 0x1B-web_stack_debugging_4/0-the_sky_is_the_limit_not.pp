# This Manifest fixs apache2 server 500 status code error
$command = "sed -i 's/15/200/' /etc/default/nginx"
exec { 'raise limit of workers':
  command => $command,
  path    => ['/bin', '/usr/bin'],
}

# Restart Nginx explicitly
exec { 'restart_nginx':
  command => '/usr/sbin/service nginx restart',
}
