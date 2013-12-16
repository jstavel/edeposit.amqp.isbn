Introduction
============

This package provides an AMQP middleware for checking ISBNs.

You can read [full documentation](http://edeposit-amqp-isbn.readthedocs.org/cs/latest/ "Full Documentation")


Acceptance tests
-----------------

They are written using Robot Framework.

All tests are stored at src/tests directory.

You can run them manually

    jan@jan-XPS-L421X:~/work/edeposit.amqp.isbn$ pybot --pythonpath src/edeposit/amqp/isbn/tests/ src/edeposit/amqp/isbn/tests/


... or continuously running using nosier:

    jan@jan-XPS-L421X:~/work/edeposit.amqp.isbn$ nosier -p src "pybot --pythonpath src/edeposit/amqp/isbn/tests/ src/edeposit/amqp/isbn/tests/"
