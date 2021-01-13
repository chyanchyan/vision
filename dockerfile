FROM python:3.7-slim as production

ENV PTYHONUNBUFFERED = 1
WORKDIR /app/

RUN  sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN  sed -i s@/deb.debian.org/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN  apt-get clean

RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essential \
    gcc \
    libffi-dev \
    openssl \
    postgresql \
    libpq-dev

COPY requirements/prod.txt ./requirements/prod.txt

RUN pip install -r ./requirements/prod.txt -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

COPY manage.py ./manage.py
COPY setup.cfg ./setup.cfg

COPY vision_site ./vision_site

EXPOSE 8000

FROM production as development

COPY requirements/dev.txt ./requirements/dev.txt

RUN pip install -r ./requirements/dev.txt -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

COPY . .