# animal_crossing_helper
Maintainer: geltz.andrew@gmail.com

## How to run
As a container:
1. Edit the docker-compose.yml to specify the correct filepath and networking port
2. At the filepath you are going to mount, create a file called django_secret.txt and enter a secret for the django app to run with (if you need a new secret try `python -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))'` )
3. Run `docker-compose up -d` in the directory with the docker-compose.yml file to start the container

## How to load data
If running outside of the container, skip to step 3
1. Start the container
2. Get a shell in the container
3. Ensure you are in the directory with manage.py
4. Execute `python manage.py shell` to get a django shell
5. Execute `exec(open('import_data.py').read())` to run the import script