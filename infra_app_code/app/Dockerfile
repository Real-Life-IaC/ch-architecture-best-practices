FROM public.ecr.aws/lambda/python:3.11

ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="/root/.local/bin:$PATH"

# Install python poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Copy the dependencies files to the Docker image
COPY pyproject.toml poetry.lock /

# Extract dependencies from poetry.lock and install them with pip
RUN poetry export --format requirements.txt --without-hashes --output requirements.txt && \
    pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}" --no-cache-dir --no-deps

# Copy only the relevant function code to the lambda
COPY lambda ${LAMBDA_TASK_ROOT}/lambda

CMD [ "lambda.main.handler" ]
