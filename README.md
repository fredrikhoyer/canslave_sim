# canslave_sim
Simple Canopen slave simulator

It takes an EDS file as argument and will answer with the
default values from this EDS file. If no default value exist
then 060A 0023 abort code (Resource not available) is returned.

The script assumes that the can interface is a linux socketCan
interface.

This scripts depends on the github project fredrikhoyer/canopen
branch canopenslave (or at least until these changes are pulled
into the canopen main project)
