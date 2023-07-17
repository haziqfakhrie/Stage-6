## Stupendous Sloths Project Proposal - Water Level Monitoring System for Carwash

# Project Background 

The Water Level Monitoring System for Carwash is a project aimed at developing an efficient and sustainable solution for monitoring and managing water levels in carwash facilities. With the increasing concern for water conservation and environmental sustainability, it is crucial to implement effective measures to optimize water usage in various industries, including carwashes. This project proposes the implementation of a real-time monitoring system that tracks water levels and provides data-driven insights to enhance water management practices.

# Problem Statement

With the increasing demand for sustainable practices in business, carwash establishments must address the challenges of managing water resources effectively. To this end, we propose the implementation of a water level monitoring system that can provide real-time data on water usageto optimize water consumption, and contribute to environmental sustainability efforts. Our project aims to assist car wash businesses in their efforts to reduce costs, increase profitability, and enhance their reputation as responsible corporate citizens.


# System Architecture

The proposed system architecture involves using an ESP8266 microcontroller along with ultrasonic for water level monitoring. The data collected by the sensors is then transmitted to a cloud server using the MQTT protocol via EMQX. The cloud server stores the data in an MYSQL database, which is accessible through an API built using Django Framework. Finally, the data is visualized through a dashboard created using Grafana, providing real-time insights into the water tank level. This system architecture offers a complete end-to-end solution for water level monitoring enabling businesses to make informed decisions about their water usage and optimize their carwash operations.

