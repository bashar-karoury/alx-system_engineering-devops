# Install flask package with version of 2.1.0 from pip3

package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}

