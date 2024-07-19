# grpclib-bug

A repository demonstating an issue with grpclib interacting with tonic using IPv6.

## Steps to reproduce

1. Clone this repository
2. `cd grpclib-bug`
3. Install `rustup` (`sudo apt install rustup`)
4. `cd helloworld-tonic`
5. `cargo run --bin helloworld-server &`
6. `cd ../client`
7. `python -m venv venv`
8. `. venv/bin/activate`
9. `python -m pip install "betterproto[compiler]==2.0.0b6" grpcio-tools grpcio protobuf`
10. `python grpclib_client.py`

* Running `python grpcio_client.py` works.
* Running using IPv4 (listenting and connecting to 127.0.0.1) works.


## Rebuilding the generated code

* `python -m grpc_tools.protoc -I .. --python_out=. --grpc_python_out=. ../helloworld.proto` `
* `python -m pip install "betterproto[compiler]==2.0.0b6" grpcio-tools grpcio protobuf`

## Network captures

Network captures with working and failing cases are avaiable in the `cap/` directory.
