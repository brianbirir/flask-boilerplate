FROM python:3.7.3-stretch
ENV PYTHONUNBUFFERED 1

WORKDIR /api_service

COPY . /api_service

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY start_server.sh /start_server.sh

RUN chmod +x /start_server.sh

ENTRYPOINT ["/start_server.sh"]

# RUN ["chmod", "+x", "start_server.sh"]