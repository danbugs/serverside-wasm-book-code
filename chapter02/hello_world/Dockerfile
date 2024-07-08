FROM rust:latest as builder

RUN USER=root cargo new --bin hello_world_host
WORKDIR /hello_world_host

# copy the Cargo.toml to get the dependencies
COPY hello_world_host/Cargo.toml Cargo.toml

# run build to cache deps
RUN cargo build --release
RUN rm src/*.rs

# copy source code
COPY hello_world_host/src src

# build your application
RUN rm target/release/deps/hello_world_host*
RUN cargo build --release

FROM debian:bookworm-slim
COPY --from=builder /hello_world_host/target/release/hello_world_host hello_world_host

ENTRYPOINT ["./hello_world_host"]
