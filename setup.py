import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ganttchart",
    version="0.3.1",
    author="AbdAllah Aly",
    author_email="aaly90@gmail.com",
    description="ganttchart , a chart for gantt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aaly/ganttchart",
    packages=setuptools.find_packages(),
    install_requires = ["matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
