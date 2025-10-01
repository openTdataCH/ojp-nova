# Development guidelines for project

# Releases
* Releases are done as tag and zip with the github mechanisms.
* They need to be thoroughly tested
* We use semantic versioning
* 
# Branches
* master is the main branch
* At same point we will create a next branch (we currently have a PR for the next version with its branch)
* Currently we don't have releases branches
* Branch protection on master will be activated at some point (when we have more than one developer)


# Coding
* The code should be clean and documented. Especially algorithm specialities should be explained.
* #TODO marks points for improvement
* mypy is done in the code: https://mypy-lang.org/
* black is used in the code: https://github.com/psf/black
* ruff is used in the code: https://docs.astral.sh/ruff/

# Testing
* Currently tests are mainly done with test_network_flow.py and activated input files (are referenced in configuration.py)

# Secrets
Secrets should be stored in local_configuration.py 


