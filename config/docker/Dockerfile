FROM django

WORKDIR /v-vault


ADD ./requirements/base.txt /v-vault/requirements/base.txt
RUN apt-get update && apt-get install -y git

RUN pip install -r ./requirements/base.txt

ADD . /v-vault

EXPOSE 80

COPY ./config/docker/docker-entrypoint.sh /
ENTRYPOINT ["./config/docker/docker-entrypoint.sh"]