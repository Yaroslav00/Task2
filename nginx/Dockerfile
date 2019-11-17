from nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY app.conf /etc/nginx/conf.d
RUN mkdir /etc/nginx/html
COPY index.html /etc/nginx/html
RUN ls
EXPOSE 80