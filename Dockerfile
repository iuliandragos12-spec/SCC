FROM python:3.11-alpine

ENV FLASK_APP=masini

# utilizator non-root pentru rularea aplicatiei in container
RUN adduser -D masini

USER masini
WORKDIR /home/masini/

COPY --chown=masini:masini app                    app
COPY --chown=masini:masini static                 static
COPY --chown=masini:masini dockerstart.sh         dockerstart.sh
COPY --chown=masini:masini pytest.ini             pytest.ini
COPY --chown=masini:masini quickrequirements.txt  quickrequirements.txt
COPY --chown=masini:masini masini.py              masini.py

# venv local + dependinte
RUN python3 -m venv .venv
RUN .venv/bin/pip install --no-cache-dir --upgrade pip
RUN .venv/bin/pip install --no-cache-dir -r quickrequirements.txt

EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
