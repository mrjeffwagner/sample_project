import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()        

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='wagner',
    url='https://github.com/mrjeffwagner/sample_project',
    project_urls = {
        "Google": "http://www.google.com"
    },
    author='Jeff Wagner',
    author_email='mr.jeff.wagner@gmail.com',
    # Needed to actually package something
    packages=['wagner'],
    # Needed for dependencies
    install_requires=['datetime'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='A sample python project that creates a log message with timestamp.',
    # We will also need a readme eventually (there will be a warning)
    long_description=long_description,
    long_description_content_type="text/markdown",
)
