#!/usr/bin/env python

__author__ = 'j5wagner@ucsd.edu'

from d3r.celppade.custom_ligand_prep import LigandPrep

class omega_lig_prep(LigandPrep):
    """Abstract class defining methods for a custom ligand docking solution
    for CELPP
    """
    LigandPrep.OUTPUT_LIG_SUFFIX = '.sdf'

    def ligand_scientific_prep(self, lig_smi_file, out_lig_file, info_dic={}):
        """Ligand scientific preparation
        :param sci_prepped_lig: Scientifically prepared ligand file
        :returns: This implementation merely returns the value of
        `sci_prepped_lig` in a list
        """

        import commands
        lig_prefix = os.path.basename(lig_smi_file).replace('.smi','')

        # Perform conformer generation using omega
        omega_stdout_file = lig_prefix + '_omega_confgen_stdout'
        omega_stderr_file = lig_prefix + '_omega_confgen_stderr'
        omega_cmd = 'omega2 -flipper true -in ' + lig_smi_file + ' -out ' + out_lig_file + ' 2> ' + omega_stderr_file + ' 1> ' + omega_stdout_file
        logging.info('Running omega command: ' + omega_cmd)
        commands.getoutput(omega_cmd)


        if not(os.path.isfile(out_lig_file)):
            logging.info('Prepared ligand file %s does not exist. Assuming that prep failed.' %(out_lig_file))
            return False
        else:
            return True






if ("__main__") == (__name__):
    from argparse import ArgumentParser
    import os
    import logging 
    import shutil
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

    lig_prepper =  omega_lig_prep()
    lig_prepper.run_scientific_ligand_prep(challenge_data_path, pdb_location, prep_result_path)

    #move the final log file to the result dir
    shutil.move(log_file_path, log_file_dest)

