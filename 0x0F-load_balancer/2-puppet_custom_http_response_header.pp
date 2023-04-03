# A script that automates the task of creating a custom HTTP header responsewith Puppet

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \"\$HOSTNAME\";/" /etc/nginx/sites-available/default ; sudo service nginx start',
}
