#include "tap_utils.h"
#include "sys_utils.h"
#include <stdbool.h>
#include <assert.h>
#include <stdint.h>
#include <arpa/inet.h>
#include <net/ethernet.h>
#include <pthread.h>

/**
 * VPort Instance
 */
struct vport_t
{
  int tapfd;                       // TAP device file descriptor, connected to linux kernel network stack
  int vport_sockfd;                // client socket, for communicating with VSwitch
  struct sockaddr_in vswitch_addr; // VSwitch address
};

void vport_init(struct vport_t *vport, const char *server_ip_str, int server_port);
void *forward_ether_data_to_vswitch(void *raw_vport);
