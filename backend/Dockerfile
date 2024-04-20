FROM python:3.11

WORKDIR /app
COPY . .

# install python dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# run entrypoint script
RUN chmod 777 ./entrypoint.sh
ENTRYPOINT ./entrypoint.sh
