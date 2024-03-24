# change sshd configuration file
file_line { 'Declare identity file':
  ensure  => present,
  path    => '/etc/ssh/sshd_config',
  line    => 'HostKey ~/.ssh/school',
  match   => '^#?HostKey.+$',
  replace => true,
}
file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/sshd_config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication.+$',
  replace => true,
}
