# file make changes to our configuration file (Using Puppet)

include stdlib
file_line { 'specify Identity File':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
