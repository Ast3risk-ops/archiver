# A dockerfile must always start by importing the base image.
# We use the keyword 'FROM' to do that.
# In our example, we want import the python image.
# So we write 'python' for the image name and 'latest' for the version.
FROM docker.io/python:latest
LABEL org.opencontainers.image.description Latest image for the Archiver bot built on every commit. See https://archiver.asterisk.lol/selfhost/docker for a setup guide.


# In order to launch our python code, we must import it into our image.
# We use the keyword 'COPY' to do that.
# The first parameter 'main.py' is the name of the file on the host.
# The second parameter '/' is the path where to put the file on the image.
# Here we put the file at the image root folder.
COPY main.py /
COPY main_emoji.py /
COPY requirements.txt /
COPY context.png /
COPY start.sh /
RUN chmod +x start.sh
RUN pip install --no-cache-dir -r requirements.txt

# We need to define the command to launch when we are going to run the image.
# We use the keyword 'CMD' to do that.
# The following command will execute "python ./main.py".
RUN adduser archiver
USER archiver
CMD [ "bash", "./start.sh --private" ]
