#base image for this project

From python:3.10-slim

#Define the working dir

WORKDIR	/app

#copy code from local to container

Copy . /app


# requiremnt for flash app

run pip install flask


#Define the post 

Expose 2000

# run the container

CMD ["python", "app.py"]
