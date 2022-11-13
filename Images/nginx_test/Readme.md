# Run nginx-test with following command

```console
# change the path on your machine to run this command
# for explanation read Readme.md in root
docker run -p 80:80 -m=40m --restart unless-stopped -ti -d -v /home/user/Documents/coding/Learning_Docker/Images/nginx_test:/usr/share/nginx/html nginx
```