from setuptools import setup

setup(
    name="examplePackage",
    version="1.0",
    description="This is my first example distributable package",
    author="Ruben Arrebola",
    author_email="ruben.arre6@gmail.com",
    url="https://www.example.com",
    scripts=[],
    packages=["Packet", "Packet.Goodbye", "Packet.Hello"]
)