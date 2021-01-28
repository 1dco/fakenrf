FROM node:10-alpine

RUN npm install -g json-server

EXPOSE 8080
COPY db.json /db.json
COPY routes.json /routes.json
ADD run.sh /run.sh

ENTRYPOINT ["sh", "/run.sh"]

CMD []
