# A myweb Flet app

An example of a minimal Flet app.

To run the app:

$ docker build -t app-web-login .
$ docker run -it --rm --name app-web-login app-web-login
$ docker run -d --restart=always -p 8080 --name app-web-login --hostname app-web-login app-web-login

```
flet run [app_directory]
```