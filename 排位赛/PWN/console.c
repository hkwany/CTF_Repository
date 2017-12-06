#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void welcome_info() {
    printf("--- Server Console ---\n\n");
}

void login() {
    int len = 20;
    char *token = malloc(len);
    char name[16] = {0};
    char password[16] = {0};
    
    printf("Token:");
    read(0, token, len);

    if (strlen(token) != 16) {
        exit(0);
    }

    printf("Login:");
    read(0, name, len);

    printf("Password:");
    read(0, password, len);

    if (0 != strcmp(name, password)) {
        exit(0);
    }

    write(1, "Welcome: ", strlen("Welcome: "));
    //write(1, name, len);
    printf("%s", name);
    write(1, "Token: ", strlen("Token: "));
    write(1, token, len);
}

void shell() {

    char cmd[16] = {0};

    while (1) {
        printf("shell> ");
        //scanf("%48s", cmd);
        read(0, cmd, 44);

        if (!strncmp(cmd, "exit", 4)) {
            break;

        } else if (!strncmp(cmd, "whoami", 6)) {
            printf("gamebox\n");

        } else if (!strncmp(cmd, "time", 4)) {
            time_t t = time(NULL);
            struct tm *p_tm = gmtime(&t);
            printf("current time: %s\n", asctime(p_tm));

        } else if (!strncmp(cmd, "status", 6)) {
            printf("service is running...\n");

        } else {
            printf("invalid command!\n");
        }
    }
}

int main() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);

    welcome_info();
    login();
    shell();
    return 0;
}
