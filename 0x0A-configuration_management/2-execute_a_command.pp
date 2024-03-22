# Execute command

exec { 'terminate process':
  command  => 'pkill killmenow',
  provider => 'shell'
}
