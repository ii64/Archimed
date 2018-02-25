#!/usr/bin/python
# -*- coding: utf-8 -*-
#
__author__ = "Anysz"
__email__  = "anyoneelsegg@gmail.com"
__status__ = "Ready, send bug to the email"
#
# Free to use, all credits belong to me, Anysz.
# Feel free to report bugs :D
# Run:
#    python archimed.py 
#  or
#    python 
#    >>> from archimed import Archimed
#    >>> x = Archimed("1-5", range(8)).parse()
#
class Archimed(object):
    data_array = []
    datalist = []
    def __init__(self, logic, datalist):
        self.datalist = datalist
        self.logic = logic
    def parse(self):
        logics = self.parse_coma(self.logic)
        theresult = []
        for logic in logics:
            if ">" in logic:
                res01 = self.do_logic(logic)
                self.util_append(res01, theresult)
            elif "<" in logic:
                res02 = self.do_logic(logic)
                self.util_append(res02, theresult)
            elif "-" in logic:
                res03 = self.do_range(logic)
                self.util_append(res03, theresult)
            else:
                res04 = self.do_append(logic)
                self.util_append(res04, theresult)
        last_step = self.util_filter_doubled(theresult)
        last_step.sort()
        return last_step
    def util_filter_doubled(self, nestlists):
        # [ [2,3,4,5] , [2] , [3,4,7] ]
        dmp = []
        for reslist in nestlists:
            for item in reslist:
                if item not in dmp:
                    dmp.append(item)
                else:
                    pass
        
        return dmp
    def util_append(self, data, thelist):
        if data != None:
            thelist.append(data)
    def do_append(self, logic):
        try:
            number = int(logic)
            if number in self.datalist:
              return [number]
            else: return None
        except:
            return None
    def do_logic(self, logic):
        dmp = []
        for d in self.datalist: 
            state = eval("{0}{1}".format(d,logic))
            if state:
                dmp.append(d)
        return dmp
    def do_range(self, logic):
        # Get x-y : from x to y
        # Range have valid and not valid data. Ex 1-9 if 1-2-8
        rangedata = self.parse_minus(logic)
        if len(rangedata) == 1:
            return None
        elif len(rangedata) == 2:
            the_min = min( (int(rangedata[0])) , (int(rangedata[1])) )
            the_max = max( (int(rangedata[0])) , (int(rangedata[1])) )
            listrange = range(the_min, the_max+1)
            dmp = []
            for iter in self.datalist:
                if iter in set(listrange):
                    dmp.append(iter)
            return dmp
        elif len(rangedata) >= 3:
            return None
    def parse_minus(self,logic):
        logic = logic.split('-')
        return logic
    def parse_coma(self, logic):
        dat = logic.split(',')
        dmp = []
        for item in dat:
            if item != '':
                dmp.append(item)
        return dmp
        
if __name__=="__main__":
    the_list = range(1, 31)
    print "So i give you this list, {0}".format(str(the_list))
    print "Your job here is just type the logic of selection."
    print "Example: "
    print "  >8 mean item greater than 8"
    print "  <8 mean item lower than 8"
    print "  1-8 mean item select from 1 to 8"
    print "  8  mean 8 itself"
    print "Or just combine them like '1,2,3,4,6-8,>10' or whatever like you want"
    print "\nLive Demo."
    while 1:
        logics = raw_input("Type the logic\n>>> ")
        selection = archimed( logics , the_list )
        print selection.parse()
        print ""


