#include <stdio.h> 
#include <stdlib.h> 

int main() {
    char *ip_address = "192.168.0.12";  // server IP address
    char command[50];

    sprintf(command, "ping -c 1 %s > /dev/null", ip_address);
    int status = system(command);

    if (status == 0) {
        printf("device %s is online\n", ip_address);
    } else {
        printf("Alert: device %s is offline\n", ip_address);
    }

    return 0;
}