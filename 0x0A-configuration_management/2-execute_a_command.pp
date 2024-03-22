# Execute command
exec { 'terminate process':
  command => 'pkill killmenow',
}
