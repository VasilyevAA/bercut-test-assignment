FROM python:3.7-alpine

RUN addgroup -g 82 app \
 && adduser -S -u 82 -g app app \
 && mkdir -p /app \
 && chown -R app:app /app

WORKDIR /app

COPY --chown=app:app requirements.txt  /app/
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

COPY --chown=app:app . /app

USER app
ENTRYPOINT ["/app/run.sh"]
