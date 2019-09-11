//in this program i was trying to control the brightness of an led using
//the output from reciver (flysky fs-i6)

int ch = 0;
int pwm = 0;
void setup() {
  // put your setup code here, to run once:
pinMode(5,INPUT);
pinMode(6,OUTPUT);
pinMode(7,OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
ch = pulseIn(5,HIGH,25000);
pwm = map(ch, 1000, 2000, 0, 255);
//brightness = int(ch/7.84) - 126;
Serial.println(pwm);
digitalWrite(7,LOW);
analogWrite(6,pwm);
//Serial.print("prog_running");
//Serial.println(ch);
delay(30);
}
