# SGI Api

Hi! This is SGI an API that supports crud for Products, on the near future 
we hope to support more services !

# Documentation
For know the documentation is within the same project so... you'll need to run
it to see it 😞  
The upside of this is that this project is too easy to run with docker! 🐳  
so... run it and go to the swagger http://localhost:8000/docs#

# How To Run Locally

1) you need to place the env ENVIRONMENT=LOCAL  
2) Run your local database at localhost:5432
3) Replace the following files 
   * **sgi/secrets/pg.ini**: represents postgres connection. i.e: DATABASE_URL="postgresql+asyncpg://sgi:password@localhost:5432/sgi"
   * **sgi/alembic.ini**: represents the connection to de DB but for migrations
     * **Note**: the sqlalchemy.url will be ignored, alembic will be automatically 
     connected to localhost:5432 if you want to change this behavior see **How To Run Remotely**
4) run `alembic -c /secrets/alembic.ini upgrade head` : this runs migrations
5) run `poetry run fastapi run src/main.py`  : this runs the project


# How To Run Jenkins

   * ```
     make jenkins
     ```    
   * go to http://localhost:8080


# How To Run With Docker
1) you need to place the env ENVIRONMENT=DEV
2) Replace the following files
   * **sgi/secrets/pg.ini**: represents postgres connection. i.e: DATABASE_URL="postgresql+asyncpg://sgi:password@postgres:5432/sgi"
   * **sgi/alembic.ini**: represents the connection to de DB but for migrations
     * **Note**: the sqlalchemy.url will be ignored, alembic will be automatically 
     connected to 'postgres' container if you want to change this behavior see **How To Run Remotely**
3) Make sure you have Docker installed on you Pc, Then execute the following commands
   * ```
     make build
     ```  
   * ``` 
     make run
     ```

And yes, that's it. 😉👍🏻


# How To Run Tests
1) you need to place the env export ENVIRONMENT=TEST
2) Replace the following files
   * **sgi/secrets/pg.ini**: represents postgres connection
   * **sgi/alembic.ini**: represents the connection to de DB but for migrations
     * **Note**: the sqlalchemy.url will be ignored, alembic will be automatically 
     connected to 'test-postgres' container if you want to change this behavior see **How To Run Remotely**
3) Make sure you have Docker installed on you Pc, Then execute the following commands
   * ```
     make build
     ```  
   * ``` 
     make test
     ```

# How To Run Remotely
1) you need to place the env ENVIRONMENT=ELSE
2) Replace the following files
   * **sgi/secrets/pg.ini**: represents postgres connection
   * **sgi/alembic.ini**: represents the connection to de DB but for migrations
   and set **sqlalchemy.url** variable
3) Make sure you have Docker installed on you machine, Then execute the following commands
   * ```
     make build
     ```  
   * ``` 
     make run
     ```


# CI/CD
based on this course https://github.com/vdespa/install-jenkins-docker  


```
docker build -t my-jenkins .
```
