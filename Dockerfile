FROM django
ADD . /v-serviceVault

WORKDIR /v-serviceVault

RUN pip install -r ./v-serviceVault/requirements/base.txt



