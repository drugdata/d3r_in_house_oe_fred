#!/usr/bin/env python


__author__ = 'j5wagner@ucsd.edu'

from d3r.celppade.custom_protein_prep import ProteinPrep


class no_prot_prep(ProteinPrep):
    """Abstract class defining methods for a custom docking solution
    for CELPP
    """
    ProteinPrep.OUTPUT_PROT_SUFFIX = '.pdb'
    def prepare_protein(self, protein_file, prepared_protein_file, info_dic={}):
        
        return super(no_prot_prep,self).prepare_protein(protein_file, prepared_protein_file, info_dic=info_dic)



    
if ("__main__") == (__name__):
    import logging
    import os
    import shutil
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-p", "--pdbdb", metavar = "PATH", help = "PDB DATABANK which we will dock into")
    parser.add_argument("-c", "--challengedata", metavar="PATH", help = "PATH to the unpacked challenge data package")
    parser.add_argument("-o", "--prepdir", metavar = "PATH", help = "PATH to the output directory")
    logger = logging.getLogger()
    logging.basicConfig( format  = '%(asctime)s: %(message)s', datefmt = '%m/%d/%y %I:%M:%S', filename = 'final.log', filemode = 'w', level = logging.INFO )
    opt = parser.parse_args()
    pdb_location = opt.pdbdb
    challenge_data_path = opt.challengedata
    prep_result_path = opt.prepdir

    #running under this dir
    abs_running_dir = os.getcwd()
    log_file_path = os.path.join(abs_running_dir, 'final.log')
    log_file_dest = os.path.join(os.path.abspath(prep_result_path), 'final.log')

    prot_prepper = no_prot_prep()
    prot_prepper.run_scientific_protein_prep(challenge_data_path, pdb_location, prep_result_path)

    #move the final log file to the result dir
    shutil.move(log_file_path, log_file_dest)
