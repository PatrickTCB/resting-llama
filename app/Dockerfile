FROM python:3

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN mkdir /app
RUN mkdir /app/lib
RUN apt-get clean && apt-get update && apt-get install -y locales
RUN locale-gen en_US.UTF-8
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
ENV LC_ALL="en_US.UTF-8"
ENV LC_CTYPE="en_US.UTF-8"
RUN dpkg-reconfigure --frontend=noninteractive locales
RUN pip3 install requests
RUN pip3 install "fastapi[standard]"
RUN pip3 install ollama

COPY ./lib/ /app/lib
COPY ./main.py /app

WORKDIR /app

EXPOSE 8000

CMD [ "fastapi", "run", "main.py"]
