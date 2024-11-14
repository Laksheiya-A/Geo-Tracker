GEO-TRACKER-HUB :

Geo Tracker is a Python-based web application designed for tracking and displaying the location of mobile numbers in real-time. Built with Django, OpenCage API, phonenumbers library, and integrated with OpenStreetMap and Leaflet.js, this tool allows users to input phone numbers and get their exact geographical location plotted on a map. The application also includes extra features for enhanced functionality and user experience, such as geofencing alerts, a distance calculator, and offline location sharing.



Features :

Real-time Mobile Location Tracking: Locate the exact position of a phone number and display it on a dynamic map.
Geofencing Alerts: Define geofenced areas to receive alerts if the tracked number enters or exits a specified region.
Distance Calculator: Calculate the distance between multiple tracked locations. (on-process)
Multi-Number Tracking: Track and monitor several phone numbers.
Offline Location Sharing: Allows sharing of the last known location when an internet connection is unavailable.


Screens :

Home: Introduction and overview of the Geo Tracker.
Tracker: Main tracking interface with a form to input phone numbers and initiate tracking.
History: Stores and displays past tracking sessions.
Login/Sign Up: User authentication for secured access.


Technologies Used :

Django: Backend framework for managing server-side logic and database operations.
Leaflet.js & OpenStreetMap: For rendering interactive maps to display real-time tracking data.
OpenCage API: To convert phone numbers into geographical coordinates.
Python Libraries:
phonenumbers: For parsing, formatting, and validating phone numbers.
geopy: For calculating distances and geolocation data.
requests: For handling API calls.


Usage :

Register or log in to access tracking features.
Go to the Tracker page, input the phone number, and click on Track.
The map will display the location, and history will be saved for future reference.
Use features like Distance Calculator and Geofencing Alerts for enhanced tracking.


Future Enhancements :
Enhanced Analytics Dashboard: For visualizing tracking history and patterns.
Advanced Notification System: Customizable notification triggers based on proximity and events.
