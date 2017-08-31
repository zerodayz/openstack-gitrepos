# openstack-gitrepos
Generates all OpenStack repositories

```
./generate-repos.py

for p in $(cat gitrepos); \
  do git clone $p; done
```
