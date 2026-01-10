FROM nvidia/cuda:12.8.0-cudnn-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.10 \
    python3.10-distutils \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirement.txt ./

RUN pip install --no-cache-dir\
    --default-timeout=1000 \
    --retries 10 \
    -r requirement.txt

COPY . .

EXPOSE 8000

ENV PYTHONPATH=/app
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
