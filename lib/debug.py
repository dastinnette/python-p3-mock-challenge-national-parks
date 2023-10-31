#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    v1 = Visitor("Emiley")
    v2 = Visitor("Adam")
    n1 = NationalPark("Zion")
    n2 = NationalPark("Arches")
    t1 = Trip(v1, n1, "September 1st", "October 1st")
    t1 = Trip(v1, n2, "April 1st", "May 1st")
    t1 = Trip(v2, n1, "January 1st", "February 1st")

    ipdb.set_trace()
