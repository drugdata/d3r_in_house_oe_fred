# Clear previous test results so we don't get mixed up
rm -r 1-get_challenge_data
rm -r 2-protein_prep
rm -r 3-ligand_prep
rm -r 4-docking
rm -r 5-pack_docking_results
rm -r 6-evaluate_docking_results



mkdir 1-get_challenge_data
getchallengedata.py --unpackdir 1-get_challenge_data --localdata celpp_weekXX_XXXX.tar.gz 

mkdir 2-protein_prep
python ../cookiecutter-custom-celpp-contestant/custom_celpp_contestant_protein_prep.py --challengedata 1-get_challenge_data/celpp_weekXX_XXXX --prepdir 2-protein_prep


mkdir 3-ligand_prep
python ../cookiecutter-custom-celpp-contestant/custom_celpp_contestant_ligand_prep.py --challengedata 1-get_challenge_data/celpp_weekXX_XXXX --prepdir 3-ligand_prep

mkdir 4-docking
python ../cookiecutter-custom-celpp-contestant/custom_celpp_contestant_dock.py --protsciprepdir 2-protein_prep --ligsciprepdir 3-ligand_prep --outdir  4-docking

mkdir 5-pack_docking_results
packdockingresults.py --dockdir 4-docking --packdir 5-pack_docking_results

mkdir 6-evaluate_docking_results
evaluate.py --dockdir 5-pack_docking_results --outdir 6-evaluate_docking_results --pdbdb mini_pdb
