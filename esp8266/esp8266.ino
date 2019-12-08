#include <ESP8266WiFi.h>

const char* ssid = "father";
const char* password = "myfather";

const char* host = "192.168.12.1";

const int LED = 5; //D1

void setup()
{
  pinMode(LED, OUTPUT);
  digitalWrite(LED, LOW);
  Serial.begin(9600);
  Serial.printf("Connecting to %s ", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" connected");
}

WiFiClient client;
void loop()
{
  Serial.printf("\n[Connecting to %s ... ", host);
  if (client.connect(host, 8040))
  {
    Serial.println("connected");
    while(client.connected()){
      digitalWrite(LED, HIGH);
      //Serial.println("[Sending a message]");
      //client.print("hello");
      //delay(500);
      if (Serial.available() > 0)//判读是否串口有数据
      {
        String comdata = "";//缓存清零
        while (Serial.available() > 0)//循环串口是否有数据
        {
          comdata += char(Serial.read());//叠加数据到comdata
          delay(2);//延时等待响应
        }
        if (comdata.length() > 0)//如果comdata有数据
        {
          client.print(comdata);
        }
      }
    }
    digitalWrite(LED, LOW);
    client.stop();
    Serial.println("\n[Disconnected]");
  }
  else
  {
    Serial.println("connection failed!]");
    client.stop();
  }
}
