test_install:
	@pip install -r requirements_test.txt

test: test_install
	@pytest --cov-report term-missing --cov=deprecated tests/

upload:
	@python setup.py sdist bdist_wheel upload
