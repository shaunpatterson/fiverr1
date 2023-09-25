#!/bin/bash
# YOU SHOULD RUN THIS
#docker run --name test-postgres -p 5432:5432 -e POSTGRES_USER=admin -e POSTGRES_DB=test -e POSTGRES_PASSWORD=postgres -d postgres

docker build -t test:0 .

SQLALCHEMY_DATABASE_URI=postgresql://admin:postgres@host.docker.internal:5432/test

#
# SQLALCHEMY_DATABASE_URI needs to be built from the Terraform output
#
docker run -e SQLALCHEMY_DATABASE_URI=$SQLALCHEMY_DATABASE_URI -p 8080:8080 --add-host host.docker.internal:host-gateway test:0


# then run
# curl localhost:8080/api/test
# or point your browser to that URL


