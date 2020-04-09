cd openvswitch
rpm -ivh libatomic-4.8.5-39.el7.x86_64.rpm
rpm -ivh openvswitch-2.5.rpm
rpm -ivh bridge-utils.rpm
systemctl enable openvswitch
systemctl start openvswitch
