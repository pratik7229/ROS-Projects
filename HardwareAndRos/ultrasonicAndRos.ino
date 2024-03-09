#include <ros.h>
#include <std_msgs/Float32.h>
#define trigPin 2
#define echoPin 4
long duration;
int distance;ros::NodeHandle nh;
std_msgs::Float32 range_msg;
ros::Publisher range_pub("/range", &range_msg);
void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  nh.initNode();
  nh.advertise(range_pub);}
void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;
  range_msg.data = distance;
  range_pub.publish(&range_msg);
  nh.spinOnce();}
