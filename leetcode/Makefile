TYPECHECK=mypy
LINT=pylint -d redefined-outer-name,no-self-use,missing-docstring,too-many-arguments,too-few-public-methods,fixme,too-many-locals,too-many-public-methods,too-many-instance-attributes,R0801,c-extension-no-member
LINT2=pycodestyle
PACKAGES=*.py
LOG_DIR=tmp

lint_all: lint lint2

typecheck:
	$(TYPECHECK) $(PACKAGES)

lint:
	$(LINT) $(PACKAGES)

lint2:
	$(LINT2) $(PACKAGES)

clean:
	rm -rf tmp/*  __pycache__ *.pyc */__pycache__ */*.pyc .mypy_cache .pytest_cache .pytype

todo:
	leetcode list  | grep ✘

