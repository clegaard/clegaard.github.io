+++
title="Publications"
+++

For a list of my publications, see my [Google Scholar account](https://scholar.google.com/citations?user=NwJFl9cAAAAJ&hl=en).
Below is a list of publications sorted by year of publication.

# 2023

## Constructing Neural Network Based Models for Simulating Dynamical Systems

Dynamical systems see widespread use in natural sciences like physics, biology, and chemistry, as well as engineering disciplines such as circuit analysis, computational fluid dynamics, and control. For simple systems, the differential equations governing the dynamics can be derived by applying fundamental physical laws. However, for more complex systems, this approach becomes exceedingly difficult. Data-driven modeling is an alternative paradigm that seeks to learn an approximation of the dynamics of a system using observations of the true system. In recent years, there has been an increased interest in applying data-driven modeling techniques to solve a wide range of problems in physics and engineering. This article provides a survey of the different ways to construct models of dynamical systems using neural networks. In addition to the basic overview, we review the related literature and outline the most significant challenges from numerical simulations that this modeling paradigm must overcome. Based on the reviewed literature and identified challenges, we provide a discussion on promising research areas.

[Paper](https://doi.org/10.1145/3567591) |
[Code](https://github.com/clegaard/deep_learning_for_dynamical_systems)

![](survey_structure.svg)
![](ts.svg)
<!-- <figure>
    <img src={{get_url(path='publications/survey_structure.svg')}} alt="Survey structure" width=60%>
    <img src={{get_url(path='publications/ts.svg')}} alt="Time-stepper Model" width=60%>
</figure> -->
# 2021

## A Universal Mechanism for Implementing Functional Mock-up Units

Producing independent simulation units that can be used in a Functional Mock-Up Interface (FMI) setting is challenging. In some cases, a modelling tool may be available that provides the exact capabilities needed by exporting such units. However, there may be cases where existing tools are not suitable, or the cost is prohibitive, thus it may be necessary to implement a Functional Mock-up Unit (FMU) from scratch. Correctly implementing an FMU from scratch requires a deep technical understanding of the FMI specification and the technologies it is built upon. A consequence of FMI being a C-based standard is that an FMU must, generally, be implemented in C or a compiled language that offers a binary-compatible with C such as C++, Rust, or Fortran. In this paper we present UniFMU, a tool that makes it possible to implement FMUs in any language, by writing an adapter that can be plugged in to our modular approach. UniFMU also provides both a graphical user interface and command-line interface feature for generating new FMUs from a selection of programming languages. We expect our tool and approach to be useful for the simulation community both when porting simulators written in languages without FMI support, and when implementing or re-implementing such support.

[Paper](https://doi.org/10.5220/0010577601210129) |
[Code](https://github.com/INTO-CPS-Association/unifmu)

![](unifmu_rpc.png)
![](unifmu_model.png)

<!-- <figure>
    <img src={{get_url(path='publications/unifmu_rpc.png')}} width=49%>
    <img src={{get_url(path='publications/unifmu_model.png')}} width=30%>
<figure> -->


## Portable runtime environments for Python-based FMUs: Adding Docker support to UniFMU

Co-simulation is a means to combine and leverage the strengths of different modeling tools, environments and formalisms and has been applied successfully in various domains. 
The Functional Mock-Up Interface (FMI) is the most commonly used standard for co-simulation. 
In this paper we extend UniFMU, a tool that allows users to build Functional Mock-Up Units (FMUs) in virtually any programming language, to support execution within Docker. 
As a result the generated FMUs can be distributed in an environment containing all runtime dependencies. 
To describe the process of creating Dockerized FMUs using UniFMU, we show how to model and co-simulate a robotic arm and a controller using two Python-based FMUs.

[Paper](https://doi.org/10.3384/ecp21181419) | [Tool](https://github.com/INTO-CPS-Association/unifmu) | [Models](https://github.com/Daniella1/robot_unifmu)

![](unifmu_robot.png)
![](unifmu_results.png)
![](unifmu_docker.png)

<!-- <figure>
    <img src={{get_url(path='publications/unifmu_robot.png')}} height=70px>
    <img src={{get_url(path='publications/unifmu_results.png')}} height=70px>
    <img src={{get_url(path='publications/unifmu_docker.png')}} height=70px>
<figure> -->


## Coupling physical and machine learning models: case study of a single-family house
Future intelligent and integrated energy systems must have a high degree of flexibility and efficiency to ensure reliable and sustainable operation. Along with the rapid expansion of renewable energy, this degree of flexibility and efficiency can be achieved by overcoming the clear separation between different sectors and by increasing connectivity and the associated data availability through the integration of sensors and edge/fog computing. All of these developments drive the transition from towards so-called Cyber-Physical Energy Systems. The Cyber technologies (sensors, edge/fog computing, IoT networks, etc.) are able to monitor the physical systems, to enable communication between different subsystems and to control them. The emergence of Cyber-Physical Systems poses new challenges for traditional modelling and simulation approaches.


[Paper](https://doi.org/10.3384/ecp21181335) |
[Code](https://github.com/tug-cps/NextHyb2)


![](house_model.png)
![](house_prediction.png)
<!-- <figure>
    <img src={{get_url(path='publications/house_model.png')}} alt="schematic of house" width=49%>
    <img src={{get_url(path='publications/house_prediction.png')}} alt="time series prediction" width=49%>
<figure> -->

## Energy Prediction under Changed Demand Conditions: Robust Machine Learning Models and Input Feature Combinations
Deciding on a suitable algorithm for energy demand prediction in a building is non-trivial and depends on the availability of data. 
In this paper we compare four machine learning models, commonly found in the literature, in terms of their generalization performance and in terms of how using different sets of input features affects accuracy. 
This is tested on a data set where consumption patterns differ significantly between training and evaluation because of the Covid-19 pandemic. 
We provide a hands-on guide and supply a Python framework for building operators to adapt and use in their applications.

[Paper](https://doi.org/10.26868/25222708.2021.30806)

![](features_vs_accuracy.png)
<!-- <figure>
    <img src={{get_url(path='publications/features_vs_accuracy.png')}} alt="number of features and accuracy of model" width=70%>
<figure> -->

# 2020

## Rapid Prototyping of Self-Adaptive-Systems Using Python Functional Mockup Units
During the development of Cyber-Physical Systems (CPSs), it is crucial to enable efficient collaboration between different disciplines.
Co-simulation plays a key role in this by allowing the system as a whole to be simulated by composing simulations of its parts.
The ability to do this coupling relies on the models adhering to a well-defined interface.
The Functional Mockup Interface (FMI) defines this interface and the models that implemented it are called Functional Mockup Units (FMUs).
While a wealth of specialized simulation tools can generate FMUs, they are often commercial and do not support of complex software prototypes.
Rather than implement these as FMUs from scratch (FMI requires expertise in C), losing valuable time, the contribution presented in this paper is a tool that allows FMUs to be implemented rapidly in Python.
The advantages of this approach are demonstrated in an industrial use case, where a tracking simulator is implemented as an FMU.

[Paper](https://dl.acm.org/doi/abs/10.5555/3427510.3427532) | 
[Tool](https://github.com/INTO-CPS-Association/pyfmu) | 
[Models](https://github.com/INTO-CPS-Association/pyfmu/releases/tag/0.0.4)

![](robotti.png)
![](tracking_simulator.png)
<!-- <figure>
    <img src={{get_url(path='publications/robotti.png')}} alt="Agricultural robot" width=70%>
    <img src={{get_url(path='publications/tracking_simulator.png')}} alt="Tracking simulator" width=70%>
</figure> -->