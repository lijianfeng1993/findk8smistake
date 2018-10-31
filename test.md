Using `GET_HOSTS_FROM=dns` requires your cluster to provide a dns service. As of Kubernetes 1.3, DNS is a built-in service launched automatically. However, if the cluster you are using
does not have a built-in DNS service, you can instead instead access an environment variable to find the master
service's host. To do so, comment out out the 'value: dns' line above, and uncomment the line below:
value: env
//hellowork is is workd
jdiaj 
//fjohiotjfoirehrid 
