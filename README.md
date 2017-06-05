# oio-frontend
python tornado frontend for OpenIO SDS

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

Debian/Ubuntu:

```sh
$ echo "deb http://mirror.openio.io/pub/repo/openio/sds/16.10/$(lsb_release -i -s)/ $(lsb_release -c -s)/" | sudo tee /etc/apt/sources.list.d/openio-sds.list
$ sudo apt-get install curl -y
$ curl http://mirror.openio.io/pub/repo/openio/APT-GPG-KEY-OPENIO-0 | sudo apt-key add -
$ sudo apt-get update; sudo apt-get install openio-sds
```

Centos:

```sh
$ yum -y install http://mirror.openio.io/pub/repo/openio/sds/16.10/el/openio-sds-release-16.10-1.el.noarch.rpm
$ yum -y install openio-sds-server-3.2.3-1.el7.oio.x86_64
```

```sh
git clone [this repo]
```