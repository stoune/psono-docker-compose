# All in one docker-compose for psono password manager self-hosting

## Prerequisites:

1. docker
2. docker-compose
3. Python 3

## Setup:

Only first time, (warning it will clean all existing data):

```
python3 ./setup_and_run.py --regenerate-keys --clean-data
```

## Run

Next times without cleaning data:

```
python3 ./setup_and_run.py 
```

To see all possible command-line options run:
```
python3 ./setup_and_run.py --help
```

If everything prepared you may use docker compose directly
```
# Up the compose in the background
docker compose -f docker-compose.yml up -d
# down the compose and clean data
docker compose -f docker-compose.yml down -v
```

## Usefull code sniplets commands         

To review django settings. Login into psono-combo container and modify /root/psono/settings.py 

```
def print_settings():
    from  pprint import pp
    print("---------------------------------")
    for s in dir(settings):
        pp(f"{s} : {getattr(settings, s)}")
    print("--------------------------------")

print_settings()

```

### show users on database

`docker exec -it psono-db psql -U psono -d psono -c "\du"`

### show databases

```bash
# list databases
docker exec -it psono-db  psql -U psono -c "\l"
docker exec -it psono-db printenv
docker exec -it psono-combo printenv
docker exec -it psono-backend bash
```
\l to display all the schema

\dt to display all tables.

Run - \c schema_name to connect to db

```bash
docker exec -it psono-db 'PGPASSWORD="<DB_PASSWORD>" psql -U psono -d psono -c "\du"'
```


