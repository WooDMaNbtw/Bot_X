FROM python:3.11

ENV PATH="/scripts:${PATH}"

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y gcc libc-dev
RUN pip install -r requirements.txt

RUN apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /botX
COPY Bot_X_API /botX
WORKDIR /botX
COPY scripts /scripts

RUN chmod +x /scripts/*

CMD ["entrypoint.sh"]
