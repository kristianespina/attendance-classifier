FROM python:3.9

# Set timezone
ENV TZ=Asia/Manila
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ADD . /app/
WORKDIR /app/
RUN pip install -r requirements.txt

CMD ["echo", "hello"]