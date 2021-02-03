# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 09:05:16 2021

@author: mansu
"""

import sys
import numpy as np
sys.path.append("../../")
from pycircos import *
from Bio import SeqIO


if __name__ == "__main__":
    gbk = SeqIO.parse("Genome.gb","genbank")
    
    gcircle = Gcircle()
    
    
    gcircle.interspace = 0.0
    gcircle.read_locus(gbk, bottom=900, height=0, linewidth=0) 
    gcircle.set_locus()
    locus_names = list(gcircle.locus_dict.keys())
    
    
    #gcircle.add_locus("1", 1000, bottom=900, height=100) #name, length, bottom (0<=bottom<=1000), height (0<=bottom<=1000)
    gcircle.add_locus("ToCSVgp1", 400000, bottom=850, height=50, facecolor="#cc33ff")
    gcircle.add_locus("ToCSVgp2", 400000, bottom=850, height=50, facecolor="#6DCCDA")
    gcircle.add_locus("ToCSVgp3", 400000, bottom=850, height=50, facecolor="#ED97CA")
    gcircle.add_locus("ToCSVgp4", 400000, bottom=850, height=50, facecolor="#EDC948")
    gcircle.add_locus("ToCSVgp5", 400000, bottom=850, height=50, facecolor="#009900")
    gcircle.set_locus() #Create figure object
    
    gcircle.chord_plot(["ToCSVgp3", 4000, 4500, 950], ["ToCSVgp4", 500, 1000, 400], color="#F2BE2B")
    
    #gcircle.plot_features('NC_004675.1', bottom=800, height=50, facecolor="#ef6f6a", requirement=lambda x:x.location.strand==-1)
    #gcircle.plot_features('NC_004675.1', bottom=750, height=50, facecolor="#6388b4", requirement=lambda x:x.location.strand==1)
    
    
    gcircle.save()
