# Use an NVIDIA CUDA base image
FROM nvidia/cuda:11.2.2-base-ubuntu20.04

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    python3.10 \
    python3.10-venv \
    python3.10-dev \
    python3.10-distutils \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create and activate a virtual environment
RUN python3.10 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Upgrade pip and install Poetry
RUN pip install --upgrade pip && \
    pip install poetry


# Set the working directory
WORKDIR /app

# Copy the project files into the Docker image
COPY pyproject.toml poetry.lock ./
COPY src ./src
COPY data ./data

# Install project dependencies using Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

# Expose the Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "src/app.py"]
