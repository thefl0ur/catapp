## CatFact

Simple FastAPI app to display image and fact about cats.

## Build

Project uses [uv](https://docs.astral.sh/uv/) for managing and is targeting Python 3.13.

Sync used python packages with 

```bash
uv sync --locked
```

### Docker image

```bash
docker build -t azska/catapp .
```

Prebuild image can be found [here](https://hub.docker.com/r/azska/catapp)

## Running app

### Local run

To run project execute next command

```
uv run fastapi <mode>
```

Replace `<mode>` with one of the following options:
* dev
* run

Application accepts connections on port `8000`


### Running docker image

```bash
docker run -d -p 8000:8000 azska/catapp
```
To view application go to [127.0.0.1:8000](http://127.0.0.1:8000)