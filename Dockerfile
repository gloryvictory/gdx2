FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEVENV=prod \
    GDX2_SERVER_HOST=0.0.0.0 \
    GDX2_SERVER_PORT=8001 \
    GDX2_SCHEMA=gdx2 \
    FOLDER_BASE=/opt/gdx2/ \
    FOLDER_REPORT=/opt/gdx2/upload

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /opt/gdx2/log /opt/gdx2/upload /opt/gdx2/geojson /opt/gdx2/data

EXPOSE 8001

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8001"]
