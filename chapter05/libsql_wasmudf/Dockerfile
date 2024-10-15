FROM rust:slim-bullseye

# Install necessary system dependencies
RUN apt-get update && \
    apt-get install -y \
        git \
        tcl8.6-dev \
        build-essential \
        autoconf \
        libtool \
        pkg-config \
        wget \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /home/libsql

# Clone the libsql repository
RUN git clone https://github.com/danbugs/libsql.git .

# Configure and build the project
RUN ./configure --enable-wasm-runtime --enable-releasemode --enable-all && \
    make

# Set the entrypoint to the built binary
ENTRYPOINT ["./libsql"]
