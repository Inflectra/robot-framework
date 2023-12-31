# Robot Framework Integration for Spira
This repository contains the source code for the integration between Robot Framework and the Inflectra Spira platform. This plugin lets you execute Robot Framework test suites, and have the results automatically transmitted back to Spira. It can be run locally or as part of a CI/CD pipeline.

## About Robot Framework
[Robot Framework](https://robotframework.org/) is a generic open source automation framework. It can be used for test automation and robotic process automation (RPA).

Robot Framework is supported by Robot Framework Foundation. Many industry-leading companies use the tool in their software development.


## About Spira
Spira is the end-to-end platform from [Inflectra](https://www.inflectra.com) for product creation, from idea to release. Whether you are building software yourself, or deploying third-party systems, Spira is the integrated hub into which you can plug in specialized tools for the rest of the software development lifecycle. 

Spira comes in three flavors:
- [SpiraTest](https://www.inflectra.com/SpiraTest/), powerful requirements and test management
- [SpiraTeam](https://www.inflectra.com/SpiraTeam/), agile planning and test management for teams
- [SpiraPlan](https://www.inflectra.com/SpiraPlan/), enterprise planning and testing platform

## Installing the Integration
This section outlines how to install the Spira plugin for Robot Framework. It assumes that you already have a working installation of Spira v6.0 or later. If you have an earlier version of Spira you will need to upgrade to at least v6.0 before trying to use this plugin. You will also need to have Python (with pip) and Robot Framework installed.

To obtain the latest version of the plugin, simply run the following command:

`pip install spira-robot-framework`

This command will install the latest version of the plugin straight from the Python Package Index (PyPI). Once the Spira plugin is successfully installed, all you need to do is configure the plugin, annotate your Robot Framework test cases with Spira-specific tags, then you can begin testing!

## Using the Integration
TBD

## Have Questions or Need Assistance?
If you are an Inflectra customer, please contact our customer support at:
- Email: support@inflectra.com
- Help Desk: https://www.inflectra.com/Support/

Otherwise, please feel free to post a question on our public forums:
- [Test Case Integration Forum](https://www.inflectra.com/Support/Forum/integrations/unit-testing/List.aspx)

run the sample test
`robot tests.robot`
`python -m robot tests.robot`

run the Spira results integration to upload the results to Spira
`python robot_spira_integration.py`
`python robot_spira_integration.py Output.xml spira.cfg`