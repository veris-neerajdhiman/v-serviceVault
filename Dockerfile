FROM django
ADD . /v-vault

WORKDIR /v-vault

RUN apt-get update && apt-get install -y git
RUN pip install -r ./requirements/base.txt
