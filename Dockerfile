FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app

EXPOSE 8000

ADD . .

RUN uv sync --locked

CMD ["uv", "run", "fastapi", "run"]