#####################
IS 210 Assignment #02
#####################
******************
Synthesizing Tasks
******************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Lesson: 02
:Points: 18
:Due-Date: YYYY-MM-DDTHH:mm:ss

Overview
========

The synthesizing tasks in this lesson will challenge you to use some of our
advanced tools like reStructuredText nd our various testing tools. From this point forward, unless otherwise directed, please add and commit all 

Instructions
============

The following tasks will either have you interacting with existing files in
the assignment repository or creating new ones on the fly. Don't forget to add
your interpreter directive, utf-8 encoding, and a short docstring with any new
files that you create!

.. important::

    In these exercises, you may, on occasion, come across a task that requres
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the offical Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the language in practice and the search skills
    necessary to become functional programmers.

Synthesizing Tasks
==================

Task 01
-------

The first synthesizing task this week will have you create a reStructuredText
file capable of producing a duplicate of the included reference file. This
will challenge you to get comfortable with some of the reStructuredText syntax
and *directives*.

Specifications
^^^^^^^^^^^^^^

1.  Open the included reference file, ``reference\task_01.html`` in Firefox.

2.  Create a new reStructuredText file called ``task_01.rst`` with a text
    editor like Idle.

3.  Add the correct reStructuredText to ``task_01.rst`` to replicate the
    content and structure of your reference file.

4.  As you complete sections and wish to test your output, use ``rst2html`` to
    output an html file.

    .. code:: console

        $ rst2html task_01.rst task_01.html

5.  Open ``task_01.html`` and compare it against ``reference\task_01.html``

6.  Once ``task_01.rst`` and ``task_01.html`` are complete, add both files
    to the repository and commit your changes.

.. note::

    This task does not use automated testing.

Task 02
-------

For the next task, you'll need to add a docstring to a python file that
happens to be missing this all-important element.

Specifications
^^^^^^^^^^^^^^

1.  Open ``task_02.py`` and add a docstring in the appropriate location.

2.  Be sure to run your tests to make sure you got it in the right location!

3.  Add and commit your changes.

Task 03
-------

Your final task this week will be to interpret the test results for a given
Python file in order to fix it so that it no longer produces errors.

Specifications
^^^^^^^^^^^^^^

1.  Run your tests locally with ``runtests.sh`` to see what errors are
    currently being reported for ``task_03.py``

2.  Interpret the test results in order to make corrections to ``task_03.py``
    and modify ``task_03.py`` accordingly.

3.  Keep running tests periodically to make sure you're moving in the right
    direction.

4.  Once you have no-more lint or unittest errors, commit your changes and
    submit.

Executing Tests
===============

Code must be functional and pass tests before it will be eligible for credit.

Linting
-------

Lint tests check your code for syntactic or stylistic errors To execute lint
tests against a specific file, simply open a terminal in the same directory as
your code repository and type:

.. code:: console

    $ pylint filename.py

Where ``filename.py`` is the name of the file you wish to lint test.

Unit Tests
----------

Unit tests check that your code performs the tested objectives. Unit tests
may be executed individually by opening a terminal in the same directory as
your code repository and typing:

.. code:: console

    $ nosetests tests/name_of_test.py

Where ``name_of_test.py`` is the name of the testfile found in the ``tests``
directory of your source code.

Running All Tests
-----------------

All tests may be run simultaneously by executing the ``runtests.sh`` script
from the root of your assignment repository. To execute all tests, open a
terminal in the same directory as your code repository and type:

.. code:: console

    $ sh runtests.sh

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Week Two.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
