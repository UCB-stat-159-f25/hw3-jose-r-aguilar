ENV_NAME ?= stat259
ENV_FILE ?= environment.yml
CONDA_BASE := $(shell conda info --base)

.ONESHELL:
SHELL := /bin/bash

.PHONY: env html clean

env:
	@source $(CONDA_BASE)/etc/profile.d/conda.sh
	if conda env list | awk '{print $$1}' | grep -qx "$(ENV_NAME)"; then
		echo "Updating existing environment: $(ENV_NAME)"
		conda env update -n $(ENV_NAME) -f $(ENV_FILE) --prune
	else
		echo "Creating new environment: $(ENV_NAME)"
		conda env create -n $(ENV_NAME) -f $(ENV_FILE)
	fi

html:
	myst build --html

clean:
	rm -rf figures/* audio/* _build