FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    binutils \
    g++ \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# GDAL related ENV VARS - REMOVED
# ENV GDAL_VERSION=3.6.2
# ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
# ENV C_INCLUDE_PATH=/usr/include/gdal

# Install GDAL Python bindings - REMOVED
# RUN pip install --no-cache-dir GDAL==${GDAL_VERSION}

RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
# Ensure GDAL is not installed again from requirements.txt - REMOVED (no longer necessary)
# RUN sed -i '/^GDAL==/d' requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /app/entrypoint.sh

RUN echo "Execute the entrypoint.sh script"

ENTRYPOINT ["bash", "/app/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8050"]
