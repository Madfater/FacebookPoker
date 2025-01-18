FROM python:3.12.8-bullseye AS builder

RUN pip install patchright

RUN patchright install chromium

RUN patchright install-deps

FROM python:3.12.8-bullseye

COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12

COPY --from=builder /root/.cache /root/.cache

COPY --from=builder /usr/lib /usr/lib

RUN apt-get update

RUN apt-get install -y libdbus-1-3

COPY /FacebookPoker.py .

CMD ["python3", "-u", "FacebookPoker.py"]