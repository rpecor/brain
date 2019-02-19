FROM python:3
WORKDIR /mnt
RUN useradd -G news,ssh rpecor
RUN useradd -G news,mail,proxy testuser
