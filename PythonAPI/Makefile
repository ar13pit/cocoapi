all:
    # install pycocotools locally
	python setup.py build_ext --inplace
	rm -rf build

install:
	# install pycocotools to the Python site-packages
	python setup.py build_ext install
	rm -rf build

pip2:
	# Local install with pip2
	cp -r ../common .
	pip2 install --user .
	rm -rf common

pip3:
	# Local install with pip2
	cp -r ../common .
	pip3 install --user .
	rm -rf common
