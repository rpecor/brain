Quick Start --- To execute the quick start, you must have Docker installed.
1. Clone this repo: git clone https://github.com/rpecor/brain.git

2. Navigate to the brain directory and build the docker image: docker build -t brain-py .

3. From within the cloned directory run: docker run -d -v $(pwd):/mnt brain-py python run.py

An out.json file will be generated in the current directory with the containers user information


If you would like to execute the script on another host run: 'python run.py /testfile/etc/passwd /testlocation/etc/group' with the first argument being the path to the passwd file and second path being the path to the group file.

Have a look around in the container with this command: docker run -it -v $(pwd):/mnt --entrypoint /bin/bash brain-py

Future considerations:

I'd like to add some better argument logic, if just one of the paths are needed or given it would be nice to handle that.

It would probably be worth dynamically generating the file name so its not always overwritten. Then clean up out.json files that are a certain age.
And no reason to run if the passwd and group files haven't changed.