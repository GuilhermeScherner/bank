FROM python:3.11-slim

WORKDIR /app

# Copy only dependency files first for efficient caching
COPY poetry.lock pyproject.toml ./

# Install dependencies using poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false  # Install directly in system Python
RUN poetry install --no-dev  # Install only production dependencies

# Copy the rest of the project files
COPY . .

# Expose the API port
EXPOSE 5000  # Replace with your desired port if different

# Run the application
CMD ["python", "-m", "bank"]
