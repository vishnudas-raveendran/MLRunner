FROM python:3.6-slim
COPY ./server.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./DiabetesPredModel.pkl /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "server.py"]