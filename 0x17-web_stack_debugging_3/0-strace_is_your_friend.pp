# This Manifest fixs apache2 server 500 status code error
exec { 'fix typo':
  command => "sed -i \"s|^require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );"+
  "$|require_once( ABSPATH . WPINC . '/class-wp-locale.php' );|\" /var/www/html/wp-settings.php",
  path    => ['/bin', '/usr/bin'],
}
