/* Базу создавать так*/
CREATE USER gdx2map WITH ENCRYPTED PASSWORD 'gdx2mappwd';
CREATE DATABASE gdx2map WITH OWNER gdx2map;
GRANT ALL PRIVILEGES ON DATABASE gdx2map TO gdx2map;

/* коннектимся как пользователь gdx2map*/
\c gdx2map;
ALTER ROLE gdx2map SET client_encoding TO 'utf8';
CREATE SCHEMA IF NOT EXISTS gdx2map AUTHORIZATION gdx2map;
GRANT ALL ON SCHEMA gdx2map TO gdx2map;
SET search_path to gdx2map;

CREATE EXTENSION hstore;
CREATE EXTENSION postgis;
