import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="piti", 
    version="0.0.1",
    author="author",
    author_email="mail@vhasanov.com",
    description="This is a tool to manage some of the AWS services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vusalhasanli/aws-python",
    packages=['commands'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3+",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['boto3', 'click'],
    entry_points='''
            [console_scripts]
            piti=commands.aws_env:aws_env
    ''',
)