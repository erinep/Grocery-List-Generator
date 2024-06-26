FROM python:3.9 AS env

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./recipeprinter recipeprinter/

# Make port 5000 available to the world outside this container
# EXPOSE 5000

# Define environment variables
ENV FLASK_APP recipeprinter:app

# Run the flask app within docker. 
# host=0.0.0.0 is required to share with localhost
# CMD ["python", "-m", "flask", "--debug",  "run", "--host=0.0.0.0"]
CMD ["waitress-serve", "--port=5000", "recipeprinter:app"]]