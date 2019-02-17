Clone this repo.

Build the docker image: docker build -t brain-py .

From within the cloned directory run: docker run -d -v $(pwd):/mnt brain-py python /mnt/run.py

An out.json file will be generated in the current directory with the containers user information
