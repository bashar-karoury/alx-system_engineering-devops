# This Manifest fixs apache2 server 500 status code error
$command1 = "sed -i 's/holberton hard nofile 5/holberton hard nofile 50/' /etc/security/limits.conf"
$command2 = "sed -i 's/holberton soft nofile 4/holberton soft nofile 40/' /etc/security/limits.conf"
exec { 'raise holberton hard f limit':
  command => $command1,
  path    => ['/bin', '/usr/bin'],
}

exec { 'raise holberton soft f limit':
  command => $command2,
  path    => ['/bin', '/usr/bin'],
}
