test_install:
	@pip install -r requirements_test.txt

test: test_install
	@py.test --cov-report term-missing --cov=deprecated

upload:
	@python setup.py sdist bdist_wheel upload