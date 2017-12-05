SpotCheck
=========

A simple CLI tool to check the spot prices of AWS EC2 instances. This
tool is utilized to check the recent prices of spot instances for
different instance type, so the user can make an informed decision on
the price to set for spot instances.

Background
----------

`Spot Instances <https://aws.amazon.com/ec2/spot/>`__ are a good
resource to use AWS EC2 instances for fairly cheap, and I am very
frugal. This tool allows me (and you, the user) to check historical
prices of spot instances to make an informed decision on the prices to
set when creating an EC2 instance.

Installation
------------

To install, use pip such that

.. code:: bash

    pip3 install --user spotcheck

Setup
-----

Since ``spotcheck`` uses boto3, you’ll have to setup the same way. You
can view the `docs
here <http://boto3.readthedocs.io/en/latest/guide/quickstart.html>`__

Usage
-----

To use, run

.. code:: bash

    spotcheck

and a series of questions will be prompted.

The results is of the form

::

    +------------------+-------------------+---------------+--------------+---------------+
    | Timestamp        | Availability Zone | Instance Type | Product Desc | Spot Price($) |
    +------------------+-------------------+---------------+--------------+---------------+
    | 2017-11-28 01:00 | ca-central-1a     | t2.micro      | Linux/UNIX   | 0.006100      |
    | 2017-11-28 01:00 | ca-central-1b     | t2.micro      | Linux/UNIX   | 0.006100      |
    | 2017-11-29 01:00 | ca-central-1a     | t2.micro      | Linux/UNIX   | 0.006100      |
            .                   .                   .               .           .
            .                   .                   .               .           .
            .                   .                   .               .           .
            .                   .                   .               .           .
    +------------------+-------------------+---------------+--------------+---------------+

Repeatable Usage
~~~~~~~~~~~~~~~~

If you don’t want to enter the CLI every time, you can run the CLI with
the options

::

    spotcheck --InstanceType=t2.micro --ProductDescription=Linux/UNIX --StartTime=$(date -d "3 days ago" +"%Y-%m-%d") --EndTime=$(date +"%Y-%m-%d")

Version
-------

-  **1.0.x**

   -  Fix Bugs

-  **1.0.0**

   -  First publish
