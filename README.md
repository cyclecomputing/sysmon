sysmon component
================

This is a very simple example of a CycleServer component. It periodically runs 'ps'
on the local host and displays running processes. It only works if installed
on *nix host.

For more information, see the CycleServer Development Guide.


Requirements
------------

This component requires CycleServer 4.5 or higher. It demonstrates how to create basic 
user interface components and how to create a task that runs on a timer.

Building this component requires [gradle](http://gradle.org)

After installing gradle and CycleServer, you will need to configure gradle by running:
   
    $ cd cycle_server_install 
    $ sudo util/devel initialize
    

Building
--------

To build the component

    $ gradle build
    
To deploy the component, copy the built zip file to the `components/` subdirectory of your
CycleServer installation.

To view the Sysmon component in action, go to http://localhost:8080 (or wherever you have installed CycleServer)
and click the "Sysmon" dropdown. Choose either simple or advanced view.