FROM python:3.12-alpine3.19

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1

# install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --dev

ENV PATH="/.venv/bin:$PATH"
ENV APP_HOME /app
WORKDIR $APP_HOME
RUN mkdir $APP_HOME/logs

# final set up
COPY ./supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY . ./
EXPOSE 5000
CMD ["/usr/bin/supervisord"]