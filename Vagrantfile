# This Vagrantfile brings up an Ubuntu virtual machine.
#   (https://www.vagrantup.com/)
# If the bootstrap fails, you can run 'vagrant provision' to try again.

$bootstrap = <<THIS_IS_A_BASH_SCRIPT
set -e
apt-get update
cd /vagrant/
sudo ./bin/install
THIS_IS_A_BASH_SCRIPT

Vagrant.configure("2") do |config|
  config.vm.provider "virtualbox" do |v|
    v.memory=4096
  end
  config.vm.box = "debian/contrib-jessie64"
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.provision "shell", inline: $bootstrap
end
