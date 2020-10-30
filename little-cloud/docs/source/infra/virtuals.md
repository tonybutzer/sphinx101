# Virtual Machines

## Installing NFS

**nuc**
[Configure NFS Server. ](https://www.server-world.info/en/note?os=Ubuntu_15.04&p=nfs&f=1)

```
sudo apt install nfs-common


```

## ODC

- used for odc-lcmap testing local

## ELASTIC

* purpose is to support the elastic search

### installing elastic search

[elasticsearch downloads](https://www.elastic.co/downloads)


```bash
In config/elasticsearch.yml put

network.host: 0.0.0.0
```



- create the vm - clone ubuntu ?

```bash

tony@bashful:~$ virsh list --all
 Id    Name                           State
----------------------------------------------------
 1     clojure1                       running
 2     odc                            running
 -     ubuntu16.04-gold               shut off


[link]()
tom ~ $ virsh list --all
 Id    Name                           State
----------------------------------------------------
 1     bastion                        running
 2     ns                             running
 3     pizza                          running

```

- clone ubuntu as elastic with virt-manager


### Java Install

this will be in pkg/install_JAVA.sh


### Elastic Search Install

### ElasticSearch Listening 



```bash
In config/elasticsearch.yml put

network.host: 0.0.0.0
```





