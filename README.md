Sysmon component
================
Sysmon is a simple example of a CycleServer component. It periodically runs 'ps'
on the local host and displays running processes. It only works if installed
on *nix host.

For more information, see the CycleServer Development Guide.


Requirements
------------
Requires CycleServer 5.0 or higher, and must run on a host with the *nix 'ps' 
command on the path. It demonstrates how to create basic user interface 
components and how to create a task that runs on a timer.

Building this component requires [Gradle](http://gradle.org) 2.0 or higher and [Java](https://www.java.com) 1.7 or higher.

After installing Gradle and CycleServer, you will need to configure Gradle by running:
   
    $ cd /path/to/cycle_server 
    $ sudo ./util/devel initialize
    

Building and Deploying
----------------------
To build the component

    $ gradle clean build
    
To deploy the component, either copy the built zip file (located inside 
build/distributions) to the `components` subdirectory of your CycleServer 
installation, or run the following command, which will build and deploy
the zip file in one step:

    $ gradle clean deploy

To view the Sysmon component in action, go to http://localhost:8080 
(or wherever you have installed CycleServer) and click the "Sysmon" menu item. 
Choose either simple or advanced view.


Project Layout
--------------
This project follows the standard CycleServer component layout. Below is a partial
file/directory listing with descriptions:

- **build.gradle**: a standard gradle build file, with an "apply plugin" line to support component building/deployment.

- **src/main/component:** the root directory of the component. This contains a configuration file, "component.cfg" and a "plugins" directory, which contains any CycleServer plugins.

- **src/main/component/plugins/sysmon/init/ads:** initial records which will be saved to the data store when the component is loaded (note that this directory supports multiple file formats/extensions such as .txt, .json and .xml)

- **src/main/component/plugins/sysmon/monitor.py:** the "sysmon.monitor" timer plugin. Runs the process monitor and synchronizes the results with records of type "Sysmon.Process" in the data store.

- **src/main/component/plugins/sysmon/monitor.cfg:** the configuration file for the "sysmon.monitor" plugin. This tells CycleServer that this is both a timer plugin (Timer = true) and a URL handler (WebContent = dynamic). The URL handled maps to the plugin name by default (/sysmon/monitor in this case).

- **src/main/component/plugins/sysmon/process/simple:** a simple HTML template-based user interface for viewing process information.

- **src/main/component/plugins/sysmon/process/advanced:** a dynamic Javascript-based user interface for viewing process information.

- **src/main/python:** Python modules used by the component. These follow standard module conventions and will be interpreted using [Jython](http://www.jython.org/).

- **src/test/python:** Python unit tests and test resources. These will not be included in the built zip file.
