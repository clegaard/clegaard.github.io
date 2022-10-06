+++
title = "Implementing FMUs in Python"
date = 2022-10-06
draft = true
+++

The *Functional Mock-up Interface* (FMI) is a standard which defines a format for exchanging models between simulation tools.
In the context of FMI a model is referred to as a *Functional Mock-up Unit* (FMU).
If a tool states it supports FMI it can mean one of two things:
* It can import and execute a simulation of a FMU
* It can export FMUs that can be imported by a tool that supports FMI based simulation

We will refer to programs capable of doing the former as **importers** and programs capable of the latter as **exporters**


