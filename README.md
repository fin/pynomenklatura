## nomenklatura - Python client

This library provides a Python client for the [nomenklatura API](http://nomenklatura.okfnlabs.org). Nomenklatura de-duplicates and integrates different names for entities - people, organisations or public bodies - to help you clean up messy data and to find links between different datasets. 

### Usage

The Python client library can be used to find, match and create entities in nomenklatura datasets:

    import nomenklatura
    
    dataset = nomenklatura.Dataset("german-politicians")
    entity = dataset.entity_by_name("Angela Merkel")
    print entity

### Installation

The easiest way to install the client is via the Python package index and pip/easy_install:

    pip install -e git+https://github.com/pudo/pynomenklatura.git#egg=pynomenklatura

If you want to develop the client library's code, check out the [repository](http://github.com/pudo/pynomenklatura) and set up dependencies etc. with the command:

    python setup.py develop

``pynomenklautura`` depends on [requests](http://requests.readthedocs.org/en/latest/) newer than 1.2.

### Configuration 

Several aspects of ``pynomenklatura`` can be configured, including the host name of the nomenklatura server and the API key that is to be used for authentication. To determine these settings, the library will evaluate the following configuration sources in the listed order:

1. Read the ``~/.nomenklatura.ini`` file in the user's home directory. The file is a simple .ini configuration as detailed below.
2. Check the contents of the following environment variables: ``NOMENKLATURA_HOST``, ``NOMENKLATURA_APIKEY``.
3. Evaluate the keyword arguments passed into the constructor of ``nomenklatura.Dataset``.

A simple configuration file for ``pynomenklatura`` might look like this:

	[client]
	host = http://opennames.org
	api_key = xxxxx-xxxxx-xxxxx (see user profile in nomenklatura)

### Limitations

Due mainly to the laziness of the author, this library does not implement the full API of the nomenklatura web service. Some unsupported functions include:

* Dataset creation and editing.
* Import and mapping of CSV files. 

### License

Copyright (c) 2013, Friedrich Lindenberg, Michael Bauer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

