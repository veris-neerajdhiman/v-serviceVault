## About

- v-serviceVault is `market-place` for all micro-service, one need to register his micro-service so taht he can use them.
- All micro-service also adde don kong simultaneously so taht platform can use them.
 But we need to move this task in platform itself.

## Prerequisites

#### Environment Variables : 

 - DATABASE_NAME_VAULT
 - DATABASE_USER
 - DATABASE_PASSWORD
 - DATABASE_HOST
 - DATABASE_PORT
 - SECRET_KEY
 - KONG_API_HOST
 - KONG_SERVER


## Installation :

1 ) Clone this repo

2 ) Setup virtual environment
```
cd <path-to-repo>/v-serviceVault/

virtualenv -p /usr/bin/python3 env

```

3 ) Activate Virtual environment
```
source env/bin/activate
```
4 ) Install requirements

- Base Requirements

```
pip install -r requirements/base.txt

```
- Testing Requirements
```
pip install -r requirements/test.txt

```
- Local requirements
```
pip install -r requirements/local.txt

```
- Production requirements

```
pip install -r requirements/production.txt

```
5 ) Prerequisites
- Makes sure above `Prerequisites` we mentioned above must be defined and fulfilled.
- Kong server must be in running state and its access-points must be added in respective `environment variables`

6 ) Run Server 
```
python manage.py runserver
```

## API Reference : 

- API documentation is hosted on [Swagger hub](https://swaggerhub.com/apis/veris-neerajdhiman/Service_Vault/0.1) 
and is public.

## Signals : 

1 ) Add service to kong.
2 ) Remove service from kong.
 
## Tests : 

- Run tests using 
```
make test
```
 
 