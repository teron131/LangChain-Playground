from setuptools import find_packages, setup

setup(
    name="langchain-playground",
    version="0.1.0",
    author="Teron",
    author_email="teron131@gmail.com",
    description="LangChain Playground for my personal use.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/teron131/langchain-playground",
    packages=find_packages(
        exclude=[
            "*.tests",
            "*.tests.*",
            "tests.*",
            "tests",
            "*.ipynb",
            "*.__pycache__",
            "*.cache",
            "images",
            "audio",
            "pdfs",
            "databases",
            "standalone-GUI",
        ]
    ),
    package_data={
        "": [
            "!*.log",
            "!*.png",
            "!*.jpg",
            "!*.pdf",
            "!*.json",
            "!*.ipynb",
            "!.env",
            "!.cache",
        ],
    },
    install_requires=[
        # Core LangChain dependencies
        "langchain",
        "langchain-community",
        "langchain-openai",
        "langchain-together",
        # UI and Interface
        "gradio",
        # YouTubeLoader dependencies
        "fal-client",
        "ipython",
        "more-itertools",
        "numpy",
        "openai-whisper",
        "opencc-python-reimplemented",
        "optimum",
        "pytubefix",
        "python-dotenv",
        "tiktoken",
        "torch",
        "transformers",
        "tqdm",
    ],
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
