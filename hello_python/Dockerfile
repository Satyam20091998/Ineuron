FROM python:3-alpine
WORKDIR /service
COPY requirement.txt .
RUN pip install -r requirement.txt
COPY . ./
EXPOSE 8082
ENTRYPOINT [ "python3", "app.py" ]