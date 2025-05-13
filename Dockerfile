#base image for this project

From python:3.10-slim

#Define the working dir

WORKDIR	/app

#copy code from local to container

Copy app.py /app


# requiremnt for flash app

run pip install flash


#Define the post 

Expose 5000

# run the container

CMD ["python", "app.py"]
