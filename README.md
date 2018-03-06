# oio-frontend
python tornado frontend for OpenIO SDS

A web server to access to your OpenIO data: http://ip:port/container/object

You will need an OpenIO cluster up and running, you can try the docker container http://docs.openio.io/docker-image/)

This is a demo, feel free to improve it.

```sh
Usage: oio-front.py [options]

Options:
  -h, --help            show this help message and exit
  -n NAMESPACE, --namespace=NAMESPACE
                        Namespace to use
  -u URL, --url=URL     OIO-Proxy IP:PORT
  -a ACCOUNT, --account=ACCOUNT
                        Account to use
  -p PORT, --port=PORT  OpenIO front port
```

Setup
---

```sh
pip install tornado
```

Install OpenIO SDS SDK

Debian/Ubuntu:

Follow the doc until the "puppet manifest" section  
http://docs.openio.io/17.04/install-guide-ubuntu/installation.html

Then run:
```sh
apt-get install -y openio-sds-server
```

Centos:

Follow the doc until the "puppet manifest" section  
http://docs.openio.io/17.04/install-guide-centos/installation.html

Then run:
```sh
yum install -y openio-sds-server
```

```sh
git clone [this repo]
```

Then run it!  
e.g.
```sh
python oio-front.py -n OPENIO -a video_account -u 192.168.1.174:6006 -p 8282
```
