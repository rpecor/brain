Clone this repo.

Build the docker image: docker build -t brain-py .

From within the cloned directory run: docker run -d -v $(pwd):/mnt brain-py python /mnt/run.py

An out.json file will be generated in the current directory with the containers user information

Have a look around in the container with this command: docker run -it -v $(pwd):/mnt --entrypoint /bin/bash brain-py


Future considerations:

I'd like to add some better argument logic, if just one of the paths are needed or given it would be nice to handle that.

It would probably be worth dynamically generating the file name so its not always overwritten. Then clean up out.json files that are 30 days old.
And no reason to run if the passwd and group files haven't changed.