FROM postgres:15.13-bookworm
RUN mkdir -p /docker-entrypoint-initdb.d
RUN echo "CREATE DATABASE db;" > /docker-entrypoint-initdb.d/init.sql