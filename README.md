# Django api gateway

- MVT (Model View Template)
- Model dengan version migrate

- command

```sh
# run docker-compose to connect with database
docker-compose up -d

# command
python3 manage.py help
python3 manage.py runserver

# wajib dijalankan pas awal aplikasin jalan
python3 manage.py migrate
python3 manage.py createsuperuser

# add or create app
python3 manage.py startapp

# apple M1 Chip
arch -x86_64 brew install mysql
arch -x86_64 brew install mysql-client


pip3 install mysqlclient
```

- auth

  - static token
  - jwt [simple-jwt]

- error
  - message
    - NameError: name '\_mysql' is not defined
  - soution
    - on setting.py, add the following 2 line of code
      ```py
      import pymysql
      pymysql.install_as_MySQLdb()
      ```
- documentation
  - django-swagger
