FROM python:alpine

ENV APP_DIR /app


ADD . /${APP_DIR}
VOLUME [${APP_DIR}]
WORKDIR ${APP_DIR}
RUN pip install -r requirements.txt


EXPOSE 5000

CMD [ "python", "run.py", "--host=0.0.0.0"]
