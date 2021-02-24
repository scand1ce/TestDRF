CREATE DATABASE drftask;
CREATE USER scand WITH PASSWORD 'postgres';
ALTER ROLE scand SET client_encoding TO 'utf8';
ALTER ROLE scand SET default_transaction_isolation TO 'read committed';
ALTER ROLE scand SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE drftask TO scand;
