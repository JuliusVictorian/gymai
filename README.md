# gymai
# ubuntu 16.04 and up
# docker needed
sudo apt-get update

sudo apt-get install python-pip

pip install numpy

sudo apt-get install golang libjpeg-turbo8-dev make

sudo apt-get install cmake

sudo pip install universe

# If you get errors

sudo apt-get install libx11-dev libxcursor-dev libxrandr-dev libxinerama-dev libxi-dev \
libxxf86vm-dev libgl1-mesa-dev mesa-common-dev

sudo apt-get install -y python-dev make golang libjpeg-turbo8-dev

git clone https://github.com/openai/go-vncdriver.git

cd go-vncdriver

python build.py

pip install -e .

cd ..

python random.py
