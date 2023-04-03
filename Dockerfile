FROM node:19.3.0-alpine as build

WORKDIR /
COPY web/package.json web/package.json
COPY web/package-lock.json web/package-lock.json

WORKDIR /web
RUN npm ci --silent
COPY web/ .
RUN npm run build


FROM python:3.11.1-alpine

WORKDIR /

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

COPY --from=build /web/build /web/build

COPY ./src /src
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
