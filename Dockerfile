# Use a newer base image (Bullseye is more stable than Buster currently)
FROM python:3.10-slim-bullseye

WORKDIR /app

# 1. Install System Deps
# Combined into one block to reduce layers.
# using apt-get ensures exit code 100 doesn't happen due to interactive prompts.
RUN apt-get update && apt-get install -y --no-install-recommends \
    awscli \
    && rm -rf /var/lib/apt/lists/*

# 2. Install Python Deps
# We copy ONLY the requirements file first.
# This creates a cached layer. If requirements.txt doesn't change,
# Docker skips this step instantly on future builds.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy Source Code
# This is now the last step. Changing your code only rebuilds this layer.
COPY . .

CMD ["python3", "app.py"]