![Alt text](https://github.com/haziqfakhrie/Stage-6/blob/fda703dc1857baf682b8524acf2045ce4e81c795/Images/Software%20Engineering%20Project%20System%20Architecture%20(1).png)

# Sensor & Devices

## Protocol
Using the MQTT protocol with EMQ X as the MQTT broker is an excellent choice for IoT projects like a water tank monitoring system. MQTT's lightweight and efficient communication model makes it ideal for resource-constrained devices such as ESP32. EMQ X, an open-source MQTT broker, provides a reliable platform for hosting MQTT-based IoT applications. It offers scalability, high availability, and security features like TLS encryption and authentication, ensuring efficient and secure communication between the ESP32 devices and the server. With EMQ X, you can handle a large number of connected devices, facilitate real-time data exchange, and ensure reliable communication for your water tank monitoring system.

## Sensors

**Ultrasonic Sensor**
The ultrasonic sensor is an ideal choice for water level monitoring in an IoT project for several reasons. Firstly, it is non-contact and can measure the water level accurately without coming into contact with the water. This feature eliminates the risk of sensor damage due to corrosion and fouling, which is common in contact sensors.

Secondly, ultrasonic sensors are easy to install and do not require complex calibration. They can be easily attached to the top of the water tank, making installation and maintenance a simple task. Next, ultrasonic sensors can measure the water level in real-time, allowing the system to send alerts and adjust water usage accordingly. This capability enables businesses to optimize water usage, prevent equipment damage, and contribute to environmental sustainability efforts.

Finally, the ultrasonic sensor is cost-effective and readily available, making it an accessible and practical solution for small and medium-sized businesses. When used in conjunction with the ESP8266 microcontroller, the ultrasonic sensor can provide accurate and reliable data to monitor water levels in real-time, making it a suitable choice for a water level monitoring IoT project.



## Device

**ESP8266 Microcontroller**
This proposed IoT project aims to monitor water levels in a carwash in order to optimize water usage and minimize costs. The water level will be monitored using an ultrasonic sensor connected to an ESP8266 microcontroller. Additionally, a proximity sensor will be used to count cars passing through the carwash, which will provide data on the water usage per car. The ESP8266 is chosen due to its low cost, high processing power, and Wi-Fi connectivity, making it a suitable choice for this project. By monitoring water levels and usage, the carwash can optimize water usage, reduce costs, and improve overall efficiency.


**Ingest Data**
Firstly, DjangoREST framework allows for easy creation of RESTful APIs, which are ideal for IoT projects that require data ingestion from multiple sources. RESTful APIs are lightweight, flexible, and can handle a large number of requests, making them suitable for IoT projects that involve large volumes of data.

Secondly, DjangoREST framework is built on top of the Django web framework, which provides a robust set of tools for building web applications. This makes it easy to integrate the API with other components of the IoT project, such as the database and frontend components.

Thirdly, DjangoREST framework provides built-in support for serialization and deserialization of data in a variety of formats, such as JSON and XML. This makes it easy to handle data ingestion from different types of devices in an IoT project.

Additionally, DjangoREST framework provides a secure and scalable platform for ingesting data as an API, with support for authentication, authorization, and rate limiting. This ensures that the API is secure and can handle a large number of requests from multiple devices.

Overall, DjangoREST framework is a suitable choice for ingesting data as an API in IoT projects due to its flexibility, scalability, ease of use, and support for a variety of data formats. It provides a robust platform for building RESTful APIs that can handle large volumes of data and integrate easily with other components of the IoT project.

**Storage**

MySQL is a widely-used relational database management system that offers several advantages for storing IoT data. It provides a structured approach for efficient storage and management of structured IoT data. With its SQL query language, MySQL enables complex data operations like aggregations and filtering. The widespread adoption of MySQL ensures extensive community support and resources for troubleshooting. It scales well, handles large datasets, and maintains data integrity through ACID compliance. While it may not have specialized time-series capabilities, MySQL is a reliable choice for IoT projects that prioritize structured data management and relational capabilities.


# Dashboard

Grafana is a suitable tool in IoT projects because it provides a real-time monitoring and visualization platform that can display data from various sources, including IoT devices. Its customizable dashboards and visualization options make it easy to track and analyze complex data in real-time, enabling users to quickly identify and troubleshoot issues. Grafana also supports alerting and dashboard sharing, making it a versatile and collaborative tool for IoT projects.


![Alt text](https://github.com/haziqfakhrie/Stage-6/blob/fda703dc1857baf682b8524acf2045ce4e81c795/Images/grafana%20dashboard.jpg)

# Results

The Water Level Monitoring System for Carwash project was successful in achieving its objectives of providing a real-time monitoring solution for water levels in carwash facilities. The implemented system effectively tracked water levels using ultrasonic sensors connected to ESP8266 microcontrollers. The MQTT protocol, facilitated by EMQ X as the MQTT broker, ensured efficient and reliable communication between the devices and the cloud server. The data collected from the sensors was ingested into an MYSQL database using the DjangoREST framework.

The system successfully provided real-time insights into the water tank levels through a Grafana dashboard. This visualization platform enabled carwash businesses to monitor water usage and make data-driven decisions to optimize water consumption and improve their environmental sustainability efforts. The integration of proximity sensors to count cars passing through the carwash further enhanced the system's ability to track water usage per car, allowing businesses to analyze water consumption patterns and identify opportunities for improvement.

Overall, the Water Level Monitoring System for Carwash project demonstrated the successful implementation of a comprehensive IoT solution for monitoring and managing water levels in carwash facilities. By providing real-time data, the system empowered businesses to optimize water usage, reduce costs, and enhance their reputation as environmentally responsible entities.

# Project Replication

To get started with the Water Level Monitoring System for Carwash project, follow the steps outlined in the documentation provided. Make sure to set up the required hardware, configure the ESP8266 microcontrollers, establish the MQTT communication with EMQ X broker, configure the DjangoREST framework for data ingestion, set up the MySQL database for data storage, and create the Grafana dashboard for data visualization. The documentation provides detailed explanations and code snippets to assist you throughout the process.

**Hardware Requirements**

ESP8266 microcontrollers (quantity depends on the number of water tanks to monitor)
Ultrasonic sensors (HC-SR04 or similar)
Breadboards or PCBs for circuit connections
Jumper wires
Power supply (based on the requirements of your ESP8266 microcontrollers)

Ensure you have the following software installed:

**Software Requirements**

Arduino IDE for programming ESP8266 microcontrollers
Python 3.x for running the DjangoREST framework and connecting to the MySQL database
EMQ X broker for MQTT communication
MySQL database management system
Grafana for data visualization

**Hardware Setup**
1. Connect the ultrasonic sensors to the ESP8266 microcontrollers following the circuit diagrams provided in the Hardware directory of this repository.
2. Ensure proper power supply connections to the ESP8266 microcontrollers and ultrasonic sensors.
3. Repeat the hardware setup for each water tank you want to monitor.

**Software Setup**
1. Install the Arduino IDE and necessary libraries to program the ESP8266 microcontrollers. Refer to the documentation provided by Arduino for detailed instructions.
2. Set up the EMQ X broker and configure the MQTT settings. Follow the official EMQ X documentation for installation and configuration instructions.
3. Install Python 3.x and set up a virtual environment for running the DjangoREST framework.
4. Install the required Python packages by running the following command in the terminal:

```
pip install -r requirements.txt
```

1. Set up the MySQL database and create the necessary tables. Refer to the MySQL documentation for detailed instructions on installation and configuration.
2. Install Grafana and configure the data source to connect to the MySQL database. Refer to the Grafana documentation for detailed instructions on installation and configuration.

**Configuration**
1. Update the MQTT broker settings in the ESP8266 microcontroller code (Hardware/esp8266_code.ino) with the appropriate broker IP address, port, username, and password.
2. Configure the DjangoREST framework to connect to the MySQL database. Update the database settings in the settings.py file located in the Software/DjangoREST directory.
3. Configure Grafana to connect to the MySQL data source and set up the necessary dashboards for water level visualization.

**Usage**
1. Upload the ESP8266 microcontroller code (`Hardware/esp8266_code.ino`) to the respective microcontrollers using the Arduino IDE.
2. Start the EMQ X broker and ensure it is running and accessible.
3. Run the DjangoREST framework by executing the following command in the terminal within the `Software/DjangoREST` directory:

```
python manage.py runserver
```

4. Start the Grafana server and access it through the web browser.
5. Create a new data source in Grafana, connecting it to the MySQL database.
6. Create dashboards in Grafana to visualize the water level data.

## Disclaimer

Please note that while this project aims to provide a comprehensive solution for water level monitoring in carwash facilities, it is important to adapt and customize the system to meet your specific requirements and comply with local regulations. The developers of this project are not responsible for any issues, damages, or legal implications that may arise from the implementation and usage of the Water Level Monitoring System for Carwash.

Feel free to explore the source code, documentation, and adapt the Water Level Monitoring System for Carwash to your needs. Happy monitoring!
