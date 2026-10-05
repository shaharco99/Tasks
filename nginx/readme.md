# nginx reverse proxy 
To create the docker image run this command in current directory
```bash
$ docker build -t nginx .
```
after image is created run
```bash
$ docker run -p 8080:80 --rm nginx
```