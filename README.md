## Stupendous Sloths Project Proposal - Water Level Monitoring System for Carwash

# Project Background 

The Water Level Monitoring System for Carwash is a project aimed at developing an efficient and sustainable solution for monitoring and managing water levels in carwash facilities. With the increasing concern for water conservation and environmental sustainability, it is crucial to implement effective measures to optimize water usage in various industries, including carwashes. This project proposes the implementation of a real-time monitoring system that tracks water levels and provides data-driven insights to enhance water management practices.

# Problem Statement

With the increasing demand for sustainable practices in business, carwash establishments must address the challenges of managing water resources effectively. To this end, we propose the implementation of a water level monitoring system that can provide real-time data on water usageto optimize water consumption, and contribute to environmental sustainability efforts. Our project aims to assist car wash businesses in their efforts to reduce costs, increase profitability, and enhance their reputation as responsible corporate citizens.


# System Architecture

The proposed system architecture involves using an ESP8266 microcontroller along with ultrasonic for water level monitoring. The data collected by the sensors is then transmitted to a cloud server using the MQTT protocol via CloudMQTT. The cloud server stores the data in an MYSQL database, which is accessible through an API built using Django Framework. Finally, the data is visualized through a dashboard created using Grafana, providing real-time insights into the water tank level. This system architecture offers a complete end-to-end solution for water level monitoring enabling businesses to make informed decisions about their water usage and optimize their carwash operations.

![Alt text](https://github.com/haziqfakhrie/Stage-6/blob/fda703dc1857baf682b8524acf2045ce4e81c795/Images/Software%20Engineering%20Project%20System%20Architecture%20(1).png)

# Sensor & Devices

## Protocol
The MQTT protocol using cloudMQTT is an ideal choice for IoT projects due to its lightweight and efficient communication model, as well as its ability to handle a large number of connected devices. CloudMQTT is a cloud-based broker service that provides a scalable and reliable platform for hosting MQTT-based IoT applications. It offers various plans that allow for customization of the number of connections, data transfer limits, and security features to suit the specific needs of the project. The MQTT protocol using cloudMQTT is a suitable choice for this IoT project due to its lightweight and efficient communication model, ability to handle a large number of connected devices, and support for secure and reliable communication. It offers a scalable and reliable platform for hosting MQTT-based IoT applications, making it ideal for a water tank monitoring system

## Sensors

**Ultrasonic Sensor**
The ultrasonic sensor is an ideal choice for water level monitoring in an IoT project for several reasons. Firstly, it is non-contact and can measure the water level accurately without coming into contact with the water. This feature eliminates the risk of sensor damage due to corrosion and fouling, which is common in contact sensors.

Secondly, ultrasonic sensors are easy to install and do not require complex calibration. They can be easily attached to the top of the water tank, making installation and maintenance a simple task. Next, ultrasonic sensors can measure the water level in real-time, allowing the system to send alerts and adjust water usage accordingly. This capability enables businesses to optimize water usage, prevent equipment damage, and contribute to environmental sustainability efforts.

Finally, the ultrasonic sensor is cost-effective and readily available, making it an accessible and practical solution for small and medium-sized businesses. When used in conjunction with the ESP8266 microcontroller, the ultrasonic sensor can provide accurate and reliable data to monitor water levels in real-time, making it a suitable choice for a water level monitoring IoT project.



## Device

**ESP8266 Microcontroller**
This proposed IoT project aims to monitor water levels in a carwash in order to optimize water usage and minimize costs. The water level will be monitored using an ultrasonic sensor connected to an ESP8266 microcontroller. Additionally, a proximity sensor will be used to count cars passing through the carwash, which will provide data on the water usage per car. The ESP8266 is chosen due to its low cost, high processing power, and Wi-Fi connectivity, making it a suitable choice for this project. By monitoring water levels and usage, the carwash can optimize water usage, reduce costs, and improve overall efficiency.

# Cloud Platform

**Ingest Data**
Firstly, DjangoREST framework allows for easy creation of RESTful APIs, which are ideal for IoT projects that require data ingestion from multiple sources. RESTful APIs are lightweight, flexible, and can handle a large number of requests, making them suitable for IoT projects that involve large volumes of data.

Secondly, DjangoREST framework is built on top of the Django web framework, which provides a robust set of tools for building web applications. This makes it easy to integrate the API with other components of the IoT project, such as the database and frontend components.

Thirdly, DjangoREST framework provides built-in support for serialization and deserialization of data in a variety of formats, such as JSON and XML. This makes it easy to handle data ingestion from different types of devices in an IoT project.

Additionally, DjangoREST framework provides a secure and scalable platform for ingesting data as an API, with support for authentication, authorization, and rate limiting. This ensures that the API is secure and can handle a large number of requests from multiple devices.

Overall, DjangoREST framework is a suitable choice for ingesting data as an API in IoT projects due to its flexibility, scalability, ease of use, and support for a variety of data formats. It provides a robust platform for building RESTful APIs that can handle large volumes of data and integrate easily with other components of the IoT project.

**Storage**
Firstly, InfluxDB is designed to handle time-series data, which is ideal for IoT projects that involve real-time data collection from sensors and other devices. It can efficiently store and manage large volumes of data with high write and read throughput, making it suitable for high-frequency data ingestion in IoT projects.

Secondly, InfluxDB has a flexible data model that allows for easy organization and querying of data. It uses a tag-based schema that can be used to add metadata to data points, making it easy to filter and query data based on different criteria.

Thirdly, InfluxDB provides a powerful query language, InfluxQL, which allows for complex data queries and aggregations. This makes it easy to analyze and visualize data from different sensors and devices in an IoT project.

Additionally, InfluxDB has built-in support for continuous queries and retention policies, which allow for data to be automatically aggregated and downsampled over time. This reduces the storage requirements for long-term data retention, making it more cost-effective for IoT projects that involve long-term data storage.

Overall, InfluxDB is a suitable choice for storing data in IoT projects due to its ability to handle large volumes of time-series data efficiently, flexible data model, powerful query language, and built-in support for data retention policies.


# Dashboard

Grafana is a suitable tool in IoT projects because it provides a real-time monitoring and visualization platform that can display data from various sources, including IoT devices. Its customizable dashboards and visualization options make it easy to track and analyze complex data in real-time, enabling users to quickly identify and troubleshoot issues. Grafana also supports alerting and dashboard sharing, making it a versatile and collaborative tool for IoT projects.


![Alt text](https://github.com/haziqfakhrie/Stage-6/blob/fda703dc1857baf682b8524acf2045ce4e81c795/Images/grafana%20dashboard.jpg)



