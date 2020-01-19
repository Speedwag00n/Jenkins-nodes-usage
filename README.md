##General

1. Install JDK on each node:
	* apt: apt-get install default-jdk
2. Install Jenkins on master node:
	- apt: apt-get install jenkins
3. Configure slave nodes. Add following labels: 
	* nodes-usage-database (for node with database)
	* nodes-usage-node1 and nodes-usage-node2 (for nodes with flask app)
	* nodes-usage-nginx (for node with nginx)
4. Install Docker on each node:
	* apt: apt-get install docker.io
5. Enable autoloading and start docker:
	* systemctl enable docker
	* systemctl startdocker
6. Create jenkins user on slave nodes:
	* adduser jenkins -d /var/jenkins_home
7. Add jenkins user to a docker group on each node:
	* usermod -aG docker jenkins

##Backend

1. Change nginx.conf file in nginx directory: change server directives in upstream "nodes-usage-app" (they must have ips and ports of nodes with flask app).
2. Run build-backend Jenkins job. Be attentive with databaseAddress param. It must be ip of node with database.

##Frontend

1. Configure api url.
2. Run build-frontend Jenkins job.