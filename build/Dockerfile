FROM nginx:1.23.1-alpine

EXPOSE 80

RUN rm /usr/share/nginx/html/index.html
COPY . /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf