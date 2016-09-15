#!/usr/bin/env python

__author__ = 'j5wagner@ucsd.edu'


from d3r.celppade.custom_dock import Dock

import commands

class oe_fred_dock(Dock):
    """Abstract class defining methods for a custom docking solution
    for CELPP
    """
    Dock.SCI_PREPPED_LIG_SUFFIX = '_prepared.sdf'
    Dock.SCI_PREPPED_PROT_SUFFIX = '_prepared.pdb'


    def lig_technical_prep(self, sci_prepped_lig):
        """Technical preparation" is the step immediate preceding
        docking. During this step, you should perform any file
        conversions or processing that are specific to your docking
        program.
        :param sci_prepped_lig: Scientifically prepared ligand file
        :returns: This implementation merely returns the value of
        `sci_prepped_lig` in a list
        """
        return super(oe_fred_dock,
                     self).lig_technical_prep(sci_prepped_lig)

    def receptor_technical_prep(self, sci_prepped_receptor, pocket_center):
        """Technical preparation" is the step immediately preceding
        docking. During this step, you should perform any file
        conversions or processing that are specific to your docking
        program.
        """

        # Finally, we return the filenames that will be needed in the
        # docking step. This list is passed to the dock() function as the
        # tech_prepped_receptor_list argument. Here we pass the docking
        # box file (for the docking) and the original scientifically
        # prepped ligand pdb, as that's the easiest way to return the
        # final receptor conformation.
 # For FRED, receptor_technical_prep takes a scientifically
        # prepared pdb file and creates a docking grid.

        receptor_prefix = sci_prepped_receptor.replace('.pdb','')
        docking_box_file = receptor_prefix + '.oeb.gz'

        # It helps to capture stdout and stderr from these steps for debugging
        stdout_file = receptor_prefix + '_docking_box_gen_stdout'
        stderr_file = receptor_prefix + '_docking_box_gen_stderr'

        # Technical prep for FRED consists of generating a docking box. The
        # box is defined by a .xyz file with two atoms specifying the
        # corners
        box_xyz_file = 'box.xyz'
        box_size = 30.
        corner_1 = (float(pocket_center[0]) - (box_size / 2),
                    float(pocket_center[1]) - (box_size / 2),
                    float(pocket_center[2]) - (box_size / 2))
        corner_2 = (float(pocket_center[0]) + (box_size / 2),
                    float(pocket_center[1]) + (box_size / 2),
                    float(pocket_center[2]) + (box_size / 2))
        box_xyz_text = '''2 
    CELPP auto-generated docking box 
     X %i %i %i 
     X %i %i %i 
    ''' %(corner_1[0], corner_1[1], corner_1[2], 
          corner_2[0], corner_2[1], corner_2[2])
        with open(box_xyz_file, 'wb') as of:
            of.write(box_xyz_text)

        # Run the box generation command
        cmd = 'receptor_setup -protein ' + sci_prepped_receptor + ' -box ' + box_xyz_file + ' -receptor ' + docking_box_file + ' 2> ' + stderr_file + ' 1> ' + stdout_file
        logging.info('Running tech prep command [%s]' %(cmd))
        commands.getoutput(cmd)

        # Check for success
        if not(os.path.exists(docking_box_file)):
            # This step will be run on all ligands, so it helps to be very descriptive about file locations
            abs_stdout_file = os.path.abspath(stdout_file)
            abs_stderr_file = os.path.abspath(stderr_file)
            logging.info('Docking box generation failed. See %s and %s for details' %(abs_stdout_file, abs_stderr_file))
            # CELPPade handles errors by returning False
            return False


        # Finally, we return the filenames that will be needed in the
        # docking step. This list is passed to the dock() function as the
        # tech_prepped_receptor_list argument. Here we pass the docking
        # box file (for the docking) and the original scientifically
        # prepped ligand pdb, as that's the easiest way to return the
        # final receptor conformation.
        return [docking_box_file, sci_prepped_receptor]

    def dock(self, tech_prepped_lig_list, tech_prepped_receptor_list, output_receptor_pdb, output_lig_mol):
        """# The dock step needs to run the actual docking algorithm. Its first two
        # arguments are the return values from the technical preparation
        # functions for the ligand and receptor. The outputs from this
        # step must be two files - a pdb with the filename specified in
        # the output_receptor_pdb argument, and a mol with the filename
        # specified in the output_ligand_mol argument.
        :returns: Always returns False
        """

        tech_prepped_grid = tech_prepped_receptor_list[0]
        sci_prepped_receptor = tech_prepped_receptor_list[1]
        receptor_prefix = os.path.basename(tech_prepped_grid).replace('.oeb.gz','')

        tech_prepped_lig = tech_prepped_lig_list[0]

        # FRED can only output .oeb and .sdf files. We'll have it output a
        # .sdf, then convert it to mol after FRED runs.
        docked_lig_sdf = receptor_prefix + '_docked.sdf'
        #docked_lig_mol = receptor_prefix + '_docked.mol'

        # It helps to capture stdout and stderr from these steps for debugging
        fred_stdout_file = receptor_prefix + '_fred_dock_stdout'
        fred_stderr_file = receptor_prefix + '_fred_dock_stderr'
        babel_stdout_file = receptor_prefix + '_babel_sdf2mol_stdout'
        babel_stderr_file = receptor_prefix + '_babel_sdf2mol_stderr'


        # Run the docking command
        dock_command = 'fred -receptor ' + tech_prepped_grid + ' -dbase ' + tech_prepped_lig + ' -docked_molecule_file ' + docked_lig_sdf + ' 2> ' + fred_stderr_file + ' 1> ' + fred_stdout_file
        logging.info('Running docking command [%s]' %(dock_command))
        commands.getoutput(dock_command)
        if not(os.path.isfile(docked_lig_sdf)):
            logging.info("Docking failed for protein %s and ligand %s" %(tech_prepped_grid, tech_prepped_lig))
            return False

        ## Create the required output files
        # First, the ligand needs to be converted from .sdf to .mol
        lig_convert_command = 'babel -isdf ' + docked_lig_sdf + ' -omol ' + output_lig_mol +  ' 2> ' + babel_stderr_file + ' 1> ' + babel_stdout_file
        commands.getoutput(lig_convert_command)
        if not(os.path.isfile(output_lig_mol)):
            logging.info("Babel conversion failed for docked ligand  %s" %(docked_lig_sdf))
            return False

        # And now we need to prepare the final receptor file. Because this
        # docking didn't modify the receptor, we will just copy the
        # original scientifically-prepped receptor pdb and give it the
        # appropriate name.
        shutil.copyfile(sci_prepped_receptor, output_receptor_pdb)

        # And do a final sanity check
        if not(os.path.isfile(output_receptor_pdb)):
            logging.info("File copy failed for receptor %s" %(output_receptor_pdb))
            return False

        return True


if ("__main__") == (__name__):
    import os
    import logging
    import shutil
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-l", "--ligsciprepdir", metavar="PATH", help = "PATH where we can find the scientific ligand prep output")
    parser.add_argument("-p", "--protsciprepdir", metavar="PATH", help = "PATH where we can find the scientific protein prep output")
    parser.add_argument("-o", "--outdir", metavar = "PATH", help = "PATH where we will put the docking output")
    # Leave option for custom logging config here
    logger = logging.getLogger()
    logging.basicConfig( format  = '%(asctime)s: %(message)s', datefmt = '%m/%d/%y %I:%M:%S', filename = 'final.log', filemode = 'w', level   = logging.INFO )
    opt = parser.parse_args()
    lig_sci_prep_dir = opt.ligsciprepdir
    prot_sci_prep_dir = opt.protsciprepdir
    dock_dir = opt.outdir
    #running under this dir
    abs_running_dir = os.getcwd()
    log_file_path = os.path.join(abs_running_dir, 'final.log')
    log_file_dest = os.path.join(os.path.abspath(dock_dir), 'final.log')
    docker = oe_fred_dock()
    docker.run_dock(prot_sci_prep_dir,
                    lig_sci_prep_dir,
                    dock_dir)
    #move the final log file to the result dir
    shutil.move(log_file_path, log_file_dest)
