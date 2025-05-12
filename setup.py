from setuptools import setup, find_packages

setup(
    name="blogging_platform_app",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "python-dotenv",
        "psycopg2"
    ],  
    entry_points={  
        "console_scripts": [
            "blogging-platform=blogging_platform_app.app:app.run" 
        ]
    },
    author="Lewie Jackson",
    author_email="LewieJ08@gmail.com",
    description="A simple web app to allow uses to create, read, update and delete posts",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LewieJ08/blogging_platform_app",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)