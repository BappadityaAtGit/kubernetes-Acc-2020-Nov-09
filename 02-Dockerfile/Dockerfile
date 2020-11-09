# Base OS Images
FROM ubuntu:16.04

# Update Apt Repo. 
RUN apt-get update

# Install Apache Packages 
RUN apt-get install apache2 -y 

# Custom Web Page ( Welcome.html ) 
COPY hello.html /var/www/html/welcome.html 

# Exposing WebServer
EXPOSE 80 
EXPOSE 3306 

# Service Start
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"] 
