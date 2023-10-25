#!/bin/bash

hidden1="Njg3NDc0NzA3MzNhMmYyZjc3Njk2ZTY0NmY3NzczNmM2OTc2NjU3NTcwNjQ2MTc0NjU3MjJlNjg3NDYyMmY0ODU0NDI3Yjcz"
hidden2="NzAzMDMwNmI3OTVmNzA2ODMxNzM2ODMxNmU2NzVmNzczMTc0Njg1ZjczNzAzMDMwNmI3OTVmNzM3MDcyMzMzNDY0NzM2ODMzMzM3NDczN2QyZjYxNzA3MDJlNzg2YzczNzgyZTY1Nzg2NQ=="

echo -n "$hidden1$hidden2" | base64 -d | xxd -r -p | grep -o 'HTB{[^}]*}'