# Python Dapr Workflow - employee_onboarding_workflow
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/root/.cargo/bin:${PATH}"

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        git \
        make \
        gcc \
        g++ \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install uv - a faster Python package installer and resolver
RUN curl -sSf https://astral.sh/uv/install.sh | sh && \
    # Verify installation
    uv --version

# Create and use non-root user for better security
RUN groupadd -r workflow && useradd -r -g workflow -d /home/workflow -m workflow
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt

# Copy application code
COPY . .

# Change ownership of the application code
RUN chown -R workflow:workflow /app

# Switch to non-root user
USER workflow

# Define the entry point
CMD ["python3", "src/app.py"]