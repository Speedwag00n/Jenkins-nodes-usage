# Build

## Installing Docker and Jenkins

1. Install docker on each node.
2. Enable autoloading and start docker:
	* systemctl enable docker
	* systemctl startdocker
3. Install JDK on a master node:
	* apt: apt-get install default-jdk
4. Install Jenkins on the master node:
	- apt: apt-get install jenkins
5. Add 'swarm-manager' label for the master node. 
6. Add jenkins user to a docker group on the master node:
	* usermod -aG docker jenkins

## Docker Swarm configuration

1. Run 'docker swarm init --advertise-addr <master-node-ip>' on the master node.
2. Command from previous step generate command for join worker nodes (docker swarm join --token <token> <master-node-ip>:2377). Run this command on each worker node.
3. (Optional) If you want not to run flask app and database containers on manager node, you can disable it as a worker. Use command 'docker node update --availability drain <manager-name>' (use 'docker node ls to see all existing nodes').

## Build

1. Change nginx.conf file in nginx directory: change server directives in upstream "nodes-usage-app" (they must have ips of all nodes with flask app and port of containers with flask app).
2. Run Nodes-usage-backend-build Jenkins job.

## Update

1. Run Nodes-usage-backend-update Jenkins job.