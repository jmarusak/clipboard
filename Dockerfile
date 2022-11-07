# syntax=docker/dockerfile:1

FROM golang:1.19-alpine

WORKDIR /app

COPY go.mod ./

COPY *.go ./
COPY *.html ./

RUN go build -o ./clipboard

EXPOSE 8080

CMD [ "./clipboard" ]
