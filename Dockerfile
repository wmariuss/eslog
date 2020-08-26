FROM python:3.5
LABEL maintainer "Marius Stanca <me@marius.xyz>"


# Set locale
RUN echo "LC_ALL=en_US.UTF-8" > /etc/default/locale && \
    echo "LANG=en_US.UTF-8" >> /etc/default/locale

# Add executable
ADD dist/eslog.pex /bin/eslog

ENTRYPOINT ["/bin/eslog"]
