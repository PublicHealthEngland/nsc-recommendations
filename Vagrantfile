# Vagrant configuration for National Screening Centre
#
# Usage:
#   sudo apt-get install vagrant virtualbox
# 	vagrant up --provision
#   vagrant ssh-config > ssh-config
#   vagrant ssh
#   vagrant halt

APPLICATION_NAME = "nsc"

VM_NAME = "#{APPLICATION_NAME}".upcase

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/bionic64"

  config.vm.define "#{APPLICATION_NAME}.local", primary: true do |app|
    app.vm.hostname = "#{APPLICATION_NAME}"
    config.vm.network :private_network, ip: "192.168.10.10"
  end

  config.vm.provider "virtualbox" do |vb|
     vb.customize ["modifyvm", :id, "--name", "#{VM_NAME}", "--memory", "4096"]
  end

  # Uncomment if you want to share with vagrant
  # config.vm.synced_folder ".", "/home/vagrant/nsc"

  config.vm.provision "shell", :privileged => false, inline: <<-SHELL

    sudo apt-get update
    sudo apt-get --yes install python-setuptools python-pip

  SHELL

end
