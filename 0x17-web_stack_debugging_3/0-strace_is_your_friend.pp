# This Manifest fixs apache2 server 500 status code error
$one = "sed -i \"s|^require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );"
$two = "$|require_once( ABSPATH . WPINC . '/class-wp-locale.php' );|\" /var/www/html/wp-settings.php"
$value = "${one}${two}"
exec { 'fix typo':
  command => $value,
  path    => ['/bin', '/usr/bin'],
}
