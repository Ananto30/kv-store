FROM node:19.1.0-alpine as build

WORKDIR /
COPY web-app/package.json web-app/package.json
COPY web-app/package-lock.json web-app/package-lock.json

WORKDIR /web-app
RUN npm ci --silent
COPY web-app/src src
COPY web-app/rollup.config.js rollup.config.js
COPY web-app/public public
RUN npm run build


FROM python:3.11.0-alpine

WORKDIR /

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

COPY --from=build /web-app/public /web-app/public

COPY ./src /src
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
