# This Manifest fixs apache2 server 500 status code error
$one = "sed -i 's/worker_processes 4;/worker_processes 40;/' /path/to/your/nginx.conf"
$two = "$|require_once( ABSPATH . WPINC . '/class-wp-locale.php' );|\" /var/www/html/wp-settings.php"
$value = "${one}${two}"
exec { 'fix typo':
  command => $one,
  path    => ['/bin', '/usr/bin'],
}
