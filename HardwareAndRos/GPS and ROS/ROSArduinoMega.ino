#include <ros.h>
#include <sensor_msgs/NavSatFix.h>
#include <std_msgs/Float64.h>
#include <TinyGPSPlus.h>

static const uint32_t GPSBaud = 9600;

TinyGPSPlus gps;

ros::NodeHandle nh;

sensor_msgs::NavSatFix gps_msg;
ros::Publisher gpsData("/gps", &gps_msg);

void setup() {
  Serial1.begin(GPSBaud);
  nh.initNode();
  nh.advertise(gpsData);
}

void loop() {
  while (Serial1.available()) {
    if (gps.encode(Serial1.read())) {
      publishGPSData();
    }
  }

  nh.spinOnce();
}

void publishGPSData() {
  if (gps.location.isValid()) {
    gps_msg.latitude = gps.location.lat();
    gps_msg.longitude = gps.location.lng();
    gps_msg.altitude = gps.altitude.meters();
    gps_msg.header.stamp = nh.now();
    gpsData.publish(&gps_msg);
  }
}
