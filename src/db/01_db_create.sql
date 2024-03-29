/* Базу создавать так*/
CREATE USER gdx2 WITH ENCRYPTED PASSWORD 'gdx2pwd';
CREATE DATABASE gdx2 WITH OWNER gdx2;
GRANT ALL PRIVILEGES ON DATABASE gdx2 TO gdx2;

/* коннектимся как пользователь gdx2*/
\c gdx2;
ALTER ROLE gdx2 SET client_encoding TO 'utf8';
CREATE SCHEMA IF NOT EXISTS gdx2 AUTHORIZATION gdx2;
GRANT ALL ON SCHEMA gdx2 TO gdx2;
SET search_path to gdx2;

CREATE EXTENSION hstore;
CREATE EXTENSION postgis;
